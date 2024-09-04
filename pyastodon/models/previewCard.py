from typing import Optional
from pyastodon.models.base.deprecated import Deprecated

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.previewCardAuthor import PreviewCardAuthorModel
from pyastodon.models.enums.previewCardType import PreviewCardType


@dataclass()
class PreviewCardModel(ObjectModel):
    url: str
    title: str
    description: str
    type: PreviewCardType
    authors: list[PreviewCardAuthorModel]
    author_name: Deprecated[str]
    author_url: Deprecated[str]
    provider_name: str
    provider_url: str
    html: str
    width: int
    height: int
    image: Optional[str]
    embed_url: str
    blurhash: Optional[str]