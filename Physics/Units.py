Units = {
    "M": "Mass in kg",
    "T": "Time in s",
    "F": "Force in N",
    "V": "Velocity in m/s",
    "A": "Acceleration in m/s^2",
    "E": "Energy in J",
    "P": "Power in W",
    "W": "Work in J",
    "L": "Length in m",
    "I": "Current in A",
}

class UnitList(list[str]):
    def __init__(self, units: list[str] = []):
        for unit in units: 
            self.append(unit)

    def append(self, unit):
        self.checkUnit(unit)
        super().append(unit)

    def __setItem__(self, index, unit):
        self.checkUnit(unit)
        super().__setitem__(index, unit)
        
    def checkUnit(self, unit):
        if unit not in Units:
            raise ValueError(f"Invalid unit: {unit}")
        
    def __eq__(self, value):
        if not isinstance(value, UnitList):
            raise TypeError(f"Unsupported type: {type(value)}")
        
        return sorted(self) == sorted(value)


    def __str__(self):
        return "*".join(self) if self else "1"

