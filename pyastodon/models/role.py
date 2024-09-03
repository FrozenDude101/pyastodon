from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.permissions import Permissions


@dataclass(kw_only=True)
class RoleModel(ObjectModel):
    id: str
    name: str
    color: str
    permissions: Permissions
    highlighted: bool