import math
from .Cell import Cell
from .Group import Group

class Sudoku:
    '''
    A sudoku board
    '''
    size: int
    values: list[int]
    board: list[list[Cell]]
    groups: list[Group]

    def __init__(self, size: int = 9, board: list[list[str]] = None):
        if math.sqrt(size) % 1 != 0:
            raise ValueError("Size must be a perfect square")
        
        self.size = size
        self.values = [i for i in range(1, size + 1)]

        if board is None:
            self.board = [[Cell(self.values.copy()) for _ in range(size)] for _ in range(size)]
        else:
            self.board = [[Cell([board[i][j]]) if int(board[i][j]) in self.values else Cell(self.values.copy()) for j in range(size)] for i in range(size)]

        self.groups = [Group(row,self.values) for row in self.board]
        self.groups += [Group([self.board[i][j] for i in range(size)],self.values) for j in range(size)]
        self.groups += [Group([self.board[i][j] for i in range(x, x + int(math.sqrt(size))) for j in range(y, y + int(math.sqrt(size)))],self.values) for x in range(0, size, int(math.sqrt(size))) for y in range(0, size, int(math.sqrt(size)))]

    def solve(self):
        for row in self.board:
            for cell in row:
                cell.reserveInGroups()
    
    def getList(self) -> list[list[int]]:
        return [[row[i].get_Value() for i in range(self.size)] for row in self.board]
    
    def print(self):
        for row in self.board:
            print(" ".join([str(cell.get_Value() or "-") for cell in row]))
        # print()
        # print("Groups:")
        # for group in self.groups:
        #     print(" ".join([str(cell.get_Value() or "-") for cell in group.cells]))