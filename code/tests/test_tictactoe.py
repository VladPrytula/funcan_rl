"""
Unit tests for Tic-Tac-Toe game engine and minimax algorithm.

Tests cover:
- Game mechanics (moves, win detection, state transitions)
- Minimax correctness (optimal play never loses)
- Edge cases (full board, invalid moves)

"""

import pytest
import numpy as np
import sys
import os

# Add rl_toolkit to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rl_toolkit.envs.tictactoe import TicTacToe
from rl_toolkit.algorithms.minimax import MinimaxSolver, get_optimal_move


class TestTicTacToeBasics:
    """Test basic game mechanics."""

    def test_initialization(self):
        """Test environment initializes correctly."""
        env = TicTacToe()
        assert env.board.shape == (3, 3)
        assert np.all(env.board == 0)
        assert env.current_player == 1
        assert not env.done
        assert env.winner is None

    def test_reset(self):
        """Test reset returns to initial state."""
        env = TicTacToe()
        env.step(0)
        env.step(1)
        env.reset()
        assert np.all(env.board == 0)
        assert env.current_player == 1
        assert not env.done

    def test_legal_moves_initial(self):
        """Test all moves are legal initially."""
        env = TicTacToe()
        legal = env.get_legal_moves()
        assert len(legal) == 9
        assert np.array_equal(legal, np.arange(9))

    def test_legal_moves_after_move(self):
        """Test legal moves update after a move."""
        env = TicTacToe()
        env.step(4)  # Center
        legal = env.get_legal_moves()
        assert len(legal) == 8
        assert 4 not in legal

    def test_step_basic(self):
        """Test step updates board correctly."""
        env = TicTacToe()
        state, reward, done, info = env.step(4)
        assert state[1, 1] == 1  # Player 1 (X) placed
        assert not done
        assert reward == 0.0

    def test_step_player_switch(self):
        """Test players alternate correctly."""
        env = TicTacToe()
        env.step(0)
        assert env.current_player == -1  # Player 2's turn
        env.step(1)
        assert env.current_player == 1  # Player 1's turn

    def test_invalid_move(self):
        """Test that invalid moves raise errors."""
        env = TicTacToe()
        env.step(4)
        with pytest.raises(ValueError, match="already occupied"):
            env.step(4)  # Same square


class TestWinDetection:
    """Test win condition detection."""

    def test_win_row_0(self):
        """Test win detection for top row."""
        env = TicTacToe()
        env.step(0); env.step(3)
        env.step(1); env.step(4)
        env.step(2)  # Player 1 wins (row 0)
        assert env.done
        assert env.winner == 1
        assert env.check_win(1)

    def test_win_column_1(self):
        """Test win detection for middle column."""
        env = TicTacToe()
        env.step(1); env.step(0)
        env.step(4); env.step(2)
        env.step(7)  # Player 1 wins (col 1)
        assert env.done
        assert env.winner == 1

    def test_win_main_diagonal(self):
        """Test win detection for main diagonal."""
        env = TicTacToe()
        env.step(0); env.step(1)
        env.step(4); env.step(2)
        env.step(8)  # Player 1 wins (diagonal)
        assert env.done
        assert env.winner == 1

    def test_win_anti_diagonal(self):
        """Test win detection for anti-diagonal."""
        env = TicTacToe()
        env.step(2); env.step(0)
        env.step(4); env.step(1)
        env.step(6)  # Player 1 wins (anti-diagonal)
        assert env.done
        assert env.winner == 1

    def test_draw(self):
        """Test draw detection (no winner, no moves)."""
        env = TicTacToe()
        # Force a draw position
        # X plays: 0, 1, 5, 6, 7
        # O plays: 2, 3, 4, 8
        # Result: draw
        moves = [0, 2, 1, 3, 5, 4, 6, 8, 7]  # Known draw sequence
        for move in moves:
            env.step(move)
        assert env.done
        assert env.winner is None  # Draw


