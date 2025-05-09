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

    def __init__(self, size: int = 9, board: list[list[int]] = None):
        if math.sqrt(size) % 1 != 0:
            raise ValueError("Size must be a perfect square")
        
        self.size = size
        self.values = [i for i in range(1, size + 1)]

        if board is None:
            self.board = [[Cell(self.values.copy()) for _ in range(size)] for _ in range(size)]
        else:
            self.board = [[Cell([board[i][j]]) if board[i][j] != 0 else Cell(self.values.copy()) for j in range(size)] for i in range(size)]

        self.groups = [FullGroup(row,self.values) for row in self.board]
        self.groups += [FullGroup([self.board[i][j] for i in range(size)],self.values) for j in range(size)]
        self.groups += [FullGroup([self.board[i][j] for i in range(x, x + int(math.sqrt(size))) for j in range(y, y + int(math.sqrt(size)))],self.values) for x in range(0, size, int(math.sqrt(size))) for y in range(0, size, int(math.sqrt(size)))]

    def solve(self):
        pass
    
    def getList(self) -> list[list[int]]:
        return [[row[i].get_Value() for i in range(self.size)] for row in self.board]
    
    def print(self):
        for row in self.board:
            print(" ".join([str(cell.get_Value() or "-") for cell in row]))
        print()
        print("Groups:")
        for group in self.groups:
            print(" ".join([str(cell.get_Value() or "-") for cell in group.cells]))

def solveSudoku(sudoku:list[list[int]]) -> list[list[int]]:
    '''
    Solve a sudoku puzzle using the Sudoku class.
    '''
    print("Solving Sudoku...")
    sudokuSolver = Sudoku(9,sudoku)
    sudokuSolver.print()
    sudokuSolver.solve()
    print("Solved Sudoku:")
    sudokuSolver.print()
    sudoku = sudokuSolver.getList()
    return sudoku
    

if __name__ == "__main__":
    from Benchmark import benchmark_solver
    benchmark_solver(solveSudoku, difficulty='medium', num_puzzles=5)