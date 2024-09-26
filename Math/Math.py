from math import sqrt
from itertools import chain, combinations

def Potenzmenge(Set: set) -> list[set]:
    return list(map(set, chain.from_iterable(combinations(Set, r) for r in range(len(Set) + 1))))

def getDividors(value: int) -> set[int]:
    result = set()
    for i in range(1, int(sqrt(value))):
        if value % i == 0:
            result.add(i)
            result.add(int(value / i))
    return result

def gT(a: int, b: int) -> set[int]:
    return getDividors(a).intersection(getDividors(b))


def ggt(a: int, b: int) -> int:
    # return max(gT(a,b))
    if a == 0:
        return b
    if a > b:
        return ggt(b, a)
    else:
        return ggt(a, b-a)