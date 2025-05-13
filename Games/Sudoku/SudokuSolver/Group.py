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
                cell.removePossibility(value)

    def removePossibility(self, value: int, cell: Cell):
        '''
        Remove a value possibility from the group.
        '''
        if not self.haveAllValues:
            return
        
        if len(self.possiblePlacements[value]) <= 1:
            raise ValueError(f"Value {value} is not possible for this group")
        
        if cell not in self.possiblePlacements[value]:
            return
        self.possiblePlacements[value].remove(cell)

        # if there's only one possible placement for a value, set the value of the cell
        if len(self.possiblePlacements[value]) == 1:
            if self.possiblePlacements[value][0].getValue() is None:
                if self.logger is not None:
                    self.logger(f"Only place for Value {value} in Group", [self.possiblePlacements[value][0]], [self])
                self.possiblePlacements[value][0].setValue(value)
        else:
            # if all possible placements are also in another group, the number can't be at other places of the other group
            for group in self.possiblePlacements[value][0].groups:
                group: Group
                if group == self:
                    continue
                if any(cell.getValue() == value for cell in group.cells):
                    continue
                if all(cell in group.cells for cell in self.possiblePlacements[value]):
                    if self.logger is not None:
                        self.logger(f"Value {value} must be in this place, blocking other places of the group", self.possiblePlacements[value], [group])
                    group.reserveValue(value, self.possiblePlacements[value])

    def isValid(self) -> bool:
        '''
        Check if the group is valid.
        '''
        if self.haveAllValues:
            for value in self.values:
                if len(self.possiblePlacements[value]) != 1:
                    return False
        
        if self.unallowDuplicates:
            cellValues = [cell.getValue() for cell in self.cells if cell.getValue() is not None]
            if len(cellValues) != len(set(cellValues)):
                return False
        
        return True

    def __repr__(self):
        return f"Group({self.cells})"