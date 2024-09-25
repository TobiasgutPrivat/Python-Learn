from Math.Set import Set

A = {1,2,3,4}
B = {0,1,2}

C = A ^ B

print(A)
print(B)
print(C)
print(len(C))
print(C.isdisjoint(A & B))