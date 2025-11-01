"""
Board visualization utilities for grid-based games.

Provides ASCII rendering for n×n board games (Tic-Tac-Toe, Connect Four, Gomoku, Reversi).
Reusable across all game projects.

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
          a   b   c
        +---+---+---+
      1 | X |   | O |
        +---+---+---+
      2 |   | X |   |
        +---+---+---+
      3 | O |   | X |
        +---+---+---+
    """
    if symbols is None:
        symbols = {0: ' ', 1: 'X', -1: 'O'}

    rows, cols = board.shape

    # Build the output string
    lines = []

    # Column indices (if requested) - use algebraic notation (a, b, c...)
    if show_indices:
        col_header = "  " + "   ".join(chr(ord('a') + i) for i in range(cols))
        lines.append(col_header)

    # Top border
    border = "  " + "+---" * cols + "+"
    lines.append(border)

    # Board rows
    for i in range(rows):
        # Row with symbols
        row_str = ""
        if show_indices:
            row_str += f"{i + 1} "  # 1-indexed row numbers (algebraic notation)

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


def get_position_name(index: int, board_size: int) -> str:
    """
    Convert flattened board index to algebraic notation (for square boards).

    Algebraic notation: column letter (a-z) + row number (1-based).
    Examples: a1, b2, c3 for 3×3 board; a1-d4 for 4×4 board.

    Parameters
    ----------
    index : int
        Flattened board index (row-major order)
    board_size : int
        Size of the square board (n×n)

    Returns
    -------
    str
        Algebraic notation position name

    Examples
    --------
    >>> get_position_name(0, 3)  # Top-left of 3×3
    'a1'
    >>> get_position_name(4, 3)  # Center of 3×3
    'b2'
    >>> get_position_name(8, 3)  # Bottom-right of 3×3
    'c3'
    """
    row = index // board_size
    col = index % board_size
    col_letter = chr(ord('a') + col)
    row_number = row + 1
    return f'{col_letter}{row_number}'


def get_position_name_rect(index: int, rows: int, cols: int) -> str:
    """
    Convert flattened board index to algebraic notation (for rectangular boards).

    Extension of get_position_name for boards where rows ≠ cols.
    Algebraic notation: column letter (a-z) + row number (1-based).

    Parameters
    ----------
    index : int
        Flattened board index (row-major order)
    rows : int
        Number of rows
    cols : int
        Number of columns

    Returns
    -------
    str
        Algebraic notation position name

    Examples
    --------
    >>> get_position_name_rect(0, 6, 7)  # Bottom-left of Connect Four (6×7)
    'a1'
    >>> get_position_name_rect(41, 6, 7)  # Top-right of Connect Four
    'g6'
    >>> get_position_name_rect(20, 6, 7)  # Middle of Connect Four
    'd3'
    """
    row = index // cols
    col = index % cols
    col_letter = chr(ord('a') + col)
    row_number = row + 1
    return f'{col_letter}{row_number}'


def parse_position_name(position: str, board_size: int) -> int:
    """
    Convert algebraic notation to flattened board index (for square boards).

    Inverse of get_position_name.

    Parameters
    ----------
    position : str
        Algebraic notation position (e.g., 'a1', 'b2')
    board_size : int
        Size of the square board (n×n)

    Returns
    -------
    int
        Flattened board index

    Raises
    ------
    ValueError
        If position format is invalid

    Examples
    --------
    >>> parse_position_name('a1', 3)
    0
    >>> parse_position_name('b2', 3)
    4
    >>> parse_position_name('c3', 3)
    8
    """
    if len(position) < 2:
        raise ValueError(f"Invalid position format: {position}")

    col_letter = position[0].lower()
    row_str = position[1:]

    if not ('a' <= col_letter <= 'z'):
        raise ValueError(f"Invalid column letter: {col_letter}")

    try:
        row_number = int(row_str)
    except ValueError:
        raise ValueError(f"Invalid row number: {row_str}")

    col = ord(col_letter) - ord('a')
    row = row_number - 1

    if row < 0 or row >= board_size or col < 0 or col >= board_size:
        raise ValueError(f"Position {position} out of bounds for {board_size}×{board_size} board")

    return row * board_size + col


def parse_position_name_rect(position: str, rows: int, cols: int) -> int:
    """
    Convert algebraic notation to flattened board index (for rectangular boards).

    Inverse of get_position_name_rect.

    Parameters
    ----------
    position : str
        Algebraic notation position (e.g., 'a1', 'g6')
    rows : int
        Number of rows
    cols : int
        Number of columns

    Returns
    -------
    int
        Flattened board index

    Raises
    ------
    ValueError
        If position format is invalid

    Examples
    --------
    >>> parse_position_name_rect('a1', 6, 7)
    0
    >>> parse_position_name_rect('d3', 6, 7)
    20
    >>> parse_position_name_rect('g6', 6, 7)
    41
    """
    if len(position) < 2:
        raise ValueError(f"Invalid position format: {position}")

    col_letter = position[0].lower()
    row_str = position[1:]

    if not ('a' <= col_letter <= 'z'):
        raise ValueError(f"Invalid column letter: {col_letter}")

    try:
        row_number = int(row_str)
    except ValueError:
        raise ValueError(f"Invalid row number: {row_str}")

    col = ord(col_letter) - ord('a')
    row = row_number - 1

    if row < 0 or row >= rows or col < 0 or col >= cols:
        raise ValueError(f"Position {position} out of bounds for {rows}×{cols} board")

    return row * cols + col


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
