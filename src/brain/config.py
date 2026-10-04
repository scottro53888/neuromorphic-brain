from dataclasses import dataclass, field
from typing import Dict, Any, Optional


@dataclass
class BrainConfig:
    observation_dim: int = 128
    hidden_dim: int = 256
    memory_dim: int = 128
    action_dim: int = 8
    recurrent_layers: int = 2
    attention_heads: int = 4
    episodic_slots: int = 256
    semantic_dim: int = 128
    homeostatic_dim: int = 16


@dataclass
class BrainState:
    hidden: Optional[Any] = None
    memory: Dict[str, Any] = field(default_factory=dict)
    goals: Dict[str, float] = field(default_factory=dict)
    beliefs: Dict[str, float] = field(default_factory=dict)
    internal_state: Dict[str, float] = field(default_factory=dict)
