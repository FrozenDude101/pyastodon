from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class V1InstanceStatsModel(ObjectModel):
    user_count: int
    status_count: int
    domain_count: int