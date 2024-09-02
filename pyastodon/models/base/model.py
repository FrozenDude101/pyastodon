from typing import Any


class Model:

    @classmethod
    def deserialize(cls, value: Any) -> Any:
        raise NotImplementedError()