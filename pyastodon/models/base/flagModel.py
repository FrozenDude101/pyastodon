from typing import Any, Self

from enum import Flag

from pyastodon.models.base.enumModel import EnumModel
from pyastodon.models.base.modelErrors import InvalidAttributeTypeException


class FlagModel(EnumModel, Flag):

    @classmethod
    def deserialize(cls, value: Any) -> Self:
        if value in cls:
            return cls(int(value))
        raise InvalidAttributeTypeException()