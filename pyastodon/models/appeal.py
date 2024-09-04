from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.appealState import AppealState


@dataclass()
class AppealModel(ObjectModel):
    text: str
    state: AppealState