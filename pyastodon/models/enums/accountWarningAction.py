from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class AccountWarningAction(EnumModel):
    NONE                       = auto()
    DISABLE                    = auto()
    MARK_STATUSES_AS_SENSITIVE = auto()
    DELETE_STATUSES            = auto()
    SENSITIVE                  = auto()
    SILENCE                    = auto()
    SUSPEND                    = auto()
