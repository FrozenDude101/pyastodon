from typing import Optional
from dataclasses import dataclass

from .model import ModelTestCase

from pyastodon.models.base import (
    Deprecated,
    Model,
)
from typing import override

class TestDeprecated(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: Deprecated[int]

    def testValue(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertAttributeEquals(json, 1)

    def testMissing(self) -> None:
        json = "{}"
        self.assertAttributeEquals(json, None)

    def testNull(self) -> None:
        json = "{\"attribute\": null}"
        self.assertInvalidAttribute(json)

class TestDeprecatedOptional(TestDeprecated):
    
    @dataclass
    class TestClass(Model): # type: ignore
        attribute: Deprecated[Optional[int]]

    def testValue(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertAttributeEquals(json, 1)

    def testMissing(self) -> None:
        json = "{}"
        self.assertAttributeEquals(json, None)

    def testNull(self) -> None:
        json = "{\"attribute\": null}"
        self.assertAttributeEquals(json, None)

    def testWarningOnGet(self) -> None:
        test = self.TestClass.deserialize("{\"attribute\": 1}")
        attr = test.attribute

    def testWarningOnSet(self) -> None:
        test = self.TestClass.deserialize("{\"attribute\": 1}")
        test.attribute = 2