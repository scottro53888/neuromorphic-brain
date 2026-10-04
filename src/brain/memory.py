import torch
import torch.nn as nn


class WorkingMemory(nn.Module):
    """Short-term memory for the current task context."""

    def __init__(self, dim: int, slots: int = 16):
        super().__init__()
        self.dim = dim
        self.slots = slots
        self.memory = nn.Parameter(torch.zeros(slots, dim))

    def forward(self, current_state):
        query = current_state
        scores = torch.matmul(self.memory, query.unsqueeze(-1)).squeeze(-1)
        weights = torch.softmax(scores, dim=0)
        return torch.sum(weights.unsqueeze(-1) * self.memory, dim=0)


class EpisodicMemory(nn.Module):
    """Stores structured traces of experience."""

    def __init__(self, dim: int, capacity: int = 256):
        super().__init__()
        self.dim = dim
        self.capacity = capacity
        self.storage = nn.Parameter(torch.zeros(capacity, dim))

    def forward(self, event_embedding):
        scores = torch.matmul(self.storage, event_embedding.unsqueeze(-1)).squeeze(-1)
        weights = torch.softmax(scores, dim=0)
        return torch.sum(weights.unsqueeze(-1) * self.storage, dim=0)


class SemanticMemory(nn.Module):
    """General knowledge representation."""

    def __init__(self, input_dim: int, output_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, output_dim),
            nn.ReLU(),
            nn.Linear(output_dim, output_dim),
        )

    def forward(self, x):
        return self.net(x)
