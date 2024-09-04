from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class TranslationPollOptionModel(ObjectModel):
    title: str