from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.translationPollOption import TranslationPollOptionModel


@dataclass()
class TranslationPollModel(ObjectModel):
    id: str
    options: list[TranslationPollOptionModel]