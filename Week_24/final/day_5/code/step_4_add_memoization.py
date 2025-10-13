"""
Step 4: Memoization (Dynamic Programming - Another 76% Speedup)

Goal: Recognize that Tic-Tac-Toe has only ~5,478 reachable states - cache results

Theory Connection:
- [THM-16.2.1] Banach Fixed Point Theorem:
  V* satisfies V* = T(V*) where T is Bellman operator
- Dynamic programming: Solve subproblems once, store results
- State space size: Only 5,478 reachable states (vs. 3^9 = 19,683 possible)
- Subproblem overlap: Same positions reached via different move orders

Key Insight:
- Game tree has duplicate states (e.g., X plays a1 then O plays b2 = same as
  X plays b2 then O plays a1 after reflection/rotation)
- First evaluation: Compute and cache
- Subsequent evaluations: Instant cache lookup (O(1))

Expected Results:
- Step 3: 18,297 nodes (many duplicates), 0.82s
- Step 4: ~2,500 unique states (first pass), 0.3-0.5s
- Cache hits on subsequent moves (near-instant)

Time: 10 minutes (read memoization pattern + run + observe cache hits)
"""

import numpy as np
from step_1_simple_env import TicTacToe, get_position_name
from typing import Tuple, Optional, Dict


# Global counters
node_count = 0
cache_hits = 0
cache_misses = 0


def minimax_with_memo(
    env: TicTacToe,
    maximize: bool = True,
    alpha: float = -float('inf'),
    beta: float = float('inf'),
    memo: Optional[Dict] = None,
    return_move: bool = True
) -> Tuple[float, Optional[int]]:
    """
    Minimax with alpha-beta pruning AND memoization

    Args:
        env: Current game state
        maximize: True if maximizing player (X), False if minimizing (O)
        alpha: Best value maximizer can guarantee
        beta: Best value minimizer can guarantee
        memo: Cache of (state_key → value) mappings
        return_move: If True, must return a move (skip cache at root level)

    Returns:
        (best_value, best_move): V*(s) and optimal action

    Theory - Dynamic Programming:
    - Bellman operator T: V = T(V) has unique fixed point V* ([THM-16.2.1])
    - Subproblem overlap: Same states reached via different paths
    - Memoization: Store T(V)(s) for each visited state s

    Cache Key:
    - state_key = (board_bytes, current_player)
    - board_bytes: env.board.tobytes() (hashable representation)
    - current_player: Who moves next (matters for value sign)

    Complexity:
    - First pass: O(|S|) where |S| ≈ 5,478 reachable states
    - Cache warm: O(1) per lookup (instant)
    """
    global node_count, cache_hits, cache_misses

    if memo is None:
        memo = {}

    node_count += 1

    # Check cache BEFORE any computation (but not at root if we need a move)
    state_key = (env.board.tobytes(), env.current_player)
    if not return_move and state_key in memo:
        cache_hits += 1
        return memo[state_key], None  # ← Cache hit! Instant return

    if state_key not in memo:
        cache_misses += 1

    # Base case: Terminal state
    if env.is_terminal():
        result = env.get_result(player=1)
        memo[state_key] = result
        return result, None

    legal_moves = env.get_legal_moves()

    if maximize:
        # Maximizing player
        best_value = -float('inf')
        best_move = legal_moves[0]

        for move in legal_moves:
            env_copy = env.copy()
            env_copy.step(move)
            value, _ = minimax_with_memo(env_copy, False, alpha, beta, memo, return_move=False)

            if value > best_value:
                best_value = value
                best_move = move

            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Alpha-beta pruning

        # Store in cache BEFORE returning
        memo[state_key] = best_value
        return best_value, best_move

    else:
        # Minimizing player
        best_value = float('inf')
        best_move = legal_moves[0]

        for move in legal_moves:
            env_copy = env.copy()
            env_copy.step(move)
            value, _ = minimax_with_memo(env_copy, True, alpha, beta, memo, return_move=False)

            if value < best_value:
                best_value = value
                best_move = move

            beta = min(beta, value)
            if beta <= alpha:
                break

        memo[state_key] = best_value
        return best_value, best_move


# ============================================================================
# Test: Compare to Step 3 + Demonstrate Cache Hits
# ============================================================================

