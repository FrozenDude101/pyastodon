from tests.models import ModelTestCase
from pyastodon.models import Permission


class TestPermissionModel(ModelTestCase):
    
    def testBlankString(self) -> None:
        INPUT = ""
        EXPECTED_RESULT = Permission.NONE

        result = Permission.deserialize(INPUT)
        self.assertPermissionEqual(result, EXPECTED_RESULT)

    def testZeroString(self) -> None:
        INPUT = "0"
        EXPECTED_RESULT = Permission.NONE

        result = Permission.deserialize(INPUT)
        self.assertPermissionEqual(result, EXPECTED_RESULT)

    def testAdminString(self) -> None:
        INPUT = "1"
        EXPECTED_RESULT = Permission.ADMINISTRATOR

        result = Permission.deserialize(INPUT)
        self.assertPermissionEqual(result, EXPECTED_RESULT)

    def testCompositeString(self) -> None:
        INPUT = "12"
        EXPECTED_RESULT = Permission.VIEW_AUDIT_LOG | Permission.VIEW_DASHBOARD

        result = Permission.deserialize(INPUT)
        self.assertPermissionEqual(result, EXPECTED_RESULT)

    def testAllString(self) -> None:
        INPUT = "1048575"
        EXPECTED_RESULT = Permission.ALL

        result = Permission.deserialize(INPUT)
        self.assertPermissionEqual(result, EXPECTED_RESULT)

    def testNonePermission(self) -> None:
        INPUT = Permission.NONE
        EXPECTED_RESULT = "0"

        result = str(INPUT)
        self.assertEqual(result, EXPECTED_RESULT)

    def testAdminPermission(self) -> None:
        INPUT = Permission.ADMINISTRATOR
        EXPECTED_RESULT = "1"

        result = str(INPUT)
        self.assertEqual(result, EXPECTED_RESULT)

    def testCompositePermission(self) -> None:
        INPUT = Permission.VIEW_AUDIT_LOG | Permission.VIEW_DASHBOARD
        EXPECTED_RESULT = "12"

        result = str(INPUT)
        self.assertEqual(result, EXPECTED_RESULT)

    def testAllPermission(self) -> None:
        INPUT = Permission.ALL
        EXPECTED_RESULT = "1048575"

        result = str(INPUT)
        self.assertEqual(result, EXPECTED_RESULT)