from __future__ import annotations
import json

import typing, types
from typing import Any, Optional, Self, Union

from pyastodon.models.base.modelErrors import (
    CantFindTypeException,
    InvalidAttributeTypeException,
    MissingAttributeException,
    UnsupportedTypeException,
)


INVALID = object()

class Model:

    @classmethod
    def deserialize(cls, raw: str) -> Self:
        jsonDict = json.loads(raw)
        return cls._fromJson(jsonDict)
    
    @classmethod
    def _fromJson(cls, jsonDict: dict[str, Any]) -> Self:
        try:
            annotations = typing.get_type_hints(cls)
        except NameError:
            raise CantFindTypeException()
        
        for attribute in annotations:
            annotation = annotations[attribute]
            if attribute not in jsonDict:
                if cls._castValue(annotation, None) is not INVALID:
                    jsonDict[attribute] = None
                    continue
                raise MissingAttributeException(attribute)
            
            value = jsonDict[attribute]
            castValue = cls._castValue(annotation, value)
            if castValue is INVALID:
                raise InvalidAttributeTypeException(annotation, value)
            jsonDict[attribute] = castValue

        return cls(**jsonDict)

    
    @classmethod
    def _castValue(cls, annotation: type, value) -> Optional[Any]:
        origin = typing.get_origin(annotation)
        args = typing.get_args(annotation)

        if origin is None:
            if annotation is type(None):
                if value is None:
                    return value
                return INVALID
            
            if annotation is bool:
                if isinstance(value, bool):
                    return value
                return INVALID
            
            if annotation is int:
                if isinstance(value, int) and not isinstance(value, bool):
                    return value
                return INVALID 
            
            if annotation is float:
                if isinstance(value, float) or isinstance(value, int) and not isinstance(value, bool):
                    return value
                return INVALID
            
            if annotation is str:
                if isinstance(value, str):
                    return value
                return INVALID
            
            if annotation is list:
                if isinstance(value, list):
                    return value
                return INVALID
            
            if annotation is tuple:
                if isinstance(value, list):
                    return tuple(value)
                return INVALID
            
            if annotation is dict:
                if isinstance(value, dict):
                    return value
                return INVALID
            
            if issubclass(annotation, Model):
                if isinstance(value, dict):
                    return annotation._fromJson(value)
                return INVALID
        
        elif origin is list:
            if not isinstance(value, list):
                return INVALID
            if len(args) == 0:
                return value
            
            castValue = [cls._castValue(args[0], v) for v in value]
            if any([cv is INVALID for cv in castValue]):
                return INVALID
            return castValue
        
        elif origin is tuple:
            if not isinstance(value, list):
                return INVALID
            if len(args) == 0:
                return tuple(value)
            if len(args) != len(value):
                return INVALID
            
            castValue = tuple(cls._castValue(a, v) for a, v in zip(args, value))
            if any([cv is INVALID for cv in castValue]):
                return INVALID
            return castValue
        
        elif origin is dict:
            if not isinstance(value, dict):
                return INVALID
            if len(args) == 0:
                return value
            if args[0] is not str:
                raise UnsupportedTypeException()
            
            castValue = {cls._castValue(args[0], k): cls._castValue(args[1], v) for k, v in value.items()}
            if any([cv is INVALID for cv in castValue.values()]):
                return INVALID
            return castValue
        
        elif origin is Union or origin is types.UnionType:
            castValue = [cls._castValue(a, value) for a in args]
            for cv in castValue:
                if cv is not INVALID:
                    return cv
            return INVALID
        
        raise UnsupportedTypeException(annotation)
