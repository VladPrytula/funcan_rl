"""
Monte Carlo Tree Search with UCT (Upper Confidence bounds for Trees).

Theory Connection (Syllabus Week 27-28):
    - [THM-28.X.Y]: UCB1 achieves logarithmic regret in multi-armed bandits
    - MCTS: Each tree node is a bandit problem (arms = legal actions)
    - UCT: UCB1 applied recursively to game trees (Kocsis & Szepesvári 2006)

Algorithm (Coulom 2006, Kocsis & Szepesvári 2006):
    1. Selection: Traverse tree using UCT until leaf or non-fully-expanded node
    2. Expansion: Add one new child to tree
    3. Simulation: Random playout to terminal state (or depth limit with heuristic)
    4. Backpropagation: Update statistics along path to root

References:
    - Coulom (2006): "Efficient Selectivity and Backup Operators in Monte-Carlo Tree Search"
    - Kocsis & Szepesvári (2006): "Bandit based Monte-Carlo Planning"
    - Browne et al. (2012): "A Survey of Monte Carlo Tree Search Methods"
"""

from typing import Any, Dict, Optional, Tuple
import numpy as np
import random


class MCTSNode:
    """
    Node in Monte Carlo search tree.

    Theory Connection (Week 27-28):
    - Each node is a multi-armed bandit problem
    - Arms = legal actions from this state
    - UCT formula balances exploration-exploitation

    Attributes:
        env: Game state at this node
        parent: Parent node (None for root)
        move_from_parent: Action that led to this node
        children: Dict[action, MCTSNode] - expanded children
        visit_count: N(s) - number of visits
        total_value: W(s) - cumulative value (from perspective of player to move at parent)
        untried_moves: List of actions not yet expanded
    """

    def __init__(
        self,
        env: Any,
        parent: Optional['MCTSNode'] = None,
        move_from_parent: Optional[int] = None
    ):
        """
        Initialize MCTS node.

        Args:
            env: Game state (must have copy() method)
            parent: Parent node (None for root)
            move_from_parent: Action that led to this node
        """
        self.env = env.copy()
        self.parent = parent
        self.move_from_parent = move_from_parent

        self.children: Dict[int, MCTSNode] = {}
        self.visit_count = 0
        self.total_value = 0.0

        # Untried moves (for expansion)
        if not env.is_terminal():
            self.untried_moves = list(env.get_legal_moves())
        else:
            self.untried_moves = []

    def uct_score(self, c: float = 1.41) -> float:
        """
        UCT formula: Q(s,a) + c * sqrt(log(N(s)) / N(s,a))

        Theory Connection (Week 28):
        - [THM-28.X.Y]: UCB1 achieves logarithmic regret
        - c = sqrt(2) is theoretically optimal for bounded rewards in [0,1]
        - Exploration term: sqrt(log N(s) / N(s,a)) → ∞ as N(s,a) → 0

        Practice:
        - c = 1.41 (sqrt(2)) is standard
        - Tune for your domain: higher c → more exploration
        - Terminal nodes: return exploitation value only

        Args:
            c: Exploration constant (default: sqrt(2))

        Returns:
            UCT score (higher = better to explore)
        """
        if self.visit_count == 0:
            return float('inf')  # Force exploration of unvisited nodes

        # Exploitation: average value from this node
        exploitation = self.total_value / self.visit_count

        # Exploration: bonus for under-explored nodes
        if self.parent is None:
            exploration = 0.0
        else:
            exploration = c * np.sqrt(np.log(self.parent.visit_count) / self.visit_count)

        return exploitation + exploration

    def is_fully_expanded(self) -> bool:
        """All legal moves have been tried once."""
        return len(self.untried_moves) == 0

    def best_child(self, c: float = 1.41) -> 'MCTSNode':
        """
        Select child with highest UCT score.

        Args:
            c: Exploration constant

        Returns:
            Child node with highest UCT score
        """
        return max(self.children.values(), key=lambda node: node.uct_score(c))

    def expand(self) -> 'MCTSNode':
        """
        Expand one untried move, return new child node.

        Returns:
            New child node
        """
        if len(self.untried_moves) == 0:
            raise ValueError("No untried moves to expand")

        # Randomly select an untried move
        move = self.untried_moves.pop(random.randrange(len(self.untried_moves)))

        # Create child environment
        child_env = self.env.copy()
        child_env.step(move)

        # Create child node
        child_node = MCTSNode(child_env, parent=self, move_from_parent=move)
        self.children[move] = child_node

        return child_node


