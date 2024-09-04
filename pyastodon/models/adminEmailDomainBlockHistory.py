from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class AdminEmailDomainBlockHistoryModel(ObjectModel):
    day: str
    accounts: str
    uses: str