from __future__ import annotations

from enum import auto

from pyastodon.models.base.strFlagModel import StrFlagModel


class Scope(StrFlagModel):
    NONE = 0

    READ_ACCOUNTS       = auto()
    READ_BLOCKS         = auto()
    READ_BOOKMARKS      = auto()
    READ_FAVOURITES     = auto()
    READ_FILTERS        = auto()
    READ_FOLLOWS        = auto()
    READ_LISTS          = auto()
    READ_MUTES          = auto()
    READ_NOTIFICATIONS  = auto()
    READ_SEARCH         = auto()
    READ_STATUSES       = auto()
    READ = (
        READ_ACCOUNTS | READ_BLOCKS | READ_BLOCKS | READ_BOOKMARKS
        | READ_FAVOURITES | READ_FILTERS | READ_FOLLOWS | READ_LISTS
        | READ_MUTES | READ_NOTIFICATIONS |READ_SEARCH | READ_STATUSES
    )

    WRITE_ACCOUNTS      = auto()
    WRITE_BLOCKS        = auto()
    WRITE_BOOKMARKS     = auto()
    WRITE_CONVERSATIONS = auto()
    WRITE_FAVOURITES    = auto()
    WRITE_FILTERS       = auto()
    WRITE_FOLLOWS       = auto()
    WRITE_LISTS         = auto()
    WRITE_MEDIA         = auto()
    WRITE_MUTES         = auto()
    WRITE_NOTIFCATIONS  = auto()
    WRITE_REPORTS       = auto()
    WRITE_STATUSES      = auto()
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

    PUSH = auto()

    ADMIN_READ_ACCOUNTS                 = auto()
    ADMIN_READ_REPORTS                  = auto()
    ADMIN_READ_DOMAIN_ALLOWS            = auto()
    ADMIN_READ_DOMAIN_BLOCKS            = auto()
    ADMIN_READ_IP_BLOCKS                = auto()
    ADMIN_READ_EMAIL_DOMAIN_BLOCKS      = auto()
    ADMIN_READ_CANONICAL_EMAIL_BLOCKS   = auto()
    ADMIN_READ = (
        ADMIN_READ_ACCOUNTS | ADMIN_READ_REPORTS | ADMIN_READ_DOMAIN_ALLOWS
        | ADMIN_READ_DOMAIN_BLOCKS | ADMIN_READ_IP_BLOCKS
        | ADMIN_READ_EMAIL_DOMAIN_BLOCKS | ADMIN_READ_CANONICAL_EMAIL_BLOCKS
    )
    
    ADMIN_WRITE_ACCOUNTS                = auto()
    ADMIN_WRITE_REPORTS                 = auto()
    ADMIN_WRITE_DOMAIN_ALLOWS           = auto()
    ADMIN_WRITE_DOMAIN_BLOCKS           = auto()
    ADMIN_WRITE_IP_BLOCKS               = auto()
    ADMIN_WRITE_EMAIL_DOMAIN_BLOCKS     = auto()
    ADMIN_WRITE_CANONICAL_EMAIL_BLOCKS  = auto()
    ADMIN_WRITE = (
        ADMIN_WRITE_ACCOUNTS | ADMIN_WRITE_REPORTS | ADMIN_WRITE_DOMAIN_ALLOWS
        | ADMIN_WRITE_DOMAIN_BLOCKS | ADMIN_WRITE_IP_BLOCKS
        | ADMIN_WRITE_EMAIL_DOMAIN_BLOCKS | ADMIN_WRITE_CANONICAL_EMAIL_BLOCKS
    )

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
            name = scope.name.lower().replace("_", ":", 2) #type: ignore
            strings.append(name)
            seen |= scope

        return " ".join(strings)