[[Day 3]]

# Day 3 Exercises: Fatou's Lemma and Dominated Convergence Theorem

---

## Exercise 1: Prove that if $f_n \to f$ in $L^1$, there exists a subsequence converging almost everywhere {#EX-1.3.3}

**Statement:** Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^{\infty}$ be a sequence of measurable functions such that $f_n \to f$ in $L^1$, i.e.:
$$
\lim_{n \to \infty} \int |f_n - f| \, d\mu = 0
$$
Prove that there exists a subsequence $\{f_{n_k}\}$ such that $f_{n_k}(x) \to f(x)$ for $\mu$-almost every $x \in X$.

---

*Proof.*

**Step 1: Extract a rapidly converging subsequence.**

By the definition of $L^1$ convergence, for each $k \in \mathbb{N}$, there exists $n_k \in \mathbb{N}$ such that:
$$
\int |f_{n_k} - f| \, d\mu < \frac{1}{2^k}
$$
We may assume without loss of generality that the sequence $\{n_k\}$ is strictly increasing (if not, we can always choose a larger $n_k$ satisfying the inequality). Thus $\{f_{n_k}\}$ is a subsequence of $\{f_n\}$ with the property:
$$
\sum_{k=1}^{\infty} \int |f_{n_k} - f| \, d\mu < \sum_{k=1}^{\infty} \frac{1}{2^k} = 1 < \infty
$$

**Step 2: Apply Markov's inequality and Borel-Cantelli.**

For each $k$ and each $\varepsilon > 0$, Markov's inequality [@durrett:probability:2019, §1.6] (which states that for a non-negative random variable $X$ and $a > 0$, $\mathbb{P}(X \geq a) \leq \mathbb{E}[X]/a$, or in measure-theoretic form: $\mu(\{x : g(x) \geq a\}) \leq \frac{1}{a} \int g \, d\mu$ for $g \geq 0$) yields:
$$
\mu\left(\left\{x : |f_{n_k}(x) - f(x)| \geq \varepsilon\right\}\right) \leq \frac{1}{\varepsilon} \int |f_{n_k} - f| \, d\mu < \frac{1}{\varepsilon \cdot 2^k}
$$
Define the sets:
$$
E_k = \left\{x : |f_{n_k}(x) - f(x)| \geq \frac{1}{k}\right\}
$$
Then:
$$
\mu(E_k) \leq k \int |f_{n_k} - f| \, d\mu < \frac{k}{2^k}
$$
Since $\sum_{k=1}^{\infty} k/2^k < \infty$ (this series converges by the ratio test: $\frac{(k+1)/2^{k+1}}{k/2^k} = \frac{k+1}{2k} \to \frac{1}{2} < 1$), we have:
$$
\sum_{k=1}^{\infty} \mu(E_k) < \infty
$$

**Step 3: Apply the Borel-Cantelli Lemma.**

By the first Borel-Cantelli lemma [@durrett:probability:2019, §2.3] (which states: if $\{E_k\}$ is a sequence of measurable sets with $\sum_{k=1}^{\infty} \mu(E_k) < \infty$, then $\mu(\limsup_{k \to \infty} E_k) = 0$), we have:
$$
\mu\left(\limsup_{k \to \infty} E_k\right) = 0
$$
where:
$$
\limsup_{k \to \infty} E_k = \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} E_k = \left\{x : x \in E_k \text{ for infinitely many } k\right\}
$$
The complement is:
$$
\left(\limsup_{k \to \infty} E_k\right)^c = \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} E_k^c = \left\{x : x \in E_k \text{ for only finitely many } k\right\}
$$
This set has full measure: $\mu\left(\left(\limsup E_k\right)^c\right) = \mu(X) - \mu\left(\limsup E_k\right) = \mu(X) - 0$.

**Step 4: Verify almost-everywhere convergence on the complement.**

Let $x \in \left(\limsup E_k\right)^c$. Then there exists $K$ such that for all $k \geq K$, we have $x \notin E_k$, meaning:
$$
|f_{n_k}(x) - f(x)| < \frac{1}{k}
$$
As $k \to \infty$, we have $1/k \to 0$, so $f_{n_k}(x) \to f(x)$.

