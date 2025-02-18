import math

def AircraftDistance(Plane1x, Plane1y, Plane2x, Plane2y):
    return math.sqrt((Plane1x - Plane2x) ** 2 + (Plane1y - Plane2y) ** 2)


Plane1x = int(input("Enter the x coordinate of Plane 1: "))
Plane1y = int(input("Enter the y coordinate of Plane 1: "))

Plane2x = int(input("Enter the x coordinate of Plane 2: "))
Plane2y = int(input("Enter the y coordinate of Plane 2: "))

print("Distance between Plane 1 and Plane 2: ", AircraftDistance(Plane1x, Plane1y, Plane2x, Plane2y))
