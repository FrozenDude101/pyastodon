from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import Account
from pyastodon.models.accountWarningAction import AccountWarningAction
from pyastodon.models.appeal import Appeal


@dataclass(kw_only=True)
class AccountWarning(ObjectModel):
    id: str
    action: AccountWarningAction
    text: str
    status_ids: list[str]
    target_account: Account
    appeal: Optional[Appeal]
    created_at: str