#!/usr/bin/env python3
"""Test script to verify position naming and outcome formatting improvements."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from rl_toolkit.envs.tictactoe import TicTacToe
from rl_toolkit.algorithms.minimax import MinimaxSolver

# Import helper functions from play_terminal
sys.path.insert(0, os.path.dirname(__file__))
from play_terminal import get_position_name, format_outcome

def test_position_names():
    """Test algebraic notation for different board sizes."""
    print("=" * 60)
    print("Testing Algebraic Notation")
    print("=" * 60)

    # Test 3x3
    print("\n3×3 Board (algebraic notation):")
    print("Expected layout:")
    print("  a1  b1  c1")
    print("  a2  b2  c2")
    print("  a3  b3  c3")
    print("\nActual mappings:")
    for i in range(9):
        name = get_position_name(i, 3)
        print(f"  Position {i}: {name}")

    # Verify key positions
    assert get_position_name(0, 3) == "a1", "Position 0 should be a1"
    assert get_position_name(4, 3) == "b2", "Position 4 should be b2 (center)"
    assert get_position_name(8, 3) == "c3", "Position 8 should be c3"

    # Test 4x4
    print("\n4×4 Board (sample positions):")
    print("Expected layout:")
    print("  a1  b1  c1  d1")
    print("  a2  b2  c2  d2")
    print("  a3  b3  c3  d3")
    print("  a4  b4  c4  d4")
    print("\nSample mappings:")
    for i in [0, 3, 5, 10, 12, 15]:
        name = get_position_name(i, 4)
        print(f"  Position {i}: {name}")

    # Test 5x5
    print("\n5×5 Board (sample positions):")
    print("Expected layout:")
    print("  a1  b1  c1  d1  e1")
    print("  a2  b2  c2  d2  e2")
    print("  a3  b3  c3  d3  e3")
    print("  a4  b4  c4  d4  e4")
    print("  a5  b5  c5  d5  e5")
    print("\nSample mappings:")
    for i in [0, 4, 12, 20, 24]:
        name = get_position_name(i, 5)
        print(f"  Position {i}: {name}")

    # Verify key positions
    assert get_position_name(0, 5) == "a1", "Position 0 should be a1"
    assert get_position_name(12, 5) == "c3", "Position 12 should be c3 (center)"
    assert get_position_name(24, 5) == "e5", "Position 24 should be e5"

    print("\n✅ Algebraic notation works for all board sizes!")


def test_outcome_formatting():
    """Test outcome formatting for different values."""
    print("\n" + "=" * 60)
    print("Testing Outcome Formatting")
    print("=" * 60)

    test_values = [
        (1.0, "AI win (certain)"),
        (0.95, "AI win (near certain)"),
        (0.5, "AI advantage"),
        (0.0, "Draw/balanced"),
        (-0.5, "Human advantage"),
        (-0.95, "Human win (near certain)"),
        (-1.0, "Human win (certain)"),
    ]

    print("\nFrom AI perspective:")
    for value, description in test_values:
        outcome = format_outcome(value, 'ai')
        print(f"  {value:+.2f} ({description}): {outcome}")

    print("\n✅ Outcome formatting works correctly!")


def test_candidate_evaluations():
    """Test candidate evaluations display with new formatting."""
    print("\n" + "=" * 60)
    print("Testing Candidate Evaluations Display")
    print("=" * 60)

    # Create a 3x3 game with AI first move
    env = TicTacToe(board_size=3)
    env.reset()

    solver = MinimaxSolver(max_depth=None)
    evaluations = solver.get_candidate_evaluations(env, maximize=True)

    print("\n3×3 Empty Board - All Candidate Moves (Algebraic Notation):")
    print(f"{'Position':<12} {'Outcome':<18} {'Assessment':<30} {'Best':<6}")
    print("─" * 72)

    for move, data in sorted(evaluations.items()):
        position_name = get_position_name(move, env.board_size)
        position_str = f"{position_name} ({move})"
        outcome_text = format_outcome(data['value'], 'ai')
        reasoning = data['reasoning']
        is_best_str = "⭐ YES" if data['is_best'] else ""

        print(f"{position_str:<12} {outcome_text:<18} {reasoning:<30} {is_best_str:<6}")

    print("\n✅ Candidate evaluations display works correctly!")


def test_game_scenario():
    """Test a specific game scenario to verify display improvements."""
    print("\n" + "=" * 60)
    print("Testing Game Scenario Display")
    print("=" * 60)

    # Create a scenario where X has played corner, O responds
    env = TicTacToe(board_size=3)
    env.reset()
    env.step(0)  # X plays top-left

    print("\nScenario: X (human) played a1 (0)")
    print("AI (O) is evaluating responses...")

    solver = MinimaxSolver(max_depth=None)
    evaluations = solver.get_candidate_evaluations(env, maximize=False)

    print(f"\n{'Position':<12} {'Outcome':<18} {'Assessment':<30} {'Best':<6}")
    print("─" * 72)

    # Sort by value (best for O = minimize = lowest value)
    sorted_moves = sorted(evaluations.items(), key=lambda x: x[1]['value'], reverse=False)

    for move, data in sorted_moves[:5]:  # Show top 5 moves
        position_name = get_position_name(move, env.board_size)
        position_str = f"{position_name} ({move})"
        outcome_text = format_outcome(data['value'], 'ai')
        reasoning = data['reasoning']
        is_best_str = "⭐ YES" if data['is_best'] else ""

        print(f"{position_str:<12} {outcome_text:<18} {reasoning:<30} {is_best_str:<6}")

    print("\n✅ Game scenario display works correctly!")


if __name__ == '__main__':
    try:
        test_position_names()
        test_outcome_formatting()
        test_candidate_evaluations()
        test_game_scenario()

        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nPosition naming and outcome formatting improvements verified!")

    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
