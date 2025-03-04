from Units import UnitList

class Value:
    value: float
    mulUnits: UnitList
    divUnits: UnitList

    def __init__(self, value, mulUnits: UnitList | list[str] | str = [], divUnits: UnitList | list[str] | str = []):
        self.value = value

        if not isinstance(mulUnits, UnitList):
            if isinstance(mulUnits, str):
                mulUnits = [mulUnits]
            else:
                mulUnits = UnitList(mulUnits)

        if not isinstance(divUnits, UnitList):
            if isinstance(divUnits, str):
                divUnits = [divUnits]
            else:
                divUnits = UnitList(divUnits)

        self.mulUnits = UnitList(mulUnits)
        self.divUnits = UnitList(divUnits)
        
    def __mul__(self, other):
        if isinstance(other, Value):
            return Value(self.value * other.value, self.mulUnits + other.mulUnits, self.divUnits + other.divUnits)
        elif isinstance(other, int) or isinstance(other, float):
            return Value(self.value * other, self.mulUnits, self.divUnits)
        else:
            raise TypeError(f"Unsupported type: {type(other)}")
        
    def __truediv__(self, other):
        if isinstance(other, Value):
            return Value(self.value / other.value, self.mulUnits + other.divUnits, self.divUnits + other.mulUnits)
        elif isinstance(other, int) or isinstance(other, float):
            return Value(self.value / other, self.mulUnits, self.divUnits)
        else:
            raise TypeError(f"Unsupported type: {type(other)}")

    def __add__(self, other):
        if not isinstance(other, Value):
            raise TypeError(f"Unsupported type: {type(other)}")
        
        if self.mulUnits != other.mulUnits or self.divUnits != other.divUnits:
            raise ValueError("Units must be the same")
        
        return Value(self.value + other.value, self.mulUnits, self.divUnits)

    def __str__(self):
        return f"{self.value} ({self.mulUnits})/({self.divUnits})"