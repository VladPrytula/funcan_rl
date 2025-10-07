### Agenda:

##### 📘 Day 2 – Week 1: The Lebesgue Integral and Monotone Convergence
**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (40 min) – Reading**

**Topic:** _Construction of the Lebesgue integral and convergence theorems_

- Read from **Folland, "Real Analysis" §2.1–2.2** or equivalent in Durrett Ch.2.
- Focus on:
    - Construction pathway: simple functions → non-negative measurable → general measurable
    - Monotone Convergence Theorem (MCT) statement and proof strategy
    - Why integration must be built in stages
- _Key takeaway:_ The Lebesgue integral extends to functions too irregular for Riemann integration, enabling rigorous treatment of expectations in RL.

---

#### **⏱️ Segment 2 (40 min) – Proof/Exercise**  

**Exercise:**
Prove the Monotone Convergence Theorem completely, including all technical details.

**Hints:**
- Step 1: Measurability of the limit function
- Step 2: Easy direction using monotonicity of integral
- Step 3: Hard direction via α-trick with simple functions
- Step 4: Reflect on where monotonicity was essential

---

#### **⏱️ Segment 3 (10 min) – Coding / Reflection**

**Micro-coding task:**
Verify MCT numerically with a sequence of functions converging monotonically.

**Conceptual bridge to RL:**
- MCT justifies computing expectations via limits in value iteration
- When value functions converge monotonically, integration and limit commute
- Essential for proving convergence of policy evaluation algorithms

---

📅 Tomorrow (Day 3): **Fatou's Lemma and Dominated Convergence Theorem**, establishing the full convergence hierarchy.

---

### **Chapter 1: Foundations in Measure and Probability Theory**

#### **1.3 The Lebesgue Integral: From Simple Functions to Expectation Operators**

**Motivation:** In reinforcement learning, the central object of study is not a deterministic quantity, but an **expectation**—the average return under a stochastic policy in a stochastic environment. The mathematical formalization of expectation is the integral with respect to a probability measure. Before we can rigorously define the expected return $\mathbb{E}^{\pi}[G_t]$, or the value function $V^{\pi}(s) = \mathbb{E}^{\pi}[\sum_{k=0}^{\infty} \gamma^k R_{t+k} | S_t = s]$, we must construct a theory of integration that can handle:

1. **Discontinuous functions**: Indicator functions of sets (which correspond to events in our probability space) are not Riemann integrable on arbitrary measurable sets.
2. **Unbounded domains**: State spaces in continuous control are often $\mathbb{R}^n$, which has infinite Lebesgue measure.
3. **Interchange of limits and integrals**: Algorithms like value iteration produce sequences of value functions $V_n \to V^*$. We need theorems guaranteeing $\mathbb{E}[V_n] \to \mathbb{E}[V^*]$ under appropriate conditions.

The Riemann integral, defined via partitions of the domain, is inadequate for these tasks. The **Lebesgue integral**, constructed by partitioning the range rather than the domain, is the correct analytical tool. This section develops the Lebesgue integral from first principles, culminating in the **Monotone Convergence Theorem**—the first and most fundamental result enabling interchange of limits and integrals.

**Learning Objectives:**
* Understand the three-stage construction: simple functions → non-negative functions → general functions
* Appreciate why measurability is prerequisite for integration
* Master the Monotone Convergence Theorem and its proof technique (the α-trick)
* Recognize MCT as the foundation for proving convergence of value iteration

---

### **I. Core Theory: The Construction Hierarchy**

The Lebesgue integral is defined through a careful bootstrap procedure. We begin with the simplest class of functions—those taking only finitely many values—and extend systematically.

#### **A. Simple Functions: The Foundation**

**Definition 1.9 (Simple Function).** Let $(X, \mathcal{F}, \mu)$ be a measure space. A function $\varphi: X \to \mathbb{R}$ is **simple** if it takes only finitely many distinct values and is measurable. Equivalently, $\varphi$ can be written in the canonical form:
$$
\varphi(x) = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}(x)
$$
where $a_1, \ldots, a_n \in \mathbb{R}$ are distinct, $A_i = \{x : \varphi(x) = a_i\} \in \mathcal{F}$, and the sets $\{A_i\}$ form a partition of $X$.

**Definition 1.10 (Integral of Simple Functions).** For a non-negative simple function $\varphi = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}$ with $a_i \geq 0$, we define:
$$
\int \varphi \, d\mu = \sum_{i=1}^{n} a_i \mu(A_i)
$$
where the convention $0 \cdot \infty = 0$ is adopted.

