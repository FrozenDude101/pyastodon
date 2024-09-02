from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.base.deprecated import Deprecated


@dataclass(kw_only=True)
class ApplicationModel(ObjectModel):
    name: str
    website: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    vapid_key: Deprecated[str]