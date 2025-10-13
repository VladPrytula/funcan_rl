"""
Unit tests for position naming utilities.

Tests cover:
- Algebraic notation conversion (index ↔ algebraic)
- Tuple conversion (index ↔ tuple, tuple ↔ algebraic)
- Validation functions
- Error handling for invalid inputs
- Multiple board sizes (3×3, 4×4, 5×5)
- Edge cases (bounds checking, format validation)

Theory Connection (Week 24):
Position utilities separate human interface from internal representation,
enabling consistent UI/UX across all game implementations.
"""

import pytest
import sys
import os

# Add rl_toolkit to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rl_toolkit.utils.position_utils import (
    index_to_algebraic,
    algebraic_to_index,
    validate_position,
    tuple_to_index,
    index_to_tuple,
    tuple_to_algebraic,
    algebraic_to_tuple,
    pos_to_name,  # Alias
    name_to_pos   # Alias
)


class TestIndexToAlgebraic:
    """Test conversion from flat index to algebraic notation."""

    def test_3x3_top_left(self):
        """Test top-left corner (index 0 → a1)."""
        assert index_to_algebraic(0, 3) == "a1"

    def test_3x3_center(self):
        """Test center position (index 4 → b2)."""
        assert index_to_algebraic(4, 3) == "b2"

    def test_3x3_bottom_right(self):
        """Test bottom-right corner (index 8 → c3)."""
        assert index_to_algebraic(8, 3) == "c3"

    def test_3x3_all_positions(self):
        """Test all positions on 3×3 board."""
        expected = [
            "a1", "b1", "c1",  # Row 1
            "a2", "b2", "c2",  # Row 2
            "a3", "b3", "c3"   # Row 3
        ]
        for i, exp in enumerate(expected):
            assert index_to_algebraic(i, 3) == exp

    def test_4x4_corners(self):
        """Test corners on 4×4 board."""
        assert index_to_algebraic(0, 4) == "a1"   # Top-left
        assert index_to_algebraic(3, 4) == "d1"   # Top-right
        assert index_to_algebraic(12, 4) == "a4"  # Bottom-left
        assert index_to_algebraic(15, 4) == "d4"  # Bottom-right

    def test_4x4_center(self):
        """Test center positions on 4×4 board."""
        assert index_to_algebraic(5, 4) == "b2"
        assert index_to_algebraic(10, 4) == "c3"

    def test_5x5_corners(self):
        """Test corners on 5×5 board."""
        assert index_to_algebraic(0, 5) == "a1"   # Top-left
        assert index_to_algebraic(4, 5) == "e1"   # Top-right
        assert index_to_algebraic(20, 5) == "a5"  # Bottom-left
        assert index_to_algebraic(24, 5) == "e5"  # Bottom-right

    def test_5x5_center(self):
        """Test center position on 5×5 board (index 12 → c3)."""
        assert index_to_algebraic(12, 5) == "c3"

    def test_out_of_bounds_raises(self):
        """Test that out-of-bounds index raises ValueError."""
        with pytest.raises(ValueError, match="out of range"):
            index_to_algebraic(9, 3)  # 3×3 has indices 0-8

        with pytest.raises(ValueError, match="out of range"):
            index_to_algebraic(-1, 3)  # Negative index

        with pytest.raises(ValueError, match="out of range"):
            index_to_algebraic(16, 4)  # 4×4 has indices 0-15


