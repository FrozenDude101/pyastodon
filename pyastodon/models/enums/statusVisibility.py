from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class StatusVisibility(EnumModel):
    PUBLIC   = auto()
    UNLISTED = auto()
    PRIVATE  = auto()
    DIRECT   = auto()