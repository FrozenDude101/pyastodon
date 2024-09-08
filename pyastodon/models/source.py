from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.field import FieldModel
from pyastodon.models.enums.sourcePrivacy import SourcePrivacy


@dataclass()
class SourceModel(ObjectModel):
    note: str
    fields: list[FieldModel]
    privacy: SourcePrivacy
    sensitive: bool
    language: Optional[str]
    follow_requests_count: int
    # Unknown
    hide_collections: Optional[bool]
    discoverable: Optional[bool]
    indexable: Optional[bool]