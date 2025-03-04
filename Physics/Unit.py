class Unit:
    def __init__(self, units=None):
        """Initialize a unit system as a dictionary of unit exponents."""
        self.units = units or {}

    def __mul__(self, other):
        if not isinstance(other, Unit):
            raise TypeError("Can only multiply Units")
        new_units = self.units.copy()
        for unit, exp in other.units.items():
            new_units[unit] = new_units.get(unit, 0) + exp
        return Unit(new_units)

    def __truediv__(self, other):
        if not isinstance(other, Unit):
            raise TypeError("Can only divide Units")
        new_units = self.units.copy()
        for unit, exp in other.units.items():
            new_units[unit] = new_units.get(unit, 0) - exp
        return Unit(new_units)

    def __eq__(self, other):
        if not isinstance(other, Unit):
            return False
        return self == other

    def __str__(self):
        """Return a human-readable unit string."""

        return " * ".join(
            f"{unit}^{exp}" if exp != 1 else unit
            for unit, exp in sorted(self.items()) if exp != 0
        ) or "1"
