from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.status import StatusModel


@dataclass()
class ContextModel(ObjectModel):
    ancestors: list[StatusModel]
    descendants: list[StatusModel]