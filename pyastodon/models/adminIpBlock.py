from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.adminIpBlockSeverity import AdminIpBlockSeverity


@dataclass(kw_only=True)
class AdminIpBlockModel(ObjectModel):
    id: str
    ip: str
    severity: AdminIpBlockSeverity
    comment: str
    created_at: str
    expires_at: Optional[str]