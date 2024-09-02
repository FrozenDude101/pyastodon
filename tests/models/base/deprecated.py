from typing import Optional
from dataclasses import dataclass

from .objectModel import ModelTestCase

from pyastodon.models.base import (
    Deprecated,
    ObjectModel,
)
from typing import override

class TestDeprecated(ModelTestCase):

    @dataclass
    class TestClass(ObjectModel):
        attribute: Deprecated[int]

    def testValue(self) -> None:
        json = {"attribute": 1}
        self.assertAttributeEquals(json, 1)

    def testMissing(self) -> None:
        json = {}
        self.assertAttributeEquals(json, None)

    def testNull(self) -> None:
        json = {"attribute": None}
        self.assertInvalidAttribute(json)

class TestDeprecatedOptional(TestDeprecated):
    
    @dataclass
    class TestClass(ObjectModel): # type: ignore
        attribute: Deprecated[Optional[int]]

    def testNull(self) -> None:
        json = {"attribute": None}
        self.assertAttributeEquals(json, None)