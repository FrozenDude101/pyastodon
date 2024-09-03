from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class AdminReportCategory(EnumModel):
    SPAM     = auto()
    VIOLATON = auto()
    OTHER    = auto()