class Cell:
    '''
    A cell in the sudoku board
    '''
    value: int | None
    possibleValues: list[int]
    inGroups: list['Group']

    def __init__(self, possibleValues: list[int]):
        self.possibleValues = possibleValues
        self.inGroups = []
        self.value = None
    
    def removePossibility(self, value: int):
        if value in self.possibleValues:
            self.possibleValues.remove(value)

    def get_Value(self):
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
    
    def reserveInGroups(self):
        '''
        Reserve a value in all groups the cell is in.
        '''
        if len(self.possibleValues) == 1:
            value = self.possibleValues[0]
            for group in self.inGroups:
                group.reserveValue(value)

    def __repr__(self):
        return f"Cell({self.get_Value() or self.possibleValues})"