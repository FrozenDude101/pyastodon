from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class AnnouncementAccountModel(ObjectModel):
    id: str
    username: str
    url: str
    acct: str