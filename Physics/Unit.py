class Unit(dict):
    def __init__(self, units=None):
        """Initialize a unit system as a dictionary of unit exponents."""
        super().__init__(units or {})

    def __mul__(self, other):
        if not isinstance(other, Unit):
            raise TypeError("Can only multiply Units")
        # Combine the units from both instances
        new_units = self.copy()
        for unit, exp in other.items():
            new_units[unit] = new_units.get(unit, 0) + exp
        return Unit(new_units)

    def __truediv__(self, other):
        if not isinstance(other, Unit):
            raise TypeError("Can only divide Units")
        # Subtract exponents when dividing units
        new_units = self.copy()
        for unit, exp in other.items():
            new_units[unit] = new_units.get(unit, 0) - exp
        return Unit(new_units)

    def __eq__(self, other):
        if not isinstance(other, Unit):
            return False
        return dict(self) == dict(other)  # Ensure the comparison works between dict-like objects

    def __str__(self):
        """Return a human-readable unit string."""
        return " * ".join(
            f"{unit}^{exp}" if exp != 1 else unit
            for unit, exp in sorted(self.items()) if exp != 0
        ) or "1"
