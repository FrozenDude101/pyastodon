from typing import Any


class Model:

    @classmethod
    def deserialize(cls, json: Any) -> Any:
        raise NotImplementedError()