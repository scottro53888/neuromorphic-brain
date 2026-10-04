#!/usr/bin/env python3

from src.brain.controller import BrainController


def main():
    config = {
        "observation_dim": 128,
        "hidden_dim": 256,
        "memory_dim": 128,
        "action_dim": 8,
    }

    controller = BrainController(config)
    sensory_input = {
        "vision": [0.1, 0.2, 0.3],
        "audio": [0.0, 0.0, 0.0],
        "proprioception": [0.5, 0.5],
    }

    result = controller.step(sensory_input)
    print(result)


if __name__ == "__main__":
    main()
