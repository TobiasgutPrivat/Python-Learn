# ISO Unit Names
Units = {
    "M": "kg",  # Mass in kilograms
    "T": "s",   # Time in seconds
    "F": "N",   # Force in Newtons
    "V": "m/s",  # Velocity
    "A": "m/s^2",  # Acceleration
    "E": "J",   # Energy in Joules
    "P": "W",   # Power in Watts
    "W": "J",   # Work in Joules
    "L": "m",   # Length in meters
    "I": "A",   # Current in Amperes
}

class UnitList(list[str]):
    def __init__(self, units: list[str] = []):
        super().__init__(units)

    def append(self, unit):
        self.checkUnit(unit)
        super().append(unit)

    def __setitem__(self, index, unit):
        self.checkUnit(unit)
        super().__setitem__(index, unit)
        
    def checkUnit(self, unit):
        if unit not in Units:
            raise ValueError(f"Invalid unit: {unit}")
        
    def __eq__(self, value):
        if not isinstance(value, UnitList):
            raise TypeError(f"Unsupported type: {type(value)}")
        return sorted(self) == sorted(value)

    def formatted(self):
        """Returns units in ISO format with exponents (e.g., 's²' instead of 's*s')."""
        unit_counts = {}
        for unit in self:
            unit_counts[unit] = unit_counts.get(unit, 0) + 1

        return "*".join(f"{Units[unit]}{f'^{count}' if count > 1 else ''}" for unit, count in sorted(unit_counts.items()))

    def __str__(self):
        return self.formatted() if self else "1"