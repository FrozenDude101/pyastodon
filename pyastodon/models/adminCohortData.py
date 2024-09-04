from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class AdminCohortDataModel(ObjectModel):
    date: str
    rate: float
    value: int