Thus $f_{n_k} \to f$ pointwise on $\left(\limsup E_k\right)^c$, a set of full measure. Therefore, $f_{n_k} \to f$ $\mu$-almost everywhere. □

---

**Remark (RL Relevance):** This result is fundamental in stochastic approximation theory. When we prove convergence of TD learning or Q-learning in $L^1$ (i.e., convergence of expected values $\mathbb{E}[\|\theta_n - \theta^*\|] \to 0$), we can always extract an almost-surely convergent subsequence. Almost-sure convergence implies convergence in probability, which is the relevant mode for sample-based algorithms. Thus, proving $L^1$ convergence is often sufficient for algorithmic purposes—a weaker result that is often easier to establish than full almost-sure convergence of the entire sequence.

---

## Exercise 2: Construct explicit counterexamples showing necessity of each hypothesis in MCT and DCT {#EX-1.3.4}

We construct three counterexamples demonstrating that:
1. MCT fails without monotonicity
2. DCT fails without pointwise convergence
3. DCT fails without domination

---

### **Counterexample 1: MCT Fails Without Monotonicity**

**Setup:** Let $(X, \mathcal{F}, \mu) = ([0, 1], \mathcal{B}([0,1]), \lambda)$, where $\lambda$ is Lebesgue measure.

**Construction:** Define:
$$
f_n(x) = \begin{cases}
2 & \text{if } n \text{ is even} \\
0 & \text{if } n \text{ is odd}
\end{cases}
$$
Then:
- **Non-monotone:** The sequence oscillates: $f_1 = 0, f_2 = 2, f_3 = 0, f_4 = 2, \ldots$, so neither $f_n \uparrow$ nor $f_n \downarrow$.
- **Pointwise limit does not exist:** For any $x \in [0, 1]$, the sequence $f_n(x)$ oscillates between 0 and 2, so $\lim_{n \to \infty} f_n(x)$ does not exist.
- **Integrals:** $\int f_n \, d\lambda = 0$ if $n$ is odd, and $\int f_n \, d\lambda = 2$ if $n$ is even. Thus $\int f_n$ does not converge.

**Conclusion:** MCT requires monotonicity; without it, neither the pointwise limit nor the limit of integrals need exist.

---

### **Counterexample 2: DCT Fails Without Pointwise Convergence (The Typewriter Sequence)**

**Setup:** $([0, 1], \mathcal{B}([0,1]), \lambda)$.

**Construction:** Enumerate all dyadic intervals by level, then left-to-right within each level:
- Level 0: $I_1 = [0, 1]$
- Level 1: $I_2 = [0, 1/2]$, $I_3 = [1/2, 1]$
- Level 2: $I_4 = [0, 1/4]$, $I_5 = [1/4, 1/2]$, $I_6 = [1/2, 3/4]$, $I_7 = [3/4, 1]$
- Level $k$: $2^k$ intervals of length $1/2^k$

Define $f_n = \mathbf{1}_{I_n}$.

**Properties:**
- **Bounded:** $|f_n| \leq 1$ for all $n$, so the sequence is dominated by the constant function $g(x) \equiv 1$, which is integrable on $[0, 1]$ (note: here $g(x) \equiv 1$ denotes the function that is constantly 1, with $\int g \, d\lambda = 1 < \infty$).

- **No pointwise convergence:** For any $x \in [0, 1]$, the point $x$ is contained in infinitely many dyadic intervals (exactly one at each level $k = 0, 1, 2, \ldots$). Thus $f_n(x) = 1$ infinitely often. But $x$ is also excluded from the other intervals at each level, so $f_n(x) = 0$ infinitely often. The sequence $f_n(x)$ oscillates between 0 and 1 and does not converge anywhere.

- **Integrals:** $\int f_n \, d\lambda = \lambda(I_n) = 1/2^{k_n}$ where $k_n$ is the level of interval $I_n$. As $n \to \infty$, the enumeration visits finer and finer levels, so $k_n \to \infty$, hence $\int f_n \to 0$.

**Conclusion:** Even with domination, DCT fails if pointwise convergence does not hold. The sequence $\{f_n\}$ has no pointwise limit, so the conclusion $\int f_n \to \int f$ is vacuous (there is no limit function $f$).

---

### **Counterexample 3: DCT Fails Without Domination (Escaping Mass)**

