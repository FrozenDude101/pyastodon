from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class AdminDomainAllowModel(ObjectModel):
    id: str
    domain: str
    created_at: str