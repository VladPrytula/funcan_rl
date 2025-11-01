# Tic-Tac-Toe Quick Start

Two ways to play against optimal AI:

## 🖥️ Terminal Version (Recommended for Hackers)

```bash
cd code/projects/project_04.5_tictactoe
python play_terminal.py                      # Standard gameplay
python play_terminal.py --show-thinking      # Show AI candidate evaluations
python play_terminal.py --explain-strategy   # Show AI strategy explanation
```

**Clean. Fast. Pure.**

**New Visualization Features**:
- `--show-thinking`: See V*(s,a) for all moves (demonstrates Bellman optimality)
- `--explain-strategy`: Educational explanations of AI strategy
- Live statistics display during AI thinking
- Color-coded candidate evaluations (green = strong, red = weak)

---

## 🌐 Web Version (For Demos & Students)

```bash
cd code/projects/project_04.5_tictactoe
python web_app.py
```

Open browser: **http://localhost:5001/tictactoe**

**Port options**:
- Default: 5001 (avoids macOS AirPlay on 5000)
- Custom: `python web_app.py --port 8080`

**Features**:
- Click to play (no typing!)
- Beautiful gradient UI
- Real-time search stats
- Winning line animations
- Responsive (mobile-friendly)

**New Visualization Features**:
- **Show Candidate Moves** toggle: See AI's evaluation of all legal moves
- **AI Mode Badge**: Explains "Optimal" (3×3) vs "Strong" (4×4+) with hover tooltip
- **Color-coded move values**: Green → strong, Yellow → neutral, Red → weak
- **Educational content**: Expandable sections explaining heuristics, theory connections
- **Strategy comparison table**: Compares 3×3, 4×4, 5×5 search strategies
- **Live statistics**: Nodes explored, cache hits, heuristic evaluations, compute time

---

## The AI Never Loses

**Theory**: Minimax proves Tic-Tac-Toe is a draw under optimal play.

Try to win. You can't. Best you can do is draw. 🎮

---

**More info**: See [README.md](README.md) for full documentation.
