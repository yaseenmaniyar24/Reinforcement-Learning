# Project 01: Mountain Car – Random Agent

## Aim

To create and explore the `MountainCar-v0` environment using Gymnasium and observe how an agent behaves when it selects actions randomly.

## Objective

- Create and initialize the Mountain Car environment.
- Inspect the action space and observation space.
- Run three episodes using a random agent.
- Display the environment and observe the agent's actions, rewards, and episode termination.

## Environment

**Environment:** `MountainCar-v0`

The car is positioned between two hills in a valley. It must build momentum by moving backwards and forwards to reach the flag on the hill to the right.

### Action space

There are three discrete actions:

| Action | Meaning |
|---|---|
| 0 | Push left |
| 1 | Do nothing |
| 2 | Push right |

### Observation space

The observation contains two values:

1. Position of the car.
2. Velocity of the car.

### Reward

The environment gives a reward of -1 for each time step until the goal is reached. This encourages the agent to reach the goal in fewer steps.

## Libraries

- Gymnasium: Reinforcement Learning environment.
- NumPy: Numerical operations (not essential to this random-agent example).
- Matplotlib: Optional plotting in notebook-based visualization.

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python mountain_car_random_agent.py
```

A window will display the environment. Close the window or allow the episodes to finish.

## Algorithm: Random Agent

1. Reset the environment.
2. Observe the current state.
3. Select an action randomly using `env.action_space.sample()`.
4. Apply the action using `env.step(action)`.
5. Read the next observation, reward, and termination flags.
6. Continue until the episode ends or the step limit is reached.

## Important note

This is a random agent, not a trained Reinforcement Learning model. It does not learn from rewards or maintain a Q-table or policy.

## Expected observation

The car moves left, right, or remains still according to randomly selected actions. It will generally struggle to reach the goal because it does not learn the momentum-building strategy.

Exact episode lengths and outcomes can vary between runs.

## Learning outcome

After completing this experiment, you should understand how to:

- Create a Gymnasium environment.
- Inspect action and observation spaces.
- Reset and step through an environment.
- Interpret `terminated` and `truncated`.
- Implement a basic random agent.
