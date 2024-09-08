from typing import Self

from pyastodon.models.base.flagModel import FlagModel
from pyastodon.models.base.modelErrors import InvalidAttributeTypeException


class StrFlagModel(FlagModel):

    @classmethod
    def deserialize(cls, value: str) -> Self:
        value = value.replace(":", "_").upper()
        flags = cls(0)
        for flag in value.split(" "):
            flag = flag
            if flag not in cls.__members__:
                raise InvalidAttributeTypeException()
            flags |= cls.__members__[flag] # type: ignore
        return flags
        
    def __str__(self) -> str:
        name = self.name
        if name is None:
            raise Exception()
        return name.replace("|", " ").replace("_", ":").lower()