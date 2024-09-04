from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class AnnouncementStatusModel(ObjectModel):
    id: str
    url: str