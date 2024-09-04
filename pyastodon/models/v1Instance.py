from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.rule import RuleModel
from pyastodon.models.v1InstanceUrls import V1InstanceUrlsModel
from pyastodon.models.v1InstanceStats import V1InstanceStatsModel
from pyastodon.models.v1InstanceConfiguration import V1InstanceConfigurationModel


@dataclass()
class V1InstanceModel(ObjectModel):
    uri: str
    title: str
    short_description: str
    description: str
    email: str
    version: str
    urls: V1InstanceUrlsModel
    stats: V1InstanceStatsModel
    thumbnail: Optional[str]
    languages: list[str]
    registrations: bool
    approval_required: bool
    invites_enabled: bool
    configuration: V1InstanceConfigurationModel
    contact_account: Optional[AccountModel]
    rules: list[RuleModel]