from .Cell import Cell
from typing import Callable

class Group:
    '''
    A Group of cells on a sudoku board.
    '''
    haveAllValues: bool # True if the group must have all values
    unallowDuplicates: bool # True if the group must not have duplicates
    # mustAddTo: int # needed for some types of sudokus
    values: list[int]
    cells: list[Cell]
    possiblePlacements: dict[int,list[Cell]] # Cells where a value can be placed in the group, removed if value is already placed
    logger: Callable # function to log steps

    def __init__(self, cells: list[Cell], values: list[int], logger: Callable = None, unallowDuplicates: bool = True, haveAllValues: bool = True):
        self.cells = cells
        self.values = values
        self.unallowDuplicates = unallowDuplicates
        self.haveAllValues = haveAllValues
        self.logger = logger

        for cell in cells:
            cell.groups.append(self)

        if self.haveAllValues:
            # initialize possible placements for each value
            self.possiblePlacements = {value: [] for value in values}
            for cell in cells:
                for value in cell.possibleValues:
                    self.possiblePlacements[value].append(cell)

    def reserveValue(self, value: int, exceptCells: list[Cell] = []) -> bool:
        '''
        Reserve a value for a cell in the group.
        '''
        if not self.unallowDuplicates:
            return
        
        for cell in self.cells:
            if cell in exceptCells:
                continue
            if cell.getValue() is None:
                cell.removeValue(value)

    def removePossibility(self, value: int, cell: Cell):
        '''
        Remove a value possibility from the group.
        '''
        if not self.haveAllValues or len(self.possiblePlacements[value]) <= 1:
            return
        self.possiblePlacements[value].remove(cell)

        # if there's only one possible placement for a value, set the value of the cell
        if len(self.possiblePlacements[value]) == 1:
            self.possiblePlacements[value][0].setValue(value)
        else:
            # if all possible placements are also in another group, the number can't be at other places of the other group
            # TODO: check if this works
            # for group in cell.inGroups:
            #     if group == self:
            #         continue
            #     if all(cell in group.cells for cell in self.possiblePlacements[value]):
            #         group.reserveValue(value, self.possiblePlacements[value])
            pass

    def __repr__(self):
        return f"Group({self.cells})"