class TestMinimaxOptimality:
    """Test that minimax produces optimal play."""

    def test_minimax_first_move(self):
        """Test minimax returns a valid move."""
        env = TicTacToe()
        solver = MinimaxSolver()
        move = solver.get_best_move(env, maximize=True)
        assert move in env.get_legal_moves()
        assert 0 <= move <= 8

    def test_minimax_blocks_immediate_loss(self):
        """Test AI blocks opponent's winning move."""
        env = TicTacToe()
        # Player 1 (X) has two in a row
        env.step(0); env.step(3)
        env.step(1)  # X has 0 and 1 (needs 2 to win)

        # AI (Player 2, O) should block at position 2
        solver = MinimaxSolver()
        move = solver.get_best_move(env, maximize=False)
        assert move == 2  # Must block

    def test_minimax_takes_winning_move(self):
        """Test AI takes winning move when available."""
        env = TicTacToe()
        # Set up board where AI (Player 2) can win
        env.board = np.array([
            [-1, -1,  0],  # O O _
            [ 1,  1,  0],  # X X _
            [ 0,  0,  0]   # _ _ _
        ])
        env.current_player = -1  # AI's turn

        solver = MinimaxSolver()
        move = solver.get_best_move(env, maximize=False)
        assert move == 2  # Winning move

    def test_minimax_never_loses(self):
        """Test that two minimax agents always draw."""
        env = TicTacToe()
        solver = MinimaxSolver()

        while not env.is_terminal():
            maximize = (env.current_player == 1)
            move = solver.get_best_move(env, maximize=maximize)
            env.step(move)

        # Game should be a draw (optimal play on both sides)
        assert env.winner is None  # Draw
        assert env.done

    def test_memoization_effectiveness(self):
        """Test that memoization reduces nodes explored."""
        env = TicTacToe()

        # Without memoization
        solver_no_memo = MinimaxSolver(use_memoization=False)
        solver_no_memo.get_best_move(env, maximize=True)
        nodes_no_memo = solver_no_memo.nodes_explored

        # With memoization
        solver_memo = MinimaxSolver(use_memoization=True)
        solver_memo.get_best_move(env, maximize=True)
        nodes_memo = solver_memo.nodes_explored

        # Memoization should explore same or fewer nodes
        assert nodes_memo <= nodes_no_memo


class TestGameCopy:
    """Test state copying for lookahead search."""

    def test_copy_independence(self):
        """Test that copied environment is independent."""
        env1 = TicTacToe()
        env1.step(4)

        env2 = env1.copy()
        env2.step(0)

        # Original should be unaffected
        assert env1.board[0, 0] == 0
        assert env2.board[0, 0] == -1

    def test_copy_preserves_state(self):
        """Test that copy preserves all state."""
        env1 = TicTacToe()
        env1.step(4)

        env2 = env1.copy()

        assert np.array_equal(env1.board, env2.board)
        assert env1.current_player == env2.current_player
        assert env1.done == env2.done
        assert env1.winner == env2.winner


class TestStateHash:
    """Test state hashing for memoization."""

    def test_hash_uniqueness(self):
        """Test that different states have different hashes."""
        env1 = TicTacToe()
        hash1 = env1.get_state_hash()

        env2 = TicTacToe()
        env2.step(4)
        hash2 = env2.get_state_hash()

        assert hash1 != hash2

    def test_hash_consistency(self):
        """Test that same state produces same hash."""
        env1 = TicTacToe()
        env1.step(4)
        hash1 = env1.get_state_hash()

        env2 = TicTacToe()
        env2.step(4)
        hash2 = env2.get_state_hash()

        assert hash1 == hash2


class TestConvenienceFunctions:
    """Test utility functions."""

    def test_get_optimal_move(self):
        """Test convenience function for optimal move."""
        env = TicTacToe()
        move = get_optimal_move(env, player=1)
        assert move in env.get_legal_moves()

    def test_get_result(self):
        """Test game result from player perspective."""
        env = TicTacToe()
        # No result yet
        assert env.get_result(1) is None

        # Force a win for Player 1
        env.step(0); env.step(3)
        env.step(1); env.step(4)
        env.step(2)  # Player 1 wins

        assert env.get_result(1) == 1.0   # Win
        assert env.get_result(-1) == -1.0  # Loss


