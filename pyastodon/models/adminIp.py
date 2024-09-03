from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class AdminIpModel(ObjectModel):
    ip: str
    used_at: str