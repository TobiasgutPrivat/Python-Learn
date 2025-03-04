from Measures import *
from Formulas import Formulas

mass = 10 * kg
acceleration = gE
force = mass * acceleration
print(f"{force = }")  # Output: "98.10 kg*m/s²"

distance = 5 * meter
energy = force * distance * Formulas[2] 
print(f"{energy= }")  # Output: "490.50 kg*m²/s²" (Joule)

time = Value(2, Unit({"s": 1}))
power = energy / time
print(f"{power = }")  # Output: "245.25 kg*m²/s³" (Watt)
