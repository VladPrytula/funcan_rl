#!/usr/bin/env python3
"""
Interactive Tic-Tac-Toe gameplay: Human vs. Optimal AI.

Play against an AI that uses minimax search to compute optimal moves.
The AI never loses - best you can do is draw!

Theory Connection (Week 24):
- The AI computes V*(s) for every state via backward induction
- Minimax = value iteration on game tree
- Proven: optimal play results in a draw for Tic-Tac-Toe

Usage:
    python play_terminal.py                      # Standard gameplay
    python play_terminal.py --show-thinking      # Show AI candidate evaluations
    python play_terminal.py --explain-strategy   # Show AI strategy explanation
    python play_terminal.py --show-thinking --explain-strategy  # Both features
    python play_terminal.py --show-tree         # Show move evaluation summary with α-β pruning
    python play_terminal.py --show-conversation # Show minimax dialogue explaining AI reasoning
    python play_terminal.py --board-size 4      # Play on a 4x4 board (strong AI, may take longer)

"""

import sys
import os
import time
import argparse

# Add rl_toolkit to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from rl_toolkit.envs.tictactoe import TicTacToe
from rl_toolkit.algorithms.minimax import MinimaxSolver


def get_position_name(index: int, board_size: int) -> str:
    """
    Get human-readable position name for a board index using algebraic notation.

    Uses chess-like coordinate system:
    - Columns: a, b, c, ... (left to right)
    - Rows: 1, 2, 3, ... (top to bottom)

    Parameters
    ----------
    index : int
        Board position index (0-based)
    board_size : int
        Size of the board (n×n)

    Returns
    -------
    str
        Position name in algebraic notation like "a1", "b2", "c3"

    Examples
    --------
    3×3 board:
        a1  b1  c1
        a2  b2  c2
        a3  b3  c3

    4×4 board:
        a1  b1  c1  d1
        a2  b2  c2  d2
        a3  b3  c3  d3
        a4  b4  c4  d4
    """
    row = index // board_size
    col = index % board_size

    # Column letter (a, b, c, ...)
    col_letter = chr(ord('a') + col)

    # Row number (1, 2, 3, ... from top to bottom)
    row_number = row + 1

    return f'{col_letter}{row_number}'


def format_outcome(value: float, perspective: str = 'ai') -> str:
    """
    Format a minimax value as a human-readable outcome with emoji.

    Parameters
    ----------
    value : float
        Minimax value (-1 to +1)
    perspective : str
        'ai' or 'human' (default: 'ai')

    Returns
    -------
    str
        Formatted outcome like "⚖️ Draw", "✓ AI wins", "❌ Human wins"
    """
    # Flip value if showing from human perspective
    v = -value if perspective == 'human' else value

    if v >= 0.9:
        return '✓ AI wins'
    elif v >= 0.3:
        return '🟢 AI advantage'
    elif v > -0.3:
        return '⚖️ Draw'
    elif v > -0.9:
        return '🔴 Human advantage'
    else:
        return '❌ Human wins'


def display_strategy_explanation(board_size: int, max_depth: int = None) -> None:
    """
    Display educational explanation of AI strategy for the given board size.

    Explains the difference between "Optimal" (exact search) and "Strong"
    (depth-limited search with heuristic evaluation).

    Parameters
    ----------
    board_size : int
        Size of the board (n×n)
    max_depth : int or None
        Search depth limit (None = exact search)
    """
    print("\n" + "=" * 60)
    print("  🧠 AI STRATEGY EXPLANATION")
    print("=" * 60)

    if board_size == 3 and max_depth is None:
        print("""
╔════════════════════════════════════════════════════════════╗
║  OPTIMAL AI (3×3 Board)                                    ║
╚════════════════════════════════════════════════════════════╝

Strategy: EXACT SEARCH (Minimax with complete game tree)
- State space: ~5,000 states
- Search depth: Unlimited (searches to end of game)
- Evaluation: Exact win/loss/draw values
- Compute time: ~100ms per move
- Guarantee: AI NEVER loses - proven mathematically!

Theory Connection (Week 24):
The AI computes V*(s) for every reachable state via backward
induction. By the minimax theorem, this gives optimal play.
For 3×3 Tic-Tac-Toe, optimal play by both sides → draw.

Best you can do: DRAW (tie game)
""")
    else:
        # Depth-limited search
        depth_str = f"depth-{max_depth}" if max_depth else "unlimited"
        print(f"""
╔════════════════════════════════════════════════════════════╗
║  STRONG AI ({board_size}×{board_size} Board)                                    ║
╚════════════════════════════════════════════════════════════╝

Strategy: DEPTH-LIMITED SEARCH (Minimax + Heuristic)
- State space: {'~4M states' if board_size == 4 else '~430B states'} (too large for exact search!)
- Search depth: {max_depth} moves ahead
- Evaluation: Heuristic function at depth limit
- Compute time: {'~2-3s per move' if board_size == 4 else '~1-2s per move'}
- Guarantee: STRONG play, but not proven optimal

What's a "heuristic"?
Since the AI can't search all positions, it ESTIMATES position
value by counting:
  • Potential winning lines (k-in-a-row opportunities)
  • Number of pieces in each line (2-in-a-row > 1-in-a-row)
  • Control of center squares (more valuable)

Think of it like chess: Deep Blue couldn't search all positions,
so it used evaluation functions to estimate "who's winning".

Theory Connection (Week 24):
Depth-limited minimax approximates V*(s) ≈ V̂(s) where V̂ is
our heuristic. Good heuristic → strong play even at shallow depth.

Can you beat it? MAYBE! The AI is strong but not perfect.
""")

    print("=" * 60)


