from tests.models import ModelTestCase
from pyastodon.models import Source, Field


class TestSourceModel(ModelTestCase):
    
    def testDeserialize(self) -> None:
        INPUT = """{
            "note": "Testing the Source model!",
            "fields": [{
                "name": "Field Name",
                "value": "Field Value",
                "verified_at": null
            }],
            "privacy": "public",
            "sensitive": false,
            "language": "en",
            "follow_requests_count": 0
        }"""
        EXPECTED_RESULT = Source(
            note = "Testing the Source model!",
            fields = [
                Field(
                    name = "Field Name",
                    value = "Field Value",
                    verified_at = None,
                )
            ],
            privacy = "public",
            sensitive = False,
            language = "en",
            follow_requests_count = 0,
        )

        result = Source.deserialize(INPUT)
        self.assertSourceEqual(result, EXPECTED_RESULT)