import math

class Cell:
    '''
    A cell in the sudoku board
    '''
    maxValue: int 
    possibleValues: list[int]

    def __init__(self, maxValue: int):
        self.maxValue
        self.possibleValues = [i for i in range(1, maxValue + 1)] # 1 to maxValue inclusive
    
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
    values: list
    cells: list[Cell]
    possibleValuePositions: dict[int,list]
    def __init__(self, cells: list[Cell], values):
        self.cells = cells
    
class Sudoku:
    '''
    A sudoku board
    '''
    size: int
    board: list[list[Cell]]
    groups: list[FullGroup]

    def __init__(self, size: int = 9):
        if math.sqrt(size) % 1 != 0:
            raise ValueError("Size must be a perfect square")
        
        self.size = size
        self.board = [[Cell(size) for _ in range(size)] for _ in range(size)]
        self.groups = [FullGroup(row) for row in self.board] # Placeholder for groups
        self.groups += [FullGroup([self.board[i][j] for i in range(size)]) for j in range(size)]
        self.groups += [FullGroup([self.board[i][j] for i in range(x, x + int(math.sqrt(size))) for j in range(y, y + int(math.sqrt(size)))]) for x in range(0, size, int(math.sqrt(size))) for y in range(0, size, int(math.sqrt(size)))]

    def set_Cell(self, x, y, value):
        self.board[x][y].possibleValues = [value]

    def __str__(self):
        result = ""
        for row in self.board:
            result += " ".join(str(cell.get_Value()) if cell.get_Value() else "." for cell in row) + "\n"
        result += "\n"
        for group in self.groups:
            result += " ".join(str(cell.get_Value()) if cell.get_Value() else "." for cell in group.cells) + "\n"
        return result

if __name__ == "__main__":
    sudoku = Sudoku(9)
    sudoku.set_Cell(0, 0, 5)
    sudoku.set_Cell(1, 1, 3)
    sudoku.set_Cell(2, 2, 4)
    print(sudoku)