from math import sqrt
import itertools
from typing import Callable

def Potenzmenge(Set: set) -> list[set]:
    return list(map(set, itertools.chain.from_iterable(itertools.combinations(Set, r) for r in range(len(Set) + 1))))

def evaluateList(func: Callable[[list, int], int], X: list) -> list:
    for i in range(len(X),10):
        X.append(func(X,i))
    return X

def KartesischesProdukt(*sets):
    return list(itertools.product(*sets))

def getDividors(value: int) -> set[int]:
    result = set()
    for i in range(1, int(sqrt(value))+1):
        if value % i == 0:
            result.add(i)
            result.add(int(value / i))
            result.add(-i)
            result.add(-int(value / i))
    return result

def gT(a: int, b: int) -> set[int]:
    return getDividors(a).intersection(getDividors(b))

def isPrime(value: int) -> bool:
    return len(getDividors(value)) == 4

def quersumme(value: int) -> int:
    result = 0
    while value > 0:
        result += value % 10
        value //= 10
    return result

def PrimeSepration(value: int) -> list[int]:
    if value % 2 == 0:
        set = PrimeSepration(int(value / 2))
        set.append(2)
        return set
    elif quersumme(value) % 3 == 0:
        set = PrimeSepration(int(value / 3))
        set.append(3)
        return set
    elif int(value.__str__()[len(value.__str__()) - 1]) == 5:
        set = PrimeSepration(int(value / 5))
        set.append(5)
        return set
    elif int(value.__str__()[len(value.__str__()) - 1]) == 0:
        set = PrimeSepration(int(value / 10))
        set.append(10)
        return set
    else:
        dividors = getDividors(value)
        dividors = dividors.difference({1, value,-1,-value})
        dividors = {x for x in dividors if x >= 0}
        if not len(dividors) == 0:
            dividor = min(dividors)
            set = PrimeSepration(int(value / dividor))
            set.append(dividor)
            return set
        return [value]


def ggt(a: int, b: int) -> int:
    # return max(gT(a,b))
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    if a > b:
        return ggt(b, a)
    else:
        return ggt(a, b-a)