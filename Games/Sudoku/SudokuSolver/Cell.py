from typing import Callable

class Cell:
    '''
    A cell in the sudoku board
    '''
    value: int | None
    possibleValues: list[int]
    groups: list['Group'] # Groups the cell is in
    col: int
    row: int
    logger: Callable

    def __init__(self, possibleValues: list[int], col: int, row: int, logger: Callable = None):
        self.possibleValues = possibleValues
        self.groups = []
        self.value = None
        self.col = col
        self.row = row
        self.logger = logger
    
    def setValue(self, value: int):
        '''
        Set the value of the cell.
        '''
        if value not in self.possibleValues:
            raise ValueError(f"Value {value} is not possible for this cell")
        self.value = value
        for v in self.possibleValues:
            if v != value:
                self.removeValue(v)
        self.reserveInGroups()

    def getValue(self):
        if self.value is not None:
            return self.value
        if len(self.possibleValues) == 1:
            self.value = self.possibleValues[0]
            return self.value
        return None
    
    def removeValue(self, value: int):
        '''
        Remove a value possibility from the cell.
        '''
        if value in self.possibleValues:
            self.possibleValues.remove(value)
            self.reserveInGroups()
            for group in self.groups:
                group.removePossibility(value, self)
    
    def reserveInGroups(self):
        '''
        Reserve a value in all groups the cell is in.
        '''
        if len(self.possibleValues) == 1:
            value = self.getValue()
            if self.logger is not None:
                self.logger(f"Reserve Value {value} in Groups", [self], self.groups)
                
            for group in self.groups:
                group.reserveValue(value, [self])
                

    def __repr__(self):
        return f"Cell({self.getValue() or self.possibleValues})"