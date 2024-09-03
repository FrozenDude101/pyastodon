from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class AdminCohortDataModel(ObjectModel):
    date: str
    rate: float
    value: int