def display_threat_analysis(env: TicTacToe, ai_player: int) -> None:
    """
    Display tactical threat analysis to explain the strategic situation.

    Parameters
    ----------
    env : TicTacToe
        Current game state
    ai_player : int
        AI player (1 or -1)
    """
    human_player = -ai_player
    human_symbol = 'X' if human_player == 1 else 'O'
    ai_symbol = 'X' if ai_player == 1 else 'O'

    # Analyze threats from AI's perspective
    analysis = env.analyze_threats(ai_player)

    # Only show if there are significant threats
    if not analysis['opponent_threats'] and not analysis['immediate_wins']:
        return  # No critical threats, skip this section

    print("\n" + "─" * 60)
    print("  🧠 POSITION ANALYSIS")
    print("─" * 60)

    # Show immediate wins for AI
    if analysis['immediate_wins']:
        print(f"\n✓ AI ({ai_symbol}) has immediate winning moves:")
        for pos in analysis['immediate_wins']:
            pos_name = get_position_name(pos[0] * env.board_size + pos[1], env.board_size)
            print(f"  • {pos_name} wins the game!")

    # Show human threats
    if analysis['opponent_threats']:
        # Count critical threats (one move from winning)
        critical_threats = [t for t in analysis['opponent_threats'] if 'blocking_move' in t]

        if critical_threats:
            print(f"\n⚠️  Human ({human_symbol}) has {len(critical_threats)} threatening line{'s' if len(critical_threats) > 1 else ''}:")

            for threat in critical_threats:
                # Format the line description
                line_type = threat['type']
                positions = threat['positions']
                blocking_pos = threat['blocking_move']

                # Convert positions to algebraic notation
                pos_names = [get_position_name(r * env.board_size + c, env.board_size)
                             for r, c in positions]
                blocking_name = get_position_name(blocking_pos[0] * env.board_size + blocking_pos[1],
                                                   env.board_size)

                # Show the line
                line_desc = '-'.join(pos_names)
                print(f"  • {line_type.capitalize()}: {line_desc}")
                print(f"    Must block at {blocking_name}!")

        # Show developing threats (2 in a row)
        developing = [t for t in analysis['opponent_threats'] if 'blocking_move' not in t and t['pieces'] >= 2]
        if developing and not critical_threats:
            print(f"\n⚡ Human ({human_symbol}) is building {len(developing)} potential line{'s' if len(developing) > 1 else ''}:")
            for threat in developing[:3]:  # Show max 3
                line_type = threat['type']
                print(f"  • {threat['pieces']}-in-a-row on {line_type}")

    # Defensive summary
    if analysis['blocking_moves']:
        if len(analysis['blocking_moves']) == 1:
            blocking_name = get_position_name(
                analysis['blocking_moves'][0][0] * env.board_size + analysis['blocking_moves'][0][1],
                env.board_size
            )
            print(f"\n🎯 AI must play {blocking_name} to block the threat!")
        else:
            print(f"\n🎯 AI must block one of {len(analysis['blocking_moves'])} threatening positions")

    print("─" * 60)


