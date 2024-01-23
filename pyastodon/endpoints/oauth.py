from typing import Literal, Optional

from pyastodon.endpoints.endpoint import post
from pyastodon.models import Scope, Token


def token(
    grant_type: Literal["authorization_code", "client_credentials"],
    client_id: str,
    client_secret: str,
    redirect_uris: str,
    code: Optional[str] = None,
    scope: Scope = Scope.READ
) -> Token:
    return Token.deserialize(post(
        "mastodon.social", "/oauth/token", token = False,
        grant_type = grant_type,
        code = code,
        client_id = client_id,
        client_secret = client_secret,
        redirect_uris = redirect_uris,
        scope = scope,
    ))