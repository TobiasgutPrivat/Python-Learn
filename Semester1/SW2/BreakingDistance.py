v0 = int(input("v0 [km/h]? ")) / 3.6
mu = 0.3
g = 9.81
d = 0.5*(v0**2)/(mu*g)
print(f"Breaking Distance: {round(d, 2)}m")