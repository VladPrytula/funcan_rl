# Adding a New Game: Quick Start Guide

**Status**: Ready to use
**Example**: Connect Four implementation
**Estimated Time**: 3-4 hours (game logic only—infrastructure already built)

---

## Quick Start: Connect Four in 5 Steps

### Step 1: Create the Game Class (10 minutes)

Create `code/rl_toolkit/envs/connect_four.py`:

```python
"""
Connect Four game environment.

Classic drop-piece game: 6 rows × 7 columns, 4-in-a-row wins.
"""

import numpy as np
from typing import Tuple, Optional
from rl_toolkit.envs.base_game import BaseGameEnv
from rl_toolkit.utils.board_viz import render_board_ascii


class ConnectFour(BaseGameEnv):
    """
    Connect Four environment (6×7 board, 4-in-a-row).

    Rules:
    - Players alternate dropping pieces into columns
    - Pieces fall to lowest empty row in chosen column
    - First to get 4-in-a-row (horizontal, vertical, or diagonal) wins
    - Draw if board fills with no winner
    """

    def __init__(self, rows: int = 6, cols: int = 7, win_length: int = 4):
        """Initialize Connect Four with standard 6×7 board."""
        # Use cols as board_size for BaseGameEnv compatibility
        super().__init__(board_size=cols)

        # Game-specific configuration
        self.rows = rows
        self.cols = cols
        self.win_length = win_length

        # Override board shape (not square!)
        self.board = np.zeros((rows, cols), dtype=np.int8)

    def reset(self) -> np.ndarray:
        """Reset to empty board."""
        self.board = np.zeros((self.rows, self.cols), dtype=np.int8)
        self.current_player = 1
        self.done = False
        self.winner = None
        return self.board.copy()

    def get_legal_moves(self) -> np.ndarray:
        """Return columns that aren't full."""
        # A column is legal if top row is empty
        legal_cols = []
        for col in range(self.cols):
            if self.board[0, col] == 0:
                legal_cols.append(col)
        return np.array(legal_cols, dtype=np.int64)

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, dict]:
        """
        Drop piece in column `action`.

        Action space: column indices (0 to cols-1)
        """
        if self.done:
            raise ValueError("Game over. Call reset().")

        # Validate action
        col = action
        if not (0 <= col < self.cols):
            raise ValueError(f"Invalid column {col} (must be 0-{self.cols-1})")
        if self.board[0, col] != 0:
            raise ValueError(f"Column {col} is full")

        # Find lowest empty row
        row = self._get_lowest_empty_row(col)
        if row is None:
            raise ValueError(f"Column {col} is full")

        # Place piece
        self.board[row, col] = self.current_player

        # Check for win
        reward = 0.0
        if self.check_win(self.current_player):
            self.winner = self.current_player
            self.done = True
            reward = 1.0
        elif len(self.get_legal_moves()) == 0:
            self.done = True  # Draw
            reward = 0.0
        else:
            self.current_player *= -1  # Switch player

        info = {'winner': self.winner, 'legal_moves': self.get_legal_moves()}
        return self.board.copy(), reward, self.done, info

    def _get_lowest_empty_row(self, col: int) -> Optional[int]:
        """Find the lowest empty row in a column (gravity!)."""
        for row in range(self.rows - 1, -1, -1):
            if self.board[row, col] == 0:
                return row
        return None  # Column full

    def check_win(self, player: int) -> bool:
        """Check if player has 4-in-a-row (any direction)."""
        k = self.win_length

        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - k + 1):
                if np.all(self.board[row, col:col+k] == player):
                    return True

        # Check vertical
        for col in range(self.cols):
            for row in range(self.rows - k + 1):
                if np.all(self.board[row:row+k, col] == player):
                    return True

        # Check diagonals (↘)
        for row in range(self.rows - k + 1):
            for col in range(self.cols - k + 1):
                if all(self.board[row+i, col+i] == player for i in range(k)):
                    return True

        # Check anti-diagonals (↙)
        for row in range(self.rows - k + 1):
            for col in range(k - 1, self.cols):
                if all(self.board[row+i, col-i] == player for i in range(k)):
                    return True

        return False

    def is_terminal(self) -> bool:
        """Game over if someone won or board is full."""
        return self.done

    def get_result(self, player: int) -> Optional[float]:
        """Get result from player's perspective."""
        if not self.done:
            return None
        if self.winner is None:
            return 0.0  # Draw
        return 1.0 if self.winner == player else -1.0

    def copy(self) -> 'ConnectFour':
        """Deep copy of game state."""
        new_env = ConnectFour(self.rows, self.cols, self.win_length)
        new_env.board = self.board.copy()
        new_env.current_player = self.current_player
        new_env.done = self.done
        new_env.winner = self.winner
        return new_env

    def get_state_hash(self) -> str:
        """Unique hash for memoization."""
        return f"{self.board.tobytes().hex()}_{self.current_player}"

    def render(self, mode: str = 'human') -> Optional[str]:
        """Render board."""
        board_str = render_board_ascii(self.board)
        if mode == 'human':
            print(board_str)
            return None
        return board_str

    def evaluate_heuristic(self, player: int) -> float:
        """
        Heuristic for depth-limited minimax (Connect Four has large state space).

        Score based on:
        - 3-in-a-row with 1 empty (high value)
        - 2-in-a-row with 2 empty (medium value)
        - Control of center columns (bonus)
        """
        # TODO: Implement heuristic (see TicTacToe example)
        return 0.0
```

