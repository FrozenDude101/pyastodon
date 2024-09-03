from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class AdminCohortFrequency(EnumModel):
    DAY   = auto()
    MONTH = auto()