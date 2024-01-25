from tests.models import ModelTestCase
from pyastodon.models import (
    Account, CredentialAccount, CustomEmoji, Field, Permission, Source, Role
)


class TestAccountModel(ModelTestCase):
    
    def testDeserialize(self) -> None:
        INPUT = """{
            "id": "23634",
            "username": "test",
            "acct": "test@mastodon.example",
            "url": "https://mastodon.example",
            "display_name": "testing",
            "note": "<p>Testing the Account model.:emoji:</p>",
            "avatar": "https://mastodon.example/avatar.png",
            "avatar_static": "https://mastodon.example/avatar_static.png",
            "header": "https://mastodon.example/header.png",
            "header_static": "https://mastodon.example/header_static.png",
            "locked": false,
            "emojis": [
                {
                    "shortcode": "emoji",
                    "url": "https://mastodon.example/emoji.png",
                    "static_url": "https://mastodon.example/emoji_static.png",
                    "visible_in_picker": true,
                    "category": "test"
                }
            ],
            "fields": [
                {
                    "name": "Pronouns",
                    "value": "any",
                    "verified_at": null
                }
            ],
            "bot": false,
            "group": false,
            "created_at": "2024-01-22T12:34:56.789Z",
            "last_status_at": "2024-01-22",
            "statuses_count": 123,
            "followers_count": 456,
            "following_count": 789
        }"""
        EXPECTED_RESULT = Account(
            id = "23634",
            username = "test",
            acct = "test@mastodon.example",
            url = "https://mastodon.example",
            display_name = "testing",
            note = "<p>Testing the Account model.:emoji:</p>",
            avatar = "https://mastodon.example/avatar.png",
            avatar_static = "https://mastodon.example/avatar_static.png",
            header = "https://mastodon.example/header.png",
            header_static = "https://mastodon.example/header_static.png",
            locked = False,
            emojis = [
                CustomEmoji(
                    shortcode = "emoji",
                    url = "https://mastodon.example/emoji.png",
                    static_url = "https://mastodon.example/emoji_static.png",
                    visible_in_picker = True,
                    category = "test"
                ),
            ],
            fields = [
                Field(
                    name = "Pronouns",
                    value = "any",
                    verified_at = None,
                ),
            ],
            bot = False,
            group = False,
            created_at = "2024-01-22T12:34:56.789Z",
            last_status_at = "2024-01-22",
            statuses_count = 123,
            followers_count = 456,
            following_count = 789,
        )

        result = Account.deserialize(INPUT)
        self.assertAccountEqual(result, EXPECTED_RESULT)
        

class TestCredentialAccountModel(ModelTestCase):
    
    def testDeserialize(self) -> None:
        INPUT = """{
            "id": "23634",
            "username": "test",
            "acct": "test@mastodon.example",
            "url": "https://mastodon.example",
            "display_name": "testing",
            "note": "<p>Testing the CredentialAccount model.:emoji:</p>",
            "avatar": "https://mastodon.example/avatar.png",
            "avatar_static": "https://mastodon.example/avatar_static.png",
            "header": "https://mastodon.example/header.png",
            "header_static": "https://mastodon.example/header_static.png",
            "locked": false,
            "emojis": [
                {
                    "shortcode": "emoji",
                    "url": "https://mastodon.example/emoji.png",
                    "static_url": "https://mastodon.example/emoji_static.png",
                    "visible_in_picker": true,
                    "category": "test"
                }
            ],
            "fields": [
                {
                    "name": "Pronouns",
                    "value": "any",
                    "verified_at": null
                }
            ],
            "bot": false,
            "group": false,
            "created_at": "2024-01-22T12:34:56.789Z",
            "last_status_at": "2024-01-22",
            "statuses_count": 123,
            "followers_count": 456,
            "following_count": 789,
            "source": {
                "note": "Testing the CredentialAccount model!",
                "fields": [{
                    "name": "Field Name",
                    "value": "Field Value",
                    "verified_at": null
                }],
                "privacy": "public",
                "sensitive": false,
                "language": "en",
                "follow_requests_count": 0
            },
            "role": {
                "id": 3,
                "name": "Owner",
                "color": "#ff3838",
                "permissions": 1048575,
                "highlighted": true
            }
        }"""
        EXPECTED_RESULT = CredentialAccount(
            id = "23634",
            username = "test",
            acct = "test@mastodon.example",
            url = "https://mastodon.example",
            display_name = "testing",
            note = "<p>Testing the CredentialAccount model.:emoji:</p>",
            avatar = "https://mastodon.example/avatar.png",
            avatar_static = "https://mastodon.example/avatar_static.png",
            header = "https://mastodon.example/header.png",
            header_static = "https://mastodon.example/header_static.png",
            locked = False,
            emojis = [
                CustomEmoji(
                    shortcode = "emoji",
                    url = "https://mastodon.example/emoji.png",
                    static_url = "https://mastodon.example/emoji_static.png",
                    visible_in_picker = True,
                    category = "test"
                ),
            ],
            fields = [
                Field(
                    name = "Pronouns",
                    value = "any",
                    verified_at = None,
                ),
            ],
            bot = False,
            group = False,
            created_at = "2024-01-22T12:34:56.789Z",
            last_status_at = "2024-01-22",
            statuses_count = 123,
            followers_count = 456,
            following_count = 789,
            source = Source(
                note = "Testing the CredentialAccount model!",
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
            ),
            role = Role(
                id = 3,
                name = "Owner",
                color = "#ff3838",
                permissions = Permission.ALL,
                highlighted = True,
            ),
        )

        result = CredentialAccount.deserialize(INPUT)
        self.assertCredentialAccountEqual(result, EXPECTED_RESULT)