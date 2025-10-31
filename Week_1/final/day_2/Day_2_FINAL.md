[[Day_1_FINAL#]]

### Agenda:

##### 📘 Day 2 – Week 1: The Lebesgue Integral and Monotone Convergence
**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (40 min) – Reading**

**Topic:** _Construction of the Lebesgue integral and convergence theorems_

- Read from [@folland:real_analysis:1999, §2.1–2.2] or equivalent in [@durrett:probability:2019, Ch.2].
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

**Challenge 1: Discontinuous Functions.** The indicator functions of events—fundamental to probability—are not Riemann integrable on arbitrary measurable sets. Consider the indicator function of the rationals: $\varphi(x) = \mathbf{1}_\mathbb{Q}(x)$ on $[0,1]$. This function is 1 on a dense set ($\mathbb{Q} \cap [0,1]$) of Lebesgue measure zero, and 0 on a dense set (($\mathbb{R} \setminus \mathbb{Q}) \cap [0,1]$) of measure 1. Every Riemann partition has both rationals and irrationals, so upper sums equal 1 and lower sums equal 0, preventing convergence. However, the Lebesgue integral equals 0 because $\mu(\mathbb{Q} \cap [0,1]) = 0$. In reinforcement learning, consider the event "agent reaches goal state"—represented by $\mathbf{1}_{\text{goal}}(s)$, an indicator function. If the goal region has fractured geometry (common in robotics with obstacle-rich environments), this function is discontinuous at the boundary, rendering Riemann integration inadequate.

**Challenge 2: Unbounded Domains.** State spaces in continuous control are often $\mathbb{R}^n$, which has infinite Lebesgue measure. Value functions may have support on all of $\mathbb{R}^n$, and the Riemann integral—fundamentally tied to compact domains—is inadequate for this setting.

**Challenge 3: Interchange of Limits and Integrals.** Algorithms like value iteration produce sequences of value functions $V_n \to V^*$. We need theorems guaranteeing $\mathbb{E}[V_n] \to \mathbb{E}[V^*]$ under appropriate conditions. The pathological examples that plague the Riemann theory—where pointwise convergence does not imply convergence of integrals—must be tamed.

The Riemann integral, defined via partitions of the domain, fails on all three counts. The **Lebesgue integral**, constructed by partitioning the *range* rather than the domain, succeeds completely. This section develops the Lebesgue integral from first principles, culminating in the **Monotone Convergence Theorem**—the first and most fundamental result enabling interchange of limits and integrals.

**Learning Objectives:**
* Understand the three-stage construction: simple functions → non-negative functions → general functions
* Appreciate why measurability ([DEF-1.1.3] from Day 1) is prerequisite for integration
* Master the Monotone Convergence Theorem and its proof technique (the α-trick)
* Recognize MCT as the foundation for proving convergence of value iteration

---

### **I. Core Theory: The Construction Hierarchy**

The Lebesgue integral is defined through a careful bootstrap procedure. We begin with the simplest class of functions—those taking only finitely many values—and extend systematically. At each stage, we verify that the essential properties (linearity, monotonicity, countable additivity) are preserved.

#### **A. Simple Functions: The Foundation**

The edifice of Lebesgue integration rests upon the humble class of simple functions. These are the discrete approximations from which all measurable functions shall be constructed.

**Definition 1.2.1 (Simple Function)** {#DEF-1.2.1} Let $(X, \mathcal{F}, \mu)$ be a measure space ([DEF-1.1.1] from Day 1). A function $\varphi: X \to \mathbb{R}$ is **simple** if there exist finitely many measurable sets $A_1, \ldots, A_n \in \mathcal{F}$ (not necessarily disjoint or exhaustive) and constants $a_1, \ldots, a_n \in \mathbb{R}$ such that:
$$
\varphi(x) = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}(x)
$$

Measurability of $\varphi$ follows from the measurability of the $A_i$ and finite linearity of measurable functions. The **canonical form** is obtained when the $\{A_i\}$ are the level sets of distinct values and form a partition of $X$. In the canonical form, $a_1, \ldots, a_n$ are the distinct values of $\varphi$ and $A_i = \{x : \varphi(x) = a_i\}$.

**Remark 1.6 (Non-Uniqueness of Representation).** A simple function has infinitely many representations (e.g., subdividing the $A_i$), but the **canonical form** with distinct values $\{a_i\}$ and corresponding level sets $\{A_i = \{x : \varphi(x) = a_i\}\}$ is unique. For the purposes of [DEF-1.2.2], the integral is independent of representation, as will be verified in the proof of [PROP-1.2.1].

**Definition 1.2.2 (Integral of Simple Functions)** {#DEF-1.2.2} For a non-negative simple function $\varphi = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}$ with $a_i \geq 0$, we define:
$$
\int \varphi \, d\mu = \sum_{i=1}^{n} a_i \mu(A_i)
$$
where the convention $0 \cdot \infty = 0$ is adopted.[^convention]

[^convention]: More precisely, if $a_i = 0$ in the canonical representation, then $a_i \mu(A_i) = 0$ regardless of whether $\mu(A_i)$ is finite or infinite. This convention is consistent with the interpretation that "integrating the zero function over any set yields zero," and is essential for well-definedness when dealing with measure spaces having sets of infinite measure.

**Justification of Convention.** If $a_i = 0$, the contribution of $A_i$ to the integral should be zero regardless of $\mu(A_i)$, even if $\mu(A_i) = \infty$. This is consistent with the intuition that "integrating zero over any set yields zero."

**Proposition 1.2.1 (Properties of the Integral on Simple Functions)** {#PROP-1.2.1}
Let $\varphi, \psi$ be non-negative simple functions, and $c \geq 0$ a constant. Then:
1. **(Linearity)** $\displaystyle\int (c\varphi + \psi) \, d\mu = c \int \varphi \, d\mu + \int \psi \, d\mu$
2. **(Monotonicity)** If $\varphi \leq \psi$ pointwise, then $\displaystyle\int \varphi \, d\mu \leq \int \psi \, d\mu$
3. **(Countable Additivity on Domain)** If $\{A_n\}$ are disjoint measurable sets with $\bigcup_{n=1}^{\infty} A_n = X$, then:
   $$
   \int_X \varphi \, d\mu = \sum_{n=1}^{\infty} \int_{A_n} \varphi \, d\mu
   $$

*Proof.*
**(1) Linearity:** Let $\varphi = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ and $\psi = \sum_{j=1}^m b_j \mathbf{1}_{B_j}$ be in canonical form. Consider the common refinement $\mathcal{R} = \{A_i \cap B_j : i=1,\ldots,n,\, j=1,\ldots,m\}$. Since $\mathcal{F}$ is a σ-algebra, finite intersections $A_i \cap B_j$ are measurable. The collection $\mathcal{R} = \{A_i \cap B_j : i=1,...,n, j=1,...,m\}$ forms a partition of $X$ because the $\{A_i\}$ partition $X$ and the $\{B_j\}$ partition $X$. Any $x \in X$ belongs to exactly one $A_i$ and exactly one $B_j$, hence to exactly one element $A_i \cap B_j \in \mathcal{R}$.

On each set $R \in \mathcal{R}$, both $\varphi$ and $\psi$ are constant. Write $\varphi = \sum_{R \in \mathcal{R}} \alpha_R \mathbf{1}_R$ and $\psi = \sum_{R \in \mathcal{R}} \beta_R \mathbf{1}_R$. Then:
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
By countable additivity of $\mu$ ([DEF-1.1.1] from Day 1):
$$
\sum_{n=1}^{\infty} \int_{A_n} \varphi \, d\mu = \sum_{i=1}^n a_i \sum_{n=1}^{\infty} \mu(A_i \cap A_n) = \sum_{i=1}^n a_i \mu\left(A_i \cap \bigcup_{n=1}^{\infty} A_n\right) = \sum_{i=1}^n a_i \mu(A_i) = \int_X \varphi \, d\mu
$$
$\square$

#### **B. Non-Negative Measurable Functions: Extension by Supremum**

Having defined integration for simple functions—the discrete scaffolding—we now extend to the continuous structure of all non-negative measurable functions via a supremum construction. This is the crucial conceptual leap of the Lebesgue approach.

How should we extend integration from simple functions to general measurable functions? The Riemann approach partitions the domain into intervals; the Lebesgue approach instead approximates the *function itself* from below with simple functions. For a non-negative measurable function $f$, we ask: what is the supremal integral among all simple functions that underestimate $f$? This supremum—if it exists—should be the integral of $f$.

**Definition 1.2.3 (Integral of Non-Negative Functions)** {#DEF-1.2.3} Let $f: X \to [0, \infty]$ be a measurable function. We define:
$$
\int f \, d\mu = \sup \left\{ \int \varphi \, d\mu \;\Big|\; 0 \leq \varphi \leq f, \, \varphi \text{ simple} \right\} \in [0, \infty]
$$
This supremum exists because: (i) the set is nonempty (contains $\varphi \equiv 0$), and (ii) any supremum of a nonempty subset of $[0, \infty]$ exists in the extended reals.

**Remark 1.7 (Geometric Intuition).** The integral of $f$ is the "area under the curve" computed by approximating $f$ from below with increasingly fine step functions. Unlike the Riemann integral, which partitions the domain into intervals and forms rectangles based on function values at sample points, the Lebesgue approach partitions the **range** of $f$ into levels, measuring the sets $\{x : f(x) > t\}$ for each $t \geq 0$. This reversal—from domain partition to range partition—is what enables handling discontinuous functions.

**Proposition 1.2.2 (Extension of Properties to Non-Negative Functions)** {#PROP-1.2.2}
For measurable $f, g: X \to [0, \infty]$ and $c \geq 0$:
1. **(Linearity)** $\displaystyle\int (cf + g) \, d\mu = c \int f \, d\mu + \int g \, d\mu$
2. **(Monotonicity)** If $f \leq g$ almost everywhere, then $\displaystyle\int f \, d\mu \leq \int g \, d\mu$
3. **(Countable Additivity)** If $\{A_n\}$ are disjoint in $\mathcal{F}$, then:
   $$
   \int_{\bigcup_{n=1}^{\infty} A_n} f \, d\mu = \sum_{n=1}^{\infty} \int_{A_n} f \, d\mu
   $$

*Proof.* We establish each property step by step.

**(2) Monotonicity:** If $f \leq g$ a.e., then for any simple $\varphi \leq f$, we have $\varphi \leq g$ a.e., so $\int \varphi \leq \int g$. Taking supremum over $\varphi$ gives $\int f \leq \int g$.

**(3) Countable additivity:** Follows from MCT applied to the partial sums (proof deferred to after [THM-1.2.1]).

**(1) Linearity:** We defer the complete proof of linearity for addition until after [THM-1.2.1] is established, as the proof requires MCT. For scalar multiplication: if $c \geq 0$ and $\varphi \leq f$ is simple, then $c\varphi \leq cf$ is simple, and $\int c\varphi = c\int \varphi$ by linearity for simple functions ([PROP-1.2.1]). Taking the supremum over all $\varphi \leq f$ gives $\int cf = c\int f$. $\square$

**Remark 1.7A.** The proof of linearity for addition requires MCT to avoid circularity. After establishing [THM-1.2.1], we will complete the proof using approximation by simple functions. For a direct proof without MCT, see [@folland:real_analysis:1999, §2.2, Thm 2.10].

#### **C. General Measurable Functions: Decomposition into Positive and Negative Parts**

To integrate functions that take both positive and negative values, we decompose them into positive and negative components. This is the final stage of the construction.

**Definition 1.2.4 (Positive and Negative Parts)** {#DEF-1.2.4} For a measurable function $f: X \to \mathbb{R}$, define:
$$
f^+(x) = \max\{f(x), 0\}, \qquad f^-(x) = \max\{-f(x), 0\}
$$
Then $f = f^+ - f^-$ and $|f| = f^+ + f^-$. Both $f^+$ and $f^-$ are non-negative measurable functions.

**Remark 1.7B.** Note that $f^+$ and $f^-$ are *never simultaneously nonzero* at any point: if $f(x) > 0$, then $f^+(x) = f(x)$ and $f^-(x) = 0$; if $f(x) < 0$, then $f^+(x) = 0$ and $f^-(x) = -f(x)$; if $f(x) = 0$, both vanish. Thus $f^+ \cdot f^- = 0$ pointwise, which ensures the decomposition $f = f^+ - f^-$ is unambiguous.

**Definition 1.2.5 (Integral of General Functions)** {#DEF-1.2.5} A measurable function $f: X \to \mathbb{R}$ is **integrable** (or **Lebesgue integrable**) if $\int |f| \, d\mu < \infty$. For such $f$, we define:
$$
\int f \, d\mu = \int f^+ \, d\mu - \int f^- \, d\mu
$$
Since both $\int f^+ \, d\mu$ and $\int f^- \, d\mu$ are finite, this difference is well-defined.

**Notation.** We write $f \in L^1(\mu)$ to denote that $f$ is integrable. The space $L^1(\mu)$ is the collection of all (equivalence classes of) integrable functions, where two functions are identified if they differ only on a set of measure zero ([DEF-1.1.7] from Day 1).

**Remark 1.8 (Why Integrability Requires Finiteness).** If $\int f^+ \, d\mu = \int f^- \, d\mu = \infty$, the difference "$\infty - \infty$" is undefined in extended real arithmetic. This motivates the restriction to functions with $\int |f| \, d\mu < \infty$. In probability, this condition corresponds to requiring finite expectation: $\mathbb{E}[|X|] < \infty$. For the standard Cauchy distribution with density $f(x) = 1/(\pi(1 + x^2))$ one has
$$\int_{-\infty}^{\infty} |x| f(x) \, dx = \frac{2}{\pi} \int_0^{\infty} \frac{x}{1+x^2} \, dx = \frac{1}{\pi}[\ln(1+x^2)]_0^{\infty} = \infty,$$
so $\mathbb{E}[|X|] = \infty$ and the random variable $X$ is not integrable (even though the density integrates to 1).

---

### **II. The Monotone Convergence Theorem: Guaranteeing Limit-Integral Interchange**

The power of the Lebesgue integral lies not merely in its ability to integrate a broader class of functions than the Riemann integral, but in its robust convergence theorems. The **Monotone Convergence Theorem** is the cornerstone, the first and most fundamental result that permits interchange of limits and integrals.

**Lemma 1.2.1 (Continuity of Measure from Below)** {#LEM-1.2.1} Let $(X, \mathcal{F}, \mu)$ be a measure space. If $\{E_n\}$ is an increasing sequence of measurable sets ($E_1 \subseteq E_2 \subseteq \cdots$) with $E = \bigcup_{n=1}^{\infty} E_n$, then:
$$
\mu(E) = \lim_{n \to \infty} \mu(E_n)
$$

*Proof.* Define $F_1 = E_1$ and $F_n = E_n \setminus E_{n-1}$ for $n \geq 2$. The sets $\{F_n\}$ are pairwise disjoint with $\bigcup F_n = E$. By countable additivity:
$$
\mu(E) = \sum_{n=1}^{\infty} \mu(F_n) = \lim_{N \to \infty} \sum_{n=1}^{N} \mu(F_n) = \lim_{N \to \infty} \mu(E_N)
$$
where the last equality follows from $E_N = \bigcup_{n=1}^{N} F_n$. $\square$

**Theorem 1.2.1 (Monotone Convergence Theorem – Beppo Levi)** {#THM-1.2.1} Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^{\infty}$ be a sequence of measurable functions satisfying:
1. **(Non-negativity)** $f_n \geq 0$ for all $n$
2. **(Monotonicity)** $f_1(x) \leq f_2(x) \leq f_3(x) \leq \cdots$ for all $x \in X$ (pointwise monotonicity)
3. **(Pointwise convergence)** $f_n(x) \to f(x)$ for all $x \in X$

Then $f$ is measurable and:
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu = \int \left(\lim_{n \to \infty} f_n\right) d\mu
$$
In other words, **the integral of the limit equals the limit of the integrals**.

**Remark 1.9 (Significance and Scope).** This theorem is remarkable because it requires no domination hypothesis. The sequence $\{f_n\}$ may converge to a function with infinite integral, and the theorem remains valid. The conclusion $\lim \int f_n = \int (\lim f_n)$ is the foundation for all subsequent convergence results in integration theory. Its proof, though elementary in structure, contains the α-trick—a technique that recurs throughout analysis whenever one must handle functions on sets of infinite measure.

*Proof.* The complete proof with full technical detail is provided in [[Day_2_exercises_FINAL#]]. We outline the strategy here.

**Proof Strategy:**
1. **Step 1 (Measurability):** Since $f(x) = \sup_n f_n(x)$ and each $f_n$ is measurable, $f$ is measurable (as supremum of measurable functions).

2. **Step 2 (Easy Inequality):** By monotonicity of the integral ([PROP-1.2.2]), $\int f_n \leq \int f_{n+1} \leq \int f$ for all $n$. Thus $\{\int f_n\}$ is an increasing sequence bounded above by $\int f$, hence $\lim_{n\to\infty} \int f_n$ exists and satisfies:
   $$\lim_{n \to \infty} \int f_n \, d\mu \leq \int f \, d\mu$$

3. **Step 3 (Hard Inequality via α-Trick):** This is the crux. We must show:
   $$\int f \, d\mu \leq \lim_{n \to \infty} \int f_n \, d\mu$$

   Fix an arbitrary simple function $0 \leq \varphi \leq f$. It suffices to prove:
   $$\int \varphi \, d\mu \leq \lim_{n \to \infty} \int f_n \, d\mu$$

   For any $\alpha \in (0,1)$, define:
   $$E_n = \{x \in X : f_n(x) \geq \alpha\varphi(x)\}$$

   Then $E_1 \subseteq E_2 \subseteq \cdots$ (by monotonicity of $f_n$) and $\bigcup_{n=1}^{\infty} E_n = X$. To see the exhaustion property, take any $x \in X$. If $\varphi(x) = 0$, then $\alpha\varphi(x) = 0$ for any $\alpha > 0$. Since $f_n(x) \geq 0$ for all $n$ (by hypothesis), we have $f_n(x) \geq 0 = \alpha\varphi(x)$ for all $n \geq 1$, so $x \in E_1$. In particular, $x \in \bigcup E_n$. If $\varphi(x) > 0$, then since $\alpha < 1$ and $\varphi(x) \leq f(x)$, we have $\alpha\varphi(x) < \varphi(x) \leq f(x)$. By pointwise convergence $f_n(x) \to f(x)$, there exists $N$ such that $f_N(x) \geq \alpha\varphi(x)$, so $x \in E_N \subseteq \bigcup_n E_n$. Thus $\bigcup_{n=1}^{\infty} E_n = X$.

   For each $n$:
   $$\int f_n \, d\mu \geq \int_{E_n} f_n \, d\mu \geq \alpha \int_{E_n} \varphi \, d\mu$$

   By continuity of measure from below ([LEM-1.2.1], as $E_n \uparrow X$):
   $$\lim_{n \to \infty} \int_{E_n} \varphi \, d\mu = \int_X \varphi \, d\mu$$

   Thus:
   $$\lim_{n \to \infty} \int f_n \, d\mu \geq \alpha \int \varphi \, d\mu$$

   Letting $\alpha \to 1^-$ and taking supremum over all simple $\varphi \leq f$:
   $$\lim_{n \to \infty} \int f_n \, d\mu \geq \int f \, d\mu$$

4. **Step 4 (Conclusion):** Combining Steps 2 and 3 yields equality. $\square$

**Completion of [PROP-1.2.2] (Linearity for Addition):** For non-negative measurable functions $f, g$, there exist increasing sequences $\{\varphi_n\}, \{\psi_n\}$ of simple functions with $\varphi_n \uparrow f$ and $\psi_n \uparrow g$ pointwise (by Exercise 1 in [[Day_2_exercises_FINAL#]]). Then $\varphi_n + \psi_n \uparrow f + g$, and by [THM-1.2.1], $\int(f+g) = \lim_n \int(\varphi_n + \psi_n) = \lim_n (\int \varphi_n + \int \psi_n) = \int f + \int g$.

**Corollary 1.2.1 (Countable Additivity of the Integral)** {#COR-1.2.1} Let $\{g_n\}$ be a sequence of non-negative measurable functions. Then:
$$
\int \left( \sum_{n=1}^{\infty} g_n \right) d\mu = \sum_{n=1}^{\infty} \int g_n \, d\mu
$$

*Proof.* Apply [THM-1.2.1] to the partial sums $f_N = \sum_{n=1}^{N} g_n$, which form a monotone increasing sequence converging to $\sum_{n=1}^{\infty} g_n$. $\square$

---

### **III. Computational Illustration: Verifying MCT Numerically**

To build intuition for the Monotone Convergence Theorem, we construct a concrete sequence of functions and verify numerically that the limit of integrals equals the integral of the limit. We begin with a continuous example for numerical clarity and computational simplicity.

**Remark.** For continuous functions on $[0,1]$, the Riemann and Lebesgue integrals coincide. The true power of the Lebesgue integral emerges when handling discontinuous functions. For a pathological example where Riemann integration fails catastrophically, see [[Day_2_Appendix_Numerical_Lebesgue_FINAL#]].

**Example 1.2.1 (A Monotonically Converging Sequence)** {#EX-1.2.1} Consider the functions on $[0,1]$:
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

This verifies [THM-1.2.1] for this particular sequence. We now implement this numerically.

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

**Interpretation:** The left panel demonstrates that the sequence of integrals $\{\int f_n\}$ converges monotonically to the integral of the limit function. The right panel shows the monotone pointwise convergence of the functions themselves. This numerical verification confirms the theoretical guarantee provided by [THM-1.2.1]: when a sequence of non-negative functions converges monotonically, we can interchange the limit and the integral.

**Technical Note:** The Riemann approximation used here is justified because each $f_n$ is continuous. For general measurable functions—such as those arising in the pathological examples of [[Day_2_Appendix_Numerical_Lebesgue_FINAL#]]—one would need to use more sophisticated numerical integration schemes based on approximation by simple functions. However, the conceptual verification remains the same: MCT guarantees that the numerical limit of integrals matches the integral of the numerical limit.

---

#### **Computational Illustration: MCT in Value Iteration**

We now demonstrate [THM-1.2.1] in a concrete reinforcement learning setting: value iteration on a simple finite-state MDP.

```python
import numpy as np
import matplotlib.pyplot as plt

# MDP specification: 5-state chain with non-negative rewards
np.random.seed(42)
S = 5  # number of states
A = 2  # number of actions
gamma = 0.9  # discount factor

# Transition probabilities P[s, a, s']
P = np.random.rand(S, A, S)
P = P / P.sum(axis=2, keepdims=True)  # normalize to get valid probabilities

# Non-negative rewards R[s, a]
R = np.random.rand(S, A) * 10

# Value iteration with V_0 = 0
V = np.zeros(S)
V_history = [V.copy()]

for n in range(50):
    Q = R + gamma * (P @ V)  # Q[s, a] = R[s, a] + γ Σ_s' P(s'|s,a) V(s')
    V_new = Q.max(axis=1)     # V_new(s) = max_a Q(s, a) (Bellman optimality)
    V_history.append(V_new.copy())

    # Check monotonicity
    if n > 0 and not np.all(V_new >= V - 1e-10):
        print(f"Warning: Monotonicity violated at iteration {n}")
    V = V_new

V_history = np.array(V_history)

# Verify monotonicity property
monotonicity_check = np.all(np.diff(V_history, axis=0) >= -1e-10)
print(f"Monotonicity verified: {monotonicity_check}")

# Compute expected value under uniform initial distribution
mu = np.ones(S) / S  # uniform distribution
E_V = [mu @ V_n for V_n in V_history]

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left panel: Value function convergence for each state
for s in range(S):
    axes[0].plot(V_history[:, s], label=f'$V_n(s_{s})$', alpha=0.7, linewidth=1.5)
axes[0].set_xlabel('Iteration $n$', fontsize=12)
axes[0].set_ylabel('$V_n(s)$', fontsize=12)
axes[0].set_title('Monotone Convergence: $V_n(s) \\uparrow V^*(s)$ for each $s$', fontsize=12)
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

# Right panel: Expected value convergence (MCT guarantee)
axes[1].plot(E_V, 'b.-', markersize=8, linewidth=2, label='$\\mathbb{E}_\\mu[V_n(S_0)]$')
axes[1].axhline(E_V[-1], color='r', linestyle='--', linewidth=2,
                label=f'$\\mathbb{E}_\\mu[V^*] \\approx {E_V[-1]:.3f}$')
axes[1].set_xlabel('Iteration $n$', fontsize=12)
axes[1].set_ylabel('Expected Value', fontsize=12)
axes[1].set_title('MCT: $\\lim_{n \\to \\infty} \\mathbb{E}_\\mu[V_n] = \\mathbb{E}_\\mu[V^*]$',
                   fontsize=12)
axes[1].legend(fontsize=11)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/Day2_MCT_ValueIteration.png', dpi=150)

print(f"\n{'='*70}")
print("MCT in Value Iteration: Numerical Verification")
print(f"{'='*70}")
print(f"Initial expected value: E[V_0] = {E_V[0]:.6f}")
print(f"After 10 iterations:    E[V_10] = {E_V[10]:.6f}")
print(f"After 50 iterations:    E[V_50] = {E_V[-1]:.6f}")
print(f"\nMonotonicity: V_0 ≤ V_1 ≤ ... ≤ V_50 ✓")
print(f"Convergence rate: approximately geometric with rate γ = {gamma}")
print(f"\nMCT guarantees: lim E[V_n] = E[lim V_n] = E[V*] = {E_V[-1]:.6f}")

plt.show()
```

**Key Observations:**
1. **Monotonicity:** Each iterate $V_n(s) \leq V_{n+1}(s)$ for all states $s$, verified numerically
2. **Pointwise Convergence:** $V_n(s) \to V^*(s)$ for each state (visible in left panel)
3. **MCT Application:** The expected value $\mathbb{E}_\mu[V_n(S_0)] = \sum_s \mu(s) V_n(s)$ converges to $\mathbb{E}_\mu[V^*(S_0)]$ by [THM-1.2.1]
4. **Practical Impact:** Without MCT, we could not rigorously justify stopping value iteration after $N$ steps and using $\mathbb{E}_\mu[V_N]$ as an approximation to optimal expected return

This computational experiment demonstrates that [THM-1.2.1] is not an abstract theorem—it is the mathematical guarantee enabling finite-time approximation of optimal policies in reinforcement learning.

---

### **IV. Application Bridge: Monotone Convergence in Reinforcement Learning**

The Monotone Convergence Theorem is not an abstract curiosity. It is the mathematical guarantee that underpins the convergence of the most fundamental algorithms in reinforcement learning. We now make this connection explicit.

#### **A. Value Iteration as Monotone Convergence**

In the theory of Markov Decision Processes, the **value iteration algorithm** is a fundamental method for computing optimal value functions. Starting from an initial guess $V_0$ (typically $V_0 = 0$ or $V_0 = \mathbf{0}$), we iteratively apply the Bellman optimality operator:
$$
V_{n+1} = T^* V_n, \qquad \text{where} \quad (T^* V)(s) = \max_{a \in \mathcal{A}} \left\{ R(s,a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s,a) V(s') \right\}
$$

**Theorem 1.2.2 (Monotonicity of Value Iteration - Statement Only)** {#THM-1.2.2} Assume:
1. The reward function is non-negative: $R(s,a) \geq 0$ for all $(s,a)$
2. The discount factor satisfies $\gamma \in [0,1)$
3. The initial value function is $V_0 = 0$

Then:
1. The sequence $\{V_n\}$ is monotone increasing: $0 = V_0 \leq V_1 \leq V_2 \leq \cdots$
2. The sequence converges pointwise to the optimal value function: $V_n(s) \to V^*(s)$ for all $s \in \mathcal{S}$
3. The Bellman operator $T^*$ is a $\gamma$-contraction in the supremum norm, ensuring exponential convergence at rate $\gamma^n$

*Note:* The proof requires the Banach Fixed Point Theorem, which will be established in Week 13 (Functional Analysis). We provide this result now for motivation; readers may take it on faith or consult [@puterman:mdp:2014, §6.3].

**Connection to MCT:** In finite-state MDPs, for a given initial state distribution $\mu$ on $\mathcal{S}$ (where $\mu(s) \geq 0$ and $\sum_{s} \mu(s) = 1$), let $S_0 \sim \mu$ denote a random initial state. The value function $V_n(s)$ is a deterministic vector in $\mathbb{R}^{|\mathcal{S}|}$, but the random variable $V_n(S_0)$ has expectation:
$$
\mathbb{E}_{\mu}[V_n(S_0)] = \sum_{s \in \mathcal{S}} \mu(s) V_n(s) = \int V_n \, d\mu
$$
where the integral is with respect to the discrete measure $\mu$ on the σ-algebra $2^{\mathcal{S}}$.

The **Monotone Convergence Theorem** ([THM-1.2.1]) applies because:
- **(i) Non-negativity:** $V_n(s) \geq 0$ for all $s \in \mathcal{S}$, all $n$ (from [THM-1.2.2])
- **(ii) Monotonicity:** $V_n(s) \leq V_{n+1}(s)$ for all $s \in \mathcal{S}$ (pointwise increasing)
- **(iii) Pointwise convergence:** $V_n(s) \to V^*(s)$ for all $s \in \mathcal{S}$ (from [THM-1.2.2])
- **(iv) Measurability:** All functions are measurable with respect to the discrete σ-algebra $2^{\mathcal{S}}$

Thus [THM-1.2.1] guarantees:
$$
\lim_{n \to \infty} \mathbb{E}_{\mu}[V_n(S_0)] = \mathbb{E}_{\mu}\left[\lim_{n \to \infty} V_n(S_0)\right] = \mathbb{E}_{\mu}[V^*(S_0)]
$$

This justifies the practice of approximating $V^*$ by running value iteration for finitely many steps: not only does $V_n$ converge pointwise to $V^*$, but its expected value (the policy's performance) also converges. Without [THM-1.2.1], we would have no guarantee that finite-time performance $\mathbb{E}_{\mu}[V_N]$ approximates the optimal performance $\mathbb{E}_{\mu}[V^*]$.

#### **B. Policy Evaluation and Temporal Difference Learning**

In **policy evaluation**, we seek to compute $V^{\pi}$, the value function of a fixed policy $\pi$. The Bellman consistency equation is:
$$
V^{\pi} = T^{\pi} V^{\pi}, \qquad \text{where} \quad (T^{\pi} V)(s) = R^{\pi}(s) + \gamma \sum_{s'} P^{\pi}(s'|s) V(s')
$$

Starting from $V_0 = 0$ (or any initial guess), the sequence $V_n = (T^{\pi})^n V_0$ converges to $V^{\pi}$. When rewards are non-negative, this convergence is monotone, and [THM-1.2.1] applies as in the value iteration case.

**Note:** This paragraph previews advanced material from Chapter 7 (Stochastic Approximation). Readers encountering these concepts for the first time should focus on the deterministic value iteration case (Section IV.A), where MCT applies directly. The stochastic case requires additional tools (Dominated Convergence Theorem, martingale theory) that we will develop systematically in later chapters.

We briefly preview a stochastic algorithm (full details in Chapter 7) to illustrate convergence theorems' role in probabilistic analysis. **Temporal Difference (TD) Learning** is a stochastic approximation algorithm for policy evaluation. The TD(0) update is:
$$
V_{t+1}(s_t) = V_t(s_t) + \alpha_t \left[R_t + \gamma V_t(s_{t+1}) - V_t(s_t)\right]
$$

Under appropriate conditions on the step sizes $\{\alpha_t\}$—specifically, the **Robbins-Monro conditions**: $\sum \alpha_t = \infty$ and $\sum \alpha_t^2 < \infty$ (the first ensures infinite exploration, preventing premature convergence; the second ensures bounded noise accumulation)—and the ergodicity of the Markov chain induced by $\pi$, TD learning converges to $V^{\pi}$ almost surely.

The convergence analysis relies on the **ODE method of stochastic approximation**, which uses the **Dominated Convergence Theorem** (Day 3)—not MCT directly—to justify interchanging limits and expectations under stochastic noise. MCT alone is insufficient because TD iterates fluctuate due to sampling noise and are not monotone. However, for deterministic policy evaluation (the iterates $V_n = (T^{\pi})^n V_0$), [THM-1.2.1] does apply when rewards are non-negative. This connection will be made fully rigorous when we study stochastic approximation theory in Chapter 7.

**Key Insight:** The Monotone Convergence Theorem is not merely a technical curiosity. It is the mathematical foundation that ensures the convergence of the most fundamental algorithms in reinforcement learning. Without [THM-1.2.1], we could not rigorously prove that value iteration or policy evaluation converge to the correct value function, even in the simplest finite-state setting.

---

### **V. Reflection and Forward Connections**

#### **Mathematical Insight**

The proof of [THM-1.2.1] hinges on two pillars:
1. **Monotonicity of measures:** If $\{E_n\}$ is an increasing sequence of sets, then $\mu(\bigcup E_n) = \lim \mu(E_n)$ (continuity from below, [LEM-1.2.1])
2. **Approximation by simple functions:** Any non-negative measurable function can be approximated from below by simple functions ([DEF-1.2.1])

The **α-trick** in Step 3 of the proof is subtle but crucial. When dealing with a simple function $\varphi$ that may equal the limit $f$ on a set of infinite measure, we cannot directly use the inequality $\int f_n \geq \int \varphi$ and pass to the limit. The issue is that on the complement of $E_n = \{x : f_n(x) \geq \varphi(x)\}$, we have $f_n < \varphi$, and if $\mu(E_n^c)$ remains bounded away from zero for all $n$, we cannot conclude that $\int f_n \to \int \varphi$.

Instead, we "deflate" $\varphi$ slightly by multiplying by $\alpha \in (0,1)$, obtaining sets $E_n = \{x : f_n(x) \geq \alpha\varphi(x)\}$ where the inequality is strict off of $E_n^c$. This allows us to use the continuity of measure on the increasing sequence $\{E_n\}$ to conclude $\bigcup E_n = X$. The α-trick is a recurring technique in analysis whenever one must handle functions on sets of infinite measure.

#### **RL Connection**

The Monotone Convergence Theorem provides the theoretical justification for several key results in RL:

1. **Value Iteration Convergence:** Starting from $V_0 = 0$, the sequence $V_n = (T^*)^n V_0$ converges monotonically to $V^*$, and $\mathbb{E}[V_n] \to \mathbb{E}[V^*]$ by [THM-1.2.1]
2. **Policy Evaluation:** For non-negative rewards, evaluating $V^{\pi}$ via iterated application of $T^{\pi}$ yields monotone convergence
3. **Stochastic Approximation:** The ODE method for analyzing TD learning relies on convergence theorems to justify interchanging limits and expectations

Without [THM-1.2.1], we would lack rigorous proofs that these algorithms converge to the correct value functions.

#### **Open Questions**

1. **Relaxation of Monotonicity:** Can [THM-1.2.1] be extended to sequences that are "almost monotone" (i.e., $f_n \leq f_{n+1}$ except on a set of measure zero)? The answer is affirmative: since integration ignores null sets ([DEF-1.1.7] from Day 1), we can modify $f_n$ on the exceptional set without changing its integral, reducing to the standard MCT case. This observation is crucial in stochastic approximation, where iterates are only defined almost surely (i.e., outside of negligible exceptional sets).

2. **Rate of Convergence:** [THM-1.2.1] guarantees $\int f_n \to \int f$, but provides no information about the rate of convergence. For RL applications, we care about sample complexity. Does monotone convergence of value functions imply a specific convergence rate for expected returns? This question connects to the contraction rate of the Bellman operator and the mixing time of the Markov chain.

3. **Generalization to Negative Functions:** What happens if $f_n$ are not non-negative? The sequence $f_n(x) = -1/n$ converges monotonically to $f(x) = 0$, and we have:
   $$\int_0^1 f_n(x)\,dx = -1/n \to 0 = \int_0^1 f(x)\,dx$$
   So MCT's conclusion holds in this case. However, for signed functions the Lebesgue integral may be undefined due to the indeterminate form $\infty - \infty$ (even when pointwise limits exist). This motivates the study of **Fatou's Lemma** and the **Dominated Convergence Theorem** (Day 3), which replace monotonicity with non‑negativity or domination to control integrability throughout the limit.

---

Tomorrow (Day 3), we will address the final point by developing **Fatou's Lemma** and the **Dominated Convergence Theorem**, which relax the hypotheses of MCT. These three theorems—MCT, Fatou, and DCT—form the **triumvirate of convergence** in integration theory, and they are the mathematical bedrock upon which the entire edifice of stochastic optimization and reinforcement learning is constructed.
[[Day_1_FINAL#]]

### Agenda:

##### 📘 Day 2 – Week 1: The Lebesgue Integral and Monotone Convergence
**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (40 min) – Reading**

**Topic:** _Construction of the Lebesgue integral and convergence theorems_

- Read from [@folland:real_analysis:1999, §2.1–2.2] or equivalent in [@durrett:probability:2019, Ch.2].
- Focus on:
    - Construction pathway: simple functions $\to$ non-negative measurable $\to$ general measurable
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

**Challenge 1: Discontinuous Functions.** The indicator functions of events—fundamental to probability—are not Riemann integrable on arbitrary measurable sets. Consider the indicator function of the rationals: $\varphi(x) = \mathbf{1}_\mathbb{Q}(x)$ on $[0,1]$. This function is 1 on a dense set ($\mathbb{Q} \cap [0,1]$) of Lebesgue measure zero, and 0 on a dense set (($\mathbb{R} \setminus \mathbb{Q}) \cap [0,1]$) of measure 1. Every Riemann partition has both rationals and irrationals, so upper sums equal 1 and lower sums equal 0, preventing convergence. However, the Lebesgue integral equals 0 because $\mu(\mathbb{Q} \cap [0,1]) = 0$. In reinforcement learning, consider the event "agent reaches goal state"—represented by $\mathbf{1}_{\text{goal}}(s)$, an indicator function. If the goal region has fractured geometry (common in robotics with obstacle-rich environments), this function is discontinuous at the boundary, rendering Riemann integration inadequate.

**Challenge 2: Unbounded Domains.** State spaces in continuous control are often $\mathbb{R}^n$, which has infinite Lebesgue measure. Value functions may have support on all of $\mathbb{R}^n$, and the Riemann integral—fundamentally tied to compact domains—is inadequate for this setting.

**Challenge 3: Interchange of Limits and Integrals.** Algorithms like value iteration produce sequences of value functions $V_n \to V^*$. We need theorems guaranteeing $\mathbb{E}[V_n] \to \mathbb{E}[V^*]$ under appropriate conditions. The pathological examples that plague the Riemann theory—where pointwise convergence does not imply convergence of integrals—must be tamed.

The Riemann integral, defined via partitions of the domain, fails on all three counts. The **Lebesgue integral**, constructed by partitioning the *range* rather than the domain, succeeds completely. This section develops the Lebesgue integral from first principles, culminating in the **Monotone Convergence Theorem**—the first and most fundamental result enabling interchange of limits and integrals.

**Learning Objectives:**
* Understand the three-stage construction: simple functions $\to$ non-negative functions $\to$ general functions
* Appreciate why measurability ([DEF-1.1.3] from Day 1) is prerequisite for integration
* Master the Monotone Convergence Theorem and its proof technique (the α-trick)
* Recognize MCT as the foundation for proving convergence of value iteration

---

### **I. Core Theory: The Construction Hierarchy**

The Lebesgue integral is defined through a careful bootstrap procedure. We begin with the simplest class of functions—those taking only finitely many values—and extend systematically. At each stage, we verify that the essential properties (linearity, monotonicity, countable additivity) are preserved.

#### **A. Simple Functions: The Foundation**

The edifice of Lebesgue integration rests upon the humble class of simple functions. These are the discrete approximations from which all measurable functions shall be constructed.

**Definition 1.2.1 (Simple Function)** {#DEF-1.2.1} Let $(X, \mathcal{F}, \mu)$ be a measure space ([DEF-1.1.1] from Day 1). A function $\varphi: X \to \mathbb{R}$ is **simple** if there exist finitely many measurable sets $A_1, \ldots, A_n \in \mathcal{F}$ (not necessarily disjoint or exhaustive) and constants $a_1, \ldots, a_n \in \mathbb{R}$ such that:
$$
\varphi(x) = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}(x)
$$

Measurability of $\varphi$ follows from the measurability of the $A_i$ and finite linearity of measurable functions. The **canonical form** is obtained when the $\{A_i\}$ are the level sets of distinct values and form a partition of $X$. In the canonical form, $a_1, \ldots, a_n$ are the distinct values of $\varphi$ and $A_i = \{x : \varphi(x) = a_i\}$.

**Remark 1.6 (Non-Uniqueness of Representation).** A simple function has infinitely many representations (e.g., subdividing the $A_i$), but the **canonical form** with distinct values $\{a_i\}$ and corresponding level sets $\{A_i = \{x : \varphi(x) = a_i\}\}$ is unique. For the purposes of [DEF-1.2.2], the integral is independent of representation, as will be verified in the proof of [PROP-1.2.1].

**Definition 1.2.2 (Integral of Simple Functions)** {#DEF-1.2.2} For a non-negative simple function $\varphi = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}$ with $a_i \geq 0$, we define:
$$
\int \varphi \, d\mu = \sum_{i=1}^{n} a_i \mu(A_i)
$$
where the convention $0 \cdot \infty = 0$ is adopted.[^convention]

[^convention]: More precisely, if $a_i = 0$ in the canonical representation, then $a_i \mu(A_i) = 0$ regardless of whether $\mu(A_i)$ is finite or infinite. This convention is consistent with the interpretation that "integrating the zero function over any set yields zero," and is essential for well-definedness when dealing with measure spaces having sets of infinite measure.

**Justification of Convention.** If $a_i = 0$, the contribution of $A_i$ to the integral should be zero regardless of $\mu(A_i)$, even if $\mu(A_i) = \infty$. This is consistent with the intuition that "integrating zero over any set yields zero."

**Proposition 1.2.1 (Properties of the Integral on Simple Functions)** {#PROP-1.2.1}
Let $\varphi, \psi$ be non-negative simple functions, and $c \geq 0$ a constant. Then:
1. **(Linearity)** $\displaystyle\int (c\varphi + \psi) \, d\mu = c \int \varphi \, d\mu + \int \psi \, d\mu$
2. **(Monotonicity)** If $\varphi \leq \psi$ pointwise, then $\displaystyle\int \varphi \, d\mu \leq \int \psi \, d\mu$
3. **(Countable Additivity on Domain)** If $\{A_n\}$ are disjoint measurable sets with $\bigcup_{n=1}^{\infty} A_n = X$, then:
   $$
   \int_X \varphi \, d\mu = \sum_{n=1}^{\infty} \int_{A_n} \varphi \, d\mu
   $$

*Proof.*
**(1) Linearity:** Let $\varphi = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ and $\psi = \sum_{j=1}^m b_j \mathbf{1}_{B_j}$ be in canonical form. Consider the common refinement $\mathcal{R} = \{A_i \cap B_j : i=1,\ldots,n,\, j=1,\ldots,m\}$. Since $\mathcal{F}$ is a $\sigma$-algebra, finite intersections $A_i \cap B_j$ are measurable. The collection $\mathcal{R} = \{A_i \cap B_j : i=1,...,n, j=1,...,m\}$ forms a partition of $X$ because the $\{A_i\}$ partition $X$ and the $\{B_j\}$ partition $X$. Any $x \in X$ belongs to exactly one $A_i$ and exactly one $B_j$, hence to exactly one element $A_i \cap B_j \in \mathcal{R}$.

On each set $R \in \mathcal{R}$, both $\varphi$ and $\psi$ are constant. Write $\varphi = \sum_{R \in \mathcal{R}} \alpha_R \mathbf{1}_R$ and $\psi = \sum_{R \in \mathcal{R}} \beta_R \mathbf{1}_R$. Then:
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
By countable additivity of $\mu$ ([DEF-1.1.1] from Day 1):
$$
\sum_{n=1}^{\infty} \int_{A_n} \varphi \, d\mu = \sum_{i=1}^n a_i \sum_{n=1}^{\infty} \mu(A_i \cap A_n) = \sum_{i=1}^n a_i \mu\left(A_i \cap \bigcup_{n=1}^{\infty} A_n\right) = \sum_{i=1}^n a_i \mu(A_i) = \int_X \varphi \, d\mu
$$
$\square$

#### **B. Non-Negative Measurable Functions: Extension by Supremum**

Having defined integration for simple functions—the discrete scaffolding—we now extend to the continuous structure of all non-negative measurable functions via a supremum construction. This is the crucial conceptual leap of the Lebesgue approach.

How should we extend integration from simple functions to general measurable functions? The Riemann approach partitions the domain into intervals; the Lebesgue approach instead approximates the *function itself* from below with simple functions. For a non-negative measurable function $f$, we ask: what is the supremal integral among all simple functions that underestimate $f$? This supremum—if it exists—should be the integral of $f$.

**Definition 1.2.3 (Integral of Non-Negative Functions)** {#DEF-1.2.3} Let $f: X \to [0, \infty]$ be a measurable function. We define:
$$
\int f \, d\mu = \sup \left\{ \int \varphi \, d\mu \;\Big|\; 0 \leq \varphi \leq f, \, \varphi \text{ simple} \right\} \in [0, \infty]
$$
This supremum exists because: (i) the set is nonempty (contains $\varphi \equiv 0$), and (ii) any supremum of a nonempty subset of $[0, \infty]$ exists in the extended reals.

**Remark 1.7 (Geometric Intuition).** The integral of $f$ is the "area under the curve" computed by approximating $f$ from below with increasingly fine step functions. Unlike the Riemann integral, which partitions the domain into intervals and forms rectangles based on function values at sample points, the Lebesgue approach partitions the **range** of $f$ into levels, measuring the sets $\{x : f(x) > t\}$ for each $t \geq 0$. This reversal—from domain partition to range partition—is what enables handling discontinuous functions.

**Proposition 1.2.2 (Extension of Properties to Non-Negative Functions)** {#PROP-1.2.2}
For measurable $f, g: X \to [0, \infty]$ and $c \geq 0$:
1. **(Linearity)** $\displaystyle\int (cf + g) \, d\mu = c \int f \, d\mu + \int g \, d\mu$
2. **(Monotonicity)** If $f \leq g$ almost everywhere, then $\displaystyle\int f \, d\mu \leq \int g \, d\mu$
3. **(Countable Additivity)** If $\{A_n\}$ are disjoint in $\mathcal{F}$, then:
   $$
   \int_{\bigcup_{n=1}^{\infty} A_n} f \, d\mu = \sum_{n=1}^{\infty} \int_{A_n} f \, d\mu
   $$

*Proof.* We establish each property step by step.

**(2) Monotonicity:** If $f \leq g$ a.e., then for any simple $\varphi \leq f$, we have $\varphi \leq g$ a.e., so $\int \varphi \leq \int g$. Taking supremum over $\varphi$ gives $\int f \leq \int g$.

**(3) Countable additivity:** Follows from MCT applied to the partial sums (proof deferred to after [THM-1.2.1]).

**(1) Linearity:** We defer the complete proof of linearity for addition until after [THM-1.2.1] is established, as the proof requires MCT. For scalar multiplication: if $c \geq 0$ and $\varphi \leq f$ is simple, then $c\varphi \leq cf$ is simple, and $\int c\varphi = c\int \varphi$ by linearity for simple functions ([PROP-1.2.1]). Taking the supremum over all $\varphi \leq f$ gives $\int cf = c\int f$. $\square$

**Remark 1.7A.** The proof of linearity for addition requires MCT to avoid circularity. After establishing [THM-1.2.1], we will complete the proof using approximation by simple functions. For a direct proof without MCT, see [@folland:real_analysis:1999, §2.2, Thm 2.10].

#### **C. General Measurable Functions: Decomposition into Positive and Negative Parts**

To integrate functions that take both positive and negative values, we decompose them into positive and negative components. This is the final stage of the construction.

**Definition 1.2.4 (Positive and Negative Parts)** {#DEF-1.2.4} For a measurable function $f: X \to \mathbb{R}$, define:
$$
f^+(x) = \max\{f(x), 0\}, \qquad f^-(x) = \max\{-f(x), 0\}
$$
Then $f = f^+ - f^-$ and $|f| = f^+ + f^-$. Both $f^+$ and $f^-$ are non-negative measurable functions.

**Remark 1.7B.** Note that $f^+$ and $f^-$ are *never simultaneously nonzero* at any point: if $f(x) > 0$, then $f^+(x) = f(x)$ and $f^-(x) = 0$; if $f(x) < 0$, then $f^+(x) = 0$ and $f^-(x) = -f(x)$; if $f(x) = 0$, both vanish. Thus $f^+ \cdot f^- = 0$ pointwise, which ensures the decomposition $f = f^+ - f^-$ is unambiguous.

**Definition 1.2.5 (Integral of General Functions)** {#DEF-1.2.5} A measurable function $f: X \to \mathbb{R}$ is **integrable** (or **Lebesgue integrable**) if $\int |f| \, d\mu < \infty$. For such $f$, we define:
$$
\int f \, d\mu = \int f^+ \, d\mu - \int f^- \, d\mu
$$
Since both $\int f^+ \, d\mu$ and $\int f^- \, d\mu$ are finite, this difference is well-defined.

**Notation.** We write $f \in L^1(\mu)$ to denote that $f$ is integrable. The space $L^1(\mu)$ is the collection of all (equivalence classes of) integrable functions, where two functions are identified if they differ only on a set of measure zero ([DEF-1.1.7] from Day 1).

**Remark 1.8 (Why Integrability Requires Finiteness).** If $\int f^+ \, d\mu = \int f^- \, d\mu = \infty$, the difference "$\infty - \infty$" is undefined in extended real arithmetic. This motivates the restriction to functions with $\int |f| \, d\mu < \infty$. In probability, this condition corresponds to requiring finite expectation: $\mathbb{E}[|X|] < \infty$. For the standard Cauchy distribution with density $f(x) = 1/(\pi(1 + x^2))$ one has
$$\int_{-\infty}^{\infty} |x| f(x) \, dx = \frac{2}{\pi} \int_0^{\infty} \frac{x}{1+x^2} \, dx = \frac{1}{\pi}[\ln(1+x^2)]_0^{\infty} = \infty,$$
so $\mathbb{E}[|X|] = \infty$ and the random variable $X$ is not integrable (even though the density integrates to 1).

---

### **II. The Monotone Convergence Theorem: Guaranteeing Limit-Integral Interchange**

The power of the Lebesgue integral lies not merely in its ability to integrate a broader class of functions than the Riemann integral, but in its robust convergence theorems. The **Monotone Convergence Theorem** is the cornerstone, the first and most fundamental result that permits interchange of limits and integrals.

**Lemma 1.2.1 (Continuity of Measure from Below)** {#LEM-1.2.1} Let $(X, \mathcal{F}, \mu)$ be a measure space. If $\{E_n\}$ is an increasing sequence of measurable sets ($E_1 \subseteq E_2 \subseteq \cdots$) with $E = \bigcup_{n=1}^{\infty} E_n$, then:
$$
\mu(E) = \lim_{n \to \infty} \mu(E_n)
$$

*Proof.* Define $F_1 = E_1$ and $F_n = E_n \setminus E_{n-1}$ for $n \geq 2$. The sets $\{F_n\}$ are pairwise disjoint with $\bigcup F_n = E$. By countable additivity:
$$
\mu(E) = \sum_{n=1}^{\infty} \mu(F_n) = \lim_{N \to \infty} \sum_{n=1}^{N} \mu(F_n) = \lim_{N \to \infty} \mu(E_N)
$$
where the last equality follows from $E_N = \bigcup_{n=1}^{N} F_n$. $\square$

**Theorem 1.2.1 (Monotone Convergence Theorem – Beppo Levi)** {#THM-1.2.1} Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^{\infty}$ be a sequence of measurable functions satisfying:
1. **(Non-negativity)** $f_n \geq 0$ for all $n$
2. **(Monotonicity)** $f_1(x) \leq f_2(x) \leq f_3(x) \leq \cdots$ for all $x \in X$ (pointwise monotonicity)
3. **(Pointwise convergence)** $f_n(x) \to f(x)$ for all $x \in X$

Then $f$ is measurable and:
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu = \int \left(\lim_{n \to \infty} f_n\right) d\mu
$$
In other words, **the integral of the limit equals the limit of the integrals**.

**Remark 1.9 (Significance and Scope).** This theorem is remarkable because it requires no domination hypothesis. The sequence $\{f_n\}$ may converge to a function with infinite integral, and the theorem remains valid. The conclusion $\lim \int f_n = \int (\lim f_n)$ is the foundation for all subsequent convergence results in integration theory. Its proof, though elementary in structure, contains the α-trick—a technique that recurs throughout analysis whenever one must handle functions on sets of infinite measure.

*Proof.* The complete proof with full technical detail is provided in [[Day_2_exercises_FINAL#]]. We outline the strategy here.

**Proof Strategy:**
1. **Step 1 (Measurability):** Since $f(x) = \sup_n f_n(x)$ and each $f_n$ is measurable, $f$ is measurable (as supremum of measurable functions).

2. **Step 2 (Easy Inequality):** By monotonicity of the integral ([PROP-1.2.2]), $\int f_n \leq \int f_{n+1} \leq \int f$ for all $n$. Thus $\{\int f_n\}$ is an increasing sequence bounded above by $\int f$, hence $\lim_{n\to\infty} \int f_n$ exists and satisfies:
   $$\lim_{n \to \infty} \int f_n \, d\mu \leq \int f \, d\mu$$

3. **Step 3 (Hard Inequality via α-Trick):** This is the crux. We must show:
   $$\int f \, d\mu \leq \lim_{n \to \infty} \int f_n \, d\mu$$

   Fix an arbitrary simple function $0 \leq \varphi \leq f$. It suffices to prove:
   $$\int \varphi \, d\mu \leq \lim_{n \to \infty} \int f_n \, d\mu$$

   For any $\alpha \in (0,1)$, define:
   $$E_n = \{x \in X : f_n(x) \geq \alpha\varphi(x)\}$$

   Then $E_1 \subseteq E_2 \subseteq \cdots$ (by monotonicity of $f_n$) and $\bigcup_{n=1}^{\infty} E_n = X$. To see the exhaustion property, take any $x \in X$. If $\varphi(x) = 0$, then $\alpha\varphi(x) = 0$ for any $\alpha > 0$. Since $f_n(x) \geq 0$ for all $n$ (by hypothesis), we have $f_n(x) \geq 0 = \alpha\varphi(x)$ for all $n \geq 1$, so $x \in E_1$. In particular, $x \in \bigcup E_n$. If $\varphi(x) > 0$, then since $\alpha < 1$ and $\varphi(x) \leq f(x)$, we have $\alpha\varphi(x) < \varphi(x) \leq f(x)$. By pointwise convergence $f_n(x) \to f(x)$, there exists $N$ such that $f_N(x) \geq \alpha\varphi(x)$, so $x \in E_N \subseteq \bigcup_n E_n$. Thus $\bigcup_{n=1}^{\infty} E_n = X$.

   For each $n$:
   $$\int f_n \, d\mu \geq \int_{E_n} f_n \, d\mu \geq \alpha \int_{E_n} \varphi \, d\mu$$

   By continuity of measure from below ([LEM-1.2.1], as $E_n \uparrow X$):
   $$\lim_{n \to \infty} \int_{E_n} \varphi \, d\mu = \int_X \varphi \, d\mu$$

   Thus:
   $$\lim_{n \to \infty} \int f_n \, d\mu \geq \alpha \int \varphi \, d\mu$$

   Letting $\alpha \to 1^-$ and taking supremum over all simple $\varphi \leq f$:
   $$\lim_{n \to \infty} \int f_n \, d\mu \geq \int f \, d\mu$$

4. **Step 4 (Conclusion):** Combining Steps 2 and 3 yields equality. $\square$

**Completion of [PROP-1.2.2] (Linearity for Addition):** For non-negative measurable functions $f, g$, there exist increasing sequences $\{\varphi_n\}, \{\psi_n\}$ of simple functions with $\varphi_n \uparrow f$ and $\psi_n \uparrow g$ pointwise (by Exercise 1 in [[Day_2_exercises_FINAL#]]). Then $\varphi_n + \psi_n \uparrow f + g$, and by [THM-1.2.1], $\int(f+g) = \lim_n \int(\varphi_n + \psi_n) = \lim_n (\int \varphi_n + \int \psi_n) = \int f + \int g$.

**Corollary 1.2.1 (Countable Additivity of the Integral)** {#COR-1.2.1} Let $\{g_n\}$ be a sequence of non-negative measurable functions. Then:
$$
\int \left( \sum_{n=1}^{\infty} g_n \right) d\mu = \sum_{n=1}^{\infty} \int g_n \, d\mu
$$

*Proof.* Apply [THM-1.2.1] to the partial sums $f_N = \sum_{n=1}^{N} g_n$, which form a monotone increasing sequence converging to $\sum_{n=1}^{\infty} g_n$. $\square$

---

### **III. Computational Illustration: Verifying MCT Numerically**

To build intuition for the Monotone Convergence Theorem, we construct a concrete sequence of functions and verify numerically that the limit of integrals equals the integral of the limit. We begin with a continuous example for numerical clarity and computational simplicity.

**Remark.** For continuous functions on $[0,1]$, the Riemann and Lebesgue integrals coincide. The true power of the Lebesgue integral emerges when handling discontinuous functions. For a pathological example where Riemann integration fails catastrophically, see [[Day_2_Appendix_Numerical_Lebesgue_FINAL#]].

**Example 1.2.1 (A Monotonically Converging Sequence)** {#EX-1.2.1} Consider the functions on $[0,1]$:
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

This verifies [THM-1.2.1] for this particular sequence. We now implement this numerically.

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

**Interpretation:** The left panel demonstrates that the sequence of integrals $\{\int f_n\}$ converges monotonically to the integral of the limit function. The right panel shows the monotone pointwise convergence of the functions themselves. This numerical verification confirms the theoretical guarantee provided by [THM-1.2.1]: when a sequence of non-negative functions converges monotonically, we can interchange the limit and the integral.

**Technical Note:** The Riemann approximation used here is justified because each $f_n$ is continuous. For general measurable functions—such as those arising in the pathological examples of [[Day_2_Appendix_Numerical_Lebesgue_FINAL#]]—one would need to use more sophisticated numerical integration schemes based on approximation by simple functions. However, the conceptual verification remains the same: MCT guarantees that the numerical limit of integrals matches the integral of the numerical limit.

---

#### **Computational Illustration: MCT in Value Iteration**

We now demonstrate [THM-1.2.1] in a concrete reinforcement learning setting: value iteration on a simple finite-state MDP.

```python
import numpy as np
import matplotlib.pyplot as plt

# MDP specification: 5-state chain with non-negative rewards
np.random.seed(42)
S = 5  # number of states
A = 2  # number of actions
gamma = 0.9  # discount factor

# Transition probabilities P[s, a, s']
P = np.random.rand(S, A, S)
P = P / P.sum(axis=2, keepdims=True)  # normalize to get valid probabilities

# Non-negative rewards R[s, a]
R = np.random.rand(S, A) * 10

# Value iteration with V_0 = 0
V = np.zeros(S)
V_history = [V.copy()]

for n in range(50):
    Q = R + gamma * (P @ V)  # Q[s, a] = R[s, a] + γ Σ_s' P(s'|s,a) V(s')
    V_new = Q.max(axis=1)     # V_new(s) = max_a Q(s, a) (Bellman optimality)
    V_history.append(V_new.copy())

    # Check monotonicity
    if n > 0 and not np.all(V_new >= V - 1e-10):
        print(f"Warning: Monotonicity violated at iteration {n}")
    V = V_new

V_history = np.array(V_history)

# Verify monotonicity property
monotonicity_check = np.all(np.diff(V_history, axis=0) >= -1e-10)
print(f"Monotonicity verified: {monotonicity_check}")

# Compute expected value under uniform initial distribution
mu = np.ones(S) / S  # uniform distribution
E_V = [mu @ V_n for V_n in V_history]

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left panel: Value function convergence for each state
for s in range(S):
    axes[0].plot(V_history[:, s], label=f'$V_n(s_{s})$', alpha=0.7, linewidth=1.5)
axes[0].set_xlabel('Iteration $n$', fontsize=12)
axes[0].set_ylabel('$V_n(s)$', fontsize=12)
axes[0].set_title('Monotone Convergence: $V_n(s) \\uparrow V^*(s)$ for each $s$', fontsize=12)
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

# Right panel: Expected value convergence (MCT guarantee)
axes[1].plot(E_V, 'b.-', markersize=8, linewidth=2, label='$\\mathbb{E}_\\mu[V_n(S_0)]$')
axes[1].axhline(E_V[-1], color='r', linestyle='--', linewidth=2,
                label=f'$\\mathbb{E}_\\mu[V^*] \\approx {E_V[-1]:.3f}$')
axes[1].set_xlabel('Iteration $n$', fontsize=12)
axes[1].set_ylabel('Expected Value', fontsize=12)
axes[1].set_title('MCT: $\\lim_{n \\to \\infty} \\mathbb{E}_\\mu[V_n] = \\mathbb{E}_\\mu[V^*]$',
                   fontsize=12)
axes[1].legend(fontsize=11)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/Day2_MCT_ValueIteration.png', dpi=150)

print(f"\n{'='*70}")
print("MCT in Value Iteration: Numerical Verification")
print(f"{'='*70}")
print(f"Initial expected value: E[V_0] = {E_V[0]:.6f}")
print(f"After 10 iterations:    E[V_10] = {E_V[10]:.6f}")
print(f"After 50 iterations:    E[V_50] = {E_V[-1]:.6f}")
print(f"\nMonotonicity: V_0 ≤ V_1 ≤ ... ≤ V_50 ✓")
print(f"Convergence rate: approximately geometric with rate γ = {gamma}")
print(f"\nMCT guarantees: lim E[V_n] = E[lim V_n] = E[V*] = {E_V[-1]:.6f}")

plt.show()
```

**Key Observations:**
1. **Monotonicity:** Each iterate $V_n(s) \leq V_{n+1}(s)$ for all states $s$, verified numerically
2. **Pointwise Convergence:** $V_n(s) \to V^*(s)$ for each state (visible in left panel)
3. **MCT Application:** The expected value $\mathbb{E}_\mu[V_n(S_0)] = \sum_s \mu(s) V_n(s)$ converges to $\mathbb{E}_\mu[V^*(S_0)]$ by [THM-1.2.1]
4. **Practical Impact:** Without MCT, we could not rigorously justify stopping value iteration after $N$ steps and using $\mathbb{E}_\mu[V_N]$ as an approximation to optimal expected return

This computational experiment demonstrates that [THM-1.2.1] is not an abstract theorem—it is the mathematical guarantee enabling finite-time approximation of optimal policies in reinforcement learning.

---

### **IV. Application Bridge: Monotone Convergence in Reinforcement Learning**

The Monotone Convergence Theorem is not an abstract curiosity. It is the mathematical guarantee that underpins the convergence of the most fundamental algorithms in reinforcement learning. We now make this connection explicit.

#### **A. Value Iteration as Monotone Convergence**

In the theory of Markov Decision Processes, the **value iteration algorithm** is a fundamental method for computing optimal value functions. Starting from an initial guess $V_0$ (typically $V_0 = 0$ or $V_0 = \mathbf{0}$), we iteratively apply the Bellman optimality operator:
$$
V_{n+1} = T^* V_n, \qquad \text{where} \quad (T^* V)(s) = \max_{a \in \mathcal{A}} \left\{ R(s,a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s,a) V(s') \right\}
$$

**Theorem 1.2.2 (Monotonicity of Value Iteration - Statement Only)** {#THM-1.2.2} Assume:
1. The reward function is non-negative: $R(s,a) \geq 0$ for all $(s,a)$
2. The discount factor satisfies $\gamma \in [0,1)$
3. The initial value function is $V_0 = 0$

Then:
1. The sequence $\{V_n\}$ is monotone increasing: $0 = V_0 \leq V_1 \leq V_2 \leq \cdots$
2. The sequence converges pointwise to the optimal value function: $V_n(s) \to V^*(s)$ for all $s \in \mathcal{S}$
3. The Bellman operator $T^*$ is a $\gamma$-contraction in the supremum norm, ensuring exponential convergence at rate $\gamma^n$

*Note:* The proof requires the Banach Fixed Point Theorem, which will be established in Week 13 (Functional Analysis). We provide this result now for motivation; readers may take it on faith or consult [@puterman:mdp:2014, §6.3].

**Connection to MCT:** In finite-state MDPs, for a given initial state distribution $\mu$ on $\mathcal{S}$ (where $\mu(s) \geq 0$ and $\sum_{s} \mu(s) = 1$), let $S_0 \sim \mu$ denote a random initial state. The value function $V_n(s)$ is a deterministic vector in $\mathbb{R}^{|\mathcal{S}|}$, but the random variable $V_n(S_0)$ has expectation:
$$
\mathbb{E}_{\mu}[V_n(S_0)] = \sum_{s \in \mathcal{S}} \mu(s) V_n(s) = \int V_n \, d\mu
$$
where the integral is with respect to the discrete measure $\mu$ on the $\sigma$-algebra $2^{\mathcal{S}}$.

The **Monotone Convergence Theorem** ([THM-1.2.1]) applies because:
- **(i) Non-negativity:** $V_n(s) \geq 0$ for all $s \in \mathcal{S}$, all $n$ (from [THM-1.2.2])
- **(ii) Monotonicity:** $V_n(s) \leq V_{n+1}(s)$ for all $s \in \mathcal{S}$ (pointwise increasing)
- **(iii) Pointwise convergence:** $V_n(s) \to V^*(s)$ for all $s \in \mathcal{S}$ (from [THM-1.2.2])
- **(iv) Measurability:** All functions are measurable with respect to the discrete $\sigma$-algebra $2^{\mathcal{S}}$

Thus [THM-1.2.1] guarantees:
$$
\lim_{n \to \infty} \mathbb{E}_{\mu}[V_n(S_0)] = \mathbb{E}_{\mu}\left[\lim_{n \to \infty} V_n(S_0)\right] = \mathbb{E}_{\mu}[V^*(S_0)]
$$

This justifies the practice of approximating $V^*$ by running value iteration for finitely many steps: not only does $V_n$ converge pointwise to $V^*$, but its expected value (the policy's performance) also converges. Without [THM-1.2.1], we would have no guarantee that finite-time performance $\mathbb{E}_{\mu}[V_N]$ approximates the optimal performance $\mathbb{E}_{\mu}[V^*]$.

#### **B. Policy Evaluation and Temporal Difference Learning**

In **policy evaluation**, we seek to compute $V^{\pi}$, the value function of a fixed policy $\pi$. The Bellman consistency equation is:
$$
V^{\pi} = T^{\pi} V^{\pi}, \qquad \text{where} \quad (T^{\pi} V)(s) = R^{\pi}(s) + \gamma \sum_{s'} P^{\pi}(s'|s) V(s')
$$

Starting from $V_0 = 0$ (or any initial guess), the sequence $V_n = (T^{\pi})^n V_0$ converges to $V^{\pi}$. When rewards are non-negative, this convergence is monotone, and [THM-1.2.1] applies as in the value iteration case.

**Note:** This paragraph previews advanced material from Chapter 7 (Stochastic Approximation). Readers encountering these concepts for the first time should focus on the deterministic value iteration case (Section IV.A), where MCT applies directly. The stochastic case requires additional tools (Dominated Convergence Theorem, martingale theory) that we will develop systematically in later chapters.

We briefly preview a stochastic algorithm (full details in Chapter 7) to illustrate convergence theorems' role in probabilistic analysis. **Temporal Difference (TD) Learning** is a stochastic approximation algorithm for policy evaluation. The TD(0) update is:
$$
V_{t+1}(s_t) = V_t(s_t) + \alpha_t \left[R_t + \gamma V_t(s_{t+1}) - V_t(s_t)\right]
$$

Under appropriate conditions on the step sizes $\{\alpha_t\}$—specifically, the **Robbins-Monro conditions**: $\sum \alpha_t = \infty$ and $\sum \alpha_t^2 < \infty$ (the first ensures infinite exploration, preventing premature convergence; the second ensures bounded noise accumulation)—and the ergodicity of the Markov chain induced by $\pi$, TD learning converges to $V^{\pi}$ almost surely.

The convergence analysis relies on the **ODE method of stochastic approximation**, which uses the **Dominated Convergence Theorem** (Day 3)—not MCT directly—to justify interchanging limits and expectations under stochastic noise. MCT alone is insufficient because TD iterates fluctuate due to sampling noise and are not monotone. However, for deterministic policy evaluation (the iterates $V_n = (T^{\pi})^n V_0$), [THM-1.2.1] does apply when rewards are non-negative. This connection will be made fully rigorous when we study stochastic approximation theory in Chapter 7.

**Key Insight:** The Monotone Convergence Theorem is not merely a technical curiosity. It is the mathematical foundation that ensures the convergence of the most fundamental algorithms in reinforcement learning. Without [THM-1.2.1], we could not rigorously prove that value iteration or policy evaluation converge to the correct value function, even in the simplest finite-state setting.

---

### **V. Reflection and Forward Connections**

#### **Mathematical Insight**

The proof of [THM-1.2.1] hinges on two pillars:
1. **Monotonicity of measures:** If $\{E_n\}$ is an increasing sequence of sets, then $\mu(\bigcup E_n) = \lim \mu(E_n)$ (continuity from below, [LEM-1.2.1])
2. **Approximation by simple functions:** Any non-negative measurable function can be approximated from below by simple functions ([DEF-1.2.1])

The **α-trick** in Step 3 of the proof is subtle but crucial. When dealing with a simple function $\varphi$ that may equal the limit $f$ on a set of infinite measure, we cannot directly use the inequality $\int f_n \geq \int \varphi$ and pass to the limit. The issue is that on the complement of $E_n = \{x : f_n(x) \geq \varphi(x)\}$, we have $f_n < \varphi$, and if $\mu(E_n^c)$ remains bounded away from zero for all $n$, we cannot conclude that $\int f_n \to \int \varphi$.

Instead, we "deflate" $\varphi$ slightly by multiplying by $\alpha \in (0,1)$, obtaining sets $E_n = \{x : f_n(x) \geq \alpha\varphi(x)\}$ where the inequality is strict off of $E_n^c$. This allows us to use the continuity of measure on the increasing sequence $\{E_n\}$ to conclude $\bigcup E_n = X$. The α-trick is a recurring technique in analysis whenever one must handle functions on sets of infinite measure.

#### **RL Connection**

The Monotone Convergence Theorem provides the theoretical justification for several key results in RL:

1. **Value Iteration Convergence:** Starting from $V_0 = 0$, the sequence $V_n = (T^*)^n V_0$ converges monotonically to $V^*$, and $\mathbb{E}[V_n] \to \mathbb{E}[V^*]$ by [THM-1.2.1]
2. **Policy Evaluation:** For non-negative rewards, evaluating $V^{\pi}$ via iterated application of $T^{\pi}$ yields monotone convergence
3. **Stochastic Approximation:** The ODE method for analyzing TD learning relies on convergence theorems to justify interchanging limits and expectations

Without [THM-1.2.1], we would lack rigorous proofs that these algorithms converge to the correct value functions.

#### **Open Questions**

1. **Relaxation of Monotonicity:** Can [THM-1.2.1] be extended to sequences that are "almost monotone" (i.e., $f_n \leq f_{n+1}$ except on a set of measure zero)? The answer is affirmative: since integration ignores null sets ([DEF-1.1.7] from Day 1), we can modify $f_n$ on the exceptional set without changing its integral, reducing to the standard MCT case. This observation is crucial in stochastic approximation, where iterates are only defined almost surely (i.e., outside of negligible exceptional sets).

2. **Rate of Convergence:** [THM-1.2.1] guarantees $\int f_n \to \int f$, but provides no information about the rate of convergence. For RL applications, we care about sample complexity. Does monotone convergence of value functions imply a specific convergence rate for expected returns? This question connects to the contraction rate of the Bellman operator and the mixing time of the Markov chain.

3. **Generalization to Negative Functions:** What happens if $f_n$ are not non-negative? The sequence $f_n(x) = -1/n$ converges monotonically to $f(x) = 0$, and we have:
   $$\int_0^1 f_n(x)\,dx = -1/n \to 0 = \int_0^1 f(x)\,dx$$
   So MCT's conclusion holds in this case. However, for signed functions the Lebesgue integral may be undefined due to the indeterminate form $\infty - \infty$ (even when pointwise limits exist). This motivates the study of **Fatou's Lemma** and the **Dominated Convergence Theorem** (Day 3), which replace monotonicity with non‑negativity or domination to control integrability throughout the limit.

---

Tomorrow (Day 3), we will address the final point by developing **Fatou's Lemma** and the **Dominated Convergence Theorem**, which relax the hypotheses of MCT. These three theorems—MCT, Fatou, and DCT—form the **triumvirate of convergence** in integration theory, and they are the mathematical bedrock upon which the entire edifice of stochastic optimization and reinforcement learning is constructed.
