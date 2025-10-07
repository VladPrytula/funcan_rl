[[Day_1]]

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

**Motivation:** In reinforcement learning, the central object of study is not a deterministic quantity, but an **expectation**—the average return under a stochastic policy in a stochastic environment. The mathematical formalization of expectation is the integral with respect to a probability measure. Before we can rigorously define the expected return $\mathbb{E}^{\pi}[G_t]$, or the value function $V^{\pi}(s) = \mathbb{E}^{\pi}\left[\sum_{k=0}^{\infty} \gamma^k R_{t+k} \mid S_t = s\right]$, we must construct a theory of integration that can handle three fundamental challenges that arise inevitably in the analysis of stochastic control systems.

**Challenge 1: Discontinuous Functions.** The indicator functions of events—fundamental to probability—are not Riemann integrable on arbitrary measurable sets. Consider $\mathbf{1}_A(x)$ for a set $A$ that is dense in an interval but has positive measure complement. The upper and lower Riemann sums never converge, yet this function represents a perfectly legitimate event in our probability space, and we must be able to compute its expectation.

**Challenge 2: Unbounded Domains.** State spaces in continuous control are often $\mathbb{R}^n$, which has infinite Lebesgue measure. Value functions may have support on all of $\mathbb{R}^n$, and the Riemann integral—fundamentally tied to compact domains—is inadequate for this setting.

**Challenge 3: Interchange of Limits and Integrals.** Algorithms like value iteration produce sequences of value functions $V_n \to V^*$. We need theorems guaranteeing $\mathbb{E}[V_n] \to \mathbb{E}[V^*]$ under appropriate conditions. The pathological examples that plague the Riemann theory—where pointwise convergence does not imply convergence of integrals—must be tamed.

The Riemann integral, defined via partitions of the domain, fails on all three counts. The **Lebesgue integral**, constructed by partitioning the *range* rather than the domain, succeeds completely. This section develops the Lebesgue integral from first principles, culminating in the **Monotone Convergence Theorem**—the first and most fundamental result enabling interchange of limits and integrals.

**Learning Objectives:**
* Understand the three-stage construction: simple functions → non-negative functions → general functions
* Appreciate why measurability is prerequisite for integration
* Master the Monotone Convergence Theorem and its proof technique (the α-trick)
* Recognize MCT as the foundation for proving convergence of value iteration

---

### **I. Core Theory: The Construction Hierarchy**

The Lebesgue integral is defined through a careful bootstrap procedure. We begin with the simplest class of functions—those taking only finitely many values—and extend systematically. At each stage, we verify that the essential properties (linearity, monotonicity, countable additivity) are preserved.

#### **A. Simple Functions: The Foundation**

The edifice of Lebesgue integration rests upon the humble class of simple functions. These are the discrete approximations from which all measurable functions shall be constructed.

**Definition 1.9 (Simple Function).** Let $(X, \mathcal{F}, \mu)$ be a measure space. A function $\varphi: X \to \mathbb{R}$ is **simple** if it takes only finitely many distinct values and is measurable. Equivalently, $\varphi$ can be written in the **canonical form**:
$$
\varphi(x) = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}(x)
$$
where $a_1, \ldots, a_n \in \mathbb{R}$ are distinct, $A_i = \{x : \varphi(x) = a_i\} \in \mathcal{F}$, and the sets $\{A_i\}_{i=1}^n$ form a partition of $X$ (i.e., they are pairwise disjoint and $\bigcup_{i=1}^n A_i = X$).

**Remark 1.6 (Non-Uniqueness of Representation).** A simple function may be written in infinitely many ways. For instance, $\varphi = 2\mathbf{1}_{[0,1]} + 3\mathbf{1}_{(1,2]} = 2\mathbf{1}_{[0,0.5]} + 2\mathbf{1}_{(0.5,1]} + 3\mathbf{1}_{(1,2]}$. The canonical form corresponds to the finest partition induced by the distinct values. Well-definedness of the integral (Definition 1.10) does not depend on the choice of representation.

**Definition 1.10 (Integral of Simple Functions).** For a non-negative simple function $\varphi = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}$ with $a_i \geq 0$, we define:
$$
\int \varphi \, d\mu = \sum_{i=1}^{n} a_i \mu(A_i)
$$
where the convention $0 \cdot \infty = 0$ is adopted.

