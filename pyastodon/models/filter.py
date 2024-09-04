from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.filterKeyword import FilterKeywordModel
from pyastodon.models.filterStatus import FilterStatusModel
from pyastodon.models.enums.filterAction import FilterAction
from pyastodon.models.enums.filterContext import FilterContext


@dataclass()
class FilterModel(ObjectModel):
    id: str
    title: str
    context: FilterContext
    expires_at: Optional[str]
    filter_action: FilterAction
    keywords: list[FilterKeywordModel]
    statuses: list[FilterStatusModel]