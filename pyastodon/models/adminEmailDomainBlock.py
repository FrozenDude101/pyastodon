from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.adminEmailDomainBlockHistory import AdminEmailDomainBlockHistoryModel


@dataclass()
class AdminEmailDomainBlockModel(ObjectModel):
    id: str
    domain: str
    created_at: str
    history: list[AdminEmailDomainBlockHistoryModel]