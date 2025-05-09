class Cell:
    '''
    A cell in the sudoku board
    '''
    possibleValues: list[int]

    def __init__(self, possibleValues: list[int]):
        self.possibleValues = possibleValues
    
    def removePossibility(self, value: int):
        if value in self.possibleValues:
            self.possibleValues.remove(value)

    def get_Value(self):
        if len(self.possibleValues) == 1:
            return self.possibleValues[0]
        return None