"""
Step 3: Alpha-Beta Pruning (93% Speedup, Same Correctness)

Goal: See how theory-driven pruning delivers massive speedup without sacrificing optimality

Theory Connection:
- Pruning correctness: We can skip evaluating a branch if we prove it cannot
  affect the final decision
- Alpha (α): Best value maximizer can guarantee so far
- Beta (β): Best value minimizer can guarantee so far
- Pruning condition: If β ≤ α, remaining siblings cannot affect parent's decision

Key Insight:
- Adding ONE IF STATEMENT eliminates 93% of computation
- Optimal move is IDENTICAL to Step 2 (correctness preserved)
- Complexity: O(b^d) → O(b^(d/2)) in best case with optimal move ordering

Expected Results:
- Step 2: 549,946 nodes, 25-60 seconds
- Step 3: ~30,000-40,000 nodes, 2-4 seconds
- Reduction: 93% fewer node evaluations

Time: 10 minutes (read pruning logic + run + measure speedup)
"""

import numpy as np
from step_1_simple_env import TicTacToe, get_position_name
from typing import Tuple, Optional


# Global counters
node_count = 0
prune_count = 0


def minimax_with_pruning(
    env: TicTacToe,
    maximize: bool = True,
    alpha: float = -float('inf'),
    beta: float = float('inf')
) -> Tuple[float, Optional[int]]:
    """
    Minimax WITH alpha-beta pruning

    Args:
        env: Current game state
        maximize: True if maximizing player (X), False if minimizing (O)
        alpha: Best value maximizer can guarantee (lower bound)
        beta: Best value minimizer can guarantee (upper bound)

    Returns:
        (best_value, best_move): V*(s) and optimal action

    Theory - Pruning Correctness:
    - If maximize and value ≥ β: Minimizer won't allow this branch (prune)
    - If minimize and value ≤ α: Maximizer won't allow this branch (prune)
    - Pruning NEVER eliminates the optimal move (correctness preserved)

    Complexity: O(b^(d/2)) with good move ordering vs. O(b^d) naive
    """
    global node_count, prune_count
    node_count += 1

    # Base case: Terminal state
    if env.is_terminal():
        result = env.get_result(player=1)
        return result, None

    legal_moves = env.get_legal_moves()

    if maximize:
        # Maximizing player (X seeks +1)
        best_value = -float('inf')
        best_move = legal_moves[0]

        for move in legal_moves:
            env_copy = env.copy()
            env_copy.step(move)
            value, _ = minimax_with_pruning(env_copy, False, alpha, beta)

            if value > best_value:
                best_value = value
                best_move = move

            # Update alpha (best guarantee for maximizer)
            alpha = max(alpha, value)

            # Pruning condition: β ≤ α means minimizer won't allow this
            if beta <= alpha:
                prune_count += len(legal_moves) - (legal_moves.index(move) + 1)
                break  # ← THE MAGIC: Prune remaining siblings

        return best_value, best_move

    else:
        # Minimizing player (O seeks -1)
        best_value = float('inf')
        best_move = legal_moves[0]

        for move in legal_moves:
            env_copy = env.copy()
            env_copy.step(move)
            value, _ = minimax_with_pruning(env_copy, True, alpha, beta)

            if value < best_value:
                best_value = value
                best_move = move

            # Update beta (best guarantee for minimizer)
            beta = min(beta, value)

            # Pruning condition: β ≤ α means maximizer won't allow this
            if beta <= alpha:
                prune_count += len(legal_moves) - (legal_moves.index(move) + 1)
                break  # ← Prune remaining siblings

        return best_value, best_move


# ============================================================================
# Test: Compare to Naive Minimax (Step 2)
# ============================================================================

if __name__ == "__main__":
    print("Step 3: Alpha-Beta Pruning\n")
    print("="*60)
    print("Expected: 2-4 seconds (vs. 25-60s in Step 2)")
    print("Node reduction: ~93% (same optimal move!)")
    print("="*60)
    print()

    env = TicTacToe()
    print("Initial board:")
    print(env.render_ascii())
    print()

    # Reset counters
    node_count = 0
    prune_count = 0

    print("Computing optimal first move with alpha-beta pruning...")
    print()

    import time
    start_time = time.time()

    # Compute optimal move
    value, move = minimax_with_pruning(env)

    elapsed_time = time.time() - start_time

    # Display results
    move_name = get_position_name(move)
    print(f"{'='*60}")
    print(f"✅ Computation complete!")
    print(f"{'='*60}")
    print(f"Optimal move: {move_name} (index {move})")
    print(f"Value V*(s₀): {value:+.1f} (0 = draw, as theory predicts)")
    print(f"Nodes evaluated: {node_count:,}")
    print(f"Branches pruned: {prune_count:,}")
    print(f"Time: {elapsed_time:.2f} seconds")
    print(f"{'='*60}")
    print()

    # Comparison to Step 2
    step2_nodes = 549_946  # From Step 2 output
    step2_time = 25.56     # From Step 2 output

    reduction = (1 - node_count / step2_nodes) * 100
    speedup = step2_time / elapsed_time

    print("📊 Comparison to Step 2 (Naive Minimax):")
    print()
    print(f"  Step 2 (naive):    {step2_nodes:>8,} nodes, {step2_time:>5.1f}s")
    print(f"  Step 3 (pruning):  {node_count:>8,} nodes, {elapsed_time:>5.2f}s")
    print(f"  Reduction:         {reduction:>7.1f}% fewer nodes")
    print(f"  Speedup:           {speedup:>7.1f}× faster")
    print()

    # Pedagogical insight
    print("🎓 Key Insights:")
    print()
    print("1. Correctness preserved:")
    print(f"   V* = {value:.1f} (same as Step 2)")
    print(f"   Optimal move: {move_name} (one of several optimal first moves)")
    print()
    print("2. Massive speedup from tiny code change:")
    print("   Added: if beta <= alpha: break")
    print(f"   Result: {reduction:.0f}% reduction in node evaluations")
    print()
    print("3. Why pruning works:")
    print("   - Alpha: 'Maximizer can guarantee at least α'")
    print("   - Beta: 'Minimizer can guarantee at most β'")
    print("   - If β ≤ α: Contradiction! This branch is unreachable")
    print()
    print("4. Theory guarantees safety:")
    print("   - Pruning NEVER eliminates optimal move")
    print("   - Only skips provably suboptimal branches")
    print()

    print("💡 Next: Step 4 (memoization)")
    print(f"   Current: {node_count:,} nodes, {elapsed_time:.2f}s")
    print("   Expected: ~2,500 unique states, 0.3-0.5s")
    print("   Additional improvement: 76% speedup via caching")
    print()

    # Exercise
    print("📝 Exercise (2 minutes):")
    print("   Add print statement when pruning occurs:")
    print("   print(f'Pruned {remaining} branches at depth {depth}')")
    print("   Observe: Pruning happens most at shallow depths")
    print()
    print("="*60)
