from dataclasses import dataclass

from pyastodon.models.model import JSONModel


@dataclass
class CustomEmoji(JSONModel):
    shortcode: str
    url: str
    static_url: str
    visible_in_picker: bool
    category: str