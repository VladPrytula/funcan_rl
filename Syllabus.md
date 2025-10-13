# 48-Week Rigorous Syllabus: From Measure Theory to Reinforcement Learning

**Version**: 2.0 (Adjusted Post-Week 1)
**Date**: October 10, 2025
**Duration**: 48 weeks (90 minutes/day, Monday-Friday)
**Goal**: Rigorous mathematical foundations from measure theory through deep RL with capstone project

---

## 🔄 Adjustment Note (Version 2.0)

**Context**: After completing Week 1, it turned out that we are beyond the original plan. Week 1 covered not only all planned σ-algebra/measure content but also the complete integration theory (Lebesgue integral, MCT, Fatou, DCT) originally allocated to Week 2.

**Key Changes from v1.0**:
- **Phase I** compressed from 6 weeks → 4 weeks (Weeks 1-4)
- **Phase II** shifted to Weeks 5-10 (from 7-12)
- **Phase IX** extended from 5 weeks → 7 weeks (Weeks 42-48)
- **No content reduction**: All theorems, proofs, and exercises from v1.0 retained
- **Net savings**: 2 weeks reallocated to capstone project for robust implementation

**Rationale**: See `Pre_Week_2_Reflection_Syllabus_Adjustment.md` for complete analysis.

---

## ✨ Pedagogical Innovations

This course features **four major innovations** that distinguish it from traditional RL textbooks:

### 1. 🔍 Interactive AI Thinking Visualization

Every algorithm implementation includes **real-time visualization** of the decision-making process:

**Terminal mode:**
```bash
python play_terminal.py --show-thinking
```
Displays value functions V*(s,a) with natural language reasoning in formatted tables.

**Web interface:**
- Toggle-based overlays show candidate evaluations with color-coded values
- Green (strong position) → Yellow (neutral) → Red (weak position)
- Hover for detailed reasoning

**Example (Tic-Tac-Toe minimax):**
```
Position     Outcome          Assessment             Best
────────────────────────────────────────────────────────────
a1 (0)       ⚖️ Draw          Balanced position      ⭐ YES
b2 (4)       ⚖️ Draw          Balanced position      ⭐ YES
c3 (8)       ⚖️ Draw          Balanced position      ⭐ YES
```

**Theory bridge:** Students see Bellman optimality principle in action: π*(s) = argmax_a V*(s,a) becomes visual, not abstract.

**Impact:** Algorithms transform from "trust the formula" to "watch it work in real-time."

---

### 2. ♟️ Professional Algebraic Notation

All board games use chess-style coordinate systems (a1, b2, c3) instead of numeric indices:

**Benefits:**
- Universal standard across games (Tic-Tac-Toe → Connect Four → Gomoku → Reversi)
- Axis labels on both terminal and web interfaces
- Scales naturally to larger boards (15×15 Gomoku: a1-o15)
- Professional presentation (matches published game notation)

**Implementation:**
```python
def get_position_name(index: int, board_size: int) -> str:
    """a1, b2, c3 for 3×3; a1-d4 for 4×4"""
    row = index // board_size
    col = index % board_size
    return f"{chr(ord('a') + col)}{row + 1}"
```

**Reusable:** Built once, works for all n×n board games throughout the course.

---

### 3. 🎯 Theory-Practice Gap Transparency

Implementations honestly expose when practice diverges from theory:

**Example 1 - Tic-Tac-Toe:**
- 3×3 board: Exact optimal search (theory works perfectly, V* computable)
- 5×5 board: Depth-limited heuristic search (exact theory intractable, "good enough" practice)
- Students see: same algorithm, different computational realities

