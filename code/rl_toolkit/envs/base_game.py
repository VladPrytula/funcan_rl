"""
Base game environment interface for two-player zero-sum games.

This abstract base class defines the core interface that all game environments
must implement. It enables code reuse across different games (Tic-Tac-Toe,
Connect Four, Gomoku, Reversi) and allows the minimax solver to work with
any conforming game without modification.

Theory Connection (Week 24):
- Defines the MDP interface for finite-horizon adversarial games
- State space S, action space A(s), transition dynamics T(s,a,s')
- Reward function R(s,a) and terminal state detection
- Enables value iteration and minimax search via uniform interface

References:
- Sutton & Barto (2018): Reinforcement Learning, Ch 3 (MDP formalism)
- Puterman (1994): Markov Decision Processes, Ch 2 (state space representation)
- Russell & Norvig (2020): AIMA, Ch 5 (game-playing agents)

"""

from abc import ABC, abstractmethod
import numpy as np
from typing import Tuple, Optional


class BaseGameEnv(ABC):
    """
    Abstract base class for two-player zero-sum perfect information games.

    All game environments (Tic-Tac-Toe, Connect Four, Gomoku, Reversi) inherit
    from this class and implement its abstract methods. This design enables:

    1. **Code reuse**: Minimax solver works with any conforming game
    2. **Consistent interface**: All games use the same API
    3. **Type safety**: Static type checking via abstract methods
    4. **Extensibility**: New games inherit existing functionality

    State Representation
    --------------------
    - Games use a 2D NumPy array (board) with integer values
    - Typical encoding: 0 = empty, +1 = player 1, -1 = player 2
    - Action space: flattened board indices (0 to n²-1)

    MDP Formulation (Week 24)
    -------------------------
    - **State space S**: All legal board configurations
    - **Action space A(s)**: Legal moves from state s
    - **Transition T(s,a,s')**: Deterministic (place piece always succeeds)
    - **Reward R(s)**: +1 win, -1 loss, 0 draw/non-terminal
    - **Terminal states**: Win, loss, or draw (no legal moves)

    Optimality
    ----------
    Minimax search computes V*(s) for all states:

    For maximizing player:
        V*(s) = max_{a ∈ A(s)} V*(T(s,a))

    For minimizing player:
        V*(s) = min_{a ∈ A(s)} V*(T(s,a))

    Terminal states:
        V*(s) = R(s)

    Examples
    --------
    >>> class MyGame(BaseGameEnv):
    ...     def reset(self): ...
    ...     def step(self, action): ...
    ...     # ... implement all abstract methods
    >>>
    >>> game = MyGame()
    >>> solver = MinimaxSolver()
    >>> best_move = solver.get_best_move(game, maximize=True)
    """

    def __init__(self, board_size: int, **kwargs):
        """
        Initialize base game environment.

        Parameters
        ----------
        board_size : int
            Size of the game board (n×n)
        **kwargs : dict
            Additional game-specific parameters
        """
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype=np.int8)
        self.current_player = 1  # Player 1 always starts
        self.done = False
        self.winner: Optional[int] = None

    @abstractmethod
    def reset(self) -> np.ndarray:
        """
        Reset the game to initial state.

        Returns
        -------
        np.ndarray
            Initial board state (typically all zeros)

        Examples
        --------
        >>> env.reset()
        array([[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]])
        """
        pass

    @abstractmethod
    def step(self, action: int) -> Tuple[np.ndarray, float, bool, dict]:
        """
        Execute a move and return the new state.

        Parameters
        ----------
        action : int
            Flattened board index (0 to n²-1) where to place the piece

        Returns
        -------
        state : np.ndarray
            New board state after the move
        reward : float
            Reward for the current player (+1 win, -1 loss, 0 otherwise)
        done : bool
            Whether the game has ended (win, loss, or draw)
        info : dict
            Additional information (winner, legal moves, etc.)

        Raises
        ------
        ValueError
            If the move is illegal (square occupied or out of bounds)

        Notes
        -----
        - Action space: integers 0 to (n²-1) representing board positions
        - Conversion: action = row * board_size + col
        - Inverse: row = action // board_size, col = action % board_size
        - After each move, current_player should switch (multiply by -1)

        Examples
        --------
        >>> state, reward, done, info = env.step(4)  # Center square
        >>> reward
        0.0
        >>> done
        False
        """
        pass

    @abstractmethod
    def get_legal_moves(self) -> np.ndarray:
        """
        Get all legal moves (valid actions) for the current state.

        Returns
        -------
        np.ndarray
            Array of legal move indices (flattened), shape (n_legal_moves,)
            Sorted in ascending order for consistency

        Notes
        -----
        - For most games, legal moves = empty squares
        - Connect Four: only bottom-most empty squares in each column
        - Return empty array if game is terminal

        Examples
        --------
        >>> env.reset()
        >>> env.get_legal_moves()
        array([0, 1, 2, 3, 4, 5, 6, 7, 8])
        >>> env.step(4)  # Occupy center
        >>> env.get_legal_moves()
        array([0, 1, 2, 3, 5, 6, 7, 8])
        """
        pass

    @abstractmethod
    def is_terminal(self) -> bool:
        """
        Check if the game has ended.

        Returns
        -------
        bool
            True if game is over (win, loss, or draw), False otherwise

        Notes
        -----
        Terminal conditions:
        - A player has won (achieved winning condition)
        - Draw (board full with no winner, or other draw condition)
        - No legal moves remain

        Examples
        --------
        >>> env.is_terminal()
        False
        >>> # ... play until win/draw ...
        >>> env.is_terminal()
        True
        """
        pass

    @abstractmethod
    def check_win(self, player: int) -> bool:
        """
        Check if the specified player has won.

        Parameters
        ----------
        player : int
            Player to check (1 or -1)

        Returns
        -------
        bool
            True if player has won, False otherwise

        Notes
        -----
        Winning conditions are game-specific:
        - Tic-Tac-Toe: k-in-a-row (row, column, or diagonal)
        - Connect Four: 4-in-a-row (vertical, horizontal, or diagonal)
        - Gomoku: 5-in-a-row
        - Reversi: most pieces when board is full

        Examples
        --------
        >>> env.step(0); env.step(3); env.step(1); env.step(4); env.step(2)
        >>> env.check_win(1)  # Player 1 (X) has top row
        True
        """
        pass

    @abstractmethod
    def get_result(self, player: int) -> Optional[float]:
        """
        Get the game result from the perspective of the specified player.

        Parameters
        ----------
        player : int
            Player perspective (1 or -1)

        Returns
        -------
        float or None
            +1.0 if player won
            -1.0 if player lost
            0.0 if draw
            None if game not over

        Notes
        -----
        This is the reward function R(s) for terminal states.
        Used by minimax to propagate values up the game tree.

        Theory Connection:
        - V*(s) = R(s) for terminal states
        - V*(s) = max/min_{a} V*(T(s,a)) for non-terminal states

        Examples
        --------
        >>> env.get_result(1)  # Game not over
        None
        >>> # ... play until player 1 wins ...
        >>> env.get_result(1)  # Player 1 won
        1.0
        >>> env.get_result(-1)  # Player 2 lost
        -1.0
        """
        pass

    @abstractmethod
    def copy(self) -> 'BaseGameEnv':
        """
        Create a deep copy of the current game state.

        Returns
        -------
        BaseGameEnv
            New environment instance with identical state
            All internal state (board, current_player, done, winner) copied

        Notes
        -----
        Essential for lookahead search (minimax) without modifying the original
        state. The copy must be completely independent - changes to the copy
        should not affect the original.

        Implementation Pattern:
        ```python
        def copy(self):
            new_env = self.__class__(self.board_size, ...)
            new_env.board = self.board.copy()
            new_env.current_player = self.current_player
            new_env.done = self.done
            new_env.winner = self.winner
            return new_env
        ```

        Examples
        --------
        >>> env1 = TicTacToe()
        >>> env1.step(4)
        >>> env2 = env1.copy()
        >>> env2.step(0)
        >>> env1.board[0, 0]  # Original unaffected
        0
        >>> env2.board[0, 0]  # Copy modified
        -1
        """
        pass

    @abstractmethod
    def get_state_hash(self) -> str:
        """
        Get a hashable representation of the current state.

        Returns
        -------
        str
            Unique string identifier for this board configuration and player turn

        Notes
        -----
        Used for memoization in minimax search (dynamic programming).

        Requirements:
        - Same state → same hash (deterministic)
        - Different states → different hashes (injective)
        - Include current_player in hash (important for minimax!)

        Theory Connection (Week 24):
        Caching eliminates redundant subproblem computation:
        - Without memoization: O(b^d) states explored (b = branching, d = depth)
        - With memoization: O(|S|) unique states cached (S = state space)
        - Tic-Tac-Toe: ~550K nodes → ~5K unique states (100x speedup)

        Implementation Pattern:
        ```python
        def get_state_hash(self):
            board_hash = self.board.tobytes().hex()
            return f"{board_hash}_{self.current_player}"
        ```

        Examples
        --------
        >>> env1 = TicTacToe()
        >>> env2 = TicTacToe()
        >>> env1.get_state_hash() == env2.get_state_hash()
        True
        >>> env1.step(4)
        >>> env1.get_state_hash() == env2.get_state_hash()
        False
        """
        pass

    @abstractmethod
    def render(self, mode: str = 'human') -> Optional[str]:
        """
        Render the current board state.

        Parameters
        ----------
        mode : str, optional
            Rendering mode:
            - 'human': Print to console (default)
            - 'ansi': Return string representation

        Returns
        -------
        str or None
            String representation if mode='ansi', None if mode='human'

        Notes
        -----
        Human-readable visualization of the game state.
        Should display:
        - Current board configuration
        - Current player turn
        - Game status (ongoing, win, draw)

        Examples
        --------
        >>> env.render()
         . | . | .
        -----------
         . | X | .
        -----------
         . | . | .
        Current player: O (Player -1)
        """
        pass

    # Optional methods with default implementations

    def evaluate_heuristic(self, player: int) -> float:
        """
        Heuristic evaluation function for non-terminal states.

        Parameters
        ----------
        player : int
            Player from whose perspective to evaluate (1 or -1)

        Returns
        -------
        float
            Heuristic value in range [-1, 1]
            Positive values favor player, negative favor opponent

        Notes
        -----
        **Optional but highly recommended** for games with large state spaces.

        Required for depth-limited minimax search:
        - Small boards (3×3): Exact search feasible, heuristic not needed
        - Large boards (5×5+): State space explosion, heuristic essential

        Good heuristics:
        - Count potential winning lines
        - Weight by pieces in line (2-in-a-row > 1-in-a-row)
        - Control of center squares
        - Mobility (number of legal moves)

        Theory Connection:
        Depth-limited minimax approximates V*(s) ≈ V̂(s) where V̂ is the
        heuristic. Better heuristic → stronger play at shallow depth.

        Default implementation returns 0.0 (neutral evaluation).
        Override for games requiring depth-limited search.

        Examples
        --------
        >>> env.evaluate_heuristic(player=1)
        0.42  # Slight advantage for player 1
        """
        # Default: neutral evaluation
        # Override in subclasses for depth-limited minimax
        return 0.0

    def __repr__(self) -> str:
        """String representation of the game environment."""
        return f"{self.__class__.__name__}(board_size={self.board_size}, done={self.done})"

    def __str__(self) -> str:
        """Human-readable string representation."""
        return self.render(mode='ansi') or repr(self)
