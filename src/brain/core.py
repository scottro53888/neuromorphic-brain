import torch
import torch.nn as nn


class CorticalCore(nn.Module):
    """General-purpose recurrent reasoning core."""

    def __init__(self, input_dim: int, hidden_dim: int, layers: int = 2):
        super().__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.layers = layers

        self.net = nn.ModuleList([
            nn.LSTM(input_dim if i == 0 else hidden_dim, hidden_dim, batch_first=True)
            for i in range(layers)
        ])

    def forward(self, x, hidden_state=None):
        h = x
        state = hidden_state
        for layer in self.net:
            h, state = layer(h, state)
        return h, state


class AttentionRouter(nn.Module):
    """Selective routing of sensory signals and memory."""

    def __init__(self, dim: int):
        super().__init__()
        self.query = nn.Linear(dim, dim)
        self.key = nn.Linear(dim, dim)
        self.value = nn.Linear(dim, dim)

    def forward(self, x):
        q = self.query(x)
        k = self.key(x)
        v = self.value(x)
        weights = torch.softmax((q @ k.transpose(-2, -1)) / (x.size(-1) ** 0.5), dim=-1)
        return weights @ v