---

### Step 2: Add to Package (2 minutes)

Edit `code/rl_toolkit/envs/__init__.py`:

```python
from rl_toolkit.envs.base_game import BaseGameEnv
from rl_toolkit.envs.tictactoe import TicTacToe
from rl_toolkit.envs.connect_four import ConnectFour  # ADD THIS

__all__ = ['BaseGameEnv', 'TicTacToe', 'ConnectFour']  # AND THIS
```

---

### Step 3: Write Tests (45 minutes)

Create `code/tests/test_connect_four.py`:

```python
"""Unit tests for Connect Four."""

import pytest
import numpy as np
from rl_toolkit.envs.connect_four import ConnectFour
from rl_toolkit.algorithms.minimax import MinimaxSolver


class TestConnectFourBasics:
    """Test basic game mechanics."""

    def test_initialization(self):
        """Test standard 6×7 board."""
        env = ConnectFour()
        assert env.board.shape == (6, 7)
        assert np.all(env.board == 0)
        assert env.current_player == 1
        assert not env.done

    def test_legal_moves_initial(self):
        """All columns start empty."""
        env = ConnectFour()
        legal = env.get_legal_moves()
        assert len(legal) == 7
        assert np.array_equal(legal, np.arange(7))

    def test_piece_falls(self):
        """Piece falls to bottom."""
        env = ConnectFour()
        env.step(3)  # Drop in column 3
        # Check bottom row, column 3
        assert env.board[5, 3] == 1
        # All other cells empty
        assert np.sum(env.board) == 1

    def test_pieces_stack(self):
        """Pieces stack vertically."""
        env = ConnectFour()
        env.step(0)  # Player 1 drops in col 0
        env.step(0)  # Player 2 drops in col 0
        assert env.board[5, 0] == 1   # Bottom
        assert env.board[4, 0] == -1  # On top

    def test_column_full(self):
        """Can't play in full column."""
        env = ConnectFour()
        # Fill column 0 (6 moves)
        for _ in range(6):
            env.step(0)
        # Column 0 no longer legal
        legal = env.get_legal_moves()
        assert 0 not in legal


class TestConnectFourWins:
    """Test win detection."""

    def test_horizontal_win(self):
        """Four in a row horizontally."""
        env = ConnectFour()
        # Player 1 builds bottom row: 0, 1, 2, 3
        env.step(0); env.step(0)  # Col 0
        env.step(1); env.step(1)  # Col 1
        env.step(2); env.step(2)  # Col 2
        env.step(3)  # Col 3 - wins!
        assert env.done
        assert env.winner == 1

    def test_vertical_win(self):
        """Four in a column."""
        env = ConnectFour()
        # Player 1 builds col 3: rows 5,4,3,2
        env.step(3); env.step(0)  # 1st piece
        env.step(3); env.step(0)  # 2nd piece
        env.step(3); env.step(0)  # 3rd piece
        env.step(3)  # 4th piece - wins!
        assert env.done
        assert env.winner == 1

    def test_diagonal_win(self):
        """Four in a diagonal (↗)."""
        env = ConnectFour()
        # Build diagonal: (5,0), (4,1), (3,2), (2,3)
        # This requires careful sequencing
        env.step(0)  # (5,0) P1
        env.step(1)  # (5,1) P2
        env.step(1)  # (4,1) P1
        env.step(2)  # (5,2) P2
        env.step(2)  # (4,2) P1
        env.step(3)  # (5,3) P2
        env.step(2)  # (3,2) P1
        env.step(3)  # (4,3) P2
        env.step(3)  # (3,3) P1
        env.step(4)  # (5,4) P2
        env.step(3)  # (2,3) P1 - diagonal win!
        assert env.done
        assert env.winner == 1


class TestMinimaxConnectFour:
    """Test minimax solver with Connect Four."""

    def test_minimax_basic(self):
        """Minimax returns valid move."""
        env = ConnectFour()
        solver = MinimaxSolver(max_depth=4)  # Shallow for speed
        move = solver.get_best_move(env, maximize=True)
        assert move in env.get_legal_moves()

    def test_minimax_blocks_threat(self):
        """AI blocks 3-in-a-row."""
        env = ConnectFour()
        # Manually set up board: player has 3 in bottom row
        env.board[5, 0] = 1
        env.board[5, 1] = 1
        env.board[5, 2] = 1
        env.current_player = -1  # AI's turn

        solver = MinimaxSolver(max_depth=4)
        move = solver.get_best_move(env, maximize=False)
        # Must block at column 3
        assert move == 3
```