**Remark 1.2 (Well-Definedness).** The integral is independent of the representation of $\varphi$. If $\varphi = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i} = \sum_{j=1}^{m} b_j \mathbf{1}_{B_j}$ are two representations, then by considering the common refinement $\{A_i \cap B_j\}$, one can verify that both sums yield the same value.

**Proposition 1.6 (Properties of the Integral on Simple Functions).**
Let $\varphi, \psi$ be non-negative simple functions, and $c \geq 0$ a constant. Then:
1. **(Linearity)** $\int (c\varphi + \psi) \, d\mu = c \int \varphi \, d\mu + \int \psi \, d\mu$
2. **(Monotonicity)** If $\varphi \leq \psi$ pointwise, then $\int \varphi \, d\mu \leq \int \psi \, d\mu$
3. **(Countable Additivity on Domain)** If $\{A_n\}$ are disjoint measurable sets, then:
   $$
   \int_{\bigcup A_n} \varphi \, d\mu = \sum_{n=1}^{\infty} \int_{A_n} \varphi \, d\mu
   $$

*Proof.* These properties follow directly from the definition and the corresponding properties of measures. For linearity, use the common refinement technique. For countable additivity, use the countable additivity of $\mu$ itself. $\square$

#### **B. Non-Negative Measurable Functions: Extension by Supremum**

Having defined integration for simple functions, we extend to all non-negative measurable functions via a supremum construction.

**Definition 1.11 (Integral of Non-Negative Functions).** Let $f: X \to [0, \infty]$ be a measurable function. We define:
$$
\int f \, d\mu = \sup \left\{ \int \varphi \, d\mu \mid 0 \leq \varphi \leq f, \, \varphi \text{ simple} \right\}
$$

**Remark 1.3 (Geometric Intuition).** The integral of $f$ is the "area under the curve" computed by approximating $f$ from below with increasingly fine step functions. Unlike the Riemann integral, which partitions the domain into intervals, the Lebesgue approach partitions the **range** of $f$ into levels, measuring the sets $\{x : f(x) > t\}$ for each $t \geq 0$.

**Proposition 1.7 (Extension of Properties to Non-Negative Functions).**
For measurable $f, g: X \to [0, \infty]$ and $c \geq 0$:
1. **(Linearity)** $\int (cf + g) \, d\mu = c \int f \, d\mu + \int g \, d\mu$
2. **(Monotonicity)** If $f \leq g$ a.e., then $\int f \, d\mu \leq \int g \, d\mu$
3. **(Countable Additivity)** If $\{A_n\}$ are disjoint in $\mathcal{F}$, then:
   $$
   \int_{\bigcup A_n} f \, d\mu = \sum_{n=1}^{\infty} \int_{A_n} f \, d\mu
   $$

*Proof.* Each property is established by approximating $f$ and $g$ from below with simple functions and using the corresponding property for simple functions. The supremum operation preserves these relations. The details are standard and can be found in Folland §2.2. $\square$

#### **C. General Measurable Functions: Decomposition into Positive and Negative Parts**

To integrate functions that take both positive and negative values, we decompose them into positive and negative components.

**Definition 1.12 (Positive and Negative Parts).** For a measurable function $f: X \to \mathbb{R}$, define:
$$
f^+(x) = \max\{f(x), 0\}, \qquad f^-(x) = \max\{-f(x), 0\}
$$
Then $f = f^+ - f^-$ and $|f| = f^+ + f^-$. Both $f^+$ and $f^-$ are non-negative measurable functions.

**Definition 1.13 (Integral of General Functions).** A measurable function $f: X \to \mathbb{R}$ is **integrable** (or **Lebesgue integrable**) if $\int |f| \, d\mu < \infty$. For such $f$, we define:
$$
\int f \, d\mu = \int f^+ \, d\mu - \int f^- \, d\mu
$$
Since both $\int f^+ \, d\mu$ and $\int f^- \, d\mu$ are finite, this difference is well-defined.

**Notation.** We write $f \in L^1(\mu)$ to denote that $f$ is integrable. The space $L^1(\mu)$ is the collection of all (equivalence classes of) integrable functions, where two functions are identified if they differ only on a set of measure zero.

**Remark 1.4 (Why Integrability Requires Finiteness).** If $\int f^+ \, d\mu = \int f^- \, d\mu = \infty$, the difference $\infty - \infty$ is undefined. This motivates the restriction to functions with $\int |f| \, d\mu < \infty$.

---

