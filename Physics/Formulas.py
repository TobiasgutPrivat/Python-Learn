from Unit import Unit

class Formula:
    # derived = value * unit
    derived: str
    value: float
    units: Unit
    def __init__(self, derived, value, units=None):
        self.derived = derived
        self.value = value
        self.units = units or Unit()

    def weight(self):
        return sum(abs(exp) for exp in self.units.values())
    
DerivedUnits = [ # value must be equal to 1 in physics-theory
    #Formulas
    Formula("N", 1, Unit({"kg": 1, "m": 1, "s": -2})),
    Formula("J",1, Unit({"kg": 1, "m": 2, "s": -2})),
]

DerivedUnits.sort(key=lambda x: -x.weight())

UnitConversion = [
    Formula("g", 1000, Unit({"kg": 1})), 
    Formula("mL", 1000, Unit({"L": 1})), 
    Formula("cL", 100, Unit({"L": 1})),
    Formula("dL", 10, Unit({"L": 1})),
    Formula("km", 1000, Unit({"m": 1})),
    Formula("mm", 1000, Unit({"m": 1})),
    Formula("cm", 100, Unit({"m": 1})),
    Formula("dm", 10, Unit({"m": 1})),
]
