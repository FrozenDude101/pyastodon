from typing import Optional
from pyastodon.models.base.deprecated import Deprecated

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.mediaAttachmentType import MediaAttachmentType


@dataclass()
class MediaAttachmentModel(ObjectModel):
    id: str
    type: MediaAttachmentType
    url: str
    preview_url: Optional[str]
    remote_url: Optional[str]
    meta: dict
    description: Optional[str]
    blurhash: Optional[str]
    text_url: Deprecated[str]