**Justification of Convention.** If $a_i = 0$, the contribution of $A_i$ to the integral should be zero regardless of $\mu(A_i)$, even if $\mu(A_i) = \infty$. This is consistent with the intuition that "integrating zero over any set yields zero."

**Proposition 1.6 (Properties of the Integral on Simple Functions).**
Let $\varphi, \psi$ be non-negative simple functions, and $c \geq 0$ a constant. Then:
1. **(Linearity)** $\displaystyle\int (c\varphi + \psi) \, d\mu = c \int \varphi \, d\mu + \int \psi \, d\mu$
2. **(Monotonicity)** If $\varphi \leq \psi$ pointwise, then $\displaystyle\int \varphi \, d\mu \leq \int \psi \, d\mu$
3. **(Countable Additivity on Domain)** If $\{A_n\}$ are disjoint measurable sets with $\bigcup_{n=1}^\infty A_n = X$, then:
   $$
   \int_X \varphi \, d\mu = \sum_{n=1}^{\infty} \int_{A_n} \varphi \, d\mu
   $$

*Proof.* 
**(1) Linearity:** Let $\varphi = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ and $\psi = \sum_{j=1}^m b_j \mathbf{1}_{B_j}$ be in canonical form. Consider the common refinement $\mathcal{R} = \{A_i \cap B_j : i=1,\ldots,n,\, j=1,\ldots,m\}$. On each set $R \in \mathcal{R}$, both $\varphi$ and $\psi$ are constant. Write $\varphi = \sum_{R \in \mathcal{R}} \alpha_R \mathbf{1}_R$ and $\psi = \sum_{R \in \mathcal{R}} \beta_R \mathbf{1}_R$. Then:
$$
c\varphi + \psi = \sum_{R \in \mathcal{R}} (c\alpha_R + \beta_R) \mathbf{1}_R
$$
and
$$
\int (c\varphi + \psi) \, d\mu = \sum_{R \in \mathcal{R}} (c\alpha_R + \beta_R) \mu(R) = c\sum_{R \in \mathcal{R}} \alpha_R \mu(R) + \sum_{R \in \mathcal{R}} \beta_R \mu(R) = c\int\varphi\,d\mu + \int\psi\,d\mu
$$

**(2) Monotonicity:** If $\varphi \leq \psi$, then for the common refinement, on each $R$ we have $\alpha_R \leq \beta_R$. Since $\mu(R) \geq 0$, we obtain $\alpha_R \mu(R) \leq \beta_R \mu(R)$, and summing over all $R$ yields the result.

**(3) Countable Additivity:** For $\varphi = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$, we have:
$$
\int_{A_n} \varphi \, d\mu = \sum_{i=1}^n a_i \mu(A_i \cap A_n)
$$
By countable additivity of $\mu$:
$$
\sum_{n=1}^\infty \int_{A_n} \varphi \, d\mu = \sum_{i=1}^n a_i \sum_{n=1}^\infty \mu(A_i \cap A_n) = \sum_{i=1}^n a_i \mu\left(A_i \cap \bigcup_{n=1}^\infty A_n\right) = \sum_{i=1}^n a_i \mu(A_i) = \int_X \varphi \, d\mu
$$
$\square$

#### **B. Non-Negative Measurable Functions: Extension by Supremum**

Having defined integration for simple functions—the discrete scaffolding—we now extend to the continuous structure of all non-negative measurable functions via a supremum construction. This is the crucial conceptual leap of the Lebesgue approach.

**Definition 1.11 (Integral of Non-Negative Functions).** Let $f: X \to [0, \infty]$ be a measurable function. We define:
$$
\int f \, d\mu = \sup \left\{ \int \varphi \, d\mu \;\Big|\; 0 \leq \varphi \leq f, \, \varphi \text{ simple} \right\}
$$

**Remark 1.7 (Geometric Intuition).** The integral of $f$ is the "area under the curve" computed by approximating $f$ from below with increasingly fine step functions. Unlike the Riemann integral, which partitions the domain into intervals and forms rectangles based on function values at sample points, the Lebesgue approach partitions the **range** of $f$ into levels, measuring the sets $\{x : f(x) > t\}$ for each $t \geq 0$. This reversal—from domain partition to range partition—is what enables handling discontinuous functions.

