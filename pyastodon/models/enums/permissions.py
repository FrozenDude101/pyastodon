from enum import auto

from pyastodon.models.base.flagModel import FlagModel


class Permissions(FlagModel):
    NONE                 = 0
    ADMINISTRATOR        = auto()
    DEVOPS               = auto()
    VIEW_AUDIT_LOG       = auto()
    VIEW_DASHBOARD       = auto()
    MANAGE_REPORTS       = auto()
    MANAGE_FEDERATION    = auto()
    MANAGE_SETTINGS      = auto()
    MANAGE_BLOCKS        = auto()
    MANAGE_TAXONOMIES    = auto()
    MANAGE_APPEALS       = auto()
    MANAGE_USERS         = auto()
    MANAGE_INVITES       = auto()
    MANAGE_RULES         = auto()
    MANAGE_ANNOUNCEMENTS = auto()
    MANAGE_CUSTOM_EMOJIS = auto()
    MANAGE_WEBHOOKS      = auto()
    INVITE_USERS         = auto()
    MANAGE_ROLES         = auto()
    MANAGE_USER_ACCESS   = auto()
    DELETE_USER_DATA     = auto()