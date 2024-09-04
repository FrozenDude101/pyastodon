from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class FilterKeywordModel(ObjectModel):
    id: str
    keyword: str
    whole_word: bool