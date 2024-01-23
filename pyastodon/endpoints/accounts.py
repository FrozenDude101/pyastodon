import pyastodon
from pyastodon.endpoints.endpoint import get
from pyastodon.models import Account


def verify_credentials() -> Account:
    client = pyastodon.Client.get()
    url = client.host
    return Account.deserialize(
        get(url, "/api/v1/accounts/verify_credentials")
    )