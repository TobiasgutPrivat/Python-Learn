import random
from constants import GRID_SIZE

class Game2048:
    def __init__(self):
        self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.start_game()
    
    def start_game(self):
        self.add_new_tile()
        self.add_new_tile()
    
    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
    
    def merge_left(self, row):
        non_zero = [num for num in row if num != 0]
        merged_row = []
        skip = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                merged_row.append(non_zero[i] * 2)
                skip = True
            else:
                merged_row.append(non_zero[i])
        return merged_row + [0] * (GRID_SIZE - len(merged_row))
    
    def move_left(self):
        return [self.merge_left(row) for row in self.grid]
    
    def move_right(self):
        return [self.merge_left(row[::-1])[::-1] for row in self.grid]
    
    def move_up(self):
        transposed = list(zip(*self.grid))
        merged = [self.merge_left(list(row)) for row in transposed]
        return [list(row) for row in zip(*merged)]
    
    def move_down(self):
        transposed = list(zip(*self.grid))
        merged = [self.merge_left(list(row)[::-1])[::-1] for row in transposed]
        return [list(row) for row in zip(*merged)]
    
    def can_move(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == 0:
                    return True
                if j < GRID_SIZE - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return True
                if i < GRID_SIZE - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return True
        return False

    def update_grid(self, new_grid):
        if new_grid != self.grid:
            self.grid = new_grid
            self.add_new_tile()
