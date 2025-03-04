from Unit import Unit

class Value:
    def __init__(self, value, unit=None):
        self.value = value
        self.unit = unit or Unit()

    def __mul__(self, other):
        if isinstance(other, Value):
            return Value(self.value * other.value, self.unit * other.unit)
        return Value(self.value * other, self.unit)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Value):
            return Value(self.value / other.value, self.unit / other.unit)
        return Value(self.value / other, self.unit)
    
    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __add__(self, other):
        if not isinstance(other, Value):
            raise TypeError("Can only add Values")
        if self.unit != other.unit:
            raise ValueError(f"Units must match: {self.unit} vs {other.unit}")
        return Value(self.value + other.value, self.unit)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if not isinstance(other, Value):
            raise TypeError("Can only subtract Values")
        if self.unit != other.unit:
            raise ValueError(f"Units must match: {self.unit} vs {other.unit}")
        return Value(self.value - other.value, self.unit)
    
    def __rsub__(self, other):
        return self.__sub__(other)

    def __str__(self):
        return f"{self.value:.2f} {self.unit}"
    
    def __repr__(self):
        return self.__str__()
