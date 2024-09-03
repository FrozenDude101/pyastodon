from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class AnnouncementStatusModel(ObjectModel):
    id: str
    url: str