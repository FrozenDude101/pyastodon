from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class MediaAttachmentType(EnumModel):
    UNKNOWN = auto()
    IMAGE   = auto()
    GIFV    = auto()
    VIDEO   = auto()
    AUDIO   = auto()