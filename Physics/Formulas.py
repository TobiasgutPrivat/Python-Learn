from Value import Value
from Unit import Unit

Formulas = [ # value must be equal to 1 in physics-theory
    #conversion
    Value(1000, Unit({"kg": -1, "g": 1})), 
    Value(1000, Unit({"km": -1, "m": 1})), 
    Value(1000, Unit({"L": -1, "mL": 1})), 
    Value(100, Unit({"L": -1, "cL": 1})),
    Value(10, Unit({"L": -1, "dL": 1})),
    Value(1000, Unit({"m": -1, "mm": 1})),
    Value(100, Unit({"m": -1, "cm": 1})),
    Value(10, Unit({"m": -1, "dm": 1})),

    #Formulas
    Value(1, Unit({"m/s": 1, "s": -1, "m": -1})), # 1 = 1m/s
    Value(1, Unit({"m/s^2": 1, "s": -1, "m/s": -1})), # 1 = 1m/s
    Value(1, Unit({"N": 1, "kg": -1, "m/s^2": -1})), # 1 = N*s²/kg*m
    Value(1, Unit({"J": 1, "N": -1, "m": -1})), # 1 = J/N*m
]