from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class RuleModel(ObjectModel):
    id: str
    text: str
    hint: str