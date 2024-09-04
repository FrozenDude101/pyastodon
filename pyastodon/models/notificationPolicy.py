from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.notificationPolicySummary import NotificationPolicySummaryModel
from pyastodon.models.enums.notificationPolicy import NotificationPolicy


@dataclass()
class NotificationPolicyModel(ObjectModel):
    for_not_following: NotificationPolicy
    for_not_followers: NotificationPolicy
    for_new_accounts: NotificationPolicy
    for_private_mentions: NotificationPolicy
    for_limited_accounts: NotificationPolicy
    summary: NotificationPolicySummaryModel