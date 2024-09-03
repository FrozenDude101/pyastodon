from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class AdminMeasureDataModel(ObjectModel):
    date: str
    value: str