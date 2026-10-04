# Example environment for a toy embodied brain agent

class ToyEmbodiedWorld:
    """Minimal simulation loop for a brain-inspired agent."""

    def __init__(self, size=8):
        self.size = size
        self.agent_position = [0, 0]
        self.goal = [size - 1, size - 1]

    def reset(self):
        self.agent_position = [0, 0]
        return {
            "position": self.agent_position,
            "goal": self.goal,
            "energy": 1.0,
            "arousal": 0.5,
        }

    def step(self, action):
        # Minimal movement simulation
        dx, dy = 0, 0
        if action == "up":
            dx = -1
        elif action == "down":
            dx = 1
        elif action == "left":
            dy = -1
        elif action == "right":
            dy = 1

        self.agent_position[0] = max(0, min(self.size - 1, self.agent_position[0] + dx))
        self.agent_position[1] = max(0, min(self.size - 1, self.agent_position[1] + dy))

        reward = 1.0 if self.agent_position == self.goal else -0.01
        done = self.agent_position == self.goal
        return {
            "position": self.agent_position,
            "goal": self.goal,
            "reward": reward,
            "done": done,
        }
