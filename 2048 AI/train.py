from game_environment import GameEnv
from dqn_agent import DQNAgent
import numpy as np

EPISODES = 1000

if __name__ == "__main__":
    env = GameEnv()
    state_size = env.get_state().shape[0]
    action_size = 4  # Up, Down, Left, Right
    agent = DQNAgent(state_size, action_size)

    for e in range(EPISODES):
        state = env.reset()
        state = np.reshape(state, [1, state_size])
        done = False
        total_reward = 0

        while not done:
            action = agent.act(state)
            next_state, reward, done = env.step(action)
            next_state = np.reshape(next_state, [1, state_size])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward

            if done:
                print(f"Episode {e}/{EPISODES} - Score: {total_reward}")
                break

        # Train the agent with experience replay
        if len(agent.memory) > 64:
            agent.train(64)

        # Save the model every 50 episodes
        if e % 50 == 0:
            agent.save("2048-dqn.h5")
