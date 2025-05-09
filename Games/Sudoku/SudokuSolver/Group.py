from .Cell import Cell

class Group:
    '''
    A Group of cells on a sudoku board.
    '''
    hasAllValues: bool
    # mustAddTo: int # needed for some types of sudokus
    values: list[int]
    cells: list[Cell]
    possibleValuePositions: dict[int,list]

    def __init__(self, cells: list[Cell], values: list[int]):
        self.cells = cells
        self.values = values