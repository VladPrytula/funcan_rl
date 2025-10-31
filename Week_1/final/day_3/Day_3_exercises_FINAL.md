[[Day_3_FINAL#]]

# Day 3 Exercises (FINAL_V2): Fatou's Lemma and Dominated Convergence Theorem

---

## Exercise 1: If $f_n \to f$ in $L^1$, then a subsequence converges almost everywhere {#EX-1.3.3}

**Statement.** Let $(X, \mathcal{F}, \mu)$ be a measure space. If $\{f_n\}$ are measurable and $\int |f_n - f| \, d\mu \to 0$, then there exists a subsequence $\{f_{n_k}\}$ with $f_{n_k}(x) \to f(x)$ for $\mu$‑almost every $x \in X$.

*Proof.* For each $k \in \mathbb{N}$, pick $n_k$ so that $\int |f_{n_k} - f| \, d\mu < 2^{-k}$. By Markov’s inequality, for $\varepsilon = 1/k$,
$$
\mu\big\{ |f_{n_k} - f| \ge 1/k \big\} \le k \int |f_{n_k} - f| \, d\mu \le k\, 2^{-k}.
$$
Since $\sum_k k\,2^{-k} < \infty$, the first Borel–Cantelli lemma implies $\mu(\limsup_k \{ |f_{n_k} - f| \ge 1/k \}) = 0$. Hence, outside a null set, only finitely many of these events occur, and therefore $f_{n_k}(x) \to f(x)$ for $\mu$‑a.e. $x$. □

---

## Exercise 2: Counterexamples showing necessity of hypotheses in MCT and DCT {#EX-1.3.4}

We construct three counterexamples demonstrating that:
1) MCT fails without monotonicity; 2) DCT fails without pointwise convergence; 3) DCT fails without domination.

### Counterexample 1: MCT Fails Without Monotonicity
On $([0,1], \mathcal{B}, \lambda)$, set $f_n \equiv 0$ for odd $n$ and $f_n \equiv 2$ for even $n$. Then $\{f_n\}$ is not monotone, no pointwise limit exists, and $\int f_n$ does not converge.

### Counterexample 2: DCT Fails Without Pointwise Convergence (Typewriter)
On $([0,1], \mathcal{B}, \lambda)$, enumerate dyadic intervals by level and set $f_n = \mathbf{1}_{I_n}$. Then $|f_n| \le 1$ and $\int f_n \to 0$, but for every $x$, the sequence $f_n(x)$ visits 0 and 1 infinitely many times; no pointwise limit exists.

### Counterexample 3: DCT Fails Without Domination (Escaping Mass)
On $(\mathbb{R}, \mathcal{B}, \lambda)$, set $f_n(x) = \frac{1}{n} \, \mathbf{1}_{[0,n]}(x)$. Then $f_n \to 0$ pointwise, yet $\int f_n \, d\lambda = 1$ for all $n$. Any dominator must satisfy $g(x) \ge 1/\lceil x \rceil$ for $x>0$, giving $\int_{[1,\infty)} g \, d\lambda = \infty$; no integrable dominator exists.

---

## Exercise 3: Monotone Class Theorem for Functions (π–λ for Functions), corrected and complete {#THM-1.3.3}

**Motivation.** We seek to extend a property $\mathsf{P}$ from indicators $\{\mathbf{1}_A : A \in \mathcal{A}\}$ to all bounded $\sigma(\mathcal{A})$‑measurable $f$. The correct mechanism is the functional analogue of the monotone‑class method: linear closure and monotone‑limit closure for nonnegative bounded sequences are the functional surrogates of “finite additivity” and “closure under increasing unions.”

**Theorem (Monotone Class Theorem for Functions).** Let $\mathcal{A}$ be an algebra of subsets of $X$, and let $\mathcal{H}$ be a collection of bounded real‑valued functions on $X$ satisfying:
1) (Indicators on $\mathcal{A}$) $\mathbf{1}_A \in \mathcal{H}$ for all $A \in \mathcal{A}$.
2) (Linear closure) If $f, g \in \mathcal{H}$ and $a,b \in \mathbb{R}$, then $af + bg \in \mathcal{H}$.
3) (Monotone limits, nonnegative) If $0 \le f_n \uparrow f$ pointwise with $f$ bounded and $f_n \in \mathcal{H}$, then $f \in \mathcal{H}$.

Then $\mathcal{H}$ contains all bounded $\sigma(\mathcal{A})$‑measurable functions.

*Proof.*

