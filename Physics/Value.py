from Unit import Unit
from Vec3 import Vec3

class Value:
    value: float | Vec3
    units: Unit

    def __init__(self, value: float | Vec3, unit: dict[str, int] | None = None):
        self.value = value
        self.units = Unit(unit or {})

    def format(self, displayUnits: dict[str, int] = {}):
        """Convert Value to excact display units and base units."""
        from Conversions import CONVERSIONS
        
        displayUnits = Unit(displayUnits)
        diff = (self.units / displayUnits).nonBaseUnits()

        while diff:
            for unit, exp in diff.items():
                if not CONVERSIONS.get(unit):
                    print(f"No conversion for: {unit}")
                    displayUnits[unit] = displayUnits.get(unit, 0) + exp # Add to display units if not convertable
                    continue
                
                self /= CONVERSIONS[unit] ** exp
            diff = (self.units / displayUnits).nonBaseUnits()

    def __mul__(self, other):
        if isinstance(other, Value):
            return Value(self.value * other.value, self.units * other.units)
        elif isinstance(other, (int, float)):
            return Value(self.value * other, self.units)
        else:
            raise NotImplementedError("Can only multiply by Values, ints, and floats")
        
    def __imul__(self, other):
        if isinstance(other, Value):
            self.value *= other.value
            self.units *= other.units
        else:
            self.value *= other
        return self
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Value):
            return Value(self.value / other.value, self.units / other.units)
        return Value(self.value / other, self.units)
    
    def __itruediv__(self, other):
        if isinstance(other, Value):
            self.value /= other.value
            self.units /= other.units
        else:
            self.value /= other
        return self
    
    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __add__(self, other):
        if not isinstance(other, Value):
            raise TypeError("Can only add Values")
        if self.units != other.units:
            raise ValueError(f"Units must match: {self.units} vs {other.units}")
        return Value(self.value + other.value, self.units)
        
    def __iadd__(self, other):
        if not isinstance(other, Value):
            raise TypeError("Can only add Values")
        if self.units != other.units:
            raise ValueError(f"Units must match: {self.units} vs {other.units}")
        self.value += other.value
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if not isinstance(other, Value):
            raise TypeError("Can only subtract Values")
        if self.units != other.units:
            raise ValueError(f"Units must match: {self.units} vs {other.units}")
        return Value(self.value - other.value, self.units)
    
    def __isub__(self, other):
        if not isinstance(other, Value):
            raise TypeError("Can only subtract Values")
        if self.units != other.units:
            raise ValueError(f"Units must match: {self.units} vs {other.units}")
        self.value -= other.value
    
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __pow__(self, other):
        if isinstance(other, int):
            return Value(self.value ** other, self.units ** other)
        else:
            raise NotImplementedError("Can only raise to ints")
        
    def __str__(self):
        return f"{self.value:.2f} {self.units}"
    
    def __repr__(self):
        return self.__str__()
    
