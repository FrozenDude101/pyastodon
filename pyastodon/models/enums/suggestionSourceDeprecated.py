from enum import auto

from pyastodon.models.base.enumModel import EnumModel


class SuggestionSourceDeprecated(EnumModel):
    STAFF             = auto()
    PAST_INTERACTIONS = auto()
    GLOBAL            = auto()