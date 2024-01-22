import unittest

from pyastodon.models import *


class ModelTestCase(unittest.TestCase):

    def assertScopeEqual(self, s1: Scope, s2: Scope) -> None:
        self.assertEqual(s1, s2)

    def assertTokenEqual(self, t1: Token, t2: Token) -> None:
        self.assertEqual(t1.access_token, t2.access_token)
        self.assertEqual(t1.token_type, t2.token_type)
        self.assertScopeEqual(t1.scope, t2.scope)
        self.assertEqual(t1.created_at, t2.created_at)