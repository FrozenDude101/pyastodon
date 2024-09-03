from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass(kw_only=True)
class RuleModel(ObjectModel):
    id: str
    text: str
    hint: str