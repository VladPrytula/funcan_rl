"""
Position naming utilities for board games.

Provides consistent algebraic notation (chess-like) for board positions across
all games. This enables human-readable position names like "a1", "b2", "c3"
instead of raw indices (0, 1, 2, ...).

Theory Connection:
- Separates human interface from internal representation
- Enables consistent UI/UX across all games
- Facilitates debugging and testing with readable position names

References:
- Chess algebraic notation: https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
- Standard board game coordinate systems
"""

from typing import Tuple, Optional


def index_to_algebraic(index: int, board_size: int) -> str:
    """
    Convert flat board index to algebraic notation.

    Uses chess-like coordinate system:
    - Columns: a, b, c, ... (left to right)
    - Rows: 1, 2, 3, ... (top to bottom)

    Parameters
    ----------
    index : int
        Flattened board index (0-based, row-major order)
    board_size : int
        Size of the board (n×n)

    Returns
    -------
    str
        Position name in algebraic notation (e.g., "a1", "b2", "c3")

    Raises
    ------
    ValueError
        If index is out of range [0, board_size²-1]

    Notes
    -----
    Conversion formula:
    - row = index // board_size
    - col = index % board_size
    - column_letter = chr(ord('a') + col)
    - row_number = row + 1

    Board layout (3×3 example):
        a1  b1  c1
        a2  b2  c2
        a3  b3  c3

    Indices (3×3):
        0  1  2
        3  4  5
        6  7  8

    Examples
    --------
    >>> index_to_algebraic(0, 3)
    'a1'
    >>> index_to_algebraic(4, 3)
    'b2'
    >>> index_to_algebraic(8, 3)
    'c3'
    >>> index_to_algebraic(0, 4)
    'a1'
    >>> index_to_algebraic(15, 4)
    'd4'
    """
    if not (0 <= index < board_size * board_size):
        raise ValueError(
            f"Index {index} out of range for {board_size}×{board_size} board "
            f"(valid range: 0 to {board_size * board_size - 1})"
        )

    row = index // board_size
    col = index % board_size

    # Column letter (a, b, c, ...)
    col_letter = chr(ord('a') + col)

    # Row number (1, 2, 3, ... from top to bottom)
    row_number = row + 1

    return f'{col_letter}{row_number}'


def algebraic_to_index(name: str, board_size: int) -> int:
    """
    Convert algebraic notation to flat board index.

    Inverse of index_to_algebraic().

    Parameters
    ----------
    name : str
        Position name in algebraic notation (e.g., "a1", "b2", "c3")
        Format: <column_letter><row_number>
        Column letters: a-z (lowercase)
        Row numbers: 1-9 (or higher for larger boards)
    board_size : int
        Size of the board (n×n)

    Returns
    -------
    int
        Flattened board index (0-based, row-major order)

    Raises
    ------
    ValueError
        If name format is invalid or position is out of bounds

    Notes
    -----
    Conversion formula:
    - col = ord(name[0]) - ord('a')
    - row = int(name[1:]) - 1
    - index = row * board_size + col

    Examples
    --------
    >>> algebraic_to_index('a1', 3)
    0
    >>> algebraic_to_index('b2', 3)
    4
    >>> algebraic_to_index('c3', 3)
    8
    >>> algebraic_to_index('d4', 4)
    15
    """
    if not name or len(name) < 2:
        raise ValueError(
            f"Invalid position name '{name}'. Expected format: <column_letter><row_number> (e.g., 'a1', 'b2')"
        )

    col_letter = name[0].lower()
    row_str = name[1:]

    # Validate column letter
    if not ('a' <= col_letter <= 'z'):
        raise ValueError(
            f"Invalid column letter '{col_letter}' in position '{name}'. Must be a-z (lowercase)"
        )

    # Parse row number
    try:
        row_number = int(row_str)
    except ValueError:
        raise ValueError(
            f"Invalid row number '{row_str}' in position '{name}'. Must be a positive integer"
        )

    # Convert to 0-based indices
    col = ord(col_letter) - ord('a')
    row = row_number - 1

    # Validate bounds
    if not (0 <= col < board_size):
        raise ValueError(
            f"Column '{col_letter}' out of range for {board_size}×{board_size} board "
            f"(valid columns: a-{chr(ord('a') + board_size - 1)})"
        )

    if not (0 <= row < board_size):
        raise ValueError(
            f"Row {row_number} out of range for {board_size}×{board_size} board "
            f"(valid rows: 1-{board_size})"
        )

    # Convert to flat index
    index = row * board_size + col

    return index


