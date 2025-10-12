# Board Size Generalization - Upgrade Summary

**Date**: 2025-10-12
**Feature**: Generalized Tic-Tac-Toe for n×n boards with k-in-a-row

---

## Overview

Upgraded the Tic-Tac-Toe implementation from fixed 3×3 to fully generalized n×n boards with configurable k-in-a-row winning conditions. Both terminal and web interfaces now support multiple board sizes with depth-limited minimax search for larger boards.

---

## Changes Made

### 1. Core Game Engine (`rl_toolkit/envs/tictactoe.py`)

**Generalized for any board size:**
- Added `board_size` and `win_length` parameters to `__init__()`
- Default: `board_size=3`, `win_length=board_size`
- Validation: `win_length ≤ board_size` and `win_length ≥ 3`

**Updated win detection:**
- Replaced hardcoded 3×3 checks with sliding window algorithm
- Supports k-in-a-row detection on any n×n board
- Checks all rows, columns, diagonals, and anti-diagonals

**Added heuristic evaluation function:**
```python
def evaluate_heuristic(self, player: int) -> float:
    """
    Heuristic evaluation for non-terminal states.
    Essential for depth-limited search on larger boards.

    Returns value in [-1, 1] range:
    - Positive: favorable for player
    - Negative: favorable for opponent
    - Zero: neutral

    Algorithm:
    - Counts potential winning lines (k-in-a-row opportunities)
    - Weights by number of pieces in line (2-in-a-row > 1-in-a-row)
    - Exponential reward: n pieces → n² score
    """
```

**State space complexity:**
- 3×3: ~5,000 states (exact search feasible)
- 4×4: ~4 million states (depth-limited needed)
- 5×5: ~430 billion states (depth-limited essential)

---

### 2. Minimax Algorithm (`rl_toolkit/algorithms/minimax.py`)

**Added depth-limited search:**
- New parameter: `max_depth: Optional[int] = None`
- `None`: Exact search (for 3×3)
- `int`: Depth-limited search with heuristic evaluation

**Depth limits by board size:**
```python
3×3: max_depth = None   # Exact search (optimal)
4×4: max_depth = 8      # Strong play
5×5: max_depth = 4      # Competent play
```

**Added heuristic evaluation tracking:**
- New stat: `heuristic_evals` (count of heuristic calls)
- Included in `get_stats()` and `reset_stats()`

**Performance:**
- 3×3 first move: ~1,500 nodes, 0 heuristic evals, ~100ms
- 4×4 first move: ~957K nodes, 503K heuristic evals, ~2-3 seconds
- 5×5 first move: ~187K nodes, 150K heuristic evals, ~1-2 seconds

---

### 3. Terminal Game (`projects/project_04.5_tictactoe/play_terminal.py`)

**Added board size selection menu:**
```
Choose board size:
  1. 3×3 (Classic, optimal AI)
  2. 4×4 (Challenging, depth-8 search)
  3. 5×5 (Harder, depth-4 search)
  c. Custom board
  q. Quit
```

**Dynamic move display:**
- Position grid adjusts to board size
- Shows all valid move indices
- Example for 4×4:
  ```
   0 |  1 |  2 |  3
  -----------------
   4 |  5 |  6 |  7
  -----------------
   8 |  9 | 10 | 11
  -----------------
  12 | 13 | 14 | 15
  ```

**Updated stats display:**
- Shows heuristic evaluations for depth-limited search
- Example: `(Explored 187,023 nodes, 10,444 cache hits, 149,870 heuristic evals)`

---

### 4. Web Interface (`rl_toolkit/web/templates/tictactoe.html`)

**Complete rewrite for dynamic rendering:**

**Added configuration UI:**
- Board size selector: 3×3, 4×4, 5×5
- First player selector: Human or AI
- AI mode indicator: "Optimal" (3×3) or "Strong" (4×4+)

**Dynamic board rendering:**
- Grid columns: `grid-template-columns: repeat(${size}, 1fr)`
- Font size scales with board: 3em (3×3) → 2em (5×5)
- Cells generated programmatically in JavaScript

