from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class CustomEmojiModel(ObjectModel):
    shortcode: str
    url: str
    static_url: str
    visible_in_picker: str
    category: Optional[str]