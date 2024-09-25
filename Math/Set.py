from dataclasses import dataclass

@dataclass
class Set:
    elements: list

    def __init__(self, elements: list) -> None:
        self.elements = elements
        self.CleanDupes()
        self.Sort()

    def CleanDupes(self) -> None:
        result: list = []
        for x in self.elements:
            if x not in result:
                result.append(x)
        self.elements = result

    def Sort(self) -> None:
        self.elements.sort()

    def GetElements(self, max: int = -1) -> list:
        if max == -1:
            return self.elements.copy()
        return self.elements[:max]

    def Contains(self, x):
        return x in self.GetElements()

    def And(self, other: 'Set') -> 'Set':
        result: list = []
        for x in other.GetElements():
            if self.Contains(x):
                result.append(x)
        return Set(result)
    
    def Or(self, other: 'Set') -> 'Set':
        result: list = other.GetElements()
        result.extend(self.GetElements())
        return Set(result)
    
    def Xor(self, other: 'Set') -> 'Set':
        result: Set = self.Not(other)
        result.Or(other.Not(self))
        return result
    
    def Not(self,other: 'Set') -> 'Set':
        result = []
        for x in self.GetElements():
            if not other.Contains(x):
                result.append(x)
        return Set(result)
    
    def PowerSet(self) -> 'Set':
        result: list = []
        #TODO
        return Set(result)
    
    def cardinality(self) -> int:
        return self.GetElements().__len__()
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Set):
            return False
        self.Sort()
        value.Sort()
        return self.elements == value.elements
    
    def __str__(self) -> str:
        return '{' + ', '.join(map(str, self.elements)) + '}'