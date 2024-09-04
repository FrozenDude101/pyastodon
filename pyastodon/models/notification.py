from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.accountWarning import AccountWarningModel
from pyastodon.models.relationshipSeveranceEvent import RelationshipSeveranceEventModel
from pyastodon.models.report import ReportModel
from pyastodon.models.status import StatusModel
from pyastodon.models.enums.notificationType import NotificationType


@dataclass()
class NotificationModel(ObjectModel):
    id: str
    type: NotificationType
    group_key: str
    created_at: str
    account: AccountModel
    status: Optional[StatusModel]
    report: Optional[ReportModel]
    relationship_severance_event: Optional[RelationshipSeveranceEventModel]
    moderation_warning: Optional[AccountWarningModel]