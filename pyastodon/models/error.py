from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class ErrorModel(ObjectModel):
    error: str
    error_description: Optional[str]