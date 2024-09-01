from __future__ import annotations
from unittest import TestCase
from dataclasses import dataclass
from typing import Annotated, Any, Dict, List, Optional, Tuple, Union
from abc import abstractmethod


from pyastodon.models.model import Model
from pyastodon.models.modelErrors import (
    InvalidAttributeTypeException,
    MissingAttributeException,
    UnsupportedTypeException
)


class ModelTestCase(TestCase):

    TestClass: type[Model]

    @abstractmethod
    def setUp(self) -> None:
        raise NotImplementedError()

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: None
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: bool
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: int
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: float
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: str
        self.TestClass = Test

    def testValue(self) -> None:
        json = "{\"attribute\": \"Hello, World!\"}"
        self.assertAttributeEquals(json, "Hello, World!")

    def testInvalid(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestGenericList(ModelTestCase):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: list
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: List
        self.TestClass = Test
class TestTypedList(ModelTestCase):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: list[int]
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: List[int]
        self.TestClass = Test

class TestGenericTuple(ModelTestCase):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: tuple
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: Tuple
        self.TestClass = Test
class TestTypedTuple(ModelTestCase):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: tuple[int, str, int]
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: Tuple[int, str, int]
        self.TestClass = Test

class TestGenericDict(ModelTestCase):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: dict
        self.TestClass = Test

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
    def setUp(self) -> None: 
        @dataclass
        class Test(Model):
            attribute: Dict
        self.TestClass = Test   
class TestTypedDict(ModelTestCase):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: dict[str, int]
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: Dict[str, int]
        self.TestClass = Test

class TestAnnotated(ModelTestCase):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: Annotated[int, "Hello, World!"]
        self.TestClass = Test

    def testValue(self) -> None:
        json = "{\"attribute\": 1}"
        self.assertAttributeEquals(json, 1)
        
    def testInvalid(self) -> None:
        json = "{\"attribute\": \"Hello, World!\"}"
        self.assertInvalidAttribute(json)

    def testMissing(self) -> None:
        self.assertMissingAttribute()

class TestOptional(ModelTestCase):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: Optional[int]
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: Union[int, None]
        self.TestClass = Test
class TestOptionalAsUnionAsPipe(TestOptional):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: int | None
        self.TestClass = Test
class TestMultipleOptional(TestOptional):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: Optional[int]
            attribute2: Optional[int]
        self.TestClass = Test

class TestUnion(ModelTestCase):
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: Union[int, str]
        self.TestClass = Test

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
    def setUp(self) -> None:
        @dataclass
        class Test(Model):
            attribute: int | str
        self.TestClass = Test

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