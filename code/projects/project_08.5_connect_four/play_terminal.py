"""
Play Connect Four against MCTS AI in terminal.

Usage:
    python play_terminal.py --show-search-tree --num-simulations 1000

Theory Connection (Week 27-28):
    - Visualizes MCTS search tree statistics (visit counts, Q-values, UCT scores)
    - Demonstrates exploration-exploitation tradeoff in real-time
    - Shows how UCB1 formula guides tree search
"""

import argparse
import sys
from rl_toolkit.envs.connect_four import ConnectFour
from rl_toolkit.algorithms.mcts import MCTSSolver
from rl_toolkit.utils.board_viz import get_position_name_rect


def main():
    parser = argparse.ArgumentParser(
        description='Play Connect Four against MCTS AI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Theory Connection (Week 27-28):
  - MCTS implements UCT: Upper Confidence bounds for Trees
  - UCT formula: Q(s,a) + c√(ln N(s) / N(s,a))
  - Converges to minimax in limit (but scales to larger games)

Examples:
  # Basic play (1000 simulations, AI first)
  python play_terminal.py --ai-first

  # Show MCTS statistics
  python play_terminal.py --show-search-tree

  # Strong AI (1600 simulations)
  python play_terminal.py --num-simulations 1600

  # Depth-limited search with heuristic
  python play_terminal.py --max-depth 20 --show-search-tree
        """
    )
    parser.add_argument('--board-size', default='6x7',
                       help='rows×cols (default: 6x7)')
    parser.add_argument('--num-simulations', type=int, default=1000,
                       help='MCTS simulations per move (default: 1000)')
    parser.add_argument('--show-search-tree', action='store_true',
                       help='Display MCTS statistics (visits, Q-values, UCT)')
    parser.add_argument('--ai-first', action='store_true',
                       help='AI plays first (default: human first)')
    parser.add_argument('--max-depth', type=int, default=None,
                       help='MCTS simulation depth limit (default: None)')
    parser.add_argument('--exploration-constant', type=float, default=1.41,
                       help='UCT exploration constant c (default: 1.41 = sqrt(2))')

    args = parser.parse_args()

    # Parse board size
    try:
        rows, cols = map(int, args.board_size.split('x'))
    except ValueError:
        print(f"Error: Invalid board size format '{args.board_size}'. Use 'rows×cols' like '6x7'.")
        sys.exit(1)

    # Initialize
    env = ConnectFour(rows=rows, cols=cols)
    solver = MCTSSolver(
        num_simulations=args.num_simulations,
        c=args.exploration_constant,
        max_depth=args.max_depth
    )

    # Print header
    print("=" * 70)
    print("Connect Four: Human vs MCTS AI")
    print("=" * 70)
    print(f"Board: {rows}×{cols}")
    print(f"MCTS simulations: {args.num_simulations}")
    if args.max_depth:
        print(f"Max simulation depth: {args.max_depth} (uses heuristic cutoff)")
    print(f"Exploration constant: c={args.exploration_constant}")
    print(f"Columns: {chr(ord('a'))} - {chr(ord('a') + cols - 1)}")
    print()
    print("Theory Connection (Week 27-28):")
    print("  [THM-28.X.Y]: MCTS with UCT achieves logarithmic regret per node")
    print("  UCT formula: Q(s,a) + c√(ln N(s) / N(s,a))")
    print("  - Q(s,a): Average value (exploitation)")
    print("  - √(...): Exploration bonus (visits under-explored nodes)")
    print("=" * 70)

    # Game loop
    move_number = 1
    while not env.is_terminal():
        print(f"\n{'='*70}")
        print(f"Move {move_number}")
        print(f"{'='*70}")
        print(env.render())
        print()

        # Determine current player
        is_human_turn = (env.current_player == 1 and not args.ai_first) or \
                        (env.current_player == -1 and args.ai_first)

        if is_human_turn:
            # Human turn
            legal_cols = env.get_legal_moves()
            legal_names = [chr(ord('a') + c) for c in legal_cols]

            print(f"Your turn (Player {'X' if env.current_player == 1 else 'O'})")
            print(f"Legal columns: {', '.join(legal_names)}")

            while True:
                col_input = input(f"\nYour move (columns {', '.join(legal_names)}): ").strip().lower()

                if col_input == 'quit' or col_input == 'exit':
                    print("\nGame quit by user.")
                    sys.exit(0)

                if col_input and col_input in legal_names:
                    col_idx = ord(col_input) - ord('a')
                    break

                print(f"Invalid move. Choose from: {', '.join(legal_names)}")

            env.step(col_idx)
            print(f"You played: {col_input}")

        else:
            # AI turn
            print(f"AI turn (Player {'X' if env.current_player == 1 else 'O'})")
            print("AI is thinking...")

            if args.show_search_tree:
                display_mcts_statistics(env, solver, rows, cols)

            move = solver.search(env, maximize=(env.current_player == 1))
            env.step(move)

            col_name = chr(ord('a') + move)
            stats = solver.get_stats()
            print(f"\nAI played: {col_name}")
            print(f"  Nodes explored: {stats['nodes_explored']}")
            print(f"  Max tree depth: {stats['max_tree_depth']}")

        move_number += 1

    # Game over
    print(f"\n{'='*70}")
    print("GAME OVER")
    print(f"{'='*70}")
    print(env.render())
    print()

    # Determine winner
    human_player = 1 if not args.ai_first else -1
    result = env.get_result(player=human_player)

    if result > 0:
        print("🎉 You win!")
    elif result < 0:
        print("🤖 AI wins!")
    else:
        print("🤝 Draw!")

    print(f"{'='*70}")
    print(f"Total moves: {env.move_count}")
    print(f"{'='*70}")


def display_mcts_statistics(env: ConnectFour, solver: MCTSSolver, rows: int, cols: int):
    """
    Display MCTS search tree statistics.

    Shows:
    - Visit counts N(s,a)
    - Q-values (average value)
    - UCT scores
    - Natural language reasoning

    Theory Connection (Week 27-28):
    - Visualizes exploration-exploitation tradeoff
    - Best move = argmax N(s,a) (not argmax Q(s,a))
    - UCT score determines selection order during search
    """
    print("\n" + "─" * 70)
    print("MCTS Search Tree Statistics")
    print("─" * 70)
    print("Theory: UCT formula guides selection during tree search")
    print(f"  UCT(s,a) = Q(s,a) + c√(ln N(s) / N(s,a))")
    print(f"  Best move = argmax N(s,a) (most visited, not highest Q)")
    print("─" * 70)

    evaluations = solver.get_candidate_evaluations(env, maximize=(env.current_player == 1))

    if not evaluations:
        print("No evaluations available (terminal state or no legal moves)")
        return

    # Table header
    print(f"{'Column':<8} {'Visits':<8} {'Q-value':<10} {'UCT':<10} {'Assessment':<35} {'Best'}")
    print("─" * 70)

    # Sort by column index for consistent display
    for move in sorted(evaluations.keys()):
        data = evaluations[move]
        col_name = chr(ord('a') + move)
        best_mark = "⭐" if data['is_best'] else ""

        print(f"{col_name:<8} {data['visits']:<8d} "
              f"{data['value']:+.3f}     "
              f"{data['uct_score']:8.3f}   "
              f"{data['reasoning']:<35} "
              f"{best_mark}")

    print("─" * 70)
    print()


if __name__ == '__main__':
    main()