**Setup:** $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$.

**Construction:** Define:
$$
f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x)
$$

**Properties:**
- **Pointwise convergence:** For any $x \in \mathbb{R}$:
  - If $x \leq 0$, then $f_n(x) = 0$ for all $n$, so $f_n(x) \to 0$.
  - If $x > 0$, then for all $n > x$, we have $x \in [0, n]$, so $f_n(x) = 1/n \to 0$.

  Thus $f_n \to 0$ pointwise everywhere.

- **Integrals:**
  $$
  \int f_n \, d\lambda = \frac{1}{n} \cdot \lambda([0, n]) = \frac{1}{n} \cdot n = 1
  $$
  So $\int f_n = 1$ for all $n$, which does not converge to $\int 0 \, d\lambda = 0$.

- **No dominating function:** Suppose there exists an integrable $g: \mathbb{R} \to [0, \infty)$ with $|f_n(x)| \leq g(x)$ for all $n$ and all $x$. For any $x \in (0, \infty)$ and any $n \geq \lceil x \rceil$, we have $x \in [0, n]$, so $f_n(x) = 1/n$. Thus for $g$ to dominate all $f_n$, we need:
  $$
  g(x) \geq \sup_{n \geq \lceil x \rceil} f_n(x) = \sup_{n \geq \lceil x \rceil} \frac{1}{n} = \frac{1}{\lceil x \rceil}
  $$
  for all $x > 0$. Then:
  $$
  \begin{align}
  \int_{[1, \infty)} g \, d\lambda &\geq \int_{[1, \infty)} \frac{1}{\lceil x \rceil} \, d\lambda \\
  &\geq \sum_{k=1}^{\infty} \int_{k}^{k+1} \frac{1}{\lceil x \rceil} \, dx \\
  &= \sum_{k=1}^{\infty} \int_{k}^{k+1} \frac{1}{k+1} \, dx \quad \text{[since } \lceil x \rceil = k+1 \text{ for } x \in [k, k+1)\text{]} \\
  &= \sum_{k=1}^{\infty} \frac{1}{k+1} \cdot 1 \\
  &= \sum_{k=2}^{\infty} \frac{1}{k} = \infty
  \end{align}
  $$
  (The sum diverges as the harmonic series.) Thus $g$ is not integrable.

**Conclusion:** Pointwise convergence alone is insufficient for DCT. Without domination, the "mass" of the functions $f_n$ can escape to infinity (here, the support $[0, n]$ grows unboundedly), causing $\int f_n$ to diverge even when $f_n \to 0$ pointwise.

---

**Remark (Synthesis):** These three counterexamples demonstrate that:
1. **MCT** is sharp: monotonicity + non-negativity ⟹ limit interchange, but non-negativity alone is insufficient (oscillating sequences fail).
2. **DCT hypothesis 1** (pointwise convergence) is necessary: domination alone does not prevent oscillation (Typewriter Sequence).
3. **DCT hypothesis 2** (domination) is necessary: pointwise convergence alone does not prevent mass escape (Escaping Mass).

In RL theory, these counterexamples inform our proof strategy:
- **Boundedness of rewards and value functions** ensures domination.
- **Convergence theorems for iterative algorithms** (contraction mappings, stochastic approximation) ensure pointwise convergence.
- Together, they allow us to invoke DCT to conclude that expectations converge.

---

## Exercise 3: Prove the Monotone Class Theorem for Functions (π-λ for Functions) {#THM-1.3.3}

**Motivation:** In §1.6 (conditional expectation) and Week 25 (Bellman operators on general state spaces), we will need to verify properties for all bounded measurable functions. Checking every such function is impossible; the Monotone Class Theorem reduces this to verifying the property on indicators of a generating algebra. This is the functional analyst's version of Dynkin's π-λ system—a tool for extending results from simple sets to all measurable sets via function approximation.

**Statement (Monotone Class Theorem for Functions):**
Let $\mathcal{A}$ be an algebra of subsets of $X$, and let $\mathcal{H}$ be a collection of bounded real-valued functions on $X$ satisfying:
1. **Contains indicators of $\mathcal{A}$:** $\mathbf{1}_A \in \mathcal{H}$ for all $A \in \mathcal{A}$.
2. **Closed under linear combinations:** If $f, g \in \mathcal{H}$ and $a, b \in \mathbb{R}$, then $af + bg \in \mathcal{H}$.
3. **Closed under monotone limits:** If $\{f_n\} \subseteq \mathcal{H}$ with $0 \leq f_n \uparrow f$ pointwise and $f$ is bounded, then $f \in \mathcal{H}$.