**Dynamic win detection:**
- JavaScript function `generateWinningLines()` computes all k-in-a-row lines
- Supports any board size and win length
- Highlights winning line on game over

**Updated stats panel:**
```
Last AI search: 957,807 nodes
Cache hits: 206,853
Heuristic evals: 503,439
Computation time: 2,345 ms
```

---

### 5. Backend API (`projects/project_04.5_tictactoe/web_app.py`)

**Updated `/tictactoe/move` endpoint:**

**Request JSON:**
```json
{
  "board": [0, 0, 0, ...],  // Flattened board state
  "board_size": 4,           // Optional, default 3
  "win_length": 4            // Optional, default board_size
}
```

**Automatic depth configuration:**
```python
if board_size == 3:
    max_depth = None  # Exact search
elif board_size == 4:
    max_depth = 8
elif board_size >= 5:
    max_depth = 4
```

**Response includes heuristic stats:**
```json
{
  "move": 5,
  "stats": {
    "nodes_explored": 957807,
    "cache_hits": 206853,
    "cache_size": 246392,
    "heuristic_evals": 503439,
    "compute_time_ms": 2345.67
  }
}
```

---

### 6. Visualization Features (Added 2025-10-12)

**NEW: AI Thinking Visualization** to illustrate minimax search process in real-time.

#### Terminal Visualization (`play_terminal.py`)

**Added command-line flags:**
```bash
python play_terminal.py --show-thinking      # Show AI candidate evaluations
python play_terminal.py --explain-strategy   # Show AI strategy explanation
```

**Features:**
- **Candidate evaluations table**: Shows V*(s,a) for all legal moves
- **Color-coded values**: ANSI colors (green → yellow → red)
- **Natural language reasoning**: Translates values to strategic concepts
  - Example: "+0.80 → Creates strong threats"
  - Example: "-0.30 → Slightly defensive"
- **Live statistics**: Nodes explored, cache hits, heuristic evaluations, compute time
- **Strategy explanations**: Educational context distinguishing "Optimal" (3×3) vs "Strong" (4×4+)

**Implementation:**
- `display_candidate_evaluations()` function (80 lines)
- `display_strategy_explanation()` function (70 lines)
- `argparse` for command-line flag parsing
- Progress tracking with `time.time()` for compute duration

#### Web Visualization (`tictactoe.html`)

**Added UI elements:**
- **AI Mode Badge**: Hover tooltip explains "Optimal" vs "Strong" with info icon
- **Show Candidate Moves Toggle**: Performance-aware (default: off)
- **Color-coded overlays**: HSL color scale (hue = (value + 1) * 60°)
  - Red (-1.0) → Yellow (0.0) → Green (+1.0)
- **Best move highlight**: Glow animation with CSS keyframes
- **Expandable education section**:
  - Strategy comparison table (3×3, 4×4, 5×5)
  - Heuristic explanation (chess analogy)
  - Theory Connection (Week 24): Bellman optimality

**Backend support (`web_app.py`):**
- New `/tictactoe/candidates` endpoint (115 lines)
- Returns: `{candidates: {move: {value, reasoning, is_best, ...}}, best_move, stats}`
- Reuses solver's memoization cache for efficiency
- Expected compute times: 3×3 (~200ms), 4×4 (~10-15s), 5×5 (~8-12s)

**JavaScript functions:**
- `showCandidateEvaluations()` - fetches and displays candidate values
- `clearCandidateValues()` - removes overlays
- `toggleCandidates()` - toggle switch handler
- `updateAIMode()` - updates badge based on board size

**Theory Connection:**
Visualization exposes V*(s,a) for all actions a, demonstrating Bellman optimality:
```
π*(s) = argmax_a V*(s,a)
```

#### Minimax Enhancements (`minimax.py`)

**Added to support visualization:**
1. **Progress callbacks** (throttled to 100ms):
   - `progress_callback` parameter in `__init__()`
   - Provides: nodes_explored, cache_hits, heuristic_evals, current_depth, elapsed_time
   - Used for live stats in web UI (future feature)

