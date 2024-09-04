from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class PreviewCardType(EnumModel):
    LINK  = auto()
    PHOTO = auto()
    VIDEO = auto()
    RICH  = auto()