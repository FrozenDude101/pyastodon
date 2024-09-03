from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class AdminCanonicalEmailBlockModel(ObjectModel):
    id: str
    canonical_email_hash: str