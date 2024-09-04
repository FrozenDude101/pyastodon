from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.statusEditPollOption import StatusEditPollOptionModel


@dataclass()
class StatusEditPollModel(ObjectModel):
    options: list[StatusEditPollOptionModel]