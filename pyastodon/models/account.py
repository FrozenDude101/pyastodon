from __future__ import annotations

from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.customEmoji import CustomEmojiModel
from pyastodon.models.field import FieldModel


@dataclass()
class AccountModel(ObjectModel):
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
    fields: list[FieldModel]
    emojis: list[CustomEmojiModel]
    bot: bool
    group: bool
    discoverable: Optional[bool]
    noindex: Optional[bool]
    moved: Optional[AccountModel]
    suspended: Optional[bool]
    limited: Optional[bool]
    created_at: str
    last_status_at: Optional[str]
    statuses_count: int
    followers_count: int
    following_count: int