class MCTSSolver:
    """
    Monte Carlo Tree Search for two-player zero-sum games.

    Algorithm (Coulom 2006, Kocsis & Szepesvári 2006):
    1. Selection: Traverse tree using UCT until leaf or non-fully-expanded node
    2. Expansion: Add one new child to tree
    3. Simulation: Random playout to terminal state (or depth limit with heuristic)
    4. Backpropagation: Update statistics along path to root

    Theory Connection (Week 28):
    - [THM-28.X.Y]: MCTS converges to minimax in limit
    - UCT regret: O(sqrt(K log n / n)) per node
    - Tree grows asymmetrically toward promising moves

    Practice:
    - Simulation policy: Pure random (simple) or heuristic-guided (better)
    - Depth-limited simulation: Use heuristic evaluation at cutoff
    - Parallelization: Leaf parallelization (run multiple simulations)
    """

    def __init__(
        self,
        num_simulations: int = 1000,
        c: float = 1.41,
        max_depth: Optional[int] = None
    ):
        """
        Initialize MCTS solver.

        Args:
            num_simulations: Number of MCTS iterations (more → stronger play)
            c: UCT exploration constant (higher → more exploration)
            max_depth: Maximum simulation depth (None = until terminal)
        """
        self.num_simulations = num_simulations
        self.c = c
        self.max_depth = max_depth

        # Statistics
        self.nodes_explored = 0
        self.max_tree_depth = 0

    def search(self, env: Any, maximize: bool = True) -> int:
        """
        Run MCTS for num_simulations, return best move.

        Args:
            env: Current game state
            maximize: True if current player wants max value

        Returns:
            best_move: Action with highest visit count (not value - more robust)

        Theory-Practice Gap:
        - Theory: Return argmax Q(s,a)
        - Practice: Return argmax N(s,a) (visit count)
        - Why: Visit count is more robust to outlier simulations
        """
        root = MCTSNode(env)

        for _ in range(self.num_simulations):
            # 1. Selection: Traverse tree using UCT
            node = root
            search_env = env.copy()

            while node.is_fully_expanded() and node.children:
                node = node.best_child(self.c)
                search_env.step(node.move_from_parent)

            # 2. Expansion: Add new child (if not terminal)
            if not search_env.is_terminal() and not node.is_fully_expanded():
                node = node.expand()
                search_env = node.env.copy()

            # 3. Simulation: Random playout (or depth-limited with heuristic)
            result = self._simulate(search_env)

            # 4. Backpropagation: Update path to root
            self._backpropagate(node, result)

        # Return most visited child (not highest value)
        if not root.children:
            # No moves explored (shouldn't happen with num_simulations > 0)
            legal_moves = env.get_legal_moves()
            return legal_moves[0] if len(legal_moves) > 0 else 0

        best_move = max(root.children.items(), key=lambda x: x[1].visit_count)[0]

        # Update statistics
        self.nodes_explored = self._count_nodes(root)
        self.max_tree_depth = self._max_depth(root)

        return best_move

    def _simulate(self, env: Any) -> float:
        """
        Random playout from current state to terminal state.

        Theory: Unbiased estimate of V(s) via Monte Carlo sampling
        Practice: Can use heuristic guidance or early cutoff

        Args:
            env: Current game state

        Returns:
            result: +1 (win for player 1), -1 (loss), 0 (draw)
        """
        sim_env = env.copy()
        depth = 0

        while not sim_env.is_terminal():
            # Depth limit check (if specified)
            if self.max_depth is not None and depth >= self.max_depth:
                # Use heuristic evaluation
                return sim_env.evaluate_heuristic(player=1)

            # Random action (or heuristic-guided)
            legal_moves = sim_env.get_legal_moves()
            if len(legal_moves) == 0:
                break  # No legal moves (shouldn't happen if is_terminal is correct)

            move = random.choice(legal_moves)
            sim_env.step(move)
            depth += 1

        # Terminal state: return actual result
        if sim_env.winner is None:
            return 0.0  # Draw
        return sim_env.get_result(player=1)

    def _backpropagate(self, node: MCTSNode, result: float):
        """
        Update statistics from node to root.

        Key insight: Flip result sign for alternating players.
        - Player 1's win (+1) is Player 2's loss (-1)

        Args:
            node: Leaf node where simulation started
            result: Simulation result from Player 1's perspective
        """
        while node is not None:
            node.visit_count += 1
            node.total_value += result
            result = -result  # Flip for opponent
            node = node.parent

    def get_candidate_evaluations(self, env: Any, maximize: bool = True) -> Dict[int, Dict]:
        """
        Return MCTS statistics for visualization (analogous to minimax).

        Returns:
            {
                move_idx: {
                    'value': Q(s,a),           # Average value
                    'visits': N(s,a),          # Visit count
                    'uct_score': UCT value,    # Exploration bonus
                    'reasoning': str,          # Natural language
                    'is_best': bool            # Most visited move
                }
            }
        """
        # Run MCTS to build tree
        root = MCTSNode(env)

        for _ in range(self.num_simulations):
            # Same as search()
            node = root
            search_env = env.copy()

            while node.is_fully_expanded() and node.children:
                node = node.best_child(self.c)
                search_env.step(node.move_from_parent)

            if not search_env.is_terminal() and not node.is_fully_expanded():
                node = node.expand()
                search_env = node.env.copy()

            result = self._simulate(search_env)
            self._backpropagate(node, result)

        # Extract statistics from root's children
        evaluations = {}
        if not root.children:
            return evaluations

        best_move = max(root.children.items(), key=lambda x: x[1].visit_count)[0]

        for move, child in root.children.items():
            avg_value = child.total_value / child.visit_count if child.visit_count > 0 else 0.0
            evaluations[move] = {
                'value': avg_value,
                'visits': child.visit_count,
                'uct_score': child.uct_score(self.c),
                'reasoning': self._generate_reasoning(child, avg_value),
                'is_best': (move == best_move)
            }

        # Update statistics
        self.nodes_explored = self._count_nodes(root)
        self.max_tree_depth = self._max_depth(root)

        return evaluations

    def _generate_reasoning(self, node: MCTSNode, avg_value: float) -> str:
        """
        Generate natural language explanation.

        Args:
            node: MCTS node
            avg_value: Average value Q(s,a)

        Returns:
            Natural language reasoning
        """
        if node.visit_count > 200:
            exploration = "heavily explored"
        elif node.visit_count > 50:
            exploration = "moderately explored"
        else:
            exploration = "lightly explored"

        if avg_value > 0.3:
            assessment = "strong position"
        elif avg_value > -0.3:
            assessment = "balanced position"
        else:
            assessment = "weak position"

        return f"{exploration}, {assessment} (Q={avg_value:.2f})"

    def get_stats(self) -> Dict:
        """Return search statistics."""
        return {
            'nodes_explored': self.nodes_explored,
            'max_tree_depth': self.max_tree_depth,
            'simulations': self.num_simulations
        }

    def _count_nodes(self, node: MCTSNode) -> int:
        """Count total nodes in tree."""
        count = 1
        for child in node.children.values():
            count += self._count_nodes(child)
        return count

    def _max_depth(self, node: MCTSNode, current_depth: int = 0) -> int:
        """Get maximum depth of tree."""
        if not node.children:
            return current_depth

        return max(self._max_depth(child, current_depth + 1)
                   for child in node.children.values())
