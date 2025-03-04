from abc import ABC

class Unit(ABC):
    """Base class for all physical unit types, supporting scalar and vector operations."""
    value: float | tuple[float, ...]

    def __init__(self, value: float | tuple[float, ...]):
        self.value = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value})"
