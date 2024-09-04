from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class InstanceConfigurationVapidModel(ObjectModel):
    public_key: str