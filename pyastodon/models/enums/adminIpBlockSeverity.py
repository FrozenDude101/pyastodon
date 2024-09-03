from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class AdminIpBlockSeverity(EnumModel):
    SIGN_UP_REQUIRES_APPROVAL = auto()
    SIGN_UP_BLOCK = auto()
    NO_ACCESS = auto()