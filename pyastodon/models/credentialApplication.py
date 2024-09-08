from dataclasses import dataclass

from pyastodon.models.application import ApplicationModel


@dataclass()
class CredentialApplicationModel(ApplicationModel):
    client_id: str
    client_secret: str