2. **Candidate evaluation method** (90 lines):
   ```python
   def get_candidate_evaluations(env, maximize=True) -> Dict[int, Dict[str, Any]]
   ```
   - Returns value, reasoning, depth_used, is_best, is_terminal for each legal move
   - Shares memoization cache (efficient for 3×3)

3. **Reasoning generators** (35 lines):
   - `_generate_reasoning()` - translates values to strategic concepts
   - `_generate_terminal_reasoning()` - explains terminal outcomes

---

### 7. Tests (`tests/test_tictactoe.py`)

**Added new test class: `TestMultipleBoardSizes`**

**15 new tests (38 total, all passing ✅):**

1. `test_4x4_initialization` - Board setup
2. `test_5x5_initialization` - Board setup
3. `test_custom_win_length` - 5×5 with 4-in-a-row
4. `test_invalid_win_length` - Error handling
5. `test_win_length_too_small` - Error handling
6. `test_4x4_horizontal_win` - Win detection
7. `test_4x4_vertical_win` - Win detection
8. `test_4x4_diagonal_win` - Win detection
9. `test_5x5_with_4_in_row_win` - Custom win length
10. `test_depth_limited_minimax_4x4` - Depth-limited search
11. `test_depth_limited_minimax_5x5` - Depth-limited search
12. `test_heuristic_evaluation_empty_board` - Heuristic is neutral
13. `test_heuristic_evaluation_winning_position` - Heuristic favors player
14. `test_heuristic_evaluation_losing_position` - Heuristic recognizes threats
15. `test_4x4_legal_moves_update` - Move validation

**Test results:**
```
38 passed in 3.46s
```

---

## Theory Connections

### State Space Explosion

| Board Size | State Space | Search Strategy | Nodes (1st move) |
|------------|-------------|-----------------|------------------|
| 3×3        | ~5K states  | Exact minimax   | ~1,500           |
| 4×4        | ~4M states  | Depth-8 + heuristic | ~960K        |
| 5×5        | ~430B states| Depth-4 + heuristic | ~187K        |

### Depth-Limited Minimax

**Principle:**
- Exact search intractable for large boards
- Solution: Limit search depth, use heuristic at leaves
- Trade-off: Optimality vs. computational feasibility

**Heuristic Quality:**
- Good heuristic → strong play even at shallow depth
- Our heuristic: Count potential k-in-a-row lines, weight by pieces

**Connection to Week 24 Theory:**
- Minimax = value iteration on game tree [THM-24.X.Y]
- Depth limit = finite horizon approximation
- Heuristic = approximate value function V̂(s) ≈ V*(s)

---

## Usage

### Terminal (Quick Test)

```bash
cd code/projects/project_04.5_tictactoe

# Standard gameplay
python play_terminal.py

# With visualization features
python play_terminal.py --show-thinking      # Show AI candidate evaluations
python play_terminal.py --explain-strategy   # Show AI strategy explanation
python play_terminal.py --show-thinking --explain-strategy  # Both features

# Select board size:
# 1. 3×3 (Classic)
# 2. 4×4 (Challenging)
# 3. 5×5 (Hard)
```

### Web Interface (Full Experience)

```bash
cd code/projects/project_04.5_tictactoe
python web_app.py

# Open browser: http://localhost:5001/tictactoe
# Select board size from dropdown: 3×3, 4×4, 5×5
# Toggle "Show Candidate Moves" to see AI thinking
# Click AI Mode badge info icon for strategy explanation
```

### Run Tests

```bash
cd code
pytest tests/test_tictactoe.py -v

# Expected: 38 passed
```

---

## Performance Benchmarks

**First move computation time (MacBook, M-series chip):**

| Board | Depth | Nodes | Heuristic Evals | Time |
|-------|-------|-------|----------------|------|
| 3×3   | Exact | 1,513 | 0              | ~100ms |
| 4×4   | 8     | 957K  | 503K           | ~2.5s  |
| 5×5   | 4     | 187K  | 150K           | ~1.5s  |

