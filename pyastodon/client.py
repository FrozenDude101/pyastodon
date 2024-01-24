from __future__ import annotations
from typing import Optional

import dotenv
import logging

from pyastodon.endpoints import accounts, apps, oauth
from pyastodon.models import Application, Scope, Token
import pyastodon.logging as pLogging


class Client():
    _instance: Client

    @staticmethod
    def get() -> Client:
        return Client._instance

    def __init__(self,
        host: str,
        name: str,
        scopes = Scope.READ,
        website: Optional[str] = None,
        logger: Optional[str] = None,
        logLevel: logging._Level = logging.INFO,
        secretsFile=".secrets",
    ) -> None:
        Client._instance = self

        self.host = host

        if logger is None:
            pLogging.setupLogging(logLevel)
        self._logger = pLogging.getLogger("client")

        self._secretsFile = secretsFile
        clientId = dotenv.get_key(self._secretsFile, "CLIENT_ID")
        clientSecret = dotenv.get_key(self._secretsFile, "CLIENT_SECRET")
        if clientId is None or clientSecret is None:
            self.application = self._register(name, scopes, website)
        else:
            self.application = Application(
                name = name,
                website = website,
                client_id = clientId,
                client_secret = clientSecret,
            )

        accessToken = dotenv.get_key(self._secretsFile, "ACCESS_TOKEN") 
        if accessToken is None:
            self.token = self._getToken(scopes)
        else:
            self.token = Token(
                access_token = accessToken,
                token_type = "Bearer",
                scope = scopes,
                created_at = -1,
            )

    def _register(self,
        name: str,
        scopes: Scope,
        website: Optional[str]
    ) -> Application:
        application = apps.apps(
            name,
            "urn:ietf:wg:oauth:2.0:oob",
            scopes,
            website,
        )

        if application.client_id is None:
            raise ValueError("Missing Application.client_id.")
        if application.client_secret is None:
            raise ValueError("Missing Application.client_id.")

        dotenv.set_key(".secrets", "CLIENT_ID", application.client_id)
        dotenv.set_key(".secrets", "CLIENT_SECRET", application.client_secret)
       
        return application

    def _getToken(self, scopes) -> Token:
        if self.application.client_id is None:
            raise ValueError("Missing Application.client_id.")
        if self.application.client_secret is None:
            raise ValueError("Missing Application.client_id.")

        token = oauth.token(
            grant_type = "client_credentials",
            client_id = self.application.client_id,
            client_secret = self.application.client_secret,
            redirect_uri = "urn:ietf:wg:oauth:2.0:oob",
            scope = scopes,
        )
        dotenv.set_key(self._secretsFile, "ACCESS_TOKEN", token.access_token)
        return token
    
    def _upgradeToken(self, code: str) -> Token:
        if self.application.client_id is None:
            raise ValueError("Missing Application.client_id.")
        if self.application.client_secret is None:
            raise ValueError("Missing Application.client_id.")

        token = oauth.token(
            grant_type = "authorization_code",
            code = code,
            client_id = self.application.client_id,
            client_secret = self.application.client_secret,
            redirect_uri = "urn:ietf:wg:oauth:2.0:oob",
            scope = self.token.scope,
        )
        dotenv.set_key(self._secretsFile, "ACCESS_TOKEN", token.access_token)
        return token


    def upgrade(self) -> None:
        try:
            self.account = accounts.verify_credentials()
        except:
            url = "".join([
                f"https://{self.host}/oauth/authorize/",
                f"?client_id={self.application.client_id}",
                f"&scope={self.token.scope}".replace(" ", "%20"),
                "&redirect_uri=urn:ietf:wg:oauth:2.0:oob",
                "&response_type=code",
            ])
            print(f"Please go to this url to verify the app:\n{url}")
            code = input("Please input the given authorization code:\n")

            self.token = self._upgradeToken(code)
            self.account = accounts.verify_credentials()