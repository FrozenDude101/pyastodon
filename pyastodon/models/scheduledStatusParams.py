from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.scheduledStatusParamsPoll import ScheduledStatusParamsPollModel
from pyastodon.models.enums.statusVisibility import StatusVisibility


@dataclass()
class ScheduledStatusParamsModel(ObjectModel):
    text: str
    poll: Optional[ScheduledStatusParamsPollModel]
    media_ids: Optional[list[str]]
    sensitive: Optional[bool]
    spoiler_text: Optional[str]
    visibility: StatusVisibility