from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class NotificationType(EnumModel):
    MENTION               = auto()
    STATUS                = auto()
    REBLOG                = auto()
    FOLLOW                = auto()
    FOLLOW_REQUEST        = auto()
    FAVOURITE             = auto()
    POLL                  = auto()
    UPDATE                = auto()
    ADMIN_SIGN_UP         = auto()
    ADMIN_REPORT          = auto()
    SEVERED_RELATIONSHIPS = auto()
    MODERATION_WARNING    = auto()