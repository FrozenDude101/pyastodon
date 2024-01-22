from typing import Optional

from dataclasses import dataclass

from pyastodon.models.model import JSONModel


@dataclass
class Application(JSONModel):
    name: str
    vapid_key: str

    website: Optional[str]       = None
    client_id: Optional[str]     = None
    client_secret: Optional[str] = None