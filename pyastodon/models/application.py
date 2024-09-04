from typing import Optional
from pyastodon.models.base.deprecated import Deprecated

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class ApplicationModel(ObjectModel):
    name: str
    website: Optional[str]
    client_id: Optional[str]
    client_secret: Optional[str]
    vapid_key: Deprecated[str]