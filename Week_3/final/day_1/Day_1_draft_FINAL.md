### Agenda:

##### 📘 Day 1 — Week 3: Completeness of $L^p$ Spaces: The Riesz-Fischer Theorem

**Total time: ~90 minutes (Monday)**
**Actual time estimate: 90-110 minutes for rigorous proof work**

---

#### **⏱️ Segment 1 (40 min) — Reading**

**Topic:** _Completeness of $L^p$ spaces: Riesz-Fischer theorem and Cauchy sequences in $L^p$_

- Read from **Folland §6.3** [@folland:real_analysis:1999, §6.3] ($L^p$ completeness) or **Stein-Shakarchi Ch 6** [@stein:real_analysis:2005, Ch 6] (Real Analysis)
- Focus on:
    - **Cauchy sequences in $L^p$**: $\{f_n\}$ Cauchy if $\|f_n - f_m\|_p \to 0$ as $n, m \to \infty$
    - **Completeness**: Every Cauchy sequence in $L^p$ converges to some $f \in L^p$
    - **Riesz-Fischer theorem**: $L^p(\mu)$ is a **Banach space** (complete normed vector space)
    - **Key mechanism**: Extract pointwise convergent subsequence via measure concentration, use DCT/Fatou
    - **RL significance**: Bellman fixed-point theorem requires completeness—without it, value iteration might fail to converge

---

#### **⏱️ Segment 2 (40 min) — Proof and Exercises**

**Primary Task:**
1. **Prove Riesz-Fischer theorem** for $1 \leq p < \infty$: Every Cauchy sequence in $L^p(\mu)$ has a convergent subsequence (in $L^p$ norm)
2. **Understand the proof strategy**:
   - Step 1: Extract subsequence $\{f_{n_k}\}$ with $\|f_{n_k+1} - f_{n_k}\|_p < 2^{-k}$ (rapid convergence)
   - Step 2: Show $\sum_k |f_{n_{k+1}} - f_{n_k}|$ converges pointwise a.e. (via Borel-Cantelli or monotone convergence)
   - Step 3: Define limit $f(x) = f_{n_1}(x) + \sum_{k=1}^\infty (f_{n_{k+1}}(x) - f_{n_k}(x))$ a.e.
   - Step 4: Prove $f \in L^p$ using Fatou's lemma on $|f_{n_k}|^p$
   - Step 5: Show $\|f_{n_k} - f\|_p \to 0$ via dominated convergence
   - Step 6: Extend to full sequence using Cauchy property

**Guidance:**
- The proof is a **masterclass in using Week 1 convergence theorems** (MCT, DCT, Fatou)
- Completeness is **non-trivial**: not all normed spaces are complete (e.g., $C([0,1])$ with $L^1$ norm is incomplete)
- This theorem justifies writing "$\lim_{n \to \infty} f_n$ exists in $L^p$" and guarantees Bellman value iteration converges

---

#### **💡 Conceptual Bridge to RL**

