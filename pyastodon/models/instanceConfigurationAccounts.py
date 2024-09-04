from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class InstanceConfigurationAccountsModel(ObjectModel):
    max_featured_tags: int
    max_pinned_statuses: int