import random

class Game2048:
    grid: list[list[int]]
    score: int = 0
    is_game_over: bool = False
    last_move_merges: list[int] = []
    gridSize: int

    def __init__(self, gridSize: int = 4, seed: int = None):
        self.gridSize = gridSize
        self.grid = [[0] * self.gridSize for _ in range(self.gridSize)]
        self.add_new_tile()
        self.add_new_tile()
        if seed is not None:
            random.seed(seed)
    
    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(self.gridSize) for j in range(self.gridSize) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 1 if random.random() < 0.9 else 2
    
    def merge_left(self, row):
        non_zero = [num for num in row if num != 0]
        merged_row = []
        skip = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                new_value = non_zero[i] + 1
                merged_row.append(new_value)
                self.score += 2**new_value
                self.last_move_merges.append(new_value)
                skip = True
            else:
                merged_row.append(non_zero[i])
        return merged_row + [0] * (self.gridSize - len(merged_row))
    
    def move(self, direction: int) -> int:
        self.last_move_merges = []
        score: int = 0
        match direction:
            case 0:
                transposed = list(zip(*self.grid))
                merged = [self.merge_left(list(row)) for row in transposed]
                self.grid = [list(row) for row in zip(*merged)]
            case 1:
                transposed = list(zip(*self.grid))
                merged = [self.merge_left(list(row)[::-1])[::-1] for row in transposed]
                self.grid = [list(row) for row in zip(*merged)]
            case 2:
                self.grid = [self.merge_left(row) for row in self.grid]
            case 3:
                self.grid = [self.merge_left(row[::-1])[::-1] for row in self.grid]
            case _:
                raise ValueError("Invalid direction")

        self.add_new_tile()

        self.is_game_over = not self.can_move()

        return score
    
    def can_move(self):
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if self.grid[i][j] == 0:
                    return True
                if j < self.gridSize - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return True
                if i < self.gridSize - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return True
        return False