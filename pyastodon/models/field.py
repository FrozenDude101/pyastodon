from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class FieldModel(ObjectModel):
    name: str
    value: str
    verified_at: Optional[str]