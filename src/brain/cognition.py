import torch
import torch.nn as nn


class WorldModel(nn.Module):
    """Predicts future sensory states and latent transitions."""

    def __init__(self, state_dim: int, action_dim: int, latent_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim + action_dim, latent_dim),
            nn.ReLU(),
            nn.Linear(latent_dim, latent_dim),
            nn.ReLU(),
            nn.Linear(latent_dim, state_dim),
        )

    def forward(self, state, action):
        x = torch.cat([state, action], dim=-1)
        return self.net(x)


class ActionSelector(nn.Module):
    """Chooses actions by integrating memory, goals, and value."""

    def __init__(self, input_dim: int, action_dim: int):
        super().__init__()
        self.policy = nn.Linear(input_dim, action_dim)
        self.value = nn.Linear(input_dim, 1)

    def forward(self, x):
        return self.policy(x), self.value(x)
