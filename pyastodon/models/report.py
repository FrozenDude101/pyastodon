from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.enums.reportCategory import ReportCategory


@dataclass()
class ReportModel(ObjectModel):
    id: str
    action_taken: bool
    action_taken_at: Optional[str]
    category: ReportCategory
    comment: str
    forwarded: bool
    created_at: str
    status_ids: Optional[list[str]]
    rule_ids: Optional[list[str]]
    target_account: AccountModel