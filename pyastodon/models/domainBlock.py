from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.domainBlockSeverity import DomainBlockSeverity


@dataclass()
class DomainBlockModel(ObjectModel):
    domain: str
    digest: str
    severity: DomainBlockSeverity
    comment: Optional[str]