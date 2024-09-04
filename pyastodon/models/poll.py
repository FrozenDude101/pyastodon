from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.customEmoji import CustomEmojiModel
from pyastodon.models.pollOption import PollOptionModel


@dataclass()
class PollModel(ObjectModel):
    id: str
    expires_at: Optional[str]
    expired: bool
    multiple: bool
    votes_count: int
    voters_count: Optional[int]
    options: list[PollOptionModel]
    emojis: list[CustomEmojiModel]
    voted: Optional[bool]
    own_votes: list[int]