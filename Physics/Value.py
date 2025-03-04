from Units import UnitList

class Value:
    value: float
    mulUnits: UnitList
    divUnits: UnitList

    def __init__(self, value, mulUnits=[] , divUnits=[]):
        """Initialize Value with simplified unit handling."""
        self.value = value
        self.mulUnits = self._to_unitlist(mulUnits)
        self.divUnits = self._to_unitlist(divUnits)
        self.simplify_units()

    def _to_unitlist(self, units):
        """Ensure input is always converted to a UnitList."""
        if isinstance(units, str):
            return UnitList([units])
        return UnitList(units)

    def simplify_units(self):
        """Remove common units from numerator and denominator."""
        common_units = set(self.mulUnits) & set(self.divUnits)
        for unit in common_units:
            self.mulUnits.remove(unit)
            self.divUnits.remove(unit)

    def __mul__(self, other):
        if isinstance(other, Value):
            return Value(self.value * other.value, self.mulUnits + other.mulUnits, self.divUnits + other.divUnits)
        elif isinstance(other, (int, float)):
            return Value(self.value * other, self.mulUnits, self.divUnits)
        else:
            raise TypeError(f"Unsupported type: {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Value):
            return Value(self.value / other.value, self.mulUnits + other.divUnits, self.divUnits + other.mulUnits)
        elif isinstance(other, (int, float)):
            return Value(self.value / other, self.mulUnits, self.divUnits)
        else:
            raise TypeError(f"Unsupported type: {type(other)}")

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __add__(self, other):
        if not isinstance(other, Value):
            raise TypeError(f"Unsupported type: {type(other)}")
        if self.mulUnits != other.mulUnits or self.divUnits != other.divUnits:
            raise ValueError("Units must be the same")
        return Value(self.value + other.value, self.mulUnits, self.divUnits)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Value):
            raise TypeError(f"Unsupported type: {type(other)}")
        if self.mulUnits != other.mulUnits or self.divUnits != other.divUnits:
            raise ValueError("Units must be the same")
        return Value(self.value - other.value, self.mulUnits, self.divUnits)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __str__(self):
        """Prettier string representation using ISO units."""
        mul_str = str(self.mulUnits)
        div_str = str(self.divUnits)

        if div_str != "1":
            return f"{self.value:.2f} {mul_str} / {div_str}"
        return f"{self.value:.2f} {mul_str}"