**Step 1 (Simple functions over $\mathcal{A}$).** By (1)–(2), $\mathcal{H}$ contains all bounded $\mathcal{A}$‑simple functions $\sum_i a_i \, \mathbf{1}_{A_i}$, with $A_i \in \mathcal{A}$.

**Step 2 (Set‑theoretic bridge via a monotone class).** Define $\mathcal{M} := \{A \subseteq X : \mathbf{1}_A \in \mathcal{H}\}$. Then $\mathcal{A} \subseteq \mathcal{M}$; $\mathcal{M}$ is closed under complements (since $\mathbf{1}_{A^c} = \mathbf{1}_X - \mathbf{1}_A$ and $\mathbf{1}_X \in \mathcal{H}$ by (1)) and under increasing (hence decreasing) limits by (3). Thus $\mathcal{M}$ is a monotone class containing the algebra $\mathcal{A}$. By the Monotone Class Theorem for sets (the smallest monotone class containing an algebra $\mathcal{A}$ equals $\sigma(\mathcal{A})$), we conclude $\sigma(\mathcal{A}) \subseteq \mathcal{M}$. Equivalently, $\mathbf{1}_B \in \mathcal{H}$ for every $B \in \sigma(\mathcal{A})$.

**Step 3 (Dyadic approximation for nonnegative measurable $f$; corrected scheme).** Let $f: X \to [0,M]$ be bounded and $\sigma(\mathcal{A})$‑measurable. For $n \in \mathbb{N}$, partition $[0,M]$ into $2^n$ half‑open intervals of length $\Delta_n := M/2^n$ with left endpoints $a_{n,j} := j\,\Delta_n$ for $j=0,\dots,2^n-1$. Define
$$
E_{n,j} := f^{-1}([a_{n,j}, a_{n,j+1})) \in \sigma(\mathcal{A}), \qquad
\varphi_n(x) := \sum_{j=0}^{2^n-1} a_{n,j} \, \mathbf{1}_{E_{n,j}}(x).
$$
Then $0 \le \varphi_n \le f < \varphi_n + \Delta_n$ pointwise and $\varphi_n \uparrow f$ pointwise (the left‑endpoint bin map is nondecreasing under dyadic refinement). For each $n$, $\mathbf{1}_{E_{n,j}} \in \mathcal{H}$ by Step 2; by (2), $\varphi_n \in \mathcal{H}$; by (3), $f \in \mathcal{H}$.

**Step 4 (General bounded measurable $f$ via positive/negative parts).** For bounded $f: X \to \mathbb{R}$, write $f = f^+ - f^-$ with $f^\pm \ge 0$ bounded and $\sigma(\mathcal{A})$‑measurable. Apply Step 3 to $f^\pm$ to obtain $f^\pm \in \mathcal{H}$, then use (2) to conclude $f \in \mathcal{H}$. □

**Remarks (Corrections and structure).**

1) Set‑theoretic reference (π–λ vs monotone class): What we proved about $\mathcal{M}$ (closure under complements and monotone limits) is exactly the hypothesis of the Monotone Class Theorem for sets, not π–λ. The correct sentence is: “By the Monotone Class Theorem (for sets): the smallest monotone class containing an algebra $\mathcal{A}$ equals $\sigma(\mathcal{A})$. Hence $\sigma(\mathcal{A}) \subseteq \mathcal{M}$.” If one prefers π–λ, show that $\mathcal{M}$ is a λ‑system and only assume $\mathcal{A}$ is a π‑system; then apply the π–λ theorem. Our hypotheses already give the stronger monotone‑class route, so we proceed with it.

2) Dyadic simple‑function construction (indexing and monotonicity): We use exactly $2^n$ bins with left endpoints $a_{n,j} = j (M/2^n)$; this avoids overshooting and ensures $\varphi_n \uparrow f$ for nonnegative $f$. For general bounded $f$, monotonicity can fail if used “as‑is”; hence Step 4 passes to $f^\pm$, or equivalently one may add a constant to make $f$ nonnegative and remove it at the end using linearity (2).

---

**Remark (Why This Theorem Matters for RL).**

This theorem is the workhorse for extending properties from indicators to all bounded measurable functions. Two recurring uses:
- Conditional expectation (Week 6): verify properties on indicators and extend to bounded measurable $X$ via the functional monotone class theorem.
- Bellman operators on measurable state spaces (Week 25): verify on indicators of Borel sets (from a generating algebra), use linearity of expectation, and extend to all bounded measurable $V$. This is precisely how Puterman (2014, §4.3–4.5) establishes existence/uniqueness of value functions for MDPs with uncountable state spaces.

---

**End of Day 3 Exercises (FINAL_V2)**
