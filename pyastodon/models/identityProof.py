from pyastodon.models.base.deprecated import Deprecated

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class IdentityProofModel(ObjectModel):
    provider: Deprecated[str]
    provider_username: Deprecated[str]
    updated_at: Deprecated[str]
    proof_url: Deprecated[str]
    profile_url: Deprecated[str]