Run tests:
```bash
pytest tests/test_connect_four.py -v
```

---

### Step 4: Create Playable Demo (30 minutes)

Create `code/projects/project_08.5_connect_four/play_terminal.py`:

```python
"""Terminal interface for Connect Four."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from rl_toolkit.envs.connect_four import ConnectFour
from rl_toolkit.algorithms.minimax import MinimaxSolver


def play_game():
    """Play Connect Four against minimax AI."""
    env = ConnectFour()
    solver = MinimaxSolver(max_depth=6)  # 6-ply search

    print("\n" + "=" * 60)
    print("  CONNECT FOUR: Human vs. AI")
    print("=" * 60)
    print("Rules: Drop pieces, get 4-in-a-row to win!")
    print("=" * 60)

    env.reset()

    while not env.is_terminal():
        print("\n" + "-" * 60)
        env.render()

        if env.current_player == 1:
            # Human's turn
            legal = env.get_legal_moves()
            print(f"\nLegal columns: {legal.tolist()}")
            try:
                col = int(input("Your move (column 0-6): "))
                env.step(col)
            except (ValueError, Exception) as e:
                print(f"Error: {e}")
                continue
        else:
            # AI's turn
            print("\n🤖 AI is thinking...")
            move = solver.get_best_move(env, maximize=False)
            print(f"AI drops in column {move}")
            env.step(move)

    # Game over
    env.render()
    winner = env.winner
    if winner == 1:
        print("\n🎉 You won!")
    elif winner == -1:
        print("\n🤖 AI wins!")
    else:
        print("\n🤝 Draw!")


if __name__ == '__main__':
    play_game()
```

---

### Step 5: Test and Play! (15 minutes)

```bash
# Run tests
cd code
pytest tests/test_connect_four.py -v

# Play the game!
cd projects/project_08.5_connect_four
python play_terminal.py
```

---

## What You Get For Free

✅ **Minimax solver works immediately** (no changes needed!)
✅ **Position naming utilities** (algebraic notation for columns)
✅ **Abstract interface enforces correctness** (type checking)
✅ **Clear documentation** (docstrings with theory connections)

---

## Customization Checklist

- [ ] Implement game-specific `check_win()` logic
- [ ] Implement game-specific `get_legal_moves()` (gravity for Connect Four!)
- [ ] Implement `evaluate_heuristic()` for depth-limited search
- [ ] Write comprehensive tests (basic mechanics, win detection, minimax)
- [ ] Create terminal interface (`play_terminal.py`)
- [ ] (Optional) Create web interface (reuse Flask template from Tic-Tac-Toe)

---

## Time Breakdown

- **Step 1**: Game class (45 min) - core logic
- **Step 2**: Package integration (2 min) - trivial
- **Step 3**: Tests (45 min) - ensure correctness
- **Step 4**: Terminal interface (30 min) - playable demo
- **Step 5**: Testing & debugging (15 min) - polish

**Total**: ~2.5 hours (vs. 10+ hours without BaseGameEnv infrastructure!)

---

## Common Patterns

### Pattern 1: Square Board (Tic-Tac-Toe, Gomoku, Reversi)

```python
class MyGame(BaseGameEnv):
    def __init__(self, board_size: int = 8):
        super().__init__(board_size)  # Square board
        # ... game-specific setup
```

### Pattern 2: Rectangular Board (Connect Four, Chess)

```python
class MyGame(BaseGameEnv):
    def __init__(self, rows: int = 6, cols: int = 7):
        super().__init__(board_size=cols)  # Use one dimension
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=np.int8)  # Override shape
```

### Pattern 3: Custom Action Space (Connect Four columns)

```python
def get_legal_moves(self) -> np.ndarray:
    """Legal moves = columns that aren't full."""
    return np.array([col for col in range(self.cols) if self.board[0, col] == 0])
```

---

## Troubleshooting

### Import Error: `ModuleNotFoundError: No module named 'rl_toolkit'`

```bash
cd code/
pip install -e .
```

### Tests Fail: `AttributeError: 'MyGame' object has no attribute '...'`

→ Check that you've implemented ALL abstract methods from `BaseGameEnv`.

### Minimax Too Slow

→ Implement `evaluate_heuristic()` and use `max_depth` parameter:
```python
solver = MinimaxSolver(max_depth=6)  # Depth-limited search
```

---

## Next Steps

1. **Complete Connect Four** (~3 hours)
2. **Add web interface** (~2 hours, reuse Tic-Tac-Toe template)
3. **Implement Gomoku** (Week 40-41, ~3 hours)
4. **Implement Reversi** (Week 44-48, ~4 hours + neural nets)

---

**You're ready to build new games!** The infrastructure is complete—just implement game rules and you'll have a working minimax solver + playable interface in 3-4 hours.
