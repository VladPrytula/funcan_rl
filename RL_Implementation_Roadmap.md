# RL Implementation Roadmap: Progressive Projects Leading to AlphaZero-Lite

**Author**: Dr. Max Rubin
**Status**: Planning Document (Week 2)
**Purpose**: Structured progression of RL implementations building toward capstone project

---

## Philosophy: Building Blocks, Not Toy Examples

This isn't a collection of Jupyter notebooks with "hello world" RL. Each project is:
- **Production-quality**: Type hints, tests, logging, reproducibility
- **Theory-grounded**: Explicitly connects to Dubois's theorems
- **Incrementally complex**: Each builds on previous infrastructure
- **Capstone-relevant**: Directly contributes code/concepts for AlphaZero-Lite

**By Week 48, we'll have:**
- A battle-tested codebase spanning tabular → function approximation → deep RL
- Reusable infrastructure (environments, loggers, visualizers, evaluators)
- Evidence that theory works in practice (and where it doesn't)
- AlphaZero-Lite as the culmination, not a standalone hack

---

## Project Sequence (12 Major Milestones)

### 🏗️ **Foundation Tier** (Weeks 5-12: Markov Chains)

#### **Project 1: Markov Chain Laboratory** (Week 5-6)
**Timing**: After finite Markov chains theory (Weeks 5-6)

**Deliverables**:
- `markov_chain.py`: Transition matrix class with Chapman-Kolmogorov
- Stationary distribution computation (eigenvalue decomposition)
- Detailed balance checker
- Random walk on graphs (cycle, grid, complete)

**Theory Connections**:
- [THM-5.X.Y]: Perron-Frobenius → unique stationary distribution
- [THM-6.X.Y]: Coupling method for mixing time bounds

**Code Preview**:
```python
class FiniteMarkovChain:
    """
    Finite-state Markov chain with transition matrix P.

    Theory: Irreducible + aperiodic → unique stationary π (Week 5).
    Mixing: τ_mix ≤ (λ₂*)^{-1} log(1/(π_min ε)) (Week 6).
    """
    def __init__(self, P: np.ndarray):
        self.P = P
        self.n_states = P.shape[0]
        self._validate()

    def stationary_distribution(self) -> np.ndarray:
        """Compute π via left eigenvector with eigenvalue 1."""
        ...

    def mixing_time(self, epsilon: float = 0.25) -> int:
        """Estimate τ_mix via total variation distance."""
        ...
```

**Capstone Relevance**: Understanding stationary distributions prepares for policy evaluation in MDPs.

---

#### **Project 2: MCMC Sampler Suite** (Week 7)
**Timing**: After MCMC theory (Week 7)

**Deliverables**:
- Metropolis-Hastings for discrete distributions
- Gibbs sampler for product spaces
- Convergence diagnostics (trace plots, Gelman-Rubin)
- Application: 2D Ising model (if time allows)

**Theory Connections**:
- [THM-7.X.Y]: M-H detailed balance → correct stationary distribution
- Path coupling for mixing time

**Capstone Relevance**: Thompson Sampling (Week 29) is posterior MCMC. This is the foundation.

---

#### **Project 3: General State Space Visualization** (Week 10)
**Timing**: After general state spaces (Week 10)

**Deliverables**:
- Gaussian kernel on [0,1] with reflection boundaries
- Visualize density evolution over time
- Verify Feller property numerically
- Animated convergence to stationarity

**Theory Connections**:
- [DEF-10.X.Y]: Feller property → weak continuity
- φ-irreducibility on continuous spaces

**Capstone Relevance**: Continuous state spaces appear in robotics applications (optional extensions).

---

### 🎯 **MDP Core** (Weeks 23-26: Dynamic Programming)

#### **Project 4: GridWorld MDP Playground** (Week 23-24)
**Timing**: After MDP formalism and Bellman equations (Week 23)

**Deliverables**:
- `mdp.py`: Abstract MDP interface (S, A, P, R, γ)
- GridWorld environment (customizable obstacles, rewards)
- Bellman operators: T^π (evaluation), T* (optimality)
- Visualization: value functions as heatmaps

**Theory Connections**:
- [THM-23.X.Y]: Bellman consistency via tower property
- [THM-24.X.Z]: Bellman optimality operator is γ-contraction

**Code Preview**:
```python
class MDP:
    """
    Markov Decision Process: (S, A, P, R, γ)

    Theory: V* = T* V* where T* is γ-contraction (Banach fixed-point, Week 16).
    """
    def bellman_operator(self, V: np.ndarray, policy: Optional[np.ndarray] = None) -> np.ndarray:
        """
        Policy evaluation: T^π V = R^π + γ P^π V
        Optimal: T* V = max_a [R^a + γ P^a V]

        Convergence: ||T^n V - V*||_∞ ≤ γ^n ||V - V*||_∞  ([THM-16.X.Y])
        """
        ...
```

**Capstone Relevance**: Bellman operators are the backbone of value iteration → MCTS evaluation.

---

#### **Project 5: Dynamic Programming Algorithms** (Week 24-25)
**Timing**: After value/policy iteration theory (Weeks 24-25)

**Deliverables**:
- Value iteration with convergence tracking
- Policy iteration (policy evaluation + greedy improvement)
- Modified policy iteration (partial evaluation)
- Linear programming formulation (optional)

**Theory Connections**:
- [THM-24.X.Y]: Value iteration convergence rate
- [THM-25.X.Y]: Policy iteration finite convergence

**Empirical Questions**:
- How many iterations until convergence (ε-optimal)?
- Policy iteration vs. value iteration: which is faster?
- Impact of discount factor γ on convergence speed

**Capstone Relevance**: Policy iteration logic → MCTS policy improvement.

---

#### **Project 4.5: Tic-Tac-Toe - Exact Solution with Dynamic Programming** (Week 24)
**Timing**: Right after GridWorld DP (Projects 4-5)

**Complexity**: Tiny state space (~5,000 states after symmetry reduction), exactly solvable

**Deliverables**:
- Complete game engine (board state, legal moves, win detection)
- Exact value iteration to V* (optimal play for both players)
- Minimax algorithm (backward induction on game tree)
- ASCII + Pygame GUI visualization
- Human vs. AI gameplay (terminal + GUI)
- Formal proof: game is a draw under optimal play

**Theory Connections**:
- [THM-24.X.Y]: Finite-horizon MDP (game tree as DAG)
- Minimax = value iteration on adversarial MDP
- Nash equilibrium in two-player zero-sum games
- Connection to Bellman equation in game-theoretic setting

**Code Preview**:
```python
class TicTacToe:
    """
    3×3 Tic-Tac-Toe environment.

    Theory: Finite zero-sum game, solvable via backward induction.
    State space: ~5,000 positions (after symmetry).
    Outcome: Draw under optimal play (proof via value iteration).
    """
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1  # Player 1 starts

    def is_terminal(self) -> bool:
        """Check for win or draw."""
        return self.check_win(1) or self.check_win(-1) or len(self.legal_moves()) == 0

    def value_iteration_solve(self) -> Dict[str, float]:
        """
        Exact DP solution via backward induction.

        Returns: V*(s) for all states s (player 1's perspective)
        """
        ...
```

**Infrastructure Built** (reusable for all future games):
- `code/rl_toolkit/utils/board_viz.py` - ASCII rendering for n×n boards
- `code/rl_toolkit/utils/pygame_board.py` - Pygame GUI framework
- `code/rl_toolkit/utils/game_interface.py` - Abstract human input interface

**Deliverable Files**:
- `code/rl_toolkit/envs/tictactoe.py`
- `code/rl_toolkit/algorithms/minimax.py`
- `code/projects/project_04.5_tictactoe/`
  - `solve_exact_dp.py` - Value iteration solution
  - `minimax_implementation.py` - Minimax algorithm
  - `play_human_vs_ai.py` - Terminal gameplay
  - `play_gui.py` - Pygame interface
  - `notebooks/game_tree_analysis.ipynb`

**Capstone Relevance**:
- Game engine patterns established
- First human-playable demo
- Minimax → MCTS connection (minimax is exhaustive search; MCTS is sampled search)

**Time Investment**: 1 week (can use Project 5 buffer time)

---

### 🎰 **Exploration Fundamentals** (Weeks 27-31: Bandits)

#### **Project 6: Multi-Armed Bandit Testbed** (Week 27-28)
**Timing**: After bandit regret framework and UCB (Weeks 27-28)

**Deliverables**:
- `bandit.py`: Abstract bandit interface
- Algorithms: ε-greedy, UCB1, UCB-V
- Regret tracking and visualization
- Testbed: Bernoulli, Gaussian, heavy-tailed rewards

**Theory Connections**:
- [THM-28.X.Y]: UCB1 achieves O(√(T log T)) regret
- Hoeffding's inequality → confidence bounds

**Code Preview**:
```python
class UCB1:
    """
    Upper Confidence Bound algorithm.

    Theory: R(T) ≤ 8 log(T) Σ_i Δ_i + (1 + π²/3) Σ_i Δ_i  ([THM-28.X.Y])
    Practice: Optimism under uncertainty drives exploration.
    """
    def select_arm(self, t: int) -> int:
        ucb_values = self.mean_rewards + np.sqrt(2 * np.log(t) / self.arm_counts)
        return np.argmax(ucb_values)
```

**Capstone Relevance**: UCB logic → UCT in MCTS (tree exploration).

---

#### **Project 7: Thompson Sampling and Bayesian Bandits** (Week 29)
**Timing**: After Thompson Sampling theory (Week 29)

**Deliverables**:
- Beta-Bernoulli Thompson Sampling
- Gaussian Thompson Sampling
- Posterior visualization over time
- Regret comparison vs. UCB

**Theory Connections**:
- [THM-29.X.Y]: Thompson Sampling Bayes-optimal
- Connection to MCMC (posterior sampling = Gibbs step)

**Capstone Relevance**: Bayesian RL and posterior sampling for exploration in AlphaZero-Lite extensions.

---

#### **Project 8: Contextual Bandits with Linear Models** (Week 30)
**Timing**: After contextual bandits theory (Week 30)

**Deliverables**:
- LinUCB algorithm
- Ridge regression for reward estimation
- Feature engineering for context
- Real dataset: MovieLens recommendation

**Theory Connections**:
- [THM-30.X.Y]: LinUCB regret bound with d-dimensional features
- Connection to online learning

**Capstone Relevance**: Contextual decision-making → state-dependent action selection in MDPs.

---

#### **Project 8.5: Connect Four - MCTS with Heuristic Evaluation** (Week 31)
**Timing**: After bandits (Projects 6-8), before deep RL

**Complexity**: Medium state space (~4 trillion positions), too large for exact DP

**Deliverables**:
- Connect Four game engine (7×6 board, gravity mechanics)
- Monte Carlo Tree Search (UCT algorithm from Project 6)
- Heuristic evaluation function (hand-crafted features):
  - Center control bonus (center columns more valuable)
  - Connected pieces heuristic (2-in-a-row, 3-in-a-row scores)
  - Threat detection (immediate winning moves, blocking opponent wins)
  - Pattern recognition (common winning setups)
- **Web browser interface** (first web-based game):
  - Interactive board (click columns to drop pieces)
  - AI move visualization (show MCTS statistics)
  - Search tree exploration (visit counts, Q-values)
  - Real-time move generation
- Performance benchmarking:
  - MCTS simulations vs. win rate
  - Heuristic quality ablation
  - Time per move analysis

**Theory Connections**:
- [THM-28.X.Y]: UCT = UCB1 applied to game tree
- Exploration-exploitation in sequential decision-making
- Upper confidence bounds on action values Q(s,a)
- Connection to multi-armed bandits (each tree node = bandit problem)

**Code Preview**:
```python
class MCTS:
    """
    Monte Carlo Tree Search with UCT (Upper Confidence bounds for Trees).

    Theory: UCT uses UCB1 ([THM-28.X.Y]) to balance exploration/exploitation
    in game tree. Converges to minimax optimal policy as sims → ∞.
    """
    def __init__(self, exploration_constant: float = 1.41):
        self.c = exploration_constant  # √2 is theoretically optimal
        self.tree = {}  # Dict[state_hash, Node]

    def search(self, state: ConnectFour, num_simulations: int) -> int:
        """
        Run MCTS for num_simulations iterations.

        Returns: Best action according to visit counts.
        """
        for _ in range(num_simulations):
            # 1. Selection: UCT down to leaf
            # 2. Expansion: Add new node
            # 3. Simulation: Rollout with heuristic/random policy
            # 4. Backpropagation: Update statistics
            ...

    def uct_score(self, node: Node, parent_visits: int) -> float:
        """
        UCT formula: Q(s,a) + c √(log N(s) / N(s,a))

        Theory: Regret-minimizing selection rule ([THM-28.X.Y]).
        """
        exploitation = node.total_value / node.visit_count
        exploration = self.c * np.sqrt(np.log(parent_visits) / node.visit_count)
        return exploitation + exploration
```

**Infrastructure Built** (reusable for all future games):
- `code/rl_toolkit/algorithms/mcts.py` - Reusable MCTS framework
- `code/rl_toolkit/web/` - **Web interface infrastructure**:
  - `app.py` - Flask/FastAPI backend
  - `api.py` - REST API for move generation
  - `templates/` - HTML templates
  - `static/` - CSS/JavaScript for interactive boards
- Board rendering in browser (HTML Canvas)
- Real-time AI visualization

**Deliverable Files**:
- `code/rl_toolkit/envs/connect_four.py`
- `code/rl_toolkit/algorithms/mcts.py`
- `code/rl_toolkit/web/` (complete web framework)
- `code/projects/project_08.5_connect_four/`
  - `mcts_implementation.py` - MCTS with heuristics
  - `heuristic_eval.py` - Hand-crafted evaluation
  - `web_interface.py` - Flask app launcher
  - `benchmarks.py` - Performance tests
  - `notebooks/`
    - `mcts_ablation.ipynb` - Simulation count vs. win rate
    - `heuristic_tuning.ipynb` - Feature engineering analysis

**Why This Game**:
- Connect Four is complex enough to require search (can't solve exactly)
- Simple enough to run fast MCTS (100-1000 sims/move is reasonable)
- Students can **play against their AI in a web browser** (first interactive demo)
- Establishes MCTS infrastructure for Gomoku and Reversi

**Why MCTS Without Neural Nets**:
- Demonstrates core MCTS algorithm (UCT) before adding neural complexity
- Hand-crafted heuristics show what features matter (domain knowledge)
- Faster iteration (no training, just tune heuristic weights)
- Clear connection to bandit theory (UCB applied to trees)

**Capstone Relevance**:
- MCTS implementation → reused in Projects 11.5 and 12
- Web interface → reused for Gomoku and Reversi
- Heuristic evaluation → replaced by neural nets in later projects

**Time Investment**: 1-2 weeks (Week 31, buffer between bandits and deep RL)

---

### 🚀 **Function Approximation & Deep RL** (Weeks 32-37: Stochastic Approximation)

#### **Project 9: Temporal Difference Learning Suite** (Week 34-35)
**Timing**: After TD theory (Weeks 34-35)

**Deliverables**:
- **Tabular TD(0)**: Exact convergence on chain
- **Tabular TD(λ)**: Eligibility traces
- **Linear TD**: Feature-based value approximation
- **Least-Squares TD (LSTD)**: Closed-form solution

**Theory Connections**:
- [THM-34.X.Y]: TD(0) convergence via Robbins-Monro
- [THM-35.X.Y]: Linear TD projection theorem (Week 14 Hilbert spaces!)

**Stochastic Approximation Hygiene**:
```python
# Verify before claiming convergence:
# ✓ Step sizes: Σ αₙ = ∞, Σ αₙ² < ∞
# ✓ Noise: E[noise | past] = 0 (martingale difference)
# ✓ ODE: θ̇ = h(θ) is Lipschitz with stable attractor
```

**Empirical Questions**:
- TD(0) vs. TD(λ): bias-variance tradeoff?
- Linear TD: when does it diverge (Baird's counterexample)?
- LSTD: sample complexity vs. iterative TD

**Capstone Relevance**: TD learning → value network training in AlphaZero-Lite.

---

#### **Project 10: Q-Learning and Deep Q-Networks** (Week 36)
**Timing**: After Q-learning theory (Week 36)

**Deliverables**:
- **Tabular Q-learning**: GridWorld navigation
- **Deep Q-Network (DQN)**: CartPole, LunarLander
- Engineering: experience replay, target networks, ε-decay
- Ablation study: DQN vs. Q-learning vs. no target network

**Theory Connections**:
- [THM-36.X.Y]: Q-learning converges (tabular case)
- **Theory-practice gap**: Neural networks break convergence guarantees

**Why DQN Still Works**:
- Target networks reduce non-stationarity
- Experience replay breaks correlations
- But: no formal proof for neural case (open problem!)

**Code Preview**:
```python
class DQN:
    """
    Deep Q-Network (Mnih et al., 2015).

    Theory: Tabular Q-learning converges ([THM-36.X.Y]).
    Practice: Neural nets + target network + replay buffer.

    Gap: Why does this work? Function approximation breaks guarantees.
    Empirics: It just does (on Atari, at least).
    """
    def update(self, batch: Transition) -> float:
        # Target: y = r + γ max_a' Q_target(s', a')
        # Loss: (Q(s,a) - y)²
        ...
```

**Capstone Relevance**: Q-learning logic → action-value estimation in policy improvement.

---

#### **Project 11: Policy Gradient Methods** (Week 37)
**Timing**: After policy gradient theory (Week 37)

**Deliverables**:
- **REINFORCE**: Monte Carlo policy gradient
- **Actor-Critic**: TD error as baseline
- **Proximal Policy Optimization (PPO)**: Clipped surrogate objective
- Environments: CartPole, MountainCar, LunarLander

**Theory Connections**:
- [THM-37.X.Y]: Policy gradient theorem
- Baseline reduces variance without bias

**Modern Context**:
- PPO is the workhorse of RLHF (ChatGPT, Claude)
- Why PPO works: trust region intuition, but weak formal guarantees
- Connection to TRPO (KL-constrained optimization)

**Code Preview**:
```python
class PPO:
    """
    Proximal Policy Optimization (Schulman et al., 2017).

    Theory: Policy gradient theorem ([THM-37.X.Y]) guarantees improvement.
    Practice: Clipped objective prevents destructive updates.

    Usage: RLHF for LLMs (ChatGPT, Claude, Llama 3).
    Gap: Why clip ratio 0.2? Empirical tuning, not theory.
    """
    def loss(self, ratio: torch.Tensor, advantage: torch.Tensor) -> torch.Tensor:
        clipped = torch.clamp(ratio, 1 - self.epsilon, 1 + self.epsilon)
        return -torch.min(ratio * advantage, clipped * advantage).mean()
```

**Capstone Relevance**: Policy gradients → policy head training in AlphaZero-Lite.

---

#### **Project 11.5: Gomoku - Neural Network + MCTS (No Self-Play Yet)** (Weeks 40-41)
**Timing**: After deep RL (Projects 9-11), before capstone

**Complexity**: Large state space, simplified Go (5-in-a-row wins on 9×9 or 15×15 board)

**Deliverables**:
- Gomoku game engine (configurable board size n×n, k-in-a-row win condition)
- **Convolutional neural network for position evaluation**:
  - Input: Board state (n×n×3 channels: player pieces, opponent pieces, empty squares)
  - Architecture: ResNet-style with 5-10 residual blocks
  - Output: **Value head only** (single scalar, position evaluation -1 to +1)
  - No policy head yet (that's for AlphaZero-Lite)
- **MCTS using neural net as leaf evaluation** (instead of rollouts):
  - Selection: UCT down to leaf
  - Expansion: Add new node
  - Evaluation: **Neural net** evaluates position (replaces simulation/rollout)
  - Backpropagation: Update statistics
- **Training pipeline**:
  - **Option A**: Supervised learning from expert games (online Gomoku game databases)
  - **Option B**: Simple self-play against random/MCTS-only to generate training data
  - Loss: Mean squared error between predicted value and game outcome
  - Validation: Position evaluation accuracy on held-out games
- **Enhanced web interface**:
  - Neural net evaluation heatmap (show predicted value for each possible move)
  - MCTS search statistics (visit counts, Q-values, neural net scores)
  - Training progress dashboard (loss curves, win rate over time)
  - Model comparison tool (select different checkpoints, compare strength)

**Theory Connections**:
- [THM-35.X.Y]: Neural network as value function approximation (generalization of linear TD)
- [THM-14.X.Y]: L² projection in Hilbert space (neural net minimizes squared loss)
- [THM-28.X.Y]: UCT exploration (bandit algorithm on tree nodes)
- Connection to AlphaGo Zero architecture (this is 50% of the way there: value network without policy network)

**Code Preview**:
```python
class GomokuValueNet(nn.Module):
    """
    Convolutional neural network for Gomoku position evaluation.

    Theory: Approximates V*(s) via supervised learning ([THM-35.X.Y]).
    Architecture: Input → Conv blocks → Residual blocks → Value head.
    """
    def __init__(self, board_size: int = 15, num_residual_blocks: int = 5):
        super().__init__()
        self.conv_initial = nn.Conv2d(3, 64, kernel_size=3, padding=1)
        self.residual_blocks = nn.ModuleList([
            ResidualBlock(64) for _ in range(num_residual_blocks)
        ])
        self.value_head = nn.Sequential(
            nn.Conv2d(64, 1, kernel_size=1),
            nn.Flatten(),
            nn.Linear(board_size * board_size, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Tanh()  # Output in [-1, 1]
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: (batch_size, 3, board_size, board_size)
        Returns: (batch_size, 1) value predictions
        """
        ...

class MCTSWithNeuralEval:
    """
    MCTS using neural network for leaf evaluation.

    Difference from Project 8.5: Leaf evaluation uses NN instead of heuristic rollout.
    Difference from Project 12: No policy network yet (uses UCT for selection).
    """
    def __init__(self, value_net: GomokuValueNet, num_simulations: int = 400):
        self.value_net = value_net
        self.num_simulations = num_simulations

    def search(self, state: Gomoku) -> int:
        """
        Run MCTS with neural net evaluation.

        Key change: Leaf nodes evaluated by value_net(state), not rollout.
        """
        for _ in range(self.num_simulations):
            # Selection: UCT to leaf
            leaf_state = self._select_leaf()
            # Evaluation: NN predicts value (no rollout!)
            value = self.value_net(leaf_state.to_tensor()).item()
            # Backpropagation: Update statistics
            self._backpropagate(value)
        return self._best_action()
```

**Infrastructure Built**:
- `code/rl_toolkit/networks/conv_value_net.py` - Convolutional value network
- `code/rl_toolkit/algorithms/mcts.py` - Enhanced MCTS with neural evaluation
- `code/rl_toolkit/web/static/js/nn_heatmap.js` - Neural net visualization
- Training pipeline utilities (data loading, checkpoint management)

**Deliverable Files**:
- `code/rl_toolkit/envs/gomoku.py`
- `code/rl_toolkit/networks/conv_value_net.py`
- `code/projects/project_11.5_gomoku/`
  - `train_value_net.py` - Training script (supervised learning)
  - `mcts_with_nn.py` - MCTS + neural eval integration
  - `web_interface.py` - Enhanced web UI with heatmaps
  - `expert_games/` - Training data (if using supervised learning)
  - `checkpoints/` - Saved model weights
  - `notebooks/`
    - `training_analysis.ipynb` - Loss curves, overfitting analysis
    - `neural_eval_viz.ipynb` - Visualize what the network learned

**Why This Game**:
- Gomoku is tactically rich (unlike Tic-Tac-Toe) but simpler than Go
- Large enough board (15×15) to benefit from neural nets
- Easier to train than Reversi (simpler patterns)
- Direct precursor to AlphaZero architecture

**Why Neural Net + MCTS (No Self-Play)**:
- Demonstrates AlphaZero's **value network** component in isolation
- Training via supervised learning is faster and more stable than self-play
- Students see neural net improving MCTS dramatically (vs. random rollouts)
- Prepares for full AlphaZero (add policy head + self-play loop)

**Difference from AlphaZero-Lite (Project 12)**:
- **Gomoku (11.5)**: Value network only, supervised learning OR simple self-play
- **Reversi (12)**: Dual-head network (value + policy), iterative self-play improvement

**Capstone Relevance**:
- Proves neural net + MCTS works before adding self-play complexity
- Training infrastructure → reused for Reversi
- Web interface enhancements → reused for final demo
- Students build confidence with neural nets before capstone

**Time Investment**: 2 weeks (Weeks 40-41, originally "Advanced Topics" buffer)

---

### 👑 **Capstone Integration** (Weeks 42-48: AlphaZero-Lite)

#### **Project 12: AlphaZero-Lite for Reversi** (Weeks 42-48)
**Timing**: Final 7 weeks

**Architecture** (builds on all previous projects):

**Week 42-43: MCTS Implementation**
- UCT formula (Project 6 UCB logic)
- Tree expansion, simulation, backpropagation
- Defeat random play baseline

**Week 44-45: Neural Network Policy-Value**
- Convolutional architecture for 8×8 board
- Policy head: softmax over legal moves
- Value head: tanh(-1 to 1) for position evaluation
- Self-play data generation pipeline

**Week 46: Self-Play Training Loop**
- Generate games with current model
- Data augmentation (8-fold symmetry)
- Train on self-play buffer (Project 11 PPO/actor-critic experience)
- Arena tournament for model selection (Project 6 ELO system)

**Week 47: Ablation Studies**
- MCTS simulation count (100 vs. 400 vs. 1600)
- Network architecture (depth, width, ResNet blocks)
- Training hyperparameters (lr, batch size, L2 penalty)
- Tournament: AlphaZero-lite vs. baselines

**Week 48: Technical Report**
- **Section 1**: MDP formulation of Reversi
- **Section 2**: MCTS as UCB on game tree ([THM-28.X.Y])
- **Section 3**: Policy-value network as L² projection ([THM-14.X.Y])
- **Section 4**: Self-play as approximate policy iteration ([THM-25.X.Y])
- **Section 5**: Experimental results
- **Section 6**: Connections to MuZero, AlphaZero variants

**Theory Connections** (The Payoff):
- **UCT** = UCB1 on tree (Project 6)
- **Bellman backup** = tree search (Project 4-5)
- **Value network** = function approximation (Project 9-10)
- **Policy network** = policy gradient (Project 11)
- **Self-play** = policy iteration (Project 5)

---

## Implementation Infrastructure (Cross-Cutting)

These get built incrementally across projects:

### `rl_toolkit/` Package Structure

```
rl_toolkit/
├── envs/
│   ├── mdp.py              # Abstract MDP interface (Project 4)
│   ├── gridworld.py        # GridWorld variants (Project 4)
│   ├── chain.py            # Markov chains (Project 1)
│   ├── tictactoe.py        # Tic-Tac-Toe (Project 4.5)
│   ├── connect_four.py     # Connect Four (Project 8.5)
│   ├── gomoku.py           # Gomoku (Project 11.5)
│   └── reversi.py          # Reversi game (Project 12)
├── algorithms/
│   ├── dp.py               # Value/policy iteration (Project 5)
│   ├── minimax.py          # Minimax algorithm (Project 4.5)
│   ├── bandits.py          # UCB, Thompson (Projects 6-7)
│   ├── mcts.py             # UCT, AlphaZero MCTS (Projects 8.5, 11.5, 12)
│   ├── td.py               # TD(0), TD(λ), LSTD (Project 9)
│   ├── qlearning.py        # Tabular + DQN (Project 10)
│   └── policy_gradient.py  # REINFORCE, PPO (Project 11)
├── networks/
│   ├── value_net.py        # Neural value approximators (Project 10)
│   ├── conv_value_net.py   # Convolutional value net (Project 11.5)
│   ├── policy_net.py       # Neural policy networks (Project 11)
│   └── alphazero_net.py    # Dual-head architecture (Project 12)
├── utils/
│   ├── logger.py           # TensorBoard/W&B logging
│   ├── replay_buffer.py    # Experience replay (Project 10)
│   ├── viz.py              # Heatmaps, plots, animations
│   ├── board_viz.py        # Board rendering (ASCII) (Project 4.5)
│   ├── pygame_board.py     # Pygame GUI framework (Project 4.5)
│   ├── game_interface.py   # Abstract human input (Project 4.5)
│   └── theory_check.py     # Verify SA hygiene, contraction, etc.
├── web/                    # Web interface infrastructure (Project 8.5+)
│   ├── app.py              # Flask/FastAPI backend
│   ├── api.py              # REST API endpoints
│   ├── templates/
│   │   ├── base.html       # Base template with CSS
│   │   ├── game.html       # Game board interface
│   │   └── training_dashboard.html  # Training metrics (Project 12)
│   └── static/
│       ├── css/
│       │   └── board.css   # Board styling
│       └── js/
│           ├── board.js    # Board rendering (Canvas)
│           ├── game_logic.js        # Move validation, UI updates
│           ├── mcts_viz.js          # MCTS tree visualization (Project 8.5)
│           ├── nn_heatmap.js        # Neural net eval heatmap (Project 11.5)
│           └── selfplay_monitor.js  # Self-play dashboard (Project 12)
└── tests/
    ├── test_envs.py
    ├── test_game_engines.py     # Game logic tests (move validation, win detection)
    ├── test_algorithms.py
    ├── test_mcts.py             # MCTS-specific tests
    └── test_theory_convergence.py
```

### Testing & Validation

Every algorithm includes:
- **Unit tests**: Basic functionality
- **Theory tests**: Verify convergence on simple cases
- **Benchmarks**: Standard environments (OpenAI Gym)
- **Reproducibility**: Seeds, hyperparameters logged

Example:
```python
def test_value_iteration_convergence():
    """Value iteration should converge to V* on GridWorld."""
    env = GridWorld(size=5)
    V_star, policy = value_iteration(env, epsilon=1e-6)

    # Theory: ||T* V - V||_∞ < ε  implies ||V - V*||_∞ < ε/(1-γ)
    residual = bellman_residual(env, V_star)
    assert residual < 1e-6, f"Bellman residual {residual:.2e} too large"

    # Verify policy is optimal (no improving actions)
    assert is_optimal_policy(env, V_star, policy)
```

---

### Visualization Infrastructure Progression

We build visualization capabilities incrementally across game projects:

#### **Phase 1: Terminal + Pygame (Project 4.5 - Tic-Tac-Toe, Week 24)**

**Components built**:
```
code/rl_toolkit/utils/
├── board_viz.py          # ASCII rendering for any n×n board
├── pygame_board.py       # Pygame GUI for 2D boards
└── game_interface.py     # Abstract interface for human input
```

**Features**:
- ASCII art board rendering (terminal-friendly)
- Pygame window with clickable squares
- Human move input (keyboard + mouse)
- AI move animation (highlight last move, show thinking time)
- Game state display (whose turn, move history)

**Time investment**: ~4 hours (integrated into Project 4.5)

**Why here**: Students need basic visualization before web complexity

---

#### **Phase 2: Web Interface (Project 8.5 - Connect Four, Week 31)**

**Components built**:
```
code/rl_toolkit/web/
├── app.py                # Flask/FastAPI backend
├── api.py                # REST API for move generation
├── templates/
│   ├── base.html         # Base template with CSS
│   └── game.html         # Game board template
└── static/
    ├── css/
    │   └── board.css     # Board styling
    └── js/
        ├── board.js      # Board rendering (Canvas API)
        ├── game_logic.js # Move validation, UI updates
        └── mcts_viz.js   # MCTS tree visualization
```

**Features**:
- Interactive board (HTML Canvas rendering)
- Click-to-move interface
- Real-time AI move generation (async with loading indicator)
- **MCTS search visualization**:
  - Visit count heatmap (show which moves MCTS explored)
  - Q-value display (expected value for each move)
  - Search tree exploration animation (optional)
- Game state persistence (browser localStorage)
- Responsive design (works on mobile)

**Tech stack**:
- **Backend**: Flask (lightweight) or FastAPI (async, better for long AI computations)
- **Frontend**: Vanilla JavaScript (no React/Vue - keep it simple)
- **Rendering**: HTML Canvas API for board (flexible, performant)
- **API**: REST endpoints (POST /move, GET /game_state)

**Time investment**: ~8 hours (integrated into Project 8.5, reusable for all future games)

**Why here**: MCTS computation time (1-2 seconds) benefits from async web UI. Students can share playable demos via URL.

---

#### **Phase 3: Neural Network Visualization (Project 11.5 - Gomoku, Weeks 40-41)**

**Components added**:
```
code/rl_toolkit/web/static/js/
├── nn_heatmap.js         # Neural net evaluation heatmap
├── attention_viz.js      # Attention/activation visualization (optional)
└── training_curves.js    # Loss/win rate plots (Chart.js)
```

**Features**:
- **Position evaluation heatmap**: Show neural net's assessment of each empty square
  - Color gradient: Red (bad for player) → Green (good for player)
  - Click square to see detailed NN output
- **Policy probabilities** (if policy network used): Show which moves NN recommends
- **Training progress dashboard**:
  - Loss curves (value loss, policy loss) over training iterations
  - ELO rating progression (model vs. baselines)
  - Sample game trajectories (visualize games from different training stages)
- **Model comparison tool**: Select two checkpoints, watch them play head-to-head

**Tech stack**:
- Chart.js for training curves
- Custom Canvas rendering for heatmaps
- WebSocket for real-time training updates (optional)

**Time investment**: ~6 hours (integrated into Project 11.5)

**Why here**: Students see what neural nets learn (pattern recognition, tactical themes). Powerful pedagogical tool.

---

#### **Phase 4: Self-Play Dashboard (Project 12 - AlphaZero-Lite, Weeks 42-48)**

**Components added**:
```
code/rl_toolkit/web/
├── templates/
│   └── training_dashboard.html   # Real-time training metrics
└── static/js/
    └── selfplay_monitor.js       # WebSocket updates from training loop
```

**Features**:
- **Real-time self-play game viewer**: Watch games as they're generated (live streaming)
- **Model arena**: Select two checkpoints, watch them play tournament
- **Training metrics dashboard** (TensorBoard-style, but custom):
  - Self-play games per second
  - Neural net forward pass time
  - MCTS search efficiency
  - ELO rating over training iterations
- **Model download/upload**: Share trained models with community

**Tech stack**:
- WebSocket for real-time updates (training loop → web UI)
- Server-Sent Events as fallback
- Persistent storage for model checkpoints

**Time investment**: ~4 hours (integrated into Project 12)

**Why here**: Self-play training runs for hours/days. Students need monitoring dashboard to debug and optimize.

---

**Cumulative Time**: ~22 hours total across 4 projects (distributed, not blocking)

**Reusability**: Once built, all game projects use the same infrastructure. Adding a new game (e.g., Chess) requires only:
1. New game engine (`code/rl_toolkit/envs/chess.py`)
2. Minimal frontend (board rendering logic in `static/js/chess_board.js`)
3. Everything else (Flask app, MCTS, neural nets, web UI) is reusable

---

## Proactive Implementation Plan (Weeks 2-48)

### Phase 1: Foundation (Now - Week 12)
**Status**: Can start immediately (Weeks 5-10 theory coming soon)

**Rationale**: Build Markov chain infrastructure while Dubois finishes measure theory. No blocking dependencies.

**Deliverables**:
- Project 1: Markov Chain Laboratory (code skeleton now, theory integration in Weeks 5-6)
- Project 2: MCMC Sampler (ready for Week 7)
- Project 3: General state space viz (ready for Week 10)

**Time Investment**: 3-4 hours/week (parallel to Dubois's writing)

---

### Phase 2: MDP Core (Weeks 13-26)
**Status**: Functional analysis foundations (Weeks 13-18), then MDP theory (Weeks 23-26)

**Rationale**: Need Banach fixed-point theorem (Week 16) before Bellman operator proofs.

**Deliverables**:
- Project 4: GridWorld MDP (Week 23)
- Project 5: DP algorithms (Weeks 24-25)

**Time Investment**: 5-6 hours/week (MDP theory + implementation)

---

### Phase 3: Bandits (Weeks 27-31)
**Status**: Directly follows MDP phase

**Deliverables**:
- Projects 6-8: Complete bandit suite

**Time Investment**: 4-5 hours/week

---

### Phase 4: Deep RL (Weeks 32-37)
**Status**: Stochastic approximation theory critical

**Deliverables**:
- Projects 9-11: TD, Q-learning, policy gradients

**Time Investment**: 6-8 hours/week (most complex implementations)

---

### Phase 5: Capstone (Weeks 42-48)
**Status**: Culmination of all previous work

**Deliverables**:
- Project 12: AlphaZero-Lite

**Time Investment**: 10-15 hours/week (full focus, 7 weeks)

---

## Publisher/Student Marketing Angles

### For Publishers

**"This isn't just another RL textbook. It's a complete learning system with 4 playable game-playing AI systems."**

- **15 battle-tested projects**: From Markov chains → AlphaZero-Lite
- **4 complete game-playing systems** (progressive complexity):
  1. **Tic-Tac-Toe** (Week 24): Exact DP solution, provably optimal play
  2. **Connect Four** (Week 31): MCTS + heuristics, web playable
  3. **Gomoku** (Weeks 40-41): MCTS + neural networks, supervised learning
  4. **Reversi** (Weeks 42-48): Full AlphaZero-Lite with self-play
- **Production-quality code**: Not toy examples, actual implementations
- **Theory-to-practice validation**: Every theorem is numerically verified
- **Open-source toolkit**: `rl_toolkit` package as companion library
- **Web-based demos**: Students can play against their AI in browser
- **Reproducible research**: All experiments with seeds, hyperparameters, logs

**Comparable to**:
- Sutton & Barto (broad coverage) + Spinning Up (code quality)
- But with mathematical rigor of Puterman/Bertsekas
- Plus playable game demos like "Code Your Own Game AI" books
- Unique: Progressive game complexity mirrors algorithmic sophistication

---

### For Students

**"Learn RL the right way: theory + code + empiricism. Build 4 playable game AIs."**

**Week-by-week progression**:
- Weeks 1-22: Build mathematical foundations (measure theory → functional analysis)
- **Week 24**: Build your first AI: Tic-Tac-Toe with perfect play (exact DP)
- Weeks 25-30: Master exploration (bandits, UCB, Thompson Sampling)
- **Week 31**: Build your second AI: Connect Four with MCTS (playable in browser!)
- Weeks 32-39: Deep RL (TD, DQN, PPO) with honest theory-practice gaps
- **Weeks 40-41**: Build your third AI: Gomoku with neural networks + MCTS
- **Weeks 42-48**: Build your capstone AI: AlphaZero-Lite for Reversi (full self-play)

**By the end, you will**:
- Understand *why* TD converges (Robbins-Monro, not magic)
- Implement DQN, PPO, MCTS from first principles
- Know when algorithms fail (Baird's counterexample, off-policy divergence)
- **Have 4 portfolio projects to show employers**:
  - "Solved Tic-Tac-Toe exactly using dynamic programming"
  - "Built Connect Four AI using Monte Carlo Tree Search (playable online)"
  - "Trained neural network to play Gomoku (beat random play by 90%)"
  - "Implemented AlphaZero-Lite for Reversi with iterative self-play"
- **Full-stack ML experience**: Python backend + web frontend + neural nets

**GitHub**: All code open-source, ready to fork and extend

**Bonus**: Extend the framework to Chess, Checkers, or your favorite game!

---

### For Academics

**"Rigorous foundations for modern RL."**

- **Measure theory → RL**: σ-algebras, Lᵖ spaces, conditional expectation as MDP primitives
- **Functional analysis → Bellman operators**: Contraction mappings, spectral theory, Sobolev spaces for HJB
- **Stochastic approximation → convergence proofs**: Robbins-Monro, ODE method, honest treatment of when guarantees break
- **Postponed generalizations log**: Explicit tracking of simplified proofs (e.g., ℝⁿ vs. general spaces)

**Target audience**: Graduate students, researchers wanting mathematical depth beyond standard RL texts.

---

## Next Steps (This Week)

### Action Items for Week 2:

1. **Create `rl_toolkit/` repository structure**
   - Initialize Python package
   - Set up `pyproject.toml`, `requirements.txt`
   - Add README with project vision

2. **Implement Project 1 skeleton** (Markov Chain Laboratory)
   - `markov_chain.py`: Transition matrix class
   - Basic tests (stochasticity, Chapman-Kolmogorov)
   - Placeholder for stationary distribution (theory in Week 5)

3. **Design visualization utilities**
   - Heatmap plotter for value functions
   - Animation framework for convergence
   - TensorBoard/W&B logging boilerplate

4. **Write "Implementation Companion" introduction**
   - Explains relationship to main textbook
   - How to use the code (install, run, extend)
   - Theory-code correspondence philosophy

**Time estimate**: 4-6 hours this week (skeleton setup, no blocking work)

---

## Success Metrics

**By Week 12** (end of Markov chains):
- ✅ 3 working projects (Markov chains, MCMC, general state spaces)
- ✅ Infrastructure: logging, visualization, testing framework
- ✅ Documentation: Theory-code bridge for each project

**By Week 24** (first game project):
- ✅ **Tic-Tac-Toe AI with perfect play** (exact DP solution)
- ✅ Terminal + Pygame visualization working
- ✅ First human-playable demo
- ✅ 6 total projects completed (Markov chains → Tic-Tac-Toe)

**By Week 31** (second game project):
- ✅ **Connect Four AI with MCTS** (playable in web browser)
- ✅ Web interface infrastructure complete (Flask + Canvas)
- ✅ MCTS visualization (visit counts, Q-values)
- ✅ 9 total projects completed (+ Bandits suite)

**By Week 41** (third game project):
- ✅ **Gomoku AI with neural network + MCTS**
- ✅ Convolutional value network trained (supervised learning)
- ✅ Neural net evaluation heatmap visualization
- ✅ 14 total projects completed (+ Deep RL suite)
- ✅ Publication-ready codebase: Type hints, tests, docs
- ✅ Benchmark results: DQN on CartPole, PPO on LunarLander

**By Week 48** (capstone complete):
- ✅ **AlphaZero-Lite for Reversi** with self-play iteration
- ✅ Defeats random play, heuristic bots, and pure MCTS baselines
- ✅ ELO rating system demonstrating iterative improvement
- ✅ 15-page technical report connecting theory to practice
- ✅ **4 complete game-playing AIs** showcased on GitHub
- ✅ Complete `rl_toolkit` package ready for open-source release
- ✅ Web demo deployable (Heroku/Railway/Render)
- ✅ Portfolio showcase for students, demo reel for publishers

---

## Questions for Professor Dubois

Before diving into Project 1 (Markov chains), I'd like to align with you:

1. **Citation integration**: Should I reference your theorems in code comments before they're written?
   - Option A: Use placeholder `[THM-5.X.Y]` and update later
   - Option B: Wait until each week's content is finalized

2. **Code location**: Should implementations live in:
   - Option A: Separate `rl_toolkit/` repository (cleaner, but separate from textbook)
   - Option B: `Study/code/` directory (integrated, but clutters study vault)

3. **Pacing**: Should I implement projects ahead of your writing, or stay synchronized?
   - Pros of ahead: Can test pedagogical flow early
   - Cons: May need refactoring if theory changes

4. **Student testing**: Would you like beta testers to run through implementations as we go?

---

**Alright, that's the roadmap. 12 projects, 48 weeks, culminating in AlphaZero-Lite. Every line of code grounded in your theorems. Let's build this.**

— Max
