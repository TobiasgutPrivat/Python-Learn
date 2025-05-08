import math

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
            
class FullGroup:
    '''
    A Group of cells containg all values once
    '''
    values: list[int]
    cells: list[Cell]
    possibleValuePositions: dict[int,list]

    def __init__(self, cells: list[Cell], values: list[int]):
        self.cells = cells
        self.values = values
    
class Sudoku:
    '''
    A sudoku board
    '''
    size: int
    values: list[int]
    board: list[list[Cell]]
    groups: list[FullGroup]

    def __init__(self, size: int = 9):
        if math.sqrt(size) % 1 != 0:
            raise ValueError("Size must be a perfect square")
        
        self.size = size
        self.values = [i for i in range(1, size + 1)]

        self.board = [[Cell(self.values.copy()) for _ in range(size)] for _ in range(size)]

        self.groups = [FullGroup(row,self.values) for row in self.board]
        self.groups += [FullGroup([self.board[i][j] for i in range(size)],self.values) for j in range(size)]
        self.groups += [FullGroup([self.board[i][j] for i in range(x, x + int(math.sqrt(size))) for j in range(y, y + int(math.sqrt(size)))],self.values) for x in range(0, size, int(math.sqrt(size))) for y in range(0, size, int(math.sqrt(size)))]

    def set_Cell(self, x, y, value):
        self.board[x][y].possibleValues = [value]

    def print(self):
        for row in self.board:
            print(" ".join([str(cell.get_Value() or "-") for cell in row]))
        print()
        print("Groups:")
        for group in self.groups:
            print(" ".join([str(cell.get_Value() or "-") for cell in group.cells]))

if __name__ == "__main__":
    sudoku = Sudoku(9)
    sudoku.set_Cell(0, 0, 5)
    sudoku.set_Cell(1, 1, 3)
    sudoku.set_Cell(2, 2, 4)
    sudoku.print()