**Proposition 1.7 (Extension of Properties to Non-Negative Functions).**
For measurable $f, g: X \to [0, \infty]$ and $c \geq 0$:
1. **(Linearity)** $\displaystyle\int (cf + g) \, d\mu = c \int f \, d\mu + \int g \, d\mu$
2. **(Monotonicity)** If $f \leq g$ almost everywhere, then $\displaystyle\int f \, d\mu \leq \int g \, d\mu$
3. **(Countable Additivity)** If $\{A_n\}$ are disjoint in $\mathcal{F}$, then:
   $$
   \int_{\bigcup_{n=1}^\infty A_n} f \, d\mu = \sum_{n=1}^{\infty} \int_{A_n} f \, d\mu
   $$

*Proof.* Each property is established by approximating $f$ and $g$ from below with simple functions and using the corresponding property for simple functions (Proposition 1.6). The supremum operation preserves these relations. For a complete proof, one uses the fact that if $\varphi \leq f$ and $\psi \leq g$ are simple, then $\varphi + \psi \leq f + g$ is also simple, and:
$$
\int(\varphi + \psi)\,d\mu = \int\varphi\,d\mu + \int\psi\,d\mu \leq \sup\{\cdots\} + \sup\{\cdots\}
$$
The reverse inequality requires showing that for any simple $\chi \leq f + g$, we can find simple $\varphi \leq f$ and $\psi \leq g$ with $\chi \leq \varphi + \psi$. The technical details are standard and can be found in Folland §2.2. $\square$

#### **C. General Measurable Functions: Decomposition into Positive and Negative Parts**

To integrate functions that take both positive and negative values, we decompose them into positive and negative components. This is the final stage of the construction.

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

**Remark 1.8 (Why Integrability Requires Finiteness).** If $\int f^+ \, d\mu = \int f^- \, d\mu = \infty$, the difference "$\infty - \infty$" is undefined. This motivates the restriction to functions with $\int |f| \, d\mu < \infty$. In the context of probability spaces (where $\mu(X) = 1$), this condition is precisely the requirement that the random variable has finite expectation.

---

### **II. The Monotone Convergence Theorem: Guaranteeing Limit-Integral Interchange**

The power of the Lebesgue integral lies not merely in its ability to integrate a broader class of functions than the Riemann integral, but in its robust convergence theorems. The **Monotone Convergence Theorem** is the cornerstone, the first and most fundamental result that permits interchange of limits and integrals.

**Theorem 1.2 (Monotone Convergence Theorem – Beppo Levi).** Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^{\infty}$ be a sequence of measurable functions satisfying:
1. **(Non-negativity)** $f_n \geq 0$ for all $n$
2. **(Monotonicity)** $f_1(x) \leq f_2(x) \leq f_3(x) \leq \cdots$ for all $x \in X$ (pointwise monotonicity)
3. **(Pointwise convergence)** $f_n(x) \to f(x)$ for all $x \in X$

Then $f$ is measurable and:
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu = \int \left(\lim_{n \to \infty} f_n\right) d\mu
$$
In other words, **the integral of the limit equals the limit of the integrals**.

**Remark 1.9 (Significance and Scope).** This theorem is remarkable because it requires no domination hypothesis. The sequence $\{f_n\}$ may converge to a function with infinite integral, and the theorem remains valid. The conclusion $\lim \int f_n = \int (\lim f_n)$ is the foundation for all subsequent convergence results in integration theory. Its proof, though elementary in structure, contains the α-trick—a technique that recurs throughout analysis whenever one must handle functions on sets of infinite measure.

*Proof.* The complete proof with full technical detail is provided in [[Day_2_exercises]]. We outline the strategy here.

**Proof Strategy:**
1. **Step 1 (Measurability):** Since $f(x) = \sup_n f_n(x)$ and each $f_n$ is measurable, $f$ is measurable (as supremum of measurable functions).

2. **Step 2 (Easy Inequality):** By monotonicity of the integral, $\int f_n \leq \int f_{n+1} \leq \int f$ for all $n$. Thus $\{\int f_n\}$ is an increasing sequence bounded above by $\int f$, hence $\lim_{n\to\infty} \int f_n$ exists and satisfies:
   $$\lim_{n \to \infty} \int f_n \, d\mu \leq \int f \, d\mu$$

