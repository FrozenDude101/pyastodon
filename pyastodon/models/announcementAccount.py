from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class AnnouncementAccountModel(ObjectModel):
    id: str
    username: str
    url: str
    acct: str