**Cache effectiveness:**
- 3×3: ~39% hit rate (584/1513)
- 4×4: ~22% hit rate (207K/958K)
- 5×5: ~5% hit rate (10K/187K)

*Lower hit rate for larger boards due to higher branching factor and fewer repeated states*

---

## Future Extensions

### Immediate (Optional)

1. **Advanced heuristics:**
   - Pattern recognition (e.g., "fork" detection)
   - Mobility heuristic (number of legal moves)
   - Center control bonus

2. **Variable depth by position:**
   - Deeper search for critical positions (near-win states)
   - Shallower search for early game

3. **Transposition tables:**
   - Better memoization for larger boards
   - Symmetry reduction (rotations, reflections)

### Connect Four (Project 8.5, Week 31)

The same infrastructure extends naturally:
- Board: 6×7 (42 squares)
- Win: 4-in-a-row (any direction)
- Depth: 8-10 with advanced heuristic
- Challenge: Gravity constraint (pieces fall)

### Gomoku (Project 11.5, Weeks 40-41)

Further generalization:
- Board: 15×15 or 19×19
- Win: 5-in-a-row
- Depth: 4-6 + neural network value function
- Preparation for AlphaZero-Lite

---

## Key Insights

### What Worked Well

1. **Clean abstraction:**
   - Single `board_size` parameter generalizes everything
   - No code duplication between board sizes

2. **Sliding window algorithm:**
   - Simple, efficient k-in-a-row detection
   - Works for any n and k

3. **Depth-limited minimax:**
   - Makes 4×4 and 5×5 playable
   - Graceful trade-off: speed vs. strength

4. **Heuristic evaluation:**
   - Simple position scoring works surprisingly well
   - Exponential weighting (n² for n pieces) effective

### What's Challenging

1. **4×4 search time:**
   - ~2.5s for first move is noticeable
   - Could optimize with move ordering (try center first)

2. **Heuristic tuning:**
   - Current heuristic is basic (piece counting)
   - More sophisticated patterns could improve strength

3. **State space growth:**
   - 5×5 exact search completely intractable
   - Even with memoization, 430B states impossible

---

## Success Metrics

✅ **All goals met (Initial + Visualization):**

**Initial Implementation:**
- [x] Generalized game engine for n×n boards
- [x] Depth-limited minimax with heuristic evaluation
- [x] Terminal interface with board size selection
- [x] Web interface with dynamic rendering
- [x] Comprehensive tests (38/38 passing)
- [x] Performance acceptable (3×3: instant, 4×4: ~2.5s, 5×5: ~1.5s)

**Visualization Features (Added 2025-10-12):**
- [x] Terminal visualization with --show-thinking and --explain-strategy flags
- [x] Web visualization with candidate moves toggle and AI mode badge
- [x] Educational content (strategy tables, heuristic explanations, theory connections)
- [x] Natural language reasoning for move evaluations
- [x] Color-coded visual feedback in both interfaces
- [x] Performance-aware toggle controls (default: off for expensive operations)

**Time invested:**
- Initial board generalization: ~2 hours
- Visualization features: ~3 hours
- **Total**: ~5 hours

**Payoff:** Educational game framework with real-time AI thinking visualization + reusable for all future board games!

---

## Conclusion

The Tic-Tac-Toe implementation is now a **fully generalized n×n framework** that demonstrates:

1. **Theory → Practice:** Minimax as value iteration (Week 24)
2. **Scalability:** Works for boards up to 5×5+ with depth limits
3. **Production Quality:** Clean code, comprehensive tests, two interfaces
4. **Reusability:** Same architecture extends to Connect Four, Gomoku, Reversi

This upgrade transforms a toy 3×3 game into a **research-grade game-playing framework** ready for the full RL implementation roadmap (Projects 4.5 → 8.5 → 11.5 → 15 culminating in AlphaZero-Lite).

---

**Next Steps:**
- Week 5-10: Markov Chains (theory foundation)
- Week 24: Prove minimax optimality theorems
- Week 31: Extend to Connect Four (6×7 board)
- Week 42-48: AlphaZero-Lite for Reversi (neural nets + MCTS)

---

— Dr. Max Rubin
