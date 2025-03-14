from Unit import Unit

class Conversion:
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
    Conversion("N", 1, Unit({"kg": 1, "m": 1, "s": -2})),
    Conversion("J",1, Unit({"kg": 1, "m": 2, "s": -2})),
]

DerivedUnits.sort(key=lambda x: -x.weight())

UnitConversion = [
    Conversion("g", 1000, Unit({"kg": 1})), 
    Conversion("mL", 1000, Unit({"L": 1})), 
    Conversion("cL", 100, Unit({"L": 1})),
    Conversion("dL", 10, Unit({"L": 1})),
    Conversion("km", 1000, Unit({"m": 1})),
    Conversion("mm", 1000, Unit({"m": 1})),
    Conversion("cm", 100, Unit({"m": 1})),
    Conversion("dm", 10, Unit({"m": 1})),
]
