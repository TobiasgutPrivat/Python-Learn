from Range import Range
from Math import *

A = {1,2,3,4,8,9}
B = {1,2}
C = {1,2}

def next(X: list, n: int) -> int:
    previous = X[n-1]
    if previous == 1:
        return 1
    elif previous % 2 == 0:
        return previous / 2
    else:
        return 3 * previous + 1

print(evaluateList(next,[3]))
# C = A ^ B

# print(A)
# print(B)
# print(C)

# print(Potenzmenge(A).__len__())

# print(Range("]-inf,43[").contains(-43))