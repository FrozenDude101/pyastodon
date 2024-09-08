from typing import Optional, Any

import requests, webbrowser
import urllib.parse

from pyastodon.endpoints.base.endpoint import Endpoint

from pyastodon.models.base.model import Model
from pyastodon.models.flags.scope import Scope
from pyastodon.models.token import TokenModel


class OAuthEndpoint(Endpoint):

    def token(self, domain: str,
        grant_type: str, client_id: str, client_secret: str, redirect_uri: str,
        code: Optional[str] = None, scope: Optional[Scope] = None
    ) -> TokenModel:
        json = {
            "grant_type": grant_type,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "code": code,
            "scope": str(scope)
        }
        return self.post(TokenModel, domain, "oauth/token", base="", json=json)
    
    def authorize(self, domain: str,
        response_type: str, client_id: str, redirect_uri: str,
        scope: Optional[Scope], force_login: Optional[bool], lang: Optional[str],       
    ) -> str:
        base = ""
        route = "oauth/authorize"
        params = {
            "response_type": response_type,
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "scope": str(scope),
            "force_login": force_login,
            "lang": lang,
        }
        
        url = f"https://{domain}/{base}/{route}?"
        for key, value in params.items():
            if value is None:
                continue
            url += f"{urllib.parse.quote(key)}={urllib.parse.quote(value)}&"

        webbrowser.open(url, 1)
        return input("Auth Code >> ")

oauth = OAuthEndpoint()