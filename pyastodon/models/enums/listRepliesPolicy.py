from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class ListRepliesPolicy(EnumModel):
    FOLLOWED = auto()
    LIST     = auto()
    NONE     = auto()