def display_move_evaluation_summary(solver: MinimaxSolver, env: TicTacToe,
                                     maximize: bool) -> None:
    """
    Display move-by-move evaluation summary showing α-β pruning effectiveness.

    Shows all root moves evaluated by minimax, highlighting which moves were
    fully explored vs. pruned early by alpha-beta. This pedagogical visualization
    makes pruning effectiveness transparent.

    Parameters
    ----------
    solver : MinimaxSolver
        Solver instance (must have completed get_best_move() to populate move_evaluations)
    env : TicTacToe
        Current game state (for position names)
    maximize : bool
        Whether AI is maximizing or minimizing
    """
    if not solver.move_evaluations:
        print("\n⚠️  No move evaluations available. Call get_best_move() first.")
        return

    print("\n" + "=" * 80)
    print("  🎯 MOVE EVALUATION SUMMARY (Minimax with α-β Pruning)")
    print("=" * 80)

    # Calculate statistics for pruning detection
    move_evals = list(solver.move_evaluations.items())
    nodes_list = [data.nodes_explored for _, data in move_evals]
    avg_nodes = sum(nodes_list) / len(nodes_list) if nodes_list else 0

    # Heuristic: moves with < 30% of average nodes are likely pruned
    prune_threshold = avg_nodes * 0.3

    # Sort moves by evaluation order (chronological)
    sorted_moves = sorted(move_evals, key=lambda x: x[0])

    # Find best move
    best_move = None
    best_value = float('-inf') if maximize else float('inf')
    for move, data in sorted_moves:
        value = data.value
        if maximize and value > best_value:
            best_value = value
            best_move = move
        elif not maximize and value < best_value:
            best_value = value
            best_move = move

    # Display header
    print(f"\n{'#':<4} {'Position':<12} {'Value':<12} {'Status':<30} {'Nodes':<12} {'Time':<8}")
    print("─" * 80)

    fully_evaluated = 0
    pruned_count = 0
    total_nodes_full = 0
    total_nodes_pruned = 0

    for idx, (move, data) in enumerate(sorted_moves, 1):
        position_name = get_position_name(move, env.board_size)
        position_str = f"{position_name} ({move})"

        # Convert value to AI's perspective (positive = good for AI)
        raw_value = data.value
        value = raw_value if maximize else -raw_value

        # Format value
        if abs(value) > 0.9:
            value_str = f"{value:+.2f}"
        elif abs(value) < 0.1:
            value_str = " 0.00"
        else:
            value_str = f"{value:+.2f}"

        # Determine if pruned (heuristic based on nodes explored)
        is_pruned = data.nodes_explored < prune_threshold and data.nodes_explored < avg_nodes
        is_best = (move == best_move)

        # Status indicator
        if is_best:
            status = "⭐⭐⭐ BEST"
            status_color = "\033[92m"  # Green
        elif is_pruned:
            status = "⚡ PRUNED (α-β cutoff)"
            status_color = "\033[93m"  # Yellow
            pruned_count += 1
            total_nodes_pruned += data.nodes_explored
        else:
            status = "✓ Fully evaluated"
            status_color = "\033[0m"  # Normal
            fully_evaluated += 1
            total_nodes_full += data.nodes_explored

        # Color-code value
        if value > 0.3:
            value_colored = f"\033[92m{value_str}\033[0m"
        elif value > -0.3:
            value_colored = f"\033[93m{value_str}\033[0m"
        else:
            value_colored = f"\033[91m{value_str}\033[0m"

        # Format nodes and time
        nodes_str = f"{data.nodes_explored:,}"
        time_str = f"{data.time_elapsed:.2f}s"

        # Print row
        print(f"{idx:<4} {position_str:<12} {value_colored:<20} {status_color}{status:<30}\033[0m {nodes_str:<12} {time_str:<8}")

    print("=" * 80)

    # Summary statistics
    total_moves = len(sorted_moves)
    stats = solver.get_stats()
    total_nodes = stats['nodes_explored']

    print(f"\n📊 PRUNING EFFECTIVENESS:")
    print(f"   Total moves evaluated: {total_moves}")
    print(f"   ✓ Fully evaluated: {fully_evaluated} moves ({total_nodes_full:,} nodes, {total_nodes_full/total_nodes*100:.1f}%)")
    print(f"   ⚡ Pruned by α-β: {pruned_count} moves ({total_nodes_pruned:,} nodes, {total_nodes_pruned/total_nodes*100:.1f}%)")

    if pruned_count > 0:
        # Estimate nodes saved (very rough heuristic)
        if fully_evaluated > 0:
            avg_full_nodes = total_nodes_full / fully_evaluated
            estimated_saved = int(pruned_count * avg_full_nodes) - total_nodes_pruned
            if estimated_saved > 0:
                pruning_effectiveness = estimated_saved / (estimated_saved + total_nodes) * 100
                print(f"\n💡 Estimated node reduction: ~{estimated_saved:,} nodes saved (~{pruning_effectiveness:.0f}% reduction)")

    # Format best move value correctly
    best_raw_value = solver.move_evaluations[best_move].value
    best_adjusted_value = best_raw_value if maximize else -best_raw_value
    if abs(best_adjusted_value) > 0.9:
        best_value_str = f"{best_adjusted_value:+.2f}"
    elif abs(best_adjusted_value) < 0.1:
        best_value_str = " 0.00"
    else:
        best_value_str = f"{best_adjusted_value:+.2f}"

    print(f"\n🎯 Final choice: {get_position_name(best_move, env.board_size)} (value: {best_value_str})")
    print("=" * 80)

    print("\n📚 What you're seeing:")
    print("   • α-β pruning skips branches that can't affect the final decision")
    print("   • Pruned moves show dramatically fewer nodes explored")
    print("   • Move ordering matters: finding good moves early enables more pruning!")
    print("   • This is why minimax can search deep despite huge state spaces")
    print("=" * 80)


