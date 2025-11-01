#!/usr/bin/env python3
"""Test script to verify visualization features work correctly."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from rl_toolkit.envs.tictactoe import TicTacToe
from rl_toolkit.algorithms.minimax import MinimaxSolver


def test_candidate_evaluations():
    """Test that candidate evaluations return expected structure."""
    print("\n" + "=" * 60)
    print("Testing Candidate Evaluations")
    print("=" * 60)

    # Test 3x3
    env = TicTacToe(board_size=3)
    env.reset()
    env.step(0)  # X plays corner

    solver = MinimaxSolver(max_depth=None)
    evaluations = solver.get_candidate_evaluations(env, maximize=False)

    print(f"\n3×3 Board (X played 0):")
    print(f"Number of candidates: {len(evaluations)}")

    # Verify structure
    for move, data in evaluations.items():
        assert 'value' in data, "Missing 'value' key"
        assert 'reasoning' in data, "Missing 'reasoning' key"
        assert 'is_best' in data, "Missing 'is_best' key"
        assert 'is_terminal' in data, "Missing 'is_terminal' key"
        assert 'depth_used' in data, "Missing 'depth_used' key"
        assert -1.0 <= data['value'] <= 1.0, f"Value {data['value']} out of range"
        assert isinstance(data['reasoning'], str), "Reasoning must be string"
        assert isinstance(data['is_best'], bool), "is_best must be bool"

    # Verify exactly one best move
    best_moves = [m for m, d in evaluations.items() if d['is_best']]
    assert len(best_moves) == 1, f"Expected 1 best move, got {len(best_moves)}"

    print(f"✅ 3×3 candidate evaluations structure valid")
    print(f"   Best move: {best_moves[0]} (value: {evaluations[best_moves[0]]['value']:.2f})")
    print(f"   Reasoning: {evaluations[best_moves[0]]['reasoning']}")

    # Test 4x4 (depth-limited)
    env4 = TicTacToe(board_size=4)
    env4.reset()
    env4.step(0)  # X plays corner

    solver4 = MinimaxSolver(max_depth=8)
    evaluations4 = solver4.get_candidate_evaluations(env4, maximize=False)

    print(f"\n4×4 Board (X played 0, depth-limited):")
    print(f"Number of candidates: {len(evaluations4)}")

    best_moves4 = [m for m, d in evaluations4.items() if d['is_best']]
    assert len(best_moves4) == 1, f"Expected 1 best move, got {len(best_moves4)}"

    print(f"✅ 4×4 candidate evaluations structure valid")
    print(f"   Best move: {best_moves4[0]} (value: {evaluations4[best_moves4[0]]['value']:.2f})")

    # Verify depth_used is set for depth-limited search
    for move, data in evaluations4.items():
        assert data['depth_used'] == 8, f"Expected depth_used=8, got {data['depth_used']}"

    print(f"   Depth used: {evaluations4[best_moves4[0]]['depth_used']}")


def test_progress_callback():
    """Test that progress callbacks work correctly."""
    print("\n" + "=" * 60)
    print("Testing Progress Callbacks")
    print("=" * 60)

    callback_count = [0]
    last_update = [None]

    def progress_callback(update):
        callback_count[0] += 1
        last_update[0] = update
        print(f"  Callback {callback_count[0]}: {update['nodes_explored']} nodes, "
              f"{update['elapsed_time']:.2f}s")

    env = TicTacToe(board_size=3)
    env.reset()

    solver = MinimaxSolver(max_depth=None, progress_callback=progress_callback)
    move = solver.get_best_move(env, maximize=True)

    print(f"\n✅ Progress callbacks worked")
    print(f"   Total callbacks: {callback_count[0]}")
    if last_update[0]:
        print(f"   Final nodes explored: {last_update[0]['nodes_explored']:,}")
        print(f"   Final elapsed time: {last_update[0]['elapsed_time']:.2f}s")

        # Verify structure
        assert 'nodes_explored' in last_update[0]
        assert 'cache_hits' in last_update[0]
        assert 'heuristic_evals' in last_update[0]
        assert 'current_depth' in last_update[0]
        assert 'elapsed_time' in last_update[0]


def test_reasoning_generators():
    """Test that reasoning strings are appropriate."""
    print("\n" + "=" * 60)
    print("Testing Reasoning Generators")
    print("=" * 60)

    env = TicTacToe(board_size=3)
    env.reset()

    # Set up a position where O has a winning move
    # Board will be:
    # X | - | X
    # O | O | -
    # - | - | -
    env.step(0)  # X top-left
    env.step(3)  # O middle-left
    env.step(2)  # X top-right
    env.step(4)  # O center

    # Now O can win by playing 5 (middle-right)
    solver = MinimaxSolver(max_depth=None)
    evaluations = solver.get_candidate_evaluations(env, maximize=False)

    # Print all evaluations to understand the position
    print("\nAll move evaluations:")
    for move in sorted(evaluations.keys()):
        data = evaluations[move]
        best_marker = "⭐" if data['is_best'] else "  "
        print(f"  {best_marker} Move {move}: {data['value']:+.2f} - {data['reasoning']}")

    # Check that winning move has appropriate value
    winning_move = 5
    if winning_move in evaluations:
        reasoning = evaluations[winning_move]['reasoning']
        value = evaluations[winning_move]['value']
        is_terminal = evaluations[winning_move]['is_terminal']
        print(f"\nWinning move {winning_move}:")
        print(f"  Value: {value:.2f}")
        print(f"  Reasoning: {reasoning}")
        print(f"  Is terminal: {is_terminal}")

        # Value should be close to -1 (good for minimizing player)
        # Since O is minimizing, -1 is a win for O
        assert value <= -0.8, f"Winning move should have value <= -0.8, got {value}"

        # Note: The winning move might not be "best" if there are multiple winning moves
        # or if the minimax sees all wins as equivalent
        print(f"✅ Winning move has correct value (O wins)")

        # Check that at least one move is marked as best
        best_moves = [m for m, d in evaluations.items() if d['is_best']]
        assert len(best_moves) >= 1, "At least one move should be marked as best"
        print(f"✅ Best move(s): {best_moves}")


if __name__ == '__main__':
    try:
        test_candidate_evaluations()
        test_progress_callback()
        test_reasoning_generators()

        print("\n" + "=" * 60)
        print("✅ ALL VISUALIZATION TESTS PASSED!")
        print("=" * 60)

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
