from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.permissions import Permissions


@dataclass(kw_only=True)
class Role(ObjectModel):
    id: str
    name: str
    color: str
    permissions: Permissions
    highlighted: bool