def display_minimax_conversation(solver: MinimaxSolver, env: TicTacToe,
                                  maximize: bool, best_move: int) -> None:
    """
    Display minimax reasoning as an adversarial dialogue for the chosen move.

    Shows the Principal Variation (PV) - the best line of play assuming both
    players play optimally - formatted as a conversation between AI and Human.
    This makes the minimax tree search intuitive and pedagogical.

    Parameters
    ----------
    solver : MinimaxSolver
        Solver instance (must have completed get_best_move() with PV tracking)
    env : TicTacToe
        Current game state (for position names and player symbols)
    maximize : bool
        Whether AI is maximizing (True) or minimizing (False)
    best_move : int
        The move chosen by the AI
    """
    if not solver.move_evaluations or best_move not in solver.move_evaluations:
        print("\n⚠️  No PV available for the chosen move.")
        return

    eval_data = solver.move_evaluations[best_move]
    pv = eval_data.pv
    value = eval_data.value

    if not pv:
        print("\n⚠️  Empty PV for chosen move.")
        return

    print("\n" + "=" * 80)
    print("  🗣️  MINIMAX REASONING: Why did AI choose this move?")
    print("=" * 80)

    # Determine player symbols
    ai_player = 1 if maximize else -1
    human_player = -ai_player
    ai_symbol = 'X' if ai_player == 1 else 'O'
    human_symbol = 'O' if ai_player == 1 else 'X'

    # Display principal variation as dialogue
    print(f"\n📍 Principal Variation (best play for both sides):\n")

    # Show dialogue with alternating players
    current_player = ai_player
    indent = 0

    for i, move in enumerate(pv):
        position_name = get_position_name(move, env.board_size)

        if current_player == ai_player:
            player_label = f"AI ({ai_symbol})"
            prefix = "  " * indent
            if i == 0:
                line = f'{prefix}{player_label}:    "If I play {position_name}..."'
            else:
                line = f'{prefix}{player_label}:      "Then I\'ll play {position_name}"'
        else:
            player_label = f"Human ({human_symbol})"
            prefix = "  " * indent
            line = f'{prefix}{player_label}:   "Then I\'ll respond with {position_name} (my best counter)"'
            indent += 1  # Increase indent after human move

        print(line)
        current_player = -current_player

    # Check if we hit depth limit
    if solver.max_depth is not None and len(pv) >= solver.max_depth:
        print(f'\n{"  " * indent}AI:            "Reached depth limit ({solver.max_depth} plies)"')

        # Show heuristic evaluation
        adjusted_value = value if maximize else -value
        print(f"\n🔍 Heuristic evaluation at depth {solver.max_depth}: {adjusted_value:+.2f}")
        if abs(adjusted_value) < 0.1:
            interp = "(roughly balanced position)"
        elif adjusted_value > 0.5:
            interp = "(strong advantage for AI)"
        elif adjusted_value > 0.0:
            interp = "(slight edge for AI)"
        elif adjusted_value > -0.5:
            interp = "(slight edge for Human)"
        else:
            interp = "(strong advantage for Human)"
        print(f"   {interp}")
    else:
        # Game ends
        adjusted_value = value if maximize else -value
        if adjusted_value > 0.9:
            outcome = f"AI ({ai_symbol}) wins!"
        elif adjusted_value < -0.9:
            outcome = f"Human ({human_symbol}) wins!"
        else:
            outcome = "Draw (board filled or no winning moves)"
        print(f'\n{"  " * indent}📊 Game ends: {outcome}')

    print("\n" + "=" * 80)

    # Value propagation explanation (simplified)
    adjusted_value = value if maximize else -value
    print(f"\n💭 Result: Playing {get_position_name(best_move, env.board_size)} leads to {adjusted_value:+.2f}")

    if abs(adjusted_value) > 0.9:
        print(f"   This move {'wins' if adjusted_value > 0 else 'loses'} with optimal play!")
    elif abs(adjusted_value) < 0.1:
        print("   This move leads to a draw with optimal play.")
    else:
        print(f"   This gives {'AI' if adjusted_value > 0 else 'Human'} an advantage.")

    print("\n📚 What you're seeing:")
    print("   • The PV shows the \"game tree path\" minimax follows to evaluate this move")
    print("   • Each player assumes the opponent plays optimally (chooses their best move)")
    print("   • Values propagate up: AI maximizes, Human minimizes")
    print("   • This is why it's called \"minimax\" - alternating max and min!")
    print("=" * 80)


