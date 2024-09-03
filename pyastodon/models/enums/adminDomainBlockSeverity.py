from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class AdminDomainBlockSeverity(EnumModel):
    SILENCE = auto()
    SUSPEND = auto()
    NOOP    = auto()