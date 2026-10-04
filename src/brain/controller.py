from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class SensorSpec:
    name: str
    modality: str
    shape: tuple
    enabled: bool = True


class BrainController:
    """High-level orchestrator for the cognitive architecture."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.modules = {}

    def register_module(self, name: str, module):
        self.modules[name] = module

    def step(self, sensory_input: Dict[str, Any]):
        # High-level architecture loop.
        # Real implementation would route inputs through attention, cortex, memory, and policy.
        return {
            "status": "ok",
            "sensory_input_keys": list(sensory_input.keys()),
            "modules": list(self.modules.keys()),
        }
