from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class WebPushSubscriptionAlertsModel(ObjectModel):
    mention: bool
    status: bool
    reblog: bool
    follow: bool
    follow_request: bool
    favourite: bool
    poll: bool
    update: bool
    admin_sign_up: bool
    admin_report: bool