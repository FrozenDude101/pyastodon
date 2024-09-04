from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.appeal import AppealModel
from pyastodon.models.enums.accountWarningAction import AccountWarningAction


@dataclass()
class AccountWarningModel(ObjectModel):
    id: str
    action: AccountWarningAction
    text: str
    status_ids: list[str]
    target_account: AccountModel
    appeal: Optional[AppealModel]
    created_at: str