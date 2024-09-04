from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class StatusEditPollOptionModel(ObjectModel):
    title: str