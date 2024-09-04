from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.status import StatusModel
from pyastodon.models.tag import TagModel


@dataclass()
class SearchModel(ObjectModel):
    accounts: list[AccountModel]
    statuses: list[StatusModel]
    hashtags: list[TagModel]