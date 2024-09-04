from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.listRepliesPolicy import ListRepliesPolicy


@dataclass()
class ListModel(ObjectModel):
    id: str
    title: str
    replies_policy: ListRepliesPolicy