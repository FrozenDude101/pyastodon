import pyastodon
from pyastodon.endpoints.endpoint import get
from pyastodon.models import CredentialAccount


def verify_credentials() -> CredentialAccount:
    client = pyastodon.Client.get()
    url = client.host
    return CredentialAccount.deserialize(
        get(url, "/api/v1/accounts/verify_credentials")
    )