# Reinforcement Learning Agent for Autonomous Driving

![Agent Driving on Track](https://i.imgur.com/Ul6YFWM.png)

## 1. Name and Purpose of the Agent

The reinforcement learning agent developed for this project is called the **Autonomous Driving CarRacing Agent**. The purpose of this agent is to learn how to control a simulated self-driving car in a virtual environment by staying on track and maximizing forward progress. Through trial-and-error interactions with the environment, the agent learns optimal steering, acceleration, and braking behaviors without explicit programming. This project demonstrates how reinforcement learning can be applied to autonomous driving tasks in a simulated setting.

---

## 2. Algorithms Used

This project uses the **Proximal Policy Optimization (PPO)** reinforcement learning algorithm. PPO was selected because it is a modern policy-gradient method that is stable, efficient, and well-suited for continuous action spaces such as steering and throttle control. PPO improves learning stability by limiting large policy updates while still allowing the agent to explore the environment effectively. This makes it a common baseline algorithm for autonomous driving simulations and control tasks.

---

## 3. Dataset Information

### 3.1 Dataset Source

This project does not rely on a traditional static dataset. Instead, training data is generated dynamically through interactions with the **Gymnasium CarRacing-v3 simulation environment**. The environment provides state observations, reward signals, and termination conditions during each episode.

### 3.2 Number of Records

During training, the agent generated approximately **50,000 state–action–reward–next-state transitions**. Each transition represents one interaction step between the agent and the environment. These transitions collectively form the experience data used by the PPO algorithm to update the policy.

### 3.3 Number of Features

Each state observation is represented as an **RGB image with dimensions 96 × 96 × 3**, resulting in **27,648 input features** per observation.

### 3.4 Description of Features

| Feature Name | Description | Data Type |
|-------------|------------|-----------|
| Observation Image | Top-down RGB image of the track and vehicle | Numeric (Pixel Values) |
| Action Vector | Steering, throttle, and brake commands | Continuous Numeric |
| Reward Signal | Feedback indicating driving performance | Numeric |
| Episode Termination Flag | Indicates episode completion | Boolean |

### 3.5 Preprocessing Steps

- Observation images are normalized and processed internally by the PPO algorithm.
- No manual feature extraction is performed.
- Rewards are used directly as provided by the environment to guide learning.

---

## 4. Libraries, Toolkits, and Frameworks

- **Python:** Primary programming language used to implement the RL agent.
- **Gymnasium:** Provides the CarRacing-v3 autonomous driving simulation environment.
- **Stable-Baselines3:** Supplies the PPO implementation and training utilities.
- **NumPy:** Supports numerical operations during training.
- **Matplotlib:** Used for visualizing training performance and reward progression.

---

## 5. Application Design and Implementation

The agent follows the standard reinforcement learning loop. At the start of each episode, the environment is reset and an initial observation image is received. The agent selects actions based on the current policy, which controls steering, acceleration, and braking. After each action, the environment returns a reward and a new observation. The PPO algorithm updates the policy using collected experiences to maximize cumulative reward over time. As training progresses, the agent learns behaviors that improve track following and forward motion.

---

## 6. Instructions for Running the Agent

1. Create and activate a Python virtual environment.
2. Install required dependencies including Gymnasium and Stable-Baselines3.
3. Run the training script to begin agent learning.
4. Observe terminal logs during training.
5. After training, watch the agent perform in the simulation during evaluation mode.

---

## 7. Results

After training, the agent demonstrated improved driving behavior compared to random actions. Early episodes showed frequent off-track behavior, while later evaluations showed smoother steering and longer track traversal. Screenshots captured during evaluation show the agent navigating the track and maintaining forward progress. These results indicate that the agent successfully learned a more effective driving policy through reinforcement learning.

![Training Output](https://i.imgur.com/0M7fwsz.png)
---

## 8. Discussion and Insights

The autonomous driving agent successfully learned basic control behaviors using PPO. However, performance is limited by the complexity of the environment and the amount of training time. While the agent improved its ability to remain on the track, occasional deviations into grassy areas still occurred. Future improvements could include longer training durations, reward function tuning, or using more advanced algorithms such as Soft Actor-Critic (SAC). Despite these limitations, the project demonstrates a functional reinforcement learning system applied to autonomous driving.

---

## 9. References

Sutton, R. S., & Barto, A. G. (2018). *Reinforcement learning: An introduction* (2nd ed.). MIT Press.

Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347*.

Gymnasium Developers. (n.d.). *CarRacing-v3 environment documentation*. https://gymnasium.farama.org

Stable-Baselines3 Developers. (n.d.). *PPO documentation*. https://stable-baselines3.readthedocs.io

