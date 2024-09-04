from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class TokenModel(ObjectModel):
    access_token: str
    token_type: str
    scope: str
    created_at: int