from enum import auto

from .enumModel import EnumModelTestCase

from pyastodon.models.base import FlagModel


class TestFlagModel(EnumModelTestCase):

    class TestClass(FlagModel):
        ATTRIBUTE1 = auto()
        ATTRIBUTE2 = auto()

    def testLeft(self) -> None:
        json = 1
        self.assertParsesAs(json, self.TestClass.ATTRIBUTE1)

    def testRight(self) -> None:
        json = 2
        self.assertParsesAs(json, self.TestClass.ATTRIBUTE2)

    def testBoth(self) -> None:
        json = 3
        self.assertParsesAs(json, self.TestClass.ATTRIBUTE1 | self.TestClass.ATTRIBUTE2)

    def testInvalid(self) -> None:
        json = 4
        self.assertInvalidAttribute(json)