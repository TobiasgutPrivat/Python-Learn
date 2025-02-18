import math

i: int = 0
pi_inv: float = 0

while True:
    i += 1
    add = (math.factorial(4 * i) * (1103 + 26390 * i)) / (math.factorial(i) ** 4 * (396 ** (4 * i)))
    if add < 1e-15:
        break
    pi_inv += add
    print(f"{i}. added {add}, {pi_inv = }")

pi = 1 / (pi_inv * (2 * math.sqrt(2) / 9801))
print(f"Calculated value of pi: {pi}")