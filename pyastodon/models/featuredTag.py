from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class FeaturedTagModel(ObjectModel):
    id: str
    name: str
    url: str
    statuses_count: str
    last_status_at: str