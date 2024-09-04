from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.translationAttachment import TranslationAttachmentModel
from pyastodon.models.translationPoll import TranslationPollModel


@dataclass()
class TranslationModel(ObjectModel):
    content: str
    spoiler_text: str
    poll: Optional[TranslationPollModel]
    media_attachments: list[TranslationAttachmentModel]
    detected_source_language: str
    provider: str