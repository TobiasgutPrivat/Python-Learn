from Unit import Unit, BaseUnits
from Formulas import DerivedUnits, UnitConversion, Formula

class Value:
    value: float
    unit: Unit
    displayConversion: list[str] = []

    def __init__(self, value, unit=None):
        self.value = value
        self.unit = Unit(unit or {})
        self.makeBase()

    def makeBase(self):
        # use base units if possible
        for unit in self.unit.keys():
            if unit not in BaseUnits:
                if derived := dict((formula.derived, formula) for formula in DerivedUnits)[unit]:
                    self /= derived
                elif conversion := dict((formula.derived, formula) for formula in UnitConversion)[unit]:
                    self /= conversion
                else:
                    raise ValueError(f"Not a base unit: {unit}")

    def __imul__(self, other):
        if isinstance(other, Formula):
            self.value /= other.value
            self.unit /= other.units
            self.unit[other.derived] += 1
        else:
            raise NotImplementedError("Can only assign-multiply by Formulas")
        
    def __itruediv__(self, other):
        if isinstance(other, Formula):
            self.value *= other.value
            self.unit *= other.units
            self.unit[other.derived] -= 1
        else:
            raise NotImplementedError("Can only assign-divide by Formulas")

    def __mul__(self, other):
        if isinstance(other, Value):
            return Value(self.value * other.value, self.unit * other.unit)
        elif isinstance(other, (int, float)):
            return Value(self.value * other, self.unit)
        else:
            raise NotImplementedError("Can only multiply by Values, ints, and floats")
    
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
        displayValue = self.value
        displayUnit = self.unit
        for formula in DerivedUnits:
            if displayUnit.contains(formula.units):
                displayValue /= formula.value
                displayUnit = (displayUnit / formula.units)
                displayUnit[formula.derived] = 1
                break

        for formula in UnitConversion:
            if formula.derived in self.displayConversion and displayUnit.contains(formula.units):
                displayValue /= formula.value
                displayUnit = (displayUnit / formula.units)
                displayUnit[formula.derived] = 1
                
        return f"{displayValue:.2f} {displayUnit}"
    
    def __repr__(self):
        return self.__str__()