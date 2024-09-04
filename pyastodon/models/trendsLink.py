from dataclasses import dataclass

from pyastodon.models.previewCard import PreviewCardModel
from pyastodon.models.trendsLinkHistory import TrendsLinkHistoryModel


@dataclass()
class TrendsLinkModel(PreviewCardModel):
    history: list[TrendsLinkHistoryModel]