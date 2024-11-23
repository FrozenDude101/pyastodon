from unittest import TestCase
from enum import auto
from typing import Any


from pyastodon.models.base import (
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
        ATTRIBUTE1 = auto()
        ATTRIBUTE2 = auto()

    def testLeft(self) -> None:
        json = 1
        self.assertParsesAs(json, self.TestClass.ATTRIBUTE1)

    def testRight(self) -> None:
        json = 2
        self.assertParsesAs(json, self.TestClass.ATTRIBUTE2)

    def testInvalid(self) -> None:
        json = 3
        self.assertInvalidAttribute(json)