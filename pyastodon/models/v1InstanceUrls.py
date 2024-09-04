from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class V1InstanceUrlsModel(ObjectModel):
    streaming_api: str