"""
Step 1: Tic-Tac-Toe as an MDP (80 lines)

Goal: Understand MDP formulation and professional algebraic notation

Theory Connection:
- [DEF-25.1.1] MDP = (S, A, P, R, γ)
  - State space S: Board configurations (3^9 = 19,683 possible, ~5,478 reachable)
  - Action space A(s): Empty cell positions (variable size, max 9)
  - Transition P(s'|s,a): Deterministic (place piece, check winner, swap players)
  - Reward R(s,a,s'): +1 (X wins), -1 (O wins), 0 (draw/continue)
  - Discount γ: 1 (episodic task, no discounting)

Pedagogical Innovation: Algebraic Notation
- Professional standard: a1, b2, c3 (like chess)
- Scales to larger boards: 4×4 = a1-d4, 15×15 Gomoku = a1-o15
- Reusable across all game projects (Weeks 24, 31, 40-41, 42-48)

Time: 15 minutes (read code + run test + exercise)
"""

import numpy as np
from typing import List, Optional, Tuple


def get_position_name(index: int, board_size: int = 3) -> str:
    """
    Convert flat index to algebraic notation

    Examples (3×3 board):
        0 → a1, 1 → b1, 2 → c1
        3 → a2, 4 → b2, 5 → c2
        6 → a3, 7 → b3, 8 → c3

    Theory: Establishes professional notation standard used throughout course
    """
    row = index // board_size
    col = index % board_size
    return f"{chr(ord('a') + col)}{row + 1}"


def parse_position(pos: str, board_size: int = 3) -> int:
    """
    Convert algebraic notation to flat index

    Examples: "a1" → 0, "b2" → 4, "c3" → 8
    Handles: "A1", "a 1", "a1" (case-insensitive, ignores spaces)
    """
    pos = pos.lower().replace(" ", "")
    col = ord(pos[0]) - ord('a')
    row = int(pos[1:]) - 1
    return row * board_size + col


class TicTacToe:
    """
    Tic-Tac-Toe Environment as MDP

    State: board (9-element array): 0=empty, 1=X, -1=O
    Actions: Legal moves (empty cell indices)
    Transitions: Deterministic (place piece, check winner, swap players)
    Rewards: +1 (X wins), -1 (O wins), 0 (otherwise)
    """

    def __init__(self, board_size: int = 3):
        self.board_size = board_size
        self.board = np.zeros(board_size * board_size, dtype=np.int8)
        self.current_player = 1  # X starts

    def reset(self) -> np.ndarray:
        """Reset to empty board (initial state s₀)"""
        self.board = np.zeros(self.board_size * self.board_size, dtype=np.int8)
        self.current_player = 1
        return self.board.copy()

    def get_legal_moves(self) -> List[int]:
        """
        Action space A(s): Indices of empty cells

        Theory: A(s) ⊆ {0, 1, ..., 8} is state-dependent (shrinks as game progresses)
        """
        return np.where(self.board == 0)[0].tolist()

    def is_terminal(self) -> bool:
        """Check if game is over (win or draw)"""
        return self._check_winner() is not None or len(self.get_legal_moves()) == 0

    def step(self, action: int) -> Tuple[np.ndarray, float, bool]:
        """
        Transition function P(s'|s,a) and reward R(s,a,s')

        Returns:
            next_state: Board after move
            reward: +1 (X wins), -1 (O wins), 0 (continue/draw)
            done: True if game over

        Theory: Deterministic transition (no stochasticity in Tic-Tac-Toe)
        """
        assert self.board[action] == 0, f"Illegal move: position {action} already occupied"

        # Place piece
        self.board[action] = self.current_player

        # Check winner
        winner = self._check_winner()
        if winner is not None:
            reward = float(winner)  # +1 (X wins), -1 (O wins), 0 (draw)
            return self.board.copy(), reward, True

        # Check draw
        if len(self.get_legal_moves()) == 0:
            return self.board.copy(), 0.0, True

        # Switch players
        self.current_player *= -1
        return self.board.copy(), 0.0, False

    def _check_winner(self) -> Optional[int]:
        """
        Check all 8 winning lines (3 rows, 3 cols, 2 diagonals)

        Returns: 1 (X wins), -1 (O wins), None (no winner yet)

        Exercise: Modify to return which line won (row/column/diagonal number)
        """
        n = self.board_size

        # Check rows
        for i in range(n):
            line = self.board[i*n:(i+1)*n]
            if np.all(line == 1):
                return 1
            if np.all(line == -1):
                return -1

        # Check columns
        for i in range(n):
            line = self.board[i::n]
            if np.all(line == 1):
                return 1
            if np.all(line == -1):
                return -1

        # Check main diagonal (top-left to bottom-right)
        line = self.board[[i*n + i for i in range(n)]]
        if np.all(line == 1):
            return 1
        if np.all(line == -1):
            return -1

        # Check anti-diagonal (top-right to bottom-left)
        line = self.board[[i*n + (n-1-i) for i in range(n)]]
        if np.all(line == 1):
            return 1
        if np.all(line == -1):
            return -1

        return None

    def get_result(self, player: int) -> float:
        """
        Get game result from player's perspective

        Args:
            player: 1 (X) or -1 (O)

        Returns: +1 (player wins), -1 (player loses), 0 (draw/ongoing)
        """
        winner = self._check_winner()
        if winner is None:
            return 0.0
        return float(winner * player)

    def render_ascii(self) -> str:
        """
        Render board with algebraic notation labels

        Example (3×3):
            a  b  c
          1 X  .  O
          2 .  X  .
          3 O  .  X
        """
        n = self.board_size
        symbols = {0: '.', 1: 'X', -1: 'O'}

        # Column labels
        lines = ["  " + " ".join(chr(ord('a') + i) for i in range(n))]

        # Rows with row numbers
        for i in range(n):
            row = self.board[i*n:(i+1)*n]
            row_str = f"{i+1} " + " ".join(symbols[x] for x in row)
            lines.append(row_str)

        return "\n".join(lines)

    def copy(self):
        """Create deep copy of environment (for minimax tree search)"""
        env_copy = TicTacToe(self.board_size)
        env_copy.board = self.board.copy()
        env_copy.current_player = self.current_player
        return env_copy


# ============================================================================
# Test: Random Game with Algebraic Notation
# ============================================================================

if __name__ == "__main__":
    print("Step 1: Tic-Tac-Toe MDP with Algebraic Notation\n")
    print("Playing random game to demonstrate MDP interface...\n")

    env = TicTacToe()
    move_count = 0

    while not env.is_terminal():
        print(env.render_ascii())
        print(f"\nPlayer {'X' if env.current_player == 1 else 'O'} to move")

        # Random move
        legal_moves = env.get_legal_moves()
        action = np.random.choice(legal_moves)
        action_name = get_position_name(action)

        print(f"Action: {action_name} (index {action})")

        state, reward, done = env.step(action)
        move_count += 1
        print()

    # Game over
    print(env.render_ascii())
    print(f"\n{'='*30}")
    print(f"Game over after {move_count} moves")

    winner = env._check_winner()
    if winner == 1:
        print("Result: X wins (+1)")
    elif winner == -1:
        print("Result: O wins (-1)")
    else:
        print("Result: Draw (0)")

    print("\n" + "="*30)
    print("✅ Step 1 complete!")
    print("\nNext: Step 2 (naive minimax implementation)")
    print("Expected: First move takes 30-60 seconds (computational pain!)")
