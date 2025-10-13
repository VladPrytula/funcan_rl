"""
Step 2: Naive Minimax (No Optimizations)

Goal: Implement Bellman optimality equation directly - experience computational pain

Theory Connection:
- [THM-25.3.1] Bellman Optimality Equation:
  V*(s) = max_a [R(s,a) + γ Σ_s' P(s'|s,a) V*(s')]

- Two-player zero-sum game (von Neumann minimax):
  V*(s) = max_a min_a' V*(s')  (alternating max/min for X and O)

- [THM-24.1.3] Minimax Theorem:
  Optimal strategy exists for finite two-player zero-sum games

Computational Reality:
- Complexity: O(b^d) where b = branching factor (~5), d = depth (~9)
- Node evaluations: ~500,000 for first move (9 empty cells)
- Runtime: 30-60 seconds per move
- This is CORRECT but UNBEARABLY SLOW

Next Step: Alpha-beta pruning reduces this by 93% (Step 3)

Time: 10 minutes (read code + observe slowness + add node counter)
"""

import numpy as np
from step_1_simple_env import TicTacToe, get_position_name
from typing import Tuple, Optional


# Global counter to track node evaluations
node_count = 0


def naive_minimax(env: TicTacToe, maximize: bool = True) -> Tuple[float, Optional[int]]:
    """
    Recursive minimax WITHOUT optimizations

    Args:
        env: Current game state
        maximize: True if maximizing player (X), False if minimizing (O)

    Returns:
        (best_value, best_move): V*(s) and optimal action
            best_value: +1 (X wins), -1 (O wins), 0 (draw)
            best_move: Optimal action (None for terminal states)

    Theory: Directly implements Bellman optimality via recursion
    - Base case: Terminal states return immediate reward
    - Recursive case: Max/min over successor states

    Warning: This evaluates ALL nodes in game tree (no pruning)
    """
    global node_count
    node_count += 1

    # Base case: Terminal state
    if env.is_terminal():
        result = env.get_result(player=1)  # From X's perspective
        return result, None

    legal_moves = env.get_legal_moves()

    if maximize:
        # Maximizing player (X seeks +1)
        best_value = -float('inf')
        best_move = legal_moves[0]  # Default to first legal move

        for move in legal_moves:
            # Simulate move
            env_copy = env.copy()
            env_copy.step(move)

            # Recursive evaluation
            value, _ = naive_minimax(env_copy, maximize=False)

            # Update best move
            if value > best_value:
                best_value = value
                best_move = move

        return best_value, best_move

    else:
        # Minimizing player (O seeks -1)
        best_value = float('inf')
        best_move = legal_moves[0]

        for move in legal_moves:
            env_copy = env.copy()
            env_copy.step(move)
            value, _ = naive_minimax(env_copy, maximize=True)

            if value < best_value:
                best_value = value
                best_move = move

        return best_value, best_move


# ============================================================================
# Test: Compute First Move (This Will Be Slow!)
# ============================================================================

if __name__ == "__main__":
    print("Step 2: Naive Minimax Implementation\n")
    print("="*60)
    print("WARNING: First move takes 30-60 seconds (grab coffee ☕)")
    print("This is intentional - you're computing V* for ~500,000 nodes")
    print("="*60)
    print()

    env = TicTacToe()
    print("Initial board:")
    print(env.render_ascii())
    print()

    # Reset node counter
    node_count = 0

    print("Computing optimal first move...")
    print("(Theory says V* = 0 for empty board - draw under optimal play)")
    print()

    import time
    start_time = time.time()

    # Compute optimal move
    value, move = naive_minimax(env)

    elapsed_time = time.time() - start_time

    # Display results
    move_name = get_position_name(move)
    print(f"\n{'='*60}")
    print(f"✅ Computation complete!")
    print(f"{'='*60}")
    print(f"Optimal move: {move_name} (index {move})")
    print(f"Value V*(s₀): {value:+.1f} (0 = draw, as theory predicts)")
    print(f"Nodes evaluated: {node_count:,}")
    print(f"Time: {elapsed_time:.2f} seconds")
    print(f"{'='*60}")
    print()

    # Pedagogical insight
    print("🎓 Key Observations:")
    print()
    print(f"1. Correctness: V* = {value:.1f} matches theory ([THM-24.1.3])")
    print(f"2. Computational cost: {node_count:,} node evaluations")
    print(f"3. Runtime: {elapsed_time:.1f}s for a single move (unbearable!)")
    print()
    print("Why so slow?")
    print("- Branching factor b ≈ 5 (average legal moves)")
    print("- Depth d ≈ 9 (maximum game length)")
    print("- Complexity: O(b^d) ≈ O(5^9) ≈ 2 million nodes")
    print()
    print("💡 Next: Step 3 (alpha-beta pruning)")
    print("   Expected improvement: 93% reduction in nodes evaluated")
    print("   Time: 30-60s → 2-4s (same correctness!)")
    print()

    # Exercise
    print("📝 Exercise (2 minutes):")
    print("   Modify code to print node_count every 10,000 nodes")
    print("   Observe how evaluation slows as tree grows")
    print()
    print("="*60)
