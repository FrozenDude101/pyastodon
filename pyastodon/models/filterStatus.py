from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class FilterStatusModel(ObjectModel):
    id: str
    status_id: str