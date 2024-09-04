from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.v1NotificationPolicySummary import V1NotificationPolicySummaryModel


@dataclass()
class V1NotificationPolicyModel(ObjectModel):
    filter_not_following: bool
    filter_not_followers: bool
    filter_new_accounts: bool
    filter_private_mentions: bool
    summary: V1NotificationPolicySummaryModel