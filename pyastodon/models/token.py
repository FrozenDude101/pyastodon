from typing import Literal

from dataclasses import dataclass

from pyastodon.models.model import JSONModel
from pyastodon.models import Scope


@dataclass
class Token(JSONModel):
    access_token: str
    token_type: Literal["Bearer"]
    scope: Scope
    created_at: int

    def __str__(self) -> str:
        return f"{self.token_type} {self.access_token}"