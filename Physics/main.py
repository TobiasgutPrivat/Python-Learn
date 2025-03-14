from PhysicalObject import PhysicalObject
from Measures import *

# Create a new physical object
obj = PhysicalObject("Object")

# Define properties
obj.set_property("m", 10 * kg)  # Mass = 10kg
obj.set_property("a", 2 * meter / sec ** 2)   # Acceleration = 2m/s²

# System automatically calculates Force (F = m * a)
print(obj)

# Introduce a conflict
obj.set_property("m", 25 * kg)  # Manually override force
print(obj)

# Define a new property
obj.set_property("A", 5 * meter ** 2)  # Area = 5m²

# System calculates pressure (p = F / A)
print(obj)
