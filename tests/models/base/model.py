from __future__ import annotations
from unittest import TestCase
from dataclasses import dataclass
from typing import Annotated, Any, Dict, List, Optional, Tuple, Union
from abc import abstractmethod


from pyastodon.models.base import (
    Model,
    InvalidAttributeTypeException,
    MissingAttributeException,
    UnsupportedTypeException
)


class ModelTestCase(TestCase):

    TestClass: type[Model]

    def assertAttributeEquals(self, json: str, expected: Any) -> None:
        result = self.TestClass.deserialize(json)

        self.assertIsInstance(result, self.TestClass)
        actual = result.__getattribute__("attribute")
        self.assertEqual(expected, actual)

    def assertModelRaisesError(self, json: str, error: type[Exception]) -> None:
        with self.assertRaises(error):
            self.TestClass.deserialize(json)

    def assertInvalidAttribute(self, json: str) -> None:
        self.assertModelRaisesError(json, InvalidAttributeTypeException)

    def assertMissingAttribute(self, json: str = "{}") -> None:
        self.assertModelRaisesError(json, MissingAttributeException)

    def assertUnsupported(self, json: str = "{\"attribute\": 1}") -> None:
        self.assertModelRaisesError(json, UnsupportedTypeException)

class TestNone(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: None

    def testNull(self) -> None:
        json = "{\"attribute\": null}"
        self.assertAttributeEquals(json, None)

    def testMissing(self) -> None:
        json = "{}"
        self.assertAttributeEquals(json, None)

    def testInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

class TestBool(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: bool

    def testTrue(self) -> None:
        json = "{\"attribute\": true}"
        self.assertAttributeEquals(json, True)

    def testFalse(self) -> None:
        json = "{\"attribute\": false}"
        self.assertAttributeEquals(json, False)

    def testZeroInvalid(self) -> None:
        json = "{\"attribute\": 0}"
        self.assertInvalidAttribute(json)

    def testOneInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

class TestInt(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: int

    def testValue(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertAttributeEquals(json, 1)

    def testInvalid(self) -> None:
        json = "{\"attribute\": \"Hello, World!\"}"
        self.assertInvalidAttribute(json)

    def testBoolInvalid(self) -> None:
        json = "{\"attribute\": true}"
        self.assertInvalidAttribute(json)

    def testFloatInvalid(self) -> None:
        json = "{\"attribute\": 2.3}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestFloat(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: float

    def testValue(self) -> None:
        json = "{\"attribute\": 2.3}"
        self.assertAttributeEquals(json, 2.3)

    def testInteger(self) -> None:
        json = "{\"attribute\": 2}"
        self.assertAttributeEquals(json, 2.0)

    def testDecimal(self) -> None:
        json = "{\"attribute\": 2.0}"
        self.assertAttributeEquals(json, 2.0)

    def testBoolInvalid(self) -> None:
        json = "{\"attribute\": true}"
        self.assertInvalidAttribute(json)

class TestString(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: str

    def testValue(self) -> None:
        json = "{\"attribute\": \"Hello, World!\"}"
        self.assertAttributeEquals(json, "Hello, World!")

    def testInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()


class TestGenericList(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: list

    def testItems(self) -> None:
        json = "{\"attribute\": [1, 2, 3]}"
        self.assertAttributeEquals(json, [1, 2, 3])

    def testEmpty(self) -> None:
        json = "{\"attribute\": []}"
        self.assertAttributeEquals(json, [])

    def testNested(self) -> None:
        json = "{\"attribute\": [[1, 2], [3, 4], [5, 6]]}"
        self.assertAttributeEquals(json, [[1, 2], [3, 4], [5, 6]])

    def testInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestDeprecatedGenericList(TestGenericList):

    @dataclass
    class TestClass(Model): # type: ignore
        attribute: List


class TestTypedList(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: list[int]

    def testItems(self) -> None:
        json = "{\"attribute\": [1, 2, 3]}"
        self.assertAttributeEquals(json, [1, 2, 3])

    def testEmpty(self) -> None:
        json = "{\"attribute\": []}"
        self.assertAttributeEquals(json, [])

    def testInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

    def testInvalidItem(self) -> None:
        json = "{\"attribute\": [1, \"2\", 3]}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestDeprecatedTypedList(TestTypedList):

    @dataclass
    class TestClass(Model): # type: ignore
        attribute: List[int]

class TestGenericTuple(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: tuple

    def testItems(self) -> None:
        json = "{\"attribute\": [1, \"Hello, World!\", 3]}"
        self.assertAttributeEquals(json, (1, "Hello, World!", 3))

    def testEmpty(self) -> None:
        json = "{\"attribute\": []}"
        self.assertAttributeEquals(json, ())

    def testInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestDeprecatedGenericTuple(TestGenericTuple):

    @dataclass
    class TestClass(Model): # type: ignore
        attribute: Tuple

class TestTypedTuple(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: tuple[int, str, int]

    def testItems(self) -> None:
        json = "{\"attribute\": [1, \"Hello, World!\", 3]}"
        self.assertAttributeEquals(json, (1, "Hello, World!", 3))

    def testInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

    def testItemInvalid(self) -> None:
        json = "{\"attribute\": [1, 2, 3]}"
        self.assertInvalidAttribute(json)

    def testMissingItemInvalid(self) -> None:
        json = "{\"attribute\": [1, \"Hello, World!\"]}"
        self.assertInvalidAttribute(json)

    def testEmptyInvalid(self) -> None:
        json = "{\"attribute\": []}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestDeprecatedTypedTuple(TestTypedTuple):

    @dataclass
    class TestClass(Model): # type: ignore
        attribute: Tuple[int, str, int]


class TestGenericDict(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: dict

    def testItems(self) -> None:
        json = "{\"attribute\": {\"key1\": 1, \"key2\": \"Hello, World!\"}}"
        self.assertAttributeEquals(json, {"key1": 1, "key2": "Hello, World!"})

    def testEmpty(self) -> None:
        json = "{\"attribute\": {}}"
        self.assertAttributeEquals(json, {})

    def testInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestDeprecatedGenericDict(TestGenericDict):

    @dataclass
    class TestClass(Model): # type: ignore
        attribute: Dict

class TestTypedDict(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: dict[str, int]

    def testItems(self) -> None:
        json = "{\"attribute\": {\"key1\": 1, \"key2\": 2}}"
        self.assertAttributeEquals(json, {"key1": 1, "key2": 2})

    def testEmpty(self) -> None:
        json = "{\"attribute\": {}}"
        self.assertAttributeEquals(json, {})

    def testInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

    def testInvalidItem(self) -> None:
        json = "{\"attribute\": {\"key1\": 1, \"key2\": \"Hello, World!\"}}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestDeprecatedTypedDict(TestTypedDict):

    @dataclass
    class TestClass(Model): # type: ignore
        attribute: Dict[str, int]


class TestAnnotated(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: Annotated[int, "Hello, World!"]

    def testValue(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertAttributeEquals(json, 1)
        
    def testInvalid(self) -> None:
        json = "{\"attribute\": \"Hello, World!\"}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()


class TestOptional(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: Optional[int]

    def testValue(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertAttributeEquals(json, 1)

    def testNull(self) -> None:
        json = "{\"attribute\": null}"
        self.assertAttributeEquals(json, None)

    def testMissing(self):
        json = "{}"
        self.assertAttributeEquals(json, None)

    def testInvalid(self) -> None:
        json = "{\"attribute\": \"Hello, World!\"}"
        self.assertInvalidAttribute(json)      

class TestOptionalAsUnion(TestOptional):

    @dataclass
    class TestClass(Model): # type: ignore
        attribute: Union[int, None]

class TestOptionalAsUnionAsPipe(TestOptional):
    
    @dataclass
    class TestClass(Model): # type: ignore
        attribute: int | None

class TestMultipleOptional(TestOptional):

    @dataclass
    class TestClass(Model): # type: ignore
        attribute: Optional[int]
        attribute2: Optional[int]


class TestUnion(ModelTestCase):

    @dataclass
    class TestClass(Model):
        attribute: Union[int, str]

    def testLeft(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertAttributeEquals(json, 1)

    def testRight(self) -> None:
        json = "{\"attribute\": \"Hello, World!\"}"
        self.assertAttributeEquals(json, "Hello, World!")

    def testInvalid(self) -> None:
        json = "{\"attribute\": true}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestUnionAsPipe(TestUnion):

    @dataclass
    class TestClass(Model): # type: ignore
        attribute: int | str

# TODO
# typing.Any
# typing.AnyStr?
# typing.LiteralString?
# typing.TypeAlias
# typing.Literal
# typing.Final

# typing.Required
# typing.NotRequired

# typing.NamedTuple
# typing.NewType
# typing.TypedDict