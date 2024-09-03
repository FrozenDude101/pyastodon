from typing import Optional

from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel
from pyastodon.models.account import AccountModel
from pyastodon.models.adminIp import AdminIpModel
from pyastodon.models.role import RoleModel


@dataclass(kw_only=True)
class AdminAccountModel(ObjectModel):
    id: str
    username: str
    domain: Optional[str]
    created_at: str
    email: str
    ip: Optional[str]
    ips: list[AdminIpModel]
    locale: str
    invite_request: Optional[str]
    role: RoleModel
    confirmed: bool
    approved: bool
    disabled: bool
    silenced: bool
    suspended: bool
    account: AccountModel
    created_by_application_id: Optional[str]
    invited_by_application_id: Optional[str]
