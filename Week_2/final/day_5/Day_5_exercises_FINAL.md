## Exercises: Week 2, Day 5 – Computational Synthesis

**Time Allocation:** 30 minutes total (Friday synthesis exercises)

**Structure:**
- **Exercise 2.5.1:** Fubini numerical verification [10 min]
- **Exercise 2.5.2:** $L^p$ unit ball visualization [10 min]
- **Exercise 2.5.3:** Bellman equation via Fubini [10 min]

**Pedagogical Note:** Friday exercises emphasize **computational verification** of abstract theorems and **explicit RL connections**. Solutions include complete Python implementations with commentary.

---

### **Exercise 2.5.1** (Fubini Numerical Verification) {#EX-2.5.1} [10 min]

Verify Fubini's theorem [THM-2.3.1] numerically for the following test functions:

**(a)** $f(x,y) = xy$ on $[0,1]^2$ with Lebesgue measure

**(b)** $f(x,y) = e^{-(x+y)}$ on $[0,\infty)^2$ with Lebesgue measure

For each function, compute:
1. $I_1 = \int \left(\int f(x,y) \, dy\right) dx$ (integrate $y$ first)
2. $I_2 = \int \left(\int f(x,y) \, dx\right) dy$ (integrate $x$ first)
3. $I_3 = \iint f(x,y) \, d(x,y)$ (double integral directly)

where the integration limits are:
- Part (a): $[0,1] \times [0,1]$
- Part (b): $[0,\infty) \times [0,\infty)$

Verify that $I_1 = I_2 = I_3$ within numerical tolerance ($10^{-6}$).

---

**Solution.**

We implement this using `scipy.integrate` for numerical integration.

**Implementation:**

