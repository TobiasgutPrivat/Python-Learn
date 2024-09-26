from Range import Range
from Math import *

A = {1,2,3,4,8,9}
B = set([0,1,2])

C = A ^ B

print(A)
print(B)
print(C)

print(Potenzmenge(A).__len__())

print(Range("]-inf,43[").contains(-43))