import numpy as np
from game import Game2048

class GameEnv:
    game: Game2048
    def __init__(self):
        self.game = Game2048()
        self.reset()

    def reset(self) -> np.ndarray:
        self.game = Game2048()
        return self.get_state()

    def get_state(self) -> np.ndarray:
        # Return the game grid as a flattened 1D array
        return np.array(self.game.grid).flatten()

    def step(self, action: int) -> tuple[np.ndarray, float, bool]:
        # Map action (0=up, 1=down, 2=left, 3=right) to game moves
        self.game.move(action)

        # Calculate reward (e.g., increase in score)
        reward = sum(self.game.last_move_merges)

        # Check if the game is over
        done = self.game.is_game_over

        return self.get_state(), reward, done
