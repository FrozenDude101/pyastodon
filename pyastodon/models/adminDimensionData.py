from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class AdminDimensionDataModel(ObjectModel):
    key: str
    human_key: str
    value: str
    unit: Optional[str]
    human_value: Optional[str]