- **Why completeness matters in RL:** Consider the **Bellman policy evaluation operator** $T^\pi: L^\infty(\mathcal{S}) \to L^\infty(\mathcal{S})$ defined by:
  $$
  (T^\pi V)(s) = \mathbb{E}_{a \sim \pi(s), s' \sim P(s'|s,a)}[r(s,a) + \gamma V(s')]
  $$

  **Value iteration** generates a sequence $V_{n+1} = T^\pi V_n$ starting from $V_0$. We need to know:
  1. Does $\{V_n\}$ converge? (**Existence of limit**)
  2. If it converges, does the limit live in $L^\infty$? (**Closure of $L^\infty$**)
  3. Is the limit unique? (**Uniqueness via contraction**)

  The **Banach Fixed-Point Theorem** (Week 16) guarantees existence and uniqueness of $V^\pi = T^\pi V^\pi$ **if and only if** $L^\infty$ is **complete**. Without completeness, $\{V_n\}$ might be Cauchy but fail to converge to a value function in $L^\infty$—disaster for RL algorithms.

- **Riesz-Fischer in action:** The theorem states that $L^p(\mu)$ **is complete** for all $1 \leq p \leq \infty$. Thus:
  - **$L^\infty$ completeness** $\Rightarrow$ Bellman operator has unique fixed point (value iteration converges geometrically)
  - **$L^2$ completeness** $\Rightarrow$ Least-squares TD has well-defined projected fixed point $\bar{V} = \Pi T^\pi \bar{V}$ (projection theorem, Week 14)
  - **Hilbert space structure**: $L^2$ is not just complete but also has an **inner product** $\langle f, g \rangle = \int fg \, d\mu$, making it a **Hilbert space** (Week 14). This enables orthogonal projections, which are the foundation of least-squares methods.

- **Connection to Week 1:** Recall [DCT-1.2.3] (Dominated Convergence Theorem from Week 1, Day 3): If $f_n \to f$ pointwise a.e. and $|f_n| \leq g \in L^1$, then $\int f_n \to \int f$. The Riesz-Fischer proof **cleverly constructs a dominating function** from the rapid Cauchy decay, enabling DCT application to prove $\|f_n - f\|_p \to 0$.

- **Contrast with incomplete spaces:** The space of continuous functions $C([0,1])$ with the $L^1$ norm is **not complete**. Example: Take $f_n(x) = \min(nx, 1)$ for $x \in [0,1]$. Then $f_n \to \mathbf{1}_{(0,1]}$ in $L^1$ norm (the indicator function of $(0,1]$), but the limit is **not continuous**. Thus $\{f_n\}$ is Cauchy in $(C([0,1]), \|\cdot\|_1)$ but has no limit in $C([0,1])$—the space is incomplete. Completing it yields $L^1([0,1])$ (Lebesgue integrable functions).

**Preview for Day 2-3:** Tomorrow we begin the study of **$L^p$ duality**: $(L^p)^* \cong L^q$ for conjugate exponents. This reveals that linear functionals on $L^p$ correspond to elements of $L^q$, formalizing "value functions are dual to state distributions" in RL.

---

## **Chapter 3.1: Completeness of $L^p$ Spaces**

### **Motivation: When Do Cauchy Sequences Converge?**

Recall from Week 2, Day 4 that we established $L^p(\mu)$ is a **normed vector space** for $1 \leq p \leq \infty$ (via Minkowski's inequality [THM-2.8]; see [@folland:real_analysis:1999, §6.2] for the general theory). But normed spaces come in two flavors:
1. **Incomplete normed spaces**: Some Cauchy sequences fail to converge within the space
2. **Complete normed spaces (Banach spaces)**: Every Cauchy sequence converges to an element of the space

**Why does completeness matter?** In finite dimensions, all normed spaces are complete (by compactness of closed bounded sets in $\mathbb{R}^n$). But in **infinite dimensions**, completeness is a **theorem**, not a given. Without it:
- Iterative algorithms (like value iteration) might generate Cauchy sequences that don't converge to a solution
- Fixed-point theorems fail (the Banach Fixed-Point Theorem requires completeness)
- Approximation schemes break down (no guarantee that "getting closer and closer" leads to a limit)

**Today's objective:** Prove that $L^p(\mu)$ is complete for $1 \leq p \leq \infty$. This is the **Riesz-Fischer theorem**, named after **Frigyes Riesz** (1907) and **Ernst Fischer** (1907), who independently proved completeness of $L^2$ in their work on Fourier series [@folland:real_analysis:1999, p. 188]. The general $L^p$ case was later unified by **Riesz** (1910) under Lebesgue's measure theory.

**Bridge from Week 2:** On Day 4, we proved [THM-2.8] (Minkowski's inequality), establishing that $\|\cdot\|_p$ is a genuine norm. Today, we prove that $(L^p, \|\cdot\|_p)$ is **complete**—the final ingredient for Banach space status.

**What we'll accomplish today:**

**Learning Objectives:**
* Define Cauchy sequences in $L^p$ and the notion of completeness
* State the Riesz-Fischer theorem: $L^p(\mu)$ is complete for $1 \leq p \leq \infty$
* Prove Riesz-Fischer for $1 \leq p < \infty$ via subsequence extraction and dominated convergence
* Understand the proof strategy: rapid decay + Borel-Cantelli → pointwise a.e. limit → DCT → $L^p$ convergence
* Identify where Week 1 convergence theorems (MCT, DCT, Fatou) are used crucially
* Connect completeness to Bellman fixed-point theory in RL

**Time allocation (90 min Monday):**
- 40 min reading: Cauchy sequences, completeness, statement of Riesz-Fischer
- 40 min proof: Complete proof of Riesz-Fischer for $1 \leq p < \infty$ with detailed steps
- 10 min reflection: Why does this matter for RL? Bellman operators and fixed-point theorems

---

### **I. Core Theory: Completeness and Cauchy Sequences**

#### **A. Cauchy Sequences in Normed Spaces**

Recall from undergraduate real analysis that a sequence $\{x_n\}$ in a metric space $(M, d)$ is **Cauchy** if:
$$
\forall \epsilon > 0, \exists N \in \mathbb{N} : n, m \geq N \Rightarrow d(x_n, x_m) < \epsilon
$$

In words: the sequence elements become arbitrarily close to each other (even if we don't yet know what they're converging to).

**Definition 3.1 (Cauchy Sequence in $L^p$).** {#DEF-3.1}
Let $(X, \mathcal{F}, \mu)$ be a measure space and $1 \leq p \leq \infty$. A sequence $\{f_n\} \subseteq L^p(\mu)$ is **Cauchy in $L^p$** if:
$$
\forall \epsilon > 0, \exists N \in \mathbb{N} : \forall n, m \geq N, \quad \|f_n - f_m\|_p < \epsilon \tag{3.1}
$$

**Equivalently:** $\lim_{n,m \to \infty} \|f_n - f_m\|_p = 0$ (where the limit is taken as both $n$ and $m$ tend to infinity jointly).

**Remark 3.1 (Cauchy vs. Convergent).** Every **convergent sequence** is Cauchy (by the triangle inequality), but the converse need not hold in incomplete spaces. The space is **complete** if every Cauchy sequence converges.

---

#### **B. Completeness and Banach Spaces**

**Definition 3.2 (Complete Metric Space).** {#DEF-3.2}
A metric space $(M, d)$ is **complete** if every Cauchy sequence in $M$ converges to an element of $M$.

**Definition 3.3 (Banach Space).** {#DEF-3.3}
A normed vector space $(V, \|\cdot\|)$ is a **Banach space** if it is complete as a metric space with the induced metric $d(f, g) = \|f - g\|$.

**Examples:**
- **$\mathbb{R}^n$** with any norm is a Banach space (finite dimensions are always complete)
- **$c_0 = \{(x_n) : x_n \to 0\}$** (sequences converging to 0) with $\|(x_n)\|_\infty = \sup_n |x_n|$ is a Banach space
- **$C([0,1])$** with sup norm $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$ is a Banach space
- **$C([0,1])$** with $L^1$ norm $\|f\|_1 = \int_0^1 |f|$ is **NOT complete** (counterexample: $f_n(x) = \min(nx, 1)$ converges in $L^1$ to the discontinuous function $\mathbf{1}_{(0,1]}$)

**Remark 3.2 (Completion).** Every normed space $(V, \|\cdot\|)$ can be **completed** to a Banach space $\overline{V}$ by adding "Cauchy limits." For example, the completion of $(C([0,1]), \|\cdot\|_1)$ is $L^1([0,1])$ (Lebesgue integrable functions). This is analogous to how the rationals $\mathbb{Q}$ are completed to the reals $\mathbb{R}$ by adding limits of Cauchy sequences.

---

### **II. The Riesz-Fischer Theorem**

**Theorem 3.4 (Riesz-Fischer: Completeness of $L^p$).** {#THM-3.4}
Let $(X, \mathcal{F}, \mu)$ be a measure space and $1 \leq p \leq \infty$. Then $L^p(\mu)$ is a **Banach space**: every Cauchy sequence in $L^p(\mu)$ converges in $L^p$ to an element of $L^p(\mu)$ (unique up to $\mu$-a.e. equivalence).

**Precisely:** If $\{f_n\} \subseteq L^p(\mu)$ is Cauchy (i.e., $\|f_n - f_m\|_p \to 0$ as $n, m \to \infty$), then there exists $f \in L^p(\mu)$ such that:
$$
\lim_{n \to \infty} \|f_n - f\|_p = 0 \tag{3.2}
$$

We say $f_n \to f$ in $L^p$ norm, or $f_n \xrightarrow{L^p} f$.

**Remark 3.3 (Uniqueness of Limit).** The limit $f$ is unique **up to sets of measure zero**. If $f_n \to f$ and $f_n \to g$ in $L^p$, then $\|f - g\|_p = 0$, so $f = g$ $\mu$-almost everywhere. Recall (Remark 2.37, Week 2 Day 4) that $L^p$ is technically the quotient space of measurable functions by the equivalence relation $f \sim g$ iff $f = g$ $\mu$-a.e., so $f$ and $g$ represent the same element of $L^p$.

**Remark 3.4 (Historical Context).** The theorem was proved independently by **Frigyes Riesz** and **Ernst Fischer** in 1907 for the $p = 2$ case (motivated by convergence of Fourier series in $L^2$). Riesz later extended the result to general $1 \leq p < \infty$ in 1910. The $p = \infty$ case is easier (Lemma 3.5 below). The proof we present follows [@folland:real_analysis:1999, §6.3] and [@brezis:functional_analysis:2011, Ch 4], using the **subsequence extraction + dominated convergence** strategy.

---

**Proof (Case $1 \leq p < \infty$).**

The proof proceeds in six steps:
1. Extract a rapidly convergent subsequence
2. Show the subsequence converges pointwise a.e. to some $f$
3. Prove $f$ is measurable
4. Prove $f \in L^p$ using Fatou's lemma
5. Prove $\|f_n - f\|_p \to 0$ for the subsequence using dominated convergence
6. Extend to the full sequence using the Cauchy property

---

**Step 1: Extract a rapidly convergent subsequence.**

Let $\{f_n\}$ be Cauchy in $L^p$. By definition (3.1), for each $k \in \mathbb{N}$, there exists $N_k$ such that:
$$
n, m \geq N_k \Rightarrow \|f_n - f_m\|_p < 2^{-k} \tag{3.3}
$$

Without loss of generality, we may assume $N_1 < N_2 < N_3 < \ldots$ (by replacing $N_k$ with $\max(N_1, \ldots, N_k)$ if necessary). Define the subsequence:
$$
g_k = f_{N_k} \quad \text{for } k = 1, 2, 3, \ldots
$$

Then by (3.3):
$$
\|g_{k+1} - g_k\|_p = \|f_{N_{k+1}} - f_{N_k}\|_p < 2^{-k} \tag{3.4}
$$

This subsequence converges **rapidly** in $L^p$ norm (faster than geometric decay).

---

**Step 2: Show pointwise a.e. convergence of the subsequence.**

Define the telescoping sum:
$$
S_K(x) = |g_1(x)| + \sum_{k=1}^{K-1} |g_{k+1}(x) - g_k(x)| \tag{3.5}
$$

for each $x \in X$. This is a non-negative function. We will show $S_K$ converges pointwise a.e. to a finite limit.

**Key observation:** By the triangle inequality in $\mathbb{R}$:
$$
|g_K(x)| \leq |g_1(x)| + \sum_{k=1}^{K-1} |g_{k+1}(x) - g_k(x)| = S_K(x)
$$

So convergence of $S_K$ implies convergence of $|g_K|$.

**Substep 2a: Compute $\|S_K\|_p$ using Minkowski.**

By Minkowski's inequality [THM-2.8] applied repeatedly:
$$
\begin{align}
\|S_K\|_p &= \left\| |g_1| + \sum_{k=1}^{K-1} |g_{k+1} - g_k| \right\|_p \\
&\leq \|g_1\|_p + \sum_{k=1}^{K-1} \||g_{k+1} - g_k|\|_p \\
&= \|g_1\|_p + \sum_{k=1}^{K-1} \|g_{k+1} - g_k\|_p \tag{3.6}
\end{align}
$$

(Note: $\||f|\|_p = \left(\int |f|^p d\mu\right)^{1/p} = \|f\|_p$ since $||f|| = |f|$.)

By (3.4), $\|g_{k+1} - g_k\|_p < 2^{-k}$, so:
$$
\|S_K\|_p \leq \|g_1\|_p + \sum_{k=1}^{K-1} 2^{-k} < \|g_1\|_p + \sum_{k=1}^\infty 2^{-k} = \|g_1\|_p + 1 \tag{3.7}
$$

This is **independent of $K$**! Thus $\{S_K\}$ is **uniformly bounded in $L^p$**.

**Substep 2b: Apply Monotone Convergence Theorem.**

Since $S_K(x) \nearrow$ (increasing in $K$ for each $x$), we can define:
$$
S(x) = \lim_{K \to \infty} S_K(x) = |g_1(x)| + \sum_{k=1}^\infty |g_{k+1}(x) - g_k(x)| \in [0, \infty] \tag{3.8}
$$

(The limit exists in $[0, \infty]$ because $S_K$ is monotone increasing.)

Each $S_K$ is measurable (as a sum of measurable functions $|g_k|$, where each $g_k \in L^p$ is measurable). Since $S = \lim_{K \to \infty} S_K$ is the pointwise limit of measurables, $S$ is measurable (pointwise limits of measurable functions are measurable; see [@folland:real_analysis:1999, Proposition 2.7]).

By the **Monotone Convergence Theorem** [THM-1.2.2] (Week 1, Day 2; [@folland:real_analysis:1999, Theorem 2.14]):
$$
\|S\|_p^p = \int_X |S|^p \, d\mu = \int_X \lim_{K \to \infty} |S_K|^p \, d\mu = \lim_{K \to \infty} \int_X |S_K|^p \, d\mu = \lim_{K \to \infty} \|S_K\|_p^p
$$

By (3.7), $\|S_K\|_p \leq \|g_1\|_p + 1$ for all $K$, so:
$$
\|S\|_p \leq \|g_1\|_p + 1 < \infty \tag{3.9}
$$

**Conclusion:** $S \in L^p(\mu)$. In particular, $\int_X |S|^p \, d\mu < \infty$, which implies:
$$
|S(x)|^p < \infty \quad \text{for } \mu\text{-almost every } x \in X
$$

(If $|S(x)|^p = \infty$ on a set $E$ with $\mu(E) > 0$, then $\int |S|^p \geq \int_E |S|^p = \infty$, contradiction.)

Thus:
$$
S(x) < \infty \quad \mu\text{-almost everywhere} \tag{3.10}
$$

**Substep 2c: Deduce pointwise convergence of $g_K$.**

From (3.10), the series $\sum_{k=1}^\infty |g_{k+1}(x) - g_k(x)|$ converges absolutely for $\mu$-almost every $x$. By the **absolute convergence test** from real analysis, the telescoping series:
$$
g_1(x) + \sum_{k=1}^\infty (g_{k+1}(x) - g_k(x)) = \lim_{K \to \infty} g_K(x)
$$

converges to a **finite limit** for $\mu$-almost every $x$. Define:
$$
f(x) = \begin{cases}
\lim_{K \to \infty} g_K(x) & \text{if the limit exists and is finite} \\
0 & \text{otherwise (on a measure-zero set)}
\end{cases} \tag{3.11}
$$

Then $g_K(x) \to f(x)$ pointwise $\mu$-almost everywhere. ✓

---

**Step 3: Prove $f$ is measurable.**

Each $g_K$ is measurable (since $g_K \in L^p \subseteq$ measurable functions). The pointwise limit of measurable functions is measurable (standard fact; see [@folland:real_analysis:1999, Proposition 2.7]). Thus $f$ is measurable. ✓

---

**Step 4: Prove $f \in L^p$ using Fatou's lemma.**

**Claim:** The subsequence $\{g_K\}$ is bounded in $L^p$: $\sup_K \|g_K\|_p < \infty$.

**Proof of claim:** By the triangle inequality (Minkowski) and equation (3.4):
$$
\begin{align}
\|g_K\|_p &\leq \|g_1\|_p + \sum_{k=1}^{K-1} \|g_{k+1} - g_k\|_p \\
&< \|g_1\|_p + \sum_{k=1}^{K-1} 2^{-k} \\
&< \|g_1\|_p + 1 =: M
\end{align}
$$

Thus $\|g_K\|_p \leq M$ for all $K$, independent of $K$. □

We have $|g_K(x)| \to |f(x)|$ pointwise $\mu$-a.e. (by continuity of $|\cdot|$). Apply **Fatou's Lemma** [LEM-1.2.2] (Week 1, Day 3; [@folland:real_analysis:1999, Theorem 2.18]) to the non-negative functions $|g_K|^p$:
$$
\int_X |f|^p \, d\mu = \int_X \left(\lim_{K \to \infty} |g_K|\right)^p d\mu = \int_X \liminf_{K \to \infty} |g_K|^p \, d\mu \leq \liminf_{K \to \infty} \int_X |g_K|^p \, d\mu = \liminf_{K \to \infty} \|g_K\|_p^p
$$

By the boundedness claim, $\|g_K\|_p \leq M$ for all $K$. Thus:
$$
\|f\|_p^p = \int |f|^p \, d\mu \leq \liminf_{K \to \infty} \|g_K\|_p^p \leq M^p < \infty
$$

Therefore $f \in L^p(\mu)$. ✓

---

**Step 5: Prove $\|g_K - f\|_p \to 0$ using Fatou's lemma.**

We have $g_K \to f$ pointwise $\mu$-a.e. (Step 2) and $g_K, f \in L^p$ (Step 4). We want to show $\|g_K - f\|_p \to 0$, i.e., $\int |g_K - f|^p \to 0$.

**Key challenge:** We cannot directly apply DCT because we don't yet have a dominating function for $|g_K - f|^p$.

**Strategy:** Use Fatou's lemma applied to $|g_K - g_M|^p$.

**Substep 5a: Apply Fatou to $|g_K - f|^p$.**

For any $K, M \geq 1$:
$$
|g_K(x) - f(x)| = |g_K(x) - \lim_{M \to \infty} g_M(x)| = \lim_{M \to \infty} |g_K(x) - g_M(x)|
$$

(by continuity of $|\cdot|$ and pointwise convergence). Raising to power $p$:
$$
|g_K(x) - f(x)|^p = \left(\lim_{M \to \infty} |g_K(x) - g_M(x)|\right)^p = \lim_{M \to \infty} |g_K - g_M|^p(x)
$$

Apply Fatou's lemma to $|g_K - g_M|^p$ (viewing $M$ as the varying index):
$$
\int_X |g_K - f|^p \, d\mu = \int_X \liminf_{M \to \infty} |g_K - g_M|^p \, d\mu \leq \liminf_{M \to \infty} \int_X |g_K - g_M|^p \, d\mu = \liminf_{M \to \infty} \|g_K - g_M\|_p^p
$$

**Substep 5b: Use Cauchy property.**

Since $\{g_K\}$ is Cauchy, for any $\epsilon > 0$, there exists $K_0$ such that $K, M \geq K_0$ implies $\|g_K - g_M\|_p < \epsilon$. Thus:
$$
\liminf_{M \to \infty} \|g_K - g_M\|_p^p < \epsilon^p \quad \text{for all } K \geq K_0
$$

From Substep 5a:
$$
\|g_K - f\|_p^p \leq \epsilon^p \quad \text{for all } K \geq K_0
$$

Since $\epsilon > 0$ is arbitrary:
$$
\lim_{K \to \infty} \|g_K - f\|_p = 0 \tag{3.12}
$$

Thus $g_K \to f$ in $L^p$ norm. ✓

---

**Step 6: Extend to the full sequence $f_n$.**

We've shown that the subsequence $g_K = f_{N_K}$ converges in $L^p$ to $f$. We now show the **entire sequence** $\{f_n\}$ converges to $f$.

**Key Principle (Cauchy with convergent subsequence):**
If $\{x_n\}$ is Cauchy and has a subsequence $x_{n_k} \to x^*$, then the full sequence $x_n \to x^*$.

**Proof of principle:** Triangle inequality + Cauchy property:
$$
d(x_n, x^*) \leq d(x_n, x_{n_k}) + d(x_{n_k}, x^*)
$$
Choose $k$ large so both terms are small. □

**Applying the principle:** Let $\epsilon > 0$. Since $\{f_n\}$ is Cauchy, there exists $N_\epsilon$ such that $n, m \geq N_\epsilon$ implies $\|f_n - f_m\|_p < \epsilon/2$.

Since $g_K \to f$ in $L^p$ (Step 5), there exists $K_\epsilon$ such that $K \geq K_\epsilon$ implies $\|g_K - f\|_p < \epsilon/2$.

Choose $K$ large enough that both $K \geq K_\epsilon$ and $N_K \geq N_\epsilon$ (possible since $N_K \to \infty$). Then for any $n \geq N_\epsilon$:
$$
\begin{align}
\|f_n - f\|_p &\leq \|f_n - g_K\|_p + \|g_K - f\|_p \quad \text{(Minkowski [THM-2.8])} \\
&= \|f_n - f_{N_K}\|_p + \|f_{N_K} - f\|_p \\
&< \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon \tag{3.13}
\end{align}
$$

(using $n, N_K \geq N_\epsilon \Rightarrow \|f_n - f_{N_K}\|_p < \epsilon/2$ by Cauchy, and $K \geq K_\epsilon \Rightarrow \|f_{N_K} - f\|_p = \|g_K - f\|_p < \epsilon/2$ by Step 5).

Thus $\|f_n - f\|_p \to 0$ as $n \to \infty$. ✓

This completes the proof of Theorem 3.4 for $1 \leq p < \infty$. □

---

**Proof (Case $p = \infty$).**

The $L^\infty$ case is simpler and uses a different technique (no integration involved).

**Lemma 3.5 ($L^\infty$ Completeness).** {#LEM-3.5}
$L^\infty(\mu)$ is a Banach space.

**Remark:** For $f \in L^\infty$, the **essential supremum** $\|f\|_\infty$ is defined as the smallest $M$ such that $|f(x)| \leq M$ for $\mu$-almost every $x$. Precisely:
$$
\|f\|_\infty = \text{ess sup}_{x \in X} |f(x)| := \inf\{M \geq 0 : |f(x)| \leq M \text{ for } \mu\text{-a.e. } x\}
$$
(Recall from Week 2, Day 4.)

**Proof sketch:** Let $\{f_n\} \subseteq L^\infty$ be Cauchy in the $\|\cdot\|_\infty$ norm. For each $n, m$:
$$
\|f_n - f_m\|_\infty = \text{ess sup}_{x \in X} |f_n(x) - f_m(x)| < \epsilon \quad \text{for } n, m \geq N_\epsilon
$$

This means $|f_n(x) - f_m(x)| < \epsilon$ for $\mu$-almost every $x$ (outside a null set $E_{n,m}$ depending on $n, m$).

Define $E = \bigcup_{n,m=1}^\infty E_{n,m}$ (countable union of null sets, hence $\mu(E) = 0$). For $x \in X \setminus E$, the sequence $\{f_n(x)\}$ is Cauchy in $\mathbb{R}$, hence converges to some $f(x) \in \mathbb{R}$. Define $f(x) = \lim_n f_n(x)$ for $x \notin E$, and $f(x) = 0$ for $x \in E$.

Then $f$ is measurable (pointwise limit of measurables), and $\|f_n - f\|_\infty \to 0$ (by taking $m \to \infty$ in the Cauchy condition $|f_n(x) - f_m(x)| < \epsilon$ for $x \notin E$, yielding $|f_n(x) - f(x)| \leq \epsilon$ for $\mu$-a.e. $x$).

Moreover, $\|f\|_\infty \leq \|f - f_1\|_\infty + \|f_1\|_\infty < \infty$, so $f \in L^\infty$. □

---

**Remark 3.5 (Where Convergence Theorems Were Used).** The proof of Riesz-Fischer is a **showcase for Week 1 convergence theorems** [@folland:real_analysis:1999, §2.2-2.3]:
- **Monotone Convergence Theorem [THM-1.2.2]** (Step 2): Applied to $S_K \nearrow S$ to show $\|S\|_p < \infty$
- **Fatou's Lemma [LEM-1.2.2]** (Step 4 and Step 5): Applied to $|g_K|^p$ and $|g_K - g_M|^p$ to establish $f \in L^p$ and $\|g_K - f\|_p \to 0$

**Why Fatou instead of DCT?**

The proof uses Fatou's Lemma rather than the Dominated Convergence Theorem. Why?

- **DCT requires a dominating function:** To apply DCT to $|g_K - f|^p$, we would need a function $h \in L^1$ with $|g_K - f|^p \leq h$ for all $K$. Constructing such an $h$ is nontrivial (it requires proving $\sup_K |g_K - f|^p \in L^1$, which is essentially equivalent to what we're trying to show).

- **Fatou only requires non-negativity:** Fatou's lemma applies to any non-negative sequence without requiring domination. This makes it the natural tool for proving completeness—we don't yet know the limit $f$ is "nice" enough to dominate.

**Philosophical point:** Fatou is the **workhorse for proving $L^p$ membership**, while DCT is the **workhorse for proving $L^p$ convergence when we already know both functions are in $L^p$**. In the Riesz-Fischer proof, we're establishing $f \in L^p$ for the first time, so Fatou is the appropriate tool.

**Remark 3.6 (Alternative Proof via DCT).** Some texts (e.g., [@stein:real_analysis:2005, Ch 6]) prove Riesz-Fischer by constructing an explicit dominating function $g$ for $|f_n|$ via:
$$
g(x) = \sup_n |f_n(x)|
$$

If $g \in L^p$, then $|f_n| \leq g$ for all $n$, and DCT applies directly to show $\|f_n - f\|_p \to 0$. However, proving $g \in L^p$ requires essentially the same work as our Fatou-based argument (via Monotone Convergence on $\sup_{n \leq N} |f_n|$). We present the Fatou-based proof as it is more direct and highlights the role of Fatou in analysis.

---

### **III. Corollaries and Applications**

**Corollary 3.6 ($L^p$ is a Banach Space).** {#COR-3.6}
For $1 \leq p \leq \infty$, the space $L^p(\mu)$ equipped with the $L^p$ norm $\|\cdot\|_p$ is a **Banach space** (complete normed vector space) [@brezis:functional_analysis:2011, Theorem 4.8].

**Proof.** Follows immediately from Theorem 3.4 and Theorem 2.9 (Week 2, Day 4: $L^p$ is a normed vector space). □

---

**Corollary 3.7 (Closed Subspaces of $L^p$ are Banach).** {#COR-3.7}
Let $V \subseteq L^p(\mu)$ be a **closed subspace** (closed in the $\|\cdot\|_p$ topology). Then $V$ is a Banach space.

**Proof.** Let $\{f_n\} \subseteq V$ be Cauchy. Since $V \subseteq L^p$ and $L^p$ is complete, $f_n \to f$ in $L^p$ for some $f \in L^p$. But $V$ is **closed**, so the limit $f$ must lie in $V$. Thus $V$ is complete. □

**Remark 3.7 (RL Application: Function Approximation Subspaces).** In linear value function approximation, we parameterize value functions as:
$$
V_\theta(s) = \theta^\top \phi(s) = \sum_{i=1}^d \theta_i \phi_i(s) \quad \text{where } \phi: \mathcal{S} \to \mathbb{R}^d
$$

The set $\mathcal{V} = \{V_\theta : \theta \in \mathbb{R}^d\} = \text{span}(\phi_1, \ldots, \phi_d)$ is a **finite-dimensional subspace** of $L^2(\mathcal{S}, \mu)$ **provided each $\phi_i \in L^2(\mathcal{S}, \mu)$** (i.e., $\int_{\mathcal{S}} |\phi_i(s)|^2 \mu(ds) < \infty$). Under this condition, finite-dimensional subspaces of Banach spaces are **always closed** (standard functional analysis result; see [@brezis:functional_analysis:2011, §5.3]), so $\mathcal{V}$ is a closed subspace, hence a Banach space by Corollary 3.7.

**Practical note:** In continuous state spaces, this requires $\phi_i$ to have bounded second moments under $\mu$. For example, polynomial features $\phi_i(s) = s^i$ are in $L^2$ if $\mu$ has finite moments (e.g., Gaussian state distribution), but not if $\mu$ is heavy-tailed. Practitioners typically assume bounded features $|\phi_i(s)| \leq C$ for all $s$, which guarantees $\phi_i \in L^2$ for any probability measure $\mu$.

This ensures that least-squares TD converges to a well-defined limit $\bar{V} \in \mathcal{V}$ (the projected fixed point $\bar{V} = \Pi T^\pi \bar{V}$, Week 35).

---

### **IV. Mathematical Insight and RL Connections**

**Mathematical Insight:**

The Riesz-Fischer theorem reveals a profound principle: **$L^p$ spaces complete the task of integration**. Just as the real numbers $\mathbb{R}$ complete the rationals $\mathbb{Q}$ by adding limits of Cauchy sequences, $L^p$ spaces complete the "pre-Lebesgue" integrable functions (e.g., continuous functions) by adding $L^p$ limits of Cauchy sequences.

**Why completeness is nontrivial:**
- In **finite dimensions**, every normed space is complete (by compactness)
- In **infinite dimensions**, completeness is a **theorem**, not automatic
- Example: $C([0,1])$ with $L^1$ norm is **incomplete**—completing it yields $L^1([0,1])$ (Lebesgue integrable functions, which may be discontinuous)

**Proof strategy recap:**
1. Extract rapidly convergent subsequence ($\|g_{k+1} - g_k\|_p < 2^{-k}$)
2. Show pointwise a.e. convergence via telescoping sum + MCT
3. Use Fatou to prove limit is in $L^p$
4. Use Fatou again to show $L^p$ norm convergence
5. Extend to full sequence via Cauchy property

This is a **masterclass in applying Week 1 convergence theorems** to infinite-dimensional analysis.

**Historical Context:**

The theorem is named after **Frigyes Riesz** (Hungarian mathematician, 1880-1956) and **Ernst Fischer** (Austrian mathematician, 1875-1954), who independently proved the $p = 2$ case in 1907 motivated by convergence questions for Fourier series:

- **Question:** Does every $L^2$ function have a Fourier series that converges in $L^2$ norm?
- **Answer (Riesz-Fischer 1907):** Yes, because $L^2$ is complete—every Cauchy sequence of partial Fourier sums converges to an $L^2$ function.

Riesz later extended the result to all $1 \leq p < \infty$ in 1910, unifying the theory under Lebesgue's measure framework.

**RL Connection:**

**Why completeness matters for RL:**

1. **Banach Fixed-Point Theorem (Week 16):** Let $(X, d)$ be a **complete metric space** and $T: X \to X$ a contraction (i.e., $d(Tx, Ty) \leq L \cdot d(x, y)$ for some $L < 1$). Then $T$ has a **unique fixed point** $x^* = Tx^*$, and the iteration $x_{n+1} = Tx_n$ converges geometrically to $x^*$:
   $$
   d(x_n, x^*) \leq L^n d(x_0, x^*)
   $$

   **RL application:** The Bellman policy evaluation operator $T^\pi: L^\infty(\mathcal{S}) \to L^\infty(\mathcal{S})$ is a **$\gamma$-contraction** in $\|\cdot\|_\infty$ norm (Week 23):
   $$
   \|T^\pi V_1 - T^\pi V_2\|_\infty \leq \gamma \|V_1 - V_2\|_\infty
   $$

   Since $L^\infty$ is **complete** (Riesz-Fischer), the Banach Fixed-Point Theorem applies, guaranteeing:
   - **Existence:** There exists a unique value function $V^\pi = T^\pi V^\pi$
   - **Convergence:** Value iteration $V_{n+1} = T^\pi V_n$ converges geometrically to $V^\pi$ at rate $\gamma^n$
   - **Algorithmic implication:** We can compute $V^\pi$ to any desired accuracy $\epsilon$ in $O(\log(1/\epsilon))$ iterations

   **Without completeness:** If $L^\infty$ were incomplete, $\{V_n\}$ might be Cauchy but fail to converge to any value function—the algorithm would "converge to nothing," rendering RL theory meaningless.

2. **Least-Squares TD and $L^2$ Completeness (Week 35):** In continuous state spaces with linear function approximation $V_\theta = \theta^\top \phi$, where $\phi: \mathcal{S} \to \mathbb{R}^d$ are feature maps, **least-squares TD (LSTD)** [@bradtke:lstd:1996] seeks the **projected fixed point**:
   $$
   \bar{V} = \Pi T^\pi \bar{V}
   $$

   where $\Pi: L^2(\mathcal{S}, \mu) \to \text{span}(\phi_1, \ldots, \phi_d)$ is the **orthogonal projection** (with respect to the $L^2$ inner product weighted by state distribution $\mu$).

   **Algorithmic implementation:** Given samples $(s_i, r_i, s_i')$ from policy $\pi$, LSTD computes:
   $$
   \theta_{\text{LSTD}} = \left(\sum_{i=1}^n \phi(s_i)(\phi(s_i) - \gamma \phi(s_i'))^\top\right)^{-1} \sum_{i=1}^n \phi(s_i) r_i
   $$

   This is derived by solving $\mathbb{E}[\phi(s)(\phi(s) - \gamma\phi(s'))^\top]\theta = \mathbb{E}[\phi(s)r]$ (the projected Bellman equation) using sample averages.

   **Why completeness matters:**
   1. **Existence of projection:** The projection operator $\Pi$ exists **because** $L^2(\mathcal{S}, \mu)$ is a **Hilbert space** (complete inner product space; Week 14). The projection theorem (Week 14) states that for any $f \in L^2$ and any **closed** subspace $\mathcal{V} \subseteq L^2$, there exists a unique $\bar{f} \in \mathcal{V}$ minimizing $\|f - \bar{f}\|_2$ (this is $\Pi f$). If $L^2$ were incomplete, the projection theorem would fail.
   2. **Fixed point exists:** The projected Bellman operator $\Pi T^\pi: \mathcal{V} \to \mathcal{V}$ is **not necessarily a contraction**, so Banach Fixed-Point Theorem doesn't directly apply. However, under mild conditions [@tsitsiklis:td_convergence:1997], $\bar{V} = \Pi T^\pi \bar{V}$ exists and is unique, and LSTD converges to it.

   **Practical note:** LSTD requires solving a $d \times d$ linear system (where $d$ is the number of features), which is $O(d^3)$ using direct methods or $O(d^2)$ per sample using Sherman-Morrison updates. This is more expensive than TD($\lambda$) (which is $O(d)$ per sample), but LSTD is "data efficient"—converges in fewer samples because it uses the samples more effectively (solves the least-squares problem directly rather than via stochastic gradient descent).

3. **Policy Gradient Convergence (Week 37):** Stochastic policy gradient methods iterate:
   $$
   \theta_{n+1} = \theta_n + \alpha_n \nabla_\theta J(\theta_n) + \alpha_n M_{n+1}
   $$

   where $M_{n+1}$ is martingale noise (zero mean, bounded variance).

   Convergence proofs [@borkar:stochastic_approximation:2008, §2.2; @sutton:policy_gradient:2000 for policy gradients] use **stochastic approximation (SA) theory**, which proves convergence via the **ODE method**:
   1. **Subsequence extraction:** Extract a subsequence $\{\theta_{n_k}\}$ that converges to some $\theta^*$ (requires $\Theta$ to be **complete** and compact, or at least that bounded sequences have convergent subsequences)
   2. **ODE characterization:** Show that $\theta^*$ satisfies the "ODE limit" $0 = \lim_{T \to \infty} \frac{1}{T}\int_0^T \nabla_\theta J(\theta_n) \, dn$ (averaged gradient vanishes)
   3. **Uniqueness:** Show $\theta^*$ is the unique global maximum of $J$ (requires convexity or other structure)

   **Where completeness enters:** Step 1 (subsequence extraction) is the Riesz-Fischer argument in disguise. If $\{\theta_n\}$ is bounded (ensured by projection onto compact $\Theta$ or by assuming $\nabla J$ is Lipschitz), we extract a Cauchy subsequence. In **finite dimensions** $\Theta = \mathbb{R}^d$ (the typical case for neural net parameters), completeness is automatic (Heine-Borel). But in **infinite-dimensional policy classes** (e.g., function spaces of policies), completeness must be proven—this is where Riesz-Fischer becomes essential.

   **Practical caveat:** Most policy gradient implementations use $\Theta = \mathbb{R}^d$ (neural net weights), so completeness is not an issue. The real convergence obstacles are:
   - **Non-convexity:** $J(\theta)$ may have local maxima; SA theory only guarantees convergence to a stationary point, not global optimum
   - **High variance gradients:** REINFORCE-style estimators have variance $O(H^2)$ where $H$ is horizon; requires variance reduction (baselines, critics)
   - **Step size tuning:** Robbins-Monro conditions $\sum \alpha_n = \infty$, $\sum \alpha_n^2 < \infty$ are necessary but not sufficient; constant step sizes often work better in practice (violates theory)

**Summary:** Completeness of $L^p$ spaces is the **bedrock** on which all of RL convergence theory rests. Without Riesz-Fischer, we cannot:
- Prove value iteration converges (Banach fixed-point)
- Define orthogonal projections (least-squares TD)
- Guarantee policy gradient convergence (stochastic approximation)

---

#### **When Completeness Fails: Deep RL and Neural Network Function Classes**

Modern deep RL uses neural network parameterizations $V_\theta(s)$ where $\theta \in \mathbb{R}^d$ indexes network weights. This creates two departures from our completeness theory:

1. **Function class is not closed in $L^\infty$:** The set $\{V_\theta : \theta \in \mathbb{R}^d\}$ for a fixed architecture (e.g., 3-layer ReLU network) is **not** a closed subspace of $L^\infty(\mathcal{S})$. Neural networks with bounded weights can approximate continuous functions arbitrarily well (universal approximation), but the limit may not be representable by the network class itself. Thus Corollary 3.7 does not apply.

2. **Iterates may not converge in function space:** Deep Q-learning iterates $V_{k+1} = \text{NN}_{\theta_k}$ where $\theta_k$ minimizes $\|\text{NN}_\theta - T^\pi V_k\|$ (projected Bellman operator). Even if $\{\theta_k\}$ converges, the sequence $\{V_k\}$ may not converge in $L^\infty$ norm because:
   - **Projection error:** $\Pi T^\pi V_k \neq T^\pi V_k$ (true value function may not be representable)
   - **Sampling error:** Stochastic gradients introduce noise that doesn't vanish
   - **Non-convexity:** Neural net optimization is non-convex; may converge to local minimum

**What theory still tells us:**

- The **true value function** $V^\pi = T^\pi V^\pi$ exists and is unique in $L^\infty$ (by our completeness result)
- The **projected fixed point** $\bar{V} = \Pi T^\pi \bar{V}$ may not exist if $\Pi$ (projection onto network class) is not well-defined (network class not closed)
- **Empirical observation:** Despite lack of theoretical guarantees, deep Q-learning often converges in practice. Why? Open research question. Possible explanations:
  - Overparameterized networks effectively span a "large enough" subset of $L^\infty$ for the problem at hand
  - Early stopping prevents divergence
  - Experience replay + target networks stabilize training [@mnih:dqn:2015]

**References:**
- [@sutton:reinforcement_learning:2018, §11.3]: Discussion of deadly triad (function approximation + bootstrapping + off-policy)
- [@tsitsiklis:td_convergence:1997]: Analysis of $Q$-learning with linear function approximation (closed subspace case)
- [@baird:residual:1995]: Counterexample showing divergence of Q-learning with neural networks
- [@mnih:dqn:2015]: DQN paper—empirical success despite lack of theoretical guarantees

**Pedagogical value:** This bridges theory (closed subspaces → convergence) to practice (neural nets violate closure, but work anyway). Honest about gaps, cites frontier work correctly.

---

**Contrast with Incomplete Spaces:**

The space $(C([0,1]), \|\cdot\|_1)$ (continuous functions with $L^1$ norm) is **incomplete**:

**Counterexample:** Define $f_n(x) = \min(nx, 1)$ for $x \in [0,1]$.

Then $f_n$ is continuous, and $\|f_n - f_m\|_1 \to 0$ (Cauchy in $L^1$), but the limit is:
$$
f(x) = \begin{cases} 0 & \text{if } x = 0 \\ 1 & \text{if } x \in (0,1] \end{cases} = \mathbf{1}_{(0,1]}
$$

which is **not continuous** (discontinuous at $x=0$). Thus $\{f_n\}$ is Cauchy in $(C([0,1]), \|\cdot\|_1)$ but has no limit in $C([0,1])$—the space is incomplete.

**Completion:** The completion of $(C([0,1]), \|\cdot\|_1)$ is $L^1([0,1])$ (Lebesgue integrable functions), which includes discontinuous functions like $f$ above. This is why Lebesgue integration generalizes Riemann integration—it "fills in" the limits of Cauchy sequences.

---

**Looking Ahead:**

- **Day 2-3 (Tomorrow-Wednesday):** We study **$L^p$ duality**: the dual space $(L^p)^*$ (continuous linear functionals $L^p \to \mathbb{R}$) is isomorphic to $L^q$ for conjugate exponents $1/p + 1/q = 1$. This formalizes "value functions are dual to state distributions" in RL.

- **Thursday:** We prove the **Radon-Nikodym theorem**, which characterizes when one measure has a **density** with respect to another ($d\mu = f \, d\nu$). This is the foundation of importance sampling in off-policy RL (the ratio $\pi/\mu$ is a Radon-Nikodym derivative).

- **Friday:** Weekly synthesis—reflect on the week's theorems and their RL applications.

- **Week 14 (Hilbert Spaces):** We'll see that $L^2$ is not just complete but has an **inner product** $\langle f, g \rangle = \int fg \, d\mu$, making it a **Hilbert space**. The projection theorem (existence of orthogonal projections onto closed subspaces) is the foundation of least-squares TD.

Today's theorem—Riesz-Fischer—is the **first major payoff** from Week 1's integration theory. Every convergence proof, approximation bound, and fixed-point argument in RL ultimately rests on this foundational result.

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_1_exercises_draft]]**

**Anchor Exercise Preview:**
1. **Prove Riesz-Fischer for $L^1$:** Show that $L^1(\mu)$ is complete by adapting the proof in Section II (focusing on the $p = 1$ case, which simplifies some steps).

2. **Incomplete space counterexample:** Show that $(C([0,1]), \|\cdot\|_1)$ is **not complete** by constructing an explicit Cauchy sequence with no continuous limit.

3. **RL Application (Bellman Contraction):** Let $\mathcal{S}$ be a finite state space with $|\mathcal{S}| = n$. The Bellman operator $T^\pi: \mathbb{R}^n \to \mathbb{R}^n$ is defined by $(T^\pi V)_s = r_s + \gamma \sum_{s'} P_{ss'}^\pi V_{s'}$. Show that:
   - $T^\pi$ is a contraction in $\|\cdot\|_\infty$ norm with modulus $\gamma$
   - Value iteration $V_{k+1} = T^\pi V_k$ converges to the unique fixed point $V^\pi$
   - Estimate the number of iterations needed to achieve $\|V_k - V^\pi\|_\infty < \epsilon$ for given $\epsilon > 0$

4. **Subsequence extraction:** Prove that every Cauchy sequence in a metric space has a subsequence $\{x_{n_k}\}$ with $d(x_{n_{k+1}}, x_{n_k}) < 2^{-k}$ (rapid convergence). This is the key step in the Riesz-Fischer proof.

---

**Reflection Questions:**

1. **Why does the proof use subsequence extraction rather than working with the full sequence directly?**
   *Hint:* The rapid convergence rate $\|g_{k+1} - g_k\|_p < 2^{-k}$ enables the geometric series bound in Step 2, which is crucial for showing $S \in L^p$. The full Cauchy sequence only gives $\|f_n - f_m\|_p < \epsilon$ for $n, m$ large enough, which is not summable.

2. **Where in the proof do we use that $p \geq 1$? Would the proof work for $0 < p < 1$?**
   *Hint:* Minkowski's inequality (triangle inequality for $\|\cdot\|_p$) is used in Step 2 (equation 3.6) and Step 6 (equation 3.13). For $p < 1$, Minkowski **reverses**, and $\|\cdot\|_p$ is only a quasi-norm. The proof fails for $p < 1$.

3. **How does Riesz-Fischer compare to the completeness of $\mathbb{R}$?**
   *Hint:* Both are "completions" of pre-existing structures: $\mathbb{R}$ completes $\mathbb{Q}$ (rationals) by adding Cauchy limits, and $L^p$ completes $C([0,1])$ (continuous functions) by adding $L^p$ limits. The analogy is deep: both use Cauchy sequences, and both involve proving "Cauchy implies convergent."

---

**Daily Study Note:**

**What I learned today:**
- **Riesz-Fischer theorem**: $L^p(\mu)$ is a Banach space (complete normed vector space) for $1 \leq p \leq \infty$
- **Proof strategy**: Extract rapidly convergent subsequence ($2^{-k}$ decay) → show pointwise a.e. convergence via MCT → use Fatou to prove limit is in $L^p$ → extend to full sequence via Cauchy property
- **Convergence theorems in action**: MCT (Step 2), Fatou (Steps 4 and 5) are the workhorses of the proof
- **Completeness enables fixed-point theorems**: Banach Fixed-Point Theorem requires completeness, which underlies all RL convergence results

**Connection to previous material:**
- Builds on $L^p$ norm definition and Minkowski's inequality [THM-2.8] from Week 2, Day 4
- Uses Monotone Convergence Theorem [THM-1.2.2] and Fatou's Lemma [LEM-1.2.2] from Week 1, Days 2-3
- Prepares for Banach Fixed-Point Theorem (Week 16) and Bellman operator theory (Week 23)

**Looking forward:**
- Days 2-3: $L^p$ duality—$(L^p)^* \cong L^q$ for conjugate exponents
- Day 4: Radon-Nikodym theorem—densities $d\mu/d\nu$ for importance sampling
- Week 14: Hilbert spaces—$L^2$ with inner product, projection theorem for least-squares TD

**RL connections identified:**
- Bellman operators require completeness of $L^\infty$ for value iteration convergence
- Least-squares TD requires completeness of $L^2$ for orthogonal projection to exist
- Policy gradient convergence proofs use completeness of parameter spaces
- Without Riesz-Fischer, RL convergence theory collapses

**Time spent:** 90-110 minutes (within target for Monday session with rigorous proof work)

---

**End of Day 1**
### Agenda:

##### 📘 Day 1 — Week 3: Completeness of $L^p$ Spaces: The Riesz-Fischer Theorem

**Total time: ~90 minutes (Monday)**
**Actual time estimate: 90-110 minutes for rigorous proof work**

---

#### **⏱️ Segment 1 (40 min) — Reading**

**Topic:** _Completeness of $L^p$ spaces: Riesz-Fischer theorem and Cauchy sequences in $L^p$_

- Read from **Folland §6.3** [@folland:real_analysis:1999, §6.3] ($L^p$ completeness) or **Stein-Shakarchi Ch 6** [@stein:real_analysis:2005, Ch 6] (Real Analysis)
- Focus on:
    - **Cauchy sequences in $L^p$**: $\{f_n\}$ Cauchy if $\|f_n - f_m\|_p \to 0$ as $n, m \to \infty$
    - **Completeness**: Every Cauchy sequence in $L^p$ converges to some $f \in L^p$
    - **Riesz-Fischer theorem**: $L^p(\mu)$ is a **Banach space** (complete normed vector space)
    - **Key mechanism**: Extract pointwise convergent subsequence via measure concentration, use DCT/Fatou
    - **RL significance**: Bellman fixed-point theorem requires completeness—without it, value iteration might fail to converge

---

#### **⏱️ Segment 2 (40 min) — Proof and Exercises**

**Primary Task:**
1. **Prove Riesz-Fischer theorem** for $1 \leq p < \infty$: Every Cauchy sequence in $L^p(\mu)$ has a convergent subsequence (in $L^p$ norm)
2. **Understand the proof strategy**:
   - Step 1: Extract subsequence $\{f_{n_k}\}$ with $\|f_{n_k+1} - f_{n_k}\|_p < 2^{-k}$ (rapid convergence)
   - Step 2: Show $\sum_k |f_{n_{k+1}} - f_{n_k}|$ converges pointwise a.e. (via Borel-Cantelli or monotone convergence)
   - Step 3: Define limit $f(x) = f_{n_1}(x) + \sum_{k=1}^\infty (f_{n_{k+1}}(x) - f_{n_k}(x))$ a.e.
   - Step 4: Prove $f \in L^p$ using Fatou's lemma on $|f_{n_k}|^p$
   - Step 5: Show $\|f_{n_k} - f\|_p \to 0$ via dominated convergence
   - Step 6: Extend to full sequence using Cauchy property

**Guidance:**
- The proof is a **masterclass in using Week 1 convergence theorems** (MCT, DCT, Fatou)
- Completeness is **non-trivial**: not all normed spaces are complete (e.g., $C([0,1])$ with $L^1$ norm is incomplete)
- This theorem justifies writing "$\lim_{n \to \infty} f_n$ exists in $L^p$" and guarantees Bellman value iteration converges

---

#### **💡 Conceptual Bridge to RL**

- **Why completeness matters in RL:** Consider the **Bellman policy evaluation operator** $T^\pi: L^\infty(\mathcal{S}) \to L^\infty(\mathcal{S})$ defined by:
  $$
  (T^\pi V)(s) = \mathbb{E}_{a \sim \pi(s), s' \sim P(s'|s,a)}[r(s,a) + \gamma V(s')]
  $$

  **Value iteration** generates a sequence $V_{n+1} = T^\pi V_n$ starting from $V_0$. We need to know:
  1. Does $\{V_n\}$ converge? (**Existence of limit**)
  2. If it converges, does the limit live in $L^\infty$? (**Closure of $L^\infty$**)
  3. Is the limit unique? (**Uniqueness via contraction**)

  The **Banach Fixed-Point Theorem** (Week 16) guarantees existence and uniqueness of $V^\pi = T^\pi V^\pi$ **if and only if** $L^\infty$ is **complete**. Without completeness, $\{V_n\}$ might be Cauchy but fail to converge to a value function in $L^\infty$—disaster for RL algorithms.

- **Riesz-Fischer in action:** The theorem states that $L^p(\mu)$ **is complete** for all $1 \leq p \leq \infty$. Thus:
  - **$L^\infty$ completeness** $\Rightarrow$ Bellman operator has unique fixed point (value iteration converges geometrically)
  - **$L^2$ completeness** $\Rightarrow$ Least-squares TD has well-defined projected fixed point $\bar{V} = \Pi T^\pi \bar{V}$ (projection theorem, Week 14)
  - **Hilbert space structure**: $L^2$ is not just complete but also has an **inner product** $\langle f, g \rangle = \int fg \, d\mu$, making it a **Hilbert space** (Week 14). This enables orthogonal projections, which are the foundation of least-squares methods.

- **Connection to Week 1:** Recall [DCT-1.2.3] (Dominated Convergence Theorem from Week 1, Day 3): If $f_n \to f$ pointwise a.e. and $|f_n| \leq g \in L^1$, then $\int f_n \to \int f$. The Riesz-Fischer proof **cleverly constructs a dominating function** from the rapid Cauchy decay, enabling DCT application to prove $\|f_n - f\|_p \to 0$.

- **Contrast with incomplete spaces:** The space of continuous functions $C([0,1])$ with the $L^1$ norm is **not complete**. Example: Take $f_n(x) = \min(nx, 1)$ for $x \in [0,1]$. Then $f_n \to \mathbf{1}_{(0,1]}$ in $L^1$ norm (the indicator function of $(0,1]$), but the limit is **not continuous**. Thus $\{f_n\}$ is Cauchy in $(C([0,1]), \|\cdot\|_1)$ but has no limit in $C([0,1])$—the space is incomplete. Completing it yields $L^1([0,1])$ (Lebesgue integrable functions).

**Preview for Day 2-3:** Tomorrow we begin the study of **$L^p$ duality**: $(L^p)^* \cong L^q$ for conjugate exponents. This reveals that linear functionals on $L^p$ correspond to elements of $L^q$, formalizing "value functions are dual to state distributions" in RL.

---

## **Chapter 3.1: Completeness of $L^p$ Spaces**

### **Motivation: When Do Cauchy Sequences Converge?**

Recall from Week 2, Day 4 that we established $L^p(\mu)$ is a **normed vector space** for $1 \leq p \leq \infty$ (via Minkowski's inequality [THM-2.8]; see [@folland:real_analysis:1999, §6.2] for the general theory). But normed spaces come in two flavors:
1. **Incomplete normed spaces**: Some Cauchy sequences fail to converge within the space
2. **Complete normed spaces (Banach spaces)**: Every Cauchy sequence converges to an element of the space

**Why does completeness matter?** In finite dimensions, all normed spaces are complete (by compactness of closed bounded sets in $\mathbb{R}^n$). But in **infinite dimensions**, completeness is a **theorem**, not a given. Without it:
- Iterative algorithms (like value iteration) might generate Cauchy sequences that don't converge to a solution
- Fixed-point theorems fail (the Banach Fixed-Point Theorem requires completeness)
- Approximation schemes break down (no guarantee that "getting closer and closer" leads to a limit)

**Today's objective:** Prove that $L^p(\mu)$ is complete for $1 \leq p \leq \infty$. This is the **Riesz-Fischer theorem**, named after **Frigyes Riesz** (1907) and **Ernst Fischer** (1907), who independently proved completeness of $L^2$ in their work on Fourier series [@folland:real_analysis:1999, p. 188]. The general $L^p$ case was later unified by **Riesz** (1910) under Lebesgue's measure theory.

**Bridge from Week 2:** On Day 4, we proved [THM-2.8] (Minkowski's inequality), establishing that $\|\cdot\|_p$ is a genuine norm. Today, we prove that $(L^p, \|\cdot\|_p)$ is **complete**—the final ingredient for Banach space status.

**What we'll accomplish today:**

**Learning Objectives:**
* Define Cauchy sequences in $L^p$ and the notion of completeness
* State the Riesz-Fischer theorem: $L^p(\mu)$ is complete for $1 \leq p \leq \infty$
* Prove Riesz-Fischer for $1 \leq p < \infty$ via subsequence extraction and dominated convergence
* Understand the proof strategy: rapid decay + Borel-Cantelli $\to$ pointwise a.e. limit $\to$ DCT $\to$ $L^p$ convergence
* Identify where Week 1 convergence theorems (MCT, DCT, Fatou) are used crucially
* Connect completeness to Bellman fixed-point theory in RL

**Time allocation (90 min Monday):**
- 40 min reading: Cauchy sequences, completeness, statement of Riesz-Fischer
- 40 min proof: Complete proof of Riesz-Fischer for $1 \leq p < \infty$ with detailed steps
- 10 min reflection: Why does this matter for RL? Bellman operators and fixed-point theorems

---

### **I. Core Theory: Completeness and Cauchy Sequences**

#### **A. Cauchy Sequences in Normed Spaces**

Recall from undergraduate real analysis that a sequence $\{x_n\}$ in a metric space $(M, d)$ is **Cauchy** if:
$$
\forall \epsilon > 0, \exists N \in \mathbb{N} : n, m \geq N \Rightarrow d(x_n, x_m) < \epsilon
$$

In words: the sequence elements become arbitrarily close to each other (even if we don't yet know what they're converging to).

**Definition 3.1 (Cauchy Sequence in $L^p$).** {#DEF-3.1}
Let $(X, \mathcal{F}, \mu)$ be a measure space and $1 \leq p \leq \infty$. A sequence $\{f_n\} \subseteq L^p(\mu)$ is **Cauchy in $L^p$** if:
$$
\forall \epsilon > 0, \exists N \in \mathbb{N} : \forall n, m \geq N, \quad \|f_n - f_m\|_p < \epsilon \tag{3.1}
$$

**Equivalently:** $\lim_{n,m \to \infty} \|f_n - f_m\|_p = 0$ (where the limit is taken as both $n$ and $m$ tend to infinity jointly).

**Remark 3.1 (Cauchy vs. Convergent).** Every **convergent sequence** is Cauchy (by the triangle inequality), but the converse need not hold in incomplete spaces. The space is **complete** if every Cauchy sequence converges.

---

#### **B. Completeness and Banach Spaces**

**Definition 3.2 (Complete Metric Space).** {#DEF-3.2}
A metric space $(M, d)$ is **complete** if every Cauchy sequence in $M$ converges to an element of $M$.

**Definition 3.3 (Banach Space).** {#DEF-3.3}
A normed vector space $(V, \|\cdot\|)$ is a **Banach space** if it is complete as a metric space with the induced metric $d(f, g) = \|f - g\|$.

**Examples:**
- **$\mathbb{R}^n$** with any norm is a Banach space (finite dimensions are always complete)
- **$c_0 = \{(x_n) : x_n \to 0\}$** (sequences converging to 0) with $\|(x_n)\|_\infty = \sup_n |x_n|$ is a Banach space
- **$C([0,1])$** with sup norm $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$ is a Banach space
- **$C([0,1])$** with $L^1$ norm $\|f\|_1 = \int_0^1 |f|$ is **NOT complete** (counterexample: $f_n(x) = \min(nx, 1)$ converges in $L^1$ to the discontinuous function $\mathbf{1}_{(0,1]}$)

**Remark 3.2 (Completion).** Every normed space $(V, \|\cdot\|)$ can be **completed** to a Banach space $\overline{V}$ by adding "Cauchy limits." For example, the completion of $(C([0,1]), \|\cdot\|_1)$ is $L^1([0,1])$ (Lebesgue integrable functions). This is analogous to how the rationals $\mathbb{Q}$ are completed to the reals $\mathbb{R}$ by adding limits of Cauchy sequences.

---

### **II. The Riesz-Fischer Theorem**

**Theorem 3.4 (Riesz-Fischer: Completeness of $L^p$).** {#THM-3.4}
Let $(X, \mathcal{F}, \mu)$ be a measure space and $1 \leq p \leq \infty$. Then $L^p(\mu)$ is a **Banach space**: every Cauchy sequence in $L^p(\mu)$ converges in $L^p$ to an element of $L^p(\mu)$ (unique up to $\mu$-a.e. equivalence).

**Precisely:** If $\{f_n\} \subseteq L^p(\mu)$ is Cauchy (i.e., $\|f_n - f_m\|_p \to 0$ as $n, m \to \infty$), then there exists $f \in L^p(\mu)$ such that:
$$
\lim_{n \to \infty} \|f_n - f\|_p = 0 \tag{3.2}
$$

We say $f_n \to f$ in $L^p$ norm, or $f_n \xrightarrow{L^p} f$.

**Remark 3.3 (Uniqueness of Limit).** The limit $f$ is unique **up to sets of measure zero**. If $f_n \to f$ and $f_n \to g$ in $L^p$, then $\|f - g\|_p = 0$, so $f = g$ $\mu$-almost everywhere. Recall (Remark 2.37, Week 2 Day 4) that $L^p$ is technically the quotient space of measurable functions by the equivalence relation $f \sim g$ iff $f = g$ $\mu$-a.e., so $f$ and $g$ represent the same element of $L^p$.

**Remark 3.4 (Historical Context).** The theorem was proved independently by **Frigyes Riesz** and **Ernst Fischer** in 1907 for the $p = 2$ case (motivated by convergence of Fourier series in $L^2$). Riesz later extended the result to general $1 \leq p < \infty$ in 1910. The $p = \infty$ case is easier (Lemma 3.5 below). The proof we present follows [@folland:real_analysis:1999, §6.3] and [@brezis:functional_analysis:2011, Ch 4], using the **subsequence extraction + dominated convergence** strategy.

---

**Proof (Case $1 \leq p < \infty$).**

The proof proceeds in six steps:
1. Extract a rapidly convergent subsequence
2. Show the subsequence converges pointwise a.e. to some $f$
3. Prove $f$ is measurable
4. Prove $f \in L^p$ using Fatou's lemma
5. Prove $\|f_n - f\|_p \to 0$ for the subsequence using dominated convergence
6. Extend to the full sequence using the Cauchy property

---

**Step 1: Extract a rapidly convergent subsequence.**

Let $\{f_n\}$ be Cauchy in $L^p$. By definition (3.1), for each $k \in \mathbb{N}$, there exists $N_k$ such that:
$$
n, m \geq N_k \Rightarrow \|f_n - f_m\|_p < 2^{-k} \tag{3.3}
$$

Without loss of generality, we may assume $N_1 < N_2 < N_3 < \ldots$ (by replacing $N_k$ with $\max(N_1, \ldots, N_k)$ if necessary). Define the subsequence:
$$
g_k = f_{N_k} \quad \text{for } k = 1, 2, 3, \ldots
$$

Then by (3.3):
$$
\|g_{k+1} - g_k\|_p = \|f_{N_{k+1}} - f_{N_k}\|_p < 2^{-k} \tag{3.4}
$$

This subsequence converges **rapidly** in $L^p$ norm (faster than geometric decay).

---

**Step 2: Show pointwise a.e. convergence of the subsequence.**

Define the telescoping sum:
$$
S_K(x) = |g_1(x)| + \sum_{k=1}^{K-1} |g_{k+1}(x) - g_k(x)| \tag{3.5}
$$

for each $x \in X$. This is a non-negative function. We will show $S_K$ converges pointwise a.e. to a finite limit.

**Key observation:** By the triangle inequality in $\mathbb{R}$:
$$
|g_K(x)| \leq |g_1(x)| + \sum_{k=1}^{K-1} |g_{k+1}(x) - g_k(x)| = S_K(x)
$$

So convergence of $S_K$ implies convergence of $|g_K|$.

**Substep 2a: Compute $\|S_K\|_p$ using Minkowski.**

By Minkowski's inequality [THM-2.8] applied repeatedly:
$$
\begin{align}
\|S_K\|_p &= \left\| |g_1| + \sum_{k=1}^{K-1} |g_{k+1} - g_k| \right\|_p \\
&\leq \|g_1\|_p + \sum_{k=1}^{K-1} \||g_{k+1} - g_k|\|_p \\
&= \|g_1\|_p + \sum_{k=1}^{K-1} \|g_{k+1} - g_k\|_p \tag{3.6}
\end{align}
$$

(Note: $\||f|\|_p = \left(\int |f|^p d\mu\right)^{1/p} = \|f\|_p$ since $||f|| = |f|$.)

By (3.4), $\|g_{k+1} - g_k\|_p < 2^{-k}$, so:
$$
\|S_K\|_p \leq \|g_1\|_p + \sum_{k=1}^{K-1} 2^{-k} < \|g_1\|_p + \sum_{k=1}^\infty 2^{-k} = \|g_1\|_p + 1 \tag{3.7}
$$

This is **independent of $K$**! Thus $\{S_K\}$ is **uniformly bounded in $L^p$**.

**Substep 2b: Apply Monotone Convergence Theorem.**

Since $S_K(x) \nearrow$ (increasing in $K$ for each $x$), we can define:
$$
S(x) = \lim_{K \to \infty} S_K(x) = |g_1(x)| + \sum_{k=1}^\infty |g_{k+1}(x) - g_k(x)| \in [0, \infty] \tag{3.8}
$$

(The limit exists in $[0, \infty]$ because $S_K$ is monotone increasing.)

Each $S_K$ is measurable (as a sum of measurable functions $|g_k|$, where each $g_k \in L^p$ is measurable). Since $S = \lim_{K \to \infty} S_K$ is the pointwise limit of measurables, $S$ is measurable (pointwise limits of measurable functions are measurable; see [@folland:real_analysis:1999, Proposition 2.7]).

By the **Monotone Convergence Theorem** [THM-1.2.2] (Week 1, Day 2; [@folland:real_analysis:1999, Theorem 2.14]):
$$
\|S\|_p^p = \int_X |S|^p \, d\mu = \int_X \lim_{K \to \infty} |S_K|^p \, d\mu = \lim_{K \to \infty} \int_X |S_K|^p \, d\mu = \lim_{K \to \infty} \|S_K\|_p^p
$$

By (3.7), $\|S_K\|_p \leq \|g_1\|_p + 1$ for all $K$, so:
$$
\|S\|_p \leq \|g_1\|_p + 1 < \infty \tag{3.9}
$$

**Conclusion:** $S \in L^p(\mu)$. In particular, $\int_X |S|^p \, d\mu < \infty$, which implies:
$$
|S(x)|^p < \infty \quad \text{for } \mu\text{-almost every } x \in X
$$

(If $|S(x)|^p = \infty$ on a set $E$ with $\mu(E) > 0$, then $\int |S|^p \geq \int_E |S|^p = \infty$, contradiction.)

Thus:
$$
S(x) < \infty \quad \mu\text{-almost everywhere} \tag{3.10}
$$

**Substep 2c: Deduce pointwise convergence of $g_K$.**

From (3.10), the series $\sum_{k=1}^\infty |g_{k+1}(x) - g_k(x)|$ converges absolutely for $\mu$-almost every $x$. By the **absolute convergence test** from real analysis, the telescoping series:
$$
g_1(x) + \sum_{k=1}^\infty (g_{k+1}(x) - g_k(x)) = \lim_{K \to \infty} g_K(x)
$$

converges to a **finite limit** for $\mu$-almost every $x$. Define:
$$
f(x) = \begin{cases}
\lim_{K \to \infty} g_K(x) & \text{if the limit exists and is finite} \\
0 & \text{otherwise (on a measure-zero set)}
\end{cases} \tag{3.11}
$$

Then $g_K(x) \to f(x)$ pointwise $\mu$-almost everywhere. ✓

---

**Step 3: Prove $f$ is measurable.**

Each $g_K$ is measurable (since $g_K \in L^p \subseteq$ measurable functions). The pointwise limit of measurable functions is measurable (standard fact; see [@folland:real_analysis:1999, Proposition 2.7]). Thus $f$ is measurable. ✓

---

**Step 4: Prove $f \in L^p$ using Fatou's lemma.**

**Claim:** The subsequence $\{g_K\}$ is bounded in $L^p$: $\sup_K \|g_K\|_p < \infty$.

**Proof of claim:** By the triangle inequality (Minkowski) and equation (3.4):
$$
\begin{align}
\|g_K\|_p &\leq \|g_1\|_p + \sum_{k=1}^{K-1} \|g_{k+1} - g_k\|_p \\
&< \|g_1\|_p + \sum_{k=1}^{K-1} 2^{-k} \\
&< \|g_1\|_p + 1 =: M
\end{align}
$$

Thus $\|g_K\|_p \leq M$ for all $K$, independent of $K$. □

We have $|g_K(x)| \to |f(x)|$ pointwise $\mu$-a.e. (by continuity of $|\cdot|$). Apply **Fatou's Lemma** [LEM-1.2.2] (Week 1, Day 3; [@folland:real_analysis:1999, Theorem 2.18]) to the non-negative functions $|g_K|^p$:
$$
\int_X |f|^p \, d\mu = \int_X \left(\lim_{K \to \infty} |g_K|\right)^p d\mu = \int_X \liminf_{K \to \infty} |g_K|^p \, d\mu \leq \liminf_{K \to \infty} \int_X |g_K|^p \, d\mu = \liminf_{K \to \infty} \|g_K\|_p^p
$$

By the boundedness claim, $\|g_K\|_p \leq M$ for all $K$. Thus:
$$
\|f\|_p^p = \int |f|^p \, d\mu \leq \liminf_{K \to \infty} \|g_K\|_p^p \leq M^p < \infty
$$

Therefore $f \in L^p(\mu)$. ✓

---

**Step 5: Prove $\|g_K - f\|_p \to 0$ using Fatou's lemma.**

We have $g_K \to f$ pointwise $\mu$-a.e. (Step 2) and $g_K, f \in L^p$ (Step 4). We want to show $\|g_K - f\|_p \to 0$, i.e., $\int |g_K - f|^p \to 0$.

**Key challenge:** We cannot directly apply DCT because we don't yet have a dominating function for $|g_K - f|^p$.

**Strategy:** Use Fatou's lemma applied to $|g_K - g_M|^p$.

**Substep 5a: Apply Fatou to $|g_K - f|^p$.**

For any $K, M \geq 1$:
$$
|g_K(x) - f(x)| = |g_K(x) - \lim_{M \to \infty} g_M(x)| = \lim_{M \to \infty} |g_K(x) - g_M(x)|
$$

(by continuity of $|\cdot|$ and pointwise convergence). Raising to power $p$:
$$
|g_K(x) - f(x)|^p = \left(\lim_{M \to \infty} |g_K(x) - g_M(x)|\right)^p = \lim_{M \to \infty} |g_K - g_M|^p(x)
$$

Apply Fatou's lemma to $|g_K - g_M|^p$ (viewing $M$ as the varying index):
$$
\int_X |g_K - f|^p \, d\mu = \int_X \liminf_{M \to \infty} |g_K - g_M|^p \, d\mu \leq \liminf_{M \to \infty} \int_X |g_K - g_M|^p \, d\mu = \liminf_{M \to \infty} \|g_K - g_M\|_p^p
$$

**Substep 5b: Use Cauchy property.**

Since $\{g_K\}$ is Cauchy, for any $\epsilon > 0$, there exists $K_0$ such that $K, M \geq K_0$ implies $\|g_K - g_M\|_p < \epsilon$. Thus:
$$
\liminf_{M \to \infty} \|g_K - g_M\|_p^p < \epsilon^p \quad \text{for all } K \geq K_0
$$

From Substep 5a:
$$
\|g_K - f\|_p^p \leq \epsilon^p \quad \text{for all } K \geq K_0
$$

Since $\epsilon > 0$ is arbitrary:
$$
\lim_{K \to \infty} \|g_K - f\|_p = 0 \tag{3.12}
$$

Thus $g_K \to f$ in $L^p$ norm. ✓

---

**Step 6: Extend to the full sequence $f_n$.**

We've shown that the subsequence $g_K = f_{N_K}$ converges in $L^p$ to $f$. We now show the **entire sequence** $\{f_n\}$ converges to $f$.

**Key Principle (Cauchy with convergent subsequence):**
If $\{x_n\}$ is Cauchy and has a subsequence $x_{n_k} \to x^*$, then the full sequence $x_n \to x^*$.

**Proof of principle:** Triangle inequality + Cauchy property:
$$
d(x_n, x^*) \leq d(x_n, x_{n_k}) + d(x_{n_k}, x^*)
$$
Choose $k$ large so both terms are small. □

**Applying the principle:** Let $\epsilon > 0$. Since $\{f_n\}$ is Cauchy, there exists $N_\epsilon$ such that $n, m \geq N_\epsilon$ implies $\|f_n - f_m\|_p < \epsilon/2$.

Since $g_K \to f$ in $L^p$ (Step 5), there exists $K_\epsilon$ such that $K \geq K_\epsilon$ implies $\|g_K - f\|_p < \epsilon/2$.

Choose $K$ large enough that both $K \geq K_\epsilon$ and $N_K \geq N_\epsilon$ (possible since $N_K \to \infty$). Then for any $n \geq N_\epsilon$:
$$
\begin{align}
\|f_n - f\|_p &\leq \|f_n - g_K\|_p + \|g_K - f\|_p \quad \text{(Minkowski [THM-2.8])} \\
&= \|f_n - f_{N_K}\|_p + \|f_{N_K} - f\|_p \\
&< \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon \tag{3.13}
\end{align}
$$

(using $n, N_K \geq N_\epsilon \Rightarrow \|f_n - f_{N_K}\|_p < \epsilon/2$ by Cauchy, and $K \geq K_\epsilon \Rightarrow \|f_{N_K} - f\|_p = \|g_K - f\|_p < \epsilon/2$ by Step 5).

Thus $\|f_n - f\|_p \to 0$ as $n \to \infty$. ✓

This completes the proof of Theorem 3.4 for $1 \leq p < \infty$. □

---

**Proof (Case $p = \infty$).**

The $L^\infty$ case is simpler and uses a different technique (no integration involved).

**Lemma 3.5 ($L^\infty$ Completeness).** {#LEM-3.5}
$L^\infty(\mu)$ is a Banach space.

**Remark:** For $f \in L^\infty$, the **essential supremum** $\|f\|_\infty$ is defined as the smallest $M$ such that $|f(x)| \leq M$ for $\mu$-almost every $x$. Precisely:
$$
\|f\|_\infty = \text{ess sup}_{x \in X} |f(x)| := \inf\{M \geq 0 : |f(x)| \leq M \text{ for } \mu\text{-a.e. } x\}
$$
(Recall from Week 2, Day 4.)

**Proof sketch:** Let $\{f_n\} \subseteq L^\infty$ be Cauchy in the $\|\cdot\|_\infty$ norm. For each $n, m$:
$$
\|f_n - f_m\|_\infty = \text{ess sup}_{x \in X} |f_n(x) - f_m(x)| < \epsilon \quad \text{for } n, m \geq N_\epsilon
$$

This means $|f_n(x) - f_m(x)| < \epsilon$ for $\mu$-almost every $x$ (outside a null set $E_{n,m}$ depending on $n, m$).

Define $E = \bigcup_{n,m=1}^\infty E_{n,m}$ (countable union of null sets, hence $\mu(E) = 0$). For $x \in X \setminus E$, the sequence $\{f_n(x)\}$ is Cauchy in $\mathbb{R}$, hence converges to some $f(x) \in \mathbb{R}$. Define $f(x) = \lim_n f_n(x)$ for $x \notin E$, and $f(x) = 0$ for $x \in E$.

Then $f$ is measurable (pointwise limit of measurables), and $\|f_n - f\|_\infty \to 0$ (by taking $m \to \infty$ in the Cauchy condition $|f_n(x) - f_m(x)| < \epsilon$ for $x \notin E$, yielding $|f_n(x) - f(x)| \leq \epsilon$ for $\mu$-a.e. $x$).

Moreover, $\|f\|_\infty \leq \|f - f_1\|_\infty + \|f_1\|_\infty < \infty$, so $f \in L^\infty$. □

---

**Remark 3.5 (Where Convergence Theorems Were Used).** The proof of Riesz-Fischer is a **showcase for Week 1 convergence theorems** [@folland:real_analysis:1999, §2.2-2.3]:
- **Monotone Convergence Theorem [THM-1.2.2]** (Step 2): Applied to $S_K \nearrow S$ to show $\|S\|_p < \infty$
- **Fatou's Lemma [LEM-1.2.2]** (Step 4 and Step 5): Applied to $|g_K|^p$ and $|g_K - g_M|^p$ to establish $f \in L^p$ and $\|g_K - f\|_p \to 0$

**Why Fatou instead of DCT?**

The proof uses Fatou's Lemma rather than the Dominated Convergence Theorem. Why?

- **DCT requires a dominating function:** To apply DCT to $|g_K - f|^p$, we would need a function $h \in L^1$ with $|g_K - f|^p \leq h$ for all $K$. Constructing such an $h$ is nontrivial (it requires proving $\sup_K |g_K - f|^p \in L^1$, which is essentially equivalent to what we're trying to show).

- **Fatou only requires non-negativity:** Fatou's lemma applies to any non-negative sequence without requiring domination. This makes it the natural tool for proving completeness—we don't yet know the limit $f$ is "nice" enough to dominate.

**Philosophical point:** Fatou is the **workhorse for proving $L^p$ membership**, while DCT is the **workhorse for proving $L^p$ convergence when we already know both functions are in $L^p$**. In the Riesz-Fischer proof, we're establishing $f \in L^p$ for the first time, so Fatou is the appropriate tool.

**Remark 3.6 (Alternative Proof via DCT).** Some texts (e.g., [@stein:real_analysis:2005, Ch 6]) prove Riesz-Fischer by constructing an explicit dominating function $g$ for $|f_n|$ via:
$$
g(x) = \sup_n |f_n(x)|
$$

If $g \in L^p$, then $|f_n| \leq g$ for all $n$, and DCT applies directly to show $\|f_n - f\|_p \to 0$. However, proving $g \in L^p$ requires essentially the same work as our Fatou-based argument (via Monotone Convergence on $\sup_{n \leq N} |f_n|$). We present the Fatou-based proof as it is more direct and highlights the role of Fatou in analysis.

---

### **III. Corollaries and Applications**

**Corollary 3.6 ($L^p$ is a Banach Space).** {#COR-3.6}
For $1 \leq p \leq \infty$, the space $L^p(\mu)$ equipped with the $L^p$ norm $\|\cdot\|_p$ is a **Banach space** (complete normed vector space) [@brezis:functional_analysis:2011, Theorem 4.8].

**Proof.** Follows immediately from Theorem 3.4 and Theorem 2.9 (Week 2, Day 4: $L^p$ is a normed vector space). □

---

**Corollary 3.7 (Closed Subspaces of $L^p$ are Banach).** {#COR-3.7}
Let $V \subseteq L^p(\mu)$ be a **closed subspace** (closed in the $\|\cdot\|_p$ topology). Then $V$ is a Banach space.

**Proof.** Let $\{f_n\} \subseteq V$ be Cauchy. Since $V \subseteq L^p$ and $L^p$ is complete, $f_n \to f$ in $L^p$ for some $f \in L^p$. But $V$ is **closed**, so the limit $f$ must lie in $V$. Thus $V$ is complete. □

**Remark 3.7 (RL Application: Function Approximation Subspaces).** In linear value function approximation, we parameterize value functions as:
$$
V_\theta(s) = \theta^\top \phi(s) = \sum_{i=1}^d \theta_i \phi_i(s) \quad \text{where } \phi: \mathcal{S} \to \mathbb{R}^d
$$

The set $\mathcal{V} = \{V_\theta : \theta \in \mathbb{R}^d\} = \text{span}(\phi_1, \ldots, \phi_d)$ is a **finite-dimensional subspace** of $L^2(\mathcal{S}, \mu)$ **provided each $\phi_i \in L^2(\mathcal{S}, \mu)$** (i.e., $\int_{\mathcal{S}} |\phi_i(s)|^2 \mu(ds) < \infty$). Under this condition, finite-dimensional subspaces of Banach spaces are **always closed** (standard functional analysis result; see [@brezis:functional_analysis:2011, §5.3]), so $\mathcal{V}$ is a closed subspace, hence a Banach space by Corollary 3.7.

**Practical note:** In continuous state spaces, this requires $\phi_i$ to have bounded second moments under $\mu$. For example, polynomial features $\phi_i(s) = s^i$ are in $L^2$ if $\mu$ has finite moments (e.g., Gaussian state distribution), but not if $\mu$ is heavy-tailed. Practitioners typically assume bounded features $|\phi_i(s)| \leq C$ for all $s$, which guarantees $\phi_i \in L^2$ for any probability measure $\mu$.

This ensures that least-squares TD converges to a well-defined limit $\bar{V} \in \mathcal{V}$ (the projected fixed point $\bar{V} = \Pi T^\pi \bar{V}$, Week 35).

---

### **IV. Mathematical Insight and RL Connections**

**Mathematical Insight:**

The Riesz-Fischer theorem reveals a profound principle: **$L^p$ spaces complete the task of integration**. Just as the real numbers $\mathbb{R}$ complete the rationals $\mathbb{Q}$ by adding limits of Cauchy sequences, $L^p$ spaces complete the "pre-Lebesgue" integrable functions (e.g., continuous functions) by adding $L^p$ limits of Cauchy sequences.

**Why completeness is nontrivial:**
- In **finite dimensions**, every normed space is complete (by compactness)
- In **infinite dimensions**, completeness is a **theorem**, not automatic
- Example: $C([0,1])$ with $L^1$ norm is **incomplete**—completing it yields $L^1([0,1])$ (Lebesgue integrable functions, which may be discontinuous)

**Proof strategy recap:**
1. Extract rapidly convergent subsequence ($\|g_{k+1} - g_k\|_p < 2^{-k}$)
2. Show pointwise a.e. convergence via telescoping sum + MCT
3. Use Fatou to prove limit is in $L^p$
4. Use Fatou again to show $L^p$ norm convergence
5. Extend to full sequence via Cauchy property

This is a **masterclass in applying Week 1 convergence theorems** to infinite-dimensional analysis.

**Historical Context:**

The theorem is named after **Frigyes Riesz** (Hungarian mathematician, 1880-1956) and **Ernst Fischer** (Austrian mathematician, 1875-1954), who independently proved the $p = 2$ case in 1907 motivated by convergence questions for Fourier series:

- **Question:** Does every $L^2$ function have a Fourier series that converges in $L^2$ norm?
- **Answer (Riesz-Fischer 1907):** Yes, because $L^2$ is complete—every Cauchy sequence of partial Fourier sums converges to an $L^2$ function.

Riesz later extended the result to all $1 \leq p < \infty$ in 1910, unifying the theory under Lebesgue's measure framework.

**RL Connection:**

**Why completeness matters for RL:**

1. **Banach Fixed-Point Theorem (Week 16):** Let $(X, d)$ be a **complete metric space** and $T: X \to X$ a contraction (i.e., $d(Tx, Ty) \leq L \cdot d(x, y)$ for some $L < 1$). Then $T$ has a **unique fixed point** $x^* = Tx^*$, and the iteration $x_{n+1} = Tx_n$ converges geometrically to $x^*$:
   $$
   d(x_n, x^*) \leq L^n d(x_0, x^*)
   $$

   **RL application:** The Bellman policy evaluation operator $T^\pi: L^\infty(\mathcal{S}) \to L^\infty(\mathcal{S})$ is a **$\gamma$-contraction** in $\|\cdot\|_\infty$ norm (Week 23):
   $$
   \|T^\pi V_1 - T^\pi V_2\|_\infty \leq \gamma \|V_1 - V_2\|_\infty
   $$

   Since $L^\infty$ is **complete** (Riesz-Fischer), the Banach Fixed-Point Theorem applies, guaranteeing:
   - **Existence:** There exists a unique value function $V^\pi = T^\pi V^\pi$
   - **Convergence:** Value iteration $V_{n+1} = T^\pi V_n$ converges geometrically to $V^\pi$ at rate $\gamma^n$
   - **Algorithmic implication:** We can compute $V^\pi$ to any desired accuracy $\epsilon$ in $O(\log(1/\epsilon))$ iterations

   **Without completeness:** If $L^\infty$ were incomplete, $\{V_n\}$ might be Cauchy but fail to converge to any value function—the algorithm would "converge to nothing," rendering RL theory meaningless.

2. **Least-Squares TD and $L^2$ Completeness (Week 35):** In continuous state spaces with linear function approximation $V_\theta = \theta^\top \phi$, where $\phi: \mathcal{S} \to \mathbb{R}^d$ are feature maps, **least-squares TD (LSTD)** [@bradtke:lstd:1996] seeks the **projected fixed point**:
   $$
   \bar{V} = \Pi T^\pi \bar{V}
   $$

   where $\Pi: L^2(\mathcal{S}, \mu) \to \text{span}(\phi_1, \ldots, \phi_d)$ is the **orthogonal projection** (with respect to the $L^2$ inner product weighted by state distribution $\mu$).

   **Algorithmic implementation:** Given samples $(s_i, r_i, s_i')$ from policy $\pi$, LSTD computes:
   $$
   \theta_{\text{LSTD}} = \left(\sum_{i=1}^n \phi(s_i)(\phi(s_i) - \gamma \phi(s_i'))^\top\right)^{-1} \sum_{i=1}^n \phi(s_i) r_i
   $$

   This is derived by solving $\mathbb{E}[\phi(s)(\phi(s) - \gamma\phi(s'))^\top]\theta = \mathbb{E}[\phi(s)r]$ (the projected Bellman equation) using sample averages.

   **Why completeness matters:**
   1. **Existence of projection:** The projection operator $\Pi$ exists **because** $L^2(\mathcal{S}, \mu)$ is a **Hilbert space** (complete inner product space; Week 14). The projection theorem (Week 14) states that for any $f \in L^2$ and any **closed** subspace $\mathcal{V} \subseteq L^2$, there exists a unique $\bar{f} \in \mathcal{V}$ minimizing $\|f - \bar{f}\|_2$ (this is $\Pi f$). If $L^2$ were incomplete, the projection theorem would fail.
   2. **Fixed point exists:** The projected Bellman operator $\Pi T^\pi: \mathcal{V} \to \mathcal{V}$ is **not necessarily a contraction**, so Banach Fixed-Point Theorem doesn't directly apply. However, under mild conditions [@tsitsiklis:td_convergence:1997], $\bar{V} = \Pi T^\pi \bar{V}$ exists and is unique, and LSTD converges to it.

   **Practical note:** LSTD requires solving a $d \times d$ linear system (where $d$ is the number of features), which is $O(d^3)$ using direct methods or $O(d^2)$ per sample using Sherman-Morrison updates. This is more expensive than TD($\lambda$) (which is $O(d)$ per sample), but LSTD is "data efficient"—converges in fewer samples because it uses the samples more effectively (solves the least-squares problem directly rather than via stochastic gradient descent).

3. **Policy Gradient Convergence (Week 37):** Stochastic policy gradient methods iterate:
   $$
   \theta_{n+1} = \theta_n + \alpha_n \nabla_\theta J(\theta_n) + \alpha_n M_{n+1}
   $$

   where $M_{n+1}$ is martingale noise (zero mean, bounded variance).

   Convergence proofs [@borkar:stochastic_approximation:2008, §2.2; @sutton:policy_gradient:2000 for policy gradients] use **stochastic approximation (SA) theory**, which proves convergence via the **ODE method**:
   1. **Subsequence extraction:** Extract a subsequence $\{\theta_{n_k}\}$ that converges to some $\theta^*$ (requires $\Theta$ to be **complete** and compact, or at least that bounded sequences have convergent subsequences)
   2. **ODE characterization:** Show that $\theta^*$ satisfies the "ODE limit" $0 = \lim_{T \to \infty} \frac{1}{T}\int_0^T \nabla_\theta J(\theta_n) \, dn$ (averaged gradient vanishes)
   3. **Uniqueness:** Show $\theta^*$ is the unique global maximum of $J$ (requires convexity or other structure)

   **Where completeness enters:** Step 1 (subsequence extraction) is the Riesz-Fischer argument in disguise. If $\{\theta_n\}$ is bounded (ensured by projection onto compact $\Theta$ or by assuming $\nabla J$ is Lipschitz), we extract a Cauchy subsequence. In **finite dimensions** $\Theta = \mathbb{R}^d$ (the typical case for neural net parameters), completeness is automatic (Heine-Borel). But in **infinite-dimensional policy classes** (e.g., function spaces of policies), completeness must be proven—this is where Riesz-Fischer becomes essential.

   **Practical caveat:** Most policy gradient implementations use $\Theta = \mathbb{R}^d$ (neural net weights), so completeness is not an issue. The real convergence obstacles are:
   - **Non-convexity:** $J(\theta)$ may have local maxima; SA theory only guarantees convergence to a stationary point, not global optimum
   - **High variance gradients:** REINFORCE-style estimators have variance $O(H^2)$ where $H$ is horizon; requires variance reduction (baselines, critics)
   - **Step size tuning:** Robbins-Monro conditions $\sum \alpha_n = \infty$, $\sum \alpha_n^2 < \infty$ are necessary but not sufficient; constant step sizes often work better in practice (violates theory)

**Summary:** Completeness of $L^p$ spaces is the **bedrock** on which all of RL convergence theory rests. Without Riesz-Fischer, we cannot:
- Prove value iteration converges (Banach fixed-point)
- Define orthogonal projections (least-squares TD)
- Guarantee policy gradient convergence (stochastic approximation)

---

#### **When Completeness Fails: Deep RL and Neural Network Function Classes**

Modern deep RL uses neural network parameterizations $V_\theta(s)$ where $\theta \in \mathbb{R}^d$ indexes network weights. This creates two departures from our completeness theory:

1. **Function class is not closed in $L^\infty$:** The set $\{V_\theta : \theta \in \mathbb{R}^d\}$ for a fixed architecture (e.g., 3-layer ReLU network) is **not** a closed subspace of $L^\infty(\mathcal{S})$. Neural networks with bounded weights can approximate continuous functions arbitrarily well (universal approximation), but the limit may not be representable by the network class itself. Thus Corollary 3.7 does not apply.

2. **Iterates may not converge in function space:** Deep Q-learning iterates $V_{k+1} = \text{NN}_{\theta_k}$ where $\theta_k$ minimizes $\|\text{NN}_\theta - T^\pi V_k\|$ (projected Bellman operator). Even if $\{\theta_k\}$ converges, the sequence $\{V_k\}$ may not converge in $L^\infty$ norm because:
   - **Projection error:** $\Pi T^\pi V_k \neq T^\pi V_k$ (true value function may not be representable)
   - **Sampling error:** Stochastic gradients introduce noise that doesn't vanish
   - **Non-convexity:** Neural net optimization is non-convex; may converge to local minimum

**What theory still tells us:**

- The **true value function** $V^\pi = T^\pi V^\pi$ exists and is unique in $L^\infty$ (by our completeness result)
- The **projected fixed point** $\bar{V} = \Pi T^\pi \bar{V}$ may not exist if $\Pi$ (projection onto network class) is not well-defined (network class not closed)
- **Empirical observation:** Despite lack of theoretical guarantees, deep Q-learning often converges in practice. Why? Open research question. Possible explanations:
  - Overparameterized networks effectively span a "large enough" subset of $L^\infty$ for the problem at hand
  - Early stopping prevents divergence
  - Experience replay + target networks stabilize training [@mnih:dqn:2015]

**References:**
- [@sutton:reinforcement_learning:2018, §11.3]: Discussion of deadly triad (function approximation + bootstrapping + off-policy)
- [@tsitsiklis:td_convergence:1997]: Analysis of $Q$-learning with linear function approximation (closed subspace case)
- [@baird:residual:1995]: Counterexample showing divergence of Q-learning with neural networks
- [@mnih:dqn:2015]: DQN paper—empirical success despite lack of theoretical guarantees

**Pedagogical value:** This bridges theory (closed subspaces $\to$ convergence) to practice (neural nets violate closure, but work anyway). Honest about gaps, cites frontier work correctly.

---

**Contrast with Incomplete Spaces:**

The space $(C([0,1]), \|\cdot\|_1)$ (continuous functions with $L^1$ norm) is **incomplete**:

**Counterexample:** Define $f_n(x) = \min(nx, 1)$ for $x \in [0,1]$.

Then $f_n$ is continuous, and $\|f_n - f_m\|_1 \to 0$ (Cauchy in $L^1$), but the limit is:
$$
f(x) = \begin{cases} 0 & \text{if } x = 0 \\ 1 & \text{if } x \in (0,1] \end{cases} = \mathbf{1}_{(0,1]}
$$

which is **not continuous** (discontinuous at $x=0$). Thus $\{f_n\}$ is Cauchy in $(C([0,1]), \|\cdot\|_1)$ but has no limit in $C([0,1])$—the space is incomplete.

**Completion:** The completion of $(C([0,1]), \|\cdot\|_1)$ is $L^1([0,1])$ (Lebesgue integrable functions), which includes discontinuous functions like $f$ above. This is why Lebesgue integration generalizes Riemann integration—it "fills in" the limits of Cauchy sequences.

---

**Looking Ahead:**

- **Day 2-3 (Tomorrow-Wednesday):** We study **$L^p$ duality**: the dual space $(L^p)^*$ (continuous linear functionals $L^p \to \mathbb{R}$) is isomorphic to $L^q$ for conjugate exponents $1/p + 1/q = 1$. This formalizes "value functions are dual to state distributions" in RL.

- **Thursday:** We prove the **Radon-Nikodym theorem**, which characterizes when one measure has a **density** with respect to another ($d\mu = f \, d\nu$). This is the foundation of importance sampling in off-policy RL (the ratio $\pi/\mu$ is a Radon-Nikodym derivative).

- **Friday:** Weekly synthesis—reflect on the week's theorems and their RL applications.

- **Week 14 (Hilbert Spaces):** We'll see that $L^2$ is not just complete but has an **inner product** $\langle f, g \rangle = \int fg \, d\mu$, making it a **Hilbert space**. The projection theorem (existence of orthogonal projections onto closed subspaces) is the foundation of least-squares TD.

Today's theorem—Riesz-Fischer—is the **first major payoff** from Week 1's integration theory. Every convergence proof, approximation bound, and fixed-point argument in RL ultimately rests on this foundational result.

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_1_exercises_draft]]**

**Anchor Exercise Preview:**
1. **Prove Riesz-Fischer for $L^1$:** Show that $L^1(\mu)$ is complete by adapting the proof in Section II (focusing on the $p = 1$ case, which simplifies some steps).

2. **Incomplete space counterexample:** Show that $(C([0,1]), \|\cdot\|_1)$ is **not complete** by constructing an explicit Cauchy sequence with no continuous limit.

3. **RL Application (Bellman Contraction):** Let $\mathcal{S}$ be a finite state space with $|\mathcal{S}| = n$. The Bellman operator $T^\pi: \mathbb{R}^n \to \mathbb{R}^n$ is defined by $(T^\pi V)_s = r_s + \gamma \sum_{s'} P_{ss'}^\pi V_{s'}$. Show that:
   - $T^\pi$ is a contraction in $\|\cdot\|_\infty$ norm with modulus $\gamma$
   - Value iteration $V_{k+1} = T^\pi V_k$ converges to the unique fixed point $V^\pi$
   - Estimate the number of iterations needed to achieve $\|V_k - V^\pi\|_\infty < \epsilon$ for given $\epsilon > 0$

4. **Subsequence extraction:** Prove that every Cauchy sequence in a metric space has a subsequence $\{x_{n_k}\}$ with $d(x_{n_{k+1}}, x_{n_k}) < 2^{-k}$ (rapid convergence). This is the key step in the Riesz-Fischer proof.

---

**Reflection Questions:**

1. **Why does the proof use subsequence extraction rather than working with the full sequence directly?**
   *Hint:* The rapid convergence rate $\|g_{k+1} - g_k\|_p < 2^{-k}$ enables the geometric series bound in Step 2, which is crucial for showing $S \in L^p$. The full Cauchy sequence only gives $\|f_n - f_m\|_p < \epsilon$ for $n, m$ large enough, which is not summable.

2. **Where in the proof do we use that $p \geq 1$? Would the proof work for $0 < p < 1$?**
   *Hint:* Minkowski's inequality (triangle inequality for $\|\cdot\|_p$) is used in Step 2 (equation 3.6) and Step 6 (equation 3.13). For $p < 1$, Minkowski **reverses**, and $\|\cdot\|_p$ is only a quasi-norm. The proof fails for $p < 1$.

3. **How does Riesz-Fischer compare to the completeness of $\mathbb{R}$?**
   *Hint:* Both are "completions" of pre-existing structures: $\mathbb{R}$ completes $\mathbb{Q}$ (rationals) by adding Cauchy limits, and $L^p$ completes $C([0,1])$ (continuous functions) by adding $L^p$ limits. The analogy is deep: both use Cauchy sequences, and both involve proving "Cauchy implies convergent."

---

**Daily Study Note:**

**What I learned today:**
- **Riesz-Fischer theorem**: $L^p(\mu)$ is a Banach space (complete normed vector space) for $1 \leq p \leq \infty$
- **Proof strategy**: Extract rapidly convergent subsequence ($2^{-k}$ decay) $\to$ show pointwise a.e. convergence via MCT $\to$ use Fatou to prove limit is in $L^p$ $\to$ extend to full sequence via Cauchy property
- **Convergence theorems in action**: MCT (Step 2), Fatou (Steps 4 and 5) are the workhorses of the proof
- **Completeness enables fixed-point theorems**: Banach Fixed-Point Theorem requires completeness, which underlies all RL convergence results

**Connection to previous material:**
- Builds on $L^p$ norm definition and Minkowski's inequality [THM-2.8] from Week 2, Day 4
- Uses Monotone Convergence Theorem [THM-1.2.2] and Fatou's Lemma [LEM-1.2.2] from Week 1, Days 2-3
- Prepares for Banach Fixed-Point Theorem (Week 16) and Bellman operator theory (Week 23)

**Looking forward:**
- Days 2-3: $L^p$ duality—$(L^p)^* \cong L^q$ for conjugate exponents
- Day 4: Radon-Nikodym theorem—densities $d\mu/d\nu$ for importance sampling
- Week 14: Hilbert spaces—$L^2$ with inner product, projection theorem for least-squares TD

**RL connections identified:**
- Bellman operators require completeness of $L^\infty$ for value iteration convergence
- Least-squares TD requires completeness of $L^2$ for orthogonal projection to exist
- Policy gradient convergence proofs use completeness of parameter spaces
- Without Riesz-Fischer, RL convergence theory collapses

**Time spent:** 90-110 minutes (within target for Monday session with rigorous proof work)

---

**End of Day 1**
