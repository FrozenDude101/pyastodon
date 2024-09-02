from __future__ import annotations

from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.customEmoji import CustomEmoji
from pyastodon.models.field import Field


@dataclass(kw_only=True)
class Account(ObjectModel):
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
    discoverable: Optional[bool]
    noindex: Optional[bool]
    moved: Optional[Account]
    suspended: Optional[bool]
    limited: Optional[bool]
    created_at: str
    last_status_at: Optional[str]
    statuses_count: int
    followers_count: int
    following_count: int