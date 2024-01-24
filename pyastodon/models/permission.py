from __future__ import annotations

import enum

from pyastodon.models.model import StringModel


@enum.verify(enum.UNIQUE)
class Permission(StringModel, enum.IntFlag):

    NONE = 0

    ADMINISTRATOR        = enum.auto()
    DEVOPS               = enum.auto()
    VIEW_AUDIT_LOG       = enum.auto()
    VIEW_DASHBOARD       = enum.auto()
    MANAGE_REPORTS       = enum.auto()
    MANAGE_FEDERATION    = enum.auto()
    MANAGE_SETTINGS      = enum.auto()
    MANAGE_BLOCKS        = enum.auto()
    MANAGE_TAXONOMIES    = enum.auto()
    MANAGE_APPEALS       = enum.auto()
    MANAGE_USERS         = enum.auto()
    MANAGE_INVITES       = enum.auto()
    MANAGE_RULES         = enum.auto()
    MANAGE_ANNOUNCEMENTS = enum.auto()
    MANAGE_CUSTOM_EMOJIS = enum.auto()
    MANAGE_WEBHOOKS      = enum.auto()
    INVITE_USERS         = enum.auto()
    MANAGE_ROLES         = enum.auto()
    MANAGE_USER_ACCESS   = enum.auto()
    DELETE_USER_DATA     = enum.auto()

    ALL = (
        ADMINISTRATOR | DEVOPS | VIEW_AUDIT_LOG | VIEW_DASHBOARD
        | MANAGE_REPORTS | MANAGE_FEDERATION | MANAGE_SETTINGS | MANAGE_BLOCKS
        | MANAGE_TAXONOMIES | MANAGE_APPEALS | MANAGE_USERS | MANAGE_INVITES
        | MANAGE_RULES | MANAGE_ANNOUNCEMENTS | MANAGE_CUSTOM_EMOJIS
        | MANAGE_WEBHOOKS | INVITE_USERS | MANAGE_ROLES | MANAGE_USER_ACCESS
        | DELETE_USER_DATA
    )   

    @classmethod
    def fromString(cls, string: str) -> Permission:
        if string == "":
            return Permission.NONE
        return Permission(int(string))