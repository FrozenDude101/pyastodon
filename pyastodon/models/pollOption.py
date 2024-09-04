from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class PollOptionModel(ObjectModel):
    title: str
    votes_count: Optional[int]