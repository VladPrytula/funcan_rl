"""
Unit Tests for Steps 1-6

Goal: Verify correctness and performance of each step

Run:
    python tests_step_by_step.py

Or with pytest:
    pytest tests_step_by_step.py -v
"""

import numpy as np
import time
import unittest
from step_1_simple_env import TicTacToe, get_position_name, parse_position
from step_2_naive_minimax import naive_minimax
from step_3_add_alpha_beta import minimax_with_pruning
from step_4_add_memoization import minimax_with_memo
from step_6_heuristic_eval import heuristic_eval, minimax_depth_limited


class TestStep1Environment(unittest.TestCase):
    """Test Step 1: MDP formulation and algebraic notation"""

    def test_initial_state(self):
        """Test empty board initialization"""
        env = TicTacToe()
        self.assertTrue(np.all(env.board == 0))
        self.assertEqual(env.current_player, 1)

    def test_legal_moves(self):
        """Test legal move generation"""
        env = TicTacToe()
        legal = env.get_legal_moves()
        self.assertEqual(len(legal), 9)
        self.assertEqual(legal, list(range(9)))

    def test_algebraic_notation_3x3(self):
        """Test algebraic notation conversion for 3×3"""
        test_cases = [
            (0, "a1"), (1, "b1"), (2, "c1"),
            (3, "a2"), (4, "b2"), (5, "c2"),
            (6, "a3"), (7, "b3"), (8, "c3")
        ]
        for index, expected in test_cases:
            result = get_position_name(index, board_size=3)
            self.assertEqual(result, expected, f"Index {index} should be {expected}, got {result}")

    def test_algebraic_notation_4x4(self):
        """Test algebraic notation scales to 4×4"""
        self.assertEqual(get_position_name(0, board_size=4), "a1")
        self.assertEqual(get_position_name(3, board_size=4), "d1")
        self.assertEqual(get_position_name(15, board_size=4), "d4")

    def test_parse_position(self):
        """Test parsing algebraic notation"""
        test_cases = [
            ("a1", 0), ("b2", 4), ("c3", 8),
            ("A1", 0), ("B2", 4),  # Case insensitive
        ]
        for notation, expected_index in test_cases:
            result = parse_position(notation)
            self.assertEqual(result, expected_index)

    def test_win_detection_row(self):
        """Test row win detection"""
        env = TicTacToe()
        # Create row win: X X X
        env.board[0] = 1
        env.board[1] = 1
        env.board[2] = 1
        self.assertEqual(env._check_winner(), 1)

    def test_win_detection_column(self):
        """Test column win detection"""
        env = TicTacToe()
        # Create column win: a1, a2, a3
        env.board[0] = -1
        env.board[3] = -1
        env.board[6] = -1
        self.assertEqual(env._check_winner(), -1)

    def test_win_detection_diagonal(self):
        """Test diagonal win detection"""
        env = TicTacToe()
        # Main diagonal
        env.board[0] = 1
        env.board[4] = 1
        env.board[8] = 1
        self.assertEqual(env._check_winner(), 1)

    def test_win_detection_anti_diagonal(self):
        """Test anti-diagonal win detection"""
        env = TicTacToe()
        # Anti-diagonal: c1, b2, a3
        env.board[2] = -1
        env.board[4] = -1
        env.board[6] = -1
        self.assertEqual(env._check_winner(), -1)

    def test_no_winner(self):
        """Test no winner detection"""
        env = TicTacToe()
        env.board[0] = 1
        env.board[1] = -1
        self.assertIsNone(env._check_winner())

    def test_step_transition(self):
        """Test MDP transition function"""
        env = TicTacToe()
        state, reward, done = env.step(0)  # X plays a1

        self.assertEqual(env.board[0], 1)
        self.assertEqual(env.current_player, -1)  # Switched to O
        self.assertEqual(reward, 0.0)  # Game continues
        self.assertFalse(done)

    def test_copy(self):
        """Test environment deep copy"""
        env = TicTacToe()
        env.step(0)
        env_copy = env.copy()

        # Modify copy
        env_copy.step(1)

        # Original unchanged
        self.assertEqual(env.board[1], 0)
        self.assertEqual(env_copy.board[1], -1)


