import math
from .Cell import Cell
from .Group import Group
from .LogStep import Step
from copy import deepcopy

class Sudoku:
    '''
    A sudoku board
    '''
    size: int
    values: list[int]
    board: list[list[Cell]]
    groups: list[Group]
    log: list[Step]
    doLog: bool

    def __init__(self, size: int = 9, board: list[list[str]] | list[list[Cell]] = None, doLog: bool = False):
        if math.sqrt(size) % 1 != 0:
            raise ValueError("Size must be a perfect square")
        
        self.size = size
        self.values = [i for i in range(1, size + 1)]

        if board is None:
            self.board = [[Cell(self.values.copy(), x, y) for x in range(size)] for y in range(size)]
        elif isinstance(board[0][0], Cell):
            self.board = board
        else:
            self.board = [[Cell([board[y][x]], x, y) if int(board[y][x]) in self.values else Cell(self.values.copy(), x, y) for x in range(size)] for y in range(size)]

        self.groups = [Group(row,self.values) for row in self.board]
        self.groups += [Group([self.board[i][j] for i in range(size)],self.values) for j in range(size)]
        self.groups += [Group([self.board[i][j] for i in range(x, x + int(math.sqrt(size))) for j in range(y, y + int(math.sqrt(size)))],self.values) for x in range(0, size, int(math.sqrt(size))) for y in range(0, size, int(math.sqrt(size)))]

        self.log = []
        self.doLog = doLog

    def solve(self):
        for row in self.board:
            for cell in row:
                cell.reserveInGroups()
    
    def getList(self) -> list[list[int]]:
        return [[row[i].getValue() for i in range(self.size)] for row in self.board]
    
    def registerStep(self, step: str, markCause: list[Cell], markEffect: list[Cell]):
        if not self.doLog:
            return
        board: list[list[Cell]] = deepcopy(self.board)
        markCause: list[Cell] = [board[cell.y][cell.x] for cell in markCause]
        markEffect: list[Cell] = [board[cell.y][cell.x] for cell in markEffect]
        step = Step(board, step, markCause, markEffect)
        self.log.append(step)
    
    def print(self):
        box_size = int(math.sqrt(self.size))
        for i, row in enumerate(self.board):
            if i % box_size == 0 and i != 0:
                print("-" * (self.size * 2 + box_size - 1))
            line = ""
            for j, cell in enumerate(row):
                if j % box_size == 0 and j != 0:
                    line += "| "
                line += f"{cell.getValue() or '-'} "
            print(line.strip())