from pyastodon.models.base.deprecated import Deprecated

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.enums.suggestionSource import SuggestionSource
from pyastodon.models.enums.suggestionSourceDeprecated import SuggestionSourceDeprecated


@dataclass()
class SuggestionModel(ObjectModel):
    source: Deprecated[SuggestionSourceDeprecated]
    sources: list[SuggestionSource]
    account: AccountModel