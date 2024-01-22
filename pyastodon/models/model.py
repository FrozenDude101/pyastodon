from __future__ import annotations
from typing import Self, TypeVar


class Model():

    @classmethod
    def deserialize(cls, data: str) -> Self:
        raise NotImplementedError()
    
class StringModel(Model):

    @classmethod
    def deserialize(cls, data: str) -> Self:
        return cls.fromString(data)
    
    @classmethod
    def fromString(cls, string: str) -> Self:
        raise NotImplementedError()