[[Day 3]]

# Day 3 Exercises: Fatou's Lemma and Dominated Convergence Theorem

---

## Exercise 1: Prove that if $f_n \to f$ in $L^1$, there exists a subsequence converging almost everywhere

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

**Step 2: Apply Markov's inequality (or Chebyshev) and Borel-Cantelli.**

For each $k$ and each $\varepsilon > 0$, Markov's inequality yields:
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
Since $\sum_{k=1}^{\infty} k/2^k < \infty$ (ratio test or comparison with geometric series), we have:
$$
\sum_{k=1}^{\infty} \mu(E_k) < \infty
$$

**Step 3: Apply the Borel-Cantelli Lemma.**

By the first Borel-Cantelli lemma, if $\sum \mu(E_k) < \infty$, then:
$$
\mu\left(\limsup_{k \to \infty} E_k\right) = 0
$$
where:
$$
\limsup_{k \to \infty} E_k = \left\{x : x \in E_k \text{ for infinitely many } k\right\}
$$
The complement is:
$$
\left(\limsup_{k \to \infty} E_k\right)^c = \left\{x : x \in E_k \text{ for only finitely many } k\right\}
$$
This set has full measure, i.e., $\mu\left(\left(\limsup E_k\right)^c\right) = \mu(X)$ (up to the total measure).

**Step 4: Verify almost-everywhere convergence on the complement.**

Let $x \in \left(\limsup E_k\right)^c$. Then there exists $K$ such that for all $k \geq K$, we have $x \notin E_k$, meaning:
$$
|f_{n_k}(x) - f(x)| < \frac{1}{k}
$$
As $k \to \infty$, we have $1/k \to 0$, so $f_{n_k}(x) \to f(x)$.

Thus $f_{n_k} \to f$ pointwise on $\left(\limsup E_k\right)^c$, a set of full measure. Therefore, $f_{n_k} \to f$ $\mu$-almost everywhere. □

---

**Remark:** This result is fundamental in stochastic approximation theory. When we prove convergence of TD learning or Q-learning in $L^1$ (i.e., convergence of expected values), we can always extract an almost-surely convergent subsequence. This is often sufficient for algorithmic purposes, as almost-sure convergence implies convergence in probability, which is the relevant mode for sample-based algorithms.

---

## Exercise 2: Construct explicit counterexamples showing necessity of each hypothesis in MCT and DCT

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
- **Integrals:** $\int f_n = 0$ if $n$ is odd, and $\int f_n = 2$ if $n$ is even. Thus $\int f_n$ does not converge.

**Conclusion:** MCT requires monotonicity; without it, neither the pointwise limit nor the limit of integrals need exist.

---

### **Counterexample 2: DCT Fails Without Pointwise Convergence (The Sliding Bump)**

**Setup:** $([0, 1], \mathcal{B}([0,1]), \lambda)$.

**Construction:** Define:
$$
f_n(x) = n \cdot \mathbf{1}_{\left[\frac{k}{n}, \frac{k+1}{n}\right]}(x)
$$
where $k = (n \mod n)$, or more simply, let the bump "slide" across $[0, 1]$. A cleaner construction:

For $n = 1, 2, 3, \ldots$, write $n = 2^k + j$ where $0 \leq j < 2^k$ (i.e., decompose $n$ into levels of a binary tree). Define:
$$
f_n = 2^{k+1} \cdot \mathbf{1}_{I_{k,j}}
$$
where $I_{k,j} = [j/2^k, (j+1)/2^k]$ is the $j$-th dyadic interval at level $k$.

**Properties:**
- **No pointwise limit:** For any $x \in [0, 1]$, the sequence $f_n(x)$ takes the value $2^{k+1}$ when $n$ corresponds to an interval $I_{k,j}$ containing $x$, and 0 otherwise. Since $x$ is contained in infinitely many dyadic intervals (one at each level $k$), the sequence $f_n(x)$ is unbounded and does not converge.
- **Domination fails:** There is no integrable function $g$ with $|f_n| \leq g$ for all $n$, because $f_n$ can be arbitrarily large (heights $2^{k+1} \to \infty$ as $k \to \infty$).
- **Integrals:** $\int f_n = 2^{k+1} \cdot (1/2^k) = 2$ for all $n$, so $\int f_n = 2 \to 2$. But there is no limit function $f$ with $\int f = 2$ and $f_n \to f$ pointwise.

**Better Counterexample (Simpler):** The **Typewriter Sequence** (mentioned in Day 3 notes).

On $([0, 1], \mathcal{B}([0,1]), \lambda)$, enumerate all dyadic intervals of the form $[k/2^n, (k+1)/2^n]$ for $n = 0, 1, 2, \ldots$ and $k = 0, 1, \ldots, 2^n - 1$. Label them as $I_1, I_2, I_3, \ldots$. Define:
$$
f_n = \mathbf{1}_{I_n}
$$

