from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class InstanceRegistrationsModel(ObjectModel):
    enabled: bool
    approval_required: bool
    message: Optional[str]