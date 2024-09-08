from typing import Any, Self

from enum import Enum

from pyastodon.models.base.model import Model
from pyastodon.models.base.modelErrors import InvalidAttributeTypeException


class EnumModel(Model, Enum):

    @classmethod
    def deserialize(cls, value: str) -> Self:
        if value.upper() in cls.__members__:
            return cls.__members__[value.upper()]
        raise InvalidAttributeTypeException()
