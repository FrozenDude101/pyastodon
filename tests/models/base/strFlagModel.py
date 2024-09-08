from enum import auto

from .enumModel import EnumModelTestCase

from pyastodon.models.base import StrFlagModel


class TestStrFlagModel(EnumModelTestCase):

    class TestClass(StrFlagModel):
        ATTRIBUTE1 = auto()
        ATTRIBUTE2 = auto()

    def testLeft(self) -> None:
        json = "ATTRIBUTE1"
        self.assertParsesAs(json, self.TestClass.ATTRIBUTE1)

    def testRight(self) -> None:
        json = "ATTRIBUTE2"
        self.assertParsesAs(json, self.TestClass.ATTRIBUTE2)

    def testBoth(self) -> None:
        json = "ATTRIBUTE1 ATTRIBUTE2"
        self.assertParsesAs(json, self.TestClass.ATTRIBUTE1 | self.TestClass.ATTRIBUTE2)

    def testLower(self) -> None:
        json = "attribute1 ATTRIBUTE2"
        self.assertParsesAs(json, self.TestClass.ATTRIBUTE1 | self.TestClass.ATTRIBUTE2)

    def testInvalid(self) -> None:
        json = "ATTRIBUTE3"
        self.assertInvalidAttribute(json)