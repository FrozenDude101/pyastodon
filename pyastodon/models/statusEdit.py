from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.customEmoji import CustomEmojiModel
from pyastodon.models.mediaAttachment import MediaAttachmentModel
from pyastodon.models.statusEditPoll import StatusEditPollModel


@dataclass()
class StatusEditModel(ObjectModel):
    content: str
    spoiler_text: str
    sensitive: bool
    created_at: str
    account: AccountModel
    poll: Optional[StatusEditPollModel]
    media_attachments: list[MediaAttachmentModel]
    emojis: list[CustomEmojiModel]