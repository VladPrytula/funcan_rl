"""
Board visualization utilities for grid-based games.

Provides ASCII rendering for n×n board games (Tic-Tac-Toe, Connect Four, Gomoku, Reversi).
Reusable across all game projects.

Author: Dr. Max Rubin
"""

import numpy as np
from typing import Optional, Dict, Any


def render_board_ascii(
    board: np.ndarray,
    symbols: Optional[Dict[int, str]] = None,
    show_indices: bool = True
) -> str:
    """
    Render a 2D board as ASCII art with grid lines.

    Parameters
    ----------
    board : np.ndarray
        2D array representing the board state.
        Shape: (rows, cols)
    symbols : Dict[int, str], optional
        Mapping from board values to display symbols.
        Default: {0: ' ', 1: 'X', -1: 'O'}
    show_indices : bool, optional
        Whether to show row/column indices. Default: True

    Returns
    -------
    str
        ASCII representation of the board

    Examples
    --------
    >>> board = np.array([[1, 0, -1], [0, 1, 0], [-1, 0, 1]])
    >>> print(render_board_ascii(board))
          0   1   2
        +---+---+---+
      0 | X |   | O |
        +---+---+---+
      1 |   | X |   |
        +---+---+---+
      2 | O |   | X |
        +---+---+---+
    """
    if symbols is None:
        symbols = {0: ' ', 1: 'X', -1: 'O'}

    rows, cols = board.shape

    # Build the output string
    lines = []

    # Column indices (if requested)
    if show_indices:
        col_header = "  " + "   ".join(str(i) for i in range(cols))
        lines.append(col_header)

    # Top border
    border = "  " + "+---" * cols + "+"
    lines.append(border)

    # Board rows
    for i in range(rows):
        # Row with symbols
        row_str = ""
        if show_indices:
            row_str += f"{i} "

        row_str += "|"
        for j in range(cols):
            cell_value = board[i, j]
            symbol = symbols.get(cell_value, '?')
            row_str += f" {symbol} |"

        lines.append(row_str)

        # Horizontal separator
        lines.append(border)

    return "\n".join(lines)


def render_board_compact(board: np.ndarray, symbols: Optional[Dict[int, str]] = None) -> str:
    """
    Render board in compact format (no grid lines, just symbols).

    Useful for logging or quick debugging.

    Parameters
    ----------
    board : np.ndarray
        2D array representing the board state
    symbols : Dict[int, str], optional
        Mapping from board values to display symbols

    Returns
    -------
    str
        Compact ASCII representation

    Examples
    --------
    >>> board = np.array([[1, 0, -1], [0, 1, 0], [-1, 0, 1]])
    >>> print(render_board_compact(board))
    X O
     X
    O X
    """
    if symbols is None:
        symbols = {0: '.', 1: 'X', -1: 'O'}

    lines = []
    for row in board:
        line = " ".join(symbols.get(val, '?') for val in row)
        lines.append(line)

    return "\n".join(lines)


def board_to_string(board: np.ndarray) -> str:
    """
    Convert board to hashable string representation.

    Useful for memoization in minimax search.

    Parameters
    ----------
    board : np.ndarray
        Board state to convert

    Returns
    -------
    str
        String representation suitable for dictionary keys
    """
    return board.tobytes().hex()


def print_move_prompt(legal_moves: np.ndarray, board_shape: tuple) -> None:
    """
    Print available moves in human-readable format.

    Parameters
    ----------
    legal_moves : np.ndarray
        Array of legal move indices (flattened or (row, col) pairs)
    board_shape : tuple
        Shape of the board (rows, cols)
    """
    if len(legal_moves) == 0:
        print("No legal moves available.")
        return

    # Check if moves are flattened indices or (row, col) pairs
    if legal_moves.ndim == 1:
        # Convert flattened indices to (row, col)
        rows, cols = board_shape
        moves_2d = [(idx // cols, idx % cols) for idx in legal_moves]
    else:
        moves_2d = legal_moves

    print("Available moves:")
    for i, (row, col) in enumerate(moves_2d, 1):
        print(f"  {i}. Row {row}, Col {col}")
