from typing import Optional

from dataclasses import dataclass

from pyastodon.models.account import AccountModel


@dataclass()
class MutedAccountModel(AccountModel):
    mute_expires_at: Optional[str]