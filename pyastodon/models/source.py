from typing import Literal

from dataclasses import dataclass

from pyastodon.models.model import JSONModel
from pyastodon.models import Field


@dataclass
class Source(JSONModel):
    note: str
    fields: list[Field]
    privacy: Literal["public", "unlisted", "private", "direct"]
    sensitive: bool
    language: str
    follow_requests_count: int