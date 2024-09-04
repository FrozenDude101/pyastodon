from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel


@dataclass()
class ConversationModel(ObjectModel):
    id: str
    accounts: list[AccountModel]