class TestAlgebraicToIndex:
    """Test conversion from algebraic notation to flat index."""

    def test_3x3_valid_positions(self):
        """Test valid positions on 3×3 board."""
        assert algebraic_to_index("a1", 3) == 0
        assert algebraic_to_index("b2", 3) == 4
        assert algebraic_to_index("c3", 3) == 8

    def test_3x3_all_positions(self):
        """Test all positions on 3×3 board."""
        positions = [
            ("a1", 0), ("b1", 1), ("c1", 2),
            ("a2", 3), ("b2", 4), ("c2", 5),
            ("a3", 6), ("b3", 7), ("c3", 8)
        ]
        for name, expected_idx in positions:
            assert algebraic_to_index(name, 3) == expected_idx

    def test_4x4_valid_positions(self):
        """Test valid positions on 4×4 board."""
        assert algebraic_to_index("a1", 4) == 0
        assert algebraic_to_index("d1", 4) == 3
        assert algebraic_to_index("b2", 4) == 5
        assert algebraic_to_index("d4", 4) == 15

    def test_5x5_valid_positions(self):
        """Test valid positions on 5×5 board."""
        assert algebraic_to_index("a1", 5) == 0
        assert algebraic_to_index("c3", 5) == 12  # Center
        assert algebraic_to_index("e5", 5) == 24

    def test_case_insensitive(self):
        """Test that column letters are case-insensitive."""
        assert algebraic_to_index("A1", 3) == 0
        assert algebraic_to_index("B2", 3) == 4
        assert algebraic_to_index("C3", 3) == 8

    def test_invalid_format_empty_string(self):
        """Test that empty string raises ValueError."""
        with pytest.raises(ValueError, match="Invalid position name"):
            algebraic_to_index("", 3)

    def test_invalid_format_too_short(self):
        """Test that single character raises ValueError."""
        with pytest.raises(ValueError, match="Invalid position name"):
            algebraic_to_index("a", 3)

    def test_invalid_column_letter(self):
        """Test that invalid column letter raises ValueError."""
        with pytest.raises(ValueError, match="Invalid column letter"):
            algebraic_to_index("@1", 3)  # @ is before 'a'

        with pytest.raises(ValueError, match="Invalid column letter"):
            algebraic_to_index("11", 3)  # Number instead of letter

    def test_invalid_row_number(self):
        """Test that invalid row number raises ValueError."""
        with pytest.raises(ValueError, match="Invalid row number"):
            algebraic_to_index("ax", 3)  # Letter instead of number

        # Negative numbers parse successfully but fail bounds check
        with pytest.raises(ValueError, match="out of range"):
            algebraic_to_index("a-1", 3)  # Negative row number (out of bounds)

    def test_out_of_bounds_column(self):
        """Test that column beyond board size raises ValueError."""
        with pytest.raises(ValueError, match="out of range"):
            algebraic_to_index("d1", 3)  # 3×3 only has columns a-c

        with pytest.raises(ValueError, match="out of range"):
            algebraic_to_index("f1", 5)  # 5×5 only has columns a-e

    def test_out_of_bounds_row(self):
        """Test that row beyond board size raises ValueError."""
        with pytest.raises(ValueError, match="out of range"):
            algebraic_to_index("a4", 3)  # 3×3 only has rows 1-3

        with pytest.raises(ValueError, match="out of range"):
            algebraic_to_index("a0", 3)  # Row 0 doesn't exist


class TestValidatePosition:
    """Test position validation function."""

    def test_valid_positions_return_true(self):
        """Test that valid positions return True."""
        assert validate_position("a1", 3) is True
        assert validate_position("b2", 3) is True
        assert validate_position("c3", 3) is True
        assert validate_position("d4", 4) is True

    def test_invalid_positions_return_false(self):
        """Test that invalid positions return False."""
        assert validate_position("d1", 3) is False  # Column out of bounds
        assert validate_position("a4", 3) is False  # Row out of bounds
        assert validate_position("invalid", 3) is False  # Invalid format
        assert validate_position("", 3) is False  # Empty string

    def test_edge_cases(self):
        """Test edge cases for validation."""
        assert validate_position("a0", 3) is False  # Row 0 doesn't exist
        assert validate_position("@1", 3) is False  # Invalid column
        assert validate_position("11", 3) is False  # No column letter


class TestTupleToIndex:
    """Test conversion from (row, col) tuple to flat index."""

    def test_3x3_positions(self):
        """Test tuple conversion on 3×3 board."""
        assert tuple_to_index((0, 0), 3) == 0  # Top-left
        assert tuple_to_index((1, 1), 3) == 4  # Center
        assert tuple_to_index((2, 2), 3) == 8  # Bottom-right

    def test_4x4_positions(self):
        """Test tuple conversion on 4×4 board."""
        assert tuple_to_index((0, 0), 4) == 0   # Top-left
        assert tuple_to_index((1, 2), 4) == 6   # Row 1, Col 2
        assert tuple_to_index((3, 3), 4) == 15  # Bottom-right

    def test_out_of_bounds_raises(self):
        """Test that out-of-bounds tuple raises ValueError."""
        with pytest.raises(ValueError, match="out of bounds"):
            tuple_to_index((3, 0), 3)  # Row 3 doesn't exist on 3×3

        with pytest.raises(ValueError, match="out of bounds"):
            tuple_to_index((0, 3), 3)  # Col 3 doesn't exist on 3×3

        with pytest.raises(ValueError, match="out of bounds"):
            tuple_to_index((-1, 0), 3)  # Negative row