3. **Step 3 (Hard Inequality via α-Trick):** This is the crux. We must show:
   $$\int f \, d\mu \leq \lim_{n \to \infty} \int f_n \, d\mu$$
   
   Fix an arbitrary simple function $0 \leq \varphi \leq f$. It suffices to prove:
   $$\int \varphi \, d\mu \leq \lim_{n \to \infty} \int f_n \, d\mu$$
   
   For any $\alpha \in (0,1)$, define:
   $$E_n = \{x \in X : f_n(x) \geq \alpha\varphi(x)\}$$
   
   Then $E_1 \subseteq E_2 \subseteq \cdots$ (by monotonicity of $f_n$) and $\bigcup_{n=1}^\infty E_n = X$ (since $f_n \to f \geq \varphi$ pointwise).
   
   For each $n$:
   $$\int f_n \, d\mu \geq \int_{E_n} f_n \, d\mu \geq \alpha \int_{E_n} \varphi \, d\mu$$
   
   By continuity of measure from below (as $E_n \uparrow X$):
   $$\lim_{n \to \infty} \int_{E_n} \varphi \, d\mu = \int_X \varphi \, d\mu$$
   
   Thus:
   $$\lim_{n \to \infty} \int f_n \, d\mu \geq \alpha \int \varphi \, d\mu$$
   
   Letting $\alpha \to 1^-$ and taking supremum over all simple $\varphi \leq f$:
   $$\lim_{n \to \infty} \int f_n \, d\mu \geq \int f \, d\mu$$

4. **Step 4 (Conclusion):** Combining Steps 2 and 3 yields equality. $\square$

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
3. **Monotonicity:** Since $e^{-nx}$ is decreasing in $n$, we have $1 - e^{-nx}$ increasing in $n$, hence:
   $$f_n(x) \leq f_{n+1}(x) \quad \text{for all } x \in [0,1]$$

The limit function is $f(x) = x$, which has integral:
$$\int_0^1 x \, dx = \frac{1}{2}$$

For each $f_n$, we compute the integral analytically. We have:
$$
\int_0^1 f_n(x) \, dx = \int_0^1 x(1 - e^{-nx}) \, dx = \int_0^1 x \, dx - \int_0^1 x e^{-nx} \, dx
$$

The first integral is $1/2$. For the second, integration by parts gives:
$$
\int_0^1 x e^{-nx} \, dx = \left[-\frac{x e^{-nx}}{n}\right]_0^1 + \frac{1}{n}\int_0^1 e^{-nx} \, dx = -\frac{e^{-n}}{n} + \frac{1}{n^2}(1 - e^{-n})
$$

As $n \to \infty$, both terms approach $0$, so:
$$
\int_0^1 f_n(x) \, dx \to \frac{1}{2} = \int_0^1 f(x) \, dx
$$

This verifies MCT for this particular sequence. We now implement this numerically.

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
print(f"\nConclusion: As n → ∞, ∫f_n → ∫f = 0.5, confirming MCT.")

