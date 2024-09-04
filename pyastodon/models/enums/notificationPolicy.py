from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class NotificationPolicy(EnumModel):
    ACCEPT = auto()
    FILTER = auto()
    DROP   = auto()