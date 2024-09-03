from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.adminAccount import AdminAccountModel
from pyastodon.models.rule import RuleModel
from pyastodon.models.status import StatusModel
from pyastodon.models.enums.adminReportCategory import AdminReportCategory


@dataclass(kw_only=True)
class AdminReportModel(ObjectModel):
    id: str
    action_taken: bool
    action_taken_at: Optional[str]
    category: AdminReportCategory
    comment: str
    forwarded: bool
    created_at: str
    updated_at: str
    account: AdminAccountModel
    target_account: AdminAccountModel
    assigned_account: Optional[AdminAccountModel]
    action_taken_by_account: Optional[AdminAccountModel]
    statuses: list[StatusModel]
    rules: list[RuleModel]