from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class AppealState(EnumModel):
    APPROVED = auto()
    REJECTED = auto()
    PENDING  = auto()