def display_candidate_evaluations(env: TicTacToe, solver: MinimaxSolver,
                                   maximize: bool) -> None:
    """
    Display candidate move evaluations in a formatted table.

    Shows all legal moves with their minimax values and reasoning,
    highlighting the best move. This exposes V*(s,a) for all actions,
    demonstrating the Bellman optimality principle.

    Parameters
    ----------
    env : TicTacToe
        Current game state
    solver : MinimaxSolver
        Solver instance (with shared memoization cache)
    maximize : bool
        Whether AI is maximizing or minimizing
    """
    print("\n" + "─" * 60)
    print("  🤔 AI CANDIDATE EVALUATIONS")
    print("─" * 60)

    # Get candidate evaluations
    start_time = time.time()
    evaluations = solver.get_candidate_evaluations(env, maximize=maximize)
    compute_time = time.time() - start_time

    # Find best move and best value
    best_move = None
    best_value = None
    for move, data in evaluations.items():
        if data['is_best']:
            best_move = move
            best_value = data['value']
            break

    # Sort moves: best first, then by value
    sorted_moves = sorted(evaluations.items(),
                          key=lambda x: (-int(x[1]['is_best']), -x[1]['value'] if maximize else x[1]['value']))

    # Display table header
    print(f"\n{'Position':<12} {'Value':<12} {'If AI plays here...':<35} {'Priority':<10}")
    print("─" * 72)

    for move, data in sorted_moves:
        # Get position name
        position_name = get_position_name(move, env.board_size)
        position_str = f"{position_name} ({move})"

        # Format minimax value with interpretation
        # Note: value is from AI's perspective (maximize=True means AI is player +1, maximize=False means AI is player -1)
        # We need to adjust display so positive always means "good for AI"
        raw_value = data['value']

        # Convert to AI's perspective (positive = good for AI)
        value = raw_value if maximize else -raw_value

        if value > 0.9:
            value_str = f"+1 (AI wins)"
        elif value < -0.9:
            value_str = f"-1 (Human wins)"
        elif abs(value) < 0.1:
            value_str = f"0 (Draw)"
        else:
            value_str = f"{value:+.2f}"

        # Generate consequence explanation
        consequence = data['reasoning']

        # Priority indicator (use adjusted value)
        if data['is_best']:
            priority = "⭐⭐⭐ BEST"
        elif value < -0.5:
            priority = "⚠️ AVOID"
        elif best_value is not None:
            best_adjusted = best_value if maximize else -best_value
            if value < best_adjusted - 0.3:
                priority = "○ Worse"
            else:
                priority = "○ OK"
        else:
            priority = "○ OK"

        # Color-code the value (use adjusted value)
        if value > 0.3:
            value_colored = f"\033[92m{value_str}\033[0m"  # Green
        elif value > -0.3:
            value_colored = f"\033[93m{value_str}\033[0m"  # Yellow
        else:
            value_colored = f"\033[91m{value_str}\033[0m"  # Red

        print(f"{position_str:<12} {value_colored:<20} {consequence:<35} {priority:<10}")

    print("─" * 72)

    # Bottom summary
    best_position_name = get_position_name(best_move, env.board_size)
    if best_value is not None:
        # Adjust best_value for comparison (positive = good for AI)
        best_adjusted = best_value if maximize else -best_value

        if best_adjusted < -0.9:
            reason = "All moves lose - this is the least bad option"
        elif best_adjusted > 0.9:
            reason = "Winning move!"
        elif abs(best_adjusted) < 0.1:
            # Check if other moves are significantly worse
            worse_moves = [m for m, d in evaluations.items() if not d['is_best']]
            if worse_moves:
                # Adjust other values for comparison
                other_values = [evaluations[m]['value'] if maximize else -evaluations[m]['value'] for m in worse_moves]
                if all(v < -0.5 for v in other_values):
                    reason = "Only move that prevents human victory!"
                else:
                    reason = "Best positional play"
            else:
                reason = "Best positional play"
        else:
            reason = "Highest value under optimal play"

        print(f"🎯 AI chooses {best_position_name}: {reason}")

    # Stats
    stats = solver.get_stats()
    stats_parts = [f"{compute_time:.2f}s"]
    stats_parts.append(f"Nodes: {stats['nodes_explored']:,}")
    stats_parts.append(f"Cache hits: {stats['cache_hits']:,}")
    if stats['heuristic_evals'] > 0:
        stats_parts.append(f"Heuristic evals: {stats['heuristic_evals']:,}")
    print(f"Computation: {' | '.join(stats_parts)}")
    print("─" * 72)

    print("\n💡 Theory Connection (Week 24):")
    print("   Value = outcome assuming both players play optimally from here")
    print("   Bellman optimality: π*(s) = argmax_a V*(s,a)")
    print("   In other words: choose the action with highest value!")
    print("─" * 60)