class TestIndexToTuple:
    """Test conversion from flat index to (row, col) tuple."""

    def test_3x3_positions(self):
        """Test index to tuple on 3×3 board."""
        assert index_to_tuple(0, 3) == (0, 0)  # Top-left
        assert index_to_tuple(4, 3) == (1, 1)  # Center
        assert index_to_tuple(8, 3) == (2, 2)  # Bottom-right

    def test_4x4_positions(self):
        """Test index to tuple on 4×4 board."""
        assert index_to_tuple(0, 4) == (0, 0)   # Top-left
        assert index_to_tuple(6, 4) == (1, 2)   # Row 1, Col 2
        assert index_to_tuple(15, 4) == (3, 3)  # Bottom-right

    def test_out_of_bounds_raises(self):
        """Test that out-of-bounds index raises ValueError."""
        with pytest.raises(ValueError, match="out of range"):
            index_to_tuple(9, 3)  # 3×3 has indices 0-8

        with pytest.raises(ValueError, match="out of range"):
            index_to_tuple(-1, 3)  # Negative index


class TestRoundTripConversions:
    """Test that conversions are invertible (round-trip correctness)."""

    def test_index_algebraic_roundtrip(self):
        """Test index → algebraic → index round-trip."""
        for board_size in [3, 4, 5]:
            for index in range(board_size * board_size):
                algebraic = index_to_algebraic(index, board_size)
                result = algebraic_to_index(algebraic, board_size)
                assert result == index, f"Round-trip failed: {index} → {algebraic} → {result}"

    def test_tuple_index_roundtrip(self):
        """Test tuple → index → tuple round-trip."""
        for board_size in [3, 4, 5]:
            for row in range(board_size):
                for col in range(board_size):
                    index = tuple_to_index((row, col), board_size)
                    result = index_to_tuple(index, board_size)
                    assert result == (row, col), f"Round-trip failed: ({row},{col}) → {index} → {result}"

    def test_tuple_algebraic_roundtrip(self):
        """Test tuple → algebraic → tuple round-trip."""
        for board_size in [3, 4, 5]:
            for row in range(board_size):
                for col in range(board_size):
                    algebraic = tuple_to_algebraic((row, col), board_size)
                    result = algebraic_to_tuple(algebraic, board_size)
                    assert result == (row, col), f"Round-trip failed: ({row},{col}) → {algebraic} → {result}"


class TestConvenienceFunctions:
    """Test convenience wrapper functions."""

    def test_tuple_to_algebraic(self):
        """Test tuple to algebraic conversion."""
        assert tuple_to_algebraic((0, 0), 3) == "a1"
        assert tuple_to_algebraic((1, 1), 3) == "b2"
        assert tuple_to_algebraic((2, 2), 3) == "c3"

    def test_algebraic_to_tuple(self):
        """Test algebraic to tuple conversion."""
        assert algebraic_to_tuple("a1", 3) == (0, 0)
        assert algebraic_to_tuple("b2", 3) == (1, 1)
        assert algebraic_to_tuple("c3", 3) == (2, 2)

    def test_aliases(self):
        """Test that aliases work correctly."""
        # pos_to_name is alias for index_to_algebraic
        assert pos_to_name(4, 3) == "b2"
        assert pos_to_name(4, 3) == index_to_algebraic(4, 3)

        # name_to_pos is alias for algebraic_to_index
        assert name_to_pos("b2", 3) == 4
        assert name_to_pos("b2", 3) == algebraic_to_index("b2", 3)


class TestLargerBoards:
    """Test position utilities work correctly on larger boards."""

    def test_8x8_chess_board(self):
        """Test 8×8 board (chess-sized)."""
        # Corners
        assert index_to_algebraic(0, 8) == "a1"
        assert index_to_algebraic(7, 8) == "h1"
        assert index_to_algebraic(56, 8) == "a8"
        assert index_to_algebraic(63, 8) == "h8"

        # Center
        assert index_to_algebraic(27, 8) == "d4"
        assert index_to_algebraic(28, 8) == "e4"

        # Verify round-trip
        assert algebraic_to_index("d4", 8) == 27
        assert algebraic_to_index("e4", 8) == 28

    def test_10x10_board(self):
        """Test 10×10 board (larger than typical games)."""
        # Corners
        assert index_to_algebraic(0, 10) == "a1"
        assert index_to_algebraic(9, 10) == "j1"
        assert index_to_algebraic(90, 10) == "a10"
        assert index_to_algebraic(99, 10) == "j10"

        # Verify round-trip
        assert algebraic_to_index("j10", 10) == 99


# Run tests
if __name__ == '__main__':
    pytest.main([__file__, '-v'])