plt.show()
```

**Interpretation:** The left panel demonstrates that the sequence of integrals $\{\int f_n\}$ converges monotonically to the integral of the limit function. The right panel shows the monotone pointwise convergence of the functions themselves. This numerical verification confirms the theoretical guarantee provided by MCT: when a sequence of non-negative functions converges monotonically, we can interchange the limit and the integral.

**Technical Note:** The Riemann approximation used here is justified because each $f_n$ is continuous. For general measurable functions—such as those arising in the pathological examples of [[Day_2_Appendix_Numerical_Lebesgue]]—one would need to use more sophisticated numerical integration schemes based on approximation by simple functions. However, the conceptual verification remains the same: MCT guarantees that the numerical limit of integrals matches the integral of the numerical limit.

---

### **IV. Application Bridge: Monotone Convergence in Reinforcement Learning**

The Monotone Convergence Theorem is not an abstract curiosity. It is the mathematical guarantee that underpins the convergence of the most fundamental algorithms in reinforcement learning. We now make this connection explicit.

#### **A. Value Iteration as Monotone Convergence**

In the theory of Markov Decision Processes, the **value iteration algorithm** is a fundamental method for computing optimal value functions. Starting from an initial guess $V_0$ (typically $V_0 = 0$ or $V_0 = \mathbf{0}$), we iteratively apply the Bellman optimality operator:
$$
V_{n+1} = T^* V_n, \qquad \text{where} \quad (T^* V)(s) = \max_{a \in \mathcal{A}} \left\{ R(s,a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s,a) V(s') \right\}
$$

**Theorem 1.3 (Monotonicity of Value Iteration).** Assume the reward function is non-negative: $R(s,a) \geq 0$ for all $(s,a)$. Then:
1. The sequence $\{V_n\}$ is monotone increasing: $0 = V_0 \leq V_1 \leq V_2 \leq \cdots$
2. The sequence converges pointwise to the optimal value function: $V_n(s) \to V^*(s)$ for all $s \in \mathcal{S}$
3. The Bellman operator $T^*$ is a $\gamma$-contraction in the supremum norm, ensuring exponential convergence

*Proof Sketch.* Since $V_0 = 0$ and $R \geq 0$, we have:
$$V_1(s) = T^* V_0(s) = \max_a R(s,a) \geq 0 = V_0(s)$$

By induction, if $V_n \geq V_{n-1}$, then the monotonicity of the max operator and the transition probabilities (which are non-negative) give:
$$V_{n+1}(s) = T^* V_n(s) \geq T^* V_{n-1}(s) = V_n(s)$$

The sequence $\{V_n(s)\}$ is monotone increasing for each $s$. By the contraction property of $T^*$ in the supremum norm (a consequence of the discount factor $\gamma < 1$), the sequence is also bounded above by $V^*(s)$. Hence it converges. The unique fixed point of the contraction $T^*$ is $V^*$, so $V_n \to V^*$ pointwise. $\square$

**Connection to MCT:** In finite-state MDPs, the value function $V_n$ can be viewed as a function on the discrete probability space $(\mathcal{S}, 2^{\mathcal{S}}, \mu)$ where $\mu$ is the initial state distribution. The expected return under the greedy policy at step $n$ is:
$$
\mathbb{E}_{\mu}[V_n] = \sum_{s \in \mathcal{S}} \mu(s) V_n(s) = \int V_n \, d\mu
$$

The **Monotone Convergence Theorem** guarantees:
$$
\lim_{n \to \infty} \mathbb{E}_{\mu}[V_n] = \mathbb{E}_{\mu}\left[\lim_{n \to \infty} V_n\right] = \mathbb{E}_{\mu}[V^*]
$$

This justifies the practice of approximating $V^*$ by running value iteration for finitely many steps: not only does $V_n$ converge pointwise to $V^*$, but its expected value (the policy's performance) also converges. Without MCT, we would have no guarantee that finite-time performance $\mathbb{E}_{\mu}[V_N]$ approximates the optimal performance $\mathbb{E}_{\mu}[V^*]$.

#### **B. Policy Evaluation and Temporal Difference Learning**

In **policy evaluation**, we seek to compute $V^{\pi}$, the value function of a fixed policy $\pi$. The Bellman consistency equation is:
$$
V^{\pi} = T^{\pi} V^{\pi}, \qquad \text{where} \quad (T^{\pi} V)(s) = R^{\pi}(s) + \gamma \sum_{s'} P^{\pi}(s'|s) V(s')
$$

Starting from $V_0 = 0$ (or any initial guess), the sequence $V_n = (T^{\pi})^n V_0$ converges to $V^{\pi}$. When rewards are non-negative, this convergence is monotone, and MCT applies as in the value iteration case.

**Temporal Difference (TD) Learning** is a stochastic approximation algorithm for policy evaluation. The TD(0) update is:
$$
V_{t+1}(s_t) = V_t(s_t) + \alpha_t \left[R_t + \gamma V_t(s_{t+1}) - V_t(s_t)\right]
$$

Under appropriate conditions on the step sizes $\{\alpha_t\}$ (specifically, $\sum \alpha_t = \infty$ and $\sum \alpha_t^2 < \infty$) and the ergodicity of the Markov chain induced by $\pi$, TD learning converges to $V^{\pi}$. The convergence analysis relies on the **ODE method of stochastic approximation**, which in turn uses the Monotone Convergence Theorem to justify taking limits inside expectations. This connection will be made fully rigorous in **Week 34–36** when we study stochastic approximation theory.

**Key Insight:** The Monotone Convergence Theorem is not merely a technical curiosity. It is the mathematical foundation that ensures the convergence of the most fundamental algorithms in reinforcement learning. Without MCT, we could not rigorously prove that value iteration or policy evaluation converge to the correct value function, even in the simplest finite-state setting.

---

### **V. Reflection and Forward Connections**

#### **Mathematical Insight**

The proof of MCT hinges on two pillars:
1. **Monotonicity of measures:** If $\{E_n\}$ is an increasing sequence of sets, then $\mu(\bigcup E_n) = \lim \mu(E_n)$ (continuity from below)
2. **Approximation by simple functions:** Any non-negative measurable function can be approximated from below by simple functions

The **α-trick** in Step 3 of the proof is subtle but crucial. When dealing with a simple function $\varphi$ that may equal the limit $f$ on a set of infinite measure, we cannot directly use the inequality $\int f_n \geq \int \varphi$ and pass to the limit. The issue is that on the complement of $E_n = \{x : f_n(x) \geq \varphi(x)\}$, we have $f_n < \varphi$, and if $\mu(E_n^c)$ remains bounded away from zero for all $n$, we cannot conclude that $\int f_n \to \int \varphi$. 

Instead, we "deflate" $\varphi$ slightly by multiplying by $\alpha \in (0,1)$, obtaining sets $E_n = \{x : f_n(x) \geq \alpha\varphi(x)\}$ where the inequality is strict off of $E_n^c$. This allows us to use the continuity of measure on the increasing sequence $\{E_n\}$ to conclude $\bigcup E_n = X$. The α-trick is a recurring technique in analysis whenever one must handle functions on sets of infinite measure.

#### **RL Connection**

The Monotone Convergence Theorem provides the theoretical justification for several key results in RL:

1. **Value Iteration Convergence:** Starting from $V_0 = 0$, the sequence $V_n = (T^*)^n V_0$ converges monotonically to $V^*$, and $\mathbb{E}[V_n] \to \mathbb{E}[V^*]$
2. **Policy Evaluation:** For non-negative rewards, evaluating $V^{\pi}$ via iterated application of $T^{\pi}$ yields monotone convergence
3. **Stochastic Approximation:** The ODE method for analyzing TD learning relies on MCT to justify interchanging limits and expectations

Without MCT, we would lack rigorous proofs that these algorithms converge to the correct value functions.

#### **Open Questions**

1. **Relaxation of Monotonicity:** Can MCT be extended to sequences that are "almost monotone" (i.e., $f_n \leq f_{n+1}$ except on a set of measure zero)? The answer is affirmative: since integration ignores null sets, we can modify $f_n$ on the exceptional set without changing its integral, reducing to the standard MCT case. This observation is crucial in stochastic approximation, where iterates are only defined almost surely (i.e., outside of negligible exceptional sets).

2. **Rate of Convergence:** MCT guarantees $\int f_n \to \int f$, but provides no information about the rate of convergence. For RL applications, we care about sample complexity. Does monotone convergence of value functions imply a specific convergence rate for expected returns? This question connects to the contraction rate of the Bellman operator and the mixing time of the Markov chain.

3. **Generalization to Negative Functions:** What happens if $f_n$ are not non-negative? The sequence $f_n(x) = -1/n$ converges monotonically to $f(x) = 0$, and we have:
   $$\int_0^1 f_n(x)\,dx = -1/n \to 0 = \int_0^1 f(x)\,dx$$
   So MCT's conclusion holds in this case. However, if $\int f_n = -\infty$ for all $n$ and $\int f = -\infty$, the equation "$-\infty = -\infty$" is not meaningful in extended real arithmetic. This motivates the study of **Fatou's Lemma** and the **Dominated Convergence Theorem** (Day 3), which relax the hypotheses of MCT at the cost of weaker conclusions.

---

Tomorrow (Day 3), we will address the final point by developing **Fatou's Lemma** and the **Dominated Convergence Theorem**, which relax the hypotheses of MCT. These three theorems—MCT, Fatou, and DCT—form the **triumvirate of convergence** in integration theory, and they are the mathematical bedrock upon which the entire edifice of stochastic optimization and reinforcement learning is constructed.