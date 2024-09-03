from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.announcementAccount import AnnouncementAccountModel
from pyastodon.models.announcementStatus import AnnouncementStatusModel
from pyastodon.models.customEmoji import CustomEmojiModel
from pyastodon.models.statusTag import StatusTagModel
from pyastodon.models.reaction import ReactionModel


@dataclass(kw_only=True)
class AnnouncementModel(ObjectModel):
    id: str
    content: str
    starts_at: Optional[str]
    ends_at: Optional[str]
    published: bool
    all_day: bool
    published_at: Optional[str]
    updated_at: Optional[str]
    read: Optional[str]
    mentions: list[AnnouncementAccountModel]
    statuses: list[AnnouncementStatusModel]
    tags: list[StatusTagModel]
    emojis: list[CustomEmojiModel]
    reactions: list[ReactionModel]