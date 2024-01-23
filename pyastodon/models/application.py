from typing import Annotated, Optional

from dataclasses import dataclass

from pyastodon.models.model import DEPREACTED, JSONModel


@dataclass
class Application(JSONModel):
    name: str

    website: Optional[str]       = None
    client_id: Optional[str]     = None
    client_secret: Optional[str] = None
    vapid_key: Annotated[Optional[str], DEPREACTED] = None