### **II. The Monotone Convergence Theorem: Guaranteeing Limit-Integral Interchange**

The power of the Lebesgue integral lies in its robust convergence theorems. The **Monotone Convergence Theorem** is the cornerstone.

**Theorem 1.2 (Monotone Convergence Theorem – Beppo Levi).** Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^{\infty}$ be a sequence of measurable functions satisfying:
1. **(Non-negativity)** $f_n \geq 0$ for all $n$
2. **(Monotonicity)** $f_1 \leq f_2 \leq f_3 \leq \cdots$ pointwise (i.e., $f_n(x) \leq f_{n+1}(x)$ for all $x \in X$)
3. **(Pointwise convergence)** $f_n(x) \to f(x)$ for all $x \in X$

Then $f$ is measurable and:
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu
$$
In other words, **the integral of the limit equals the limit of the integrals**.

**Remark 1.5 (Significance).** This theorem is remarkable because it requires no domination hypothesis. The sequence $\{f_n\}$ may converge to a function with infinite integral, and the theorem remains valid. The conclusion $\lim \int f_n = \int (\lim f_n)$ is the foundation for all subsequent convergence results in integration theory.

*Proof.* (Detailed proof provided in Day_2_exercises.md) $\square$

**Corollary 1.1 (Countable Additivity of the Integral).** Let $\{g_n\}$ be a sequence of non-negative measurable functions. Then:
$$
\int \left( \sum_{n=1}^{\infty} g_n \right) d\mu = \sum_{n=1}^{\infty} \int g_n \, d\mu
$$

*Proof.* Apply MCT to the partial sums $f_N = \sum_{n=1}^{N} g_n$, which form a monotone increasing sequence converging to $\sum_{n=1}^{\infty} g_n$. $\square$

---

### **III. Computational Illustration: Verifying MCT Numerically**

To build intuition for the Monotone Convergence Theorem, we construct a concrete sequence of functions and verify numerically that the limit of integrals equals the integral of the limit.

**Example 1.3 (A Monotonically Converging Sequence).** Consider the functions on $[0,1]$:
$$
f_n(x) = x(1 - e^{-nx}), \qquad n = 1, 2, 3, \ldots
$$

**Properties:**
1. Each $f_n$ is continuous and non-negative on $[0,1]$
2. For fixed $x \in (0,1]$: $e^{-nx} \to 0$ as $n \to \infty$, so $f_n(x) \to x$
3. Monotonicity: Since $e^{-nx}$ is decreasing in $n$, we have $f_n(x) \leq f_{n+1}(x)$

The limit function is $f(x) = x$, which has integral $\int_0^1 x \, dx = 1/2$.

Each $f_n$ has integral:
$$
\int_0^1 x(1 - e^{-nx}) \, dx = \int_0^1 x \, dx - \int_0^1 x e^{-nx} \, dx
$$

The first integral is $1/2$. For the second, integration by parts gives:
$$
\int_0^1 x e^{-nx} \, dx = \left[-\frac{x e^{-nx}}{n}\right]_0^1 + \frac{1}{n}\int_0^1 e^{-nx} \, dx = -\frac{e^{-n}}{n} + \frac{1}{n^2}(1 - e^{-n})
$$

As $n \to \infty$, this approaches $0$, so $\int f_n \to 1/2 = \int f$, verifying MCT.