Then $\mathcal{H}$ contains all bounded $\sigma(\mathcal{A})$-measurable functions.

---

**Proof.**

**Step 1:** Show that $\mathcal{H}$ contains all bounded $\mathcal{A}$-simple functions.

By hypothesis (1), $\mathbf{1}_A \in \mathcal{H}$ for all $A \in \mathcal{A}$. Since $\mathcal{A}$ is an algebra, it is closed under finite unions, intersections, and complements. Any simple function:
$$
\varphi = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}
$$
with $A_i \in \mathcal{A}$ and $a_i \in \mathbb{R}$ can be written as a linear combination of indicators in $\mathcal{H}$. By hypothesis (2), $\varphi \in \mathcal{H}$.

**Step 2:** Show that the collection of sets whose indicators are in $\mathcal{H}$ forms a σ-algebra.

Define:
$$
\mathcal{M} = \left\{A \subseteq X : \mathbf{1}_A \in \mathcal{H}\right\}
$$
We will show that $\mathcal{M}$ is a monotone class containing the algebra $\mathcal{A}$, hence $\sigma(\mathcal{A}) \subseteq \mathcal{M}$ by the Dynkin π-λ theorem (Day 1, Exercise 3).

**Substep 2.1:** $\mathcal{A} \subseteq \mathcal{M}$ by hypothesis (1).

**Substep 2.2:** $\mathcal{M}$ is closed under complements.

For $A \in \mathcal{M}$, we have $\mathbf{1}_A \in \mathcal{H}$. Since $\mathcal{A}$ is an algebra, $X \in \mathcal{A}$ (by definition of algebra: $X$ and $\emptyset$ are in $\mathcal{A}$), so $\mathbf{1}_X \in \mathcal{H}$ by hypothesis (1). Then:
$$
\mathbf{1}_{A^c} = \mathbf{1}_X - \mathbf{1}_A
$$
By hypothesis (2), $\mathcal{H}$ is closed under linear combinations, so $\mathbf{1}_{A^c} \in \mathcal{H}$. Thus $A^c \in \mathcal{M}$.

**Substep 2.3:** $\mathcal{M}$ is closed under increasing limits.

Let $A_n \in \mathcal{M}$ with $A_n \uparrow A$ (i.e., $A_1 \subseteq A_2 \subseteq \cdots$ and $\bigcup_{n=1}^{\infty} A_n = A$). Then $\mathbf{1}_{A_n} \in \mathcal{H}$ for all $n$, and $\mathbf{1}_{A_n} \uparrow \mathbf{1}_A$ pointwise. Since $0 \leq \mathbf{1}_{A_n} \leq 1$ and $\mathbf{1}_A$ is bounded, hypothesis (3) implies $\mathbf{1}_A \in \mathcal{H}$, so $A \in \mathcal{M}$.

**Substep 2.4:** $\mathcal{M}$ is closed under decreasing limits.

Let $A_n \in \mathcal{M}$ with $A_n \downarrow A$ (i.e., $A_1 \supseteq A_2 \supseteq \cdots$ and $\bigcap_{n=1}^{\infty} A_n = A$). Then $A_n^c \uparrow A^c$. By Substep 2.2, $A_n^c \in \mathcal{M}$ for all $n$. By Substep 2.3, $A^c \in \mathcal{M}$. By Substep 2.2 again, $A = (A^c)^c \in \mathcal{M}$.

**Substep 2.5:** Conclusion from Monotone Class Theorem for sets.

We have shown that $\mathcal{M}$ is a monotone class (closed under increasing and decreasing limits) containing the algebra $\mathcal{A}$. By the Dynkin π-λ theorem (Day 1, Exercise 3: if a monotone class contains an algebra $\mathcal{A}$, then it contains $\sigma(\mathcal{A})$), we have $\sigma(\mathcal{A}) \subseteq \mathcal{M}$. Thus $\mathbf{1}_A \in \mathcal{H}$ for all $A \in \sigma(\mathcal{A})$.

