from Measures import *

mass = 10 * kg
acceleration = gE
force = mass * acceleration
print(f"{force = }")  # Output: "98.10 kg*m/s²"

distance = 5 * meter
energy = force * distance
print(f"{energy = }")  # Output: "490.50 kg*m²/s²" (Joule)

distance = 1000000 * meter
velocity = distance / 5 * sec
velocity.displayConversion.append("km")
print(f"{velocity = }")