```python
import numpy as np
import matplotlib.pyplot as plt

def f_n(x, n):
    """The nth function in our monotone sequence"""
    return x * (1 - np.exp(-n * x))

def f_limit(x):
    """The limit function"""
    return x

# Domain
x = np.linspace(0, 1, 1000)
dx = x[1] - x[0]

# Compute integrals for increasing n
n_values = range(1, 51)
integrals_f_n = []

for n in n_values:
    y = f_n(x, n)
    integral = np.sum(y) * dx  # Riemann approximation
    integrals_f_n.append(integral)

# True integral of limit function
true_integral = 0.5

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left panel: Convergence of integrals
axes[0].plot(n_values, integrals_f_n, 'b.-', label='$\\int f_n \\, dx$', markersize=4)
axes[0].axhline(true_integral, color='r', linestyle='--', linewidth=2, 
                label='$\\int f \\, dx = 1/2$')
axes[0].set_xlabel('$n$', fontsize=12)
axes[0].set_ylabel('Integral value', fontsize=12)
axes[0].set_title('Monotone Convergence Theorem:\n$\\lim_{n\\to\\infty} \\int f_n = \\int f$', 
                   fontsize=13)
axes[0].legend(fontsize=11)
axes[0].grid(True, alpha=0.3)

# Right panel: Function convergence
for n in [1, 3, 10, 50]:
    y = f_n(x, n)
    axes[1].plot(x, y, label=f'$f_{{{n}}}(x)$', linewidth=1.5)
axes[1].plot(x, f_limit(x), 'k--', linewidth=2.5, label='$f(x) = x$')
axes[1].set_xlabel('$x$', fontsize=12)
axes[1].set_ylabel('$f_n(x)$', fontsize=12)
axes[1].set_title('Monotone convergence: $f_n(x) = x(1 - e^{-nx}) \\to x$', fontsize=13)
axes[1].legend(fontsize=10)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/Day2_MCT_verification.png', dpi=150)
print(f"\nMCT Verification:")
print(f"  Integral of f_1:  {integrals_f_n[0]:.6f}")
print(f"  Integral of f_10: {integrals_f_n[9]:.6f}")
print(f"  Integral of f_50: {integrals_f_n[-1]:.6f}")
print(f"  True integral:    {true_integral:.6f}")
print(f"  Error at n=50:    {abs(integrals_f_n[-1] - true_integral):.2e}")
print(f"\nConclusion: As n → ∞, ∫fₙ → ∫f = 0.5, confirming MCT.")
plt.show()
```

**Interpretation:** The left panel demonstrates that the sequence of integrals $\{\int f_n\}$ converges to the integral of the limit function. The right panel shows the monotone pointwise convergence of the functions themselves. This numerical verification confirms the theoretical guarantee provided by MCT: when a sequence of non-negative functions converges monotonically, we can interchange the limit and the integral.

**Technical Note:** The Riemann approximation used here is justified because each $f_n$ is continuous. For general measurable functions, one would need to use more sophisticated numerical integration schemes, but the conceptual verification remains the same.

---

### **IV. Application Bridge: Monotone Convergence in Reinforcement Learning**

#### **A. Value Iteration as Monotone Convergence**

