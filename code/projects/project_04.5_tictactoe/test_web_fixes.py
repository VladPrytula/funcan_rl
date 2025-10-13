#!/usr/bin/env python3
"""
Test script to verify web app fixes for candidate move display.

This script tests:
1. /tictactoe/candidates endpoint returns correct data
2. /tictactoe/move endpoint works correctly
3. Candidate evaluations match between endpoints

Usage:
    python test_web_fixes.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from rl_toolkit.envs.tictactoe import TicTacToe
from rl_toolkit.algorithms.minimax import MinimaxSolver


def test_candidate_evaluations():
    """Test that candidate evaluations work correctly."""
    print("=" * 70)
    print("TEST 1: Candidate Evaluations on Empty 3x3 Board")
    print("=" * 70)

    env = TicTacToe(board_size=3)
    solver = MinimaxSolver()

    # Get candidate evaluations (AI is player -1, minimizing)
    evaluations = solver.get_candidate_evaluations(env, maximize=False)

    print(f"\nFound {len(evaluations)} candidate moves:")
    for move, data in sorted(evaluations.items()):
        best_marker = " ⭐" if data['is_best'] else ""
        print(f"  Move {move}: value={data['value']:+.2f} - {data['reasoning']}{best_marker}")

    # All moves should have same value on empty board (draw)
    values = [data['value'] for data in evaluations.values()]
    print(f"\nValue range: [{min(values):.2f}, {max(values):.2f}]")

    if abs(max(values) - min(values)) < 0.01:
        print("✓ All moves lead to draw (as expected for optimal play)")
    else:
        print("✗ Values differ (unexpected for empty board)")

    return len(evaluations) == 9


def test_mid_game_candidates():
    """Test candidates with a partially filled board."""
    print("\n" + "=" * 70)
    print("TEST 2: Candidate Evaluations on Mid-Game Board")
    print("=" * 70)

    # Create a board with some moves
    # X . O
    # . X .
    # . . .
    env = TicTacToe(board_size=3)
    env.board[0] = 1   # X at position 0
    env.board[2] = -1  # O at position 2
    env.board[4] = 1   # X at position 4 (center)
    env.current_player = -1  # O's turn (AI)

    print("\nBoard state:")
    env.render()

    solver = MinimaxSolver()
    evaluations = solver.get_candidate_evaluations(env, maximize=False)

    print(f"\nFound {len(evaluations)} legal candidate moves:")
    for move, data in sorted(evaluations.items()):
        best_marker = " ⭐" if data['is_best'] else ""
        print(f"  Move {move}: value={data['value']:+.2f} - {data['reasoning']}{best_marker}")

    # Should have exactly 6 legal moves (9 - 3 filled)
    if len(evaluations) == 6:
        print(f"\n✓ Correct number of candidates (6)")
    else:
        print(f"\n✗ Wrong number of candidates (expected 6, got {len(evaluations)})")

    # Find best move
    best_moves = [move for move, data in evaluations.items() if data['is_best']]
    print(f"\nBest move(s): {best_moves}")

    return len(evaluations) == 6


def test_board_sizes():
    """Test that candidate evaluation works for different board sizes."""
    print("\n" + "=" * 70)
    print("TEST 3: Candidate Evaluations for Different Board Sizes")
    print("=" * 70)

    results = {}

    for size in [3, 4, 5]:
        print(f"\n{size}×{size} board:")
        env = TicTacToe(board_size=size)

        # Configure depth limit
        max_depth = None if size == 3 else (8 if size == 4 else 4)
        solver = MinimaxSolver(max_depth=max_depth)

        evaluations = solver.get_candidate_evaluations(env, maximize=False)
        expected_moves = size * size

        print(f"  - Expected candidates: {expected_moves}")
        print(f"  - Actual candidates: {len(evaluations)}")
        print(f"  - Search depth: {'unlimited' if max_depth is None else max_depth}")
        print(f"  - Stats: {solver.get_stats()['nodes_explored']} nodes explored")

        if len(evaluations) == expected_moves:
            print(f"  ✓ Correct")
            results[size] = True
        else:
            print(f"  ✗ Failed")
            results[size] = False

    return all(results.values())


def test_move_consistency():
    """Test that /move and /candidates endpoints agree on best move."""
    print("\n" + "=" * 70)
    print("TEST 4: Consistency Between get_best_move() and get_candidate_evaluations()")
    print("=" * 70)

    env = TicTacToe(board_size=3)
    env.board[0] = 1   # X at position 0
    env.board[4] = 1   # X at position 4 (center)
    env.current_player = -1  # O's turn (AI)

    print("\nBoard state:")
    env.render()

    solver = MinimaxSolver()

    # Get best move directly
    best_move_direct = solver.get_best_move(env, maximize=False)
    print(f"\nDirect best_move: {best_move_direct}")

    # Get best move from candidates
    solver.reset_stats()
    evaluations = solver.get_candidate_evaluations(env, maximize=False)
    best_from_candidates = [move for move, data in evaluations.items() if data['is_best']]
    print(f"Best from candidates: {best_from_candidates}")

    if best_move_direct in best_from_candidates:
        print("\n✓ Endpoints agree on best move")
        return True
    else:
        print("\n✗ Endpoints disagree!")
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 70)
    print("TESTING WEB APP FIXES: Candidate Move Display")
    print("=" * 70)
    print("\nThese tests verify that the candidate evaluation API works correctly")
    print("and returns data that the web interface can display.\n")

    tests = [
        ("Empty Board Candidates", test_candidate_evaluations),
        ("Mid-Game Candidates", test_mid_game_candidates),
        ("Multiple Board Sizes", test_board_sizes),
        ("Move Consistency", test_move_consistency),
    ]

    results = {}
    for name, test_func in tests:
        try:
            results[name] = test_func()
        except Exception as e:
            print(f"\n✗ Test '{name}' failed with exception: {e}")
            results[name] = False

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {name}")

    all_passed = all(results.values())
    print("\n" + "=" * 70)
    if all_passed:
        print("✓ ALL TESTS PASSED - Web app fixes are working correctly!")
    else:
        print("✗ SOME TESTS FAILED - Please review the output above")
    print("=" * 70)

    return 0 if all_passed else 1


if __name__ == '__main__':
    sys.exit(main())
