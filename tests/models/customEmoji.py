from tests.models import ModelTestCase
from pyastodon.models import CustomEmoji


class TestCustomEmojiModel(ModelTestCase):
    
    def testDeserialize(self) -> None:
        INPUT = """{
            "shortcode": "blobaww",
            "url": "https://files.mastodon.social/custom_emojis/images/000/011/739/original/blobaww.png",
            "static_url": "https://files.mastodon.social/custom_emojis/images/000/011/739/static/blobaww.png",
            "visible_in_picker": true,
            "category": "Blobs"
        }"""
        EXPECTED_RESULT = CustomEmoji(
            shortcode = "blobaww",
            url = "https://files.mastodon.social/custom_emojis/images/000/011/739/original/blobaww.png",
            static_url = "https://files.mastodon.social/custom_emojis/images/000/011/739/static/blobaww.png",
            visible_in_picker = True,
            category = "Blobs",
        )

        result = CustomEmoji.deserialize(INPUT)
        self.assertCustomEmojiEqual(result, EXPECTED_RESULT)