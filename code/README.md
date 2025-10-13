# RL Toolkit: Reinforcement Learning from Theory to Practice

**Companion code for the textbook**: *From Measure Theory to Deep Reinforcement Learning*

---

## Overview

This repository contains **15 progressive RL implementation projects**, spanning from basic Markov chains to a full AlphaZero-Lite system for Reversi. Every algorithm is grounded in rigorous mathematical theory and validated empirically.

### **4 Playable Game-Playing AI Systems**

Build increasingly sophisticated game AIs as you progress through the textbook:

1. **Tic-Tac-Toe** (Week 24): Exact dynamic programming, provably optimal play
2. **Connect Four** (Week 31): Monte Carlo Tree Search + heuristics, web-playable demo
3. **Gomoku** (Weeks 40-41): MCTS + neural network evaluation
4. **Reversi** (Weeks 42-48): Full AlphaZero-Lite with self-play iteration

---

## Installation

### Prerequisites

- Python 3.10+
- pip or conda

### Quick Start

```bash
# Clone repository (or navigate to this directory)
cd code/

# Install in editable mode
pip install -e .

# Run tests
pytest tests/ -v

# Try a sample project
cd projects/project_01_markov_chains
python markov_chain_lab.py
```

---

## Package Structure

```
rl_toolkit/                 # Reusable infrastructure
├── envs/                   # Environments (MDPs, games, Markov chains)
├── algorithms/             # RL algorithms (DP, bandits, MCTS, TD, Q-learning, PPO)
├── networks/               # Neural network architectures
├── utils/                  # Utilities (logging, visualization, theory validation)
└── web/                    # Web interface infrastructure (Flask + JavaScript)

projects/                   # 15 milestone projects
├── project_01_markov_chains/
├── project_04.5_tictactoe/
├── project_08.5_connect_four/
├── project_11.5_gomoku/
└── project_12_alphazero_lite/

tests/                      # Unit tests and theory validation
```

---

## Project Roadmap

| # | Project | Week | Theory | Code |
|---|---------|------|--------|------|
| 1 | Markov Chain Laboratory | 5-6 | Perron-Frobenius, stationary distributions | ✓ |
| 2 | MCMC Sampler Suite | 7 | Metropolis-Hastings, detailed balance | ✓ |
| 3 | General State Space Viz | 10 | Feller property | ✓ |
| 4 | GridWorld MDP Playground | 23-24 | Bellman operators | ✓ |
| 4.5 | **Tic-Tac-Toe (Exact DP)** | 24 | Finite-horizon MDPs, minimax | ✓ |
| 5 | Dynamic Programming Algorithms | 24-25 | Value/policy iteration | ✓ |
| 6 | Multi-Armed Bandit Testbed | 27-28 | UCB, regret bounds | ✓ |
| 7 | Thompson Sampling | 29 | Bayesian bandits | ✓ |
| 8 | Contextual Bandits (LinUCB) | 30 | Linear models | ✓ |
| 8.5 | **Connect Four (MCTS + Web)** | 31 | UCT, exploration-exploitation | ✓ |
| 9 | TD Learning Suite | 34-35 | Robbins-Monro, convergence | ✓ |
| 10 | Q-Learning & DQN | 36 | Off-policy learning | ✓ |
| 11 | Policy Gradient Methods (PPO) | 37 | Policy gradient theorem | ✓ |
| 11.5 | **Gomoku (Neural Net + MCTS)** | 40-41 | Function approximation, CNN | ✓ |
| 12 | **AlphaZero-Lite (Reversi)** | 42-48 | Self-play iteration | ✓ |

---

## Usage Examples

### Example 1: Solve GridWorld with Value Iteration

```python
from rl_toolkit.envs import GridWorld
from rl_toolkit.algorithms.dp import value_iteration
from rl_toolkit.utils.viz import plot_value_function

# Create environment
env = GridWorld(size=10, gamma=0.9)

# Solve for optimal value function
V_star, policy = value_iteration(env, epsilon=1e-6)

# Visualize
plot_value_function(V_star, env)
```

### Example 2: Play Connect Four Against MCTS AI

```bash
cd projects/project_08.5_connect_four
python web_interface.py

# Open browser to http://localhost:5000
# Click to drop pieces, AI responds with MCTS search
```

### Example 3: Train Gomoku Neural Network

```bash
cd projects/project_11.5_gomoku
python train_value_net.py --board-size 15 --epochs 100 --batch-size 32

# Web demo with neural net heatmap
python web_interface.py
```

---

## Theory-to-Code Correspondence

Every algorithm includes explicit references to theorems from the textbook:

```python
def bellman_operator(V, policy, gamma=0.99):
    """
    Apply Bellman operator to value function.

    Theory: T^π V = R^π + γ P^π V ([THM-24.2.1])
    Contraction: ||T V1 - T V2||_∞ ≤ γ ||V1 - V2||_∞ ([THM-16.3.2])
    """
    ...
```

---

## Running Tests

```bash
# All tests
pytest tests/ -v

# Specific category
pytest tests/test_game_engines.py -v
pytest tests/test_theory_convergence.py -v

# With coverage
pytest tests/ --cov=rl_toolkit --cov-report=html
```

---

## Contributing

This codebase follows strict standards (see `Code_Organization_Guide.md`):

- **Type hints** (PEP 484) on all functions
- **Docstrings** (NumPy style) with theory references
- **Unit tests** for all algorithms
- **Theory validation tests** verifying convergence/correctness

Before submitting:
```bash
# Type check
mypy rl_toolkit/ --ignore-missing-imports

# Format code
black rl_toolkit/ tests/

# Run tests
pytest tests/ -v
```

---

## Documentation

- **`Code_Organization_Guide.md`**: Detailed code standards and architecture
- **`RL_Implementation_Roadmap.md`**: Complete project specifications
- **Textbook**: Full mathematical theory and proofs

---

## Citation

If you use this code in your research or teaching, please cite:

```bibtex
@book{dubois2026measure,
  title={From Measure Theory to Deep Reinforcement Learning},
  author={},
  publisher={Springer},
  year={2026}
}
```

---

## License

MIT License - see LICENSE file for details.

---

## Acknowledgments

Built with:
- **NumPy** / **PyTorch** / **JAX** for numerical computation
- **Flask** for web interfaces
- **Matplotlib** / **Seaborn** for visualization
- **pytest** for testing

Inspired by:
- Sutton & Barto's *Reinforcement Learning: An Introduction*
- OpenAI Spinning Up
- DeepMind's AlphaZero paper

---

**Questions?** See the `Code_Organization_Guide.md` or open an issue on GitHub.

