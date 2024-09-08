from typing import Optional

from pyastodon.endpoints.base.endpoint import Endpoint
from pyastodon.models.credentialAccount import CredentialAccountModel


class AccountsEndpoint(Endpoint):

    def verify_credentials(self, domain: str) -> CredentialAccountModel:
        return self.get(CredentialAccountModel, domain, "v1/accounts/verify_credentials")

accounts = AccountsEndpoint()