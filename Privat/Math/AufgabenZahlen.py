from MathLib.Math import *

print("Aufgabe 9a")
def next9a(X: list, n: int) -> int:
    return X[n-1] + X[n-2]

print(evaluateList(next9a,[1,1]))

print("\nAufgabe 9b")
def next9b(X: list, n: int) -> int:
    return X[n-1] * (n + 1)
print(evaluateList(next9b,[1]))

print("\nAufgabe 9c")
def next9c(X: list, n: int) -> int:
    previous = X[n-1]
    if previous == 1:
        return 1
    elif previous % 2 == 0:
        return previous / 2
    else:
        return 3 * previous + 1

print(evaluateList(next9c,[3]))