from typing import Optional

from pyastodon.endpoints.endpoint import get, post
from pyastodon.models import Application, Scope


def apps(
    client_name: str,
    redirect_uris: str,
    scopes = Scope.READ,
    website: Optional[str] = None,
) -> Application:
    return Application.deserialize(
        post("mastodon.social", "/api/v1/apps", token = False,
            client_name = client_name,
            redirect_uris = redirect_uris,
            scopes = scopes,
            website = website,
        )
    )

def verify_credentials() -> Application:
    return Application.deserialize(
        get("mastodon.social", "/api/v1/apps/verify_credentials")
    )