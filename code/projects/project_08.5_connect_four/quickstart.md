# Connect Four: 5-Minute Quick Start

Get playing against MCTS AI in 5 minutes.

---

## Installation

**No installation needed!** All dependencies are already in `rl_toolkit`.

---

## Play Now

**All commands run from the Study root directory.**

### Basic Game (Human vs AI)

```bash
# From Study root directory
PYTHONPATH="code:$PYTHONPATH" python code/projects/project_08.5_connect_four/play_terminal.py
```

You play first (O), AI plays second (X). Enter column letters (a-g) to drop pieces.

---

### See the AI Think (Recommended!)

```bash
# From Study root directory
PYTHONPATH="code:$PYTHONPATH" python code/projects/project_08.5_connect_four/play_terminal.py --show-search-tree
```

**You'll see:**
```
Column   Visits   Q-value    UCT        Assessment
─────────────────────────────────────────────────────────
a        347      +0.680     0.520   heavily explored, strong position    ⭐
b        128      +0.540     0.760   moderately explored
c        289      +0.620     0.580   heavily explored, strong position
...
```

**What this shows:**
- **Visits**: How many times MCTS explored this move
- **Q-value**: Average game outcome (+1 = win, -1 = loss)
- **UCT**: Exploration score (higher = will explore more)
- **⭐**: Best move (most visited)

**Theory Connection:**
- This is UCB1 (bandit algorithm from Week 27-28) applied to game trees
- Formula: `UCT(s,a) = Q(s,a) + c√(ln N(s) / N(s,a))`
- Balances exploitation (high Q) vs. exploration (low visits)

---

## Configuration

### Stronger AI

```bash
# Default: 1000 simulations per move (~1 second)
PYTHONPATH="code:$PYTHONPATH" python code/projects/project_08.5_connect_four/play_terminal.py --num-simulations 1600

# Very strong (will take longer)
PYTHONPATH="code:$PYTHONPATH" python code/projects/project_08.5_connect_four/play_terminal.py --num-simulations 3200
```

### AI Plays First

```bash
PYTHONPATH="code:$PYTHONPATH" python code/projects/project_08.5_connect_four/play_terminal.py --ai-first --show-search-tree
```

### Faster Search (Depth-Limited)

```bash
# Use heuristic evaluation at depth 20 (faster, less accurate)
PYTHONPATH="code:$PYTHONPATH" python code/projects/project_08.5_connect_four/play_terminal.py --max-depth 20
```

---

## Running Tests

**All test commands run from Study root directory.**

### Environment Tests (Gravity, Win Detection)

```bash
PYTHONPATH="code:$PYTHONPATH" python -m pytest code/tests/test_connect_four.py -v
```

**Expected:** 29 tests pass

### MCTS Algorithm Tests

```bash
PYTHONPATH="code:$PYTHONPATH" python -m pytest code/projects/project_08.5_connect_four/test_mcts.py -v
```

**Expected:** 20 tests pass

### Web API Tests

```bash
PYTHONPATH="code:$PYTHONPATH" python -m pytest code/projects/project_08.5_connect_four/test_api.py -v
```

**Expected:** 16 tests pass

---

## Theory Cheat Sheet

**Connect Four as MDP ([THM-24.X.Y]):**
- State: Board position (4.5 trillion reachable states)
- Action: Column choice (max 7)
- Transition: Deterministic (gravity drops piece)
- Reward: +1 (win), -1 (loss), 0 (draw)

**MCTS as UCB1 on Trees ([THM-28.X.Y]):**
- Each node = multi-armed bandit problem
- UCT formula: Q(s,a) + c√(ln N(s) / N(s,a))
- Converges to minimax in the limit
- Scales to larger games (unlike exact minimax)

**Heuristic Evaluation:**
- Theory: V*(s) = exact optimal value
- Practice: h(s) ≈ V*(s) via pattern recognition
- Gap: h is "good enough" but not optimal

---

## Example Session

```bash
# From Study root directory
$ PYTHONPATH="code:$PYTHONPATH" python code/projects/project_08.5_connect_four/play_terminal.py --show-search-tree

======================================================================
Connect Four: Human vs MCTS AI
======================================================================
Board: 6×7
MCTS simulations: 1000
Columns: a - g

Theory Connection (Week 27-28):
  [THM-28.X.Y]: MCTS with UCT achieves logarithmic regret per node
  UCT formula: Q(s,a) + c√(ln N(s) / N(s,a))
======================================================================

Move 1
  a b c d e f g
  -------------
6 . . . . . . .
5 . . . . . . .
4 . . . . . . .
3 . . . . . . .
2 . . . . . . .
1 . . . . . . .

Your turn (Player X)
Legal columns: a, b, c, d, e, f, g

Your move: d

You played: d

Move 2
AI turn (Player O)
AI is thinking...

MCTS Search Tree Statistics
──────────────────────────────────────────────────────────────────────
Column   Visits   Q-value    UCT        Assessment
──────────────────────────────────────────────────────────────────────
a        142      +0.521     0.654   moderately explored, strong
b        98       +0.480     0.721   lightly explored, balanced
c        167      +0.556     0.602   moderately explored, strong
d        203      +0.601     0.531   heavily explored, strong    ⭐
e        145      +0.538     0.647   moderately explored, strong
f        120      +0.492     0.693   moderately explored, balanced
g        125      +0.504     0.680   moderately explored, strong
──────────────────────────────────────────────────────────────────────

AI played: d
  Nodes explored: 1001
  Max tree depth: 12

...
```

---

## Need Help?

- **Full docs**: See `README.md`
- **Implementation**: See `rl_toolkit/algorithms/mcts.py` for UCT code
- **Tests**: See `test_mcts.py` for examples

---

## Next Steps

1. **Play a game** with `--show-search-tree`
2. **Watch the UCT scores** change as AI explores
3. **Try different simulation counts** (100 vs. 1600)
4. **Read README.md** for theory connections

**Theory Connection:**
You're watching [THM-28.X.Y] (UCB1 regret bounds) applied to game trees in real-time. This is the foundation for AlphaGo, AlphaZero, and MuZero.

---

**Ready? Let's play!**

```bash
# From Study root directory
PYTHONPATH="code:$PYTHONPATH" python code/projects/project_08.5_connect_four/play_terminal.py --show-search-tree
```
