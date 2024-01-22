from __future__ import annotations
from typing import Literal, Self, Union, Any
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
            if isOptional and (name not in jsonData or jsonData[name] is None):
                kwargs[name] = None
                continue

            if name not in jsonData:
                raise KeyError(f"Missing key {name} for {cls} to deserialize.")
            value = jsonData[name]

            parsed = cls._parseValueToType(type_, value)
            kwargs[name] = parsed

        return cls(**kwargs)
    
    @classmethod
    def _parseValueToType(cls, type_: type, value: Any) -> Any:
        origin = typing.get_origin(type_)

        if origin is None:
            if issubclass(type_, StringModel):
                return type_.deserialize(value)
            if issubclass(type_, JSONModel):
                return type_.deserialize(json.dumps(value))
            return type_(value)

        args = typing.get_args(type_)
        if origin is list:
            return list(map(lambda v: cls._parseValueToType(
                args[0], v
            ), value))
        
        if origin is Union:
            for a in args:
                try: return cls._parseValueToType(a, value)
                except Exception: pass

        if origin is Literal:
            for a in args:
                if value == a:
                    return a
                
        raise TypeError(f"Unsupported type '{type_}'.")