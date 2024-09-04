from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class ReportCategory(EnumModel):
    SPAM     = auto()
    VIOLATON = auto()
    OTHER    = auto()