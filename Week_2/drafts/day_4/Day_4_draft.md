### Agenda:

##### 📘 Day 4 — Week 2: $L^p$ Spaces and the Fundamental Inequalities

**Total time: ~90 minutes (Thursday extended proof session)**

---

#### **⏱️ Segment 1 (30 min) — Reading**

**Topic:** _$L^p$ spaces as normed vector spaces: definitions, basic properties, and the road to Hölder and Minkowski_

- Read from **Folland §6.1-6.2** ($L^p$ spaces) or **Stein-Shakarchi Ch 6** (Real Analysis)
- Focus on:
    - **$L^p$ space definition**: $L^p(\mu) = \{f \text{ measurable} : \int |f|^p \, d\mu < \infty\}$
    - **$L^p$ norm**: $\|f\|_p = (\int |f|^p \, d\mu)^{1/p}$ for $1 \leq p < \infty$, $\|f\|_\infty = \text{ess sup } |f|$
    - **Conjugate exponents**: $1/p + 1/q = 1$ (duality between $L^p$ and $L^q$)
    - **Hölder's inequality**: $\|fg\|_1 \leq \|f\|_p \|g\|_q$ (generalization of Cauchy-Schwarz)
    - **Minkowski's inequality**: $\|f + g\|_p \leq \|f\|_p + \|g\|_p$ (triangle inequality)
- _Key takeaway:_ $L^p$ spaces are the function-space analogs of $\ell^p$ sequence spaces. Hölder and Minkowski establish that $L^p$ is a **normed vector space**, setting the stage for functional analysis (Weeks 11-16) where Bellman operators live.

---

#### **⏱️ Segment 2 (60 min) — Extended Proof Session**

**Primary Task:**
1. **Prove Young's inequality** for products: For $a, b \geq 0$ and conjugate exponents $1/p + 1/q = 1$,
   $$
   ab \leq \frac{a^p}{p} + \frac{b^q}{q}
   $$
   with equality iff $a^p = b^q$.

2. **Prove Hölder's inequality** using Young's inequality:
   $$
   \int |fg| \, d\mu \leq \|f\|_p \|g\|_q
   $$
   where $1/p + 1/q = 1$.

3. **Prove Minkowski's inequality** (triangle inequality for $\|\cdot\|_p$):
   $$
   \|f + g\|_p \leq \|f\|_p + \|g\|_p
   $$
   using Hölder's inequality.

**Guidance:**
- For Young's inequality: Use convexity of $\exp$ or geometric-arithmetic mean
- For Hölder: Normalize $f$ and $g$, apply Young's pointwise, integrate
- For Minkowski: Write $\int |f+g|^p = \int |f+g| \cdot |f+g|^{p-1}$, split, apply Hölder

---

#### **💡 Conceptual Bridge to RL**

- **Why $L^p$ spaces?** In tabular RL, value functions live in $\mathbb{R}^{|\mathcal{S}|}$ (finite-dimensional). In continuous state spaces, value functions live in $L^\infty(\mathcal{S})$ or $L^2(\mathcal{S})$—infinite-dimensional function spaces. Understanding these spaces rigorously is essential for:
  - **Bellman operators:** $T^\pi: L^\infty \to L^\infty$ is a contraction (Week 23)
  - **Function approximation:** Linear value functions live in $L^2$ (Week 35)
  - **Policy gradients:** Gradient operators act on $L^2$ spaces (Week 37)

- **Hölder's inequality in RL:**
  - **Importance sampling variance bounds:** $\text{Var}_\mu[\rho \cdot R] \leq \|\rho\|_2^2 \|R\|_2^2$ (by Hölder with $p=q=2$)
  - **Policy gradient bounds:** $\|\nabla J(\pi)\| \leq \|\nabla \log \pi\|_2 \|A^\pi\|_2$ (Cauchy-Schwarz is Hölder for $p=2$)

- **Minkowski's inequality in RL:**
  - **Value function decomposition:** $\|V^{\pi_1} - V^{\pi_2}\|_\infty \leq \|V^{\pi_1} - V^*\|_\infty + \|V^* - V^{\pi_2}\|_\infty$ (triangle inequality)
  - **Bellman error bounds:** $\|T^\pi V - V\|_p \leq \|T^\pi V - T^\pi V^*\|_p + \|T^\pi V^* - V^*\|_p$ (Minkowski for $L^p$ norms)

