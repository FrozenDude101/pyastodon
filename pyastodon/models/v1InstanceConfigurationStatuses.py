from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class V1InstanceConfigurationStatusesModel(ObjectModel):
    max_characters: int
    max_media_attachments: int
    characters_reserved_per_url: int