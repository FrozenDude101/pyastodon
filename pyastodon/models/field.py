from typing import Optional

from dataclasses import dataclass

from pyastodon.models.model import JSONModel


@dataclass
class Field(JSONModel):
    name: str
    value: str

    verified_at: Optional[str] = None