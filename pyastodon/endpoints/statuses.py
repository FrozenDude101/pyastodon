from pyastodon.endpoints.base.endpoint import Endpoint
from pyastodon.models.status import StatusModel


class StatusesEndpoint(Endpoint):
    def __call__(self, domain: str,
        status: str
    ) -> StatusModel:
        json = {
            "status": status
        }
        return self.post(StatusModel, domain, "v1/statuses", json=json)

statuses = StatusesEndpoint()