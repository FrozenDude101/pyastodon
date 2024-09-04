from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class V1InstanceConfigurationPollsModel(ObjectModel):
    max_options: int
    max_characters_per_option: int
    min_expiration: int
    max_expiration: int