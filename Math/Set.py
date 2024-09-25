from dataclasses import dataclass
from itertools import chain, combinations
from .UniversalSet import *
from math import sqrt

def Potenzmenge(Set: set) -> list[set]:
    return list(map(set, chain.from_iterable(combinations(Set, r) for r in range(len(Set) + 1))))

def getDividors(value: int) -> set[int]:
    result = set()
    for i in range(1, int(sqrt(value))):
        if value % i == 0:
            result.add(i)
            result.add(int(value / i))
    return result

class Range():
    start: float
    end: float
    includeStart: bool
    includeEnd: bool
    StartInfinite: bool
    EndInfinite: bool

    def contains(self, value: float) -> bool:
        result: bool = True
        if not self.StartInfinite:
            if self.includeStart:
                result &= value >= self.start
            else:
                result &= value > self.start
        if not self.EndInfinite:
            if self.includeEnd:
                result &= value <= self.end
            else:
                result &= value < self.end
        
        return result
        
    def __init__(self, Expression: str):
        if Expression[0] == "]":
            self.includeStart = False
        elif Expression[0] == "[":
            self.includeStart = True
        else:
            raise ValueError("Invalid Expression")
        
        if Expression[len(Expression)-1] == "]":
            self.includeEnd = True
        elif Expression[len(Expression)-1] == "[":
            self.includeEnd = False

        Expression = Expression[1:len(Expression) - 1]

        Values = Expression.split(",")
        if Values[0] == "-inf":
            self.StartInfinite = True
        else:
            self.StartInfinite = False
            self.start = float(Values[0])
        if Values[1] == "inf":
            self.EndInfinite = True
        else:
            self.EndInfinite = False
            self.end = float(Values[1])
    
    def __str__(self) -> str:
        result: str = ""
        if self.includeStart:
            result += "["
        else:
            result += "]"
        if self.StartInfinite:
            result += "-inf"
        else:
            result += str(self.start)
        result += ","
        if self.EndInfinite:
            result += "inf"
        else:
            result += str(self.end)
        if self.includeEnd:
            result += "]"
        else:
            result += "["
        return result