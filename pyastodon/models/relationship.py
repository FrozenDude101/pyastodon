from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class RelationshipModel(ObjectModel):
    id: str
    following: bool
    showing_reblogs: bool
    notifying: bool
    languages: list[str]
    followed_by: bool
    blocking: bool
    blocked_by: bool
    muting: bool
    muting_notifications: bool
    requested: bool
    requested_by: bool
    domain_blocking: bool
    endorsed: bool
    note: str