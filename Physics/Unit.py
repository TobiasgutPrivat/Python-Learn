BaseUnits = [ # from ISO
    "m", # Length in meters
    "kg", # Mass in kilograms
    "s", # Time in seconds
    "A", # Electric current in amperes
    "K", # Temperature in Kelvin
    "L", # Volume in liters
    "mol", # Amount of substance in moles
    "cd", # Luminous intensity in candela
    "rad" # Angle in radians
]

class Unit(dict):
    def __init__(self, units: dict = {}):
        """Initialize a unit system as a dictionary of unit exponents."""
        super().__init__(units)

    def __mul__(self, other):
        if not isinstance(other, Unit):
            raise TypeError("Can only multiply Units")
        
        new_units = self.copy()
        for unit, exp in other.items():
            new_units[unit] = new_units.get(unit, 0) + exp
        return Unit(new_units)

    def __truediv__(self, other):
        if not isinstance(other, Unit):
            raise TypeError("Can only divide Units")
        
        new_units = self.copy()
        for unit, exp in other.items():
            new_units[unit] = new_units.get(unit, 0) - exp
        return Unit(new_units)

    def __eq__(self, other):
        if not isinstance(other, Unit):
            return False
        return dict(self) == dict(other)  # Ensure the comparison works between dict-like objects

    def __str__(self):
        """Return a human-readable unit string, with fractional representation for negative exponents."""
        num_units = []
        denom_units = []

        for unit, exp in sorted(self.items()):
            if exp > 0:
                num_units.append(f"{unit}^{exp}" if exp != 1 else unit)
            elif exp < 0:
                denom_units.append(f"{unit}^{-exp}" if exp != -1 else unit)

        num_part = " * ".join(num_units) or "1"
        denom_part = " * ".join(denom_units) or "1"

        if denom_part != "1":
            return f"{num_part} / {denom_part}"
        return num_part
    
    def contains(self, unit: 'Unit'):
        for unit, exp in unit.items():
            if unit not in self:
                return False
            if abs(self[unit]) < abs(exp) or exp * self[unit] < 0:
                return False
        return True

    def invert(self):
        return Unit({unit: -exp for unit, exp in self.items()})
