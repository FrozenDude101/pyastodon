from typing import Optional
from pyastodon.models.base.deprecated import Deprecated

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class ApplicationModel(ObjectModel):
    id: str
    name: str
    website: Optional[str]
    redirect_uri: Optional[str]
    vapid_key: Deprecated[str]