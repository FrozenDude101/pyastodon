from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class InstanceIconModel(ObjectModel):
    src: str
    size: str