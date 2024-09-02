from typing import Literal

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.field import Field


@dataclass(kw_only=True)
class Source(ObjectModel):
    note: str
    fields: list[Field]
    privacy: Literal["public", "unlisted", "private", "direct"]
    sensitive: bool
    language: str
    follow_requests_count: str