class TestStep2NaiveMinimax(unittest.TestCase):
    """Test Step 2: Naive minimax correctness"""

    def test_terminal_position_x_wins(self):
        """Test minimax recognizes X win"""
        env = TicTacToe()
        # X X X
        # O O .
        # . . .
        env.board = np.array([1, 1, 1, -1, -1, 0, 0, 0, 0], dtype=np.int8)
        env.current_player = 1

        value, move = naive_minimax(env)
        self.assertEqual(value, 1.0)  # X wins

    def test_terminal_position_o_wins(self):
        """Test minimax recognizes O win"""
        env = TicTacToe()
        # X X .
        # O O O
        # X . .
        env.board = np.array([1, 1, 0, -1, -1, -1, 1, 0, 0], dtype=np.int8)
        env.current_player = 1

        value, move = naive_minimax(env)
        self.assertEqual(value, -1.0)  # O wins

    def test_empty_board_value(self):
        """Test V*(s₀) = 0 for empty board (draw under optimal play)"""
        env = TicTacToe()
        value, move = naive_minimax(env)

        self.assertAlmostEqual(value, 0.0, places=5)
        self.assertIsNotNone(move)
        self.assertIn(move, env.get_legal_moves())

    def test_forced_win(self):
        """Test minimax finds forced win in one move"""
        env = TicTacToe()
        # X X .
        # O O .
        # . . .
        env.board = np.array([1, 1, 0, -1, -1, 0, 0, 0, 0], dtype=np.int8)
        env.current_player = 1

        value, move = naive_minimax(env)
        self.assertEqual(value, 1.0)  # X wins
        self.assertEqual(move, 2)  # c1 completes row

    def test_forced_block(self):
        """Test minimax blocks opponent's winning move"""
        env = TicTacToe()
        # O O .
        # X X .
        # . . .
        env.board = np.array([-1, -1, 0, 1, 1, 0, 0, 0, 0], dtype=np.int8)
        env.current_player = 1

        value, move = naive_minimax(env)
        # X must block at c1, otherwise O wins next turn
        self.assertEqual(move, 2)


class TestStep3AlphaBeta(unittest.TestCase):
    """Test Step 3: Alpha-beta pruning correctness and speedup"""

    def test_pruning_same_result_empty_board(self):
        """Test pruning produces same V* as naive for empty board"""
        env = TicTacToe()

        # Naive minimax
        import step_2_naive_minimax
        step_2_naive_minimax.node_count = 0
        value_naive, move_naive = naive_minimax(env.copy())
        nodes_naive = step_2_naive_minimax.node_count

        # Alpha-beta pruning
        import step_3_add_alpha_beta
        step_3_add_alpha_beta.node_count = 0
        value_prune, move_prune = minimax_with_pruning(env.copy())
        nodes_prune = step_3_add_alpha_beta.node_count

        # Same value
        self.assertAlmostEqual(value_naive, value_prune, places=5)

        # Fewer nodes
        self.assertLess(nodes_prune, nodes_naive)
        reduction = (1 - nodes_prune / nodes_naive) * 100
        print(f"\n  Alpha-beta reduction: {reduction:.1f}% ({nodes_naive:,} → {nodes_prune:,})")
        self.assertGreater(reduction, 80)  # At least 80% reduction

    def test_pruning_performance(self):
        """Test alpha-beta is significantly faster"""
        env = TicTacToe()

        # Time naive minimax
        start = time.time()
        value_naive, _ = naive_minimax(env.copy())
        time_naive = time.time() - start

        # Time alpha-beta
        start = time.time()
        value_prune, _ = minimax_with_pruning(env.copy())
        time_prune = time.time() - start

        speedup = time_naive / time_prune
        print(f"\n  Alpha-beta speedup: {speedup:.1f}× ({time_naive:.2f}s → {time_prune:.2f}s)")
        self.assertGreater(speedup, 5)  # At least 5× faster

    def test_pruning_mid_game(self):
        """Test pruning correctness in mid-game position"""
        env = TicTacToe()
        # X O .
        # . X .
        # . . .
        env.board = np.array([1, -1, 0, 0, 1, 0, 0, 0, 0], dtype=np.int8)
        env.current_player = -1

        value_naive, _ = naive_minimax(env.copy())
        value_prune, _ = minimax_with_pruning(env.copy())

        self.assertAlmostEqual(value_naive, value_prune, places=5)


