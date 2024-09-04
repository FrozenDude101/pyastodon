from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class RelationshipSeveranceEventType(EnumModel):
    DOMAIN_BLOCK       = auto()
    USER_DOMAIN_BLOCK  = auto()
    ACCOUNT_SUSPENSION = auto()