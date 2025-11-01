"""
Tic-Tac-Toe game environment.

3×3 Tic-Tac-Toe as a two-player zero-sum game, solvable via exact dynamic programming.
This implementation serves as the foundation for understanding game-theoretic MDPs.

Theory Connections (Week 24):
- Finite-horizon MDP formulation with adversarial transitions
- Minimax as value iteration on game tree [THM-24.X.Y]
- Nash equilibrium: game is a draw under optimal play
- Connection to Bellman optimality principle in zero-sum games

References:
- Puterman Ch 6: Value iteration for finite MDPs
- Bertsekas Vol I Ch 1: Dynamic programming and optimal control
- von Neumann (1928): Minimax theorem for zero-sum games

"""

import numpy as np
from typing import Optional, Tuple, List
from rl_toolkit.utils.board_viz import render_board_ascii


class TicTacToe:
    """
    3×3 Tic-Tac-Toe environment.

    State Space
    -----------
    - Board: 3×3 grid with values in {-1, 0, 1}
    - 0: empty square
    - 1: player 1 (X)
    - -1: player 2 (O)
    - Total states: ~5,000 after symmetry reduction

    Action Space
    ------------
    - Actions: place piece at (row, col) where board[row, col] == 0
    - Actions encoded as integers 0-8 (flattened board indices)

    Dynamics
    --------
    - Deterministic: placing a piece always succeeds if legal
    - Terminal states: win, loss, or draw (no legal moves)

    Reward
    ------
    - +1 for win
    - -1 for loss
    - 0 for draw
    - 0 for non-terminal states

    Theory (Week 24)
    ----------------
    This is a finite-horizon MDP with adversarial transitions:
    - State value: V*(s) = expected outcome under optimal play
    - Bellman optimality: V*(s) = max_a E[V*(s')|s,a] for maximizing player
    - Minimax equivalence: max-player maximizes, min-player minimizes
    - Result: V*(s) = 0 for all states (provable draw)

    Examples
    --------
    >>> env = TicTacToe()
    >>> env.reset()
    >>> env.step(4)  # Place X in center
    >>> env.render()
    >>> env.is_terminal()
    False
    """

    def __init__(self, board_size: int = 3, win_length: int = None):
        """
        Initialize Tic-Tac-Toe environment with configurable board size.

        Parameters
        ----------
        board_size : int, optional
            Size of the board (n×n), default 3
        win_length : int, optional
            Number in a row needed to win (k-in-a-row), default equals board_size
            For example: 5×5 board with win_length=4 is more balanced

        Examples
        --------
        >>> env = TicTacToe()  # Classic 3×3
        >>> env = TicTacToe(board_size=5, win_length=4)  # 5×5 board, 4-in-a-row wins
        """
        self.board_size = board_size
        self.win_length = win_length if win_length is not None else board_size
        self.board = np.zeros((board_size, board_size), dtype=np.int8)
        self.current_player = 1  # Player 1 starts (X)
        self.winner = None
        self.done = False

        # Validate parameters
        if self.win_length > self.board_size:
            raise ValueError(f"win_length ({self.win_length}) cannot exceed board_size ({self.board_size})")
        if self.win_length < 3:
            raise ValueError(f"win_length ({self.win_length}) must be at least 3")

    def reset(self) -> np.ndarray:
        """
        Reset the game to initial state.

        Returns
        -------
        np.ndarray
            Initial board state (all zeros)
        """
        self.board = np.zeros((self.board_size, self.board_size), dtype=np.int8)
        self.current_player = 1
        self.winner = None
        self.done = False
        return self.board.copy()

    def get_legal_moves(self) -> np.ndarray:
        """
        Get all legal moves (empty squares).

        Returns
        -------
        np.ndarray
            Array of legal move indices (flattened), shape (n_legal_moves,)

        Examples
        --------
        >>> env = TicTacToe()
        >>> env.get_legal_moves()
        array([0, 1, 2, 3, 4, 5, 6, 7, 8])
        """
        return np.where(self.board.flatten() == 0)[0]

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, dict]:
        """
        Execute a move and return the new state.

        Parameters
        ----------
        action : int
            Flattened board index (0-8) where to place the piece

        Returns
        -------
        state : np.ndarray
            New board state after the move
        reward : float
            Reward for the current player (+1 win, -1 loss, 0 otherwise)
        done : bool
            Whether the game has ended
        info : dict
            Additional information (winner, legal moves)

        Raises
        ------
        ValueError
            If the move is illegal (square already occupied)

        Examples
        --------
        >>> env = TicTacToe()
        >>> state, reward, done, info = env.step(4)  # Center square
        >>> reward
        0.0
        >>> done
        False
        """
        if self.done:
            raise ValueError("Game is already over. Call reset() to start a new game.")

        # Convert flattened index to (row, col)
        row, col = action // self.board_size, action % self.board_size

        # Check if move is legal
        if self.board[row, col] != 0:
            raise ValueError(f"Illegal move: square ({row}, {col}) is already occupied.")

        # Place the piece
        self.board[row, col] = self.current_player

        # Check for win or draw
        reward = 0.0
        if self.check_win(self.current_player):
            self.winner = self.current_player
            self.done = True
            reward = 1.0  # Current player wins
        elif len(self.get_legal_moves()) == 0:
            # Draw (no winner, no legal moves)
            self.done = True
            reward = 0.0
        else:
            # Game continues, switch player
            self.current_player *= -1

        info = {
            'winner': self.winner,
            'legal_moves': self.get_legal_moves() if not self.done else []
        }

        return self.board.copy(), reward, self.done, info

    def check_win(self, player: int) -> bool:
        """
        Check if the specified player has won (k-in-a-row on n×n board).

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
        Winning conditions (k = win_length):
        - k in a row (any row, any position)
        - k in a column (any column, any position)
        - k on a diagonal (any diagonal, either direction)

        Algorithm uses sliding window to check for k consecutive marks.
        Complexity: O(n²) where n = board_size
        """
        k = self.win_length
        n = self.board_size

        # Check rows
        for row in range(n):
            for col in range(n - k + 1):
                if np.all(self.board[row, col:col+k] == player):
                    return True

        # Check columns
        for col in range(n):
            for row in range(n - k + 1):
                if np.all(self.board[row:row+k, col] == player):
                    return True

        # Check diagonals (top-left to bottom-right)
        for row in range(n - k + 1):
            for col in range(n - k + 1):
                if all(self.board[row+i, col+i] == player for i in range(k)):
                    return True

        # Check anti-diagonals (top-right to bottom-left)
        for row in range(n - k + 1):
            for col in range(k - 1, n):
                if all(self.board[row+i, col-i] == player for i in range(k)):
                    return True

        return False

    def is_terminal(self) -> bool:
        """
        Check if the game has ended.

        Returns
        -------
        bool
            True if game is over (win or draw), False otherwise
        """
        return self.done

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
            +1 if player won, -1 if player lost, 0 if draw, None if game not over

        Examples
        --------
        >>> env = TicTacToe()
        >>> env.step(0); env.step(3); env.step(1); env.step(4); env.step(2)
        >>> env.get_result(1)  # Player 1 (X) wins
        1.0
        """
        if not self.done:
            return None

        if self.winner is None:
            return 0.0  # Draw
        elif self.winner == player:
            return 1.0  # Win
        else:
            return -1.0  # Loss

    def render(self, mode: str = 'human') -> Optional[str]:
        """
        Render the current board state.

        Parameters
        ----------
        mode : str, optional
            Rendering mode. Options:
            - 'human': print to console
            - 'ansi': return string representation

        Returns
        -------
        str or None
            String representation if mode='ansi', None if mode='human'
        """
        board_str = render_board_ascii(self.board)

        if mode == 'human':
            print(board_str)
            if self.done:
                if self.winner == 1:
                    print("Game Over: X (Player 1) wins!")
                elif self.winner == -1:
                    print("Game Over: O (Player 2) wins!")
                else:
                    print("Game Over: Draw!")
            else:
                player_symbol = 'X' if self.current_player == 1 else 'O'
                print(f"Current player: {player_symbol} (Player {self.current_player})")
            return None
        elif mode == 'ansi':
            return board_str
        else:
            raise ValueError(f"Unknown render mode: {mode}")

    def copy(self) -> 'TicTacToe':
        """
        Create a deep copy of the current game state.

        Returns
        -------
        TicTacToe
            New environment instance with identical state

        Notes
        -----
        Useful for lookahead search (minimax) without modifying original state.
        """
        new_env = TicTacToe()
        new_env.board = self.board.copy()
        new_env.current_player = self.current_player
        new_env.winner = self.winner
        new_env.done = self.done
        return new_env

    def get_state_hash(self) -> str:
        """
        Get a hashable representation of the current state.

        Returns
        -------
        str
            Unique string identifier for this board configuration

        Notes
        -----
        Used for memoization in minimax search (dynamic programming).
        Theory: Caching eliminates redundant subproblem computation.
        """
        # Include both board state and current player
        return f"{self.board.tobytes().hex()}_{self.current_player}"
