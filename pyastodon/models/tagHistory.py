from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class TagHistoryModel(ObjectModel):
    day: str
    uses: str
    accounts: str