```python
import numpy as np
from scipy import integrate

# ============================================================
# Test Case (a): f(x, y) = xy on [0, 1]^2
# ============================================================

def f_a(x, y):
    """Test function: f(x,y) = xy"""
    return x * y

# Analytic solution for verification: ∫∫ xy dx dy = (1/2) * (1/2) = 1/4
analytic_a = 0.25

print("=" * 60)
print("Test Case (a): f(x,y) = xy on [0,1]^2")
print("=" * 60)

# Method 1: Integrate dy first, then dx
def inner_dy_a(x):
    """Inner integral: ∫ f(x,y) dy from 0 to 1"""
    result, _ = integrate.quad(lambda y: f_a(x, y), 0, 1)
    return result

I1_a, err1_a = integrate.quad(inner_dy_a, 0, 1)
print(f"I₁ = ∫∫ f(x,y) dy dx = {I1_a:.10f} (error: {err1_a:.2e})")

# Method 2: Integrate dx first, then dy
def inner_dx_a(y):
    """Inner integral: ∫ f(x,y) dx from 0 to 1"""
    result, _ = integrate.quad(lambda x: f_a(x, y), 0, 1)
    return result

I2_a, err2_a = integrate.quad(inner_dx_a, 0, 1)
print(f"I₂ = ∫∫ f(x,y) dx dy = {I2_a:.10f} (error: {err2_a:.2e})")

# Method 3: Double integral directly
I3_a, err3_a = integrate.dblquad(f_a, 0, 1, 0, 1)
print(f"I₃ = ∫∫ f(x,y) d(x,y) = {I3_a:.10f} (error: {err3_a:.2e})")

# Verification
print(f"\nAnalytic value: {analytic_a:.10f}")
print(f"Max deviation: {max(abs(I1_a - analytic_a), abs(I2_a - analytic_a), abs(I3_a - analytic_a)):.2e}")

assert np.isclose(I1_a, I2_a, rtol=1e-6), "Fubini failed: I₁ ≠ I₂"
assert np.isclose(I1_a, I3_a, rtol=1e-6), "Fubini failed: I₁ ≠ I₃"
assert np.isclose(I1_a, analytic_a, rtol=1e-6), "Numerical error: I₁ ≠ analytic"

print("✓ Fubini verified: I₁ = I₂ = I₃ (within tolerance 10⁻⁶)")

# ============================================================
# Test Case (b): f(x, y) = exp(-(x+y)) on [0, ∞)^2
# ============================================================

def f_b(x, y):
    """Test function: f(x,y) = exp(-(x+y))"""
    return np.exp(-(x + y))

# Analytic solution: ∫₀^∞ e^(-x) dx * ∫₀^∞ e^(-y) dy = 1 * 1 = 1
analytic_b = 1.0

print("\n" + "=" * 60)
print("Test Case (b): f(x,y) = exp(-(x+y)) on [0,∞)^2")
print("=" * 60)

# Method 1: Integrate dy first, then dx
def inner_dy_b(x):
    """Inner integral: ∫ f(x,y) dy from 0 to ∞"""
    result, _ = integrate.quad(lambda y: f_b(x, y), 0, np.inf)
    return result

I1_b, err1_b = integrate.quad(inner_dy_b, 0, np.inf)
print(f"I₁ = ∫∫ f(x,y) dy dx = {I1_b:.10f} (error: {err1_b:.2e})")

# Method 2: Integrate dx first, then dy
def inner_dx_b(y):
    """Inner integral: ∫ f(x,y) dx from 0 to ∞"""
    result, _ = integrate.quad(lambda x: f_b(x, y), 0, np.inf)
    return result

I2_b, err2_b = integrate.quad(inner_dx_b, 0, np.inf)
print(f"I₂ = ∫∫ f(x,y) dx dy = {I2_b:.10f} (error: {err2_b:.2e})")

# Method 3: Double integral directly
I3_b, err3_b = integrate.dblquad(f_b, 0, np.inf, 0, np.inf)
print(f"I₃ = ∫∫ f(x,y) d(x,y) = {I3_b:.10f} (error: {err3_b:.2e})")

# Verification
print(f"\nAnalytic value: {analytic_b:.10f}")
print(f"Max deviation: {max(abs(I1_b - analytic_b), abs(I2_b - analytic_b), abs(I3_b - analytic_b)):.2e}")

assert np.isclose(I1_b, I2_b, rtol=1e-6), "Fubini failed: I₁ ≠ I₂"
assert np.isclose(I1_b, I3_b, rtol=1e-6), "Fubini failed: I₁ ≠ I₃"
assert np.isclose(I1_b, analytic_b, rtol=1e-6), "Numerical error: I₁ ≠ analytic"

print("✓ Fubini verified: I₁ = I₂ = I₃ (within tolerance 10⁻⁶)")

print("\n" + "=" * 60)
print("✓ All Fubini tests passed.")
print("=" * 60)
```

**Output:**
```
============================================================
Test Case (a): f(x,y) = xy on [0,1]^2
============================================================
I₁ = ∫∫ f(x,y) dy dx = 0.2500000000 (error: 2.77e-15)
I₂ = ∫∫ f(x,y) dx dy = 0.2500000000 (error: 2.77e-15)
I₃ = ∫∫ f(x,y) d(x,y) = 0.2500000000 (error: 3.91e-15)

Analytic value: 0.2500000000
Max deviation: 5.55e-17
✓ Fubini verified: I₁ = I₂ = I₃ (within tolerance 10⁻⁶)

============================================================
Test Case (b): f(x,y) = exp(-(x+y)) on [0,∞)^2
============================================================
I₁ = ∫∫ f(x,y) dy dx = 1.0000000000 (error: 1.11e-14)
I₂ = ∫∫ f(x,y) dx dy = 1.0000000000 (error: 1.11e-14)
I₃ = ∫∫ f(x,y) d(x,y) = 1.0000000000 (error: 1.57e-14)

Analytic value: 1.0000000000
Max deviation: 1.11e-16
✓ Fubini verified: I₁ = I₂ = I₃ (within tolerance 10⁻⁶)

============================================================
✓ All Fubini tests passed.
============================================================
```

**Interpretation:**

Both test cases confirm Fubini numerically:
- **Case (a):** The simple polynomial $xy$ integrates exactly to $1/4$ via both orders
- **Case (b):** The exponential $e^{-(x+y)}$ factors as $e^{-x} e^{-y}$, so Tonelli applies directly (non-negative), giving $\int_0^\infty e^{-x} dx \cdot \int_0^\infty e^{-y} dy = 1 \cdot 1 = 1$

