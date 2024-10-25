import numpy as np
from game import Game2048
from constants import GRID_SIZE

class GameEnv:
    def __init__(self):
        self.game = Game2048()
        self.reset()

    def reset(self):
        self.game.start_game()
        return self.get_state()

    def get_state(self):
        # Return the game grid as a flattened 1D array
        return np.array(self.game.grid).flatten()

    def step(self, action):
        # Map action (0=up, 1=down, 2=left, 3=right) to game moves
        if action == 0:
            new_grid = self.game.move_up()
        elif action == 1:
            new_grid = self.game.move_down()
        elif action == 2:
            new_grid = self.game.move_left()
        elif action == 3:
            new_grid = self.game.move_right()
        else:
            raise ValueError("Invalid Action")

        # Update game grid
        self.game.update_grid(new_grid)

        # Calculate reward (e.g., increase in score)
        reward = self.calculate_reward(new_grid)

        # Check if the game is over
        done = not self.game.can_move()

        return self.get_state(), reward, done

    def calculate_reward(self, new_grid):
        # A simple reward function could be the sum of merged tiles
        reward = sum([new_grid[i][j] for i in range(GRID_SIZE) for j in range(GRID_SIZE)])
        return reward