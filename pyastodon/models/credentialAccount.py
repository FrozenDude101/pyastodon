from dataclasses import dataclass

from pyastodon.models.account import Account
from pyastodon.models.role import Role
from pyastodon.models.source import Source


@dataclass(kw_only=True)
class CredentialAccount(Account):
    source: Source
    role: Role