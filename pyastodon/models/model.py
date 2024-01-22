from __future__ import annotations
from typing import Literal, Self, Optional, Union
import typing

import dataclasses
import inspect
import json


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

@dataclasses.dataclass(kw_only=True)
class JSONModel(Model):

    @classmethod
    def deserialize(cls, data: str) -> Self:
        jsonData = json.loads(data)
        if not isinstance(jsonData, dict):
            raise ValueError("JSON value must be a dictionary to be parsed.")
        return cls.fromJSON(jsonData)
    
    @classmethod
    def fromJSON(cls, jsonData: dict) -> Self:
        classAnnotations = list(map(
            lambda c: inspect.get_annotations(c, eval_str=True),
            cls.__mro__[:-3]
        ))[::-1]
        annotations = {n: t for cA in classAnnotations for n,t in cA.items()}

        kwargs = {}
        for name, type_ in annotations.items():
            origin = typing.get_origin(type_)

            isUnion = origin is typing.Union
            isOptional = isUnion and None.__class__ in typing.get_args(type_)
            if name not in jsonData and isOptional:
                kwargs[name] = None
                continue
            if name not in jsonData:
                raise KeyError(f"Missing key {name} for {cls} to deserialize.")
            value = jsonData[name]

            types = typing.get_args(type_) if isUnion else (type_,)

            for t in types:
                origin = typing.get_origin(t)

                if origin is typing.Literal:
                    for literal in typing.get_args(type_):
                        if literal == value:
                            kwargs[name] = literal

                elif issubclass(t, StringModel):
                    kwargs[name] = t.deserialize(value)
                elif issubclass(t, JSONModel):
                    kwargs[name] = t.deserialize(json.dumps(value))
                    
                else:
                    try:
                        kwargs[name] = t(value)
                    except Exception:
                        continue

        return cls(**kwargs)