**Example 2 - Deep RL:**
- Theory (Tabular TD): Convergence guaranteed under Robbins-Monro conditions
- Practice (Neural TD): Neural networks break convergence guarantees (deadly triad)
- Students learn: Why it still works (target networks, experience replay), when it fails (Baird's counterexample)

**Philosophy:** No hand-waving. When theory and practice diverge, we say so explicitly and explain the gap.

---

### 4. 📚 Self-Contained Lab Session Appendices

Each major project includes a complete tutorial (4-7 sessions, 90 minutes each):

**Structure:**
```
Lab Session 1: [Component] (90 min)
  - Theory Recap: Connection to Week N theorems
  - Task 1.1: [Subtask] (30 min) - step-by-step code
  - Task 1.2: [Subtask] (20 min) - tests and experiments
  - Task 1.3: Verification (40 min) - exercises
```

**Content:**
- Theory recaps before each lab (bridge to Dubois's proofs)
- Complete, runnable code with explanations
- Time-calibrated tasks (each with explicit duration)
- Exercises testing understanding
- Ready for independent study or classroom use

**Total:** ~8,000 lines of tutorial content across 4 game projects (Tic-Tac-Toe, Connect Four, Gomoku, Reversi)

**Impact:** Students can work independently without instructor, following structured progression from theory to working code.

---

### Why These Matter

**Traditional RL course:**
1. Read theorem → Trust it works
2. See pseudocode → Implement yourself (often fails)
3. Debug for hours → Give up or copy solution
4. Never see "why" visually

**This course:**
1. Read theorem → See it proven (Dubois, Weeks 1-41)
2. See production code → Understand design choices (Rubin, RL implementations)
3. Run with `--show-thinking` → Watch algorithm work (visualization)
4. Play against AI → Feel optimal vs. heuristic (hands-on)

**Result:** Theory + Code + Visualization = Deep Understanding

---

## Structural Principles

### Daily Time Allocation
**Total**: 90 minutes, Monday-Friday (weekends off)

### Adaptive Weekly Template
- **Monday-Wednesday**: 40 min reading + 40 min proof/exercise + 10 min reflection note
- **Thursday**: 30 min reading + 60 min extended proof or multi-part exercise
- **Friday**: 20 min reading + 30 min proof review + 40 min coding synthesis

### Phase Structure
Nine major phases with clear mathematical and RL objectives, plus extended capstone project phase.

---

## Phase I: Measure-Theoretic Foundations (Weeks 1-4, COMPRESSED)

**Objective**: Rigorous traversal of measure theory and integration, emphasizing aspects critical for probability and RL. Compressed from original 6 weeks to 4 weeks due to Week 1 acceleration.

### ✅ Week 1: σ-Algebras, Measures, Integration, and Convergence (COMPLETED)

**Status**: Completed October 3-7, 2025

**Actual Coverage**:
- **Day 1**: σ-algebras, measurable functions, completeness, σ-finiteness
- **Day 2**: Lebesgue integral construction (simple → non-negative → general), Monotone Convergence Theorem
- **Day 3**: Fatou's Lemma, Dominated Convergence Theorem, counterexamples, RL applications
- **Day 4**: Carathéodory extension theorem (complete proof), outer measure, Lebesgue measure on ℝⁿ
- **Day 5**: Friday synthesis, discrete σ-algebra generators, observability in RL

**Content Equivalence**: Original v1.0 Weeks 1 + 2 (Days 1-3)

**Anchor Exercises** (All Completed):
1. ✅ Prove π-λ theorem
2. ✅ Show Borel σ-algebra generated by open balls
3. ✅ Complete proof of MCT with α-trick
4. ✅ Complete proof of DCT via Fatou's Lemma

**Postponed Generalizations**:
- Carathéodory extension for general metric spaces (postponed to Week 10)
- Full Birkhoff ergodic theorem (postponed to Week 9)

**Files**: `Week_1/final/Day_1_FINAL.md` through `Day_5.md`

---

### Week 2: Product Measures, Fubini, and $L^p$ Spaces Introduction

**Primary Reference**: Folland §2.4-2.5 (product measures), §6.1-6.2 ($L^p$ spaces)

**Monday-Tuesday** (90 min each):
- Product σ-algebras: construction of $\mathcal{F}_X \otimes \mathcal{F}_Y$
- Product measures: uniqueness and construction via Carathéodory
- Fubini-Tonelli theorem statement and proof strategy
- **Key insight**: Tonelli for non-negative functions, Fubini requires integrability

**Wednesday** (90 min):
- Complete proof of Tonelli theorem
- Outline of Fubini's extension to integrable functions
- Counterexamples: failure without σ-finiteness, failure without integrability

**Thursday** (90 min - extended proof session):
- $L^p(\mu)$ spaces: definition and basic properties
- Hölder's inequality (complete proof via Young's inequality)
- Minkowski's inequality (triangle inequality for $L^p$ norm)

**Friday** (90 min - synthesis):
- Review: Product measures enable trajectory space construction for MDPs
- Code: Verify Fubini numerically (compute double integral via iterated integrals)
- Code: Visualize $L^p$ unit balls in ℝ² for $p = 1, 2, \infty$
- Reflection: How does Fubini relate to computing $\mathbb{E}_{s,a}[V(s')]$ in policy evaluation?

**Anchor Exercises**:
1. Prove Tonelli theorem: if $f \geq 0$ is measurable on $X \times Y$, then iterated integrals equal
2. Construct counterexample to Fubini without σ-finiteness (counting measure on uncountable set)
3. Prove Hölder's inequality: $\|fg\|_1 \leq \|f\|_p \|g\|_q$ where $1/p + 1/q = 1$

**Content Equivalence**: Original v1.0 Week 3 (Fubini) + Week 5 (Days 1-2, $L^p$ intro)

---

### Week 3: $L^p$ Duality and Radon-Nikodym Theorem

**Primary Reference**: Folland §6.3-6.4 ($L^p$ duality), §3.1-3.4 (Radon-Nikodym)

**Monday** (90 min):
- Completeness of $L^p$ spaces: Riesz-Fischer theorem
- Proof sketch via Cauchy sequences and dominated convergence
- **Key insight**: Completeness ensures fixed-point theorems apply to Bellman operators

**Tuesday-Wednesday** (90 min each):
- Duality of $L^p$ spaces: $(L^p)^* \cong L^q$ for $1 \leq p < \infty$
- Riesz representation theorem for $(L^p)^*$ when $1 < p < \infty$
- Special cases: $(L^1)^* \cong L^\infty$ (on σ-finite spaces)
- **RL connection**: Linear value function approximation lives in $(L^2)^*$

**Thursday** (90 min - extended proof session):
- Signed measures and Hahn decomposition theorem (complete proof)
- Absolute continuity ($\mu \ll \nu$) and singularity
- Radon-Nikodym theorem statement and proof via Hilbert space projection
- **Key mechanism**: Density $d\mu/d\nu$ as "weight" function

**Friday** (90 min - synthesis):
- Review: Radon-Nikodym densities arise in importance sampling (RL off-policy methods)
- Code: Implement Radon-Nikodym density estimation for simple discrete measures
- Code: Visualize importance sampling ratios $d\pi/d\mu$ for policy gradients
- Reflection: How does chain rule for Radon-Nikodym derivatives simplify policy gradient derivations?

**Anchor Exercises**:
1. Prove Riesz-Fischer: every Cauchy sequence in $L^p$ converges
2. Prove Hahn decomposition: signed measure $\nu$ has $\nu = \nu^+ - \nu^-$ with $\nu^+ \perp \nu^-$
3. Show Radon-Nikodym chain rule: if $\mu \ll \nu \ll \lambda$, then $d\mu/d\lambda = (d\mu/d\nu)(d\nu/d\lambda)$ a.e.

**Content Equivalence**: Original v1.0 Week 5 (Days 3-5) + Week 4

---

### Week 4: Probability Spaces and Conditional Expectation

**Primary Reference**: Durrett §1.1-1.6, §5.1 (conditional expectation)

**Monday** (90 min):
- Probability spaces $(\Omega, \mathcal{F}, \mathbb{P})$ as special measure spaces
- Random variables as measurable functions
- Independence: product measures and $\sigma(\mathcal{G}) \perp \sigma(\mathcal{H})$
- **Bridge**: MDPs formalized as probability spaces over trajectory spaces

**Tuesday-Wednesday** (90 min each):
- Conditional expectation $\mathbb{E}[X | \mathcal{G}]$ as orthogonal projection in $L^2$
- Existence and uniqueness via Hilbert space projection theorem
- Properties: tower property, taking out what is known, Jensen's inequality
- **Key insight**: Bellman consistency is a tower property application

**Thursday** (90 min - extended proof session):
- Prove existence of conditional expectation via projection
- Prove tower property: $\mathbb{E}[\mathbb{E}[X|\mathcal{G}]|\mathcal{H}] = \mathbb{E}[X|\mathcal{H}]$ when $\mathcal{H} \subseteq \mathcal{G}$
- Prove $\mathbb{E}[X|\mathcal{G}]$ minimizes $\mathbb{E}[(X - Y)^2]$ over all $\mathcal{G}$-measurable $Y$

**Friday** (90 min - synthesis):
- Review: $\mathbb{E}[R|s,a]$ in MDPs is conditional expectation
- Code: Simulate conditional expectation numerically (finite state space)
- Code: Verify tower property empirically for Markov chain
- Reflection: How does conditional expectation formalize "information" in POMDPs?

**Anchor Exercises**:
1. Prove $\mathbb{E}[X|\mathcal{G}]$ minimizes mean-squared error over $\mathcal{G}$-measurable functions
2. Establish tower property for nested σ-algebras
3. Show $\mathbb{E}[f(X) | X] = f(X)$ almost surely for measurable $f$

**Content Equivalence**: Original v1.0 Week 6

**Phase I Completion Milestone**: After Week 4, all measure-theoretic foundations for probability and RL are in place. Validate via `/validate-week 4 all` before proceeding to Phase II.

---

## Phase II: Markov Chains and Ergodic Theory (Weeks 5-10, COMPRESSED)

**Objective**: Master discrete-time Markov chains on finite and countable spaces, establishing the probabilistic backbone of MDPs. Compressed from original Weeks 7-12 → Weeks 5-10.

### Week 5: Finite Markov Chains - Fundamentals

**Primary Reference**: Levin-Peres-Wilmer (LPW) Ch 1-4

**Monday-Wednesday**:
- Transition matrices $P$ and Chapman-Kolmogorov equation: $P^{n+m} = P^n P^m$
- Irreducibility, aperiodicity, and communication classes
- Stationary distributions: $\pi P = \pi$, detailed balance $\pi_i P_{ij} = \pi_j P_{ji}$

**Thursday**:
- Prove existence and uniqueness of stationary distribution for irreducible finite chains
- Use Perron-Frobenius theorem (eigenvalue 1 with positive eigenvector)

**Friday**:
- Review: Stationary distribution is "average" state visitation under policy
- Code: Random walk on graph, compute stationary distribution via eigenvalue decomposition
- Code: Verify convergence to stationarity via simulation

**Anchor Exercises**:
1. Prove irreducible finite chain has unique stationary distribution $\pi$ with $\pi_i > 0$ for all $i$
2. Show detailed balance implies $\pi$ is stationary

**Content Equivalence**: Original v1.0 Week 7

---

### Week 6: Convergence and Mixing Times

**Primary Reference**: LPW Ch 5-7, 12

**Monday-Wednesday**:
- Total variation distance: $d_{TV}(\mu, \nu) = \sup_A |\mu(A) - \nu(A)|$
- Coupling method for bounding convergence
- Mixing time: $\tau_{mix}(\epsilon) = \min\{t : d(t) \leq \epsilon\}$

**Thursday**:
- Prove coupling inequality: $d(t) \leq \mathbb{P}(\text{coupling hasn't occurred by time } t)$
- Bound mixing time via spectral gap: $\tau_{mix} \leq (\lambda_2^*)^{-1} \log(1/(\pi_{min}\epsilon))$

**Friday**:
- Review: Mixing time bounds sample complexity in RL exploration
- Code: Implement coupling for simple chain (lazy random walk on cycle)
- Code: Visualize convergence to stationarity in total variation norm

**Anchor Exercises**:
1. Compute mixing time for random walk on cycle graph $C_n$
2. Prove spectral gap bound: $\tau_{mix} = O(\lambda_2^{-1} \log(1/\pi_{min}))$ for reversible chains

**Content Equivalence**: Original v1.0 Week 8

---

### Week 7: Markov Chain Monte Carlo

**Primary Reference**: LPW Ch 8-9, 13-14

**Monday** (with 5-min bridge):
- MCMC overview: sampling from high-dimensional distributions
- **Bridge**: Why MCMC matters for RL exploration (Thompson sampling, posterior sampling)

**Tuesday-Wednesday**:
- Metropolis-Hastings algorithm and correctness proof (detailed balance)
- Gibbs sampling as special case
- Path coupling method for mixing time bounds

**Thursday**:
- Prove Metropolis-Hastings has correct stationary distribution
- Detailed balance argument: $\pi(x) P(x \to y) = \pi(y) P(y \to x)$

**Friday** (adjusted coding):
- **Core (20 min)**: Implement Metropolis-Hastings for discrete distribution sampling
- **Optional (20 min)**: Extend to 2D Ising model (if time allows)
- **Reflection note**: "We revisit MCMC in Week 32 (Thompson sampling as posterior MCMC)"

**Anchor Exercises**:
1. Design M-H algorithm to sample from $\pi(x) \propto \exp(-U(x))$ on finite space
2. Prove detailed balance for Gibbs sampler on product space

**Content Equivalence**: Original v1.0 Week 9

---

### Week 8: Countable State Spaces - Transience and Recurrence

**Primary Reference**: Durrett §6.1-6.4

**Monday-Wednesday**:
- Classification: transient vs. recurrent states
- Null recurrence vs. positive recurrence
- First passage times and hitting probabilities

**Thursday**:
- Prove Pólya's theorem: random walk on ℤ^d is recurrent iff $d \leq 2$
- Use Fourier analysis on characteristic function

**Friday**:
- Review: Recurrence structure affects RL exploration (transient states may never be revisited)
- Code: Simulate random walks in dimensions 1, 2, 3
- Code: Empirically verify recurrence/transience

**Anchor Exercises**:
1. Show $\mathbb{P}(\text{return to } 0 | \text{start at } 0) = \sum_n P_{00}^{(n)} / (1 + \sum_n P_{00}^{(n)})$
2. Prove finite state space cannot have all transient states

**Content Equivalence**: Original v1.0 Week 10

---

### Week 9: Ergodic Theorems

**Primary Reference**: Durrett §6.5-6.7, Meyn-Tweedie Ch 17

**Monday** (clear expectations):
- Ergodic theorem overview
- **Statement**: We'll prove finite-state SLLN; Birkhoff stated with intuition
- **Generalization note**: Birkhoff handles measure-preserving transformations

**Tuesday-Wednesday**:
- Strong law of large numbers for finite-state Markov chains
- Birkhoff's ergodic theorem (statement only, proof deferred)
- Application: time averages converge to spatial averages

**Thursday** (finite-state SLLN proof):
- Prove SLLN for finite irreducible positive recurrent chains
- Use coupling + DCT argument
- **Gap note**: "Full Birkhoff needed for multichain MDPs (Week 28 in original, now Week 24)"

**Friday** (numerical verification):
- Code: Verify ergodic theorem for various chains
- Code: Demonstrate failure for non-ergodic chain (multiple recurrent classes)
- **Reflection**: "Distinction between SLLN and Birkhoff matters for: (1) multichain, (2) continuous-time"

**Anchor Exercises**:
1. For irreducible positive recurrent chain, prove $(1/n)\sum_{i=1}^n f(X_i) \to \sum_x \pi_x f(x)$ a.s.
2. Construct null recurrent chain where time average exists but differs from spatial average

**Content Equivalence**: Original v1.0 Week 11

---

### Week 10: General State Spaces - Introduction

**Primary Reference**: Meyn-Tweedie Ch 3-4 (selected topics)

**Monday-Wednesday**:
- Transition kernels on general measurable spaces
- Feller property: $C_b(X) \to C_b(X)$ continuity
- Irreducibility and aperiodicity on general spaces

**Thursday**:
- Prove Feller property implies weak continuity in initial distribution
- Connection to continuity of value functions

**Friday** (concrete kernel example):
- **Example (15 min)**: Gaussian kernel on $[0,1]$ with reflection at boundaries
  - $K(x, dy) = \mathcal{N}(y; x, \sigma^2)$ with boundary reflection
  - Verify Feller property and φ-irreducibility
- Code: Implement Markov chain with this kernel, visualize density evolution

**Anchor Exercises**:
1. Define φ-irreducibility and show finite chains are φ-irreducible for counting measure φ
2. Verify Feller property for Gaussian random walk: $X_{n+1} = X_n + \varepsilon_n$, $\varepsilon_n \sim N(0, \sigma^2)$

**Content Equivalence**: Original v1.0 Week 12

**Phase II Completion Milestone**: After Week 10, Markov chain theory (finite, countable, general state spaces) is complete. Validate before proceeding to functional analysis.

---

## Phase III: Functional Analysis and Operator Theory (Weeks 11-16, COMPRESSED)

**Objective**: Establish function space framework where Bellman operators reside. Compressed from original Weeks 13-18 → Weeks 11-16.

### Week 11: Normed Spaces and Banach Spaces

**Primary Reference**: Brezis Ch 1, §1.1-1.3

**Monday-Wednesday**:
- Normed vector spaces: definition, examples ($\ell^p$, $C([0,1])$, $L^p$)
- Completeness and Banach spaces
- Finite-dimensional spaces: equivalence of norms

**Thursday**:
- Prove all norms on ℝⁿ are equivalent
- Compactness of closed bounded sets in ℝⁿ (Heine-Borel)

**Friday**:
- Review: Space $\mathcal{B}(\mathcal{S})$ of bounded functions with sup norm is Banach
- Code: Visualize unit balls in ℝ² for various norms ($L^1$, $L^2$, $L^\infty$)

**Anchor Exercises**:
1. Show $C([0,1])$ with sup norm is complete but $C([0,1])$ with $L^1$ norm is not
2. Prove every finite-dimensional normed space is complete

**Content Equivalence**: Original v1.0 Week 13

---

### Week 12: Linear Operators and Dual Spaces

**Primary Reference**: Brezis Ch 1, §1.4-1.6

**Monday-Wednesday**:
- Bounded linear operators, operator norm $\|T\| = \sup_{\|x\| \leq 1} \|Tx\|$
- Dual space $X^*$ and Hahn-Banach theorem (extension form)
- Weak and weak* topologies

**Thursday**:
- Prove Hahn-Banach theorem (geometric form: separating hyperplane)
- Applications to convex optimization

**Friday**:
- Review: Linear value functions correspond to functionals; duality in policy gradients
- Code: Implement linear functionals on finite-dimensional spaces, visualize separating hyperplanes

**Anchor Exercises**:
1. If $X$ is Banach and $T: X \to Y$ linear with closed graph, prove $T$ is bounded
2. Compute dual of $c_0$ (sequences converging to 0): $(c_0)^* \cong \ell^1$

**Content Equivalence**: Original v1.0 Week 14

---

### Week 13: Three Fundamental Theorems

**Primary Reference**: Brezis Ch 2, §2.1-2.7

**Monday-Wednesday**:
- Uniform Boundedness Principle (Banach-Steinhaus)
- Open Mapping Theorem and Inverse Mapping Theorem
- Closed Graph Theorem

**Thursday**:
- Prove Uniform Boundedness Principle via Baire category theorem
- **Key mechanism**: Complete metric space + category argument

**Friday**:
- Review: UBP implies pointwise bounded Bellman iterates are uniformly bounded
- Code: Construct example of pointwise but not uniformly bounded sequence on infinite-dimensional space

**Anchor Exercises**:
1. Use UBP: if $T_n x$ converges for each $x$, then $T = \lim T_n$ is bounded
2. Prove surjective bounded operator between Banach spaces is open

**Content Equivalence**: Original v1.0 Week 15

---

### Week 14: Hilbert Spaces

**Primary Reference**: Brezis Ch 5, §5.1-5.5

**Monday-Wednesday**:
- Inner product spaces, Cauchy-Schwarz inequality
- Orthogonality and projection theorem
- Riesz representation: $H^* \cong H$

**Thursday**:
- Prove projection theorem: every closed convex subset has unique nearest point
- Use parallelogram law and completeness

**Friday**:
- Review: Least-squares TD uses orthogonal projection in feature space
- Code: Implement orthogonal projection onto subspaces in ℝⁿ, visualize geometry

**Anchor Exercises**:
1. Prove parallelogram law characterizes inner product spaces
2. Show weak convergence + norm convergence implies strong convergence

**Content Equivalence**: Original v1.0 Week 16

---

### Week 15: Compact Operators and Spectral Theory

**Primary Reference**: Brezis Ch 6, §6.1-6.5

**Monday-Wednesday**:
- Compact operators: definition and basic properties
- Fredholm alternative
- Spectrum of bounded operators

**Thursday**:
- Prove spectral theorem for compact self-adjoint operators
- Fredholm alternative as consequence (~10 min)

**Friday**:
- Review: Bellman equation $(I - \gamma P^\pi)V = R$ as Fredholm problem
- Code: Solve Bellman via eigendecomposition (20 min)
- Code: Verify spectral theorem numerically for discrete Laplacian (20 min)

**Anchor Exercises**:
1. Show composition of bounded with compact is compact
2. For compact self-adjoint $T$, prove $Tx = \lambda x$ iff $\lambda$ is eigenvalue

**Content Equivalence**: Original v1.0 Week 17

---

### Week 16: Contraction Mappings and Fixed Points

**Primary Reference**: Brezis Ch 9, §9.1-9.3; Puterman Appendix A

**Monday-Wednesday**:
- Metric spaces and completeness review
- Banach Fixed Point Theorem (complete proof)
- Applications to differential and integral equations

**Thursday**:
- Prove Banach Fixed Point with explicit convergence rate
- Error bound: $d(x_n, x^*) \leq L^n d(x_0, x^*)/(1-L)$

**Friday**:
- Review: Bellman operator $T^\pi$ is γ-contraction in $L^\infty$
- Code: Visualize fixed point iteration for various contractions, demonstrate linear convergence

**Anchor Exercises**:
1. Prove error bound for contraction iteration
2. Show non-expansive map on compact metric space has fixed point

**Content Equivalence**: Original v1.0 Week 18

**Phase III Completion Milestone**: After Week 16, functional analysis foundations complete. Ready for Sobolev spaces and PDEs.

---

## Phase IV: Sobolev Spaces, PDEs, and Control Theory (Weeks 17-22)

**Objective**: Deep exploration of Sobolev spaces and variational methods, connecting to HJB equations and continuous control.

### Week 17: Weak Derivatives and Sobolev Spaces $W^{k,p}$

**Primary Reference**: Brezis Ch 8, §8.1-8.3

**Content**: (Same as original v1.0 Week 19)

**Anchor Exercises**:
1. Show trace operator is well-defined on $W^{1,p}(\Omega)$ for bounded Lipschitz $\Omega$
2. Prove density of $C_c^\infty(\Omega)$ in $W^{1,p}(\Omega)$

---

### Week 18: Sobolev Embeddings and Compactness

**Primary Reference**: Brezis Ch 9, §9.1-9.4

**Content**: (Same as original v1.0 Week 20)

---

### Week 19: Variational Formulations and Weak Solutions

**Primary Reference**: Brezis Ch 8, §8.4-8.6; Ch 9, §9.5

**Content**: (Same as original v1.0 Week 21)

---

### Week 20: Hamilton-Jacobi Equations and Viscosity Solutions

**Primary Reference**: Bardi-Capuzzo Dolcetta Ch 1-2

**Content**: (Same as original v1.0 Week 22)

---

### Week 21: Viscosity Solutions - Theory

**Primary Reference**: Bardi-Capuzzo Dolcetta Ch 3-4

**Content**: (Same as original v1.0 Week 23)

---

### Week 22: Optimal Control and HJB in Continuous Time

**Primary Reference**: Yong-Zhou Ch 3-4

**Content**: (Same as original v1.0 Week 24)

---

## Phase V: Markov Decision Processes and Dynamic Programming (Weeks 23-26)

**Objective**: Rigorous MDP theory where all prior mathematics pays dividends.

### Week 23: MDP Formalism and Bellman Equations

**Primary Reference**: Puterman Ch 3-4, Bertsekas Vol I Ch 1-2

**Content**: (Same as original v1.0 Week 25)

---

### Week 24: Optimal Policies and Value Iteration

**Primary Reference**: Puterman Ch 6, Bertsekas Vol I Ch 1

**Content**: (Same as original v1.0 Week 26)

---

### Week 25: Policy Iteration and Linear Programming

**Primary Reference**: Puterman Ch 6-7

**Content**: (Same as original v1.0 Week 27)

---

### Week 26: Average Reward MDPs and Ergodic Theory

**Primary Reference**: Puterman Ch 8, Meyn-Tweedie Ch 17

**Content**: (Same as original v1.0 Week 28)

---

## Phase VI: Bandit Algorithms (Weeks 27-31)

**Objective**: Systematic treatment of multi-armed bandits and exploration-exploitation.

### Weeks 27-31: (Same content as original v1.0 Weeks 29-33)

- Week 27: Multi-Armed Bandits - Regret Framework
- Week 28: UCB Algorithms and Optimism
- Week 29: Thompson Sampling and Bayesian Bandits
- Week 30: Contextual Bandits and Linear Models
- Week 31: Advanced Topics in Bandits (Adversarial, Structured)

---

## Phase VII: Stochastic Approximation and RL Algorithms (Weeks 32-37)

**Objective**: Rigorous convergence theory for TD learning via stochastic approximation.

### Stochastic Approximation Hygiene Checklist

(Same as original v1.0)

### Weeks 32-37: (Same content as original v1.0 Weeks 34-39)

- Week 32: Robbins-Monro and Stochastic Approximation
- Week 33: ODE Method for Stochastic Approximation
- Week 34: Temporal Difference Learning - Tabular Case
- Week 35: TD with Function Approximation - Linear Case
- Week 36: Q-Learning and Off-Policy Learning
- Week 37: Policy Gradient Methods

---

## Phase VIII: Advanced Topics and Continuous-Time Control (Weeks 38-41)

**Objective**: Connect to continuous-time formulations and modern deep RL.

### Weeks 38-41: (Same content as original v1.0 Weeks 40-43)

- Week 38: Continuous-Time MDPs and HJB Revisited
- Week 39: Mean-Field Games and Multi-Agent RL
- Week 40: Deep RL Theory - Approximation and Generalization
- Week 41: Synthesis - From Theory to Practice

---

## Phase IX: Capstone Project (Weeks 42-48, EXTENDED)

**Objective**: Implement sophisticated RL project demonstrating mastery of theory and practice.

**Extension Rationale**: 2 weeks saved from Phase I compression reallocated here for robust implementation and thorough evaluation.

### Project: AlphaZero-Lite for Reversi (Othello)

### Weeks 42-43: Environment and MCTS Implementation

**Monday-Wednesday**:
- Implement Reversi game engine with optimized board representation
- Monte Carlo Tree Search from first principles
- UCT formula and exploration-exploitation balance

**Thursday**:
- Prove UCT satisfies "regret minimization" property (connection to bandit theory)
- Relate to UCB algorithm from Week 27

**Friday**:
- Integrate and test MCTS on random play
- Performance benchmarking

**Deliverable**: Fully functional MCTS player defeating random play

---

### Weeks 44-45: Neural Network Policy-Value Architecture

**Monday-Wednesday**:
- Design convolutional architecture for 8×8 board evaluation
- ResNet blocks for spatial feature extraction
- Dual-head architecture: policy head (action probabilities) + value head (position evaluation)
- Self-play data generation pipeline

**Thursday**:
- Implement training loop with mini-batch SGD
- Loss function: policy cross-entropy + value MSE + L2 regularization

**Friday**:
- Test trained network as MCTS evaluation function
- Ablation: pure network vs. pure MCTS vs. hybrid

**Deliverable**: Trained network improving MCTS play strength

---

### Week 46: Self-Play and Training Iteration

**Monday-Wednesday**:
- Self-play loop: generate games using current best model
- Data augmentation: board rotations and reflections (8-fold symmetry)
- Training: update network on self-play buffer
- Model selection: arena tournament to select best checkpoint

**Thursday**:
- Implement ELO rating system for model comparison
- Track training metrics: policy entropy, value accuracy, game length

**Friday**:
- Run extended self-play session (overnight if needed)
- Analyze learning curves and convergence

**Deliverable**: Self-improving agent via iterative training

---

### Week 47: Ablation Studies and Evaluation

**Monday-Tuesday**:
- **Ablation 1**: MCTS simulation count (100 vs. 400 vs. 1600 sims/move)
- **Ablation 2**: Network architecture (depth, width, ResNet blocks)
- **Ablation 3**: Training hyperparameters (learning rate, batch size, L2 penalty)

**Wednesday-Thursday**:
- Tournament evaluation: AlphaZero-lite vs. baselines
  - Random play
  - Pure MCTS (no neural network)
  - Greedy policy network (no search)
  - Human player (you!)
- Compute ELO ratings for all agents

**Friday**:
- Analyze failure modes: positions where agent blunders
- Visualize learned policy and value landscapes

**Deliverable**: Comprehensive evaluation with ELO ratings and ablation results

---

### Week 48: Technical Report and Final Presentation

**Monday-Wednesday**:
- Write 15-page technical report connecting implementation to theory:
  - **Section 1**: MDP formulation of Reversi (state space, action space, transition dynamics)
  - **Section 2**: MCTS as UCB on game tree (bandit theory from Week 27)
  - **Section 3**: Policy-value network as function approximation ($L^2$ projection from Week 14)
  - **Section 4**: Self-play as approximate policy iteration (Week 25)
  - **Section 5**: Experimental results and ablations
  - **Section 6**: Connections to frontier research (MuZero, AlphaZero variants)

**Thursday**:
- Prepare slides for final presentation (20 minutes + 10 min Q&A)
- Rehearse presentation, anticipate questions

**Friday**:
- Final presentation
- Reflect on 48-week journey: mathematical insights, RL applications, future directions

**Final Deliverable**:
1. Complete codebase on GitHub (with README, requirements.txt, trained model checkpoints)
2. 15-page technical report (LaTeX, publication-ready)
3. 20-minute presentation (slides + demo)
4. Trained AlphaZero-lite model defeating baselines

---

## Daily Reflection Protocol

(Same as original v1.0)

---

## Postponed Generalizations Log

(Same as original v1.0, updated as needed)

---

## Reference Library Organization

(Same as original v1.0)

---

## Critical Checklists

(Same as original v1.0)

---

## Phase Overview Summary (Adjusted)

| Phase | Weeks | Original | Content | Key Milestone |
|-------|-------|----------|---------|---------------|
| **I: Measure Theory** | 1-4 | 1-6 | σ-algebras, integration, $L^p$, conditional expectation | Product measures + DCT |
| **II: Markov Chains** | 5-10 | 7-12 | Finite, countable, general state spaces, ergodic theory | Birkhoff theorem + Feller property |
| **III: Functional Analysis** | 11-16 | 13-18 | Banach, Hilbert, compact operators, contractions | Spectral theorem + Banach fixed-point |
| **IV: Sobolev + PDEs** | 17-22 | 19-24 | Weak derivatives, embeddings, HJB, viscosity solutions | Lax-Milgram + viscosity uniqueness |
| **V: MDPs** | 23-26 | 25-28 | MDP formalism, value/policy iteration, average reward | Bellman optimality + contraction |
| **VI: Bandits** | 27-31 | 29-33 | MAB, UCB, Thompson, contextual, adversarial | UCB regret bound + LinUCB |
| **VII: Stochastic Approx** | 32-37 | 34-39 | Robbins-Monro, ODE method, TD, Q-learning, policy gradient | ODE tracking + convergence |
| **VIII: Advanced Topics** | 38-41 | 40-43 | Continuous-time, mean-field, deep RL theory, synthesis | HJB continuous-time |
| **IX: Capstone** | 42-48 | 44-48 | AlphaZero-lite: MCTS + neural nets + self-play | Fully functional agent |

**Net Compression**: 6 weeks saved (Phases I-II), 2 weeks reallocated to Phase IX.

---

## Meta-Cognitive Strategies

(Same as original v1.0)

---

## Notes for Claude Code

(Same as original v1.0, plus):

**Adjusted Syllabus Awareness**:
- When generating content for Week N, consult this v2.0 Syllabus (not v1.0)
- Cross-reference week numbers carefully (e.g., "Week 27" in v2.0 = "Week 29" in v1.0)
- If uncertain, check `Pre_Week_2_Reflection_Syllabus_Adjustment.md` for mapping

---

## Git Workflow

(Same as original v1.0)

---

**End of Adjusted Syllabus v2.0**

*Version 2.0 - Adjusted post-Week 1 to reflect accelerated pace*
*Total duration: 48 weeks × 5 days × 90 minutes = 360 hours (unchanged)*
*Prepared for: Rigorous journey from measure theory to deep reinforcement learning*
*Next review: End of Week 4 (Post-Phase I validation)*
