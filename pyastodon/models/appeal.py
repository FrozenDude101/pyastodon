from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.appealState import AppealState


@dataclass(kw_only=True)
class Appeal(ObjectModel):
    text: str
    state: AppealState