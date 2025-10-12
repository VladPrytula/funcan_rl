# Code Organization Guide

**Author**: Dr. Max Rubin
**Purpose**: Standards and conventions for `rl_toolkit` package and project implementations
**Status**: Living document (updated as infrastructure evolves)

---

## Overview

This guide covers **how to write code** for the RL Toolkit. For **what to build**, see:
- **`RL_Implementation_Roadmap.md`**: Complete project sequence (15 projects), game progression (Tic-Tac-Toe → Reversi), theory connections
- **`CLAUDE.md`**: Repository overview and workflow integration

---

## Table of Contents

1. [Philosophy: Three-Tier Architecture](#philosophy-three-tier-architecture)
2. [Code Standards](#code-standards)
3. [Import Conventions](#import-conventions)
4. [File Organization Patterns](#file-organization-patterns)
5. [Theory Validation Requirements](#theory-validation-requirements)
6. [Game Engine Abstractions](#game-engine-abstractions)
7. [Web Interface Standards](#web-interface-standards)
8. [Testing Philosophy](#testing-philosophy)
9. [Git Workflow for Code](#git-workflow-for-code)
10. [Common Tasks](#common-tasks)

---

## Philosophy: Three-Tier Architecture

The codebase is organized into three tiers with distinct purposes:

### **Tier 1: `code/rl_toolkit/` - Reusable Infrastructure**

**Purpose**: Production-quality, battle-tested components used across multiple projects.

**Contents**:
- `envs/`: Environment implementations (MDPs, games, Markov chains)
- `algorithms/`: Core RL algorithms (DP, bandits, MCTS, TD, Q-learning, policy gradients)
- `networks/`: Neural network architectures (value nets, policy nets, AlphaZero dual-head)
- `utils/`: Shared utilities (logging, visualization, theory validation)
- `web/`: Web interface infrastructure (Flask app, REST API, templates, JavaScript)

**When to add code here**:
- ✅ Component is reusable across multiple projects
- ✅ Code is tested, documented, and production-ready
- ✅ API is stable (breaking changes affect downstream projects)

**When NOT to add code here**:
- ❌ Experimental code (use `projects/` instead)
- ❌ Single-use scripts (use `projects/` or `Week_X/final/day_Y/code/`)
- ❌ Quick hacks or prototypes

**Quality bar**: Code in `rl_toolkit/` should be:
- Type-hinted (PEP 484)
- Docstring-documented (NumPy style)
- Unit tested (pytest)
- Theory-grounded (references theorem numbers in comments)

---

### **Tier 2: `code/projects/` - Milestone Demonstrations**

**Purpose**: Self-contained implementations demonstrating specific algorithms or systems.

**Contents**:
- `project_01_markov_chains/`: Markov chain laboratory
- `project_04.5_tictactoe/`: Tic-Tac-Toe with exact DP
- `project_08.5_connect_four/`: Connect Four with MCTS + heuristics
- `project_11.5_gomoku/`: Gomoku with neural net + MCTS
- `project_12_alphazero_lite/`: Full AlphaZero-Lite for Reversi
- ... (15 projects total)

**Structure of each project folder**:
```
project_XX_name/
├── README.md                   # Project goals, theory connections, usage
├── main_implementation.py      # Core algorithm implementation
├── experiments.py              # Numerical experiments / benchmarks
├── web_interface.py            # Flask app launcher (if applicable)
├── notebooks/                  # Jupyter notebooks for analysis
│   ├── training_analysis.ipynb
│   └── visualization.ipynb
├── data/                       # Training data (if applicable)
├── checkpoints/                # Saved model weights
└── tests/                      # Project-specific tests
```

**When to add code here**:
- ✅ Demonstrating a specific project (from RL_Implementation_Roadmap.md)
- ✅ Combining `rl_toolkit` components in novel ways
- ✅ Ablation studies, benchmarks, experiments
- ✅ Training scripts for neural networks

**Quality bar**: Less strict than `rl_toolkit/`, but still:
- Clear README explaining the project
- Runnable scripts with command-line arguments
- Reproducible experiments (seeds, hyperparameters logged)

---

### **Tier 3: `Week_X/final/day_Y/code/` - Pedagogical Exercises**

**Purpose**: Friday coding sessions verifying theoretical concepts from that week.

**Contents**:
- Numerical verification of theorems
- Simple visualizations
- Theory-to-code bridges
- NOT meant to be reusable

**When to add code here**:
- ✅ Weekly Friday coding session (30-40 minutes)
- ✅ Verifying a theorem numerically (e.g., Fubini, Lebesgue integration)
- ✅ Quick visualization to build intuition

**Quality bar**: Minimal
- Must run without errors
- Comments explaining theory connection
- No need for tests or production-quality code

---

## Complete Directory Structure

**Detailed file tree for the `code/` directory:**

```
code/
├── README.md                        # Package overview, installation, quick start
├── Code_Organization_Guide.md       # This file - detailed standards and conventions
├── pyproject.toml                   # Python package configuration
├── requirements.txt                 # Dependencies (NumPy, PyTorch, JAX, Flask, etc.)
├── setup.py                         # Editable install: pip install -e .
│
├── rl_toolkit/                      # Reusable infrastructure (grows incrementally)
│   ├── __init__.py
│   ├── envs/                        # Environment implementations
│   │   ├── __init__.py
│   │   ├── mdp.py                   # Abstract MDP interface (Project 4)
│   │   ├── chain.py                 # Markov chains (Project 1)
│   │   ├── gridworld.py             # GridWorld variants (Project 4)
│   │   ├── tictactoe.py             # Tic-Tac-Toe (Project 4.5)
│   │   ├── connect_four.py          # Connect Four (Project 8.5)
│   │   ├── gomoku.py                # Gomoku (Project 11.5)
│   │   └── reversi.py               # Reversi/Othello (Project 12)
│   ├── algorithms/                  # Core RL algorithms
│   │   ├── __init__.py
│   │   ├── dp.py                    # Value/policy iteration (Project 5)
│   │   ├── minimax.py               # Minimax algorithm (Project 4.5)
│   │   ├── bandits.py               # UCB, Thompson (Projects 6-7)
│   │   ├── mcts.py                  # UCT, AlphaZero MCTS (Projects 8.5, 11.5, 12)
│   │   ├── td.py                    # TD(0), TD(λ), LSTD (Project 9)
│   │   ├── qlearning.py             # Tabular + DQN (Project 10)
│   │   └── policy_gradient.py       # REINFORCE, PPO (Project 11)
│   ├── networks/                    # Neural network architectures
│   │   ├── __init__.py
│   │   ├── value_net.py             # Value function approximators
│   │   ├── conv_value_net.py        # Convolutional value net (Project 11.5)
│   │   ├── policy_net.py            # Policy networks
│   │   └── alphazero_net.py         # Dual-head architecture (Project 12)
│   ├── utils/                       # Shared utilities
│   │   ├── __init__.py
│   │   ├── logger.py                # TensorBoard/W&B logging
│   │   ├── replay_buffer.py         # Experience replay
│   │   ├── viz.py                   # Visualization (heatmaps, plots)
│   │   ├── board_viz.py             # Board rendering (ASCII) (Project 4.5)
│   │   ├── pygame_board.py          # Pygame GUI framework (Project 4.5)
│   │   ├── game_interface.py        # Abstract human input (Project 4.5)
│   │   └── theory_check.py          # Verify SA hygiene, contraction, etc.
│   └── web/                         # Web interface infrastructure (Project 8.5+)
│       ├── __init__.py
│       ├── app.py                   # Flask/FastAPI backend
│       ├── api.py                   # REST API endpoints
│       ├── templates/
│       │   ├── base.html            # Base template with CSS
│       │   ├── game.html            # Game board interface
│       │   └── training_dashboard.html  # Training metrics (Project 12)
│       └── static/
│           ├── css/
│           │   └── board.css        # Board styling
│           └── js/
│               ├── board.js         # Board rendering (Canvas)
│               ├── game_logic.js    # Move validation, UI updates
│               ├── mcts_viz.js      # MCTS tree visualization (Project 8.5)
│               ├── nn_heatmap.js    # Neural net eval heatmap (Project 11.5)
│               └── selfplay_monitor.js  # Self-play dashboard (Project 12)
│
├── projects/                        # 15 milestone project implementations
│   ├── project_01_markov_chains/
│   │   ├── README.md                # Project goals, theory connections
│   │   ├── markov_chain_lab.py      # Main implementation
│   │   ├── experiments.py           # Numerical experiments
│   │   └── notebooks/
│   │       └── visualizations.ipynb # Interactive visualizations
│   ├── project_02_mcmc/
│   ├── project_03_general_state_spaces/
│   ├── project_04_gridworld_mdp/
│   ├── project_04.5_tictactoe/      # NEW: Exact DP solution (Week 24)
│   │   ├── README.md
│   │   ├── solve_exact_dp.py
│   │   ├── minimax_implementation.py
│   │   ├── play_human_vs_ai.py
│   │   ├── play_gui.py
│   │   └── notebooks/
│   ├── project_05_dp_algorithms/
│   ├── project_06_bandits/
│   ├── project_07_thompson_sampling/
│   ├── project_08_contextual_bandits/
│   ├── project_08.5_connect_four/   # NEW: MCTS + web interface (Week 31)
│   │   ├── README.md
│   │   ├── mcts_implementation.py
│   │   ├── heuristic_eval.py
│   │   ├── web_interface.py
│   │   ├── benchmarks.py
│   │   └── notebooks/
│   ├── project_09_td_learning/
│   ├── project_10_qlearning_dqn/
│   ├── project_11_policy_gradients/
│   ├── project_11.5_gomoku/         # NEW: Neural net + MCTS (Weeks 40-41)
│   │   ├── README.md
│   │   ├── train_value_net.py
│   │   ├── mcts_with_nn.py
│   │   ├── web_interface.py
│   │   ├── expert_games/
│   │   ├── checkpoints/
│   │   └── notebooks/
│   └── project_12_alphazero_lite/   # Capstone (Weeks 42-48)
│       ├── README.md
│       ├── reversi_env.py
│       ├── mcts.py
│       ├── neural_net.py
│       ├── self_play.py
│       ├── train.py
│       ├── arena.py
│       ├── web_interface.py
│       └── notebooks/
│
├── tests/                           # Unit tests for rl_toolkit
│   ├── __init__.py
│   ├── test_envs.py
│   ├── test_game_engines.py         # Game logic tests
│   ├── test_algorithms.py
│   ├── test_mcts.py                 # MCTS-specific tests
│   └── test_theory_convergence.py   # Theory validation tests
│
└── notebooks/                       # Shared Jupyter notebooks
    ├── bandits_comparison.ipynb
    ├── td_convergence_analysis.ipynb
    └── value_iteration_visualization.ipynb
```

---

## Code Standards

### Type Hints (PEP 484)

**All functions in `rl_toolkit/` must have type hints.**

```python
from typing import Optional, List, Dict, Tuple
import numpy as np
import torch

def bellman_operator(
    V: np.ndarray,           # Shape: (num_states,)
    policy: Optional[np.ndarray] = None,  # Shape: (num_states, num_actions)
    gamma: float = 0.99
) -> np.ndarray:
    """
    Apply Bellman operator to value function V.

    Theory: T^π V = R^π + γ P^π V ([THM-24.X.Y])

    Args:
        V: Value function (one value per state)
        policy: Policy matrix (if None, use optimal policy)
        gamma: Discount factor

    Returns:
        Updated value function after one Bellman backup
    """
    ...
```

**Benefits**:
- IDE autocomplete works
- Type checking with `mypy`
- Self-documenting code

**Common types**:
- `np.ndarray` - NumPy arrays
- `torch.Tensor` - PyTorch tensors
- `List[int]`, `Dict[str, float]`, `Tuple[int, int]`
- `Optional[X]` - X or None

---

### Docstrings (NumPy Style)

**All public functions/classes in `rl_toolkit/` must have docstrings.**

**Format**:
```python
def function_name(arg1: type1, arg2: type2) -> return_type:
    """
    One-line summary of what this function does.

    Theory: Reference to relevant theorem ([THM-X.Y.Z]) or definition ([DEF-X.Y.Z]).

    More detailed explanation of the function's purpose, algorithms used,
    and any important implementation details.

    Args:
        arg1: Description of arg1
        arg2: Description of arg2

    Returns:
        Description of return value

    Raises:
        ValueError: When arg1 is negative
        RuntimeError: When algorithm fails to converge

    Example:
        >>> result = function_name(5, 10)
        >>> print(result)
        15
    """
    ...
```

**Theory references**:
- Always cite relevant theorems: `"[THM-24.2.1] guarantees convergence..."`
- Cite Dubois's definitions: `"Using [DEF-5.3.2] (stationary distribution)..."`
- Explain theory-practice gaps: `"Theory assumes tabular case; we use neural net (no guarantees)."`

---

### Code Comments

**When to comment**:
- ✅ Non-obvious algorithmic choices: "Why this epsilon-greedy parameter?"
- ✅ Theory connections: "This is the UCT formula ([THM-28.X.Y])"
- ✅ Numerical stability hacks: "Log-space to avoid underflow"
- ✅ TODOs: "TODO: Replace with PyTorch einsum for efficiency"

**When NOT to comment**:
- ❌ Obvious code: `x = x + 1  # Increment x` (redundant)
- ❌ Stale comments that don't match code

**Example**:
```python
def uct_score(self, node: Node, parent_visits: int) -> float:
    """
    UCT selection formula ([THM-28.X.Y]).

    Theory: Balances exploitation (Q-value) and exploration (√log term).
    """
    exploitation = node.total_value / node.visit_count

    # Exploration term: √(2 log(N(parent)) / N(child))
    # Factor of √2 is theoretically optimal for UCB1
    exploration = np.sqrt(2 * np.log(parent_visits) / node.visit_count)

    return exploitation + self.c * exploration
```

---

## Import Conventions

### Importing from `rl_toolkit`

**Standard imports**:
```python
# Environments
from rl_toolkit.envs import MDP, GridWorld, TicTacToe, ConnectFour

# Algorithms
from rl_toolkit.algorithms.dp import value_iteration, policy_iteration
from rl_toolkit.algorithms.mcts import MCTS, UCTNode
from rl_toolkit.algorithms.bandits import UCB1, ThompsonSampling

# Neural networks
from rl_toolkit.networks import ValueNet, PolicyNet, AlphaZeroNet

# Utilities
from rl_toolkit.utils.viz import plot_value_function, plot_training_curve
from rl_toolkit.utils.logger import Logger
from rl_toolkit.utils.theory_check import verify_contraction, check_robbins_monro
```

**Avoid wildcard imports**:
```python
# BAD
from rl_toolkit.envs import *

# GOOD
from rl_toolkit.envs import GridWorld
```

---

### Standard library imports order

**Follow PEP 8 import order**:

```python
# 1. Standard library imports
import os
import sys
from typing import List, Optional

# 2. Third-party imports
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 3. Local application imports
from rl_toolkit.envs import GridWorld
from rl_toolkit.algorithms.dp import value_iteration
```

---

## File Organization Patterns

### When to Create a New File in `rl_toolkit/`

**Decision tree**:

1. **Is it a new environment?**
   - Yes → Create `rl_toolkit/envs/new_env.py`
   - Must inherit from `MDP` base class

2. **Is it a new algorithm?**
   - Yes → Add to existing file if related (`dp.py`, `bandits.py`, etc.)
   - Or create new file if it's a major new category

3. **Is it a neural network architecture?**
   - Yes → Create `rl_toolkit/networks/new_net.py`
   - Must inherit from `nn.Module`

4. **Is it a utility/helper function?**
   - Yes → Add to `rl_toolkit/utils/` in appropriate file
   - `viz.py` for visualization
   - `logger.py` for logging
   - `theory_check.py` for validation

5. **Is it game-specific?**
   - Yes → Might belong in `projects/` instead of `rl_toolkit/`

---

### File Size Guidelines

**Keep files focused** (single responsibility principle):
- **Small**: 100-300 lines (single algorithm, single environment)
- **Medium**: 300-600 lines (related algorithms, complex environment)
- **Large**: 600+ lines (should probably be split)

**When to split a file**:
- File has multiple unrelated responsibilities
- File is hard to navigate (> 800 lines)
- Logical groupings emerge (e.g., `bandits.py` → `bandits/ucb.py` + `bandits/thompson.py`)

---

## Theory Validation Requirements

**Every algorithm in `rl_toolkit/` must have theory validation.**

### Validation Checklist

For each algorithm, verify:

#### **1. Convergence (if applicable)**
```python
def test_value_iteration_convergence():
    """Value iteration should converge to V* on simple MDP."""
    env = GridWorld(size=5, gamma=0.9)
    V_star, policy = value_iteration(env, epsilon=1e-6)

    # Theory: ||T* V - V||_∞ < ε  implies V is ε-optimal ([THM-24.X.Y])
    residual = bellman_residual(env, V_star)
    assert residual < 1e-6, f"Bellman residual {residual:.2e} too large"
```

#### **2. Correctness on Toy Problem**
```python
def test_mcts_on_trivial_game():
    """MCTS should find optimal move in trivial game."""
    # Game: Two moves, one leads to +1 reward, other to -1
    env = TrivialGame()
    mcts = MCTS(num_simulations=1000)
    action = mcts.search(env)

    # Should always pick the +1 move
    assert action == 0, f"MCTS picked suboptimal action {action}"
```

#### **3. Theory Compliance**

For stochastic approximation algorithms (TD, Q-learning, policy gradients):
```python
def test_td_robbins_monro_conditions():
    """TD(0) step sizes must satisfy Robbins-Monro conditions."""
    step_sizes = [1 / (n + 1) for n in range(1000)]

    # Condition 1: Σ αₙ = ∞
    assert sum(step_sizes[:100]) > 10, "Step sizes sum too small"

    # Condition 2: Σ αₙ² < ∞
    assert sum(s**2 for s in step_sizes) < 10, "Step sizes squared sum too large"
```

---

### Numerical Verification Examples

**Verify theorem predictions**:

```python
def test_gamma_affects_convergence_rate():
    """Theorem: Convergence rate is O(γⁿ) for value iteration."""
    env = GridWorld(size=5)

    for gamma in [0.5, 0.9, 0.99]:
        env.gamma = gamma
        iterations_to_converge = value_iteration(env, epsilon=1e-6, return_iterations=True)

        # Higher gamma → more iterations (theory predicts this)
        print(f"γ={gamma:.2f}: {iterations_to_converge} iterations")
```

---

## Game Engine Abstractions

All game environments should follow a common interface for consistency.

### Base Game Interface

```python
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
import numpy as np

class TwoPlayerGame(ABC):
    """
    Abstract base class for two-player, zero-sum, perfect-information games.

    Used by: Tic-Tac-Toe, Connect Four, Gomoku, Reversi.
    """

    @abstractmethod
    def reset(self) -> np.ndarray:
        """Reset game to initial state. Returns initial board state."""
        pass

    @abstractmethod
    def legal_moves(self) -> List[int]:
        """Return list of legal move indices."""
        pass

    @abstractmethod
    def step(self, action: int) -> Tuple[np.ndarray, float, bool]:
        """
        Execute one move.

        Args:
            action: Move index (from legal_moves())

        Returns:
            next_state: New board state
            reward: +1 (win), -1 (loss), 0 (draw/ongoing)
            done: True if game is over
        """
        pass

    @abstractmethod
    def render(self, mode: str = "ascii") -> Optional[str]:
        """
        Render game state.

        Args:
            mode: "ascii" (terminal), "pygame" (GUI), or "canvas" (web)

        Returns:
            String representation (for "ascii"), else None
        """
        pass

    @abstractmethod
    def clone(self) -> "TwoPlayerGame":
        """Return deep copy of current game state (for MCTS)."""
        pass

    @property
    @abstractmethod
    def current_player(self) -> int:
        """Return current player (1 or -1)."""
        pass

    @property
    @abstractmethod
    def board_shape(self) -> Tuple[int, ...]:
        """Return shape of board (e.g., (3, 3) for Tic-Tac-Toe)."""
        pass
```

### Implementation Example

```python
class TicTacToe(TwoPlayerGame):
    """3×3 Tic-Tac-Toe. Player 1 is X, Player -1 is O."""

    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1  # Player 1 starts

    def reset(self) -> np.ndarray:
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1
        return self.board.copy()

    def legal_moves(self) -> List[int]:
        """Return indices of empty squares (row-major order)."""
        return [i for i in range(9) if self.board.flat[i] == 0]

    def step(self, action: int) -> Tuple[np.ndarray, float, bool]:
        row, col = divmod(action, 3)
        self.board[row, col] = self.player

        # Check win
        if self._check_win(self.player):
            return self.board.copy(), 1.0, True

        # Check draw
        if len(self.legal_moves()) == 0:
            return self.board.copy(), 0.0, True

        # Continue game
        self.player *= -1
        return self.board.copy(), 0.0, False

    def _check_win(self, player: int) -> bool:
        """Check if player has won."""
        # Rows, columns, diagonals
        for i in range(3):
            if np.all(self.board[i, :] == player):
                return True
            if np.all(self.board[:, i] == player):
                return True
        if np.all(np.diag(self.board) == player):
            return True
        if np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

    # ... other methods
```

---

## Web Interface Standards

### Flask App Structure

All web-based games follow this pattern:

```
code/rl_toolkit/web/
├── app.py                  # Main Flask app (shared across games)
├── api.py                  # REST API endpoints
├── templates/
│   ├── base.html           # Base template with CSS/JS imports
│   ├── game.html           # Generic game board interface
│   └── tictactoe.html      # Game-specific template (extends game.html)
└── static/
    ├── css/
    │   └── board.css       # Board styling
    └── js/
        ├── board.js        # Generic board rendering
        ├── tictactoe.js    # Game-specific rendering logic
        └── mcts_viz.js     # MCTS visualization (reusable)
```

### REST API Conventions

**Standard endpoints** (all games):

```python
from flask import Flask, request, jsonify
from rl_toolkit.envs import TicTacToe
from rl_toolkit.algorithms.mcts import MCTS

app = Flask(__name__)

@app.route('/api/new_game', methods=['POST'])
def new_game():
    """Start a new game."""
    game = TicTacToe()
    game_id = generate_game_id()
    store_game(game_id, game)
    return jsonify({'game_id': game_id, 'board': game.board.tolist()})

@app.route('/api/move', methods=['POST'])
def make_move():
    """
    Human makes a move, then AI responds.

    Request body:
        {
            "game_id": "abc123",
            "action": 4  // Index of move (0-8 for Tic-Tac-Toe)
        }

    Response:
        {
            "board": [[0, 1, 0], [0, -1, 0], [0, 0, 0]],
            "ai_move": 2,
            "game_over": false,
            "winner": null,
            "mcts_stats": {  // Optional: for visualization
                "visit_counts": [10, 5, 100, ...],
                "q_values": [0.5, 0.3, 0.8, ...]
            }
        }
    """
    data = request.json
    game = load_game(data['game_id'])

    # Human move
    game.step(data['action'])

    # AI move (if game not over)
    if not game.is_terminal():
        mcts = MCTS(num_simulations=1000)
        ai_move = mcts.search(game)
        game.step(ai_move)
    else:
        ai_move = None

    return jsonify({
        'board': game.board.tolist(),
        'ai_move': ai_move,
        'game_over': game.is_terminal(),
        'winner': game.get_winner(),
        'mcts_stats': mcts.get_stats()  // For visualization
    })
```

### JavaScript Board Rendering

**Canvas API** (preferred for flexibility):

```javascript
class BoardRenderer {
    constructor(canvasId, boardSize) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.boardSize = boardSize;  // e.g., 3 for 3×3
        this.cellSize = this.canvas.width / boardSize;
    }

    render(board) {
        // board is 2D array: [[0, 1, 0], [0, -1, 0], [0, 0, 0]]
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw grid
        this.drawGrid();

        // Draw pieces
        for (let row = 0; row < this.boardSize; row++) {
            for (let col = 0; col < this.boardSize; col++) {
                const piece = board[row][col];
                if (piece !== 0) {
                    this.drawPiece(row, col, piece);
                }
            }
        }
    }

    drawGrid() {
        // Draw lines separating cells
        for (let i = 0; i <= this.boardSize; i++) {
            const pos = i * this.cellSize;
            // Vertical line
            this.ctx.beginPath();
            this.ctx.moveTo(pos, 0);
            this.ctx.lineTo(pos, this.canvas.height);
            this.ctx.stroke();
            // Horizontal line
            this.ctx.beginPath();
            this.ctx.moveTo(0, pos);
            this.ctx.lineTo(this.canvas.width, pos);
            this.ctx.stroke();
        }
    }

    drawPiece(row, col, player) {
        const x = col * this.cellSize + this.cellSize / 2;
        const y = row * this.cellSize + this.cellSize / 2;

        if (player === 1) {
            // Draw X
            this.drawX(x, y, this.cellSize * 0.8);
        } else {
            // Draw O
            this.drawO(x, y, this.cellSize * 0.4);
        }
    }

    // ... drawX(), drawO(), etc.
}
```

---

## Testing Philosophy

### Test Organization

```
code/tests/
├── test_envs.py                 # Test environment implementations
├── test_game_engines.py         # Game-specific tests (move validation, win detection)
├── test_algorithms.py           # Test RL algorithms
├── test_mcts.py                 # MCTS-specific tests
└── test_theory_convergence.py   # Theory validation tests
```

### Test Categories

#### **1. Unit Tests** (basic functionality)
```python
def test_gridworld_step():
    """GridWorld.step() should update state correctly."""
    env = GridWorld(size=5)
    env.reset()
    state, reward, done = env.step(0)  # Move right

    assert state != env.current_state, "State should have changed"
    assert not done, "Game shouldn't be over after one step"
```

#### **2. Integration Tests** (components working together)
```python
def test_mcts_with_tictactoe():
    """MCTS should be able to play a full Tic-Tac-Toe game."""
    game = TicTacToe()
    mcts = MCTS(num_simulations=100)

    while not game.is_terminal():
        action = mcts.search(game)
        game.step(action)

    assert game.is_terminal(), "Game should eventually terminate"
```

#### **3. Theory Validation Tests** (numerical verification)
```python
def test_bellman_contraction():
    """Bellman operator should be γ-contraction ([THM-24.X.Y])."""
    env = GridWorld(size=5, gamma=0.9)

    V1 = np.random.rand(env.num_states)
    V2 = np.random.rand(env.num_states)

    TV1 = bellman_operator(env, V1)
    TV2 = bellman_operator(env, V2)

    # Theory: ||T V1 - T V2||_∞ ≤ γ ||V1 - V2||_∞
    lhs = np.max(np.abs(TV1 - TV2))
    rhs = env.gamma * np.max(np.abs(V1 - V2))

    assert lhs <= rhs + 1e-10, f"Contraction property violated: {lhs} > {rhs}"
```

---

## Git Workflow for Code

### Commit Message Conventions

Follow same conventions as theory files:

**Good commit messages**:
- `"Add Tic-Tac-Toe environment (Project 4.5)"`
- `"Implement MCTS with UCT selection ([THM-28.X.Y])"`
- `"Fix Bellman operator bug in policy iteration"`
- `"Add web interface for Connect Four (Project 8.5)"`

**Bad commit messages**:
- `"Update code"`
- `"Fix bug"`
- `"asdf"`

### When to Commit

**Commit frequently** (more frequent than theory files):
- After adding a new function/class
- After fixing a bug
- After passing a new test
- Before refactoring

**Don't commit**:
- Broken code (tests failing)
- Temporary debug prints
- Large binary files (model checkpoints > 100MB)

### Branch Strategy

**Simple branching** (no need for complex GitFlow):
- `main`: Stable code, always works
- `feature/project-XX`: Feature branches for major projects
- `bugfix/description`: Bug fixes

**Merge to main** only when:
- All tests pass (`pytest code/tests/`)
- Code is documented
- PR reviewed (if working with others)

---

## Common Tasks

### Task 1: Add a New Environment

**Example**: Adding "Checkers" game

1. **Create file**: `code/rl_toolkit/envs/checkers.py`

2. **Inherit from `TwoPlayerGame`**:
```python
from rl_toolkit.envs.base import TwoPlayerGame

class Checkers(TwoPlayerGame):
    def __init__(self, board_size: int = 8):
        ...
    # Implement abstract methods
```

3. **Add tests**: `code/tests/test_game_engines.py`
```python
def test_checkers_legal_moves():
    game = Checkers()
    moves = game.legal_moves()
    assert len(moves) > 0, "Should have legal moves at start"
```

4. **Update `__init__.py`**:
```python
# code/rl_toolkit/envs/__init__.py
from .checkers import Checkers
```

5. **Commit**:
```bash
git add code/rl_toolkit/envs/checkers.py code/tests/test_game_engines.py
git commit -m "Add Checkers environment"
```

---

### Task 2: Add a New Project

**Example**: Adding "Project 13: Checkers with MCTS"

1. **Create project folder**:
```bash
mkdir -p code/projects/project_13_checkers
cd code/projects/project_13_checkers
```

2. **Create README.md** (copy template from other projects)

3. **Create main implementation**: `mcts_checkers.py`

4. **Add experiments**: `benchmarks.py`, `ablations.py`

5. **Update RL_Implementation_Roadmap.md** (if not already listed)

6. **Commit**:
```bash
git add code/projects/project_13_checkers/
git commit -m "Add Project 13: Checkers with MCTS"
```

---

### Task 3: Run All Tests

```bash
cd code
pytest tests/ -v
```

**Run specific test category**:
```bash
pytest tests/test_game_engines.py -v
pytest tests/test_theory_convergence.py -v
```

**Run with coverage**:
```bash
pytest tests/ --cov=rl_toolkit --cov-report=html
open htmlcov/index.html  # View coverage report
```

---

### Task 4: Type Check Code

```bash
cd code
mypy rl_toolkit/ --ignore-missing-imports
```

**Fix common type errors**:
- Missing return type: Add `-> ReturnType`
- Missing argument type: Add `arg: ArgType`
- `Any` type: Replace with specific type

---

### Task 5: Deploy Web Demo

**Local testing**:
```bash
cd code/projects/project_08.5_connect_four
python web_interface.py
# Open http://localhost:5000 in browser
```

**Deploy to Heroku** (optional):
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create my-rl-game-demo
git push heroku main
```

**Deploy to Railway** (simpler):
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy
railway login
railway init
railway up
```

---

## Summary: Code Quality Checklist

Before marking a component as "complete":

- ✅ Type hints on all functions
- ✅ Docstrings with theory references
- ✅ Unit tests passing
- ✅ Theory validation test (if applicable)
- ✅ Code formatted (use `black` or `autopep8`)
- ✅ No debug prints left in code
- ✅ Git commit with clear message
- ✅ Updated relevant documentation (this guide, README, etc.)

**Remember**: Code in this repository is both:
1. **Learning tool** (helps students understand RL)
2. **Research artifact** (publishable alongside textbook)

Quality matters. But don't let perfection block progress—iterate!

---

**Questions?** See the main `RL_Implementation_Roadmap.md` or ask Professor Dubois.

— Max
