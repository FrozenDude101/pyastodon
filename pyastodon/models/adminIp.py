from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class AdminIpModel(ObjectModel):
    ip: str
    used_at: str