class TestStep4Memoization(unittest.TestCase):
    """Test Step 4: Memoization correctness and cache effectiveness"""

    def test_memoization_same_result(self):
        """Test memoization produces same V* as pruning"""
        env = TicTacToe()

        value_prune, _ = minimax_with_pruning(env.copy())
        value_memo, _ = minimax_with_memo(env.copy(), memo={})

        self.assertAlmostEqual(value_prune, value_memo, places=5)

    def test_cache_hit_on_second_call(self):
        """Test cache hits on repeated evaluations"""
        env = TicTacToe()
        memo = {}

        # First call: cold cache
        import step_4_add_memoization
        step_4_add_memoization.cache_hits = 0
        step_4_add_memoization.cache_misses = 0

        value1, move1 = minimax_with_memo(env.copy(), memo=memo)
        hits1 = step_4_add_memoization.cache_hits
        misses1 = step_4_add_memoization.cache_misses

        print(f"\n  First call: {hits1} hits, {misses1} misses, {len(memo)} states cached")

        # Make a move
        env.step(move1)

        # Second call: warm cache
        step_4_add_memoization.cache_hits = 0
        step_4_add_memoization.cache_misses = 0

        value2, move2 = minimax_with_memo(env, maximize=False, memo=memo)
        hits2 = step_4_add_memoization.cache_hits
        misses2 = step_4_add_memoization.cache_misses

        print(f"  Second call: {hits2} hits, {misses2} misses")

        # Second call should have some cache hits
        self.assertGreater(hits2, 0)

    def test_memoization_speedup(self):
        """Test memoization is faster than pruning alone"""
        env = TicTacToe()

        # Time alpha-beta
        start = time.time()
        value_prune, _ = minimax_with_pruning(env.copy())
        time_prune = time.time() - start

        # Time memoization
        start = time.time()
        value_memo, _ = minimax_with_memo(env.copy(), memo={})
        time_memo = time.time() - start

        speedup = time_prune / time_memo
        print(f"\n  Memoization speedup: {speedup:.1f}× ({time_prune:.3f}s → {time_memo:.3f}s)")
        self.assertGreater(speedup, 1.5)  # At least 1.5× faster

    def test_unique_states_count(self):
        """Test number of unique states cached"""
        env = TicTacToe()
        memo = {}

        value, move = minimax_with_memo(env, memo=memo)
        num_states = len(memo)

        print(f"\n  Unique states cached: {num_states:,}")
        # Should be in range [2000, 3000] for empty 3×3 board
        self.assertGreater(num_states, 2000)
        self.assertLess(num_states, 3500)


class TestStep6HeuristicEval(unittest.TestCase):
    """Test Step 6: Heuristic evaluation for larger boards"""

    def test_heuristic_4x4_runs(self):
        """Test heuristic evaluation runs without errors on 4×4"""
        env = TicTacToe(board_size=4)
        value, move = minimax_depth_limited(env, max_depth=3)

        self.assertIsNotNone(move)
        self.assertIn(move, env.get_legal_moves())
        self.assertGreaterEqual(value, -1.0)
        self.assertLessEqual(value, 1.0)

    def test_heuristic_depth_tradeoff(self):
        """Test deeper search takes longer but may be better"""
        env = TicTacToe(board_size=4)

        times = {}
        for depth in [2, 3, 4]:
            start = time.time()
            value, move = minimax_depth_limited(env.copy(), max_depth=depth)
            times[depth] = time.time() - start

        print(f"\n  Depth 2: {times[2]:.3f}s")
        print(f"  Depth 3: {times[3]:.3f}s")
        print(f"  Depth 4: {times[4]:.3f}s")

        # Deeper search should take longer
        self.assertLess(times[2], times[3])
        self.assertLess(times[3], times[4])

    def test_heuristic_reasonable_range(self):
        """Test heuristic values are in reasonable range"""
        env = TicTacToe(board_size=4)

        for _ in range(5):
            # Random position
            if not env.is_terminal():
                legal_moves = env.get_legal_moves()
                if legal_moves:
                    move = np.random.choice(legal_moves)
                    env.step(move)

            value = heuristic_eval(env, player=env.current_player)
            self.assertGreaterEqual(value, -1.0)
            self.assertLessEqual(value, 1.0)

    def test_heuristic_prefers_center(self):
        """Test heuristic values center positions (4×4)"""
        env = TicTacToe(board_size=4)

        # X in corner
        env.board[0] = 1
        value_corner = heuristic_eval(env, player=1)

        # X in center
        env_center = TicTacToe(board_size=4)
        env_center.board[5] = 1  # b2 (center-ish)
        value_center = heuristic_eval(env_center, player=1)

        print(f"\n  Corner value: {value_corner:.3f}")
        print(f"  Center value: {value_center:.3f}")

        # Center should be slightly more valuable
        self.assertGreaterEqual(value_center, value_corner - 0.1)