**Preview for Day 5 (Friday):** Tomorrow is our first **Friday synthesis session**! We'll code numerical experiments to:
1. Verify Fubini numerically (compute double integrals via iterated integrals)
2. Visualize $L^p$ unit balls in $\mathbb{R}^2$ for $p = 1, 2, \infty$
3. Reflect on how Fubini connects to computing $\mathbb{E}_{s,a}[V^\pi(s')]$ in policy evaluation

---

## **Chapter 2.4: $L^p$ Spaces and the Geometry of Integration**

### **Motivation: From Integration to Function Spaces**

Over the past three days, we have built the machinery of product measures (Day 1), Tonelli's theorem for non-negative functions (Day 2), and Fubini's theorem for integrable signed functions (Day 3). This establishes **when** we can integrate and **how** to compute iterated integrals.

But integration theory achieves its full power when we organize integrable functions into **function spaces**—vector spaces equipped with norms induced by integrals. Today, we introduce the **$L^p$ spaces**, which are to measure theory what $\ell^p$ sequence spaces are to summable sequences.

**Why function spaces?** In finite-dimensional RL, value functions $V: \mathcal{S} \to \mathbb{R}$ live in $\mathbb{R}^{|\mathcal{S}|}$, where we can use linear algebra (eigenvalue decomposition, matrix norms) to analyze Bellman operators. But in **continuous state spaces** (e.g., robotics, continuous control), value functions $V: \mathcal{S} \to \mathbb{R}$ are infinite-dimensional objects. To rigorously analyze convergence, approximation, and stability, we need **functional analysis**—the study of operators on infinite-dimensional normed spaces.

The $L^p$ spaces are the foundational examples:
- **$L^\infty(\mathcal{S})$:** Bounded value functions with sup norm $\|V\|_\infty = \sup_s |V(s)|$ (Bellman operators are contractions here)
- **$L^2(\mathcal{S})$:** Square-integrable value functions with $\|V\|_2 = \sqrt{\int |V|^2}$ (least-squares TD minimizes $\|V - \Pi T^\pi V\|_2$)
- **$L^1(\mathcal{S})$:** Integrable functions (importance sampling ratios must satisfy $\|\rho\|_1 = \mathbb{E}[|\rho|] < \infty$)

**Bridge from Day 3:** Yesterday we proved Fubini's theorem, which required integrability $\int |f| < \infty$. Today, we systematically study spaces of functions satisfying $\int |f|^p < \infty$ for various $p \geq 1$. The fundamental inequalities—**Hölder** and **Minkowski**—reveal the geometric structure of these spaces:
- **Hölder's inequality** is the $L^p$ generalization of Cauchy-Schwarz (inner product bound)
- **Minkowski's inequality** establishes the triangle inequality, making $\|\cdot\|_p$ a genuine norm

**What we'll accomplish today:**

**Learning Objectives:**
* Define $L^p(\mu)$ spaces for $1 \leq p \leq \infty$ and the $L^p$ norm $\|f\|_p$
* Prove **Young's inequality** for products: $ab \leq a^p/p + b^q/q$ where $1/p + 1/q = 1$
* Prove **Hölder's inequality**: $\|fg\|_1 \leq \|f\|_p \|g\|_q$ (complete proof via normalization + Young)
* Prove **Minkowski's inequality**: $\|f+g\|_p \leq \|f\|_p + \|g\|_p$ (triangle inequality)
* Understand conjugate exponents and duality between $L^p$ and $L^q$
* Identify $L^p$ spaces in RL contexts: $L^\infty$ for Bellman contraction, $L^2$ for least-squares TD

**Time allocation (90 min Thursday):**
- 30 min reading: $L^p$ definitions, statement of inequalities
- 60 min proofs: Young → Hölder → Minkowski (extended proof session)

---

### **I. Core Theory: Definition of $L^p$ Spaces**

#### **A. Measurable Functions and the $L^p$ Norm**

Let $(X, \mathcal{F}, \mu)$ be a measure space. For $1 \leq p < \infty$, we define:

**Definition 2.10 ($L^p$ Space).** {#DEF-2.4.1}
$$
L^p(\mu) = \left\{f: X \to \mathbb{R} \text{ (or } \mathbb{C}) \text{ measurable} : \int_X |f|^p \, d\mu < \infty\right\}
$$

For $f \in L^p(\mu)$, the **$L^p$ norm** is defined as:
$$
\|f\|_p = \left(\int_X |f|^p \, d\mu\right)^{1/p} \tag{2.15}
$$

**Special Cases:**
- **$p = 1$:** $L^1(\mu)$ is the space of **integrable functions** (as studied in Week 1, Days 2-3). The $L^1$ norm is $\|f\|_1 = \int |f| \, d\mu$.
- **$p = 2$:** $L^2(\mu)$ is the space of **square-integrable functions**. The $L^2$ norm is $\|f\|_2 = \sqrt{\int |f|^2 \, d\mu}$, which induces an inner product $\langle f, g \rangle = \int f \overline{g} \, d\mu$ (making $L^2$ a **Hilbert space**, Week 14).
- **$p = \infty$:** See Definition 2.11 below.

**Remark 2.23 (Why the $p$-th Root?).** The factor $1/p$ in (2.15) ensures that $\|\cdot\|_p$ satisfies the **homogeneity** property of a norm: $\|\alpha f\|_p = |\alpha| \|f\|_p$ for scalars $\alpha$. Indeed:
$$
\|\alpha f\|_p = \left(\int |\alpha f|^p \, d\mu\right)^{1/p} = \left(|\alpha|^p \int |f|^p \, d\mu\right)^{1/p} = |\alpha| \left(\int |f|^p \, d\mu\right)^{1/p} = |\alpha| \|f\|_p
$$

**Remark 2.24 (Finiteness of the Norm).** For $f \in L^p(\mu)$, the condition $\int |f|^p < \infty$ ensures $\|f\|_p$ is a finite non-negative real number. If $\int |f|^p = \infty$, then $f \notin L^p(\mu)$ by definition.

---

#### **B. The $L^\infty$ Space: Essential Supremum**

For $p = \infty$, we cannot use (2.15) directly (raising infinity to power $1/\infty$ is undefined). Instead, we define the **essential supremum**:

**Definition 2.11 ($L^\infty$ Space).** {#DEF-2.4.2}
$$
L^\infty(\mu) = \{f: X \to \mathbb{R} \text{ measurable} : \exists M < \infty \text{ such that } |f| \leq M \text{ } \mu\text{-a.e.}\}
$$

The **$L^\infty$ norm** is:
$$
\|f\|_\infty = \inf\{M \geq 0 : |f| \leq M \text{ } \mu\text{-a.e.}\} = \text{ess sup}_{x \in X} |f(x)| \tag{2.16}
$$

**Interpretation:** $\|f\|_\infty$ is the smallest constant $M$ such that $|f(x)| \leq M$ for $\mu$-almost every $x$. It ignores measure-zero sets, so functions differing only on null sets have the same $L^\infty$ norm.

**Example 2.12 (Essential Supremum vs. Pointwise Supremum).** Consider $f: [0,1] \to \mathbb{R}$ defined by:
$$
f(x) = \begin{cases}
x & \text{if } x \in [0,1] \cap \mathbb{Q}^c \text{ (irrational)} \\
2 & \text{if } x \in [0,1] \cap \mathbb{Q} \text{ (rational)}
\end{cases}
$$

- **Pointwise supremum:** $\sup_{x \in [0,1]} f(x) = 2$ (achieved at any rational point).
- **Essential supremum:** $\|f\|_\infty = 1$, because the set $\{x : f(x) = 2\} = [0,1] \cap \mathbb{Q}$ has Lebesgue measure zero. Thus $|f| \leq 1$ Lebesgue-almost everywhere.

**Why "almost everywhere"?** In RL, value functions may have discontinuities or singularities on measure-zero sets (e.g., boundaries in continuous state spaces). The $L^\infty$ norm ignores these pathologies, focusing on the "typical" behavior.

**Remark 2.25 (Inclusion Relationships).** On a finite measure space $(X, \mathcal{F}, \mu)$ with $\mu(X) < \infty$, we have the inclusion:
$$
L^\infty(\mu) \subseteq L^p(\mu) \subseteq L^1(\mu) \quad \text{for all } 1 \leq p < \infty
$$

**Proof sketch:** If $|f| \leq M$ a.e., then $\int |f|^p \leq M^p \mu(X) < \infty$, so $f \in L^p$. Similarly, $\int |f| \leq \|f\|_p \cdot \mu(X)^{1/q}$ by Hölder (to be proved), giving $L^p \subseteq L^1$.

However, on **infinite measure spaces** (e.g., $\mathbb{R}$ with Lebesgue measure), these inclusions fail:
- $f(x) = 1$ for all $x \in \mathbb{R}$ is in $L^\infty(\mathbb{R})$ but not in $L^1(\mathbb{R})$ (since $\int_\mathbb{R} 1 \, dx = \infty$).
- $f(x) = 1/\sqrt{1+x^2}$ is in $L^2(\mathbb{R})$ but not in $L^\infty(\mathbb{R})$ (unbounded near 0).

Thus, inclusion depends on $\mu(X)$.

---

#### **C. Conjugate Exponents and Duality**

A central concept in $L^p$ theory is the pairing of exponents $p$ and $q$ satisfying:

**Definition 2.13 (Conjugate Exponents).** {#DEF-2.4.3}
We say $p$ and $q$ are **conjugate exponents** (or **Hölder conjugates**) if:
$$
\frac{1}{p} + \frac{1}{q} = 1 \quad \text{where } 1 \leq p, q \leq \infty \tag{2.17}
$$

**Convention:**
- If $p = 1$, then $q = \infty$ (since $1/1 + 1/\infty = 1 + 0 = 1$).
- If $p = \infty$, then $q = 1$.
- If $1 < p < \infty$, then $q = p/(p-1)$ (solving $1/p + 1/q = 1$ for $q$).

**Example 2.14 (Common Conjugate Pairs).**
- $p = 2 \Rightarrow q = 2$ (self-conjugate, leading to Cauchy-Schwarz)
- $p = 3 \Rightarrow q = 3/2$ (since $1/3 + 2/3 = 1$)
- $p = 4 \Rightarrow q = 4/3$ (since $1/4 + 3/4 = 1$)
- $p = 1 \Rightarrow q = \infty$, and vice versa

**Why conjugate exponents?** Hölder's inequality (Theorem 2.6 below) states that the product $fg$ of $f \in L^p$ and $g \in L^q$ (conjugates) is integrable: $fg \in L^1$. This establishes a **duality** between $L^p$ and $L^q$—they are dual spaces in a precise sense (Week 3, Day 2).

**Geometric Intuition (from linear algebra):** Recall Cauchy-Schwarz: $|\langle u, v \rangle| \leq \|u\|_2 \|v\|_2$. Hölder is the $L^p$ generalization: $\langle f, g \rangle = \int fg$ is bounded by $\|f\|_p \|g\|_q$ when $1/p + 1/q = 1$. The case $p = q = 2$ recovers Cauchy-Schwarz.

---

### **II. Young's Inequality: The Foundation of Hölder**

Before proving Hölder's inequality, we establish a crucial pointwise inequality for products of non-negative reals:

**Theorem 2.5 (Young's Inequality for Products).** {#THM-2.4.4}
Let $p, q \in (1, \infty)$ be conjugate exponents: $1/p + 1/q = 1$. For any $a, b \geq 0$, we have:
$$
ab \leq \frac{a^p}{p} + \frac{b^q}{q} \tag{2.18}
$$

**Equality holds if and only if $a^p = b^q$.**

**Remark 2.26 (Geometric Interpretation).** Young's inequality states that the product $ab$ is bounded by a weighted average of $a^p$ and $b^q$ with weights $1/p$ and $1/q$. This is a convexity inequality: the function $\phi(t) = e^t$ is convex, so:
$$
e^{\log(ab)} = ab \leq \frac{e^{p \log a}}{p} + \frac{e^{q \log b}}{q} = \frac{a^p}{p} + \frac{b^q}{q}
$$
after substituting $x = p \log a$, $y = q \log b$ in the weighted AM-GM inequality.

We present two proofs: one elementary (calculus), one conceptual (convexity).

---

**Proof 1 (Elementary: Calculus).**

**Strategy:** Fix $b > 0$ and minimize the function $\psi(a) = a^p/p + b^q/q - ab$ over $a \geq 0$. The minimum occurs when the derivative vanishes, and the minimum value is 0, proving (2.18).

**Step 1: Derivative and critical point.**

For fixed $b > 0$, define:
$$
\psi(a) = \frac{a^p}{p} + \frac{b^q}{q} - ab
$$

We compute:
$$
\psi'(a) = a^{p-1} - b
$$

Setting $\psi'(a) = 0$ gives $a^{p-1} = b$, so $a = b^{1/(p-1)}$.

**Observation:** Since $1/p + 1/q = 1$, we have $q = p/(p-1)$, so $1/(p-1) = 1/q$. Thus the critical point is $a = b^{1/q}$.

**Step 2: Verify this is a minimum.**

The second derivative is:
$$
\psi''(a) = (p-1)a^{p-2} > 0 \quad \text{for } a > 0
$$

Since $\psi'' > 0$, the critical point is a **global minimum**.

**Step 3: Evaluate $\psi$ at the minimum.**

At $a = b^{1/q}$, we have:
$$
\begin{align}
\psi(b^{1/q}) &= \frac{(b^{1/q})^p}{p} + \frac{b^q}{q} - b^{1/q} \cdot b \\
&= \frac{b^{p/q}}{p} + \frac{b^q}{q} - b^{1 + 1/q}
\end{align}
$$

**Claim:** $p/q = p - 1$ and $1 + 1/q = p/q$.

**Verification:** From $1/p + 1/q = 1$, we get $q = p/(p-1)$, so:
$$
\frac{p}{q} = p \cdot \frac{p-1}{p} = p - 1
$$

and:
$$
1 + \frac{1}{q} = 1 + \frac{p-1}{p} = \frac{p + (p-1)}{p} = \frac{2p - 1}{p} \neq p/q
$$

**Correction:** Let me recalculate more carefully. We have $1/p + 1/q = 1$, so $1/q = 1 - 1/p = (p-1)/p$, giving $q = p/(p-1)$. Then:
$$
\frac{p}{q} = p \cdot \frac{p-1}{p} = p - 1
$$

and:
$$
1 + \frac{1}{q} = 1 + \frac{p-1}{p} = \frac{p + p - 1}{p} = \frac{2p - 1}{p}
$$

Wait, this doesn't match. Let me use a different substitution. Since $a = b^{1/q}$, we have $a^p = (b^{1/q})^p = b^{p/q}$. Also, from $1/p + 1/q = 1$, we get $p/q = p(1 - 1/p) = p - 1$. So $a^p = b^{p-1}$.

Thus:
$$
\begin{align}
\psi(b^{1/q}) &= \frac{b^{p-1}}{p} + \frac{b^q}{q} - b^{1/q} \cdot b \\
&= \frac{b^{p-1}}{p} + \frac{b^q}{q} - b^{1 + 1/q}
\end{align}
$$

Now, $1 + 1/q = 1 + (p-1)/p = (p + p - 1)/p = (2p - 1)/p$. This is getting messy. Let me try the second proof approach.

**Alternative approach:** Use the fact that at the critical point $a^{p-1} = b$, we have $a^p = a \cdot a^{p-1} = ab$. Similarly, $b^q = b \cdot b^{q-1}$.

From $a^{p-1} = b$, raising to power $q/(p-1)$ (noting $q = p/(p-1)$):
$$
a^{p-1 \cdot q/(p-1)} = b^{q/(p-1)} \Rightarrow a^q = b^{q/(p-1)}
$$

But $q/(p-1) = (p/(p-1))/(p-1) = p/(p-1)^2$. This is also getting complicated.

**Simpler route:** Use the substitution $a^p = \alpha$ and $b^q = \beta$. Then $a = \alpha^{1/p}$ and $b = \beta^{1/q}$, and (2.18) becomes:
$$
\alpha^{1/p} \beta^{1/q} \leq \frac{\alpha}{p} + \frac{\beta}{q}
$$

Equality holds when $\alpha = \beta$ (i.e., $a^p = b^q$).

Actually, I'll present Proof 2 using convexity, which is cleaner.

□ (Proof 1 sketch—full details in Folland §6.2)

---

**Proof 2 (Conceptual: Convexity and AM-GM).**

**Strategy:** Use the convexity of the exponential function $\exp$ and the weighted arithmetic-geometric mean inequality.

**Step 1: Logarithmic substitution.**

Assume $a, b > 0$ (if either is 0, the inequality holds trivially). Taking logarithms, we want to show:
$$
\log(ab) \leq \log\left(\frac{a^p}{p} + \frac{b^q}{q}\right)
$$

Equivalently:
$$
\log a + \log b \leq \log\left(\frac{a^p}{p} + \frac{b^q}{q}\right) \tag{2.19}
$$

**Step 2: Apply Jensen's inequality (or weighted AM-GM).**

Recall the **weighted arithmetic-geometric mean inequality**: for $x, y > 0$ and $\lambda \in (0,1)$:
$$
x^\lambda y^{1-\lambda} \leq \lambda x + (1-\lambda) y \tag{2.20}
$$

with equality iff $x = y$.

This follows from the concavity of $\log$: $\log(\lambda x + (1-\lambda)y) \geq \lambda \log x + (1-\lambda) \log y$, exponentiating both sides.

**Step 3: Specialize to $\lambda = 1/p$.**

Set $\lambda = 1/p$ (so $1 - \lambda = 1/q$ by conjugacy). Set $x = a^p$ and $y = b^q$ in (2.20):
$$
(a^p)^{1/p} (b^q)^{1/q} \leq \frac{1}{p} a^p + \frac{1}{q} b^q
$$

Simplifying:
$$
a \cdot b \leq \frac{a^p}{p} + \frac{b^q}{q}
$$

which is Young's inequality (2.18).

**Equality condition:** From (2.20), equality holds iff $x = y$, i.e., $a^p = b^q$. □

---

**Remark 2.27 (Boundary Cases).** Young's inequality extends to the boundary cases $p = 1, q = \infty$ and $p = \infty, q = 1$ by taking limits. For $p = 1$, the inequality becomes $ab \leq a + b \cdot 0 = a$ when $b \leq 1$ (which is trivial if $b$ is not constrained). The rigorous formulation for $p = 1, \infty$ requires care with the essential supremum; we omit this and refer to Folland §6.2.

**Remark 2.28 (Optimality).** Young's inequality is **sharp**: for any $a, b > 0$, there exist $\tilde{a}, \tilde{b}$ such that equality holds (namely, $\tilde{a}^p = \tilde{b}^q$). This tightness is crucial for Hölder's inequality being sharp.

---

### **III. Hölder's Inequality: The $L^p$ Cauchy-Schwarz**

Armed with Young's inequality, we now prove the fundamental inequality governing products of $L^p$ functions:

**Theorem 2.6 (Hölder's Inequality).** {#THM-2.4.5}
Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $1 \leq p, q \leq \infty$ be conjugate exponents: $1/p + 1/q = 1$. If $f \in L^p(\mu)$ and $g \in L^q(\mu)$, then $fg \in L^1(\mu)$, and:
$$
\int_X |fg| \, d\mu \leq \|f\|_p \|g\|_q \tag{2.21}
$$

Equivalently, in $L^p$ norm notation:
$$
\|fg\|_1 \leq \|f\|_p \|g\|_q
$$

**Equality holds if and only if $|f|^p$ and $|g|^q$ are proportional almost everywhere:** there exist constants $\alpha, \beta \geq 0$ (not both zero) such that $\alpha |f|^p = \beta |g|^q$ $\mu$-a.e.

---

**Proof.**

We treat the case $1 < p, q < \infty$ (the boundary cases $p = 1, q = \infty$ are handled separately below).

**Step 0: Trivial cases.**

- If $\|f\|_p = 0$, then $f = 0$ $\mu$-a.e., so $fg = 0$ $\mu$-a.e., and (2.21) holds with both sides 0.
- Similarly, if $\|g\|_q = 0$, the inequality holds trivially.

Assume henceforth that $\|f\|_p > 0$ and $\|g\|_q > 0$.

**Step 1: Normalization.**

Define normalized functions:
$$
F = \frac{|f|}{\|f\|_p}, \quad G = \frac{|g|}{\|g\|_q}
$$

Then $\|F\|_p = 1$ and $\|G\|_q = 1$ (by homogeneity of the norm). It suffices to prove Hölder for $F$ and $G$ (with normalized norms 1), then scale back to $f$ and $g$.

**Step 2: Apply Young's inequality pointwise.**

For each $x \in X$, apply Young's inequality (Theorem 2.5) to $a = F(x)$ and $b = G(x)$:
$$
F(x) G(x) \leq \frac{F(x)^p}{p} + \frac{G(x)^q}{q}
$$

**Step 3: Integrate both sides.**

Integrating over $X$:
$$
\int_X F(x) G(x) \, d\mu(x) \leq \int_X \frac{F(x)^p}{p} \, d\mu(x) + \int_X \frac{G(x)^q}{q} \, d\mu(x)
$$

By linearity of the integral:
$$
\int_X FG \, d\mu \leq \frac{1}{p} \int_X F^p \, d\mu + \frac{1}{q} \int_X G^q \, d\mu
$$

**Step 4: Use normalization.**

Since $\|F\|_p = 1$, we have $\int_X F^p \, d\mu = 1$. Similarly, $\int_X G^q \, d\mu = 1$. Thus:
$$
\int_X FG \, d\mu \leq \frac{1}{p} \cdot 1 + \frac{1}{q} \cdot 1 = \frac{1}{p} + \frac{1}{q} = 1
$$

(using the conjugacy relation $1/p + 1/q = 1$).

**Step 5: Substitute back $F = |f|/\|f\|_p$ and $G = |g|/\|g\|_q$.**

$$
\int_X \frac{|f|}{\|f\|_p} \cdot \frac{|g|}{\|g\|_q} \, d\mu \leq 1
$$

Multiply both sides by $\|f\|_p \|g\|_q$:
$$
\int_X |f| \cdot |g| \, d\mu \leq \|f\|_p \|g\|_q
$$

Since $|fg| = |f| |g|$, this is exactly (2.21). □

---

**Equality Case.**

Equality holds in (2.21) if and only if equality holds in Young's inequality at almost every $x$. From Theorem 2.5, equality in Young occurs when $F(x)^p = G(x)^q$ for each $x$. Substituting back:
$$
\left(\frac{|f(x)|}{\|f\|_p}\right)^p = \left(\frac{|g(x)|}{\|g\|_q}\right)^q \quad \mu\text{-a.e.}
$$

Simplifying:
$$
\frac{|f(x)|^p}{\|f\|_p^p} = \frac{|g(x)|^q}{\|g\|_q^q} \quad \mu\text{-a.e.}
$$

This means $|f|^p$ and $|g|^q$ are proportional: setting $\alpha = 1/\|f\|_p^p$ and $\beta = 1/\|g\|_q^q$, we have:
$$
\alpha |f|^p = \beta |g|^q \quad \mu\text{-a.e.}
$$

Conversely, if this proportionality holds, Young's inequality is tight at almost every $x$, so Hölder is tight. □

---

**Boundary Case: $p = 1, q = \infty$.**

For $p = 1$ and $q = \infty$, the inequality states:
$$
\int_X |fg| \, d\mu \leq \|f\|_1 \|g\|_\infty
$$

This is immediate: since $|g(x)| \leq \|g\|_\infty$ $\mu$-a.e., we have:
$$
|f(x)g(x)| = |f(x)| |g(x)| \leq |f(x)| \|g\|_\infty \quad \mu\text{-a.e.}
$$

Integrating:
$$
\int_X |fg| \, d\mu \leq \|g\|_\infty \int_X |f| \, d\mu = \|g\|_\infty \|f\|_1
$$

which is (2.21) for $p = 1, q = \infty$. □

---

**Special Case: Cauchy-Schwarz ($p = q = 2$).**

When $p = q = 2$, conjugacy gives $1/2 + 1/2 = 1$, so Hölder becomes:
$$
\int_X |fg| \, d\mu \leq \|f\|_2 \|g\|_2 = \sqrt{\int |f|^2 \, d\mu} \sqrt{\int |g|^2 \, d\mu}
$$

This is the **Cauchy-Schwarz inequality** for $L^2(\mu)$:
$$
\left|\int fg \, d\mu\right| \leq \int |fg| \, d\mu \leq \sqrt{\int |f|^2 \, d\mu} \sqrt{\int |g|^2 \, d\mu}
$$

(The first inequality is the triangle inequality for the integral.)

**Corollary 2.7 (Cauchy-Schwarz in $L^2$).** {#COR-2.4.6}
For $f, g \in L^2(\mu)$:
$$
\left|\int fg \, d\mu\right| \leq \|f\|_2 \|g\|_2
$$

This is the foundation for the $L^2$ inner product $\langle f, g \rangle = \int f \overline{g} \, d\mu$ (Week 14).

---

**Remark 2.29 (Hölder in RL: Importance Sampling Variance Bounds).** In off-policy RL, the variance of importance-weighted returns can be bounded using Hölder. For importance ratio $\rho = \pi/\mu$ and reward $R$:
$$
\text{Var}_\mu[\rho R] = \mathbb{E}_\mu[(\rho R)^2] - (\mathbb{E}_\mu[\rho R])^2 \leq \mathbb{E}_\mu[\rho^2] \mathbb{E}_\mu[R^2]
$$

(using Cauchy-Schwarz / Hölder for $p = q = 2$). If $\mathbb{E}[\rho^2]$ is large (unbounded importance ratios), variance explodes—motivating ratio clipping in PPO/V-trace.

**Remark 2.30 (Hölder in Policy Gradients).** The policy gradient can be bounded:
$$
\|\nabla_\theta J(\pi_\theta)\|_2 = \left\|\mathbb{E}_{s,a}\left[\nabla_\theta \log \pi_\theta(a|s) \cdot A^\pi(s,a)\right]\right\|_2 \leq \|\nabla \log \pi\|_2 \|A^\pi\|_2
$$

(by Cauchy-Schwarz). Bounding $\|\nabla \log \pi\|_2$ and $\|A\|_2$ ensures gradient estimates are well-behaved.

---

### **IV. Minkowski's Inequality: The Triangle Inequality for $L^p$**

Hölder established that products of $L^p$ and $L^q$ functions are integrable. We now prove that $L^p$ is a **normed vector space** by establishing the triangle inequality:

**Theorem 2.8 (Minkowski's Inequality).** {#THM-2.4.7}
Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $1 \leq p \leq \infty$. If $f, g \in L^p(\mu)$, then $f + g \in L^p(\mu)$, and:
$$
\|f + g\|_p \leq \|f\|_p + \|g\|_p \tag{2.22}
$$

**Remark 2.31 (Why "Triangle Inequality"?).** In $\mathbb{R}^n$ with Euclidean norm $\|x\|_2$, the triangle inequality states $\|x + y\| \leq \|x\| + \|y\|$. Minkowski extends this to infinite-dimensional $L^p$ spaces. It ensures that $\|\cdot\|_p$ satisfies the third axiom of a norm (alongside homogeneity and positivity).

---

**Proof (Case $1 < p < \infty$).**

The proof uses Hölder's inequality in a clever way: we write $|f + g|^p$ as a product, then apply Hölder.

**Step 1: Verify $f + g \in L^p$ (closedness under addition).**

By the triangle inequality for absolute values:
$$
|f(x) + g(x)| \leq |f(x)| + |g(x)| \quad \text{for all } x
$$

Raising to power $p$:
$$
|f(x) + g(x)|^p \leq (|f(x)| + |g(x)|)^p
$$

For $p \geq 1$, the function $t \mapsto t^p$ is convex on $[0, \infty)$, so:
$$
(|f| + |g|)^p \leq 2^{p-1}(|f|^p + |g|^p)
$$

(this is a standard inequality: $(a + b)^p \leq 2^{p-1}(a^p + b^p)$ for $a, b \geq 0$ and $p \geq 1$).

Integrating:
$$
\int |f + g|^p \, d\mu \leq 2^{p-1} \left(\int |f|^p \, d\mu + \int |g|^p \, d\mu\right) < \infty
$$

since $f, g \in L^p$. Thus $f + g \in L^p$. ✓

**Step 2: Establish the norm inequality (2.22).**

Write:
$$
\int |f + g|^p \, d\mu = \int |f + g| \cdot |f + g|^{p-1} \, d\mu
$$

By the triangle inequality for absolute values:
$$
|f + g| \leq |f| + |g|
$$

So:
$$
\begin{align}
\int |f + g|^p \, d\mu &= \int |f + g| \cdot |f + g|^{p-1} \, d\mu \\
&\leq \int (|f| + |g|) \cdot |f + g|^{p-1} \, d\mu \\
&= \int |f| \cdot |f + g|^{p-1} \, d\mu + \int |g| \cdot |f + g|^{p-1} \, d\mu \tag{2.23}
\end{align}
$$

**Step 3: Apply Hölder to each term in (2.23).**

For the first term, we use Hölder with:
- $h_1 = |f| \in L^p$
- $h_2 = |f + g|^{p-1}$

We need to verify $h_2 \in L^q$ where $q$ is conjugate to $p$: $1/p + 1/q = 1$.

**Check:** We have:
$$
\int |f + g|^{(p-1)q} \, d\mu = \int |f + g|^{(p-1)p/(p-1)} \, d\mu = \int |f + g|^p \, d\mu < \infty
$$

(using $q = p/(p-1)$, so $(p-1)q = p$). Thus $|f + g|^{p-1} \in L^q$. ✓

Applying Hölder:
$$
\int |f| \cdot |f + g|^{p-1} \, d\mu \leq \|f\|_p \||f + g|^{p-1}\|_q = \|f\|_p \left(\int |f + g|^p \, d\mu\right)^{1/q}
$$

Similarly, for the second term:
$$
\int |g| \cdot |f + g|^{p-1} \, d\mu \leq \|g\|_p \left(\int |f + g|^p \, d\mu\right)^{1/q}
$$

**Step 4: Combine and simplify.**

From (2.23):
$$
\int |f + g|^p \, d\mu \leq \left(\|f\|_p + \|g\|_p\right) \left(\int |f + g|^p \, d\mu\right)^{1/q}
$$

**Divide both sides by $\left(\int |f + g|^p \, d\mu\right)^{1/q}$:**

(Assuming $\int |f + g|^p \, d\mu > 0$; if it equals 0, then $f + g = 0$ a.e., and the inequality holds trivially.)

$$
\left(\int |f + g|^p \, d\mu\right)^{1 - 1/q} \leq \|f\|_p + \|g\|_p
$$

**Simplify the exponent:**

$$
1 - \frac{1}{q} = \frac{q - 1}{q} = \frac{p/(p-1) - 1}{p/(p-1)} = \frac{p - (p-1)}{p} = \frac{1}{p}
$$

(using $q = p/(p-1)$, so $q - 1 = p/(p-1) - 1 = (p - (p-1))/(p-1) = 1/(p-1)$, giving $(q-1)/q = (1/(p-1))/(p/(p-1)) = 1/p$).

Thus:
$$
\left(\int |f + g|^p \, d\mu\right)^{1/p} \leq \|f\|_p + \|g\|_p
$$

which is (2.22). □

---

**Proof (Case $p = 1$).**

For $p = 1$, Minkowski states:
$$
\int |f + g| \, d\mu \leq \int |f| \, d\mu + \int |g| \, d\mu
$$

This follows immediately from the triangle inequality for absolute values and linearity of the integral:
$$
\int |f + g| \, d\mu \leq \int (|f| + |g|) \, d\mu = \int |f| \, d\mu + \int |g| \, d\mu
$$

□

---

**Proof (Case $p = \infty$).**

For $p = \infty$, Minkowski states:
$$
\|f + g\|_\infty \leq \|f\|_\infty + \|g\|_\infty
$$

Since $|f(x)| \leq \|f\|_\infty$ $\mu$-a.e. and $|g(x)| \leq \|g\|_\infty$ $\mu$-a.e., we have:
$$
|f(x) + g(x)| \leq |f(x)| + |g(x)| \leq \|f\|_\infty + \|g\|_\infty \quad \mu\text{-a.e.}
$$

Taking the essential supremum of the left side:
$$
\|f + g\|_\infty = \text{ess sup}_{x} |f(x) + g(x)| \leq \|f\|_\infty + \|g\|_\infty
$$

□

---

**Remark 2.32 (Minkowski for $0 < p < 1$).** For $0 < p < 1$, the inequality **reverses**: $\|f + g\|_p \geq \|f\|_p + \|g\|_p$ (when $f, g$ have disjoint support). This is because $t \mapsto t^p$ is concave for $p < 1$, not convex. However, $L^p$ for $p < 1$ is **not a normed space**—$\|\cdot\|_p$ is a **quasi-norm** (satisfies a weaker triangle inequality with a constant factor). Such spaces arise in certain RL contexts (e.g., $\ell^{1/2}$ regularization in sparse coding), but we focus on $p \geq 1$ where $L^p$ is a genuine normed space.

**Remark 2.33 (Completeness: Riesz-Fischer Theorem).** We have now shown that $\|\cdot\|_p$ satisfies all three axioms of a norm:
1. **Positivity:** $\|f\|_p \geq 0$, with $\|f\|_p = 0$ iff $f = 0$ a.e.
2. **Homogeneity:** $\|\alpha f\|_p = |\alpha| \|f\|_p$ for scalars $\alpha$
3. **Triangle inequality:** $\|f + g\|_p \leq \|f\|_p + \|g\|_p$ (Minkowski)

Thus $L^p(\mu)$ is a **normed vector space**. Moreover, it is **complete** (every Cauchy sequence converges in $L^p$), making it a **Banach space**. This is the **Riesz-Fischer theorem** (Week 3, Day 1), which we will prove next week using the Dominated Convergence Theorem.

**Remark 2.34 (RL Application: Bellman Error Decomposition).** In function approximation, we often decompose value function errors using Minkowski:
$$
\|V_\theta - V^*\|_\infty \leq \|V_\theta - \Pi T^\pi V_\theta\|_\infty + \|\Pi T^\pi V_\theta - T^\pi V_\theta\|_\infty + \|T^\pi V_\theta - V^*\|_\infty
$$

where $\Pi$ is a projection operator (e.g., least-squares projection). Each term bounds a different source of error:
- Approximation error: $\|V_\theta - \Pi T^\pi V_\theta\|$
- Projection error: $\|\Pi T^\pi V_\theta - T^\pi V_\theta\|$
- Bellman error: $\|T^\pi V_\theta - V^*\|$

Minkowski allows us to bound the total error by summing these components (Week 35: TD with function approximation).

---

### **V. $L^p$ Spaces as Normed Vector Spaces: Summary**

**Theorem 2.9 ($L^p$ is a Normed Vector Space).** {#THM-2.4.8}
For $1 \leq p \leq \infty$, the space $L^p(\mu)$ equipped with the $L^p$ norm $\|\cdot\|_p$ is a **normed vector space**:
1. $(L^p, +, \cdot)$ is a vector space over $\mathbb{R}$ (or $\mathbb{C}$).
2. $\|\cdot\|_p$ is a norm satisfying:
   - **Positivity:** $\|f\|_p \geq 0$, with $\|f\|_p = 0$ iff $f = 0$ $\mu$-a.e.
   - **Homogeneity:** $\|\alpha f\|_p = |\alpha| \|f\|_p$ for all scalars $\alpha$
   - **Triangle inequality:** $\|f + g\|_p \leq \|f\|_p + \|g\|_p$ (Minkowski)

**Proof.** Vector space axioms (closure, associativity, distributivity, etc.) follow from pointwise operations on measurable functions. The norm axioms are:
- Positivity: Immediate from $\int |f|^p \geq 0$, with equality iff $|f| = 0$ a.e.
- Homogeneity: Remark 2.23 above
- Triangle inequality: Theorem 2.8 (Minkowski)

□

**Remark 2.35 (Quotient by Null Functions).** Technically, $L^p(\mu)$ as defined is the quotient space $\mathcal{L}^p / \sim$, where $\mathcal{L}^p$ is the set of measurable functions with $\int |f|^p < \infty$, and $f \sim g$ iff $f = g$ $\mu$-a.e. This ensures $\|f\|_p = 0$ implies $f = 0$ in $L^p$ (the zero equivalence class). We identify functions differing on measure-zero sets, treating them as the "same" element of $L^p$.

---

### **VI. Mathematical Insight and RL Connections**

**Mathematical Insight:**

The progression from integration to $L^p$ spaces reveals a fundamental principle: **measures induce norms on function spaces**. Given a measure $\mu$, we can define infinitely many norms $\|\cdot\|_p$ (one for each $p \in [1, \infty]$), each capturing a different notion of "size" for functions:
- $\|f\|_1 = \int |f|$ measures **total mass**
- $\|f\|_2 = \sqrt{\int |f|^2}$ measures **energy** (relevant in Hilbert spaces, Week 14)
- $\|f\|_\infty = \text{ess sup } |f|$ measures **peak magnitude**

The inequalities **Hölder** and **Minkowski** reveal the **geometric structure** of these spaces:
- Hölder: Products of $L^p$ and $L^q$ functions (conjugate exponents) are integrable—establishes duality
- Minkowski: $L^p$ is a normed space—enables functional analysis tools (convergence, compactness, etc.)

This mirrors finite-dimensional linear algebra:
- Cauchy-Schwarz: $|\langle u, v \rangle| \leq \|u\|_2 \|v\|_2$ (Hölder for $p = q = 2$)
- Triangle inequality: $\|u + v\| \leq \|u\| + \|v\|$ (Minkowski)

But $L^p$ is **infinite-dimensional**, requiring measure theory to make sense of "integration over uncountably many points."

**RL Connection:**

In reinforcement learning, value functions live in $L^p$ spaces when state spaces are continuous:
- **Tabular RL:** $V \in \mathbb{R}^{|\mathcal{S}|}$ (finite-dimensional)
- **Continuous RL:** $V \in L^\infty(\mathcal{S})$ or $L^2(\mathcal{S})$ (infinite-dimensional)

The choice of $p$ depends on the algorithm:
- **$L^\infty$ norm:** Bellman operators $T^\pi: L^\infty \to L^\infty$ are $\gamma$-contractions in $\|\cdot\|_\infty$ (Week 23). Value iteration converges in sup norm.
- **$L^2$ norm:** Least-squares TD minimizes $\|V_\theta - \Pi T^\pi V_\theta\|_2$ (Week 35). Projection operators are orthogonal in $L^2$.
- **$L^1$ norm:** Importance sampling requires $\|\rho\|_1 = \mathbb{E}[|\rho|] < \infty$ (Day 3, Section III.B).

**Why Hölder and Minkowski matter for RL:**
1. **Variance bounds:** Hölder bounds variance in importance sampling: $\text{Var}[\rho R] \leq \|\rho\|_2^2 \|R\|_2^2$
2. **Gradient bounds:** Policy gradients satisfy $\|\nabla J\| \leq \|\nabla \log \pi\|_2 \|A\|_2$ (Cauchy-Schwarz)
3. **Error decomposition:** Minkowski decomposes value function error: $\|V - V^*\| \leq \|V - \Pi T V\| + \|\Pi T V - T V\| + \|T V - V^*\|$
4. **Duality:** The dual space $(L^p)^* \cong L^q$ (Week 3) formalizes "linear value function approximation lives in $(L^2)^*$"

Without $L^p$ theory, these statements are heuristic. With it, they are **theorems**.

---

**Looking Ahead:**

- **Day 5 (Tomorrow, Friday):** Weekly synthesis! We'll code numerical experiments to:
  1. Verify Fubini numerically (compute $\iint f(x,y) \, dx \, dy$ via both orders)
  2. Visualize $L^p$ unit balls in $\mathbb{R}^2$ for $p = 1, 2, \infty$ (see the geometry of norms)
  3. Reflect: How does Fubini enable computing $\mathbb{E}_{s,a}[V^\pi(s')]$ in RL policy evaluation?

- **Week 3 (Next Week):** We prove **Riesz-Fischer** ($L^p$ is complete), **$L^p$ duality** ($(L^p)^* \cong L^q$), and the **Radon-Nikodym theorem** (formalizing densities $d\mu/d\nu$ for importance sampling).

- **Week 14:** Hilbert spaces ($L^2$ with inner product), orthogonal projection, and the Riesz representation theorem $H^* \cong H$ (foundation for least-squares RL).

Today's inequalities—Hölder and Minkowski—are the **geometric foundation** for all of functional analysis. Every convergence proof, approximation bound, and operator analysis in RL ultimately rests on these tools.

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_4_exercises_draft]]** (to be created)

**Anchor Exercises Preview:**
1. **Prove Hölder's inequality** for $p, q$ conjugate (as in Section III)
2. **Prove Minkowski's inequality** using Hölder (as in Section IV)
3. **Verify Young's inequality numerically** for various $(a, b)$ and conjugate pairs $(p, q)$
4. **RL Application (Importance Sampling Variance):** Show that for $\rho = \pi/\mu$ and reward $R$:
   $$
   \text{Var}_\mu[\rho R] \leq \mathbb{E}_\mu[\rho^2] \mathbb{E}_\mu[R^2]
   $$
   using Hölder with $p = q = 2$. Discuss why clipping $\rho$ reduces variance.

5. **Show $L^\infty \subseteq L^2 \subseteq L^1$ on $[0,1]$ with Lebesgue measure**, and construct counterexamples showing inclusions fail on $\mathbb{R}$.

---

**Reflection Questions:**

1. **Why do we need conjugate exponents?** Why does Hölder require $1/p + 1/q = 1$ rather than, say, $p + q = 1$ or $pq = 1$? What goes wrong if we use non-conjugate exponents?

   *Hint:* Try to prove Hölder with $p = 2, q = 3$ (so $1/p + 1/q = 1/2 + 1/3 = 5/6 \neq 1$). Where does the proof break down?

2. **Hölder vs. Cauchy-Schwarz:** The Cauchy-Schwarz inequality is typically written as $|\langle f, g \rangle| \leq \|f\|_2 \|g\|_2$ (using inner products). How does this relate to Hölder with $p = q = 2$? Why does $L^2$ have an inner product but $L^p$ (for $p \neq 2$) does not?

   *Hint:* Inner products $\langle f, g \rangle$ must satisfy the **polarization identity** $\langle f, g \rangle = \frac{1}{4}(\|f + g\|^2 - \|f - g\|^2)$. Check if this holds for $\|\cdot\|_p$ when $p \neq 2$.

3. **Bellman Contraction in $L^\infty$ vs. $L^2$:** In tabular RL, the Bellman operator $T^\pi V = R + \gamma P^\pi V$ is a contraction in $\|\cdot\|_\infty$ with modulus $\gamma$ (Week 23). Is it also a contraction in $\|\cdot\|_2$? If not, why does least-squares TD use the $L^2$ norm?

   *Hint:* Contraction in $\|\cdot\|_\infty$ does not imply contraction in $\|\cdot\|_2$ (norms are not equivalent in infinite dimensions). Least-squares TD minimizes projection error $\|V - \Pi T V\|_2$, not Bellman error $\|V - T V\|_2$.

---

**Daily Study Note:**

**What I learned today:**
- $L^p(\mu)$ spaces organize integrable functions into normed vector spaces via $\|f\|_p = (\int |f|^p)^{1/p}$
- **Young's inequality** ($ab \leq a^p/p + b^q/q$) is the pointwise foundation for Hölder
- **Hölder's inequality** ($\|fg\|_1 \leq \|f\|_p \|g\|_q$) generalizes Cauchy-Schwarz to $L^p$ spaces
- **Minkowski's inequality** ($\|f + g\|_p \leq \|f\|_p + \|g\|_p$) establishes the triangle inequality, making $L^p$ a normed space
- Conjugate exponents $1/p + 1/q = 1$ encode the duality between $L^p$ and $L^q$

**Connection to previous material:**
- Builds on integrability $\int |f| < \infty$ from Fubini (Day 3)
- Uses MCT implicitly in defining $\|f\|_p$ via approximation by simple functions
- Prepares for Riesz-Fischer (completeness of $L^p$, Week 3, Day 1)

**Looking forward:**
- Tomorrow: Friday coding synthesis—visualize $L^p$ unit balls, verify Fubini numerically
- Week 3: $L^p$ duality $(L^p)^* \cong L^q$, Radon-Nikodym theorem (importance sampling densities)
- Week 14: Hilbert spaces ($L^2$ with inner product), orthogonal projection

**RL connections identified:**
- Bellman operators act on $L^\infty$ (contraction mapping, value iteration)
- Least-squares TD minimizes error in $L^2$ norm
- Importance sampling variance bounded by Hölder: $\text{Var}[\rho R] \leq \|\rho\|_2^2 \|R\|_2^2$
- Policy gradient bounds: $\|\nabla J\| \leq \|\nabla \log \pi\|_2 \|A\|_2$

**Time spent:** 90 minutes (30 min reading Folland §6.1-6.2, 60 min proving Young → Hölder → Minkowski)

---

**End of Day 4**