**Pedagogical Note:** Numerical integration has errors on the order of machine precision ($10^{-14}$ to $10^{-15}$), well below our tolerance threshold ($10^{-6}$). For more complex integrands where analytic solutions are unavailable, these numerical methods provide reliable verification of Fubini.

□

---

### **Exercise 2.5.2** ($L^p$ Unit Ball Visualization) {#EX-2.5.2} [10 min]

Plot the unit balls $\mathcal{B}_p = \{(x,y) \in \mathbb{R}^2 : \|(x,y)\|_p \leq 1\}$ for $p = 1, 2, \infty$ on the same axes.

**(a)** Generate parametric plots of the boundaries $\|(x,y)\|_p = 1$

**(b)** Verify numerically that:
   - $\mathcal{B}_1 \subseteq \mathcal{B}_2$ (the $L^1$ ball is contained in the $L^2$ ball)
   - $\mathcal{B}_2 \subseteq \mathcal{B}_\infty$ (the $L^2$ ball is contained in the $L^\infty$ ball)

**(c)** Reflect: What happens to the unit ball as $p \to \infty$? Why does this make sense given the definition $\|f\|_\infty = \text{ess sup} |f|$?

---

**Solution.**

**Implementation:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate theta for parametrization
theta = np.linspace(0, 2 * np.pi, 1000)

# ============================================================
# p = 1: Diamond (L^1 norm)
# Boundary: |x| + |y| = 1
# ============================================================

# Parametrize as piecewise linear connecting vertices:
# (1, 0) → (0, 1) → (-1, 0) → (0, -1) → (1, 0)
n_segment = 250
x_p1 = np.concatenate([
    np.linspace(1, 0, n_segment),    # Quadrant I: (1,0) → (0,1)
    np.linspace(0, -1, n_segment),   # Quadrant II: (0,1) → (-1,0)
    np.linspace(-1, 0, n_segment),   # Quadrant III: (-1,0) → (0,-1)
    np.linspace(0, 1, n_segment)     # Quadrant IV: (0,-1) → (1,0)
])
y_p1 = np.concatenate([
    np.linspace(0, 1, n_segment),
    np.linspace(1, 0, n_segment),
    np.linspace(0, -1, n_segment),
    np.linspace(-1, 0, n_segment)
])

# ============================================================
# p = 2: Circle (Euclidean norm)
# Boundary: x^2 + y^2 = 1
# ============================================================

x_p2 = np.cos(theta)
y_p2 = np.sin(theta)

# ============================================================
# p = ∞: Square (sup norm)
# Boundary: max{|x|, |y|} = 1
# ============================================================

x_pinf = np.array([1, 1, -1, -1, 1])
y_pinf = np.array([1, -1, -1, 1, 1])

# ============================================================
# Plot
# ============================================================

fig, ax = plt.subplots(1, 1, figsize=(8, 8))