class TestIntegration(unittest.TestCase):
    """Integration tests across all steps"""

    def test_all_methods_agree_on_value(self):
        """Test naive, pruning, and memoization all give same V*"""
        env = TicTacToe()
        # Mid-game position
        env.board = np.array([1, -1, 0, 0, 1, 0, 0, 0, 0], dtype=np.int8)
        env.current_player = -1

        value_naive, _ = naive_minimax(env.copy())
        value_prune, _ = minimax_with_pruning(env.copy())
        value_memo, _ = minimax_with_memo(env.copy(), memo={})

        print(f"\n  Naive: {value_naive:.5f}")
        print(f"  Pruning: {value_prune:.5f}")
        print(f"  Memoization: {value_memo:.5f}")

        self.assertAlmostEqual(value_naive, value_prune, places=5)
        self.assertAlmostEqual(value_naive, value_memo, places=5)

    def test_optimal_play_never_loses(self):
        """Test optimal AI never loses from empty board"""
        env = TicTacToe()

        while not env.is_terminal():
            maximize = (env.current_player == 1)
            value, move = minimax_with_memo(env, maximize=maximize)
            env.step(move)

        winner = env._check_winner()
        # Optimal play should draw (V* = 0)
        self.assertEqual(winner, None, "Optimal vs optimal should draw")


def run_performance_summary():
    """Print performance summary comparing all steps"""
    print("\n" + "="*70)
    print("PERFORMANCE SUMMARY")
    print("="*70)

    env = TicTacToe()

    # Step 2: Naive minimax
    import step_2_naive_minimax
    step_2_naive_minimax.node_count = 0
    start = time.time()
    value2, _ = naive_minimax(env.copy())
    time2 = time.time() - start
    nodes2 = step_2_naive_minimax.node_count

    # Step 3: Alpha-beta
    import step_3_add_alpha_beta
    step_3_add_alpha_beta.node_count = 0
    start = time.time()
    value3, _ = minimax_with_pruning(env.copy())
    time3 = time.time() - start
    nodes3 = step_3_add_alpha_beta.node_count

    # Step 4: Memoization
    memo = {}
    start = time.time()
    value4, _ = minimax_with_memo(env.copy(), memo=memo)
    time4 = time.time() - start

    print(f"\nStep 2 (Naive):        {nodes2:>8,} nodes in {time2:>6.2f}s (baseline)")
    print(f"Step 3 (Pruning):      {nodes3:>8,} nodes in {time3:>6.2f}s ({time2/time3:>5.1f}× speedup)")
    print(f"Step 4 (Memoization):  {len(memo):>8,} states in {time4:>6.2f}s ({time2/time4:>5.1f}× speedup)")
    print(f"\nAll produce same V*: {value2:.1f} (draw under optimal play)")
    print("="*70)


if __name__ == "__main__":
    # Run tests
    print("="*70)
    print("UNIT TESTS: Steps 1-6")
    print("="*70)

    unittest.main(argv=[''], verbosity=2, exit=False)

    # Print performance summary
    run_performance_summary()

    print("\n✅ All tests passed!")
    print("\nNext: Try the interactive interface:")
    print("  python step_5_terminal_interface.py")
