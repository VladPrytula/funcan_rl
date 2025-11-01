"""
Connect Four environment with gravity mechanics.

Theory Connection (Syllabus Week 24):
    - State space: Finite MDP with |S| ≈ 4.5 trillion reachable states
    - Action space: A(s) = {columns with empty top cell}
    - Transition: Deterministic (place piece in column, gravity drops)
    - Rewards: +1 (win), -1 (loss), 0 (draw)
    - Discount: γ=1 (episodic, no discounting)

Complexity:
    - State space: 3^42 ≈ 1.09 × 10^20 (upper bound)
    - Actual reachable: ~4.5 trillion (Allis 1988)
    - Branching factor: ~7 (vs. ~9 for Tic-Tac-Toe)

References:
    - Allis (1988): Connect Four is solved (first player win with perfect play)
    - Tromp (2008): Number of legal positions: 4,531,985,219,092
"""

from typing import Dict, Optional, Tuple
import numpy as np


class ConnectFour:
    """
    Connect Four: 7×6 board, gravity mechanics, 4-in-a-row wins.

    Theory Connection (Week 24):
    - MDP formulation: (S, A, P, R, γ) where:
      * S: Game positions (4.5 trillion reachable)
      * A(s): Columns with empty top cell (dynamic, max 7)
      * P(s'|s,a): Deterministic (gravity drops piece)
      * R(s,a,s'): +1 (win), -1 (loss), 0 (draw/continue)
      * γ: 1 (episodic, no discounting)

    [THM-24.X.Y]: Bellman optimality equation characterizes V*(s)
    V*(s) = max_a [R(s,a) + γ Σ P(s'|s,a) V*(s')]

    For Connect Four:
    - Exact search intractable (4.5T states)
    - MCTS approximates V* via Monte Carlo sampling (Week 27-28)
    """

    def __init__(self, rows: int = 6, cols: int = 7, win_length: int = 4):
        """
        Initialize Connect Four environment.

        Args:
            rows: Number of rows (default: 6)
            cols: Number of columns (default: 7)
            win_length: Number in a row to win (default: 4)
        """
        self.rows = rows
        self.cols = cols
        self.board_size = rows * cols
        self.win_length = win_length

        # Board representation: 1D array, row-major order
        # Index: row * cols + col
        # Empty: 0, Player 1: +1, Player 2: -1
        self.board = np.zeros(self.board_size, dtype=np.int8)

        self.current_player = 1  # 1 or -1
        self.winner = None  # None, 1, -1, or 0 (draw)
        self.move_count = 0
        self.last_move = None  # Last placed position (index)

    def reset(self) -> np.ndarray:
        """Reset environment to initial state."""
        self.board = np.zeros(self.board_size, dtype=np.int8)
        self.current_player = 1
        self.winner = None
        self.move_count = 0
        self.last_move = None
        return self.board.copy()

    def step(self, col: int) -> Tuple[np.ndarray, float, bool, Dict]:
        """
        Make a move in the specified column.

        Args:
            col: Column index (0 to cols-1)

        Returns:
            state: Updated board state
            reward: +1 (win), -1 (loss), 0 (draw/continue)
            done: True if game is terminal
            info: Additional information

        Raises:
            ValueError: If column is full or invalid
        """
        if col < 0 or col >= self.cols:
            raise ValueError(f"Invalid column: {col}. Must be 0-{self.cols-1}.")

        # Find lowest empty row in column (gravity)
        row = self._find_lowest_row(col)
        if row is None:
            raise ValueError(f"Column {col} is full.")

        # Place piece
        index = row * self.cols + col
        self.board[index] = self.current_player
        self.last_move = index
        self.move_count += 1

        # Check for win
        if self._check_win_from_position(index):
            self.winner = self.current_player
            reward = 1.0 if self.current_player == 1 else -1.0
            done = True
        # Check for draw
        elif self.move_count == self.board_size:
            self.winner = 0
            reward = 0.0
            done = True
        else:
            reward = 0.0
            done = False
            self.current_player = -self.current_player  # Switch players

        info = {
            'move_count': self.move_count,
            'last_move': self.last_move,
            'winner': self.winner
        }

        return self.board.copy(), reward, done, info

    def get_legal_moves(self) -> np.ndarray:
        """
        Get legal column moves (columns with empty top cell).

        Returns:
            Array of legal column indices
        """
        legal = []
        for col in range(self.cols):
            # Check if top row of column is empty
            if self.board[(self.rows - 1) * self.cols + col] == 0:
                legal.append(col)
        return np.array(legal, dtype=np.int32)

    def is_terminal(self) -> bool:
        """Check if game is over (win or draw)."""
        return self.winner is not None

    def get_result(self, player: int) -> float:
        """
        Get game result from perspective of player.

        Args:
            player: 1 or -1

        Returns:
            +1.0 if player won, -1.0 if lost, 0.0 if draw
        """
        if self.winner is None:
            raise ValueError("Game is not terminal.")
        if self.winner == 0:
            return 0.0
        return 1.0 if self.winner == player else -1.0

    def render(self, mode: str = 'human') -> Optional[str]:
        """
        Render board state.

        Args:
            mode: 'human' (print to console) or 'ansi' (return string)

        Returns:
            String representation if mode='ansi'
        """
        symbols = {0: '.', 1: 'X', -1: 'O'}

        # Column labels
        header = '  ' + ' '.join(chr(ord('a') + c) for c in range(self.cols))

        lines = [header]
        lines.append('  ' + '-' * (2 * self.cols - 1))

        # Rows (top to bottom)
        for row in range(self.rows - 1, -1, -1):
            row_str = f"{row + 1} "
            for col in range(self.cols):
                index = row * self.cols + col
                row_str += symbols[self.board[index]]
                if col < self.cols - 1:
                    row_str += ' '
            lines.append(row_str)

        board_str = '\n'.join(lines)

        if mode == 'human':
            print(board_str)
            return None
        else:
            return board_str

    def copy(self) -> 'ConnectFour':
        """Create a deep copy of the environment."""
        env_copy = ConnectFour(rows=self.rows, cols=self.cols, win_length=self.win_length)
        env_copy.board = self.board.copy()
        env_copy.current_player = self.current_player
        env_copy.winner = self.winner
        env_copy.move_count = self.move_count
        env_copy.last_move = self.last_move
        return env_copy

    def get_state_hash(self) -> str:
        """
        Get hash of current state for memoization.

        Returns:
            String hash of (board, current_player)
        """
        return f"{self.board.tobytes()}|{self.current_player}"

    def evaluate_heuristic(self, player: int) -> float:
        """
        Heuristic evaluation for depth-limited MCTS.

        Algorithm:
        1. For each line (horizontal/vertical/diagonal):
           - Count open 3-in-a-row: +100 (threat)
           - Count open 2-in-a-row: +10 (potential)
           - Penalize opponent's threats: -100
        2. Center column control: +3 per piece (positional bonus)
        3. Normalize to [-1, 1]

        Theory-Practice Gap:
        - Theory: V*(s) via exact Bellman backup (intractable)
        - Practice: Heuristic approximation (domain knowledge)
        - Honest note: This heuristic is not optimal, but "good enough"

        References:
        - Allis (1988): Connect Four is solved (first player win with perfect play)
        - Heuristic based on classic Connect Four strategy (center control, threats)

        Args:
            player: 1 or -1

        Returns:
            Estimated value in [-1, 1]
        """
        if self.is_terminal():
            return self.get_result(player)

        score = 0.0
        opponent = -player

        # 1. Sliding window over all lines
        # Horizontal lines
        for row in range(self.rows):
            for col in range(self.cols - self.win_length + 1):
                window = [self.board[row * self.cols + col + i] for i in range(self.win_length)]
                score += self._evaluate_window(window, player)

        # Vertical lines
        for col in range(self.cols):
            for row in range(self.rows - self.win_length + 1):
                window = [self.board[(row + i) * self.cols + col] for i in range(self.win_length)]
                score += self._evaluate_window(window, player)

        # Diagonal (positive slope)
        for row in range(self.rows - self.win_length + 1):
            for col in range(self.cols - self.win_length + 1):
                window = [self.board[(row + i) * self.cols + col + i] for i in range(self.win_length)]
                score += self._evaluate_window(window, player)

        # Diagonal (negative slope)
        for row in range(self.win_length - 1, self.rows):
            for col in range(self.cols - self.win_length + 1):
                window = [self.board[(row - i) * self.cols + col + i] for i in range(self.win_length)]
                score += self._evaluate_window(window, player)

        # 2. Center column bonus
        center_col = self.cols // 2
        for row in range(self.rows):
            if self.board[row * self.cols + center_col] == player:
                score += 3
            elif self.board[row * self.cols + center_col] == opponent:
                score -= 3

        # 3. Normalize
        max_score = 100 * (self.rows * self.cols)  # Rough upper bound
        return np.clip(score / max_score, -1.0, 1.0)

    def _evaluate_window(self, window: list, player: int) -> float:
        """
        Evaluate a 4-cell window.

        Args:
            window: List of 4 cell values
            player: Player to evaluate for

        Returns:
            Score contribution
        """
        opponent = -player
        player_count = window.count(player)
        opponent_count = window.count(opponent)
        empty_count = window.count(0)

        # Mixed window: no value
        if player_count > 0 and opponent_count > 0:
            return 0.0

        # Player's window
        if player_count == 3 and empty_count == 1:
            return 100.0  # Threat
        elif player_count == 2 and empty_count == 2:
            return 10.0   # Potential
        elif player_count == 4:
            return 1000.0  # Should not happen (game would be over)

        # Opponent's window
        if opponent_count == 3 and empty_count == 1:
            return -100.0  # Block threat
        elif opponent_count == 2 and empty_count == 2:
            return -10.0   # Block potential
        elif opponent_count == 4:
            return -1000.0  # Should not happen

        return 0.0

    def _find_lowest_row(self, col: int) -> Optional[int]:
        """
        Find lowest empty row in column (gravity).

        Args:
            col: Column index

        Returns:
            Row index, or None if column is full
        """
        for row in range(self.rows):
            if self.board[row * self.cols + col] == 0:
                return row
        return None

    def _check_win_from_position(self, index: int) -> bool:
        """
        Check if last placed piece at index creates 4-in-a-row.

        Args:
            index: Position of last placed piece

        Returns:
            True if win detected
        """
        row = index // self.cols
        col = index % self.cols
        player = self.board[index]

        # Horizontal
        count = 1
        # Left
        for c in range(col - 1, -1, -1):
            if self.board[row * self.cols + c] == player:
                count += 1
            else:
                break
        # Right
        for c in range(col + 1, self.cols):
            if self.board[row * self.cols + c] == player:
                count += 1
            else:
                break
        if count >= self.win_length:
            return True

        # Vertical
        count = 1
        # Down
        for r in range(row - 1, -1, -1):
            if self.board[r * self.cols + col] == player:
                count += 1
            else:
                break
        # Up
        for r in range(row + 1, self.rows):
            if self.board[r * self.cols + col] == player:
                count += 1
            else:
                break
        if count >= self.win_length:
            return True

        # Diagonal (positive slope)
        count = 1
        # Down-left
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if self.board[r * self.cols + c] == player:
                count += 1
                r -= 1
                c -= 1
            else:
                break
        # Up-right
        r, c = row + 1, col + 1
        while r < self.rows and c < self.cols:
            if self.board[r * self.cols + c] == player:
                count += 1
                r += 1
                c += 1
            else:
                break
        if count >= self.win_length:
            return True

        # Diagonal (negative slope)
        count = 1
        # Up-left
        r, c = row + 1, col - 1
        while r < self.rows and c >= 0:
            if self.board[r * self.cols + c] == player:
                count += 1
                r += 1
                c -= 1
            else:
                break
        # Down-right
        r, c = row - 1, col + 1
        while r >= 0 and c < self.cols:
            if self.board[r * self.cols + c] == player:
                count += 1
                r -= 1
                c += 1
            else:
                break
        if count >= self.win_length:
            return True

        return False
