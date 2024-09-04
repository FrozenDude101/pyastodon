from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.status import StatusModel


@dataclass()
class NotificationRequestModel(ObjectModel):
    id: str
    created_at: str
    updated_at: str
    account: AccountModel
    notifications_count: str
    last_status: Optional[StatusModel]