def get_human_move(env: TicTacToe) -> int:
    """
    Prompt human player for a move.

    Parameters
    ----------
    env : TicTacToe
        Current game state

    Returns
    -------
    int
        Selected move index
    """
    legal_moves = env.get_legal_moves()
    board_size = env.board_size
    max_move = board_size * board_size - 1

    while True:
        try:
            print("\nAvailable positions:")

            # Display position grid with axis labels (algebraic notation)
            # Column headers (a, b, c, d...)
            col_headers = "    " + "    ".join(chr(ord('a') + col) for col in range(board_size))
            print(col_headers)

            # Display each row with row label
            for row in range(board_size):
                row_label = f" {row + 1} "  # 1-indexed row number
                row_str = row_label

                for col in range(board_size):
                    pos = row * board_size + col
                    position_name = get_position_name(pos, board_size)

                    if col > 0:
                        row_str += " "

                    # Show both algebraic notation and numeric index
                    row_str += f"{position_name}({pos:2d})"

                print(row_str)

                # Separator line between rows
                if row < board_size - 1:
                    print("   " + " " * (6 * board_size - 1))

            move_str = input(f"\nEnter your move (0-{max_move}): ").strip()
            move = int(move_str)

            if move not in legal_moves:
                print(f"❌ Invalid move. Position {move} is already occupied or out of range.")
                print(f"Legal moves: {legal_moves.tolist()}")
                continue

            return move

        except ValueError:
            print(f"❌ Please enter a number between 0 and {max_move}.")
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Goodbye!")
            sys.exit(0)


