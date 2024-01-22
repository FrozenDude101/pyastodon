from tests.models import ModelTestCase
from pyastodon.models import Application


class TestApplicationModel(ModelTestCase):
    
    def testDeserialize(self) -> None:
        INPUT = """{
            "name": "test app",
            "website": null,
            "vapid_key": "BCk-QqERU0q-CfYZjcuB6lnyyOYfJ2AifKqfeGIm7Z-HiTU5T9eTG5GxVA0_OH5mMlI4UkkDTpaZwozy0TzdZ2M="
        }"""
        EXPECTED_RESULT = Application(
            name = "test app",
            vapid_key = "BCk-QqERU0q-CfYZjcuB6lnyyOYfJ2AifKqfeGIm7Z-HiTU5T9eTG5GxVA0_OH5mMlI4UkkDTpaZwozy0TzdZ2M="
        )

        result = Application.deserialize(INPUT)
        self.assertApplicationEqual(result, EXPECTED_RESULT)