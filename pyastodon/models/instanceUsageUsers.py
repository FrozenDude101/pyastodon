from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class InstanceUsageUsersModel(ObjectModel):
    active_month: int