def display_search_progress(update: dict) -> None:
    """
    Live progress callback for minimax search.

    Displays real-time search statistics as the minimax tree is explored.

    Parameters
    ----------
    update : dict
        Progress update from minimax solver containing:
        - nodes_explored: int
        - cache_hits: int
        - heuristic_evals: int
        - current_depth: int
        - max_depth: int or None
        - depth_limit_hit: bool
        - elapsed_time: float
    """
    nodes = update['nodes_explored']
    cache_hits = update['cache_hits']
    h_evals = update['heuristic_evals']
    current_depth = update['current_depth']
    max_depth = update['max_depth']
    elapsed = update['elapsed_time']

    # Calculate cache hit rate
    hit_rate = (cache_hits / nodes * 100) if nodes > 0 else 0.0

    # Build progress bar for depth
    if max_depth:
        depth_pct = min(100, int(current_depth / max_depth * 100))
        bar_length = 20
        filled = int(bar_length * depth_pct / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        depth_str = f"[{bar}] {current_depth}/{max_depth} plies"
    else:
        depth_str = f"{current_depth} plies (exact search)"

    # Display live update (overwrite previous line)
    print(f"\r🔍 Depth: {depth_str} | Nodes: {nodes:,} | Cache: {cache_hits:,} ({hit_rate:.1f}%) | Time: {elapsed:.1f}s", end='', flush=True)


def play_game(human_first: bool = True, board_size: int = 3, win_length: int = None,
              show_thinking: bool = False, explain_strategy: bool = False, show_search_progress: bool = False,
              show_tree: bool = False, show_conversation: bool = False) -> None:
    """
    Play a full game of Tic-Tac-Toe.

    Parameters
    ----------
    human_first : bool, optional
        Whether human plays first (as X) or second (as O)
    board_size : int, optional
        Size of the board (n×n), default 3
    win_length : int, optional
        Number in a row needed to win, default equals board_size
    show_thinking : bool, optional
        Whether to display AI candidate evaluations during its turn
    explain_strategy : bool, optional
        Whether to display AI strategy explanation at game start
    show_search_progress : bool, optional
        Whether to display real-time search progress (recommended for 4×4+)
    show_tree : bool, optional
        Whether to display move evaluation summary with α-β pruning stats
    show_conversation : bool, optional
        Whether to display minimax dialogue showing adversarial reasoning
    """
    env = TicTacToe(board_size=board_size, win_length=win_length)

    # Configure search depth based on board size
    # 3×3: exact search (no depth limit)
    # 4×4: depth 8-10
    # 5×5: depth 4-6
    if board_size == 3:
        max_depth = None  # Exact search
    elif board_size == 4:
        max_depth = 8
    elif board_size >= 5:
        max_depth = 4
    else:
        max_depth = None

    # Create solver with optional progress callback
    progress_callback = display_search_progress if show_search_progress else None
    solver = MinimaxSolver(max_depth=max_depth, progress_callback=progress_callback)

    human_player = 1 if human_first else -1
    ai_player = -1 if human_first else 1

    print("\n" + "=" * 60)
    print(f"  TIC-TAC-TOE ({board_size}×{board_size}): Human vs. {'Optimal' if max_depth is None else 'Strong'} AI")
    print("=" * 60)
    print(f"\nBoard: {board_size}×{board_size}, Win: {env.win_length}-in-a-row")
    print(f"You are: {'X (Player 1)' if human_first else 'O (Player 2)'}")
    print(f"AI is:   {'O (Player 2)' if human_first else 'X (Player 1)'}")
    print(f"\nTheory: The AI uses minimax search with {'exact' if max_depth is None else f'depth-{max_depth}'} search.")
    if max_depth is None:
        print("Best you can do is draw - the AI never loses!")
    else:
        print("The AI uses heuristic evaluation - can you beat it?")
    print("=" * 60)

    # Show strategy explanation if requested
    if explain_strategy:
        display_strategy_explanation(board_size, max_depth)

    env.reset()

    while not env.is_terminal():
        print("\n" + "-" * 60)
        env.render()

        if env.current_player == human_player:
            # Human's turn
            print("\n🧑 Your turn!")
            move = get_human_move(env)
            position_name = get_position_name(move, env.board_size)
            print(f"\nYou played: {position_name} ({move})")
        else:
            # AI's turn
            print("\n🤖 AI is thinking...")

            # Show progress bar if requested (and not showing full thinking)
            if show_search_progress and not show_thinking:
                print()  # Newline for progress bar

            # Show candidate evaluations if requested
            if show_thinking:
                # First show threat analysis (if threats exist)
                display_threat_analysis(env, ai_player)

                # Then show candidate evaluations
                display_candidate_evaluations(env, solver, maximize=(ai_player == 1))
                move = solver.get_best_move(env, maximize=(ai_player == 1))
            else:
                # Standard gameplay: just compute best move
                start_time = time.time()
                move = solver.get_best_move(env, maximize=(ai_player == 1))
                compute_time = time.time() - start_time

                # Newline after progress bar (if shown)
                if show_search_progress:
                    print()  # Complete the progress line

                # Show tree visualization if requested
                if show_tree:
                    display_move_evaluation_summary(solver, env, maximize=(ai_player == 1))

                # Show conversation (minimax dialogue) if requested
                if show_conversation:
                    display_minimax_conversation(solver, env, maximize=(ai_player == 1), best_move=move)

                # Show final move choice
                if show_tree or show_conversation:
                    position_name = get_position_name(move, env.board_size)
                    print(f"\n✓ AI chose: {position_name} ({move})")
                else:
                    # Display move and stats
                    stats = solver.get_stats()
                    position_name = get_position_name(move, env.board_size)
                    print(f"\nAI played: {position_name} ({move})")
                    stats_str = f"  (Explored {stats['nodes_explored']:,} nodes, {stats['cache_hits']:,} cache hits"
                    if stats['heuristic_evals'] > 0:
                        stats_str += f", {stats['heuristic_evals']:,} heuristic evals"
                    stats_str += f", {compute_time:.2f}s)"
                    print(stats_str)

        # Execute move
        try:
            env.step(move)
        except ValueError as e:
            print(f"Error: {e}")
            break

    # Game over
    print("\n" + "=" * 60)
    print("  GAME OVER")
    print("=" * 60)
    env.render()
    print()

    winner = env.winner
    if winner == human_player:
        print("🎉 You won! (This shouldn't happen - did the AI malfunction?)")
    elif winner == ai_player:
        print("🤖 AI wins! Better luck next time.")
    else:
        print("🤝 Draw! Well played - you achieved optimal play!")

    print("=" * 60)


def main():
    """Main game loop with replay option and command-line argument parsing."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Interactive Tic-Tac-Toe with Minimax AI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python play_terminal.py                      # Standard gameplay
  python play_terminal.py --show-thinking      # Show AI candidate evaluations
  python play_terminal.py --explain-strategy   # Show AI strategy explanation
  python play_terminal.py --show-thinking --explain-strategy  # Both features

Theory Connection (Week 24):
The --show-thinking flag exposes V*(s,a) for all actions a, demonstrating
the Bellman optimality principle: π*(s) = argmax_a V*(s,a)
        """
    )
    parser.add_argument('--show-thinking', action='store_true',
                        help='Display AI candidate move evaluations (shows V*(s,a) for all actions)')
    parser.add_argument('--explain-strategy', action='store_true',
                        help='Display AI strategy explanation at game start')
    parser.add_argument('--show-search-progress', action='store_true',
                        help='Display real-time search progress (recommended for 4×4+ boards)')
    parser.add_argument('--show-tree', action='store_true',
                        help='Display move evaluation summary with α-β pruning effectiveness (Mode 1)')
    parser.add_argument('--show-conversation', action='store_true',
                        help='Display minimax dialogue showing adversarial reasoning (Mode 2)')

    args = parser.parse_args()

    print("\n" + "🎮" * 30)
    print("  WELCOME TO TIC-TAC-TOE")
    print("  Project 4.5: Minimax Optimal Play")
    print("🎮" * 30)

    # Show enabled features
    if args.show_thinking or args.explain_strategy or args.show_search_progress or args.show_tree or args.show_conversation:
        print("\n" + "─" * 60)
        print("  ENABLED FEATURES:")
        if args.show_thinking:
            print("  ✓ Show AI Thinking (candidate evaluations)")
        if args.explain_strategy:
            print("  ✓ Strategy Explanation (educational context)")
        if args.show_search_progress:
            print("  ✓ Live Search Progress (minimax tree visualization)")
        if args.show_tree:
            print("  ✓ Tree Visualization (α-β pruning effectiveness)")
        if args.show_conversation:
            print("  ✓ Minimax Dialogue (adversarial reasoning)")
        print("─" * 60)

    while True:
        # Configure board size
        print("\n" + "-" * 60)
        print("Choose board size:")
        print("  1. 3×3 (Classic, optimal AI)")
        print("  2. 4×4 (Challenging, depth-8 search)")
        print("  3. 5×5 (Harder, depth-4 search)")
        print("  c. Custom board")
        print("  q. Quit")
        print("-" * 60)

        size_choice = input("\nYour choice: ").strip().lower()

        if size_choice == 'q':
            print("\nThanks for playing! Goodbye. 👋")
            break
        elif size_choice == '1':
            board_size, win_length = 3, 3
        elif size_choice == '2':
            board_size, win_length = 4, 4
        elif size_choice == '3':
            board_size, win_length = 5, 5
        elif size_choice == 'c':
            try:
                board_size = int(input("Enter board size (3-10): ").strip())
                if board_size < 3 or board_size > 10:
                    print("❌ Board size must be between 3 and 10.")
                    continue
                default_win = input(f"Win length (default {board_size}): ").strip()
                win_length = int(default_win) if default_win else board_size
                if win_length < 3 or win_length > board_size:
                    print(f"❌ Win length must be between 3 and {board_size}.")
                    continue
            except ValueError:
                print("❌ Invalid input. Please enter valid numbers.")
                continue
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, c, or q.")
            continue

        # Choose who goes first
        print("\n" + "-" * 60)
        print("Choose who goes first:")
        print("  1. Human (X)")
        print("  2. AI (X)")
        print("  b. Back to board selection")
        print("-" * 60)

        choice = input("\nYour choice: ").strip().lower()

        if choice == 'b':
            continue
        elif choice == '1':
            play_game(human_first=True, board_size=board_size, win_length=win_length,
                     show_thinking=args.show_thinking, explain_strategy=args.explain_strategy,
                     show_search_progress=args.show_search_progress, show_tree=args.show_tree,
                     show_conversation=args.show_conversation)
        elif choice == '2':
            play_game(human_first=False, board_size=board_size, win_length=win_length,
                     show_thinking=args.show_thinking, explain_strategy=args.explain_strategy,
                     show_search_progress=args.show_search_progress, show_tree=args.show_tree,
                     show_conversation=args.show_conversation)
        else:
            print("❌ Invalid choice. Please enter 1, 2, or b.")
            continue

        # Ask to play again
        print("\n" + "-" * 60)
        replay = input("Play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nThanks for playing! Goodbye. 👋")
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye! 👋")
        sys.exit(0)