**Step 3:** Extend to all bounded $\sigma(\mathcal{A})$-measurable functions.

Let $f: X \to \mathbb{R}$ be bounded and $\sigma(\mathcal{A})$-measurable, say $|f| \leq M$ for some $M > 0$. By the standard approximation theorem for measurable functions [@folland:real_analysis:1999, Thm 2.10]; or see Day 2 notes for the dyadic approximation construction), there exists a sequence of simple functions $\varphi_n$ such that $\varphi_n \to f$ pointwise. We can construct this sequence to be increasing and bounded:

For each $n \in \mathbb{N}$, partition the range $[-M, M]$ into dyadic intervals of length $2M/2^n$:
$$
\varphi_n(x) = \sum_{k=-n \cdot 2^n}^{n \cdot 2^n - 1} \frac{k \cdot 2M}{2^n} \mathbf{1}_{A_{n,k}}(x)
$$
where:
$$
A_{n,k} = f^{-1}\left(\left[\frac{k \cdot 2M}{2^n}, \frac{(k+1) \cdot 2M}{2^n}\right)\right) \in \sigma(\mathcal{A})
$$
(The sets $A_{n,k}$ are in $\sigma(\mathcal{A})$ by measurability of $f$.) Then $\varphi_n$ is a simple function with $\varphi_n \uparrow f$ pointwise and $|\varphi_n| \leq M$.

Each set $A_{n,k} \in \sigma(\mathcal{A})$, so by Step 2, $\mathbf{1}_{A_{n,k}} \in \mathcal{H}$. By hypothesis (2), $\varphi_n \in \mathcal{H}$ (as a linear combination of indicators in $\mathcal{H}$).

Now, to apply hypothesis (3), we need a non-negative increasing sequence. Write $f = f^+ - f^-$ where $f^+ = \max(f, 0)$ and $f^- = \max(-f, 0)$. By the argument above, there exist simple functions $\varphi_n^+ \uparrow f^+$ and $\varphi_n^- \uparrow f^-$ with $\varphi_n^+, \varphi_n^- \in \mathcal{H}$. By hypothesis (3), $f^+, f^- \in \mathcal{H}$. By hypothesis (2), $f = f^+ - f^- \in \mathcal{H}$. □

---

**Remark (Why This Theorem Matters for RL):**

The Monotone Class Theorem for Functions is the workhorse for proving that integrals and expectations have certain properties. For example, to show that a certain operation (e.g., conditional expectation, or properties of the Bellman operator) is well-defined for all bounded measurable functions, we:
1. Verify it for indicators of a generating algebra $\mathcal{A}$.
2. Check that the collection of functions for which it holds satisfies the three hypotheses.
3. Conclude it holds for all bounded $\sigma(\mathcal{A})$-measurable functions.

In Week 6, we will use this theorem to prove uniqueness of conditional expectation. In Week 25, it will reappear in proving properties of the Bellman operator on general measurable state spaces. This is the bridge from finite/discrete MDPs (where $\mathcal{S}$ is countable and every function is measurable) to continuous state spaces (where $\mathcal{S} = \mathbb{R}^n$ and measurability is non-trivial)—a central tool in the theoretical foundations of RL.

**Concrete RL application:** When proving that the Bellman operator $T^\pi: \mathcal{B}(\mathcal{S}) \to \mathcal{B}(\mathcal{S})$ (mapping bounded measurable functions to bounded measurable functions) is well-defined on a continuous state space $\mathcal{S} = \mathbb{R}^n$, we:
1. Verify $T^\pi$ is well-defined for indicators $\mathbf{1}_A$ where $A$ are Borel sets
2. Show $T^\pi$ preserves linear combinations (linearity of expectation)
3. Show $T^\pi$ preserves monotone limits (by Monotone Convergence Theorem applied to the expectation)
4. Conclude by Monotone Class Theorem that $T^\pi$ is well-defined for all bounded measurable value functions $V: \mathbb{R}^n \to \mathbb{R}$

This is precisely how Puterman (1994, §4.3-4.5) establishes existence and uniqueness of value functions for MDPs with uncountable state spaces.

---

**End of Day 3 Exercises**
