from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.instanceUsageUsers import InstanceUsageUsersModel


@dataclass()
class InstanceUsageModel(ObjectModel):
    users: InstanceUsageUsersModel