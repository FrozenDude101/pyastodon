from __future__ import annotations

import webbrowser

from pyastodon.credentials import Credentials

from pyastodon.endpoints.accounts import accounts
from pyastodon.endpoints.apps import apps
from pyastodon.endpoints.oauth import oauth
from pyastodon.endpoints.statuses import statuses
from pyastodon.models.flags.scope import Scope


class Bot:

    def __init__(self, domain: str, scope: Scope) -> None:
        self.domain = domain
        self.scope = scope

        try:
            Credentials.load()
        except:
            app = apps(domain, "pyastodon", "urn:ietf:wg:oauth:2.0:oob", scopes=self.scope)
            Credentials.setClientId(app.client_id)
            Credentials.setClientSecret(app.client_secret)
            token = oauth.token(
                self.domain, "client_credentials", Credentials.clientId,
                Credentials.clientSecret, "urn:ietf:wg:oauth:2.0:oob", scope=self.scope
            )
            Credentials.setAccessToken(token.access_token)

    def logIn(self) -> None:
        try:
            accounts.verify_credentials(self.domain)
        except Exception as e:
            authCode = oauth.authorize(
                self.domain, "code", Credentials.clientId, "urn:ietf:wg:oauth:2.0:oob",
                self.scope, None, None,
            )
            token = oauth.token(
                self.domain, "authorization_code", Credentials.clientId,
                Credentials.clientSecret, "urn:ietf:wg:oauth:2.0:oob",
                code=authCode, scope=self.scope
            )
            Credentials.setAccessToken(token.access_token)

    def toot(self, status: str) -> None:
        statuses(self.domain, status)