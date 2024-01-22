from __future__ import annotations
from typing import Optional

from dataclasses import dataclass

from pyastodon.models.model import JSONModel
from pyastodon.models import CustomEmoji, Field


@dataclass
class Account(JSONModel):
    id: str
    username: str
    acct: str
    url: str
    display_name: str
    note: str
    avatar: str
    avatar_static: str
    header: str
    header_static: str
    locked: bool
    fields: list[Field]
    emojis: list[CustomEmoji]
    bot: bool
    group: bool
    created_at: str
    statuses_count: int
    followers_count: int
    following_count: int

    discoverable: Optional[bool]  = None
    noindex: Optional[bool]       = None
    moved: Optional[Account]      = None
    suspended: Optional[bool]     = None
    limited: Optional[bool]       = None
    last_status_at: Optional[str] = None
