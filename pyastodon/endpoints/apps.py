from typing import Optional

import pyastodon
from pyastodon.endpoints.endpoint import get, post
from pyastodon.models import Application, Scope


def apps(
    client_name: str,
    redirect_uris: str,
    scopes = Scope.READ,
    website: Optional[str] = None,
) -> Application:
    client = pyastodon.Client.get()
    url = client.host
    return Application.deserialize(
        post(url, "/api/v1/apps", token = False,
            client_name = client_name,
            redirect_uris = redirect_uris,
            scopes = scopes,
            website = website,
        )
    )

def verify_credentials() -> Application:
    client = pyastodon.Client.get()
    url = client.host
    return Application.deserialize(
        get(url, "/api/v1/apps/verify_credentials")
    )