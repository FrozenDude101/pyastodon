from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.filter import FilterModel


@dataclass()
class FilterResultModel(ObjectModel):
    filter: FilterModel
    keyword_matches: Optional[list[str]]
    status_matches: Optional[list[str]]