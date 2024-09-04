from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.v1FilterContext import V1FilterContext


@dataclass()
class V1FilterModel(ObjectModel):
    id: str
    phrase: str
    context: list[V1FilterContext]
    expires_at: Optional[str]
    irreversible: bool
    whole_word: bool