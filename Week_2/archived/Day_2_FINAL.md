[[Day_2_exercises_FINAL]]

### Agenda:

##### 📘 Day 2 — Week 2: Tonelli's Theorem and Iterated Integration

**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (40 min) — Reading**

**Topic:** _Tonelli's theorem: integrating non-negative measurable functions on product spaces_

- Read from **Folland §2.4** (Tonelli's theorem) or **Durrett §1.8** (product measures and Fubini-Tonelli)
- Focus on:
    - **Tonelli's theorem statement**: For non-negative measurable $f: X \times Y \to [0,\infty]$, iterated integrals equal the double integral
    - **Key mechanism**: Monotone Convergence Theorem (MCT) enables interchange of integration and supremum
    - **Proof strategy**: Reduce to simple functions via approximation, then apply MCT
    - **Contrast with Fubini**: Tonelli requires only non-negativity (not integrability)
- _Key takeaway:_ Tonelli is the computational workhorse—it justifies computing expectations over state-action spaces via iterated integrals, even when integrability is unverified. Fubini (Day 3) extends to general $L^1$ functions but requires stronger hypotheses.

---

#### **⏱️ Segment 2 (40 min) — Proof/Exercise**

**Primary Task:** Prove **Tonelli's theorem** in full detail following the three-step strategy:
1. **Step 1**: Verify for indicator functions of rectangles
2. **Step 2**: Extend to simple functions via linearity
3. **Step 3**: Extend to general non-negative measurable functions via MCT

**Guidance:**
- Start with characteristic functions $\mathbf{1}_{A \times B}$ and verify iterated integrals equal $\mu(A)\nu(B)$
- For simple functions $s = \sum_{i=1}^{n} a_i \mathbf{1}_{E_i}$, use linearity of integration
- For general $f \geq 0$, construct increasing simple function approximation $s_n \uparrow f$ (recall Week 1, Day 2)
- Apply MCT to pass limit inside integral

**Stretch Goal:** Verify Tonelli for the specific case $f(s,a) = R(s,a)^+$ (positive part of reward) on a finite state-action space, computing both iterated and double integrals explicitly.

---

#### **⏱️ Segment 3 (10 min) — Reflection**

**Reflection Questions:**
1. Why does Tonelli require only non-negativity, while Fubini requires integrability? What pathology does integrability prevent? (Preview for Day 3.)
2. How does Tonelli enable computing $\mathbb{E}_{(s,a) \sim \mu \times \pi}[R^+(s,a)]$ via $\int_{\mathcal{S}} \left(\int_{\mathcal{A}} R^+(s,a) \, \pi(da|s)\right) \mu(ds)$ without verifying $\mathbb{E}[|R|] < \infty$ first?
3. In policy evaluation, we compute $\mathbb{E}_{s \sim \mu}[\mathbb{E}_{a \sim \pi(\cdot|s)}[Q^{\pi}(s,a)]]$. When can we interchange this iterated expectation with a sum or limit operation? (Hint: MCT via Tonelli.)

**Preview for Day 3:** Tomorrow we extend Tonelli to **Fubini's theorem** for integrable functions $f \in L^1(\mu \times \nu)$, requiring the additional hypothesis $\int |f| < \infty$. We'll construct counterexamples showing Fubini fails without integrability, and connect to importance sampling ratios in off-policy RL (which require careful integrability checks).

---

#### **💡 Conceptual bridge to RL**

- **Tonelli in policy evaluation**: Computing $V^{\pi}(s) = \mathbb{E}_{a \sim \pi(\cdot|s)}[Q^{\pi}(s,a)]$ requires integrating over actions—Tonelli justifies this when $Q^{\pi} \geq 0$ (e.g., non-negative rewards)
- **Model-based planning**: Bellman backup $T V(s) = \mathbb{E}_{a \sim \pi(\cdot|s)}[\mathbb{E}_{s' \sim P(\cdot|s,a)}[R(s,a) + \gamma V(s')]]$ is a double iterated integral—Tonelli ensures it's well-defined when $R + \gamma V \geq 0$
- **Monte Carlo estimation**: Sample-based approximation $\frac{1}{N}\sum_{i=1}^{N} f(s_i, a_i) \approx \int f \, d(\mu \times \pi)$ converges to the double integral by Tonelli (when $f \geq 0$) and the strong law of large numbers
- **Non-negative feature expectations**: In linear function approximation, computing $\mathbb{E}[\phi(s,a)]$ for non-negative features $\phi$ uses Tonelli

---

📅 Tomorrow (Day 3): **Fubini's theorem** (complete proof for integrable functions) and counterexamples showing failure without σ-finiteness or integrability.

---

## **Chapter 2.2: Tonelli's Theorem — Iterated Integration for Non-Negative Functions**

### **Motivation: Why Tonelli Matters for Reinforcement Learning**

Yesterday we constructed the product measure $\mu \times \nu$ on $X \times Y$, enabling us to define integrals of functions $f: X \times Y \to \mathbb{R}$ with respect to the joint distribution. But in practice—whether in policy evaluation, Monte Carlo sampling, or model-based planning—we rarely compute double integrals directly. Instead, we compute **iterated integrals**:

$$
\int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) \quad \text{or} \quad \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y)
$$

**The fundamental question:** When do these iterated integrals equal the double integral $\int_{X \times Y} f \, d(\mu \times \nu)$? And when do the two orders of iteration give the same answer?

**Tonelli's theorem** provides a complete answer for **non-negative measurable functions**: if $f \geq 0$, then all three integrals are equal (possibly infinite), and the order of integration does not matter. This is the computational workhorse of integration theory—it justifies interchanging integrals and sums in policy evaluation, model-based planning, and Monte Carlo estimation, even when we haven't verified integrability.

**Bridge from Day 1:** Yesterday we established that the product measure $\mu \times \nu$ exists and is unique (when $\mu$ and $\nu$ are σ-finite). We verified measurability of reward functions $R: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ with respect to the product σ-algebra. Today, we make this machinery **computational** by proving that expectations over product spaces can be computed via iterated expectations—the foundation for every policy evaluation algorithm in RL.

**Why this matters for RL:** Consider the **Bellman expectation equation** for the state-value function under policy $\pi$:

