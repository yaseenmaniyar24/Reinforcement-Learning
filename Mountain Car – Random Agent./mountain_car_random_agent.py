import gymnasium as gym
import time


def run_random_agent(num_episodes=3, max_steps=200, delay=0.05):
    # Create the Mountain Car environment.
    # "human" opens a display window for visualization.
    env = gym.make("MountainCar-v0", render_mode="human")

    print("Action Space:", env.action_space)
    print("Observation Space:", env.observation_space)
    print("Observation Space High:", env.observation_space.high)
    print("Observation Space Low:", env.observation_space.low)
    print("Max steps per episode:", env.spec.max_episode_steps)
    print("Reward threshold:", env.spec.reward_threshold)

    try:
        for episode in range(num_episodes):
            observation, info = env.reset()
            total_reward = 0

            print(f"\nEpisode {episode + 1} started")

            for step in range(max_steps):
                # Select a random action.
                action = env.action_space.sample()

                # Apply the action and observe the result.
                observation, reward, terminated, truncated, info = env.step(action)
                total_reward += reward

                print(
                    f"Step {step + 1}: "
                    f"Observation={observation}, "
                    f"Action={action}, "
                    f"Reward={reward}"
                )

                time.sleep(delay)

                if terminated or truncated:
                    reason = "goal reached" if terminated else "time limit reached"
                    print(
                        f"Episode {episode + 1} ended after "
                        f"{step + 1} steps ({reason})."
                    )
                    break
            else:
                print(f"Episode {episode + 1} stopped at the custom step limit.")

            print(f"Total episode reward: {total_reward}")

    finally:
        env.close()


if __name__ == "__main__":
    run_random_agent()
