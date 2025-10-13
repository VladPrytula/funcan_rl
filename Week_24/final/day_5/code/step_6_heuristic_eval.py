"""
Step 6: Heuristic Evaluation for 4×4 Boards (Theory-Practice Gap)

Goal: Confront the limits of exact methods and see why practice diverges from theory

Theory vs. Practice:
┌───────────┬─────────────┬───────────────┬────────────────────┐
│ Board Size│ State Space │ Exact Minimax │ Reality            │
├───────────┼─────────────┼───────────────┼────────────────────┤
│ 3×3       │ ~5,478      │ ✅ 0.17s      │ Theory works!      │
│ 4×4       │ ~10^9       │ ❌ Hours/days │ Need approximation │
│ 5×5       │ ~10^15      │ ❌ Intractable│ Heuristics only    │
└───────────┴─────────────┴───────────────┴────────────────────┘

Theory Says (Still True):
- [THM-24.1.3]: V* exists for any finite game
- [THM-25.3.1]: Bellman optimality equation holds

Practice Says (Computational Reality):
- Computing V* for 4×4 is intractable (even with pruning + memoization)
- Need approximation: depth-limited search + heuristic evaluation
- Tradeoff: Speed vs. optimality (no guarantees)

This Is The Theory-Practice Gap:
- Theory: V* exists and is computable (in principle)
- Practice: Can't compute V* in reasonable time (in practice)
- Solution: Approximate with heuristics (sacrifice guarantees for speed)

Time: 15-20 minutes (read heuristic + run 4×4 game + experiments)
"""

import numpy as np
from step_1_simple_env import TicTacToe, get_position_name
from typing import Tuple, Optional


def get_all_lines(board: np.ndarray, board_size: int) -> list:
    """
    Get all winning lines (rows, columns, diagonals)

    Args:
        board: Flat board array
        board_size: N for N×N board

    Returns:
        List of line arrays (each line is a subset of board indices)
    """
    lines = []

    # Rows
    for i in range(board_size):
        line_indices = list(range(i * board_size, (i + 1) * board_size))
        lines.append(board[line_indices])

    # Columns
    for i in range(board_size):
        line_indices = list(range(i, board_size * board_size, board_size))
        lines.append(board[line_indices])

    # Main diagonal
    line_indices = [i * board_size + i for i in range(board_size)]
    lines.append(board[line_indices])

    # Anti-diagonal
    line_indices = [i * board_size + (board_size - 1 - i) for i in range(board_size)]
    lines.append(board[line_indices])

    return lines


def heuristic_eval(env: TicTacToe, player: int) -> float:
    """
    Hand-crafted evaluation for N×N Tic-Tac-Toe

    Returns: Float in [-1, 1] approximating V*(s) from player's perspective

    Theory: This approximates the true value V* (which we can't compute exactly)
    Practice: Works well empirically, but NO GUARANTEES of optimality

    Heuristic Components:
    1. Open lines: Count consecutive pieces without opponent blocking
    2. Center control: Center positions are more valuable
    3. Threats: Detect immediate win/loss opportunities

    Scoring:
    - 2-in-a-row (open): +4 points
    - 3-in-a-row (open): +9 points
    - (n-1)-in-a-row: Critical threat, high value
    - Opponent threats: Negative score (mirrored)
    """
    board_size = env.board_size
    score = 0.0

    # Component 1: Line evaluation
    for line in get_all_lines(env.board, board_size):
        player_count = np.sum(line == player)
        opponent_count = np.sum(line == -player)

        # Open lines (no opponent pieces) are valuable
        if opponent_count == 0 and player_count > 0:
            score += player_count ** 2  # Quadratic: 1→1, 2→4, 3→9

        # Opponent threats
        if player_count == 0 and opponent_count > 0:
            score -= opponent_count ** 2

    # Component 2: Center control (for 4×4 and larger)
    if board_size >= 4:
        center_indices = []
        mid = board_size // 2
        for i in range(mid - 1, mid + 1):
            for j in range(mid - 1, mid + 1):
                center_indices.append(i * board_size + j)

        for idx in center_indices:
            if env.board[idx] == player:
                score += 0.5
            elif env.board[idx] == -player:
                score -= 0.5

    # Normalize to [-1, 1]
    max_score = board_size * 4 * (board_size ** 2)  # Rough upper bound
    return np.tanh(score / max_score * 3)


