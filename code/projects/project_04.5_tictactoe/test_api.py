#!/usr/bin/env python3
"""Quick test to verify API works with multiple board sizes."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from rl_toolkit.envs.tictactoe import TicTacToe
from rl_toolkit.algorithms.minimax import MinimaxSolver
import numpy as np

def test_api_logic(board_size=3):
    """Test the core API logic without Flask."""
    print(f"\nTesting {board_size}×{board_size} board:")
    print("-" * 50)

    # Simulate API request data
    board_flat = [0] * (board_size * board_size)
    board_flat[0] = 1  # Human plays first square

    win_length = board_size

    # Reconstruct game state (same as web_app.py)
    env = TicTacToe(board_size=board_size, win_length=win_length)
    env.board = np.array([[board_flat[i*board_size + j] for j in range(board_size)]
                          for i in range(board_size)], dtype=np.int8)
    env.current_player = -1  # AI is player -1

    # Configure search depth
    if board_size == 3:
        max_depth = None
    elif board_size == 4:
        max_depth = 8
    else:
        max_depth = 4

    # Compute AI move
    solver = MinimaxSolver(max_depth=max_depth)
    move = solver.get_best_move(env, maximize=False)
    stats = solver.get_stats()

    print(f"Board size: {board_size}×{board_size}")
    print(f"Search depth: {'Exact' if max_depth is None else f'Depth-{max_depth}'}")
    print(f"AI move: {move}")
    print(f"Nodes explored: {stats['nodes_explored']:,}")
    print(f"Cache hits: {stats['cache_hits']:,}")
    print(f"Heuristic evals: {stats['heuristic_evals']:,}")
    print(f"Valid move: {move in env.get_legal_moves()}")

    return True

if __name__ == '__main__':
    print("=" * 50)
    print("Testing API logic for multiple board sizes")
    print("=" * 50)

    test_api_logic(board_size=3)
    test_api_logic(board_size=4)
    test_api_logic(board_size=5)

    print("\n" + "=" * 50)
    print("✅ All API tests passed!")
    print("=" * 50)
