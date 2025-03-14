from Unit import Unit
from Value import Value  # Import inside this module

CONVERSIONS = {
    "N": Value(1, Unit({"N": 1, "kg": -1, "m": -1, "s": 2})),
    "J": Value(1, Unit({"J": 1, "N": -1, "m": -1})),
    "g": Value(1000, Unit({"g": 1, "kg": -1})), 
    "mL": Value(1000, Unit({"mL": 1, "L": -1})), 
    "cL": Value(100, Unit({"cL": 1, "L": -1})),
    "dL": Value(10, Unit({"dL": 1, "L": -1})),
    "km": Value(1000, Unit({"km": 1, "m": -1})),
    "mm": Value(1000, Unit({"mm": 1, "m": -1})),
    "cm": Value(100, Unit({"cm": 1, "m": -1})),
    "dm": Value(10, Unit({"dm": 1, "m": -1})),
}
