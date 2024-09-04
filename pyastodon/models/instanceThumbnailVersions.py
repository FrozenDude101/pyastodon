from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class InstanceThumbnailVersionsModel(ObjectModel):
    x1: Optional[str]
    x2: Optional[str]