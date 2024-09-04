from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.instanceConfigurationUrls import InstanceConfigurationUrlsModel
from pyastodon.models.instanceConfigurationVapid import InstanceConfigurationVapidModel
from pyastodon.models.instanceConfigurationAccounts import InstanceConfigurationAccountsModel
from pyastodon.models.instanceConfigurationStatuses import InstanceConfigurationStatusesModel
from pyastodon.models.instanceConfigurationMediaAttachments import InstanceConfigurationMediaAttachmentsModel
from pyastodon.models.instanceConfigurationPolls import InstanceConfigurationPollsModel
from pyastodon.models.instanceConfigurationTranslation import InstanceConfigurationTranslationModel


@dataclass()
class InstanceConfigurationModel(ObjectModel):
    urls: InstanceConfigurationUrlsModel
    vapid: InstanceConfigurationVapidModel
    accounts: InstanceConfigurationAccountsModel
    statuses: InstanceConfigurationStatusesModel
    media_attachments: InstanceConfigurationMediaAttachmentsModel
    polls: InstanceConfigurationPollsModel
    translation: InstanceConfigurationTranslationModel