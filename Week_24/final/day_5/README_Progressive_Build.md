# Week 24 Day 5: Minimax Tic-Tac-Toe (Progressive Build)
**Theory Foundation:** Week 24 Days 1-4
**Time:** 60-70 minutes (6 steps × 10-15 min each)
**Outcome:** Working minimax implementation + theory-practice gap understanding

---

## Overview

This progressive build translates **von Neumann minimax theorem** ([THM-24.1.3]) and **Bellman optimality equation** ([THM-25.3.1]) into working code.

**Pedagogical Path:**
1. Understand MDP formulation (theory → code)
2. Experience computational pain (naive minimax is SLOW)
3. See theory-driven optimizations (pruning, memoization)
4. Confront theory-practice gap (exact vs. heuristic methods)

**You will build understanding incrementally—not by filling in blanks, but by reading complete implementations and experimenting.**

---

## Prerequisites

**Mathematical Background (from Week 24 Days 1-4):**
- [DEF-25.1.1]: MDP formulation (S, A, P, R, γ)
- [THM-25.3.1]: Bellman optimality equation: V*(s) = max_a Q*(s,a)
- [THM-24.1.3]: von Neumann minimax theorem (two-player zero-sum games)
- [THM-16.2.1]: Banach fixed point theorem (contraction mapping)

**Code Setup:**
```bash
cd Week_24/final/day_5/code/
python --version  # Requires Python 3.10+
pip install numpy  # Only dependency for Steps 1-5
```

---

## Learning Path

### Step 1: MDP Formulation & Algebraic Notation (15 minutes)

**File:** `step_1_simple_env.py` (80 lines)

**Goal:** Understand Tic-Tac-Toe as an MDP and introduce professional algebraic notation.

