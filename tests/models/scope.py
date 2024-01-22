from tests.models import ModelTestCase
from pyastodon.models.scope import Scope


class TestScopeModel(ModelTestCase):
    
    def testBlankString(self) -> None:
        INPUT = ""
        EXPECTED_RESULT = Scope.READ

        result = Scope.deserialize(INPUT)
        self.assertScopeEqual(result, EXPECTED_RESULT)

    def testSingleString(self) -> None:
        INPUT = "read:accounts"
        EXPECTED_RESULT = Scope.READ_ACCOUNTS

        result = Scope.deserialize(INPUT)
        self.assertScopeEqual(result, EXPECTED_RESULT)

    def testReadString(self) -> None:
        INPUT = "read"
        EXPECTED_RESULT = Scope.READ

        result = Scope.deserialize(INPUT)
        self.assertScopeEqual(result, EXPECTED_RESULT)

    def testCompositeString(self) -> None:
        INPUT = "read write"
        EXPECTED_RESULT = Scope.READ | Scope.WRITE

        result = Scope.deserialize(INPUT)
        self.assertScopeEqual(result, EXPECTED_RESULT)

    def testEmptyScope(self) -> None:
        INPUT = Scope.NONE
        EXPECTED_RESULT = "read"

        result = str(INPUT)
        self.assertEqual(result, EXPECTED_RESULT)

    def testSingleScope(self) -> None:
        INPUT = Scope.READ_ACCOUNTS
        EXPECTED_RESULT = "read:accounts"

        result = str(INPUT)
        self.assertEqual(result, EXPECTED_RESULT)

    def testGroupedScope(self) -> None:
        INPUT = Scope.READ
        EXPECTED_RESULT = "read"

        result = str(INPUT)
        self.assertEqual(result, EXPECTED_RESULT)

    def testFollowDeprecation(self) -> None:
        INPUT = "follow"
        EXPECTED_RESULT = (
            "read:blocks read:follows read:mutes write:blocks write:follows"
            " write:mutes"
        )

        result = str(Scope.deserialize(INPUT))
        self.assertEqual(result, EXPECTED_RESULT)