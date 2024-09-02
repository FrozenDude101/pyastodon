from unittest import TestCase
from enum import auto
from typing import Any


from pyastodon.models.base import (
    FlagModel,
    EnumModel,
    InvalidAttributeTypeException,
)

class EnumModelTestCase(TestCase):

    TestClass: type[EnumModel]

    def assertParsesAs(self, value: Any, expected: EnumModel) -> None:
        result = self.TestClass.deserialize(value)

        self.assertIsInstance(result, self.TestClass)
        self.assertEqual(expected, result)

    def assertModelRaisesError(self, value: Any, error: type[Exception]) -> None:
        with self.assertRaises(error):
            self.TestClass.deserialize(value)

    def assertInvalidAttribute(self, value: Any) -> None:
        self.assertModelRaisesError(value, InvalidAttributeTypeException)


class TestEnumModel(EnumModelTestCase):

    class TestClass(EnumModel):
        attribute1 = auto()
        attribute2 = auto()

    def testLeft(self) -> None:
        json = 1
        self.assertParsesAs(json, self.TestClass.attribute1)

    def testRight(self) -> None:
        json = 2
        self.assertParsesAs(json, self.TestClass.attribute2)

    def testInvalid(self) -> None:
        json = 3
        self.assertInvalidAttribute(json)


class TestFlagModel(EnumModelTestCase):

    class TestClass(FlagModel):
        attribute1 = auto()
        attribute2 = auto()

    def testLeft(self) -> None:
        json = 1
        self.assertParsesAs(json, self.TestClass.attribute1)

    def testRight(self) -> None:
        json = 2
        self.assertParsesAs(json, self.TestClass.attribute2)

    def testBoth(self) -> None:
        json = 3
        self.assertParsesAs(json, self.TestClass.attribute1 | self.TestClass.attribute2)

    def testInvalid(self) -> None:
        json = 4
        self.assertInvalidAttribute(json)