if __name__ == "__main__":
    print("Step 4: Memoization (Dynamic Programming)\n")
    print("="*60)
    print("Expected: 0.3-0.5 seconds (vs. 0.82s in Step 3)")
    print("Unique states: ~2,500 (vs. 18,297 node evaluations in Step 3)")
    print("="*60)
    print()

    # Shared cache across moves
    memo = {}

    # ============================================
    # First Move: Cache is cold (compute all)
    # ============================================
    print("=" * 60)
    print("FIRST MOVE: Cache is cold (computing from scratch)")
    print("=" * 60)
    print()

    env = TicTacToe()
    print("Initial board:")
    print(env.render_ascii())
    print()

    # Reset counters
    node_count = 0
    cache_hits = 0
    cache_misses = 0

    import time
    start_time = time.time()

    value, move = minimax_with_memo(env, memo=memo)

    elapsed_time = time.time() - start_time

    move_name = get_position_name(move)
    print(f"Optimal move: {move_name} (index {move})")
    print(f"Value V*(s₀): {value:+.1f}")
    print(f"Unique states: {len(memo):,} (cached for future use)")
    print(f"Cache hits: {cache_hits:,}")
    print(f"Cache misses: {cache_misses:,}")
    print(f"Time: {elapsed_time:.3f} seconds")
    print()

    # ============================================
    # Second Move: Cache is warm (mostly hits)
    # ============================================
    print("=" * 60)
    print("SECOND MOVE: Cache is warm (expect many hits)")
    print("=" * 60)
    print()

    # Play the optimal first move
    env.step(move)
    print(f"After X plays {move_name}:")
    print(env.render_ascii())
    print()

    # Reset counters (but keep memo!)
    node_count = 0
    cache_hits = 0
    cache_misses = 0

    start_time = time.time()

    value, move = minimax_with_memo(env, maximize=False, memo=memo)

    elapsed_time = time.time() - start_time

    move_name = get_position_name(move)
    print(f"Optimal move: {move_name} (index {move})")
    print(f"Value V*(s): {value:+.1f}")
    print(f"Unique states in cache: {len(memo):,}")
    print(f"Cache hits: {cache_hits:,}")
    print(f"Cache misses: {cache_misses:,}")
    print(f"Hit rate: {cache_hits/(cache_hits+cache_misses)*100:.1f}%")
    print(f"Time: {elapsed_time:.3f} seconds")
    print()

    # ============================================
    # Comparison
    # ============================================
    step3_nodes = 18_297
    step3_time = 0.82

    print("="*60)
    print("📊 Comparison to Step 3 (Alpha-Beta Pruning):")
    print("="*60)
    print()
    print(f"  Step 3 (pruning):      {step3_nodes:>6,} nodes, {step3_time:>5.2f}s")
    print(f"  Step 4 (memo):         {len(memo):>6,} states, {elapsed_time:>5.3f}s (second move)")
    print()

    reduction = (1 - len(memo) / step3_nodes) * 100
    print(f"  Reduction: {reduction:.1f}% (only unique states computed)")
    print()

    # ============================================
    # Pedagogical Insights
    # ============================================
    print("🎓 Key Insights:")
    print()
    print("1. Subproblem overlap:")
    print(f"   Step 3 evaluated 18,297 nodes (many duplicates)")
    print(f"   Step 4 cached {len(memo):,} unique states")
    print(f"   Overlap: {(1 - len(memo)/step3_nodes)*100:.1f}% duplicate work eliminated")
    print()
    print("2. Cache effectiveness:")
    print("   First move: All cache misses (cold cache)")
    print("   Second move: High hit rate (warm cache)")
    print("   Later moves: Near-instant (most states already cached)")
    print()
    print("3. Dynamic programming in action:")
    print("   - Bellman operator T has fixed point V* ([THM-16.2.1])")
    print("   - Memoization computes V*(s) once per state s")
    print("   - Optimal substructure: V*(s) depends on V*(s') via recursion")
    print()
    print("4. State space size:")
    print(f"   - Theoretical: 3^9 = 19,683 possible boards")
    print(f"   - Reachable: ~5,478 (alternating moves, symmetry)")
    print(f"   - Visited (first move): {len(memo):,} states")
    print()

    print("💡 Next: Step 5 (terminal interface)")
    print("   Play against the AI using Steps 1-4")
    print("   Experience: Optimal play is unbeatable (V* = 0)")
    print()

    # Exercise
    print("📝 Exercise (2 minutes):")
    print("   1. Print memo size after each move (watch cache grow)")
    print("   2. Play full game, track cache hits per move")
    print("   3. Observe: Late-game moves are INSTANT (all cached)")
    print()
    print("="*60)