def validate_position(name: str, board_size: int) -> bool:
    """
    Check if a position name is valid for the given board size.

    Parameters
    ----------
    name : str
        Position name in algebraic notation
    board_size : int
        Size of the board (n×n)

    Returns
    -------
    bool
        True if position is valid, False otherwise

    Examples
    --------
    >>> validate_position('a1', 3)
    True
    >>> validate_position('d1', 3)  # Column 'd' doesn't exist on 3×3 board
    False
    >>> validate_position('a4', 3)  # Row 4 doesn't exist on 3×3 board
    False
    >>> validate_position('invalid', 3)
    False
    """
    try:
        algebraic_to_index(name, board_size)
        return True
    except ValueError:
        return False


def tuple_to_index(position: Tuple[int, int], board_size: int) -> int:
    """
    Convert (row, col) tuple to flat board index.

    Parameters
    ----------
    position : Tuple[int, int]
        Board position as (row, col) with 0-based indexing
    board_size : int
        Size of the board (n×n)

    Returns
    -------
    int
        Flattened board index (0-based, row-major order)

    Raises
    ------
    ValueError
        If position is out of bounds

    Examples
    --------
    >>> tuple_to_index((0, 0), 3)
    0
    >>> tuple_to_index((1, 1), 3)
    4
    >>> tuple_to_index((2, 2), 3)
    8
    """
    row, col = position

    if not (0 <= row < board_size and 0 <= col < board_size):
        raise ValueError(
            f"Position ({row}, {col}) out of bounds for {board_size}×{board_size} board"
        )

    return row * board_size + col


def index_to_tuple(index: int, board_size: int) -> Tuple[int, int]:
    """
    Convert flat board index to (row, col) tuple.

    Parameters
    ----------
    index : int
        Flattened board index (0-based, row-major order)
    board_size : int
        Size of the board (n×n)

    Returns
    -------
    Tuple[int, int]
        Board position as (row, col) with 0-based indexing

    Raises
    ------
    ValueError
        If index is out of range

    Examples
    --------
    >>> index_to_tuple(0, 3)
    (0, 0)
    >>> index_to_tuple(4, 3)
    (1, 1)
    >>> index_to_tuple(8, 3)
    (2, 2)
    """
    if not (0 <= index < board_size * board_size):
        raise ValueError(
            f"Index {index} out of range for {board_size}×{board_size} board"
        )

    row = index // board_size
    col = index % board_size
    return (row, col)


def tuple_to_algebraic(position: Tuple[int, int], board_size: int) -> str:
    """
    Convert (row, col) tuple to algebraic notation.

    Convenience function combining tuple_to_index and index_to_algebraic.

    Parameters
    ----------
    position : Tuple[int, int]
        Board position as (row, col) with 0-based indexing
    board_size : int
        Size of the board (n×n)

    Returns
    -------
    str
        Position name in algebraic notation

    Examples
    --------
    >>> tuple_to_algebraic((0, 0), 3)
    'a1'
    >>> tuple_to_algebraic((1, 1), 3)
    'b2'
    >>> tuple_to_algebraic((2, 2), 3)
    'c3'
    """
    index = tuple_to_index(position, board_size)
    return index_to_algebraic(index, board_size)


def algebraic_to_tuple(name: str, board_size: int) -> Tuple[int, int]:
    """
    Convert algebraic notation to (row, col) tuple.

    Convenience function combining algebraic_to_index and index_to_tuple.

    Parameters
    ----------
    name : str
        Position name in algebraic notation
    board_size : int
        Size of the board (n×n)

    Returns
    -------
    Tuple[int, int]
        Board position as (row, col) with 0-based indexing

    Examples
    --------
    >>> algebraic_to_tuple('a1', 3)
    (0, 0)
    >>> algebraic_to_tuple('b2', 3)
    (1, 1)
    >>> algebraic_to_tuple('c3', 3)
    (2, 2)
    """
    index = algebraic_to_index(name, board_size)
    return index_to_tuple(index, board_size)


# Convenience aliases for common patterns
pos_to_name = index_to_algebraic
name_to_pos = algebraic_to_index
