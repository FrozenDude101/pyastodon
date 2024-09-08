from typing import Any, Optional

import requests

from pyastodon.credentials import Credentials
from pyastodon.models.base.model import Model


class Endpoint():

    def _getAuth(self) -> str | None:
        return Credentials.getAuth()
    
    def get[T: Model](self, cls: type[T],
        domain:  str,
        route:   str,
        base:    str                      = "api",
        headers: Optional[dict[str, str]] = None,
        params:    Optional[dict[str, Any]] = None,
    ) -> T:
        if headers is None: 
            headers = {}

        url = f"https://{domain}/{base}/{route}"
        auth = self._getAuth()
        if auth is not None:
            headers["Authorization"] = auth
            
        response = requests.get(url, params=params, headers=headers)

        with open("out.txt", "w") as f:
            import json
            json.dump(response.json(), f)

        if response.status_code == 200:
            return cls.deserialize(response.json())
        
        if response.status_code == 429:
            print("Rate Limit Info:")
            print(response.headers["X-RateLimit-Limit"])
            print(response.headers["X-RateLimit-Remaining"])
            print(response.headers["X-RateLimit-Reset"])
            exit()

        raise Exception(response)
    
    def post[T: Model](self, cls: type[T],
        domain:  str,
        route:   str,
        base:    str                      = "api",
        headers: Optional[dict[str, str]] = None,
        json:    Optional[dict[str, Any]] = None,
    ) -> T:
        if headers is None: 
            headers = {}

        url = f"https://{domain}/{base}/{route}"

        auth = self._getAuth()
        if auth is not None:
            headers["Authorization"] = auth

        response = requests.post(url, headers=headers, json=json)
        if response.status_code == 200:
            return cls.deserialize(response.json())
        
        if response.status_code == 429:
            print("Rate Limit Info:")
            print(response.headers["X-RateLimit-Limit"])
            print(response.headers["X-RateLimit-Remaining"])
            print(response.headers["X-RateLimit-Reset"])
            exit()

        raise Exception(response)