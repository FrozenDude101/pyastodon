from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.flags.permissions import Permissions


@dataclass()
class RoleModel(ObjectModel):
    id: str
    name: str
    color: str
    permissions: Permissions
    highlighted: bool