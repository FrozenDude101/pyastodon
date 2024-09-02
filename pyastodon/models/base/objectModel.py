from __future__ import annotations

import typing, types
from typing import Any, Literal, Optional, Self, Union

from pyastodon.models.base.modelErrors import (
    CantFindTypeException,
    InvalidAttributeTypeException,
    MissingAttributeException,
    UnsupportedTypeException,
)
from pyastodon.models.base.deprecated import Deprecated
from pyastodon.models.base.model import Model


INVALID = object()

class ObjectModel(Model):

    @classmethod
    def deserialize(cls, json: dict) -> Self:
        try:
            annotations = typing.get_type_hints(cls)
        except NameError:
            raise CantFindTypeException()
        
        for attribute in annotations:
            annotation = annotations[attribute]
            if attribute not in json:
                origin = typing.get_origin(annotation)
                if (cls._castValue(annotation, None) is not INVALID
                    or origin is Deprecated
                ):
                    json[attribute] = None
                    continue

                raise MissingAttributeException(attribute)
            
            value = json[attribute]
            castValue = cls._castValue(annotation, value)
            if castValue is INVALID:
                raise InvalidAttributeTypeException(annotation, value)
            json[attribute] = castValue

        return cls(**json)

    
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
                    return annotation.deserialize(value)
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
            
        elif origin is Literal:
            if value not in args:
                return INVALID
            return value
        
        elif origin is Union or origin is types.UnionType:
            castValue = [cls._castValue(a, value) for a in args]
            for cv in castValue:
                if cv is not INVALID:
                    return cv
            return INVALID
        
        elif origin is Deprecated:
            return cls._castValue(args[0], value) 
        
        raise UnsupportedTypeException(annotation)