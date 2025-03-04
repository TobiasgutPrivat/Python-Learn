from Vector import Vector
from Acceleration import Acceleration
from Force import Force

class Distance(Vector):
    """Represents a distance in meters."""

    def __mul__(self, other: 'Acceleration') -> 'Force':
        if isinstance(other, Acceleration):
            if isinstance(self.value, tuple) and isinstance(other.value, tuple):
                return Force(tuple(a * b for a, b in zip(self.value, other.value)))
            return Force(self.value * other.value)
        return NotImplemented