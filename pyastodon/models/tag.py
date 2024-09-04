from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.tagHistory import TagHistoryModel


@dataclass()
class TagModel(ObjectModel):
    name: str
    url: str
    history: list[TagHistoryModel]
    following: Optional[bool]