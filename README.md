# From Measure Theory to AlphaZero
## A Rigorous 48-Week Journey Connecting Functional Analysis and Reinforcement Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Progress](https://img.shields.io/badge/Progress-Week%201-green.svg)](Syllabus.md)
[![Study Plan](https://img.shields.io/badge/Study%20Plan-48%20Weeks-orange.svg)](Syllabus.md)

---

## 🎯 **Vision**

**Can you build AlphaZero from first principles?**

Not by importing libraries—but by constructing the complete mathematical foundations: σ-algebras → Banach spaces → Markov chains → MDPs → stochastic approximation → deep RL theory.

This repository documents a **48-week odyssey** from Folland and Brezis to self-play game AI, proving every theorem needed along the way.

### A Personal Note

After many years in industry, building systems and shipping products, I felt a deepening urge to return to something I'd set aside: the **eternal beauty of pure mathematics**. Not as an escape from applicability—but as a way to understand *why* the tools we use actually work.

This journey reconnects two worlds I've lived in: the rigorous abstractions that captivated me during my PhD, and the practical algorithms that power modern AI. It's a bridge built in both directions—honoring the elegance of mathematical structure while never forgetting that these theorems exist because real problems demanded them.

**Target audience:** Anyone who feels this same pull—researchers with strong mathematical background (physics, pure math, engineering) who want to _truly understand_ reinforcement learning, not just run it. Those who've spent years in applied work but hunger for the deeper "why."

---

## 🗺️ **The Mathematical Journey**

### Visual Roadmap

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHASE I: MEASURE THEORY (Weeks 1-6)                  │
│  σ-algebras → Integration → Lᵖ Spaces → Conditional Expectation         │
└─────────────────────────────┬───────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
┌──────────────────────────┐    ┌────────────────────────────────┐
│  PHASE II: MARKOV CHAINS │    │  PHASE III: FUNCTIONAL ANALYSIS│
│     (Weeks 7-12)         │    │        (Weeks 13-18)           │
│  Chains → Ergodic Theory │    │  Banach → Operators → Fixed Pt │
│  MCMC → General Spaces   │    │  Spectral → Semigroups         │
└────────────┬─────────────┘    └───────────┬────────────────────┘
             │                              │
             └──────────────┬───────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │   PHASE IV: SOBOLEV & PDEs  │
              │      (Weeks 19-24)          │
              │  Weak Derivatives → HJB     │
              │  Lax-Milgram → Viscosity    │
              └──────────┬──────────────────┘
                         │
            ┌────────────┴─────────────┐
            │                          │
            ▼                          ▼
┌───────────────────────┐    ┌──────────────────────────┐
│  PHASE V: MDPs        │    │  PHASE VI: BANDITS       │
│   (Weeks 25-28)       │    │   (Weeks 29-33)          │
│  Bellman → Value Iter │    │  Regret → UCB            │
│  Policy Iter → Avg Rwd│    │  Thompson → Contextual   │
└──────────┬────────────┘    └────────┬─────────────────┘
           │                          │
           └──────────┬───────────────┘
                      │
                      ▼
        ┌─────────────────────────────────────┐
        │  PHASE VII: STOCHASTIC APPROX       │
        │        (Weeks 34-39)                │
        │  Robbins-Monro → ODE Method         │
        │  TD Learning → Q-learning → PG      │
        └────────────────┬────────────────────┘
                         │
                         ▼
        ┌─────────────────────────────────────┐
        │  PHASE VIII: ADVANCED TOPICS        │
        │        (Weeks 40-43)                │
        │  Continuous MDPs → Mean-Field       │
        │  Deep RL Theory → Synthesis         │
        └────────────────┬────────────────────┘
                         │
                         ▼
        ┌─────────────────────────────────────┐
        │  🎯 PHASE IX: ALPHAZERO CAPSTONE    │
        │        (Weeks 44-48)                │
        │  MCTS → Neural Nets → Self-Play     │
        │  Implementation → Analysis          │
        └─────────────────────────────────────┘
```

**Key Connections:**
- **Measure Theory** → Probability foundations for MDPs
- **Markov Chains** → Policy evaluation, exploration
- **Functional Analysis** → Value function spaces, Bellman operators
- **Sobolev/PDEs** → Continuous control, HJB equations
- **MDPs** → Formal RL framework
- **Bandits** → Exploration-exploitation
- **Stochastic Approximation** → All RL algorithms (TD, Q-learning, PG)
- **Deep RL Theory** → Neural function approximation
- **AlphaZero** → Theory meets practice

---

## 📚 **What This Is**

A **textbook in the making**, written in real-time as daily study notes transform into publication-quality exposition.

**Three commitments:**

1. **Rigor without compromise:** Every theorem proven, every definition precise, counterexamples for necessity
2. **RL as the North Star:** Every abstraction justified by its necessity in reinforcement learning
3. **Realistic constraints:** 90-minute daily target (up to 2.5 hours for dense material), weekends completely off

**Not another tutorial.** A bridge between:
- **Bourbaki's architectural vision** (build from the ground up)
- **Brezis's pedagogical clarity** (rigorous but readable)
- **DeepMind's algorithmic practice** (code that runs at frontier labs)

---

## ✨ **What Makes This Different**

Unlike traditional RL courses that separate theory from practice, this journey features **four features** that bridge the gap:

### 1. 🔍 **See Algorithms Think in Real-Time**

Every implementation includes **interactive visualization** of AI decision-making:

**Terminal:**
```bash
python play_terminal.py --show-thinking

🤔 AI CANDIDATE EVALUATIONS
Position     Outcome          Assessment             Best
────────────────────────────────────────────────────────────
a1 (0)       ⚖️ Draw          Balanced position      ⭐ YES
b2 (4)       ⚖️ Draw          Balanced position      ⭐ YES
...
```

**Web:** Toggle "Show Candidate Moves" to see color-coded value overlays (green = strong, red = weak)

**Impact:** You don't just learn "π*(s) = argmax_a V*(s,a)" — you watch the algorithm evaluate every move and choose the best one.

---

### 2. ♟️ **Professional Standards from Day One**

All board games use algebraic notation (a1, b2, c3) — the universal language of board games:
- Same coordinate system as chess, Go, Connect Four
- Works for any board size (3×3 → 15×15 Gomoku)
- Industry-standard presentation (portfolio-ready demos)

**Why it matters:** "Play a1" vs. "Play position 0" — one is professional, one is toy example.

---

### 3. 🎯 **Honest About Where Theory Fails**

When practice diverges from theory, we show you both and explain the gap:

**Example:**
- **Theory says:** TD(0) converges to V* (tabular case, Robbins-Monro conditions)
- **Practice needs:** Target networks + experience replay (neural networks break guarantees)
- **We show you:** Baird's counterexample (when it fails), DQN tricks (why it still works)

**No hand-waving. No "it just works."** If theory and practice diverge, you'll know exactly why.

---

### 4. 📚 **Complete Tutorials for Every Project**

Each major implementation ships with a Lab Session Appendix (4-7 sessions, 90 min each):
- Theory recaps connecting to course material
- Step-by-step code (complete, runnable, explained)
- Time-calibrated tasks (know exactly how long each part takes)
- Ready for self-study (no instructor needed)

**Total:** ~8,000 lines of tutorial content across game projects

**Example:** Tic-Tac-Toe Lab Appendix (1600 lines)
- Lab 1: Game environment (90 min)
- Lab 2: Minimax solver (90 min)
- Lab 3: Terminal interface (60 min)
- Lab 4: Web interface (90 min)

---

### **The Learning Experience**

**Traditional RL course:** Read theory → Run library code → Never really understand

**This course:** Prove theory → Build from scratch → See it work → Play against it

**Concrete example:**

You won't just implement minimax. You'll:
1. Prove it computes V* correctly (Week 24 theory)
2. Build it with α-β pruning and memoization (production code)
3. Visualize it with `--show-thinking` (watch it evaluate all moves)
4. Play against it in browser (try to beat optimal AI — spoiler: you can't!)

**Result:** Deep understanding you can't get from lectures or library code alone.

---

## 🗺️ **The Journey (48 Weeks)**

### **Phase I: Measure-Theoretic Foundations** (Weeks 1-6)
*Why RL needs $\sigma$-algebras*

- Measure spaces, $\sigma$--algebras, Carathéodory extension
- Integration: monotone/dominated convergence, Fubini/Tonelli
- Lᵖ spaces: completeness, duality, density
- Conditional expectation (RL: transition kernels, expectations)

**Key RL Connection:** Probability measures on state-action spaces, observability

---

### **Phase II: Markov Chains & Ergodic Theory** (Weeks 7-12)
*From random walks to mixing times*

- Finite/countable chains: classification, stationary distributions
- Convergence theorems: coupling, total variation
- MCMC: Metropolis-Hastings, Gibbs sampling
- General state spaces: drift conditions, small sets

**Key RL Connection:** Exploration in MDPs, policy evaluation, on-policy/off-policy learning

---

### **Phase III: Functional Analysis & Operators** (Weeks 13-18)
*The structure of value function spaces*

- Banach/Hilbert spaces: dual spaces, weak convergence
- Compact operators, spectral theory
- Contraction mappings: Banach fixed-point theorem
- Semigroups and generators

**Key RL Connection:** Bellman operators, value iteration, policy iteration, contractive properties

---

### **Phase IV: Sobolev Spaces, PDEs, & Control** (Weeks 19-24)
*From HJB equations to viscosity solutions*

- Weak derivatives, Sobolev embeddings
- Lax-Milgram theorem, variational formulations
- Hamilton-Jacobi-Bellman equations
- Viscosity solutions for optimal control

**Key RL Connection:** Continuous control, actor-critic methods, maximum principle

---

### **Phase V: Markov Decision Processes** (Weeks 25-28)
*The formal language of sequential decision-making*

- MDP formalism: state/action spaces, transition kernels, rewards
- Bellman equations: optimality, uniqueness
- Value iteration, policy iteration: convergence theory
- Average reward MDPs, multichain case

**Key RL Connection:** Foundation for all RL algorithms

---

### **Phase VI: Bandit Algorithms** (Weeks 29-33)
*Exploration-exploitation from first principles*

- Multi-armed bandits: regret framework, lower bounds
- UCB family: analysis and variants
- Thompson Sampling: Bayesian perspective
- Contextual bandits: LinUCB, neural bandits

**Key RL Connection:** Exploration in RL, credit assignment, reward shaping

---

### **Phase VII: Stochastic Approximation & RL Algorithms** (Weeks 34-39)
*The ODE method and convergence theory*

- Robbins-Monro: step sizes, martingale analysis
- ODE method: Borkar's framework
- TD learning: TD(0), TD(λ), convergence proofs
- Q-learning: off-policy learning, deadly triad
- Policy gradients: REINFORCE, actor-critic, natural gradients

**Key RL Connection:** Every modern RL algorithm is stochastic approximation

---

### **Phase VIII: Advanced Topics** (Weeks 40-43)
*Frontiers and synthesis*

- Continuous-time MDPs, jump processes
- Mean-field games and multi-agent RL
- Deep RL theory: NTK perspective, approximation error
- Integration: what we've built and why it matters

**Key RL Connection:** Research frontier, open problems

---

### **Phase IX: Capstone—AlphaZero for Reversi** (Weeks 44-48)
*Theory meets practice*

- Monte Carlo Tree Search: UCT, PUCT
- Neural network policy-value approximation
- Self-play training loop
- Implementation, debugging, performance analysis
- Final reflection: 48 weeks in retrospect

**Deliverable:** Working AlphaZero-lite implementation with complete mathematical provenance

---

## 🏗️ **Repository Structure**

```
Study/
├── README.md                    # This file
├── Syllabus.md                  # Complete 48-week plan (canonical source)
├── Week 1/                      # Weekly study materials
│   ├── Day 1.md                # Polished textbook sections
│   ├── Day 2.md
│   ├── Day 3.md
│   ├── Day 1 exercises.md      # Exercise solutions
│   └── ...
├── Week 2/
└── ...
```

---

## 🎓 **Philosophical Commitments**

### **1. Rigor ≠ Inaccessibility**

*"Rigorous does not mean impenetrable."* — Haïm Brezis

- State theorems with full generality
- Prove in illuminating special cases when pedagogy demands
- Every abstraction is motivated by a concrete RL challenge

### **2. No Orphaned Mathematics**

Every theorem answers: **Why do we need this for RL?**

Examples:
- σ-algebras → observability in MDPs, defining transition kernels
- Banach fixed-point → value iteration convergence
- Dominated convergence → policy gradient interchange

### **3. Code as Proof of Concept**

Every Friday: computational experiments verifying theory
- JAX for autodiff, PyTorch for neural nets
- Production-grade considerations (stability, complexity)
- References to frontier implementations (CleanRL, Stable-Baselines3)

### **4. Intellectual Honesty**

- **Postponed Generalizations Log:** When time constraints force simplifications, we document what's postponed and why
- **Time Constraints:** Target 90 minutes/day, acceptable up to 2.5 hours—over that, we split content
- **Gap Acknowledgment:** Where theory and practice diverge, we say so explicitly

---

## 📖 **Reference Library**

### Tier 1 (Weekly Use)
- Folland, *Real Analysis*
- Brezis, *Functional Analysis, Sobolev Spaces and PDEs*
- Puterman, *Markov Decision Processes*
- Lattimore & Szepesvári, *Bandit Algorithms*

### Tier 2 (Regular Reference)
- Durrett, *Probability: Theory and Examples*
- Levin, Peres & Wilmer, *Markov Chains and Mixing Times*
- Borkar, *Stochastic Approximation: A Dynamical Systems Viewpoint*
- Bertsekas, *Reinforcement Learning and Optimal Control*

### Tier 3 (Specialized Topics)
- Meyn & Tweedie, *Markov Chains and Stochastic Stability*
- Yong & Zhou, *Stochastic Controls*
- Bardi & Capuzzo-Dolcetta, *Optimal Control and Viscosity Solutions*
- Sutton & Barto, *Reinforcement Learning* (narrative guide)

---

## 🚀 **For Newcomers**

### **To follow this journey**

1. Start with [Syllabus.md](Syllabus.md) for the complete 48-week plan
2. Read [Week 1/Day 1.md](Week%201/Day%201.md) to see textbook quality


### **To adapt this for my own study**

1. Fork this repository
2. Modify [Syllabus.md](Syllabus.md) with your schedule/topics
3. Follow the review workflow: create → review → revise → validate

### **To contribute or provide feedback**

- Open an issue for mathematical errors, typos, or pedagogical suggestions
- Discussions on RL connections, alternative proofs, or frontier references welcome
- This is a learning journey—honest feedback improves the final textbook

---

## 🧭 **Roadmap**

- [x] Week 1: σ-algebras, measures, Carathéodory extension
- [x] Week 1: Integration theory, convergence theorems
- [x] Week 2: $L^p$ spaces, completeness, duality
- [ ] Week 3: Product measures, Fubini, Tonelli
- [ ] Week 4: Signed measures, Radon-Nikodym, conditional expectation
- [ ] ...
- [ ] Week 48: AlphaZero-lite for Reversi complete

**Progress tracking:** See [Syllabus.md](Syllabus.md) for detailed week-by-week status

---

## 📝 **Daily Workflow Philosophy**

**Monday–Wednesday (40+40+10 min):**
- 40 min: Reading from primary sources
- 40 min: Proof work or exercises
- 10 min: Reflection and RL connection

**Thursday (30+60 min):**
- 30 min: Reading
- 60 min: Extended proof (key theorem of the week)

**Friday (20+30+40 min):**
- 20 min: Reading
- 30 min: Proof review
- 40 min: Code synthesis (numerical experiments)
- End with: Weekly reflection (Mathematical Insight, RL Connection, Open Questions)

**Weekends:** Completely off (sustainability over speed)

---

## 🏆 **Ultimate Deliverable**

By Week 48, this repository will contain:

1. **A complete textbook** bridging pure analysis and RL (potentially publishable)
2. **~240 polished sections** (5 days × 48 weeks) with proofs and code
3. **A working AlphaZero implementation** built from scratch with full mathematical provenance
4. **A library of RL algorithms** (TD, Q-learning, policy gradients, bandits) with convergence proofs
5. **A model for self-directed mathematical study** combining rigor and realistic time constraints

**The Legacy:** A resource cited in PhD theses, used by practitioners who want to understand *why* RL works, not just *how* to run it.

---

## 📜 **License**

MIT License - See [LICENSE](LICENSE) for details

**Citation:**
```bibtex
@misc{measure-to-alphazero-2025,
  author = {Vladyslav Prytula},
  title = {From Measure Theory to AlphaZero: A 48-Week Journey},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/VladPrytula/funcan_rl}
}
```

---

## 🙏 **Acknowledgments**

**Inspired by:**
- Nicolas Bourbaki's *Éléments de mathématique* (architectural vision)
- Haïm Brezis's *Functional Analysis* (pedagogical clarity)
- Jacques-Louis Lions's *Optimal Control* (applied depth)
- The frontier RL community (DeepMind, OpenAI, Berkeley, FAIR)
- All my friends, colleagues, and senseis during my university, PhD, and postdoc years—from Ukraine, Spain, France, Norway, Portugal, and all over the world—whose passion for rigorous mathematics and honest intellectual pursuit shaped this journey

**Built with:**
- [Obsidian](https://obsidian.md) for markdown-based knowledge management
- [Claude Code](https://claude.ai/code) for AI-assisted code generation and review
---

## 💬 **Contact & Discussion**

- **Issues:** Mathematical errors, typos, suggestions
- **Discussions:** RL connections, alternative proofs, pedagogy
- **Pull Requests:** Corrections welcome (especially for mathematical errors)

**Remember:** This is a learning journey in public. Mistakes are expected—corrections are celebrated.

---

## 🌐 **Online Textbook (online)**

The content will be published as a GitHub Pages site for easier reading:
- **Searchable textbook format** (searchable across all weeks)
- **Better LaTeX rendering** (optimized for web)
- **Navigation by phase/week/day**
- **Downloadable PDF versions**

Preview URL (once live): `https://github.com/VladPrytula/funcan_rl.git`

---

## 📋 **Quick Start for Your Own Journey**

Want to adapt this workflow for your own study plan? Here's how:

### **Step 1: Fork the Repository**
```bash
git clone https://github.com/VladPrytula/funcan_rl.git
cd funcan_rl
```

### **Step 2: Customize Syllabus**
Edit `Syllabus.md` with your topics, timeline, and reading assignments.

---

**Status:** Week 2 completed | Next milestone: Week 6 (Measure Theory complete)

*Last updated: 2025-01-08*