def minimax_depth_limited(
    env: TicTacToe,
    maximize: bool = True,
    depth: int = 0,
    max_depth: int = 3,
    alpha: float = -float('inf'),
    beta: float = float('inf')
) -> Tuple[float, Optional[int]]:
    """
    Minimax with depth cutoff (uses heuristic at leaves)

    Args:
        env: Current game state
        maximize: True if maximizing player (X)
        depth: Current search depth
        max_depth: Maximum search depth (3-4 typical for 4×4)
        alpha, beta: Pruning bounds

    Returns:
        (value, move): Estimated value and best move

    Theory: This approximates exact minimax (which is intractable)
    Practice: depth=3 plays in ~2s, depth=4 plays in ~10s

    Key Tradeoff:
    - More depth → Closer to V* but slower
    - Less depth → Faster but weaker play
    - Heuristic quality matters at leaves
    """
    # Base case 1: Terminal state
    if env.is_terminal():
        result = env.get_result(player=1)
        return result, None

    # Base case 2: Depth limit reached (use heuristic)
    if depth >= max_depth:
        # Heuristic evaluation from current player's perspective
        value = heuristic_eval(env, player=env.current_player)
        return value, None

    legal_moves = env.get_legal_moves()

    if maximize:
        best_value = -float('inf')
        best_move = legal_moves[0]

        for move in legal_moves:
            env_copy = env.copy()
            env_copy.step(move)
            value, _ = minimax_depth_limited(
                env_copy, False, depth + 1, max_depth, alpha, beta
            )

            if value > best_value:
                best_value = value
                best_move = move

            alpha = max(alpha, value)
            if beta <= alpha:
                break

        return best_value, best_move

    else:
        best_value = float('inf')
        best_move = legal_moves[0]

        for move in legal_moves:
            env_copy = env.copy()
            env_copy.step(move)
            value, _ = minimax_depth_limited(
                env_copy, True, depth + 1, max_depth, alpha, beta
            )

            if value < best_value:
                best_value = value
                best_move = move

            beta = min(beta, value)
            if beta <= alpha:
                break

        return best_value, best_move


# ============================================================================
# Test: 4×4 Tic-Tac-Toe with Heuristic Evaluation
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Step 6: Heuristic Evaluation for 4×4 Boards")
    print("="*60)
    print()
    print("Theory-Practice Gap Demonstration:")
    print("- Theory: V* computable for finite games ([THM-24.1.3])")
    print("- Practice: 4×4 has ~10^9 states (intractable)")
    print("- Solution: Depth-limited search + heuristic eval")
    print()
    print("="*60)
    print()

    # Test different depths
    for max_depth in [2, 3, 4]:
        print(f"Testing depth={max_depth} on 4×4 board...")

        env = TicTacToe(board_size=4)

        import time
        start_time = time.time()

        value, move = minimax_depth_limited(env, maximize=True, max_depth=max_depth)

        elapsed_time = time.time() - start_time

        move_name = get_position_name(move, board_size=4)

        print(f"  Depth {max_depth}: move={move_name}, value={value:+.3f}, time={elapsed_time:.3f}s")

    print()
    print("="*60)
    print("🎓 Key Observations:")
    print("="*60)
    print()
    print("1. Computational Tradeoff:")
    print("   - Depth 2: Fast (~0.01s) but weak (shallow search)")
    print("   - Depth 3: Moderate (~1-2s) and decent")
    print("   - Depth 4: Slow (~10s) but stronger")
    print()
    print("2. No Optimality Guarantee:")
    print("   - Theory: V* exists (von Neumann theorem)")
    print("   - Practice: We approximate with heuristic")
    print("   - Result: \"Good enough\" play, not proven optimal")
    print()
    print("3. Heuristic Quality Matters:")
    print("   - Our heuristic: Count open lines, value center")
    print("   - Better heuristics → Stronger play")
    print("   - Week 40-41: Neural networks learn better heuristics")
    print()
    print("4. This Pattern Recurs Throughout RL:")
    print("   - Week 34 (TD learning): Tabular → Neural nets (no convergence)")
    print("   - Week 36 (Q-learning): Exact → DQN (needs tricks)")
    print("   - Week 37 (Policy gradients): Unbiased → High variance (needs baselines)")
    print()
    print("Making peace with approximation is essential for practical RL.")
    print()
    print("="*60)
    print()
    print("💡 Completion:")
    print("   ✅ Steps 1-6 complete!")
    print("   ✅ You understand:")
    print("      - MDP formulation (Step 1)")
    print("      - Bellman optimality (Step 2)")
    print("      - Alpha-beta pruning (Step 3)")
    print("      - Dynamic programming (Step 4)")
    print("      - Optimal play experience (Step 5)")
    print("      - Theory-practice gap (Step 6)")
    print()
    print("📦 Next: Explore full project")
    print("   Location: code/projects/project_04.5_tictactoe/")
    print("   Features: Web interface, 5×5 boards, tests, Lab Appendix")
    print()
    print("="*60)
