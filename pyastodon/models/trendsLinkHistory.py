from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class TrendsLinkHistoryModel(ObjectModel):
    day: str
    accounts: str
    uses: str