from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.adminDimensionData import AdminDimensionDataModel


@dataclass(kw_only=True)
class AdminDimensionModel(ObjectModel):
    key: str
    data: list[AdminDimensionDataModel]