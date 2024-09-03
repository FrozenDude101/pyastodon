from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class AdminDomainAllowModel(ObjectModel):
    id: str
    domain: str
    created_at: str