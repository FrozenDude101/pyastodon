from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class TranslationAttachmentModel(ObjectModel):
    id: str
    description: str