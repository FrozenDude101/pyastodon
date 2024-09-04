from __future__ import annotations

from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.application import ApplicationModel
from pyastodon.models.filterResult import FilterResultModel
from pyastodon.models.mediaAttachment import MediaAttachmentModel
from pyastodon.models.poll import PollModel
from pyastodon.models.previewCard import PreviewCardModel
from pyastodon.models.statusMention import StatusMentionModel
from pyastodon.models.statusTag import StatusTagModel
from pyastodon.models.customEmoji import CustomEmojiModel
from pyastodon.models.enums.statusVisibility import StatusVisibility


@dataclass()
class StatusModel(ObjectModel):
    id: str
    uri: str
    created_at: str
    account: AccountModel
    content: str
    visibility: StatusVisibility
    sensitive: bool
    spoiler_text: str
    media_attachments: list[MediaAttachmentModel]
    application: Optional[ApplicationModel] # TODO: Verify
    mentions: list[StatusMentionModel]
    tags: list[StatusTagModel]
    emojis: list[CustomEmojiModel]
    reblogs_count: int
    favourites_count: int
    replies_count: int
    url: Optional[str]
    in_reply_to_id: Optional[str]
    in_reply_to_account_id: Optional[str]
    reblog: Optional[StatusModel]
    poll: Optional[PollModel]
    card: Optional[PreviewCardModel]
    language: Optional[str]
    text: Optional[str]
    edited_at: Optional[str]
    favourited: Optional[bool]
    reblogged: Optional[bool]
    muted: Optional[bool]
    bookmarked: Optional[bool]
    pinned: Optional[bool]
    filtered: Optional[list[FilterResultModel]]
