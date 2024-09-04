from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class V1InstanceConfigurationAccountsModel(ObjectModel):
    max_featured_tags: int
    