class TestMultipleBoardSizes:
    """Test generalized n×n boards with k-in-a-row."""

    def test_4x4_initialization(self):
        """Test 4×4 board initializes correctly."""
        env = TicTacToe(board_size=4)
        assert env.board.shape == (4, 4)
        assert env.board_size == 4
        assert env.win_length == 4
        assert np.all(env.board == 0)
        assert len(env.get_legal_moves()) == 16

    def test_5x5_initialization(self):
        """Test 5×5 board initializes correctly."""
        env = TicTacToe(board_size=5)
        assert env.board.shape == (5, 5)
        assert env.board_size == 5
        assert env.win_length == 5
        assert len(env.get_legal_moves()) == 25

    def test_custom_win_length(self):
        """Test 5×5 board with 4-in-a-row."""
        env = TicTacToe(board_size=5, win_length=4)
        assert env.board_size == 5
        assert env.win_length == 4

    def test_invalid_win_length(self):
        """Test that win_length > board_size raises error."""
        with pytest.raises(ValueError, match="cannot exceed board_size"):
            TicTacToe(board_size=3, win_length=4)

    def test_win_length_too_small(self):
        """Test that win_length < 3 raises error."""
        with pytest.raises(ValueError, match="must be at least 3"):
            TicTacToe(board_size=5, win_length=2)

    def test_4x4_horizontal_win(self):
        """Test win detection on 4×4 board (horizontal)."""
        env = TicTacToe(board_size=4)
        # Player 1 wins top row: positions 0, 1, 2, 3
        env.step(0); env.step(4)  # X:0, O:4
        env.step(1); env.step(5)  # X:1, O:5
        env.step(2); env.step(6)  # X:2, O:6
        env.step(3)  # X:3 (wins)
        assert env.done
        assert env.winner == 1

    def test_4x4_vertical_win(self):
        """Test win detection on 4×4 board (vertical)."""
        env = TicTacToe(board_size=4)
        # Player 1 wins first column: positions 0, 4, 8, 12
        env.step(0); env.step(1)   # X:0, O:1
        env.step(4); env.step(2)   # X:4, O:2
        env.step(8); env.step(3)   # X:8, O:3
        env.step(12)  # X:12 (wins)
        assert env.done
        assert env.winner == 1

    def test_4x4_diagonal_win(self):
        """Test win detection on 4×4 board (main diagonal)."""
        env = TicTacToe(board_size=4)
        # Player 1 wins main diagonal: 0, 5, 10, 15
        env.step(0); env.step(1)   # X:0, O:1
        env.step(5); env.step(2)   # X:5, O:2
        env.step(10); env.step(3)  # X:10, O:3
        env.step(15)  # X:15 (wins)
        assert env.done
        assert env.winner == 1

    def test_5x5_with_4_in_row_win(self):
        """Test 5×5 board with 4-in-a-row winning condition."""
        env = TicTacToe(board_size=5, win_length=4)
        # Player 1 wins with 4 in a row (not all 5)
        # Top row positions: 0, 1, 2, 3
        env.step(0); env.step(5)   # X:0, O:5
        env.step(1); env.step(6)   # X:1, O:6
        env.step(2); env.step(7)   # X:2, O:7
        env.step(3)  # X:3 (wins with 4 in a row)
        assert env.done
        assert env.winner == 1

    def test_depth_limited_minimax_4x4(self):
        """Test depth-limited minimax on 4×4 board."""
        env = TicTacToe(board_size=4)
        solver = MinimaxSolver(max_depth=4)

        move = solver.get_best_move(env, maximize=True)
        assert move in env.get_legal_moves()

        # Check that heuristic evaluation was used
        stats = solver.get_stats()
        assert stats['heuristic_evals'] > 0

    def test_depth_limited_minimax_5x5(self):
        """Test depth-limited minimax on 5×5 board."""
        env = TicTacToe(board_size=5)
        solver = MinimaxSolver(max_depth=3)

        move = solver.get_best_move(env, maximize=True)
        assert move in env.get_legal_moves()

        # Check that heuristic evaluation was used
        stats = solver.get_stats()
        assert stats['heuristic_evals'] > 0

    def test_heuristic_evaluation_empty_board(self):
        """Test heuristic evaluation on empty board."""
        env = TicTacToe(board_size=4)
        score = env.evaluate_heuristic(player=1)
        # Empty board should be neutral (close to 0)
        assert -0.1 <= score <= 0.1

    def test_heuristic_evaluation_winning_position(self):
        """Test heuristic favors positions with more pieces."""
        env = TicTacToe(board_size=4)
        # Place some pieces for player 1
        env.board[0, 0] = 1
        env.board[0, 1] = 1  # Two in a row
        score = env.evaluate_heuristic(player=1)
        # Should be positive (favorable for player 1)
        assert score > 0

    def test_heuristic_evaluation_losing_position(self):
        """Test heuristic recognizes opponent's threats."""
        env = TicTacToe(board_size=4)
        # Place pieces for player -1 (opponent)
        env.board[0, 0] = -1
        env.board[0, 1] = -1  # Two in a row for opponent
        score = env.evaluate_heuristic(player=1)
        # Should be negative (unfavorable for player 1)
        assert score < 0

    def test_4x4_legal_moves_update(self):
        """Test legal moves update correctly on 4×4 board."""
        env = TicTacToe(board_size=4)
        assert len(env.get_legal_moves()) == 16

        env.step(5)  # Center-ish position
        assert len(env.get_legal_moves()) == 15
        assert 5 not in env.get_legal_moves()


# Run tests
if __name__ == '__main__':
    pytest.main([__file__, '-v'])
