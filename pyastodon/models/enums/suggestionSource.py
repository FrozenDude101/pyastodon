from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class SuggestionSource(EnumModel):
    FEATURED                     = auto()
    MOST_FOLLOWED                = auto()
    MOST_INTERACTIONS            = auto()
    SIMILAR_TO_RECENTLY_FOLLOWED = auto()
    FRIENDS_OF_FRIENDS           = auto()