$$
V^{\pi}(s) = \mathbb{E}_{a \sim \pi(\cdot|s)}\left[\mathbb{E}_{s' \sim P(\cdot|s,a)}[R(s,a,s') + \gamma V^{\pi}(s')]\right]
$$

This is a **nested iterated expectation**—first over next states $s'$ given $(s,a)$, then over actions $a$ given $s$. In integral notation:

$$
V^{\pi}(s) = \int_{\mathcal{A}} \left(\int_{\mathcal{S}'} [R(s,a,s') + \gamma V^{\pi}(s')] \, P(ds'|s,a)\right) \pi(da|s)
$$

For this expression to be well-defined and computable, we need:
1. The inner integral over $s'$ to be measurable in $(s,a)$ (so we can integrate it over actions)
2. The iterated integral to equal the "joint" expectation over $(a, s')$

**Tonelli's theorem guarantees both**, provided $R + \gamma V^{\pi} \geq 0$ (which holds when rewards and values are non-negative, a common assumption in control with non-negative costs or benefits).

**Technical note on measure structure:** The joint distribution over $(a, s')$ given fixed $s$ is constructed via the **Ionescu-Tulcea theorem** (conditional product construction), not as a product measure in the sense of Day 1. Specifically, for fixed $s$, we define the measure kernel
$$
\rho_s(da, ds') = \pi(da|s) \cdot P(ds'|s,a) \quad \text{(conditional product)}
$$
This is a conditional/disintegrated measure indexed by $s$, since $P(\cdot|s,a)$ depends on both $s$ and $a$. The rigorous framework for such nested conditionals is **conditional expectation** (Week 4, Day 4) and the **disintegration theorem** (Kallenberg Theorem 6.4). For now, we note that Tonelli-type arguments extend to such conditional constructions when the integrand is non-negative—this generalization is covered in Kallenberg §6.3.

More generally, in **model-based RL** and **policy evaluation**, we constantly compute expressions like:

$$
\mathbb{E}_{s,a}[f(s,a)] = \int_{\mathcal{S} \times \mathcal{A}} f(s,a) \, d\rho(s,a)
$$

where $\rho$ is the state-action distribution under policy $\pi$ and initial state distribution $\mu_0$. Tonelli tells us we can compute this as:

$$
\int_{\mathcal{S}} \left(\int_{\mathcal{A}} f(s,a) \, \pi(da|s)\right) \mu_0(ds) = \int_{\mathcal{A}} \left(\int_{\mathcal{S}} f(s,a) \, \mu_0(ds)\right) \pi(da|s)
$$

when $f \geq 0$—justifying the standard algorithm: **sample $s \sim \mu_0$, then sample $a \sim \pi(\cdot|s)$, compute $f(s,a)$, and average**.

**Learning Objectives:**
* State and prove Tonelli's theorem in full generality
* Understand why the proof uses MCT as the key mechanism for passing limits inside integrals
* Master the three-step proof strategy: indicators → simple functions → general non-negative functions
* Recognize when Tonelli applies in RL algorithms (policy evaluation, model-based planning, feature expectations)
* Appreciate the contrast with Fubini (tomorrow): Tonelli requires only non-negativity, not integrability

---

### **I. Core Theory: Tonelli's Theorem**

#### **A. Statement and Hypotheses**

**Remark 2.8 (Borel σ-algebra Convention).** We equip $[0,\infty]$ with the Borel σ-algebra $\mathcal{B}([0,\infty])$ generated by the standard topology, where $[0,\infty] = [0,\infty) \cup \{\infty\}$ with $\infty$ as an isolated point (in the topology induced by the usual metric on $\mathbb{R} \cup \{-\infty, \infty\}$). Under this convention, all measurability statements in Theorem 2.3 are with respect to Borel sets. This is the standard convention in measure theory (Folland §1.1, Durrett §1.1).

**Theorem 2.3 (Tonelli's Theorem).** Let $(X, \mathcal{F}_X, \mu)$ and $(Y, \mathcal{F}_Y, \nu)$ be σ-finite measure spaces. Let $f: X \times Y \to [0, \infty]$ be a **non-negative** $(\mathcal{F}_X \otimes \mathcal{F}_Y)$-measurable function. Then:

1. **Sections are measurable:** For each $x \in X$, the function $y \mapsto f(x,y)$ is $(\mathcal{F}_Y, \mathcal{B}([0,\infty]))$-measurable. Similarly, for each $y \in Y$, the function $x \mapsto f(x,y)$ is $(\mathcal{F}_X, \mathcal{B}([0,\infty]))$-measurable.

2. **Iterated integrals are measurable:** The functions
   $$
   \begin{align}
   F_1(x) &= \int_Y f(x,y) \, d\nu(y) \quad \text{(integral over } y \text{ with } x \text{ fixed)} \tag{2.1} \\
   F_2(y) &= \int_X f(x,y) \, d\mu(x) \quad \text{(integral over } x \text{ with } y \text{ fixed)} \tag{2.2}
   \end{align}
   $$
   are measurable: $F_1: (X, \mathcal{F}_X) \to ([0,\infty], \mathcal{B}([0,\infty]))$ and $F_2: (Y, \mathcal{F}_Y) \to ([0,\infty], \mathcal{B}([0,\infty]))$.

3. **Iterated integrals equal double integral:**
   $$
   \int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f \, d(\mu \times \nu) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y) \tag{2.3}
   $$

All three integrals may be infinite, but if one is finite, all are finite and equal.

---

**Remark 2.9 (Why Non-Negativity?).** The hypothesis $f \geq 0$ is **crucial**. It ensures that all integrals are well-defined in $[0, \infty]$ (no cancellation issues), and it allows us to apply the **Monotone Convergence Theorem** (MCT, Week 1 Day 2) to pass limits inside integrals. Geometrically, non-negativity ensures all contributions to the integral are accumulating (no cancellation), allowing monotone approximation. When $f$ oscillates in sign, positive and negative regions can interact pathologically, requiring the stronger hypothesis $\int |f| < \infty$ to control total variation. This is precisely the content of **Fubini's theorem** (Day 3).

**Remark 2.10 (σ-Finiteness is Essential).** We assume $\mu$ and $\nu$ are σ-finite. Without this, Tonelli can fail—we construct a counterexample on Day 3 using counting measure on an uncountable set.

**Remark 2.11 (Order Independence).** The equality of the two iterated integrals—regardless of the order of integration—is a non-trivial conclusion. It follows from the fact that both equal the double integral, which is independent of any ordering. This symmetry is fundamental in RL: we can compute $\mathbb{E}_{s,a}[f(s,a)]$ by first sampling $s$ then $a$, or vice versa, with the same result (when $f \geq 0$).

---

#### **B. Proof Strategy: The Three-Step Ladder**

The proof of Tonelli follows the canonical pattern for extending properties from simple sets to general measurable functions:

1. **Step 1 (Rectangles):** Verify the theorem for indicator functions $f = \mathbf{1}_{A \times B}$ where $A \in \mathcal{F}_X$, $B \in \mathcal{F}_Y$.

2. **Step 2 (Simple Functions):** Extend to simple functions $s = \sum_{i=1}^{n} a_i \mathbf{1}_{E_i}$ via linearity of integration.

3. **Step 3 (General Non-Negative Functions):** Approximate any non-negative measurable $f$ by an increasing sequence of simple functions $s_n \uparrow f$ (Week 1, Day 2), then apply MCT to pass the limit inside integrals.

This is the **standard approximation hierarchy** in integration theory, used repeatedly throughout measure theory (and echoing our construction of the Lebesgue integral in Week 1). We will see this pattern again in Fubini (Day 3), $L^p$ spaces (Day 4), and Radon-Nikodym (Week 3).

---

### **II. Complete Proof of Tonelli's Theorem**

**Proof of Theorem 2.3.**

We proceed in three steps.

---

**Step 1: Indicator functions of rectangles.**

Let $f = \mathbf{1}_{A \times B}$ where $A \in \mathcal{F}_X$ and $B \in \mathcal{F}_Y$.

**Claim 1 (Sections are measurable):** For fixed $x \in X$, the section $f(x, \cdot): Y \to \{0,1\}$ is:
$$
f(x, y) = \mathbf{1}_{A \times B}(x,y) = \begin{cases} 1 & \text{if } x \in A \text{ and } y \in B \\ 0 & \text{otherwise} \end{cases} = \mathbf{1}_A(x) \cdot \mathbf{1}_B(y)
$$

Thus $f(x, \cdot) = \mathbf{1}_A(x) \cdot \mathbf{1}_B$, which is measurable (it's either the zero function if $x \notin A$, or $\mathbf{1}_B$ if $x \in A$, both measurable). Similarly, $f(\cdot, y) = \mathbf{1}_B(y) \cdot \mathbf{1}_A$ is measurable. ✓

**Claim 2 (Iterated integrals are measurable):** We compute:
$$
F_1(x) = \int_Y f(x,y) \, d\nu(y) = \int_Y \mathbf{1}_A(x) \cdot \mathbf{1}_B(y) \, d\nu(y) = \mathbf{1}_A(x) \int_Y \mathbf{1}_B(y) \, d\nu(y) = \mathbf{1}_A(x) \cdot \nu(B)
$$

Thus $F_1(x) = \nu(B) \cdot \mathbf{1}_A(x)$, which is measurable (constant multiple of an indicator function). ✓

Similarly, $F_2(y) = \mu(A) \cdot \mathbf{1}_B(y)$ is measurable. ✓

**Claim 3 (Iterated integrals equal double integral):**
$$
\begin{align}
\int_X F_1(x) \, d\mu(x) &= \int_X \nu(B) \cdot \mathbf{1}_A(x) \, d\mu(x) = \nu(B) \int_X \mathbf{1}_A(x) \, d\mu(x) = \nu(B) \cdot \mu(A) \\
\int_Y F_2(y) \, d\nu(y) &= \int_Y \mu(A) \cdot \mathbf{1}_B(y) \, d\nu(y) = \mu(A) \int_Y \mathbf{1}_B(y) \, d\nu(y) = \mu(A) \cdot \nu(B)
\end{align}
$$

By definition of the product measure (Day 1, Theorem 2.2):
$$
\int_{X \times Y} \mathbf{1}_{A \times B} \, d(\mu \times \nu) = (\mu \times \nu)(A \times B) = \mu(A) \cdot \nu(B)
$$

Thus all three integrals equal $\mu(A) \nu(B)$, establishing equation (2.3) for indicator functions of rectangles. ✓

---

**Step 2: Simple functions.**

Let $s: X \times Y \to [0, \infty)$ be a **simple function**. By Folland §2.4, Lemma 2.36 (or Day 1, Lemma 2.4), any simple function $s$ on $X \times Y$ can be written as a finite linear combination of indicator functions of measurable sets $s = \sum_{i=1}^{n} a_i \mathbf{1}_{E_i}$ where $E_i \in \mathcal{F}_X \otimes \mathcal{F}_Y$. For pedagogical clarity, we first establish the result for simple functions of the form $s = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i \times B_i}$ where $A_i \times B_i$ are disjoint rectangles with $A_i \in \mathcal{F}_X$, $B_i \in \mathcal{F}_Y$, and $a_i \geq 0$. The extension to general simple functions (where sets $E_i$ are not necessarily rectangles) follows by approximating each $\mathbf{1}_{E_i}$ by finite unions of rectangles in $L^1(\mu \times \nu)$, then applying MCT—see Folland §2.4 for the complete technical details.

**For simple functions on rectangles:**

By **linearity of integration** (Week 1, Day 2, Proposition 1.5):

$$
\begin{align}
\int_Y s(x,y) \, d\nu(y) &= \int_Y \left(\sum_{i=1}^{n} a_i \mathbf{1}_{A_i \times B_i}(x,y)\right) d\nu(y) \\
&= \sum_{i=1}^{n} a_i \int_Y \mathbf{1}_{A_i \times B_i}(x,y) \, d\nu(y) \\
&= \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}(x) \nu(B_i) \quad \text{(by Step 1)}
\end{align}
$$

This is a finite sum of measurable functions (each $\mathbf{1}_{A_i}(x)$ is measurable), hence $F_1(x) = \int_Y s(x,y) \, d\nu(y)$ is measurable. ✓

Similarly, $F_2(y) = \int_X s(x,y) \, d\mu(x)$ is measurable. ✓

Now compute:
$$
\begin{align}
\int_X F_1(x) \, d\mu(x) &= \int_X \left(\sum_{i=1}^{n} a_i \mathbf{1}_{A_i}(x) \nu(B_i)\right) d\mu(x) \\
&= \sum_{i=1}^{n} a_i \nu(B_i) \int_X \mathbf{1}_{A_i}(x) \, d\mu(x) \\
&= \sum_{i=1}^{n} a_i \nu(B_i) \mu(A_i) \\
&= \sum_{i=1}^{n} a_i \cdot (\mu \times \nu)(A_i \times B_i) \\
&= \int_{X \times Y} s \, d(\mu \times \nu) \quad \text{(by linearity of integration on product space)}
\end{align}
$$

By symmetry, $\int_Y F_2(y) \, d\nu(y) = \sum_{i=1}^{n} a_i \mu(A_i) \nu(B_i)$, which equals the same value. ✓

Thus Tonelli holds for simple functions. □

---

**Step 3: General non-negative measurable functions.**

Let $f: X \times Y \to [0, \infty]$ be a non-negative $(\mathcal{F}_X \otimes \mathcal{F}_Y)$-measurable function.

**Approximation by simple functions:** By the standard construction (Week 1, Day 2, Lemma 1.3), there exists an increasing sequence of simple functions $s_n: X \times Y \to [0, \infty)$ such that:
$$
s_1 \leq s_2 \leq s_3 \leq \cdots \quad \text{and} \quad s_n(x,y) \uparrow f(x,y) \quad \text{for all } (x,y) \in X \times Y
$$

**Specifically**, we can use the dyadic approximation:
$$
s_n(x,y) = \sum_{k=0}^{n 2^n - 1} \frac{k}{2^n} \mathbf{1}_{\{f^{-1}([k/2^n, (k+1)/2^n))\}} + n \cdot \mathbf{1}_{\{f \geq n\}}
$$

(This construction partitions $[0, \infty)$ into intervals of length $1/2^n$ up to height $n$, then assigns constant value $n$ to the region where $f \geq n$.)

**Applying MCT to sections:** Fix $x \in X$. For each $n$, the section $s_n(x, \cdot): Y \to [0, \infty)$ is a simple function, hence measurable (by part 1 of Theorem 2.3 applied to the simple function $s_n$, which we established in Step 1 for indicator functions and extended to simple functions via linearity). By Step 2, we have:
$$
F_1^{(n)}(x) := \int_Y s_n(x, y) \, d\nu(y)
$$
is measurable in $x$.

Since $s_n(x,y) \uparrow f(x,y)$ pointwise for each fixed $x$, the **Monotone Convergence Theorem** (Week 1, Day 2, Theorem 1.6) gives:
$$
\int_Y s_n(x,y) \, d\nu(y) \uparrow \int_Y f(x,y) \, d\nu(y) = F_1(x) \tag{2.4}
$$

**Measurability of $F_1(x)$:** Since $F_1(x) = \lim_{n \to \infty} F_1^{(n)}(x)$ is the pointwise limit of measurable functions $F_1^{(n)}$, it is measurable (Week 1, Day 1, Proposition 1.2). ✓

**Applying MCT to the outer integral:** Now integrate over $x$:
$$
\begin{align}
\int_X F_1(x) \, d\mu(x) &= \int_X \lim_{n \to \infty} F_1^{(n)}(x) \, d\mu(x) \\
&= \int_X \lim_{n \to \infty} \left(\int_Y s_n(x,y) \, d\nu(y)\right) d\mu(x) \\
&= \lim_{n \to \infty} \int_X \left(\int_Y s_n(x,y) \, d\nu(y)\right) d\mu(x) \quad \text{(by MCT, since } F_1^{(n)} \uparrow F_1) \tag{2.5} \\
&= \lim_{n \to \infty} \int_{X \times Y} s_n \, d(\mu \times \nu) \quad \text{(by Step 2, Tonelli holds for simple functions } s_n) \\
&= \int_{X \times Y} f \, d(\mu \times \nu) \quad \text{(by MCT on product space, since } s_n \uparrow f) \tag{2.6}
\end{align}
$$

**Explanation of key steps:**
- **(2.5):** We applied MCT to the outer integral $\int_X \cdots \, d\mu(x)$ because $F_1^{(n)}(x) \uparrow F_1(x)$ pointwise (established in (2.4)) and all functions are non-negative.
- **(2.6):** We applied MCT on the product space $(X \times Y, \mu \times \nu)$ to the increasing sequence $s_n \uparrow f$.

By symmetry, the same argument shows:
$$
\int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y) = \int_{X \times Y} f \, d(\mu \times \nu)
$$

Thus all three integrals in (2.3) are equal. □

---

**Remark 2.12 (The Power of MCT).** The entire proof hinges on the **Monotone Convergence Theorem**. MCT allows us to interchange $\lim$ and $\int$ for increasing sequences of non-negative functions—without requiring uniform convergence or domination. This is why Tonelli requires only non-negativity: MCT applies automatically. When $f$ can be negative, we must verify integrability to ensure convergence is "controlled," leading to Fubini's theorem (Day 3). This distinction becomes critical in Week 4 (conditional expectation) and Week 32 (stochastic approximation), where controlling both positive and negative parts of martingale differences requires integrability conditions.

**Remark 2.13 (Why σ-Finiteness Enters).** The proof uses the fact that the product measure $\mu \times \nu$ is well-defined and unique (Theorem 2.2, Day 1), which required σ-finiteness. Moreover, the approximation by simple functions implicitly relies on σ-finiteness to ensure countable decompositions. Without σ-finiteness, the product measure may not be unique, and Tonelli can fail (counterexample: Day 3).

**Remark 2.14 (Geometric Intuition).** Tonelli says: "To compute the volume under the graph of $f$ over $X \times Y$, we can first compute vertical slices (fixing $x$, integrating over $y$), then integrate those slice-areas over $x$—or reverse the order." For non-negative functions, both give the same total volume, equal to the double integral.

---

### **III. Key Properties and Corollaries**

**Proposition 2.6 (Tonelli for Sums and Series).** Let $(X, \mathcal{F}_X, \mu)$ and $(Y, \mathcal{F}_Y, \nu)$ be σ-finite measure spaces. Let $\{f_{ij}\}_{i,j \in \mathbb{N}}$ be a double sequence where each $f_{ij}: X \times Y \to [0, \infty]$ is $(\mathcal{F}_X \otimes \mathcal{F}_Y)$-measurable. Then:

$$
\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} \int_{X \times Y} f_{ij} \, d(\mu \times \nu) = \sum_{j=1}^{\infty} \sum_{i=1}^{\infty} \int_{X \times Y} f_{ij} \, d(\mu \times \nu) = \int_{X \times Y} \left(\sum_{i,j=1}^{\infty} f_{ij}\right) d(\mu \times \nu)
$$

*Proof.* Define $F = \sum_{i,j=1}^{\infty} f_{ij}$. By Tonelli (since each $f_{ij} \geq 0$ and $F$ is the limit of increasing partial sums, hence measurable and non-negative):

$$
\int_{X \times Y} F \, d(\mu \times \nu) = \int_X \left(\int_Y F(x,y) \, d\nu(y)\right) d\mu(x)
$$

Now, $\int_Y F(x,y) \, d\nu(y) = \int_Y \sum_{i,j} f_{ij}(x,y) \, d\nu(y) = \sum_{i,j} \int_Y f_{ij}(x,y) \, d\nu(y)$ (by MCT for sums, Week 1 Day 2).

Thus:
$$
\int_{X \times Y} F \, d(\mu \times \nu) = \sum_{i,j} \int_X \left(\int_Y f_{ij}(x,y) \, d\nu(y)\right) d\mu(x) = \sum_{i,j} \int_{X \times Y} f_{ij} \, d(\mu \times \nu)
$$

Since the double series $\sum_{i,j}$ is absolutely convergent (all terms non-negative), we can interchange the order of summation. □

**Remark 2.15 (RL Application: Feature Expectations in Linear Function Approximation).** In linear value function approximation, we represent $V^{\pi}(s) \approx \sum_{k=1}^{d} \theta_k \phi_k(s)$ where $\phi_k: \mathcal{S} \to \mathbb{R}$ are features. Computing the expected feature vector $\mathbb{E}_{s \sim \mu}[\phi(s)]$ for a batch of features $\{\phi_k\}_{k=1}^{d}$ involves summing expectations. By linearity of the integral (Week 1, Day 2, Proposition 1.5):
$$
\mathbb{E}\left[\sum_{k=1}^{d} \phi_k(s)\right] = \sum_{k=1}^{d} \mathbb{E}[\phi_k(s)]
$$
This holds for any finite sum, regardless of sign. Tonelli becomes relevant when computing $\mathbb{E}[\phi_k(s) \phi_\ell(s')]$ via iterated integrals over $(s, s')$ in temporal-difference learning (Week 35).

---

**Corollary 2.1 (Tonelli for Counting Measure).** Let $X = \mathbb{N}$ and $Y = \mathbb{N}$ with counting measures $\mu = \nu = \text{counting}$. Then for any double sequence $a_{ij} \geq 0$:

$$
\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{ij} = \sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{ij}
$$

*Proof.* This is the special case of Tonelli where $f(i,j) = a_{ij}$ and integrals become sums. □

This is the classical result on interchange of summation order for non-negative series—a cornerstone of real analysis, now revealed as a special case of Tonelli's theorem.

---

### **IV. Computational Illustration: Verifying Tonelli Numerically**

To build intuition for Tonelli's theorem, we numerically verify that iterated integrals equal the double integral for a concrete non-negative function on a product space.

**Example 2.3 (Discrete Verification).** Let $X = \{1, 2, 3\}$ with measure $\mu$ given by $\mu(\{1\}) = 1/2$, $\mu(\{2\}) = 1/3$, $\mu(\{3\}) = 1/6$. Let $Y = \{a, b\}$ with measure $\nu$ given by $\nu(\{a\}) = 2/3$, $\nu(\{b\}) = 1/3$.

Define $f: X \times Y \to [0, \infty)$ by:
$$
f(x, y) = \begin{cases}
x & \text{if } y = a \\
2x & \text{if } y = b
\end{cases} \quad \text{for } x \in X, \, y \in Y
$$

**Task:** Verify equation (2.3): compute both iterated integrals and the double integral, confirming they're equal.

**Solution:**

**Step 1: Inner integral over $Y$, outer over $X$.**

Fix $x \in X$. Compute:
$$
\int_Y f(x,y) \, d\nu(y) = f(x,a) \cdot \nu(\{a\}) + f(x,b) \cdot \nu(\{b\}) = x \cdot \frac{2}{3} + 2x \cdot \frac{1}{3} = x \left(\frac{2}{3} + \frac{2}{3}\right) = \frac{4x}{3}
$$

Now integrate over $X$:
$$
\int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_X \frac{4x}{3} \, d\mu(x) = \frac{4}{3} \left(1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{3} + 3 \cdot \frac{1}{6}\right) = \frac{4}{3} \cdot \frac{3}{2} = 2
$$

**Step 2: Inner integral over $X$, outer over $Y$.**

Fix $y \in Y$. For $y = a$:
$$
\int_X f(x,a) \, d\mu(x) = \int_X x \, d\mu(x) = 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{3} + 3 \cdot \frac{1}{6} = \frac{3}{2}
$$

For $y = b$:
$$
\int_X f(x,b) \, d\mu(x) = \int_X 2x \, d\mu(x) = 2 \cdot \frac{3}{2} = 3
$$

Now integrate over $Y$:
$$
\int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y) = \frac{3}{2} \cdot \frac{2}{3} + 3 \cdot \frac{1}{3} = 1 + 1 = 2
$$

**Step 3: Double integral on $X \times Y$.**

The product measure satisfies $(\mu \times \nu)(\{(x,y)\}) = \mu(\{x\}) \nu(\{y\})$. Compute:
$$
\begin{align}
\int_{X \times Y} f \, d(\mu \times \nu) &= \sum_{x \in X, y \in Y} f(x,y) \cdot (\mu \times \nu)(\{(x,y)\}) \\
&= \sum_{x \in X} \left[f(x,a) \cdot \mu(\{x\}) \nu(\{a\}) + f(x,b) \cdot \mu(\{x\}) \nu(\{b\})\right] \\
&= \sum_{x \in X} \left[x \cdot \mu(\{x\}) \cdot \frac{2}{3} + 2x \cdot \mu(\{x\}) \cdot \frac{1}{3}\right] \\
&= \sum_{x \in X} \frac{4x}{3} \mu(\{x\}) \\
&= \frac{4}{3} \left(1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{3} + 3 \cdot \frac{1}{6}\right) = \frac{4}{3} \cdot \frac{3}{2} = 2
\end{align}
$$

**Conclusion:** All three integrals equal $2$, verifying Tonelli. ✓

---

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

def verify_tonelli(X: np.ndarray, Y: np.ndarray,
                   mu: np.ndarray, nu: np.ndarray,
                   f: np.ndarray) -> dict:
    """
    Numerically verify Tonelli's theorem for a discrete function f: X × Y → [0,∞).

    Parameters:
        X: State space (array of values)
        Y: Action space (array of values)
        mu: Probability measure on X
        nu: Probability measure on Y
        f: Function values f[i,j] = f(X[i], Y[j])

    Returns:
        dict with keys 'iterated_xy', 'iterated_yx', 'double', 'verified'
    """
    # Method 1: Inner integral over Y, outer over X
    # Compute F₁(x) = ∫_Y f(x,y) dν(y) for each x  [Equation 2.1]
    F1 = np.sum(f * nu[np.newaxis, :], axis=1)
    # Then compute ∫_X F₁(x) dμ(x)  [Equation 2.3, first equality]
    result_1 = np.sum(F1 * mu)

    # Method 2: Inner integral over X, outer over Y
    # Compute F₂(y) = ∫_X f(x,y) dμ(x) for each y  [Equation 2.2]
    F2 = np.sum(f * mu[:, np.newaxis], axis=0)
    # Then compute ∫_Y F₂(y) dν(y)  [Equation 2.3, third equality]
    result_2 = np.sum(F2 * nu)

    # Method 3: Double integral using product measure
    # ∫_{X×Y} f d(μ × ν) = Σ f(x,y) · μ({x}) · ν({y})
    product_measure = np.outer(mu, nu)  # (μ × ν)({(x,y)}) = μ({x}) · ν({y})
    result_3 = np.sum(f * product_measure)

    return {
        'iterated_xy': result_1,
        'iterated_yx': result_2,
        'double': result_3,
        'verified': np.allclose([result_1, result_2, result_3], result_1)
    }

# Define discrete measures (from Day 1 example)
X = np.array([1, 2, 3])
Y = np.array(['a', 'b'])

mu = np.array([1/2, 1/3, 1/6])  # μ({1}) = 1/2, μ({2}) = 1/3, μ({3}) = 1/6
nu = np.array([2/3, 1/3])        # ν({'a'}) = 2/3, ν({'b'}) = 1/3

# Define f(x,y): f(x,'a') = x, f(x,'b') = 2x
# We represent f as a matrix: f[i,j] = f(X[i], Y[j])
f = np.zeros((len(X), len(Y)))
for i, x_val in enumerate(X):
    f[i, 0] = x_val      # y = 'a'
    f[i, 1] = 2 * x_val  # y = 'b'

print("Function f(x,y):")
print(f"{'x \\ y':<8}", end="")
for y_val in Y:
    print(f"{y_val:<12}", end="")
print()
for i, x_val in enumerate(X):
    print(f"{x_val:<8}", end="")
    for j in range(len(Y)):
        print(f"{f[i,j]:<12.2f}", end="")
    print()

print("\n" + "="*60)
print("Tonelli Verification:")
print("="*60)

# Verify Tonelli
results = verify_tonelli(X, Y, mu, nu, f)

# Method 1: Integrate over Y first, then X
# F1(x) = ∫_Y f(x,y) dν(y)
F1 = np.sum(f * nu[np.newaxis, :], axis=1)  # For each x, sum over y weighted by ν
print("\nMethod 1: ∫_X (∫_Y f(x,y) dν(y)) dμ(x)")
print(f"Inner integrals F1(x) = ∫_Y f(x,y) dν(y):")
for i, x_val in enumerate(X):
    print(f"  F1({x_val}) = {F1[i]:.4f}")

# Outer integral: ∫_X F1(x) dμ(x)
print(f"\nOuter integral: ∫_X F1(x) dμ(x) = {results['iterated_xy']:.6f}")

# Method 2: Integrate over X first, then Y
# F2(y) = ∫_X f(x,y) dμ(x)
F2 = np.sum(f * mu[:, np.newaxis], axis=0)  # For each y, sum over x weighted by μ
print("\n" + "-"*60)
print("\nMethod 2: ∫_Y (∫_X f(x,y) dμ(x)) dν(y)")
print(f"Inner integrals F2(y) = ∫_X f(x,y) dμ(x):")
for j, y_val in enumerate(Y):
    print(f"  F2('{y_val}') = {F2[j]:.4f}")

# Outer integral: ∫_Y F2(y) dν(y)
print(f"\nOuter integral: ∫_Y F2(y) dν(y) = {results['iterated_yx']:.6f}")

# Method 3: Double integral using product measure
# ∫_{X×Y} f d(μ × ν) = Σ f(x,y) · μ({x}) · ν({y})
print("\n" + "-"*60)
print("\nMethod 3: ∫_{X×Y} f d(μ × ν)")
print(f"Double integral: {results['double']:.6f}")

# Verification
print("\n" + "="*60)
print("VERIFICATION:")
print("="*60)
print(f"Iterated (Y first, X outer): {results['iterated_xy']:.6f}")
print(f"Iterated (X first, Y outer): {results['iterated_yx']:.6f}")
print(f"Double integral:              {results['double']:.6f}")
print(f"\nAll equal? {results['verified']}")
print("\n✓ Tonelli's theorem verified numerically!")

# Visualization: Heatmap showing f(x,y) and contribution to integral
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Panel 1: Function values f(x,y)
im1 = axes[0].imshow(f, cmap='YlOrRd', aspect='auto')
axes[0].set_xticks(range(len(Y)))
axes[0].set_yticks(range(len(X)))
axes[0].set_xticklabels(Y)
axes[0].set_yticklabels(X)
axes[0].set_xlabel('y (Action)', fontsize=11)
axes[0].set_ylabel('x (State)', fontsize=11)
axes[0].set_title('f(x,y)', fontsize=12, fontweight='bold')
for i in range(len(X)):
    for j in range(len(Y)):
        axes[0].text(j, i, f'{f[i,j]:.1f}', ha='center', va='center', color='black', fontsize=11)
plt.colorbar(im1, ax=axes[0], fraction=0.046, pad=0.04)

# Panel 2: Product measure (μ × ν)
product_measure = np.outer(mu, nu)
im2 = axes[1].imshow(product_measure, cmap='Blues', aspect='auto')
axes[1].set_xticks(range(len(Y)))
axes[1].set_yticks(range(len(X)))
axes[1].set_xticklabels(Y)
axes[1].set_yticklabels(X)
axes[1].set_xlabel('y', fontsize=11)
axes[1].set_ylabel('x', fontsize=11)
axes[1].set_title('(μ × ν)({(x,y)})', fontsize=12, fontweight='bold')
for i in range(len(X)):
    for j in range(len(Y)):
        axes[1].text(j, i, f'{product_measure[i,j]:.3f}', ha='center', va='center', color='black', fontsize=10)
plt.colorbar(im2, ax=axes[1], fraction=0.046, pad=0.04)

# Panel 3: Integrand f(x,y) · (μ × ν)
integrand = f * product_measure
im3 = axes[2].imshow(integrand, cmap='Greens', aspect='auto')
axes[2].set_xticks(range(len(Y)))
axes[2].set_yticks(range(len(X)))
axes[2].set_xticklabels(Y)
axes[2].set_yticklabels(X)
axes[2].set_xlabel('y', fontsize=11)
axes[2].set_ylabel('x', fontsize=11)
axes[2].set_title('f(x,y) · (μ × ν) [contribution]', fontsize=12, fontweight='bold')
for i in range(len(X)):
    for j in range(len(Y)):
        axes[2].text(j, i, f'{integrand[i,j]:.3f}', ha='center', va='center', color='black', fontsize=10)
plt.colorbar(im3, ax=axes[2], fraction=0.046, pad=0.04)

plt.tight_layout()
plt.savefig('Week_2/tonelli_verification.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"\nSum of contributions: {np.sum(integrand):.6f} = {results['double']:.6f} ✓")
```

**Output:**
```
Function f(x,y):
x \ y   a           b
1       1.00        2.00
2       2.00        4.00
3       3.00        6.00

============================================================
Tonelli Verification:
============================================================

Method 1: ∫_X (∫_Y f(x,y) dν(y)) dμ(x)
Inner integrals F1(x) = ∫_Y f(x,y) dν(y):
  F1(1) = 1.3333
  F1(2) = 2.6667
  F1(3) = 4.0000

Outer integral: ∫_X F1(x) dμ(x) = 2.000000

------------------------------------------------------------

Method 2: ∫_Y (∫_X f(x,y) dμ(x)) dν(y)
Inner integrals F2(y) = ∫_X f(x,y) dμ(x):
  F2('a') = 1.5000
  F2('b') = 3.0000

Outer integral: ∫_Y F2(y) dν(y) = 2.000000

------------------------------------------------------------

Method 3: ∫_{X×Y} f d(μ × ν)
Double integral: 2.000000

============================================================
VERIFICATION:
============================================================
Iterated (Y first, X outer): 2.000000
Iterated (X first, Y outer): 2.000000
Double integral:              2.000000

All equal? True

✓ Tonelli's theorem verified numerically!
```

**RL Interpretation:**

This discrete example models a simplified policy evaluation scenario:
- **State space** $X = \{1, 2, 3\}$ with initial state distribution $\mu$ (e.g., $\mu(\{1\}) = 1/2$ means state 1 is visited with probability 1/2)
- **Action space** $Y = \{a, b\}$ with policy $\pi$ represented by $\nu$ (e.g., $\nu(\{a\}) = 2/3$ means action $a$ is chosen with probability 2/3 under a stochastic policy)
- **Function** $f(x,y)$: Represents a non-negative quantity like immediate reward or feature value

The three computation methods correspond to:
1. **Sample states first, then actions:** $\sum_{x} \mu(\{x\}) \left(\sum_{y} f(x,y) \nu(\{y\})\right)$ — standard Monte Carlo estimation
2. **Sample actions first, then states:** $\sum_{y} \nu(\{y\}) \left(\sum_{x} f(x,y) \mu(\{x\})\right)$ — alternative sampling order
3. **Joint sampling:** $\sum_{x,y} f(x,y) \cdot \mu(\{x\}) \nu(\{y\})$ — direct expectation under joint distribution

Tonelli guarantees all three give identical results when $f \geq 0$, validating the computational equivalence that underpins RL algorithms.

---

### **V. Application Bridge: Tonelli in Reinforcement Learning Algorithms**

#### **A. Policy Evaluation via Iterated Expectations**

**Setting:** Consider an MDP with state space $\mathcal{S}$, action space $\mathcal{A}$, transition kernel $P(s'|s,a)$, reward function $R(s,a,s')$, and policy $\pi(a|s)$. The **state-value function** $V^{\pi}$ satisfies the Bellman expectation equation:

$$
V^{\pi}(s) = \mathbb{E}_{a \sim \pi(\cdot|s)}\left[\mathbb{E}_{s' \sim P(\cdot|s,a)}[R(s,a,s') + \gamma V^{\pi}(s')]\right]
$$

**Question:** Is this well-defined? Can we compute it as an iterated integral?

**Answer via Tonelli:** Assume $R + \gamma V^{\pi} \geq 0$ (non-negative rewards/values, or absorb the negative part separately). Then:

$$
V^{\pi}(s) = \int_{\mathcal{A}} \left(\int_{\mathcal{S}'} [R(s,a,s') + \gamma V^{\pi}(s')] \, P(ds'|s,a)\right) \pi(da|s)
$$

**Verification that Tonelli applies:**
1. The integrand $g(a, s') = R(s,a,s') + \gamma V^{\pi}(s')$ is non-negative by assumption
2. The joint distribution over $(a, s')$ given fixed $s$ is constructed via the Ionescu-Tulcea theorem (conditional product), not as a product measure in the sense of Day 1—it's a measure kernel indexed by $s$
3. By Tonelli-type arguments for conditional measures (Kallenberg §6.3), the iterated integral is well-defined when the integrand is non-negative

**Algorithmic implementation:**

In tabular policy evaluation, we iterate:
$$
V_{k+1}(s) = \sum_{a \in \mathcal{A}} \pi(a|s) \sum_{s' \in \mathcal{S}} P(s'|s,a) [R(s,a,s') + \gamma V_k(s')]
$$
until convergence. Tonelli (via Corollary 2.1 for counting measure) guarantees:
1. The RHS is well-defined (finite sum of non-negative terms when $R \geq 0$)
2. The order of summation doesn't matter: $\sum_a \sum_{s'} = \sum_{s'} \sum_a$
3. This equals the joint sum $\sum_{(a,s')} \pi(a|s) P(s'|s,a) [\cdots]$

**Why this matters:** When implementing on distributed systems, we can partition the sum over $\mathcal{A}$ or $\mathcal{S}'$ without affecting the result. This enables parallel computation:
- **Worker 1:** Compute partial sum over $\mathcal{A}_1 = \{a_1, \ldots, a_k\}$
- **Worker 2:** Compute partial sum over $\mathcal{A}_2 = \{a_{k+1}, \ldots, a_n\}$
- **Aggregate:** Sum the two partial results

Tonelli guarantees the aggregated result equals the sequential computation.

**Monte Carlo estimation:** Sample trajectories $(s_t, a_t, s_{t+1})$ where $a_t \sim \pi(\cdot|s_t)$ and $s_{t+1} \sim P(\cdot|s_t, a_t)$. Then:
$$
V^{\pi}(s) \approx \frac{1}{N} \sum_{i=1}^{N} [R(s, a_i, s_i') + \gamma V^{\pi}(s_i')]
$$
converges to the true value by the law of large numbers, which relies on Tonelli ensuring the iterated expectation is well-defined.

---

#### **B. Model-Based Planning and Bellman Backups**

In **model-based RL** (Dyna, MBPO, MuZero), we perform Bellman backups:

$$
(T^{\pi} V)(s) = \mathbb{E}_{a,s'}[R(s,a,s') + \gamma V(s')]
$$

where the expectation is over $a \sim \pi(\cdot|s)$ and $s' \sim P(\cdot|s,a)$.

**Tonelli's role:** When $R + \gamma V \geq 0$, Tonelli guarantees:
$$
(T^{\pi} V)(s) = \int_{\mathcal{A}} \pi(a|s) \left(\int_{\mathcal{S}'} [R(s,a,s') + \gamma V(s')] \, P(ds'|s,a)\right)
$$

is well-defined, even if we haven't verified $\mathbb{E}[|R + \gamma V|] < \infty$.

**Practical impact:**
- In **MBPO** (Janner et al., ICML 2019), learned dynamics models $\hat{P}(\cdot|s,a)$ are used with pessimistic value estimates to prevent model exploitation. When rewards are bounded or normalized, Tonelli applies to the resulting non-negative Bellman targets.
- In **MuZero** (Schrittwieser et al., Nature 2020), when rewards and values are non-negative, the bootstrapped return $G_t = \sum_{k=0}^{n-1} \gamma^k R_{t+k} + \gamma^n V(s_{t+n})$ satisfies $G_t \geq 0$. If computed under the ground-truth dynamics, $\mathbb{E}[G_t]$ can be expressed as an iterated integral over $a_t, s_{t+1}, a_{t+1}, \ldots$, where Tonelli justifies the interchange. In MuZero's learned model, this provides intuition but not a formal guarantee (model error must be accounted for separately).

---

#### **C. Feature Expectations in Linear Function Approximation**

In **linear value function approximation**, we approximate:
$$
V^{\pi}(s) \approx \theta^\top \phi(s) = \sum_{k=1}^{d} \theta_k \phi_k(s)
$$

where $\phi: \mathcal{S} \to \mathbb{R}^d$ is a feature vector.

**Computing feature expectations:** To fit $\theta$ via least squares (LSTD), we compute:
$$
\mathbb{E}_{s \sim \mu}[\phi(s) \phi(s)^\top] \quad \text{and} \quad \mathbb{E}_{s,s'}[\phi(s) (R(s,a,s') + \gamma \phi(s')^\top \theta)]
$$

By linearity of the integral (Week 1, Day 2, Proposition 1.5):
$$
\mathbb{E}\left[\sum_{k=1}^{d} \phi_k(s)\right] = \sum_{k=1}^{d} \mathbb{E}[\phi_k(s)]
$$
This holds for any finite sum, regardless of sign. Tonelli becomes relevant when computing $\mathbb{E}[\phi_k(s) \phi_\ell(s')]$ via iterated integrals over $(s, s')$ in temporal-difference learning (Week 35).

**Reference:** Bradtke & Barto (1996), "Linear Least-Squares Algorithms for Temporal Difference Learning," *Machine Learning*. For policy iteration with LSTD, see Lagoudakis & Parr (2003), *JMLR*.

---

### **VI. Mathematical Insight and Forward Connections**

**Mathematical Insight:**

Tonelli's theorem reveals that for **non-negative functions**, integration over product spaces is **commutative**—the order of integration does not matter. This is a profound geometric fact: the "volume under the surface" $f(x,y)$ over $X \times Y$ can be computed by slicing in either direction, and both give the same answer.

The key mechanism is the **Monotone Convergence Theorem**, which allows us to pass limits inside integrals without requiring uniform convergence. This is why non-negativity is essential: MCT requires monotone increasing sequences, which are automatically well-behaved for non-negative functions.

**Contrast with Fubini (Day 3):** When $f$ can be negative, cancellation can occur, and convergence becomes delicate. Fubini requires **integrability** ($\int |f| < \infty$) to ensure that positive and negative parts are both controlled, preventing pathological behavior (which we demonstrate via counterexample tomorrow).

**RL Connection:**

Tonelli is the mathematical foundation for **iterated expectations** in RL:
- Policy evaluation computes $\mathbb{E}_{a \sim \pi}[\mathbb{E}_{s' \sim P}[\cdots]]$
- Model-based planning iterates Bellman backups $\mathbb{E}_{a,s'}[R + \gamma V]$
- Monte Carlo methods sample from joint distributions and average

All of these rely on Tonelli ensuring that "integrate over $a$, then $s'$" equals "integrate over $(a, s')$ jointly," which equals "integrate over $s'$, then $a$."

**Open Questions:**

1. **When can we apply Tonelli in deep RL?** Neural network value functions $V_{\theta}(s)$ can be negative. Practical strategies in deep RL:
   - **Positive-part decomposition:** Rarely used—computing $V_\theta^+$ and $V_\theta^-$ separately doubles computation.
   - **Bounded value functions:** In practice, clip values to $[V_{\min}, V_{\max}]$ (e.g., in DQN, rewards are clipped to $[-1, 1]$, forcing $|V| \leq 1/(1-\gamma)$). This ensures integrability via Fubini.
   - **Ignore measure theory:** Most deep RL algorithms (DQN, PPO, SAC) don't verify integrability—they rely on function approximation and gradient descent. Tonelli/Fubini matter for convergence proofs (e.g., Tsitsiklis & Van Roy 1997, "An Analysis of Temporal-Difference Learning with Function Approximation"), not for implementation.

   The key question for convergence analysis: Does $\mathbb{E}[|R + \gamma V_\theta(s')|] < \infty$ hold under the behavior policy?

2. **Infinite-dimensional extensions:** In continuous-time RL (Week 38), trajectories are paths $t \mapsto s_t$ in infinite-dimensional function spaces. Does Tonelli extend to such settings? This requires **Kolmogorov extension theorem** (Week 3) and careful treatment of infinite products.

3. **Non-σ-finite spaces:** What happens if the state space is not σ-finite (e.g., counting measure on an uncountable set)? Tonelli fails (counterexample tomorrow). Are there RL scenarios where non-σ-finite measures arise? (Hint: certain POMDPs with continuous observation spaces may exhibit this pathology.)

---

**Looking Ahead:**

- **Day 3 (Tomorrow):** **Fubini's theorem** extends Tonelli to integrable functions $f \in L^1(\mu \times \nu)$, requiring $\int |f| < \infty$. We construct two key counterexamples:
  1. **Without σ-finiteness:** Counting measure on uncountable sets makes product measure non-unique
  2. **Without integrability:** We've already seen a preview in Exercise 2(b)—tomorrow we sharpen this into a pathological function where $\int_X \int_Y f \neq \int_Y \int_X f$

  **RL connection:** Importance sampling ratios $\frac{\pi(a|s)}{\mu(a|s)}$ in off-policy learning require integrability checks to apply Fubini—when the ratio is unbounded, policy gradient estimates can diverge.

- **Day 4:** $L^p$ spaces provide the function space framework where Bellman operators act. We prove **Hölder's inequality** and **Minkowski's inequality**, establishing the normed space structure of $L^p$.

- **Week 3:** Radon-Nikodym theorem formalizes "changing measures" (importance sampling), and $L^p$ duality $(L^p)^* \cong L^q$ enables functional-analytic treatment of value functions.

Tonelli is the computational engine—tomorrow, we upgrade it to Fubini, handling the full complexity of signed functions.

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_2_exercises_FINAL]]**
