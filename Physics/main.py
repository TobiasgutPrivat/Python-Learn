from Distance import Distance
from Acceleration import Acceleration

# Example usage
d = Distance((10, 0, 0))  # Vector Distance
a = Acceleration((2, 0, 0))  # Vector Acceleration
f = d * a  # Force calculation

print(f)  # Force((20, 0, 0))
print(type(f))  # <class '__main__.Force'>
print(f.magnitude())  # 20.0