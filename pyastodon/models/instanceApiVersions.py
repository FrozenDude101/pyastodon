from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class InstanceApiVersionsModel(ObjectModel):
    mastodon: int