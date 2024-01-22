from tests.models import ModelTestCase
from pyastodon.models import Scope, Token


class TestTokenModel(ModelTestCase):
    
    def testDeserialize(self) -> None:
        INPUT = """{
            "access_token": "ZA-Yj3aBD8U8Cm7lKUp-lm9O9BmDgdhHzDeqsY8tlL0",
            "token_type": "Bearer",
            "scope": "read write follow push",
            "created_at": 1573979017
        }"""
        EXPECTED_RESULT = Token(
            access_token = "ZA-Yj3aBD8U8Cm7lKUp-lm9O9BmDgdhHzDeqsY8tlL0",
            token_type = "Bearer",
            scope = Scope.READ | Scope.WRITE | Scope.PUSH,
            created_at = 1573979017
        )

        result = Token.deserialize(INPUT)
        self.assertTokenEqual(result, EXPECTED_RESULT)