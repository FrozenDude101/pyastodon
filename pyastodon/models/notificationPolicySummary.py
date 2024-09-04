from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class NotificationPolicySummaryModel(ObjectModel):
    pending_requests_count: int
    pending_notifications_count: int