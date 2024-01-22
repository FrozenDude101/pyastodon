from __future__ import annotations

import enum


@enum.verify(enum.UNIQUE)
class Scope(enum.Flag):

    NONE = 0

    READ_ACCOUNTS       = enum.auto()
    READ_BLOCKS         = enum.auto()
    READ_BOOKMARKS      = enum.auto()
    READ_FAVOURITES     = enum.auto()
    READ_FILTERS        = enum.auto()
    READ_FOLLOWS        = enum.auto()
    READ_LISTS          = enum.auto()
    READ_MUTES          = enum.auto()
    READ_NOTIFICATIONS  = enum.auto()
    READ_SEARCH         = enum.auto()
    READ_STATUSES       = enum.auto()
    READ = (
        READ_ACCOUNTS | READ_BLOCKS | READ_BLOCKS | READ_BOOKMARKS
        | READ_FAVOURITES | READ_FILTERS | READ_FOLLOWS | READ_LISTS
        | READ_MUTES | READ_NOTIFICATIONS |READ_SEARCH | READ_STATUSES
    )

    WRITE_ACCOUNTS      = enum.auto()
    WRITE_BLOCKS        = enum.auto()
    WRITE_BOOKMARKS     = enum.auto()
    WRITE_CONVERSATIONS = enum.auto()
    WRITE_FAVOURITES    = enum.auto()
    WRITE_FILTERS       = enum.auto()
    WRITE_FOLLOWS       = enum.auto()
    WRITE_LISTS         = enum.auto()
    WRITE_MEDIA         = enum.auto()
    WRITE_MUTES         = enum.auto()
    WRITE_NOTIFCATIONS  = enum.auto()
    WRITE_REPORTS       = enum.auto()
    WRITE_STATUSES      = enum.auto()
    WRITE = (
        WRITE_ACCOUNTS | WRITE_BLOCKS | WRITE_BOOKMARKS | WRITE_CONVERSATIONS
        | WRITE_FAVOURITES | WRITE_FILTERS | WRITE_FOLLOWS | WRITE_LISTS
        | WRITE_MEDIA | WRITE_MUTES | WRITE_NOTIFCATIONS | WRITE_REPORTS
        | WRITE_STATUSES
    )

    FOLLOW = (
        READ_BLOCKS | WRITE_BLOCKS | READ_FOLLOWS | WRITE_FOLLOWS | READ_MUTES
        | WRITE_MUTES
    )

    PUSH = enum.auto()

    ADMIN_READ_ACCOUNTS                 = enum.auto()
    ADMIN_READ_REPORTS                  = enum.auto()
    ADMIN_READ_DOMAIN_ALLOWS            = enum.auto()
    ADMIN_READ_DOMAIN_BLOCKS            = enum.auto()
    ADMIN_READ_IP_BLOCKS                = enum.auto()
    ADMIN_READ_EMAIL_DOMAIN_BLOCKS      = enum.auto()
    ADMIN_READ_CANONICAL_EMAIL_BLOCKS   = enum.auto()
    ADMIN_READ = (
        ADMIN_READ_ACCOUNTS | ADMIN_READ_REPORTS | ADMIN_READ_DOMAIN_ALLOWS
        | ADMIN_READ_DOMAIN_BLOCKS | ADMIN_READ_IP_BLOCKS
        | ADMIN_READ_EMAIL_DOMAIN_BLOCKS | ADMIN_READ_CANONICAL_EMAIL_BLOCKS
    )
    
    ADMIN_WRITE_ACCOUNTS                = enum.auto()
    ADMIN_WRITE_REPORTS                 = enum.auto()
    ADMIN_WRITE_DOMAIN_ALLOWS           = enum.auto()
    ADMIN_WRITE_DOMAIN_BLOCKS           = enum.auto()
    ADMIN_WRITE_IP_BLOCKS               = enum.auto()
    ADMIN_WRITE_EMAIL_DOMAIN_BLOCKS     = enum.auto()
    ADMIN_WRITE_CANONICAL_EMAIL_BLOCKS  = enum.auto()
    ADMIN_WRITE = (
        ADMIN_WRITE_ACCOUNTS | ADMIN_WRITE_REPORTS | ADMIN_WRITE_DOMAIN_ALLOWS
        | ADMIN_WRITE_DOMAIN_BLOCKS | ADMIN_WRITE_IP_BLOCKS
        | ADMIN_WRITE_EMAIL_DOMAIN_BLOCKS | ADMIN_WRITE_CANONICAL_EMAIL_BLOCKS
    )

    @staticmethod
    def fromString(string: str) -> Scope:
        if string == "":
            return Scope.READ
        
        scope = Scope.NONE
        for s in string.split(" "):
            s = s.upper().replace(":", "_", 2)
            scope |= Scope.__members__[s]

        return scope

    def __str__(self) -> str:
        if self is Scope.NONE:
            return "read"
        
        strings = []
        seen = Scope.NONE
        
        if Scope.READ in self:
            strings.append("read")
            seen |= Scope.READ
        
        if Scope.WRITE in self:
            strings.append("write")
            seen |= Scope.WRITE

        for scope in self:
            if scope in seen:
                continue
            name = scope.name.lower().replace("_", ":", 2)
            strings.append(name)
            seen |= scope

        return " ".join(strings)