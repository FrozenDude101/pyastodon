from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class ReactionModel(ObjectModel):
    name: str
    count: int
    me: Optional[bool]
    url: Optional[str]
    static_url: Optional[str]