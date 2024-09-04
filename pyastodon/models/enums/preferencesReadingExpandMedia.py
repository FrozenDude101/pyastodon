from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class PreferencesReadingExpandMedia(EnumModel):
    DEFAULT  = auto()
    SHOW_ALL = auto()
    HIDE_ALL = auto()