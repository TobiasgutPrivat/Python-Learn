from typing import Union

class Vec3:
    x: float
    y: float
    z: float

    def __init__(self, value: Union[int, float, tuple, 'Vec3']):
        if isinstance(value, (int, float)):  # Single number
            self.x, self.y, self.z = value, 0, 0
        elif isinstance(value, tuple) and len(value) == 2:  # Tuple of 2
            self.x, self.y, self.z = value[0], value[1], 0
        elif isinstance(value, tuple) and len(value) == 3:  # Tuple of 3
            self.x, self.y, self.z = value
        elif isinstance(value, Vec3):  # Already Vec3
            self.x, self.y, self.z = value.x, value.y, value.z
        else:
            raise ValueError("Unsupported type for Vec3")

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y and self.z == value.z
    
    def __add__(self, value):
        if isinstance(value, Vec3):
            return Vec3((self.x + value.x, self.y + value.y, self.z + value.z))
        else:
            raise ValueError("Unsupported type for Vec3 addition")
        
    def __sub__(self, value):
        if isinstance(value, Vec3):
            return Vec3((self.x - value.x, self.y - value.y, self.z - value.z))
        else:
            raise ValueError("Unsupported type for Vec3 subtraction")
        
    def __mul__(self, value):
        if isinstance(value, float):
            return Vec3((self.x * value, self.y * value, self.z * value))
        else:
            raise ValueError("Unsupported type for Vec3 multiplication")
        
    def cross(self, value: 'Vec3'):
        return Vec3((self.y * value.z - self.z * value.y, self.z * value.x - self.x * value.z, self.x * value.y - self.y * value.x))
    
    def dot(self, value: 'Vec3'):
        return self.x * value.x + self.y * value.y + self.z * value.z
    
    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5