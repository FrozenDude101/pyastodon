from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class StatusMentionModel(ObjectModel):
    id: str
    username: str
    url: str
    acct: str