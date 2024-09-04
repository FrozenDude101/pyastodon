from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.instanceThumbnailVersions import InstanceThumbnailVersionsModel


@dataclass()
class InstanceThumbnailModel(ObjectModel):
    url: str
    blurhash: Optional[str]
    versions: Optional[InstanceThumbnailVersionsModel]