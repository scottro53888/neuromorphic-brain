# Neuromorphic Brain

A brain-inspired cognitive architecture designed to approximate the major functions of a human brain in a practical, engineered system.

This project is not a literal biological brain replica. Instead, it models the core functional subsystems that make human cognition work:

- sensory perception
- attention routing
- cortical-like reasoning
- working memory
- episodic memory
- semantic memory
- procedural memory
- world modeling
- action selection
- reward and motivation
- predictive control
- continual learning

The goal is to bring the system as close as possible to human-like cognitive behavior within engineering limits.

## Architecture overview

The system is organized into a hybrid cognitive stack:

1. Sensory front end
   - vision, audio, touch, proprioception, interoception
2. Attention router
   - thalamus-like salience selection
3. Cortical hierarchy
   - recurrent multimodal reasoning
4. Working memory
   - short-term goal and task maintenance
5. Long-term memory
   - episodic, semantic, procedural memory
6. World model
   - predictive simulation of environment and self
7. Action selection
   - policy + value network + goal arbitration
8. Motor control
   - cerebellum-like adaptation
9. Homeostatic control
   - energy, stress, fatigue, safety regulation
10. Memory consolidation
   - sleep-like replay and offline learning

## Repository structure

- `docs/brain_architecture.md` — design spec and subsystem breakdown
- `src/brain/` — brain core implementation
- `src/simulations/` — environment and embodied simulation examples
- `requirements.txt` — dependencies
- `examples/` — demo entry points

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python examples/demo_brain.py
```

## Important note

This is a research and engineering blueprint for a human-brain-inspired cognitive system. It is a practical approximation of cognitive function, not a biological reconstruction of a real human brain.

## Planned milestones

- prototype recurrent agent with memory
- multimodal sensory fusion
- episodic and semantic memory modules
- planning and world model integration
- embodied simulation in a toy environment
- neuromorphic or spiking-network backend
- continual learning and consolidation

## License

MIT
