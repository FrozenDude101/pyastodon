from typing import Optional

from dataclasses import dataclass

from pyastodon.models.account import Account


@dataclass(kw_only=True)
class MutedAccount(Account):
    mute_expires_at: Optional[str]