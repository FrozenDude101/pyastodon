from tests.models import ModelTestCase
from pyastodon.models import Permission, Role


class TestRoleModel(ModelTestCase):
    
    def testDeserialize(self) -> None:
        INPUT = """{
            "id": 3,
            "name": "Owner",
            "color": "#ff3838",
            "permissions": 1048575,
            "highlighted": true
        }"""
        EXPECTED_RESULT = Role(
            id = 3,
            name = "Owner",
            color = "#ff3838",
            permissions = Permission.ALL,
            highlighted = True,
        )

        result = Role.deserialize(INPUT)
        self.assertRoleEqual(result, EXPECTED_RESULT)