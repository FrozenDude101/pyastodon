from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.mediaAttachment import MediaAttachmentModel
from pyastodon.models.scheduledStatusParams import ScheduledStatusParamsModel


@dataclass()
class ScheduledStatusModel(ObjectModel):
    id: str
    scheduled_at: str
    params: ScheduledStatusParamsModel
    media_attachments: list[MediaAttachmentModel]