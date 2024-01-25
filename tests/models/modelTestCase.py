import unittest

from pyastodon.models import *


class ModelTestCase(unittest.TestCase):

    def assertAccountEqual(self, a1: Account, a2: Account) -> None:
        self.assertEqual(a1.id, a2.id)
        self.assertEqual(a1.username, a2.username)
        self.assertEqual(a1.acct, a2.acct)
        self.assertEqual(a1.url, a2.url)
        self.assertEqual(a1.display_name, a2.display_name)
        self.assertEqual(a1.note, a2.note)
        self.assertEqual(a1.avatar, a2.avatar)
        self.assertEqual(a1.avatar_static, a2.avatar_static)
        self.assertEqual(a1.header, a2.header)
        self.assertEqual(a1.header_static, a2.header_static)
        self.assertEqual(a1.locked, a2.locked)
        self.assertEqual(a1.bot, a2.bot)
        self.assertEqual(a1.group, a2.group)
        self.assertEqual(a1.discoverable, a2.discoverable)
        self.assertEqual(a1.noindex, a2.noindex)
        self.assertEqual(a1.moved, a2.moved)
        self.assertEqual(a1.suspended, a2.suspended)
        self.assertEqual(a1.limited, a2.limited)
        self.assertEqual(a1.created_at, a2.created_at)
        self.assertEqual(a1.last_status_at, a2.last_status_at)
        self.assertEqual(a1.statuses_count, a2.statuses_count)
        self.assertEqual(a1.followers_count, a2.followers_count)
        self.assertEqual(a1.following_count, a2.following_count)

        self.assertEqual(len(a1.emojis), len(a2.emojis))
        for (e1, e2) in zip(a1.emojis, a2.emojis):
            self.assertCustomEmojiEqual(e1, e2)

        self.assertEqual(len(a1.fields), len(a2.fields))
        for (f1, f2) in zip(a1.fields, a2.fields):
            self.assertFieldEqual(f1, f2)

    def assertApplicationEqual(self, a1: Application, a2: Application) -> None:
        self.assertEqual(a1.name, a2.name)
        self.assertEqual(a1.website, a2.website)
        self.assertEqual(a1.client_id, a2.client_id)
        self.assertEqual(a1.client_secret, a2.client_secret)
        self.assertEqual(a1.vapid_key, a2.vapid_key)

    def assertCredentialAccountEqual(self, ca1: CredentialAccount, ca2: CredentialAccount) -> None:
        self.assertAccountEqual(ca1, ca2)
        self.assertSourceEqual(ca1.source, ca2.source)
        self.assertRoleEqual(ca1.role, ca2.role)

    def assertCustomEmojiEqual(self, e1: CustomEmoji, e2: CustomEmoji) -> None:
        self.assertEqual(e1.shortcode, e2.shortcode)
        self.assertEqual(e1.url, e2.url)
        self.assertEqual(e1.static_url, e2.static_url)
        self.assertEqual(e1.visible_in_picker, e2.visible_in_picker)
        self.assertEqual(e1.category, e2.category)

    def assertFieldEqual(self, f1: Field, f2: Field) -> None:
        self.assertEqual(f1.name, f2.name)
        self.assertEqual(f1.value, f2.value)
        self.assertEqual(f1.verified_at, f2.verified_at)

    def assertPermissionEqual(self, p1: Permission, p2: Permission) -> None:
        self.assertEqual(p1, p2)

    def assertRoleEqual(self, r1: Role, r2: Role) -> None:
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.name, r2.name)
        self.assertEqual(r1.color, r2.color)
        self.assertPermissionEqual(r1.permissions, r2.permissions)
        self.assertEqual(r1.highlighted, r2.highlighted)

    def assertScopeEqual(self, s1: Scope, s2: Scope) -> None:
        self.assertEqual(s1, s2)

    def assertSourceEqual(self, s1: Source, s2: Source) -> None:
        self.assertEqual(s1.note, s2.note)
        self.assertEqual(s1.privacy, s2.privacy)
        self.assertEqual(s1.sensitive, s2.sensitive)
        self.assertEqual(s1.language, s2.language)
        self.assertEqual(s1.follow_requests_count, s2.follow_requests_count)

        self.assertEqual(len(s1.fields), len(s2.fields))
        for (f1, f2) in zip(s1.fields, s1.fields):
            self.assertFieldEqual(f1, f2)

    def assertTokenEqual(self, t1: Token, t2: Token) -> None:
        self.assertEqual(t1.access_token, t2.access_token)
        self.assertEqual(t1.token_type, t2.token_type)
        self.assertScopeEqual(t1.scope, t2.scope)
        self.assertEqual(t1.created_at, t2.created_at)