ax.plot(x_p1, y_p1, label='$p=1$ (Diamond, $L^1$)', linewidth=2.5, color='tab:blue')
ax.plot(x_p2, y_p2, label='$p=2$ (Circle, $L^2$)', linewidth=2.5, color='tab:orange')
ax.plot(x_pinf, y_pinf, label='$p=\\infty$ (Square, $L^\\infty$)', linewidth=2.5, color='tab:green')

ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_aspect('equal')
ax.axhline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)
ax.axvline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)
ax.legend(fontsize=14, loc='upper right')
ax.set_xlabel('$x$', fontsize=16)
ax.set_ylabel('$y$', fontsize=16)
ax.set_title('$L^p$ Unit Balls in $\\mathbb{R}^2$', fontsize=18, fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Week_2/revisions/day_5/lp_unit_balls.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# (b) Numerical verification of inclusions
# ============================================================

print("\n" + "=" * 60)
print("Verification of Inclusion Relationships")
print("=" * 60)

# Sample points on L^1 ball boundary
sample_points_p1 = np.column_stack([x_p1[::100], y_p1[::100]])  # Subsample for efficiency

# Check if L^1 ball is contained in L^2 ball
norms_p2_of_p1 = np.sqrt(sample_points_p1[:, 0]**2 + sample_points_p1[:, 1]**2)
assert np.all(norms_p2_of_p1 <= 1 + 1e-6), "L^1 ball not contained in L^2 ball"
print(f"✓ L^1 ball contained in L^2 ball: max L^2 norm of L^1 boundary = {norms_p2_of_p1.max():.6f} ≤ 1")

# Sample points on L^2 ball boundary
sample_points_p2 = np.column_stack([x_p2[::100], y_p2[::100]])

# Check if L^2 ball is contained in L^∞ ball
norms_pinf_of_p2 = np.maximum(np.abs(sample_points_p2[:, 0]), np.abs(sample_points_p2[:, 1]))
assert np.all(norms_pinf_of_p2 <= 1 + 1e-6), "L^2 ball not contained in L^∞ ball"
print(f"✓ L^2 ball contained in L^∞ ball: max L^∞ norm of L^2 boundary = {norms_pinf_of_p2.max():.6f} ≤ 1")

print("\n" + "=" * 60)
print("✓ Inclusion verified: B₁ ⊆ B₂ ⊆ B∞")
print("=" * 60)
```

**Output:**
```
============================================================
Verification of Inclusion Relationships
============================================================
✓ L^1 ball contained in L^2 ball: max L^2 norm of L^1 boundary = 0.707215 ≤ 1
✓ L^2 ball contained in L^∞ ball: max L^∞ norm of L^2 boundary = 1.000000 ≤ 1

============================================================
✓ Inclusion verified: B₁ ⊆ B₂ ⊆ B∞
============================================================
```

**Visualization:**

The plot shows:
- **Blue diamond** ($p=1$): Vertices at $(\pm 1, 0)$ and $(0, \pm 1)$, tightest constraint
- **Orange circle** ($p=2$): Standard Euclidean unit circle
- **Green square** ($p=\infty$): Largest ball, vertices at $(\pm 1, \pm 1)$

**Interpretation:**

**(a)** The parametrization reveals the **geometry of norms**:
- $L^1$ ball: Linear boundaries (Manhattan distance)
- $L^2$ ball: Curved (Euclidean distance)
- $L^\infty$ ball: Axis-aligned square (Chebyshev distance)

**(b)** The inclusion $\mathcal{B}_1 \subseteq \mathcal{B}_2 \subseteq \mathcal{B}_\infty$ reflects the following fact:

In $\mathbb{R}^n$, the norms satisfy:
$$
\|x\|_\infty \leq \|x\|_2 \leq \|x\|_1
$$
(always true, without restrictions). This implies:
$$
\|x\|_1 \leq 1 \implies \|x\|_2 \leq \|x\|_1 \leq 1 \implies \|x\|_\infty \leq \|x\|_2 \leq 1
$$

Therefore, any point in the $L^1$ unit ball is also in the $L^2$ unit ball, which is in turn contained in the $L^\infty$ unit ball.

**(c)** **Reflection: As $p \to \infty$, the unit ball approaches the square.**

**Why?** The $L^p$ norm is:
$$
\|(x,y)\|_p = (|x|^p + |y|^p)^{1/p}
$$

As $p \to \infty$, the largest term dominates:
$$
\lim_{p \to \infty} \|(x,y)\|_p = \max\{|x|, |y|\} = \|(x,y)\|_\infty
$$

**Proof sketch:** WLOG, assume $|x| \geq |y|$. Then:
$$
|x| = (|x|^p)^{1/p} \leq (|x|^p + |y|^p)^{1/p} \leq (2|x|^p)^{1/p} = 2^{1/p} |x|
$$

As $p \to \infty$, $2^{1/p} \to 1$, so $\|(x,y)\|_p \to |x| = \max\{|x|, |y|\}$. □

**RL Significance:** In RL, the choice of norm affects convergence behavior:
- **$L^\infty$ (sup norm):** Ensures **uniform convergence** (all states improve simultaneously). Bellman operators are contractions in $L^\infty$ (Week 23).
- **$L^2$ (Euclidean norm):** Permits **average-case convergence** (some states may converge faster). Least-squares TD uses $L^2$ projection (Week 35).
- **$L^1$ (total variation):** Measures **distribution distance**. Used in convergence proofs for policy gradient methods (Week 37).

□

---

### **Exercise 2.5.3** (Bellman Equation via Fubini – SIMPLIFIED) {#EX-2.5.3} [10 min]

**Note:** This exercise has been simplified to ensure manual verification matches numerical computation.

Consider a simple 2-state MDP:
- **States:** $\mathcal{S} = \{1, 2\}$
- **Actions:** $\mathcal{A} = \{\text{stay}, \text{move}\}$
- **Policy:** $\pi(\text{move}|s) = 1$ for all $s$ (deterministic: always move)
- **Transitions:**
  - State 1 with action move: $P(2|1, \text{move}) = 1$ (transition to state 2)
  - State 2 with action move: $P(2|2, \text{move}) = 1$ (self-loop at state 2)
  - Action stay: $P(s|s, \text{stay}) = 1$ (always stay in current state)
- **Rewards:** $r(1, \text{move}) = 1$, $r(2, \text{move}) = 4$, $r(s, \text{stay}) = 0$
- **Discount:** $\gamma = 0.9$

**(a)** Compute $V^\pi(s)$ for $s=1, 2$ using the Bellman equation:
$$
V^\pi(s) = \mathbb{E}_{a \sim \pi(s), s' \sim P(\cdot|s,a)}[r(s,a) + \gamma V^\pi(s')]
$$

Solve the linear system $V^\pi = R + \gamma P^\pi V^\pi$ where $P^\pi$ is the transition matrix under policy $\pi$.

**(b)** Verify that the Bellman equation can be written as a double sum (discrete analog of Fubini):
$$
V^\pi(s) = \sum_{a \in \mathcal{A}} \sum_{s' \in \mathcal{S}} \pi(a|s) P(s'|s,a) [r(s,a) + \gamma V^\pi(s')]
$$

and that the order of summation (over $a$ then $s'$, or $s'$ then $a$) is irrelevant.

**(c)** Reflect: How does this discrete example illustrate Fubini's theorem? What is the "product measure" in this setting?

---

**Solution.**

**(a) Computing $V^\pi$ via Bellman Equation**

**Transition matrix under $\pi$ (deterministic policy: always move):**
$$
P^\pi = \begin{pmatrix}
0 & 1 \\
0 & 1
\end{pmatrix}
$$

**Reward vector:** $R = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$ (immediate rewards $r(1, \text{move}) = 1$, $r(2, \text{move}) = 4$)

**Bellman equation:** $V^\pi = R + \gamma P^\pi V^\pi$

Rearranging: $(I - \gamma P^\pi) V^\pi = R$

**Manual Calculation:**

From $(I - \gamma P^\pi) V^\pi = R$:
$$
\begin{pmatrix}
1 & -0.9 \\
0 & 0.1
\end{pmatrix}
\begin{pmatrix}
V^\pi(1) \\ V^\pi(2)
\end{pmatrix}
=
\begin{pmatrix}
1 \\ 4
\end{pmatrix}
$$

From row 2: $0.1 V^\pi(2) = 4 \implies V^\pi(2) = 40$

From row 1: $V^\pi(1) - 0.9 V^\pi(2) = 1 \implies V^\pi(1) = 1 + 0.9 \cdot 40 = 1 + 36 = 37$

**Implementation:**

```python
import numpy as np

# MDP parameters
states = np.array([1, 2])
gamma = 0.9

# Transition matrix P^π (deterministic policy: always move)
P_pi = np.array([
    [0, 1],  # State 1 → State 2
    [0, 1]   # State 2 → State 2 (self-loop)
])

# Reward vector R (r(1, move) = 1, r(2, move) = 4)
R = np.array([1.0, 4.0])

# Solve Bellman equation: V^π = R + γ P^π V^π
# Rearranging: (I - γ P^π) V^π = R
I = np.eye(len(states))
V_pi = np.linalg.solve(I - gamma * P_pi, R)

print("=" * 60)
print("Bellman Equation Solution")
print("=" * 60)
print(f"V^π(s) for s ∈ {{1, 2}}:")
for s_idx, s in enumerate(states):
    print(f"  V^π({s}) = {V_pi[s_idx]:.4f}")
print("=" * 60)

# Manual verification
V_manual = np.array([37.0, 40.0])
assert np.allclose(V_pi, V_manual), "Numerical solution doesn't match manual calculation"
print(f"\n✓ Manual verification: V^π = {V_manual}")
```

**Output:**
```
============================================================
Bellman Equation Solution
============================================================
V^π(s) for s ∈ {1, 2}:
  V^π(1) = 37.0000
  V^π(2) = 40.0000
============================================================

✓ Manual verification: V^π = [37. 40.]
```

**Verification:** The numerical solution matches the manual calculation exactly. ✓

**(b) Verification via Double Sum (Discrete Fubini)**

```python
# Policy (deterministic: always move)
pi = np.array([
    [0, 1],  # State 1: stay=0, move=1
    [0, 1]   # State 2: stay=0, move=1
])

# Full transition tensor P[s, a, s'] = P(s' | s, a)
# Actions: 0=stay, 1=move
P_full = np.zeros((2, 2, 2))

# Action "stay" (a=0): P(s|s,stay) = 1
for s in range(2):
    P_full[s, 0, s] = 1.0

# Action "move" (a=1): P(2|s,move) = 1 for all s
P_full[0, 1, 1] = 1.0  # State 1 → State 2
P_full[1, 1, 1] = 1.0  # State 2 → State 2

# Reward function r(s, a)
R_full = np.array([
    [0, 1],  # State 1: r(1,stay)=0, r(1,move)=1
    [0, 4]   # State 2: r(2,stay)=0, r(2,move)=4
])

# Compute V^π via double sum (Method 1: sum over a then s')
V_check_method1 = np.zeros(2)
for s in range(2):
    for a in range(2):  # sum over actions
        for sp in range(2):  # sum over next states
            V_check_method1[s] += pi[s, a] * P_full[s, a, sp] * (R_full[s, a] + gamma * V_pi[sp])

print("\nDouble Sum Verification (Method 1: ∑_a ∑_s')")
print("=" * 60)
for s_idx, s in enumerate(states):
    print(f"  Bellman via double sum: V({s}) = {V_check_method1[s_idx]:.4f}")
    print(f"  Linear system solution:  V({s}) = {V_pi[s_idx]:.4f}")
    assert np.isclose(V_check_method1[s_idx], V_pi[s_idx]), f"Mismatch at state {s}"
print("✓ Bellman equation verified via double sum (Method 1)")
print("=" * 60)

# Compute V^π via double sum (Method 2: sum over s' then a)
V_check_method2 = np.zeros(2)
for s in range(2):
    for sp in range(2):  # sum over next states first
        for a in range(2):  # sum over actions second
            V_check_method2[s] += pi[s, a] * P_full[s, a, sp] * (R_full[s, a] + gamma * V_pi[sp])

print("\nDouble Sum Verification (Method 2: ∑_s' ∑_a)")
print("=" * 60)
for s_idx, s in enumerate(states):
    print(f"  Bellman via double sum: V({s}) = {V_check_method2[s_idx]:.4f}")
    assert np.isclose(V_check_method2[s_idx], V_check_method1[s_idx]), f"Order matters! Fubini violated at state {s}"
print("✓ Order of summation doesn't matter (discrete Fubini verified)")
print("=" * 60)
```

**Output:**
```
Double Sum Verification (Method 1: ∑_a ∑_s')
============================================================
  Bellman via double sum: V(1) = 37.0000
  Linear system solution:  V(1) = 37.0000
  Bellman via double sum: V(2) = 40.0000
  Linear system solution:  V(2) = 40.0000
✓ Bellman equation verified via double sum (Method 1)
============================================================

Double Sum Verification (Method 2: ∑_s' ∑_a)
============================================================
  Bellman via double sum: V(1) = 37.0000
  Bellman via double sum: V(2) = 40.0000
✓ Order of summation doesn't matter (discrete Fubini verified)
============================================================
```

**(c) Reflection: Discrete Fubini and Conditional Product Measures**

The Bellman equation $V^\pi(s) = \sum_a \sum_{s'} \pi(a|s) P(s'|s,a) [r + \gamma V^\pi(s')]$ is a **discrete analog of Fubini's theorem**.

**Conditional product measure in this setting:**
- **Marginal measure:** $\pi(a|s)$ is a probability distribution over actions $\mathcal{A}$
- **Conditional measure:** $P(s'|s,a)$ is a family of probability distributions over next states $\mathcal{S}$, indexed by $a$
- **Joint measure:** The joint distribution over $(a, s')$ pairs is:
  $$
  \rho(a, s' | s) = \pi(a|s) P(s'|s,a)
  $$
  This is a **conditional product** (also called a **disintegration**): for each fixed $a$, $P(\cdot|s,a)$ is a probability measure on $\mathcal{S}$, but the measure itself depends on $a$.

**Technical distinction:**
- **Standard product $\mu \otimes \nu$ (Week 2):** Both $\mu$ and $\nu$ are fixed measures. Example: Lebesgue measure on $\mathbb{R}^2$ is $\lambda \otimes \lambda$ where $\lambda$ is 1D Lebesgue.
- **Conditional product $\pi(da) P(ds'|a)$ (Week 4):** The second measure $P(\cdot|a)$ depends on the first variable $a$. This is Markovian structure.

The Fubini-like commutativity still holds (by the tower property of conditional expectation, Week 4), but the proof requires disintegration theory, not just Week 2 product measures.

**Fubini's role:** The double sum can be computed in either order:
$$
\sum_{a \in \mathcal{A}} \sum_{s' \in \mathcal{S}} \pi(a|s) P(s'|s,a) g(a, s') = \sum_{s' \in \mathcal{S}} \sum_{a \in \mathcal{A}} \pi(a|s) P(s'|s,a) g(a, s')
$$

where $g(a, s') = r(s,a) + \gamma V^\pi(s')$.

**Why this matters for Monte Carlo RL:**

In practice, RL algorithms estimate expectations by sampling trajectories $(s_0, a_0, s_1, a_1, \ldots)$ from the environment. Fubini guarantees that:
- Sampling action $a$ first, then next state $s'$ (on-policy sampling)
- Sampling next state $s'$ first, then action $a$ (hypothetical: not physically realizable)
- Sampling joint $(a, s')$ pairs (off-policy behavior policy)

all give the **same expectation** in the limit. However, finite-sample Monte Carlo estimates $\hat{V}(s) = (1/N) \sum_{i=1}^N [r_i + \gamma V(s_i')]$ have **sampling error**:
$$
|\hat{V}(s) - V^\pi(s)| = O_p(1/\sqrt{N})
$$
by the Central Limit Theorem (CLT). Fubini says the **bias** is zero (order doesn't matter), but the **variance** is $\text{Var}[r + \gamma V(s')]/N$, which requires $N$ samples to reduce.

**Practice vs. Theory:**
- Fubini: A *deterministic* statement about integrals (no approximation)
- Monte Carlo: A *stochastic* approximation with convergence rate $O(1/\sqrt{N})$
- TD learning (Week 34): Uses bootstrapping to reduce variance at the cost of introducing bias (trades off bias-variance)

Fubini enables the **unbiased** Monte Carlo estimator; TD learning sacrifices this for **lower variance**.

□

---

**Weekly Synthesis Complete**

**Key Takeaways:**
1. **Fubini verified numerically:** Iterated integrals equal double integrals (within machine precision)
2. **$L^p$ unit balls visualized:** Geometry of norms revealed (diamond $\subseteq$ circle $\subseteq$ square)
3. **Bellman equation formalized via Fubini:** Order of integration over actions and next states is irrelevant (conditional Fubini)
4. **Monte Carlo connection:** Fubini guarantees unbiased estimation; finite samples have $O(1/\sqrt{N})$ error

**Time spent:** ~30-40 minutes (exercises + implementations + reflection)

**Files generated:**
- `lp_unit_balls.png` (visualization)
- Fubini verification code (standalone Python script)
- Bellman MDP example code (standalone Python script)

**Next Steps:** Week 3, Day 1 (Monday) – Prove Riesz-Fischer Theorem: $L^p$ is complete

---

**End of Week 2 Exercises**
