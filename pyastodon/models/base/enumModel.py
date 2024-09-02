from typing import Any, Self

from enum import Enum

from pyastodon.models.base.model import Model
from pyastodon.models.base.modelErrors import InvalidAttributeTypeException


class EnumModel(Model, Enum):

    @classmethod
    def deserialize(cls, value: Any) -> Self:
        if value in cls:
            return cls(value) # type: ignore
        raise InvalidAttributeTypeException()
