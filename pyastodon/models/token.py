from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.flags.scope import Scope


@dataclass()
class TokenModel(ObjectModel):
    access_token: str
    token_type: str
    scope: Scope
    created_at: int