**Properties:**
- **Bounded:** $|f_n| \leq 1$ for all $n$, so the sequence is dominated by the constant function $g = 1$, which is integrable on $[0, 1]$.
- **No pointwise convergence:** For any $x \in [0, 1]$, the point $x$ is contained in infinitely many dyadic intervals (at least one per level), so $f_n(x) = 1$ infinitely often. But $x$ is also excluded from infinitely many intervals, so $f_n(x) = 0$ infinitely often. Thus $f_n(x)$ oscillates and does not converge.
- **Integrals:** $\int f_n = \text{length}(I_n) = 1/2^{k_n}$ where $k_n$ is the level of $I_n$. As $n \to \infty$, the enumeration visits finer and finer levels, so $\int f_n \to 0$.

**Conclusion:** Even with domination, DCT fails if pointwise convergence does not hold. The sequence $\{f_n\}$ has no pointwise limit, so the conclusion $\int f_n \to \int f$ is vacuous.

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
  - If $x > 0$, then for $n > x$, we have $f_n(x) = 1/n \to 0$.

  Thus $f_n \to 0$ pointwise.

- **Integrals:**
  $$
  \int f_n \, d\lambda = \frac{1}{n} \cdot \lambda([0, n]) = \frac{1}{n} \cdot n = 1
  $$
  So $\int f_n = 1$ for all $n$, which does not converge to $\int 0 = 0$.

- **No dominating function:** Suppose there exists an integrable $g: \mathbb{R} \to [0, \infty)$ with $|f_n(x)| \leq g(x)$ for all $n$ and all $x$. For any $x \in (0, \infty)$, we can choose $n$ large enough that $x \in [0, n]$, so:
  $$
  \frac{1}{n} \leq g(x)
  $$
  As $n \to \infty$, this forces $g(x) \geq 0$ for all $x > 0$, but imposes no lower bound. However, for any fixed $x > 0$, the supremum $\sup_{n} f_n(x) = \sup_{n > x} (1/n) = 1/\lceil x \rceil$. Actually, let's reconsider:

  For $g$ to dominate all $f_n$, we need $g(x) \geq f_n(x)$ for all $n$. For $x \in (0, \infty)$, the value $f_n(x) = 1/n$ for $n \geq x$. The supremum over all $n$ is $\sup_{n \geq x} (1/n)$, which is achieved at $n = \lceil x \rceil$, giving $f_{\lceil x \rceil}(x) = 1/\lceil x \rceil$. So:
  $$
  g(x) \geq \frac{1}{\lceil x \rceil}
  $$
  But then:
  $$
  \int_{[1, \infty)} g \, d\lambda \geq \int_{[1, \infty)} \frac{1}{\lceil x \rceil} \, d\lambda \geq \sum_{k=1}^{\infty} \int_{[k, k+1)} \frac{1}{k+1} \, d\lambda = \sum_{k=1}^{\infty} \frac{1}{k+1} = \infty
  $$
  (The sum diverges as the harmonic series.) Thus $g$ is not integrable.

**Conclusion:** Pointwise convergence alone is insufficient for DCT. Without domination, the "mass" of the functions $f_n$ can escape to infinity (here, the support $[0, n]$ grows), causing $\int f_n$ to diverge even when $f_n \to 0$ pointwise.

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

## Exercise 3: Prove the Monotone Class Theorem for Functions (π-λ for Functions)

**Statement (Monotone Class Theorem for Functions):**
Let $\mathcal{A}$ be an algebra of subsets of $X$, and let $\mathcal{H}$ be a collection of bounded real-valued functions on $X$ satisfying:
1. **Contains indicators of $\mathcal{A}$:** $\mathbf{1}_A \in \mathcal{H}$ for all $A \in \mathcal{A}$.
2. **Closed under linear combinations:** If $f, g \in \mathcal{H}$ and $a, b \in \mathbb{R}$, then $af + bg \in \mathcal{H}$.
3. **Closed under monotone limits:** If $\{f_n\} \subseteq \mathcal{H}$ with $0 \leq f_n \uparrow f$ pointwise and $f$ is bounded, then $f \in \mathcal{H}$.

Then $\mathcal{H}$ contains all bounded $\sigma(\mathcal{A})$-measurable functions.

---

**Proof Strategy (Outline):**

This theorem is a functional version of the Dynkin π-λ theorem. It is used constantly in probability to prove that certain properties (e.g., integrability, measurability) hold for all bounded measurable functions by verifying them only on indicators of a generating algebra.

**Step 1:** Show that $\mathcal{H}$ contains all bounded $\mathcal{A}$-simple functions.

By hypothesis (1), $\mathbf{1}_A \in \mathcal{H}$ for all $A \in \mathcal{A}$. Since $\mathcal{A}$ is an algebra, finite disjoint unions and complements are in $\mathcal{A}$. Any simple function:
$$
\varphi = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}
$$
with $A_i \in \mathcal{A}$ can be written as a linear combination of indicators in $\mathcal{H}$. By hypothesis (2), $\varphi \in \mathcal{H}$.

**Step 2:** Extend to all bounded $\sigma(\mathcal{A})$-measurable functions via approximation.

