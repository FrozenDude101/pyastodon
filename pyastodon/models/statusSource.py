from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class StatusSourceModel(ObjectModel):
    id: str
    text: str
    spoiler_text: str