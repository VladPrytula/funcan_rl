"""
Step 5: Terminal Interface (Human vs. Optimal AI)

Goal: Play against the AI and experience optimal play firsthand

Theory Connection:
- [THM-24.1.3] von Neumann Minimax Theorem:
  Tic-Tac-Toe value V* = 0 (draw under optimal play)

- Optimal policy π*:
  π*(s) = argmax_a V*(s,a) (AI implements this exactly)

- You cannot win against optimal play (theory guarantees this)
  Try anyway! 😈

Key Experience:
- Theory becomes tangible: V* = 0 isn't abstract, it's frustration of never winning
- Optimal policy π* isn't a formula, it's the AI's move selection you can't beat
- Algebraic notation (a1-c3) feels natural, like chess

Time: 10 minutes (play 3-5 games, try to find winning strategy)
"""

import numpy as np
from step_1_simple_env import TicTacToe, get_position_name, parse_position
from step_4_add_memoization import minimax_with_memo


def play_game(human_first: bool = True):
    """
    Human vs. AI game

    Args:
        human_first: If True, human plays X (goes first)
                     If False, AI plays X (goes first)
    """
    env = TicTacToe()
    memo = {}  # Shared cache across moves

    print("\n" + "="*60)
    print("Tic-Tac-Toe: Human vs. Optimal AI")
    print("="*60)
    print(f"You are {'X (first)' if human_first else 'O (second)'}")
    print("Input moves using algebraic notation: a1, b2, c3, etc.")
    print("="*60)
    print()

    move_count = 0

    while not env.is_terminal():
        print(env.render_ascii())
        print()

        is_human_turn = (env.current_player == 1 and human_first) or \
                        (env.current_player == -1 and not human_first)

        if is_human_turn:
            # Human move
            legal_moves = env.get_legal_moves()
            legal_names = [get_position_name(m) for m in legal_moves]

            print(f"Your turn ({'X' if env.current_player == 1 else 'O'})")
            print(f"Legal moves: {', '.join(legal_names)}")

            while True:
                try:
                    move_str = input("Your move: ").strip()
                    move = parse_position(move_str)

                    if move not in legal_moves:
                        print(f"Illegal move! Choose from: {', '.join(legal_names)}")
                        continue

                    break
                except (ValueError, IndexError):
                    print(f"Invalid input! Use format like: a1, b2, c3")

        else:
            # AI move
            print(f"AI thinking ({'X' if env.current_player == 1 else 'O'})...")

            maximize = (env.current_player == 1)
            value, move = minimax_with_memo(env, maximize=maximize, memo=memo)

            move_name = get_position_name(move)
            print(f"AI plays: {move_name}")
            print(f"Position value: {value:+.2f} (from AI's perspective)")

        # Make the move
        env.step(move)
        move_count += 1
        print()

    # Game over
    print("="*60)
    print("GAME OVER")
    print("="*60)
    print(env.render_ascii())
    print()

    winner = env._check_winner()
    if winner == 1:
        print("🎉 X wins!")
        if human_first:
            print("Congratulations! (AI must have a bug... check the code!)")
        else:
            print("AI wins. Theory vindicated: optimal play guarantees win/draw.")
    elif winner == -1:
        print("🎉 O wins!")
        if not human_first:
            print("Congratulations! (AI must have a bug... check the code!)")
        else:
            print("AI wins. Theory vindicated: optimal play guarantees win/draw.")
    else:
        print("⚖️  Draw!")
        print("As theory predicts: V* = 0 for Tic-Tac-Toe")
        print("Optimal play by both sides always leads to draw.")

    print()
    print(f"Game length: {move_count} moves")
    print(f"States cached: {len(memo):,}")
    print("="*60)


# ============================================================================
# Main: Play Multiple Games
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Step 5: Terminal Interface")
    print("="*60)
    print()
    print("🎮 Play Tic-Tac-Toe against optimal minimax AI")
    print()
    print("Theory ([THM-24.1.3]): V* = 0 for empty board")
    print("Meaning: Draw under optimal play from both sides")
    print()
    print("Your challenge: Try to win!")
    print("(Spoiler: You can't, if AI plays optimally)")
    print()

    while True:
        print("Choose starting player:")
        print("1. Human goes first (plays X)")
        print("2. AI goes first (plays X)")
        print("3. Quit")
        print()

        choice = input("Your choice (1/2/3): ").strip()

        if choice == "1":
            play_game(human_first=True)
        elif choice == "2":
            play_game(human_first=False)
        elif choice == "3":
            print("\n👋 Thanks for playing!")
            print()
            print("🎓 Key Takeaways:")
            print("- V* = 0: Draw under optimal play (theory)")
            print("- You experienced this: Can't beat optimal AI (practice)")
            print("- Optimal policy π* is concrete: AI's move selection")
            print()
            print("💡 Next: Step 6 (heuristic eval for 4×4)")
            print("   See what happens when exact V* is intractable")
            print()
            break
        else:
            print("Invalid choice! Enter 1, 2, or 3")
            print()
