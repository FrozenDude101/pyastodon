from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class MarkerModel(ObjectModel):
    last_read_id: str
    version: int
    updated_at: str