Let $f: X \to \mathbb{R}$ be bounded and $\sigma(\mathcal{A})$-measurable, say $|f| \leq M$. By the standard approximation theorem for measurable functions (see Folland, Theorem 2.10), there exists a sequence of simple functions $\varphi_n$ such that $\varphi_n \to f$ pointwise. We can construct this sequence to be increasing:
$$
\varphi_n = M \cdot \sum_{k=1}^{n \cdot 2^n} \frac{k-1}{2^n} \mathbf{1}_{\{x : (k-1)/2^n \leq f(x) < k/2^n\}}
$$
(This is a standard dyadic approximation; see Day 2 notes for details.)

Each set $\{x : (k-1)/2^n \leq f(x) < k/2^n\} = f^{-1}([(k-1)/2^n, k/2^n))$ is in $\sigma(\mathcal{A})$ by measurability of $f$. However, we need these sets to be in $\mathcal{A}$, not just $\sigma(\mathcal{A})$.

**Issue:** The sets in the dyadic partition are $\sigma(\mathcal{A})$-measurable but not necessarily in $\mathcal{A}$. To resolve this, we use a different approach:

**Alternate Step 2 (Correct Approach):**

By the Monotone Class Theorem for sets (Dynkin π-λ, Exercise from Day 1), we know that $\sigma(\mathcal{A})$ is the smallest monotone class containing $\mathcal{A}$. We need to translate this to functions.

Define:
$$
\mathcal{M} = \left\{A \subseteq X : \mathbf{1}_A \in \mathcal{H}\right\}
$$
We will show that $\mathcal{M}$ is a monotone class containing $\mathcal{A}$, hence $\sigma(\mathcal{A}) \subseteq \mathcal{M}$.

**Substep 2.1:** $\mathcal{A} \subseteq \mathcal{M}$ by hypothesis (1).

**Substep 2.2:** $\mathcal{M}$ is closed under increasing limits.
Let $A_n \in \mathcal{M}$ with $A_n \uparrow A$. Then $\mathbf{1}_{A_n} \in \mathcal{H}$ for all $n$, and $\mathbf{1}_{A_n} \uparrow \mathbf{1}_A$ pointwise. By hypothesis (3), $\mathbf{1}_A \in \mathcal{H}$, so $A \in \mathcal{M}$.

**Substep 2.3:** $\mathcal{M}$ is closed under decreasing limits.
Let $A_n \in \mathcal{M}$ with $A_n \downarrow A$. Then $A_n^c \uparrow A^c$. We need to show $A_n^c \in \mathcal{M}$ first.

Since $\mathcal{A}$ is an algebra, it is closed under complements. We need to verify that $\mathcal{M}$ is closed under complements. For $A \in \mathcal{M}$, we have $\mathbf{1}_A \in \mathcal{H}$. Then:
$$
\mathbf{1}_{A^c} = \mathbf{1}_X - \mathbf{1}_A
$$
By hypothesis (2), $\mathcal{H}$ is closed under linear combinations. If $\mathbf{1}_X \in \mathcal{H}$ (which follows from $X \in \mathcal{A}$ by hypothesis (1)), then $\mathbf{1}_{A^c} \in \mathcal{H}$, so $A^c \in \mathcal{M}$.

Now, $A_n \downarrow A$ implies $A_n^c \uparrow A^c$. By Substep 2.2, $A^c \in \mathcal{M}$, so $A = (A^c)^c \in \mathcal{M}$.

**Substep 2.4:** Conclusion from Monotone Class Theorem for sets.
We have shown that $\mathcal{M}$ is a monotone class containing the algebra $\mathcal{A}$. By the Dynkin π-λ theorem, $\sigma(\mathcal{A}) \subseteq \mathcal{M}$. Thus $\mathbf{1}_A \in \mathcal{H}$ for all $A \in \sigma(\mathcal{A})$.

**Step 3:** Extend to bounded $\sigma(\mathcal{A})$-measurable functions.

Any bounded $\sigma(\mathcal{A})$-measurable function $f$ can be approximated by simple functions $\varphi_n = \sum a_i \mathbf{1}_{A_i}$ with $A_i \in \sigma(\mathcal{A})$. By Step 2, $\mathbf{1}_{A_i} \in \mathcal{H}$, so by hypothesis (2), $\varphi_n \in \mathcal{H}$. If we construct $\varphi_n$ to increase to $f$ (which is always possible; see dyadic approximation), then by hypothesis (3), $f \in \mathcal{H}$. □

---

**Remark (Why This Theorem Matters for RL):**

The Monotone Class Theorem for Functions is the workhorse for proving that integrals and expectations have certain properties. For example, to show that a certain operation (e.g., conditional expectation) is well-defined for all bounded measurable functions, we:
1. Verify it for indicators of a generating algebra $\mathcal{A}$.
2. Check that the collection of functions for which it holds satisfies the three hypotheses.
3. Conclude it holds for all bounded $\sigma(\mathcal{A})$-measurable functions.

In Week 6, we will use this theorem to prove uniqueness of conditional expectation. In Week 25, it will reappear in proving properties of the Bellman operator on general measurable spaces.

---

**End of Day 3 Exercises**
