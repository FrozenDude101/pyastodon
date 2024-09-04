from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel


@dataclass()
class InstanceContactModel(ObjectModel):
    email: str
    account: Optional[AccountModel]