In the theory of Markov Decision Processes, the **value iteration algorithm** is a fundamental method for computing optimal value functions. Starting from an initial guess $V_0$ (typically $V_0 = 0$), we iteratively apply the Bellman optimality operator:
$$
V_{n+1} = T^* V_n, \qquad \text{where} \quad (T^* V)(s) = \max_{a \in \mathcal{A}} \left\{ R(s,a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s,a) V(s') \right\}
$$

**Theorem 1.3 (Monotonicity of Value Iteration).** Assume the reward function is non-negative: $R(s,a) \geq 0$ for all $(s,a)$. Then:
1. The sequence $\{V_n\}$ is monotone increasing: $0 = V_0 \leq V_1 \leq V_2 \leq \cdots$
2. The sequence converges pointwise to the optimal value function: $V_n(s) \to V^*(s)$ for all $s$
3. The Bellman operator $T^*$ is a contraction in the supremum norm

*Proof Sketch.* Since $V_0 = 0$ and $R \geq 0$, we have $V_1 = T^* V_0 \geq 0 = V_0$. By induction, if $V_n \geq V_{n-1}$, then the monotonicity of $T^*$ (inherited from the max operator) gives $V_{n+1} = T^* V_n \geq T^* V_{n-1} = V_n$. The contraction property ensures convergence to the unique fixed point $V^*$. $\square$

**Connection to MCT:** In finite-state MDPs, the value function $V_n$ can be viewed as a function on the discrete probability space $(\mathcal{S}, 2^{\mathcal{S}}, \mu)$ where $\mu$ is the initial state distribution. The expected return under the greedy policy at step $n$ is:
$$
\mathbb{E}_{\mu}[V_n] = \sum_{s \in \mathcal{S}} \mu(s) V_n(s) = \int V_n \, d\mu
$$

The Monotone Convergence Theorem guarantees:
$$
\lim_{n \to \infty} \mathbb{E}_{\mu}[V_n] = \mathbb{E}_{\mu}[\lim_{n \to \infty} V_n] = \mathbb{E}_{\mu}[V^*]
$$

This justifies the practice of approximating $V^*$ by running value iteration for finitely many steps: not only does $V_n$ converge pointwise, but its expected value (the policy's performance) also converges.

#### **B. Policy Evaluation and Temporal Difference Learning**

In **policy evaluation**, we seek to compute $V^{\pi}$, the value function of a fixed policy $\pi$. The Bellman consistency equation is:
$$
V^{\pi} = T^{\pi} V^{\pi}, \qquad \text{where} \quad (T^{\pi} V)(s) = R^{\pi}(s) + \gamma \sum_{s'} P^{\pi}(s'|s) V(s')
$$

Starting from $V_0 = 0$ (or any initial guess), the sequence $V_n = (T^{\pi})^n V_0$ converges to $V^{\pi}$. When rewards are non-negative, this convergence is monotone, and MCT applies.

**Temporal Difference (TD) Learning** is a stochastic approximation algorithm for policy evaluation. The TD(0) update is:
$$
V_{t+1}(s_t) = V_t(s_t) + \alpha_t \left[R_t + \gamma V_t(s_{t+1}) - V_t(s_t)\right]
$$

Under appropriate conditions on the step sizes $\{\alpha_t\}$ and the ergodicity of the Markov chain induced by $\pi$, TD learning converges to $V^{\pi}$. The convergence analysis relies on the ODE method of stochastic approximation, which in turn uses the Monotone Convergence Theorem to justify taking limits inside expectations.

**Key Insight:** The Monotone Convergence Theorem is not merely a technical curiosity. It is the mathematical foundation that ensures the convergence of the most fundamental algorithms in reinforcement learning. Without MCT, we could not rigorously prove that value iteration or policy evaluation converge to the correct value function, even in the simplest finite-state setting.

---

### **V. Reflection and Forward Connections**

#### **Mathematical Insight**

The proof of MCT hinges on two pillars:
1. **Monotonicity of measures:** If $\{E_n\}$ is an increasing sequence of sets, then $\mu(\bigcup E_n) = \lim \mu(E_n)$ (continuity from below)
2. **Approximation by simple functions:** Any non-negative measurable function can be approximated from below by simple functions

The **α-trick** in the proof is subtle but crucial. When dealing with a simple function $\varphi$ that may equal the limit $f$ on a set of infinite measure, we cannot directly use the inequality $\int f_n \geq \int \varphi$ and pass to the limit. Instead, we "deflate" $\varphi$ slightly by multiplying by $\alpha \in (0,1)$, obtaining sets $E_n = \{x : f_n(x) \geq \alpha \varphi(x)\}$ where the inequality is strict off of $E_n^c$. This allows us to use the continuity of measure on the increasing sequence $\{E_n\}$ to conclude $\bigcup E_n = X$.

#### **RL Connection**

The Monotone Convergence Theorem provides the theoretical justification for several key results in RL:

1. **Value Iteration Convergence:** Starting from $V_0 = 0$, the sequence $V_n = (T^*)^n V_0$ converges monotonically to $V^*$, and $\mathbb{E}[V_n] \to \mathbb{E}[V^*]$
2. **Policy Evaluation:** For non-negative rewards, evaluating $V^{\pi}$ via iterated application of $T^{\pi}$ yields monotone convergence
3. **Stochastic Approximation:** The ODE method for analyzing TD learning relies on MCT to justify interchanging limits and expectations

Without MCT, we would lack rigorous proofs that these algorithms converge to the correct value functions.

#### **Open Questions**

1. **Relaxation of Monotonicity:** Can MCT be extended to sequences that are "almost monotone" (i.e., $f_n \leq f_{n+1}$ except on a set of measure zero)? The answer is affirmative: since integration ignores null sets, we can modify $f_n$ on the exceptional set without changing its integral, reducing to the standard MCT case.

2. **Rate of Convergence:** MCT guarantees $\int f_n \to \int f$, but provides no information about the rate. For RL applications, we care about sample complexity. Does monotone convergence of value functions imply a specific convergence rate for expected returns? This question connects to the contraction rate of the Bellman operator and mixing time of the Markov chain.

3. **Generalization to Negative Functions:** What happens if $f_n$ are not non-negative? The sequence $f_n(x) = -1/n$ converges monotonically to $f(x) = 0$, but $\int f_n = -\infty$ for all $n$. MCT fails. This motivates the study of Fatou's Lemma and the Dominated Convergence Theorem, which handle more general situations.

---

Tomorrow (Day 3), we will address the final point by developing **Fatou's Lemma** and the **Dominated Convergence Theorem**, which relax the hypotheses of MCT at the cost of weaker conclusions. These three theorems—MCT, Fatou, and DCT—form the **triumvirate of convergence** in integration theory, and they are the mathematical bedrock upon which the entire edifice of stochastic optimization and reinforcement learning is constructed.

### Exercises
[[Day_2_exercises]]

### Appendix
[[Day_2_Appendix_Numerical_Lebesgue]]
