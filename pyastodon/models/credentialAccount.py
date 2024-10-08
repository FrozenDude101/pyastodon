from dataclasses import dataclass

from pyastodon.models.account import AccountModel
from pyastodon.models.role import RoleModel
from pyastodon.models.source import SourceModel


@dataclass()
class CredentialAccountModel(AccountModel):
    source: SourceModel
    role: RoleModel