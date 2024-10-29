from game_environment import GameEnv
from RLUI import RLUI2048
from stable_baselines3 import PPO  # or use DQN if actions are discrete
from stable_baselines3.common.env_checker import check_env
import time
import os

def train(gridSize: int,steps: int) -> PPO:
    env = GameEnv(gridSize)
    check_env(env)
    model = PPO("MlpPolicy", env, verbose=1, batch_size=10000, learning_rate=0.0003, n_steps=10000) 
    model.learn(total_timesteps=steps, progress_bar=True)
    return model

def evaluateRandom(gridSize, n_games: int = 1):
    env = GameEnv(gridSize)
    avg_score = 0
    for _ in range(n_games):
        obs, info = env.reset()
        terminated, truncated = False, False
        while not (terminated or truncated):  # Run for a number of steps
            action = env.action_space.sample()  # Take a random action
            obs, reward, terminated, truncated, info = env.step(action)
        avg_score += env.game.score
    print(f"Average score = {avg_score / n_games}")

def evaluate(model: PPO, gridSize, n_games: int = 1):
    env = GameEnv(gridSize)
    avg_score = 0
    for _ in range(n_games):
        obs, info = env.reset()
        terminated, truncated = False, False
        while not (terminated or truncated):  # Run for a number of steps
            action, _states = model.predict(obs, deterministic=True)  # Use deterministic=True for evaluation
            obs, reward, terminated, truncated, info = env.step(action)
        avg_score += env.game.score
    print(f"Average score = {avg_score / n_games}")
            
def evaluateVisual(model: PPO, gridSize):
    env = GameEnv(gridSize)
    UI = RLUI2048(gridSize)
    obs, info = env.reset()
    terminated, truncated = False, False
    i = 0
    while not (terminated or truncated):  # Run for a number of steps
        i += 1
        action, _states = model.predict(obs, deterministic=True)  # Use deterministic=True for evaluation
        obs, reward, terminated, truncated, info = env.step(action)
        UI.update_ui(env.game,i)
        time.sleep(0.1)
    input("Game over, press enter to continue...")

def load(name: str, gridSize: int) -> PPO:
    env = GameEnv(gridSize)
    return PPO.load(os.path.dirname(os.path.abspath(__file__)) + "/Models/"+ name, env=env)

def save(name: str, model: PPO):
    model.save(os.path.dirname(os.path.abspath(__file__)) + "/Models/"+ name)
