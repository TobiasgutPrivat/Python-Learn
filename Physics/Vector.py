from Unit import Unit

class Vector(Unit):
    """A class to handle vector operations like dot and cross product."""
    value: tuple[float, ...]

    def __init__(self, value: tuple[float, ...]):
        super().__init__(value)
    
    def __add__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            if len(self.value) != len(other.value):
                raise ValueError("Vectors must be the same dimension for addition.")
            return Vector(tuple(a + b for a, b in zip(self.value, other.value)))
        return NotImplemented

    def __sub__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            if len(self.value) != len(other.value):
                raise ValueError("Vectors must be the same dimension for subtraction.")
            return Vector(tuple(a - b for a, b in zip(self.value, other.value)))
        return NotImplemented

    def dot(self, other: 'Vector') -> float:
        """Returns the dot product of two vectors."""
        if isinstance(other, Vector) and len(self.value) == len(other.value):
            return sum(a * b for a, b in zip(self.value, other.value))
        raise ValueError("Vectors must be of the same dimension for dot product.")

    def cross(self, other: 'Vector') -> 'Vector':
        """Returns the cross product (only for 3D vectors)."""
        if isinstance(other, Vector) and len(self.value) == 3 and len(other.value) == 3:
            x1, y1, z1 = self.value
            x2, y2, z2 = other.value
            return Vector((
                y1 * z2 - z1 * y2,
                z1 * x2 - x1 * z2,
                x1 * y2 - y1 * x2
            ))
        raise ValueError("Cross product is only defined for 3D vectors.")
    
    def magnitude(self) -> float:
        return sum(a ** 2 for a in self.value) ** 0.5