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

Author: Dr. Max Rubin
"""

import sys
import os
import time
import argparse

# Add rl_toolkit to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from rl_toolkit.envs.tictactoe import TicTacToe
from rl_toolkit.algorithms.minimax import MinimaxSolver


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

    # Find best move
    best_move = None
    for move, data in evaluations.items():
        if data['is_best']:
            best_move = move
            break

    # Sort moves by value (best first)
    sorted_moves = sorted(evaluations.items(),
                          key=lambda x: x[1]['value'],
                          reverse=maximize)

    # Display table
    print(f"\n{'Move':<6} {'Value':<8} {'Assessment':<25} {'Best':<6}")
    print("─" * 60)

    for move, data in sorted_moves:
        value_str = f"{data['value']:+.2f}"
        reasoning = data['reasoning']
        is_best_str = "⭐ YES" if data['is_best'] else ""

        # Color-code value (for terminals that support ANSI colors)
        if data['value'] > 0.5:
            value_colored = f"\033[92m{value_str}\033[0m"  # Green
        elif data['value'] > -0.5:
            value_colored = f"\033[93m{value_str}\033[0m"  # Yellow
        else:
            value_colored = f"\033[91m{value_str}\033[0m"  # Red

        print(f"{move:<6} {value_colored:<15} {reasoning:<25} {is_best_str:<6}")

    print("─" * 60)
    print(f"Best move: {best_move} (value: {evaluations[best_move]['value']:+.2f})")
    print(f"Computation time: {compute_time:.2f}s")

    # Get final stats
    stats = solver.get_stats()
    print(f"Total nodes explored: {stats['nodes_explored']:,}")
    print(f"Cache hits: {stats['cache_hits']:,}")
    if stats['heuristic_evals'] > 0:
        print(f"Heuristic evaluations: {stats['heuristic_evals']:,}")

    print("\nTheory Connection (Week 24):")
    print("These values show V*(s,a) for all actions a.")
    print("The Bellman optimality principle says: π*(s) = argmax_a V*(s,a)")
    print("In other words: optimal policy chooses the action with highest value.")
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
            # Display position grid dynamically
            for row in range(board_size):
                row_str = "  "
                for col in range(board_size):
                    pos = row * board_size + col
                    if col > 0:
                        row_str += " | "
                    row_str += f"{pos:2d}"
                print(row_str)
                if row < board_size - 1:
                    print("  " + "-" * (4 * board_size - 2))

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


def play_game(human_first: bool = True, board_size: int = 3, win_length: int = None,
              show_thinking: bool = False, explain_strategy: bool = False) -> None:
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

    solver = MinimaxSolver(max_depth=max_depth)

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
            print(f"\nYou played: {move}")
        else:
            # AI's turn
            print("\n🤖 AI is thinking...")

            # Show candidate evaluations if requested
            if show_thinking:
                display_candidate_evaluations(env, solver, maximize=(ai_player == 1))
                move = solver.get_best_move(env, maximize=(ai_player == 1))
            else:
                # Standard gameplay: just compute best move
                start_time = time.time()
                move = solver.get_best_move(env, maximize=(ai_player == 1))
                compute_time = time.time() - start_time

                # Display move and stats
                stats = solver.get_stats()
                print(f"\nAI played: {move}")
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

    args = parser.parse_args()

    print("\n" + "🎮" * 30)
    print("  WELCOME TO TIC-TAC-TOE")
    print("  Project 4.5: Minimax Optimal Play")
    print("🎮" * 30)

    # Show enabled features
    if args.show_thinking or args.explain_strategy:
        print("\n" + "─" * 60)
        print("  ENABLED FEATURES:")
        if args.show_thinking:
            print("  ✓ Show AI Thinking (candidate evaluations)")
        if args.explain_strategy:
            print("  ✓ Strategy Explanation (educational context)")
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
                     show_thinking=args.show_thinking, explain_strategy=args.explain_strategy)
        elif choice == '2':
            play_game(human_first=False, board_size=board_size, win_length=win_length,
                     show_thinking=args.show_thinking, explain_strategy=args.explain_strategy)
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
