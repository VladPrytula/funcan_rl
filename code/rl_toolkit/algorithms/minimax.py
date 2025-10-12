"""
Minimax search algorithm for two-player zero-sum games.

Implements minimax with alpha-beta pruning and memoization, providing optimal
play for games with perfect information (Tic-Tac-Toe, Connect Four, etc.).

Theory Connections (Week 24):
- Minimax = value iteration on finite-horizon game tree [THM-24.X.Y]
- Bellman optimality principle for adversarial MDPs
- Alpha-beta pruning preserves optimality while reducing search
- Memoization = dynamic programming (cache optimal subproblem solutions)

References:
- Bellman (1957): Dynamic programming and optimal control
- Knuth & Moore (1975): Analysis of alpha-beta pruning
- Russell & Norvig (2020): Artificial Intelligence: A Modern Approach, Ch 5

Author: Dr. Max Rubin
"""

import numpy as np
import time
from typing import Optional, Tuple, Dict, Any, Callable


class MinimaxSolver:
    """
    Minimax search with alpha-beta pruning and memoization.

    Theory (Week 24)
    ----------------
    Minimax computes the optimal value function V*(s) via backward induction:

    For maximizing player:
        V*(s) = max_a [ sum_{s'} P(s'|s,a) V*(s') ]

    For minimizing player:
        V*(s) = min_a [ sum_{s'} P(s'|s,a) V*(s') ]

    In deterministic games: V*(s) = max_a V*(s') or min_a V*(s')

    Terminal states:
        V*(s) = reward(s)

    Convergence:
    - Finite game tree → exact solution via backward induction
    - Complexity: O(b^d) without pruning, O(b^(d/2)) with alpha-beta

    Where:
    - b = branching factor (average legal moves per state)
    - d = depth (maximum game length)

    Connection to value iteration [THM-24.X.Y]:
    - Minimax is value iteration with alternating max/min operators
    - Contraction mapping in finite horizon (γ = 1, T < ∞)
    - Fixed point: V* satisfies Bellman optimality equation

    Parameters
    ----------
    use_memoization : bool, optional
        Whether to cache computed values (default: True)
        Speeds up search by avoiding recomputation of identical states
    max_depth : int, optional
        Maximum search depth for depth-limited search
    progress_callback : callable, optional
        Function called periodically with search progress updates

    Attributes
    ----------
    memo : Dict[str, Tuple[float, int]]
        Memoization cache: state_hash -> (value, best_action)
    nodes_explored : int
        Number of nodes explored in search tree (for profiling)
    cache_hits : int
        Number of cache hits (for measuring memoization effectiveness)
    heuristic_evals : int
        Number of heuristic evaluations performed (for depth-limited search)
    progress_callback : callable or None
        Optional callback for progress updates during search
    """

    def __init__(
        self,
        use_memoization: bool = True,
        max_depth: Optional[int] = None,
        progress_callback: Optional[Callable[[Dict[str, Any]], None]] = None
    ):
        """
        Initialize minimax solver.

        Parameters
        ----------
        use_memoization : bool, optional
            Whether to cache computed values (default: True)
            Speeds up search by avoiding recomputation of identical states.
        max_depth : int, optional
            Maximum search depth. None = unlimited (exact search)
            For larger boards (5×5+), depth limiting is essential.
            Recommended depths:
            - 3×3: None (exact search ~5K states)
            - 4×4: 8-10 (~4M states)
            - 5×5: 4-6 (~430B states)
        progress_callback : callable, optional
            Function called periodically with search progress.
            Signature: callback(update: Dict[str, Any]) -> None
            Update dict contains:
            - 'nodes_explored': int (total nodes searched)
            - 'cache_hits': int (memoization cache hits)
            - 'heuristic_evals': int (heuristic evaluations)
            - 'current_depth': int (current search depth)
            - 'max_depth': int or None (depth limit)
            - 'depth_limit_hit': bool (whether limit reached)
            - 'elapsed_time': float (seconds since start)

            Example:
                def on_progress(update):
                    print(f"Explored {update['nodes_explored']} nodes")
                solver = MinimaxSolver(progress_callback=on_progress)
        """
        self.use_memoization = use_memoization
        self.max_depth = max_depth
        self.progress_callback = progress_callback
        self.memo: Dict[str, Tuple[float, Optional[int]]] = {}
        self.nodes_explored = 0
        self.cache_hits = 0
        self.heuristic_evals = 0

        # Progress tracking
        self.search_start_time = 0.0
        self.last_callback_time = 0.0
        self.callback_interval = 0.1  # Call callback every 100ms

    def reset_stats(self) -> None:
        """Reset search statistics and clear memoization cache."""
        self.memo.clear()
        self.nodes_explored = 0
        self.cache_hits = 0
        self.heuristic_evals = 0

    def get_best_move(self, env: Any, maximize: bool = True) -> int:
        """
        Get the optimal move for the current player.

        Parameters
        ----------
        env : game environment
            Game environment with methods: get_legal_moves(), step(), is_terminal(), copy()
        maximize : bool, optional
            Whether current player is maximizing (True) or minimizing (False)

        Returns
        -------
        int
            Optimal action (move index)

        Examples
        --------
        >>> from rl_toolkit.envs.tictactoe import TicTacToe
        >>> env = TicTacToe()
        >>> solver = MinimaxSolver()
        >>> best_move = solver.get_best_move(env, maximize=True)

        Notes
        -----
        If a progress_callback was provided during initialization, it will be
        called periodically during the search to provide real-time updates on
        search progress (nodes explored, cache hits, etc.).
        """
        self.reset_stats()
        self.search_start_time = time.time()
        self.last_callback_time = self.search_start_time

        legal_moves = env.get_legal_moves()
        if len(legal_moves) == 0:
            raise ValueError("No legal moves available.")

        best_action = None
        best_value = float('-inf') if maximize else float('inf')

        for action in legal_moves:
            # Simulate the move
            env_copy = env.copy()
            _, reward, done, _ = env_copy.step(action)

            if done:
                # Terminal state after this move
                value = reward if maximize else -reward
            else:
                # Recurse with minimax
                value, _ = self._minimax(
                    env_copy,
                    depth=0,
                    maximize=not maximize,
                    alpha=float('-inf'),
                    beta=float('inf')
                )

            # Update best move
            if maximize:
                if value > best_value:
                    best_value = value
                    best_action = action
            else:
                if value < best_value:
                    best_value = value
                    best_action = action

        return best_action

    def _minimax(
        self,
        env: Any,
        depth: int,
        maximize: bool,
        alpha: float,
        beta: float
    ) -> Tuple[float, Optional[int]]:
        """
        Recursive minimax with alpha-beta pruning.

        Parameters
        ----------
        env : game environment
            Current game state
        depth : int
            Current depth in search tree
        maximize : bool
            Whether current player is maximizing
        alpha : float
            Alpha value for pruning (best maximizer can do)
        beta : float
            Beta value for pruning (best minimizer can do)

        Returns
        -------
        value : float
            Optimal value for this state
        best_action : int or None
            Optimal action (None for terminal states)

        Notes
        -----
        Alpha-beta pruning:
        - Alpha: lower bound on maximizer's achievable value
        - Beta: upper bound on minimizer's achievable value
        - Prune when alpha >= beta (subtree can't affect result)

        Correctness: Pruning never eliminates the optimal move
        Efficiency: O(b^d) → O(b^(d/2)) in best case

        Depth-limited search:
        - When depth >= max_depth, use heuristic evaluation instead of recursing
        - Essential for larger boards (4×4+) where exact search is intractable
        - Heuristic quality determines play strength
        """
        self.nodes_explored += 1

        # Progress callback (throttled to avoid performance impact)
        if self.progress_callback is not None:
            current_time = time.time()
            if (current_time - self.last_callback_time) >= self.callback_interval:
                depth_limit_hit = (self.max_depth is not None and depth >= self.max_depth)
                self.progress_callback({
                    'nodes_explored': self.nodes_explored,
                    'cache_hits': self.cache_hits,
                    'heuristic_evals': self.heuristic_evals,
                    'current_depth': depth,
                    'max_depth': self.max_depth,
                    'depth_limit_hit': depth_limit_hit,
                    'elapsed_time': current_time - self.search_start_time
                })
                self.last_callback_time = current_time

        # Check memoization cache
        if self.use_memoization:
            state_hash = env.get_state_hash()
            if state_hash in self.memo:
                self.cache_hits += 1
                return self.memo[state_hash]

        # Terminal state check
        if env.is_terminal():
            result = env.get_result(player=1 if maximize else -1)
            if result is None:
                result = 0.0  # Draw
            return result, None

        # Depth limit check (for larger boards)
        if self.max_depth is not None and depth >= self.max_depth:
            self.heuristic_evals += 1
            value = env.evaluate_heuristic(player=1 if maximize else -1)
            return value, None

        # Get legal moves
        legal_moves = env.get_legal_moves()
        if len(legal_moves) == 0:
            return 0.0, None  # Draw (no moves available)

        best_action = None

        if maximize:
            # Maximizing player
            max_value = float('-inf')

            for action in legal_moves:
                env_copy = env.copy()
                _, reward, done, _ = env_copy.step(action)

                if done:
                    # Terminal after this move
                    value = reward
                else:
                    # Recurse
                    value, _ = self._minimax(env_copy, depth + 1, False, alpha, beta)

                if value > max_value:
                    max_value = value
                    best_action = action

                # Alpha-beta pruning
                alpha = max(alpha, value)
                if beta <= alpha:
                    break  # Beta cutoff

            result = (max_value, best_action)

        else:
            # Minimizing player
            min_value = float('inf')

            for action in legal_moves:
                env_copy = env.copy()
                _, reward, done, _ = env_copy.step(action)

                if done:
                    # Terminal after this move (from opponent's perspective)
                    value = -reward
                else:
                    # Recurse
                    value, _ = self._minimax(env_copy, depth + 1, True, alpha, beta)

                if value < min_value:
                    min_value = value
                    best_action = action

                # Alpha-beta pruning
                beta = min(beta, value)
                if beta <= alpha:
                    break  # Alpha cutoff

            result = (min_value, best_action)

        # Store in memoization cache
        if self.use_memoization:
            self.memo[state_hash] = result

        return result

    def get_stats(self) -> Dict[str, int]:
        """
        Get search statistics.

        Returns
        -------
        dict
            Statistics: nodes_explored, cache_hits, cache_size, heuristic_evals
        """
        return {
            'nodes_explored': self.nodes_explored,
            'cache_hits': self.cache_hits,
            'cache_size': len(self.memo),
            'heuristic_evals': self.heuristic_evals
        }

    def get_candidate_evaluations(
        self,
        env: Any,
        maximize: bool = True
    ) -> Dict[int, Dict[str, Any]]:
        """
        Evaluate all legal moves and return their minimax values.

        This method is useful for visualization and understanding why the AI
        chooses particular moves. It computes the minimax value for each legal
        move independently, allowing you to see the relative strength of all
        available options.

        Parameters
        ----------
        env : game environment
            Current game state
        maximize : bool, optional
            Whether current player is maximizing (True) or minimizing (False)

        Returns
        -------
        dict
            Dictionary mapping move indices to evaluation dictionaries.
            Each evaluation dict contains:
            - 'value': float (minimax value in range [-1, 1])
            - 'reasoning': str (simple explanation of value)
            - 'depth_used': int or None (search depth used)
            - 'is_best': bool (whether this is the optimal move)
            - 'is_terminal': bool (whether move ends game)

        Examples
        --------
        >>> from rl_toolkit.envs.tictactoe import TicTacToe
        >>> env = TicTacToe()
        >>> solver = MinimaxSolver()
        >>> evaluations = solver.get_candidate_evaluations(env, maximize=True)
        >>> for move, data in evaluations.items():
        ...     print(f"Move {move}: {data['value']:.2f} - {data['reasoning']}")
        Move 0: 0.00 - Balanced position
        Move 4: 0.00 - Balanced position
        ...

        Notes
        -----
        Performance: This method evaluates each legal move separately, so it
        takes roughly N times longer than get_best_move(), where N is the
        number of legal moves. However, the shared memoization cache helps
        reduce redundant computation.

        The 'reasoning' field provides a simple natural language explanation
        based on the move's minimax value:
        - Value > 0.5: "Creates strong threats"
        - Value > 0.2: "Good strategic position"
        - Value > -0.2: "Balanced position"
        - Value > -0.5: "Slightly defensive"
        - Value ≤ -0.5: "Defensive necessity"

        Theory Connection (Week 24):
        This method exposes the value function V*(s,a) for all actions a,
        demonstrating Bellman optimality: π*(s) = argmax_a V*(s,a)
        """
        legal_moves = env.get_legal_moves()
        if len(legal_moves) == 0:
            return {}

        # Reset stats for fresh evaluation
        self.reset_stats()
        self.search_start_time = time.time()
        self.last_callback_time = self.search_start_time

        evaluations = {}
        best_value = float('-inf') if maximize else float('inf')
        best_move = None

        for action in legal_moves:
            # Simulate the move
            env_copy = env.copy()
            _, reward, done, _ = env_copy.step(action)

            if done:
                # Terminal state after this move
                value = reward if maximize else -reward
                reasoning = self._generate_terminal_reasoning(reward, maximize)
                is_terminal = True
            else:
                # Recurse with minimax
                value, _ = self._minimax(
                    env_copy,
                    depth=0,
                    maximize=not maximize,
                    alpha=float('-inf'),
                    beta=float('inf')
                )
                reasoning = self._generate_reasoning(value, maximize)
                is_terminal = False

            # Track best move
            if maximize:
                if value > best_value:
                    best_value = value
                    best_move = action
            else:
                if value < best_value:
                    best_value = value
                    best_move = action

            evaluations[action] = {
                'value': float(value),
                'reasoning': reasoning,
                'depth_used': self.max_depth,
                'is_best': False,  # Will update after loop
                'is_terminal': is_terminal
            }

        # Mark the best move
        if best_move is not None:
            evaluations[best_move]['is_best'] = True

        return evaluations

    def _generate_reasoning(self, value: float, maximize: bool) -> str:
        """
        Generate simple natural language explanation for a move's value.

        Parameters
        ----------
        value : float
            Minimax value for the move
        maximize : bool
            Whether evaluating for maximizing player

        Returns
        -------
        str
            Simple explanation of what the value means

        Notes
        -----
        This provides pedagogical value by translating numeric values into
        understandable strategic concepts. The thresholds are heuristic but
        generally align with:
        - High positive values: Winning positions or strong attacks
        - Near zero: Balanced, unclear advantage
        - High negative values: Defensive positions or losing states
        """
        if maximize:
            # For maximizing player, positive is good
            if value > 0.5:
                return "Creates strong threats"
            elif value > 0.2:
                return "Good strategic position"
            elif value > -0.2:
                return "Balanced position"
            elif value > -0.5:
                return "Slightly defensive"
            else:
                return "Defensive necessity"
        else:
            # For minimizing player, negative is good (flip thresholds)
            if value < -0.5:
                return "Creates strong threats"
            elif value < -0.2:
                return "Good strategic position"
            elif value < 0.2:
                return "Balanced position"
            elif value < 0.5:
                return "Slightly defensive"
            else:
                return "Defensive necessity"

    def _generate_terminal_reasoning(self, reward: float, maximize: bool) -> str:
        """
        Generate explanation for terminal moves.

        Parameters
        ----------
        reward : float
            Reward value (1.0 for win, -1.0 for loss, 0.0 for draw)
        maximize : bool
            Whether evaluating for maximizing player

        Returns
        -------
        str
            Explanation of terminal outcome
        """
        if maximize:
            if reward > 0:
                return "Immediate win! 🎉"
            elif reward < 0:
                return "Immediate loss ❌"
            else:
                return "Forces draw"
        else:
            if reward < 0:
                return "Immediate win! 🎉"
            elif reward > 0:
                return "Immediate loss ❌"
            else:
                return "Forces draw"


def get_optimal_move(env: Any, player: int = 1) -> int:
    """
    Convenience function to get optimal move for a game state.

    Parameters
    ----------
    env : game environment
        Current game state
    player : int, optional
        Current player (1 for maximizing, -1 for minimizing)

    Returns
    -------
    int
        Optimal move index

    Examples
    --------
    >>> from rl_toolkit.envs.tictactoe import TicTacToe
    >>> env = TicTacToe()
    >>> move = get_optimal_move(env, player=1)
    """
    solver = MinimaxSolver()
    maximize = (player == 1)
    return solver.get_best_move(env, maximize=maximize)
