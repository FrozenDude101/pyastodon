from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class ScheduledStatusParamsPollModel(ObjectModel):
    options: list[str]
    expires_in: str
    multiple: Optional[bool]
    hide_totals: Optional[bool]