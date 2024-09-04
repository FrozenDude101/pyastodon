from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.instanceApiVersions import InstanceApiVersionsModel
from pyastodon.models.instanceConfiguration import InstanceConfigurationModel
from pyastodon.models.instanceContact import InstanceContactModel
from pyastodon.models.instanceIcon import InstanceIconModel
from pyastodon.models.instanceRegistrations import InstanceRegistrationsModel
from pyastodon.models.instanceThumbnail import InstanceThumbnailModel
from pyastodon.models.instanceUsage import InstanceUsageModel
from pyastodon.models.rule import RuleModel


@dataclass()
class InstanceModel(ObjectModel):
    domain: str
    title: str
    version: str
    source_url: str
    description: str
    usage: InstanceUsageModel
    thumbnail: InstanceThumbnailModel
    icon: list[InstanceIconModel]
    languages: list[str]
    configuration: InstanceConfigurationModel
    registrations: InstanceRegistrationsModel
    api_versions: InstanceApiVersionsModel
    contact: InstanceContactModel
    rules: list[RuleModel]