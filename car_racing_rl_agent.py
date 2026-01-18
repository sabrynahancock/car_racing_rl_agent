import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import matplotlib.pyplot as plt

def main():
    print("=== Autonomous Driving RL Agent (CarRacing-v2) ===")

    # Create environment
    env = gym.make("CarRacing-v3", render_mode=None)

    env = DummyVecEnv([lambda: env])

    # Create PPO agent
    model = PPO(
        policy="CnnPolicy",
        env=env,
        verbose=1,
        learning_rate=3e-4,
        gamma=0.99,
        n_steps=2048,
        batch_size=64
    )

    # Train the agent
    timesteps = 50_000
    print(f"Training agent for {timesteps} timesteps...")
    model.learn(total_timesteps=timesteps)

    # Save model
    model.save("ppo_car_racing_agent")
    print("Model saved as ppo_car_racing_agent")

    # Evaluate trained agent
    eval_env = gym.make("CarRacing-v3", render_mode="human")

    obs, _ = eval_env.reset()

    total_reward = 0
    for _ in range(1000):
        action, _ = model.predict(obs)
        obs, reward, terminated, truncated, _ = eval_env.step(action)
        total_reward += reward
        if terminated or truncated:
            obs, _ = eval_env.reset()

    eval_env.close()
    print(f"Evaluation total reward: {total_reward:.2f}")

if __name__ == "__main__":
    main()
