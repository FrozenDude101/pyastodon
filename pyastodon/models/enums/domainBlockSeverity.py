from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class DomainBlockSeverity(EnumModel):
    SILENCE = auto()
    SUSPEND = auto()