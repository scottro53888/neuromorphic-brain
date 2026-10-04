# Brain architecture specification

## Objective

Build a synthetic cognitive system that approximates the major functions of the human brain as closely as practical with modern AI and neuromorphic engineering.

## Core design principles

1. Statefulness
   - cognition must persist over time
2. Memory hierarchy
   - short-term and long-term memory must coexist
3. Attention
   - not every signal gets equal processing
4. Prediction
   - the system predicts future state and uses errors to learn
5. Agency
   - actions are guided by internal goals and values
6. Embodiment
   - intelligence exists with a body in a world
7. Continual learning
   - the system learns online without resetting
8. Self-modeling
   - it maintains a model of self and environment

## Subsystems

### 1. Sensory front end

Responsible for turning raw sensor data into latent representations.

Modules:
- vision encoder
- auditory encoder
- tactile encoder
- proprioception encoder
- interoception encoder

### 2. Attention routing

Filters and prioritizes signals.

Features:
- bottom-up salience detection
- top-down goal-driven focus
- context-sensitive routing
- uncertainty-based selection

### 3. Cortical reasoning core

This is the general-purpose inference engine.

Implementation ideas:
- recurrent transformer
- LSTM/GRU stack
- cortical hierarchy of latent states
- latent world representation

### 4. Working memory

Temporary structured memory used for immediate reasoning.

Functions:
- hold current task context
- maintain subgoal stack
- support multi-step deliberation

### 5. Episodic memory

Stores event traces with contextual metadata.

Attributes:
- time
- location
- emotional value
- associated sensory features
- observed outcomes

### 6. Semantic memory

Generalized knowledge representation.

Formats:
- concept embeddings
- graph knowledge base
- relational memory

### 7. Procedural memory

Encodes skill and action routines.

Examples:
- manipulation skill
- navigation policy
- motor primitives
- social routines

### 8. World model

Predicts future observations given actions and context.

Supports:
- planning
- imagination
- anticipation
- counterfactual reasoning

### 9. Action selection

Integrates goals, memories, and value to choose actions.

Mechanisms:
- value function
- policy network
- risk estimation
- exploration-exploitation balancing

### 10. Emotional and motivational system

Encodes internal drives and salience.

Subsystems:
- reward prediction
- curiosity drive
- fear / threat model
- hunger and safety regulation
- goals and urgency

### 11. Motor control and adaptation

Takes abstract action plans and turns them into executable behavior.

Components:
- motor primitives
- inverse dynamics
- closed-loop correction
- proprioceptive error correction

### 12. Homeostasis and survival regulation

Maintains internal vital state.

Examples:
- energy budget
- temperature
- fatigue
- stress
- safety constraints

### 13. Memory consolidation

Offline replay and learning from experience.

Functions:
- strengthen useful memories
- compress representations
- integrate event traces into long-term structure
- generate latent simulation data for learning

## Neural design patterns

The following patterns are recommended for implementation:

- recurrent state for temporal continuity
- attention bottlenecks for salience selection
- memory retrieval networks
- self-supervised prediction tasks
- reward-driven policy learning
- uncertainty modeling
- graph memory for structure
- embeddings for concept spaces

## Suggested module layout

```text
src/
  brain/
    __init__.py
    models/
      cortical_core.py
      attention_router.py
      world_model.py
      policy_network.py
      value_network.py
    memory/
      working_memory.py
      episodic_memory.py
      semantic_memory.py
      procedural_memory.py
      consolidation.py
    sensors/
      vision.py
      audio.py
      touch.py
      proprioception.py
    control/
      action_selector.py
      motor_controller.py
      homeostasis.py
    cognition/
      goals.py
      belief_state.py
      self_model.py
    utils/
      tensor_tools.py
      logging.py
```

## Minimal functional loop

```text
sensor input
  -> encoding
  -> attention routing
  -> cortical reasoning
  -> memory retrieval
  -> world model update
  -> action selection
  -> motor execution
  -> new sensory feedback
  -> learning and consolidation
```

## Research goals

The system should eventually support:

- one-shot memory of experiences
- cross-modal understanding
- long-horizon planning
- causal inference
- adaptive behavior under uncertainty
- identity persistence across states
- autonomous goals beyond fixed prompts

## Closing note

This project aims to approximate the human brain's function, not reproduce biology exactly. Human-like intelligence is a systems problem involving perception, memory, prediction, and embodiment rather than a single monolithic model.
