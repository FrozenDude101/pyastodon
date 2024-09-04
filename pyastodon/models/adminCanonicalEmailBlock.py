from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class AdminCanonicalEmailBlockModel(ObjectModel):
    id: str
    canonical_email_hash: str