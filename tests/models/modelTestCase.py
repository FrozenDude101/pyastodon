import unittest

from pyastodon.models import *


class ModelTestCase(unittest.TestCase):

    def assertScopeEqual(self, s1: Scope, s2: Scope) -> None:
        self.assertEqual(s1, s2)