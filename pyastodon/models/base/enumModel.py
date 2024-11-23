from typing import Self

from enum import Enum

from pyastodon.models.base.model import Model
from pyastodon.models.base.modelErrors import InvalidAttributeTypeException


class EnumModel(Model, Enum):

    @classmethod
    def deserialize(cls, value: str | int) -> Self:
        if value in cls:
            return cls(value)
        if str(value).upper() in cls.__members__:
            return cls.__members__[str(value).upper()]
        raise InvalidAttributeTypeException()
