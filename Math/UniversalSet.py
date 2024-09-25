from abc import abstractmethod
class UniversalSet:
    @abstractmethod
    def contains(self, value: float) -> bool:
        pass

    @abstractmethod
    def getfirst(self) -> float:
        pass

    @abstractmethod
    def next(self, value: float) -> float:
        pass
    
    @abstractmethod
    def fromRange(self, range: range) -> set[float]:
        pass

    def getIndex(self, index: int) -> float:
        if not Naturals0().contains(index):
            raise ValueError("Index not in Naturals0.")
        result = self.getfirst()
        for i in range(1, index):
            result = self.next(result)
        return result
    
    def getSample(self, amount: int) -> set[float]:
        result = set()
        current = self.getfirst()
        for i in range(1, amount+1):
            result.add(current)
            current = self.next(current)
        return result
                

class Naturals(UniversalSet):
    def contains(self, value: float) -> bool:
        if value > 0 and value.is_integer():
            return True
        return False
    
    def getfirst(self) -> float:
        return 1
    
    def next(self, value: float) -> float:
        return value + 1
    
    def fromRange(self, range: range) -> set[float]:
        result = set()
        current: float
        if range.start > self.getfirst():
            current = range.start
        else:
            current = self.getfirst()

        while current <= range.stop:
            result.add(current)
            current = self.next(current)
        return result
    
class Naturals0(Naturals):
    def contains(self, value: float) -> bool:
        if value >= 0 and value.is_integer():
            return True
        return False
    def getfirst(self) -> float:
        return 0
    
class Integeres(UniversalSet):
    def contains(self, value: float) -> bool:
        if value.is_integer():
            return True
        return False
    
    def getfirst(self) -> float:
        return 0
    
    def next(self, value: float) -> float:
        if value == 0:
            return 1
        if value >= 0:
            return -value
        else:
            return -value + 1
        
    def fromRange(self, range: range) -> set[float]:
        result = set()
        current: float = range.start

        while current <= range.stop:
            result.add(current)
            current = self.next(current)
        return result
    
    

            