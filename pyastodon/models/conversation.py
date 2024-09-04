from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.status import StatusModel


@dataclass()
class ConversationModel(ObjectModel):
    id: str
    unread: bool
    accounts: list[AccountModel]
    last_status: Optional[StatusModel]