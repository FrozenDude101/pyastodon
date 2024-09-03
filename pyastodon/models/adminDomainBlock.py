from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.adminDomainBlockSeverity import AdminDomainBlockSeverity


@dataclass(kw_only=True)
class AdminDomainBlock(ObjectModel):
    id: str
    domain: str
    digest: str
    created_at: str
    severity: AdminDomainBlockSeverity
    reject_media: str
    reject_reports: bool
    private_comment: Optional[str]
    public_comment: Optional[str]
    obfuscate: bool