from Measures import *

# Define values
mass = 10*kg  # 10 kg
acceleration = gE  # 9.81 m/s²

# Compute force: F = M * A
force = mass * acceleration  

print(force)  # Expected: "98.10 N" instead of "98.10 kg*m / s²"

# Compute energy: E = F * d
distance = 5*meter  # 5 m
energy = force * distance  

print(energy)  # Expected: "490.50 J" instead of "490.50 kg*m² / s²"

# Compute power: P = E / t
time = 2*sec  # 2 s 
power = energy / time  

print(power)  # Expected: "245.25 W" instead of "245.25 kg*m² / s³"
