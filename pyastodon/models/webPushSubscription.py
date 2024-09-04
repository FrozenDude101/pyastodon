from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.webPushSubscriptionAlerts import WebPushSubscriptionAlertsModel


@dataclass()
class WebPushSubscriptionModel(ObjectModel):
    id: str
    endpoint: str
    server_key: str
    alerts: WebPushSubscriptionAlertsModel