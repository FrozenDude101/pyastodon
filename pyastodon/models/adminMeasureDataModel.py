from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class AdminMeasureDataModel(ObjectModel):
    date: str
    value: str