from gymnasium import spaces, Env
import numpy as np
from game import Game2048

class GameEnv(Env):
    game: Game2048
    action_space: spaces.Discrete
    observation_space: spaces.MultiDiscrete
    actions_valid: list[int]
    gridSize: int

    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=11, shape=(gridSize, gridSize), dtype=np.int8)
        self.actions_valid = [1,1,1,1]
        self.reset()

    def reset(self, seed: int = None) -> np.ndarray:
        self.game = Game2048(self.gridSize, seed)
        info = {}
        return self.get_state(), info

    def get_state(self) -> np.ndarray:
        return np.array(self.game.grid, dtype=np.int8)

    def step(self, action: int) -> tuple[np.ndarray, float, bool, dict]:
        orignal_state = self.get_state()

        if self.actions_valid[action] == 0:
            action = np.random.choice(np.flatnonzero(self.actions_valid))

        self.game.move(action)

        new_state = self.get_state()
        if np.array_equal(new_state, orignal_state):
            self.actions_valid[action] = 0
            reward = -1
        else:
            self.actions_valid = [1,1,1,1]
            reward = len(self.game.last_move_merges)
            # reward = sum(self.game.last_move_merges)

        self.action_space = spaces.Discrete(self.actions_valid.count(1))

        # if self.game.is_game_over:
        #     print("Score: " + str(self.game.score))

        return new_state, reward, self.game.is_game_over, False, {}