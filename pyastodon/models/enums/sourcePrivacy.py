from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class SourcePrivacy(EnumModel):
    PUBLIC   = auto()
    UNLISTED = auto()
    PRIVATE  = auto()
    DIRECT   = auto()