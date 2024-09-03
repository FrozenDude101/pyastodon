from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.adminMeasureDataModel import AdminMeasureDataModel


@dataclass(kw_only=True)
class AdminMeasureModel(ObjectModel):
    key: str
    unit: Optional[str]
    total: str
    human_value: Optional[str]
    previous_total: Optional[str]
    data: list[AdminMeasureDataModel]