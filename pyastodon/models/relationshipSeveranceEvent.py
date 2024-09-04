from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.relationshipSeveranceEventType import RelationshipSeveranceEventType


@dataclass()
class RelationshipSeveranceEventModel(ObjectModel):
    id: str
    type: RelationshipSeveranceEventType
    purged: bool
    target_name: str
    relationships_count: Optional[int]
    created_at: str