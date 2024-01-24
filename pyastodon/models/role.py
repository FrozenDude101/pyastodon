from __future__ import annotations
from typing import Optional

from dataclasses import dataclass

from pyastodon.models.model import JSONModel
from pyastodon.models import Permission


@dataclass
class Role(JSONModel):
    id: int
    name: str
    color: str
    permissions: Permission
    highlighted: bool