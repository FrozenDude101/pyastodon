from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class ExtendedDescriptionModel(ObjectModel):
    updated_at: str
    content: str