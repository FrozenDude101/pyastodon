from typing import Self

import dotenv


class Credentials():

    SECRETS_FILE = ".secrets"
    clientId: str
    clientSecret: str
    accessToken: str | None = None
    authCode: str | None = None

    @classmethod
    def setClientId(cls, clientId: str) -> None:
        cls.clientId = clientId
        dotenv.set_key(cls.SECRETS_FILE, "clientId", clientId)

    @classmethod
    def setClientSecret(cls, clientSecret: str) -> None:
        cls.clientSecret = clientSecret
        dotenv.set_key(cls.SECRETS_FILE, "clientSecret", clientSecret)

    @classmethod
    def setAccessToken(cls, accessToken: str) -> None:
        cls.accessToken = accessToken
        dotenv.set_key(cls.SECRETS_FILE, "accessToken", accessToken)

    @classmethod
    def load(cls) -> None:
        secrets = dotenv.dotenv_values(cls.SECRETS_FILE)
        if (secrets["clientId"] is None
            or secrets["clientSecret"] is None
            or secrets["accessToken"] is None
        ):
            raise Exception()
        cls.setClientId(secrets["clientId"])
        cls.setClientSecret(secrets["clientSecret"])
        cls.setAccessToken(secrets["accessToken"])

    @classmethod
    def save(cls, clientId: str, clientSecret: str, accessToken: str) -> None:
        cls.setClientId(clientId)
        cls.setClientSecret(clientSecret)
        cls.setAccessToken(accessToken)
    
    @classmethod
    def getAuth(cls) -> str | None:
        if not cls.accessToken:
            return None
        return f"Bearer {cls.accessToken}"