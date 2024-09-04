from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class V1FilterContext(EnumModel):
    HOME          = auto()
    NOTIFICATIONS = auto()
    PUBLIC        = auto()
    THREAD        = auto()
    ACCOUNT       = auto()