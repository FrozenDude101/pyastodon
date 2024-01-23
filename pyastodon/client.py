from __future__ import annotations
from typing import Optional

import dotenv

from pyastodon.endpoints.apps import apps
from pyastodon.endpoints.oauth import token
from pyastodon.models import Application, Scope


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
        secretsFile=".secrets",
    ) -> None:
        Client._instance = self

        self.host = host

        secrets = dotenv.dotenv_values(secretsFile)
        self._secretsFile = secretsFile
        if "CLIENT_SECRET" not in secrets:
            self._register(name, scopes, website)
        else:
            self.application = Application(
                name = name,
                website = website,
                client_id = secrets["CLIENT_ID"],
                client_secret = secrets["CLIENT_SECRET"],
            )

        self._getToken(scopes)
        

    def _register(self,
        name: str,
        scopes: Scope,
        website: Optional[str]
    ) -> None:
        self.application = apps(
            name,
            "urn:ietf:wg:oauth:2.0:oob",
            scopes,
            website,
        )

        if self.application.client_id is None:
            raise ValueError("Missing Application.client_id.")
        if self.application.client_secret is None:
            raise ValueError("Missing Application.client_id.")

        dotenv.set_key(".secrets", "CLIENT_ID", self.application.client_id)
        dotenv.set_key(".secrets", "CLIENT_SECRET", self.application.client_secret)

    def _getToken(self, scopes) -> None:
        if self.application.client_id is None:
            raise ValueError("Missing Application.client_id.")
        if self.application.client_secret is None:
            raise ValueError("Missing Application.client_id.")

        self.token = token(
            grant_type = "client_credentials",
            client_id = self.application.client_id,
            client_secret = self.application.client_secret,
            redirect_uris = "urn:ietf:wg:oauth:2.0:oob",
            scope = scopes
        )
