from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class StatusTagModel(ObjectModel):
    name: str
    url: str