**Theory Connection:**
- **State space S:** Board configurations (3^9 = 19,683 possible, ~5,478 reachable)
- **Action space A(s):** Empty cell positions (variable size)
- **Transition P(s'|s,a):** Deterministic (place piece, check winner, swap players)
- **Reward R(s,a,s'):** +1 (X wins), -1 (O wins), 0 (draw/continue)
- **Discount γ:** 1 (episodic task, no discounting needed)

**Key Innovation: Algebraic Notation**
```python
def get_position_name(index: int, board_size: int = 3) -> str:
    """Convert flat index to algebraic notation (a1, b2, c3)"""
    row = index // board_size
    col = index % board_size
    return f"{chr(ord('a') + col)}{row + 1}"

# 3×3 board:
#   a  b  c
# 1 0  1  2
# 2 3  4  5
# 3 6  7  8
```

**Why algebraic notation?**
- Universal standard (chess, Go, Gomoku, Reversi)
- Scales naturally (4×4 = a1-d4, 15×15 Gomoku = a1-o15)
- Professional presentation (matches published game notation)
- Reusable across all board game projects (Weeks 24, 31, 40-41, 42-48)

**Tasks (15 min):**
1. **Read** `step_1_simple_env.py` (5 min)
   - Trace MDP components: `reset()`, `get_legal_moves()`, `step()`, `_check_winner()`
   - Understand algebraic notation conversion
2. **Run** basic tests (5 min):
   ```python
   python step_1_simple_env.py
   # Output: Plays random game, displays board with a1-c3 labels
   ```
3. **Exercise** (5 min): Modify `_check_winner()` to print which line won (row/column/diagonal)

**Key Takeaway:**
MDP formulation ([DEF-25.1.1]) maps directly to code: states → `self.board`, actions → `get_legal_moves()`, transitions → `step()`, rewards → win/loss detection.

---

### Step 2: Naive Minimax (Bellman Optimality in Action) (10 minutes)

**File:** `step_2_naive_minimax.py` (60 lines)

**Goal:** Implement Bellman optimality equation directly—and experience computational pain.

**Theory Connection:**
- **Bellman optimality** ([THM-25.3.1]): V*(s) = max_a [R(s,a) + γ Σ_s' P(s'|s,a) V*(s')]
- **Two-player zero-sum:** V*(s) = max_a min_a' V*(s') (alternating max/min)
- **Minimax theorem** ([THM-24.1.3]): Optimal strategy exists for finite games

**Implementation:**
```python
def naive_minimax(env, maximize=True):
    """
    Recursive minimax WITHOUT optimizations

    Complexity: O(b^d) where b=branching factor (~5), d=depth (~9)
                = ~2 million evaluations per move
    Runtime: 30-60 seconds per move (yes, really)
    """
    if env.is_terminal():
        return env.get_result(player=1), None

    legal_moves = env.get_legal_moves()

    if maximize:
        best_value = -float('inf')
        best_move = legal_moves[0]

        for move in legal_moves:
            env_copy = env.copy()
            env_copy.step(move)
            value, _ = naive_minimax(env_copy, maximize=False)

            if value > best_value:
                best_value = value
                best_move = move

        return best_value, best_move
    else:
        # Minimizing player (similar logic, flip signs)
        ...
```

**Tasks (10 min):**
1. **Read** the recursive structure (3 min)
   - Identify base case (terminal states)
   - Trace alternating max/min (max for X, min for O)
2. **Run** and observe (5 min):
   ```python
   python step_2_naive_minimax.py
   # First move takes 30-60 seconds (grab coffee ☕)
   ```
3. **Exercise** (2 min): Add counter to track nodes evaluated
   ```python
   global node_count
   node_count += 1
   # Print at end: "Evaluated X nodes"
   ```

**Expected Observations:**
- First move (9 empty cells): ~60 seconds, ~500,000 nodes
- Second move (8 empty cells): ~40 seconds, ~200,000 nodes
- **This is unbearably slow.** Theory tells us V* exists ([THM-24.1.3]), but not how to compute it efficiently.

**Key Takeaway:**
Correctness ≠ Efficiency. Naive implementation proves the algorithm works, but computational reality demands optimization.

---

### Step 3: Alpha-Beta Pruning (93% Speedup, Same Correctness) (10 minutes)

**File:** `step_3_add_alpha_beta.py` (70 lines)

**Goal:** See how theory-driven pruning delivers massive speedup without sacrificing optimality.

**Theory Connection:**
- **Pruning correctness:** If we've found a move guaranteeing value α, and opponent has a refutation guaranteeing ≤ β, we can prune when β ≤ α (opponent will never allow this branch)
- **Complexity improvement:** O(b^d) → O(b^(d/2)) in best case (with optimal move ordering)

**Key Addition (5 lines):**
```python
def minimax_with_pruning(env, maximize=True, alpha=-inf, beta=inf):
    # [Same structure as Step 2]

    for move in legal_moves:
        value, _ = minimax_with_pruning(env_copy, not maximize, alpha, beta)

        if maximize:
            best_value = max(best_value, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # ← PRUNE: opponent won't allow this
        else:
            best_value = min(best_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break  # ← PRUNE: we have a better option elsewhere
```

**Tasks (10 min):**
1. **Read** pruning logic (3 min)
   - Understand `alpha` (best guaranteed for maximizer)
   - Understand `beta` (best guaranteed for minimizer)
   - See `if beta <= alpha: break` as the pruning condition
2. **Run** and measure (5 min):
   ```python
   python step_3_add_alpha_beta.py
   # First move: ~2-4 seconds (vs. 60 seconds before!)
   # Prints: "Pruned X% of branches"
   ```
3. **Exercise** (2 min): Compare node counts from Step 2 vs. Step 3
   - Expected: Step 3 evaluates ~30,000 nodes (vs. 500,000 in Step 2)
   - **93% reduction** 🎯

**Key Takeaway:**
One `if` statement (`if beta <= alpha: break`) eliminates 93% of computation. Correctness proof: We never prune a move that could be optimal. Theory guarantees safety; practice delivers speed.

---

### Step 4: Memoization (Another 76% Speedup via Dynamic Programming) (10 minutes)

**File:** `step_4_add_memoization.py` (75 lines)

**Goal:** Recognize that Tic-Tac-Toe has only ~5,478 reachable states—cache results to avoid redundant computation.

**Theory Connection:**
- **Bellman as fixed point** ([THM-16.2.1]): V* satisfies V* = T(V*) where T is Bellman operator
- **Dynamic programming:** Solve subproblems once, store results
- **State space size:** Only 5,478 reachable states (much smaller than 3^9 = 19,683 possible)

**Key Addition (10 lines):**
```python
def minimax_with_memo(env, maximize=True, alpha=-inf, beta=inf, memo=None):
    if memo is None:
        memo = {}

    # Check cache
    state_key = (env.board.tobytes(), env.current_player)
    if state_key in memo:
        return memo[state_key], None  # ← Cache hit!

    # [Same minimax logic as Step 3]

    # Store in cache before returning
    memo[state_key] = best_value
    return best_value, best_move
```

**Tasks (10 min):**
1. **Read** memoization pattern (3 min)
   - `state_key = env.board.tobytes()` (convert board to hashable key)
   - Cache lookup before computation
   - Cache store after computation
2. **Run** and observe (5 min):
   ```python
   python step_4_add_memoization.py
   # First move: ~0.5 seconds (vs. 2-4 seconds before)
   # Second move: ~0.1 seconds (cache warm!)
   # Prints: "Cache hit rate: X%"
   ```
3. **Exercise** (2 min): Print number of unique states visited
   - Expected: ~2,000-3,000 states for first move
   - Far smaller than naive search (500,000 node evaluations)

**Expected Results:**
- Step 3 (pruning only): 2-4 seconds, ~30,000 nodes
- Step 4 (pruning + memo): 0.5 seconds, ~2,500 unique states
- **Additional 76% speedup** from caching

**Key Takeaway:**
Dynamic programming = solving subproblems once. Tic-Tac-Toe state space is small enough to cache entirely. This pattern scales to larger problems (e.g., chess opening books).

---

### Step 5: Terminal Interface (Human vs. Optimal Policy) (10 minutes)

**File:** `step_5_terminal_interface.py` (50 lines)

**Goal:** Play against the AI and experience optimal play firsthand.

**Theory Connection:**
- **Minimax theorem** ([THM-24.1.3]): Tic-Tac-Toe value V* = 0 (draw under optimal play)
- **Optimal policy π*:** AI implements π*(s) = argmax_a V*(s,a) exactly
- **You cannot win.** Theory guarantees this. Try anyway. 😈

**Implementation:**
```python
def play_game():
    """Human (X) vs. AI (O)"""
    env = TicTacToe()

    while not env.is_terminal():
        print(env.render_ascii())  # Shows a1-c3 labels

        if env.current_player == 1:
            # Human move (using algebraic notation)
            move_str = input("Your move (a1-c3): ")
            move = parse_position(move_str)  # Convert a1 → index 0
        else:
            # AI move (optimal minimax)
            value, move = minimax_with_memo(env)
            move_str = get_position_name(move)
            print(f"AI plays: {move_str} (value: {value:+.1f})")

        env.step(move)

    # Game over
    result = env.get_result(player=1)
    if result > 0:
        print("You won! (AI must have a bug...)")
    elif result < 0:
        print("AI wins.")
    else:
        print("Draw (as theory predicts).")
```

**Tasks (10 min):**
1. **Play 3-5 games** (8 min)
   - Try to win (you won't—theory guarantees draw/loss)
   - Input moves using algebraic notation (a1, b2, c3)
   - Observe AI's move selection and value estimates
2. **Exercise** (2 min): Modify AI to play suboptimally (pick random move 20% of time)
   ```python
   if random.random() < 0.2:
       move = random.choice(legal_moves)
   else:
       value, move = minimax_with_memo(env)
   ```
   - Now you can win occasionally! Theory-practice gap illustrated.

**Expected Experience:**
- **If you go first:** AI forces draw (you cannot win)
- **If AI goes first:** AI forces draw or wins if you blunder
- **Algebraic notation feels natural** (like chess)

**Key Takeaway:**
Theory becomes tangible. V* = 0 isn't abstract—it's the frustration of never winning. Optimal policy π* isn't a formula—it's the AI's move selection you can't beat.

---

### Step 6: Heuristic Evaluation for 4×4 (Theory-Practice Gap) (15 minutes, OPTIONAL)

**File:** `step_6_heuristic_eval.py` (80 lines)

**Goal:** Confront the limits of exact methods and see why practice diverges from theory.

**Theory vs. Practice:**

| Board Size | State Space | Exact Minimax | Reality |
|------------|-------------|---------------|---------|
| 3×3 | ~5,478 | ✅ 0.5 seconds | Theory works perfectly |
| 4×4 | ~10^9 | ❌ Hours/days | Need heuristic approximation |
| 5×5 | ~10^15 | ❌ Intractable | Depth-limited search + heuristics |

**Theory Says:**
- [THM-24.1.3]: V* exists for any finite game
- [THM-25.3.1]: Bellman optimality equation holds

**Practice Says:**
- Computing V* for 4×4 is intractable (even with pruning + memoization)
- Need approximation: **depth-limited search + heuristic evaluation**

**Heuristic Evaluation Function:**
```python
def heuristic_eval(env, player, board_size=4):
    """
    Hand-crafted evaluation for 4×4 Tic-Tac-Toe

    Returns: Float in [-1, 1] approximating V*(s) from player's perspective

    Theory: This approximates the true value V* (which we can't compute)
    Practice: Works well empirically, but NO GUARANTEES of optimality
    """
    score = 0

    # Count 2-in-a-row, 3-in-a-row for both players
    for line in get_all_lines(env.board, board_size):
        player_count = np.sum(line == player)
        opponent_count = np.sum(line == -player)

        # Open lines (no opponent pieces) are valuable
        if opponent_count == 0 and player_count > 0:
            score += player_count ** 2  # 2-in-a-row worth 4, 3-in-a-row worth 9

        # Opponent threats
        if player_count == 0 and opponent_count > 0:
            score -= opponent_count ** 2

    return np.tanh(score / 10)  # Normalize to [-1, 1]
```

**Depth-Limited Minimax:**
```python
def minimax_depth_limited(env, depth=0, max_depth=3, maximize=True):
    """Minimax with depth cutoff (uses heuristic at leaves)"""

    if env.is_terminal():
        return env.get_result(player=1), None

    if depth >= max_depth:
        # Reached depth limit → use heuristic (NOT exact)
        return heuristic_eval(env, env.current_player), None

    # Otherwise, standard minimax with pruning
    ...
```

**Tasks (15 min):**
1. **Read** heuristic evaluation logic (5 min)
   - Understand "open lines" scoring
   - See depth cutoff mechanism
2. **Run** 4×4 game (5 min):
   ```python
   python step_6_heuristic_eval.py --board-size 4 --max-depth 3
   # AI moves in ~2 seconds (vs. hours for exact minimax)
   ```
3. **Exercise** (5 min): Play 4×4 with depth 3
   - Does AI always win/draw? (No! Heuristic is imperfect.)
   - Try depth 4 vs. depth 3 (depth 4 should be stronger)
   - **Observe:** More depth = closer to optimal, but slower

**Expected Observations:**
- Depth 3: Plays in ~2 seconds, makes occasional mistakes
- Depth 4: Plays in ~10 seconds, stronger but still fallible
- Exact minimax (depth ∞): Computationally intractable

**Key Takeaway:**
**This is the theory-practice gap in action.**
- Theory: V* exists and Bellman equation holds ([THM-24.1.3], [THM-25.3.1])
- Practice: We can't compute V* exactly, so we approximate with heuristics
- Tradeoff: Speed vs. optimality (depth 3 is fast but imperfect)

**This pattern recurs throughout RL:**
- **Week 34 (TD learning):** Tabular convergence guaranteed → neural nets break guarantees
- **Week 36 (Q-learning):** Convergence guaranteed → DQN needs target networks + replay buffer
- **Week 37 (Policy gradients):** Unbiased estimator → high variance requires baselines

**Making peace with approximation is essential for practical RL.**

---

## Summary: What You've Built

**Progression:**
1. ✅ **Step 1:** MDP formulation + algebraic notation (theory → code)
2. ✅ **Step 2:** Naive minimax (correct but slow: 60 seconds/move)
3. ✅ **Step 3:** Alpha-beta pruning (93% speedup: 2 seconds/move)
4. ✅ **Step 4:** Memoization (76% more speedup: 0.5 seconds/move)
5. ✅ **Step 5:** Terminal interface (play vs. optimal policy)
6. ✅ **Step 6 (optional):** Heuristic eval for 4×4 (theory-practice gap)

**Total Speedup:** 60 seconds → 0.5 seconds = **120× faster** (Steps 2→4)

**Theory-Code Bridges:**
- [DEF-25.1.1] MDP → `class TicTacToe` (state, actions, transitions, rewards)
- [THM-25.3.1] Bellman optimality → `naive_minimax()` (recursive max/min)
- [THM-24.1.3] Minimax theorem → optimal play exists, V* = 0 for Tic-Tac-Toe
- [THM-16.2.1] Fixed point → memoization (DP solves subproblems once)
- **Theory-practice gap:** Exact methods fail for 4×4 → heuristics necessary

---

## Next Steps: Explore the Full Production Version

You now understand minimax, pruning, memoization, and heuristic approximation.

### 📦 Full Production Implementation

**Location:** `../../../code/projects/project_04.5_tictactoe/`

**What's Added Beyond Steps 1-6:**

1. **Web Interface** (`web_app.py`):
   - Play in browser (no terminal)
   - Real-time visualization: toggle "Show AI Thinking"
   - Color-coded move evaluations (green = strong, red = weak)
   - Hover for detailed reasoning

2. **Extended Features**:
   - Support for 4×4, 5×5 boards (heuristic eval from Step 6, scaled up)
   - Algebraic notation throughout (a1-e5 for 5×5)
   - Depth-limited search with configurable max depth
   - AI difficulty levels (depth 2 = easy, depth 4 = hard)

3. **Production Code Quality**:
   - Type hints, comprehensive docstrings
   - 75 unit tests (`tests/test_tictactoe.py`, `tests/test_position_utils.py`)
   - Reusable abstractions (`rl_toolkit/envs/base_game.py`)
   - Complete documentation (README, Lab Appendix)

4. **Lab Session Appendix** (Optional, ~2 hours):
   - Rebuild the web interface from scratch
   - Detailed commentary on Flask routes, JavaScript visualization
   - Exercises: Add new features (undo move, game history, ELO ratings)

### Recommended Path

**Immediate (Week 24):**
1. ✅ **Just completed:** Steps 1-6 (core algorithm understanding)
2. **Browse:** `projects/project_04.5_tictactoe/README.md` (see what's possible)
3. **Try:** Run web interface locally:
   ```bash
   cd ../../../code/projects/project_04.5_tictactoe/
   python web_app.py
   # Open http://localhost:5000
   # Toggle "Show AI Thinking" to see minimax in action
   ```

**Weekend (Optional):**
- Work through Lab Session Appendix (rebuild web interface, ~2 hours)
- Customize heuristic evaluation function for 5×5
- Deploy to Heroku/Render (portfolio demo)

**Later Weeks:**
- **Week 31:** Connect Four + MCTS (builds on minimax understanding)
- **Week 40-41:** Gomoku + Neural Network evaluation (replaces heuristic with learned function)
- **Week 42-48:** AlphaZero-Lite for Reversi (MCTS + neural nets + self-play)

---

## Key Pedagogical Takeaways

**1. Theory Informs Practice (Steps 1-4)**
- Bellman equation ([THM-25.3.1]) → recursive minimax implementation
- Pruning correctness → alpha-beta speedup without sacrificing optimality
- Fixed point theorem ([THM-16.2.1]) → memoization as dynamic programming

**2. Practice Diverges from Theory (Step 6)**
- Theory: V* computable for finite games ([THM-24.1.3])
- Practice: 4×4 Tic-Tac-Toe intractable → need heuristic approximation
- Tradeoff: Exact optimality vs. computational feasibility

**3. Algebraic Notation as Professional Standard**
- Scales across board sizes (3×3 → 15×15 Gomoku → 19×19 Go)
- Consistent with published game notation (chess, Go, Reversi)
- Reusable infrastructure for all future projects

**4. Incremental Complexity**
- Start with simplest case (3×3 exact minimax)
- Add optimizations one at a time (pruning, then memoization)
- Confront limits (4×4 intractable → heuristics)
- **Students experience the "why" before seeing the "how"**

---

## Troubleshooting

**"Step 2 is too slow to run"**
- Expected! First move takes 30-60 seconds (this is the pedagogical point)
- If > 2 minutes, check implementation for infinite loops
- Skip to Step 3 (pruning) if patience runs out

**"I beat the AI in Step 5"**
- Check for bugs in `_check_winner()` or `step()` logic
- AI should never lose from empty board (V* = 0 guaranteed by theory)
- If AI loses, memoization cache may be stale (restart Python session)

**"Step 6 heuristic doesn't work well for 5×5"**
- Correct observation! Hand-crafted heuristics are brittle
- This motivates Week 40-41 (neural network evaluation functions)
- For 5×5, increase depth (5-6) or improve heuristic (weight center positions higher)

**"Algebraic notation input is annoying"**
- Use `parse_position()` helper (handles "a1", "A1", "a 1" variations)
- Add autocomplete for legal moves (exercise for students)
- Web interface (full project) eliminates typing via clickable board

---

## File Checklist

Ensure you have these files in `Week_24/final/day_5/code/`:

```
✅ step_1_simple_env.py           # MDP formulation + algebraic notation
✅ step_2_naive_minimax.py         # Bellman optimality (slow)
✅ step_3_add_alpha_beta.py        # Pruning (93% speedup)
✅ step_4_add_memoization.py       # DP caching (76% speedup)
✅ step_5_terminal_interface.py    # Human vs. AI
✅ step_6_heuristic_eval.py        # 4×4 with heuristics (optional)
✅ tests_step_by_step.py           # Unit tests for each step
✅ README_Progressive_Build.md     # This file
```

**Run full test suite:**
```bash
python tests_step_by_step.py
# Expected: All tests pass (validates Steps 1-6)
```

---

## Connection to Future Weeks

**This progressive build establishes patterns used throughout the course:**

**Week 31 (Connect Four + MCTS):**
- Step 1: Connect Four env (builds on Tic-Tac-Toe MDP structure)
- Step 2: Random playout MCTS (exploration without tree policy)
- Step 3: UCB1 exploration bonus (bandit theory from Week 29)
- Same progression: naive → optimized → heuristic

**Week 36 (Q-Learning + Function Approximation):**
- Step 1: Tabular Q-learning (exact, like 3×3 minimax)
- Step 2: Neural network Q-function (approximation, like 4×4 heuristic)
- Step 3: DQN with target network (stabilization trick)
- Same theory-practice gap: exact → approximate → engineering fixes

**Week 40-41 (Gomoku + Neural Networks):**
- Step 1: 15×15 Gomoku env (extends Tic-Tac-Toe)
- Step 2: Heuristic evaluation (Step 6, scaled up)
- Step 3: Supervised learning (train CNN on expert games)
- Step 4: Neural network replaces heuristic (learned evaluation)
- **Key insight:** Neural nets learn better heuristics than hand-crafted

**Week 42-48 (AlphaZero-Lite Capstone):**
- Combines all techniques:
  - Minimax foundation (Week 24)
  - MCTS exploration (Week 31)
  - Neural network evaluation (Week 40-41)
  - Self-play training (policy iteration from Week 25)

**Everything builds on this foundation.**

---

## Questions & Clarifications

**Q: Why provide complete code instead of fill-in-the-blanks exercises?**

**A:** Three reasons:
1. **Time constraints:** Implementing from scratch takes 2-3 hours (exceeds 90-min target)
2. **Focus on concepts:** Reading complete code + experimenting teaches understanding faster than debugging syntax
3. **Realistic practice:** Real RL research involves reading paper implementations, not coding from pseudocode

**Exercises modify/extend working code—this mirrors actual research workflow.**

---

**Q: Why algebraic notation instead of numeric indices (0-8)?**

**A:** Scalability and professionalism.
- Numeric indices break for 4×4 (0-15), 5×5 (0-24), etc.
- Algebraic notation scales: 15×15 Gomoku = a1-o15 (same pattern)
- Published papers use algebraic notation (e.g., "AlphaGo played R16" not "AlphaGo played 280")
- Reusable across all game projects (one implementation, universal standard)

---

**Q: Is Step 6 (heuristic eval) required?**

**A:** No, it's optional—but **highly recommended** because:
1. Shows theory-practice gap (most important lesson in applied RL)
2. Motivates future weeks (neural networks as learned heuristics)
3. Prepares for 4×4/5×5 projects (Connect Four, Gomoku)

**If skipping Step 6:** Still read the "Theory vs. Practice" section (5 min)—understanding the gap is critical for Weeks 34-41.

---

**Q: How does this connect to Books's proofs?**

**A:** Direct correspondence:

| Proof | Code Implementation |
|--------------|---------------------|
| [THM-24.1.3] von Neumann minimax theorem | `naive_minimax()` (Step 2) |
| [THM-25.3.1] Bellman optimality equation | Recursive max/min structure |
| [THM-16.2.1] Banach fixed point | Memoization (DP subproblems) |
| Proof by induction (game tree depth) | Recursion base case (terminal states) |

** Book proves existence and uniqueness of V*. We compute it.**

---

## Final Checklist

Before moving to next topic, ensure you can answer:

- ✅ What is the MDP formulation of Tic-Tac-Toe? (S, A, P, R, γ)
- ✅ Why is naive minimax slow? (O(b^d) = ~500,000 node evaluations)
- ✅ How does alpha-beta pruning preserve correctness? (Never prunes optimal moves)
- ✅ Why does memoization work for Tic-Tac-Toe? (Only ~5,478 reachable states)
- ✅ What is V* for Tic-Tac-Toe from empty board? (V* = 0, draw under optimal play)
- ✅ When do we need heuristic evaluation? (When exact minimax is intractable)
- ✅ What's the tradeoff with heuristics? (Speed vs. optimality—no guarantees)

**If yes to all: You've mastered Week 24 implementation foundations.** 🎯

---

**Next:** Explore full project at `code/projects/project_04.5_tictactoe/` (web interface, extended features, portfolio demo)

**Future:** Week 31 (Connect Four + MCTS), Week 40-41 (Gomoku + Neural Nets), Week 42-48 (AlphaZero-Lite Capstone)

---
*Week 24 Day 5: Minimax Tic-Tac-Toe*
