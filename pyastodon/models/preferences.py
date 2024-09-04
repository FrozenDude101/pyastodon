from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.enums.preferencesReadingExpandMedia import PreferencesReadingExpandMedia
from pyastodon.models.enums.sourcePrivacy import SourcePrivacy


@dataclass()
class PreferencesModel(ObjectModel):
    posting_default_visibility: SourcePrivacy
    posting_default_sensitive: bool
    posting_default_language: Optional[str]
    reading_expand_media: PreferencesReadingExpandMedia
    reading_expand_spoilers: bool