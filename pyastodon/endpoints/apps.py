from typing import Optional

from pyastodon.endpoints.base.endpoint import Endpoint
from pyastodon.models.flags.scope import Scope
from pyastodon.models.credentialApplication import CredentialApplicationModel


class AppsEndpoint(Endpoint):
    def __call__(self, domain: str,
        client_name: str, redirect_uris: str,
        scopes: Optional[Scope] = None, website: Optional[str] = None
    ) -> CredentialApplicationModel:
        json = {
            "client_name": client_name,
            "redirect_uris": redirect_uris,
            "scopes": str(scopes),
            "website": website,
        }
        response =  self.post(CredentialApplicationModel, domain, "v1/apps", json=json)
        return response

apps = AppsEndpoint()