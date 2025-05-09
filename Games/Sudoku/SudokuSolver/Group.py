from .Cell import Cell

class Group:
    '''
    A Group of cells on a sudoku board.
    '''
    hasAllValues: bool
    unallowDuplicates: bool
    # mustAddTo: int # needed for some types of sudokus
    values: list[int]
    cells: list[Cell]
    possibleValuePositions: dict[int,list]

    def __init__(self, cells: list[Cell], values: list[int], unallowDuplicates: bool = True, hasAllValues: bool = True):
        self.cells = cells
        self.values = values
        self.unallowDuplicates = unallowDuplicates
        self.hasAllValues = hasAllValues

        for cell in cells:
            cell.inGroups.append(self)

    def reserveValue(self, value: int) -> bool:
        '''
        Reserve a value for a cell in the group.
        '''
        if not self.unallowDuplicates:
            return
        
        for cell in self.cells:
            if cell.get_Value() is None:
                cell.removeValue(value)

    def __repr__(self):
        return f"Group({self.cells})"