from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class FilterAction(EnumModel):
    WARN = auto()
    HIDE = auto()