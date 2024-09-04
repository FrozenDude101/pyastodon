from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.adminCohortData import AdminCohortDataModel
from pyastodon.models.enums.adminCohortFrequency import AdminCohortFrequency


@dataclass()
class AdminCohortModel(ObjectModel):
    period: str
    frequency: AdminCohortFrequency
    data: list[AdminCohortDataModel]