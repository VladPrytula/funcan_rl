[[Day_1_FINAL]]

# Day 1 Exercises: Foundational Tools for Measure-Theoretic RL

These exercises develop essential technical skills for working with measure spaces and measurable functions. Having established the foundational definitions in Day 1, we now build computational fluency and proof techniques. We focus on three foundational skills: characterizing asymptotic set behavior, understanding measure regularity conditions, and ensuring function compositions preserve measurability. Each exercise illuminates concepts that recur throughout reinforcement learning theory.

**Relationship to Segment 2 (Day 1.md):**
- **Exercise 3** is the **primary task** for Segment 2 (30 minutes)
- **Exercise 1** is the **stretch goal**
- **Exercise 2** provides additional depth for those who complete the primary tasks early or wish to explore measure-theoretic subtleties further. This exercise is optional enrichment that clarifies when key theorems (Fubini-Tonelli, Radon-Nikodym) apply in Weeks 3-4.

---

## Exercise 1: Characterizations of Set $\limsup$ and $\liminf$

### Motivation

In reinforcement learning, we constantly reason about asymptotic behavior: Does a learning algorithm visit every state infinitely often? Do policy iterates converge almost surely? Does exploration decay appropriately? The mathematical language for such questions is the $\limsup$ and $\liminf$ of sequences of sets.

**Concrete RL application (Week 8 preview):**

Consider a finite-state Markov chain with states $\{s_1, s_2, s_3\}$. For each time $n$, define the event:
$$E_n = \{X_n = s_1\} \quad \text{(the chain visits state } s_1 \text{ at time } n\text{)}$$

The $\limsup$ and $\liminf$ of this sequence characterize asymptotic behavior:

$$
\limsup_{n \to \infty} E_n = \{\text{visit } s_1 \text{ infinitely often}\}
$$
$$
\liminf_{n \to \infty} E_n = \{\text{visit } s_1 \text{ for all but finitely many } n\}
$$

**Key relationship:** $\liminf E_n \subseteq \limsup E_n$ always holds. The $\liminf$ is the **smaller** set (stronger condition):
- **Trajectories in $\liminf E_n$:** Eventually, the chain **never leaves** $s_1$ (it stays there forever after some finite time $N$)
- **Trajectories in $\limsup E_n$:** The chain **returns** to $s_1$ infinitely often, but may also leave it infinitely often

**Example distinguishing the two:**
- Trajectory $\omega_1$: $s_1, s_2, s_1, s_3, s_1, s_1, s_1, s_1, \ldots$ (stays in $s_1$ after time 4)
  → $\omega_1 \in \liminf E_n$ (hence also in $\limsup E_n$)

- Trajectory $\omega_2$: $s_1, s_2, s_1, s_2, s_1, s_2, \ldots$ (alternates forever)
  → $\omega_2 \in \limsup E_n$ but $\omega_2 \notin \liminf E_n$

**Full exploration in RL:**

In RL, we care whether a policy $\pi$ ensures **full exploration** of the state space. For **finite or countable state spaces** (our focus in Weeks 7-12), this means visiting every state infinitely often:

For each state $s \in \mathcal{S}$, define $E_n(s) = \{S_n = s\}$. Full exploration requires:
$$\mathbb{P}_\pi\left(\text{visit every } s \in \mathcal{S} \text{ infinitely often}\right) = \mathbb{P}_\pi\left(\bigcap_{s \in \mathcal{S}} \limsup_{n \to \infty} E_n(s)\right) = 1$$

**Key observation:** The intersection $\bigcap_{s \in \mathcal{S}}$ means we want a **single trajectory** that visits **all** states infinitely often. For finite $\mathcal{S}$, this is achievable (e.g., via $\varepsilon$-greedy exploration with $\varepsilon > 0$).

> **Note on continuous state spaces:** For **uncountable** $\mathcal{S}$ (e.g., $\mathbb{R}^n$ in continuous control), visiting every individual state is impossible—the trajectory is countable while $\mathbb{R}^n$ is uncountable. We instead require **recurrence** on regions or **ergodicity** (Weeks 9-10, 17-22). This distinction is subtle but crucial, and we develop the proper framework for continuous spaces when we study ergodic theory (Week 9-10). For now, focus on finite/countable spaces where the $\limsup$ characterization is exact.

**Why this matters:** Q-learning convergence (Week 34) requires visiting every state-action pair $(s,a)$ infinitely often. Characterizing this event precisely is where the $\limsup$ machinery becomes essential [@tsitsiklis:q_learning:1994].

**Additional applications** (to be developed later):
- Q-learning convergence (Week 34): requires visiting all $(s,a)$ infinitely often
- Stochastic approximation almost-sure convergence (Weeks 34-39): formalized via lim sup of error events

These concepts arise in exploration analysis, Markov chain recurrence theory, and almost-sure convergence results that we develop throughout the course.

### Statement and Proof

**Proposition 1.1.** For a sequence of sets $(E_n)_{n\ge1}$ in a measurable space $(X, \mathcal{F})$,
$$
\limsup_{n\to\infty} E_n=\bigcap_{k=1}^{\infty}\ \bigcup_{n\ge k} E_n
=\{x\in X:\ x\in E_n\ \text{for infinitely many } n\},
$$
$$
\liminf_{n\to\infty} E_n=\bigcup_{k=1}^{\infty}\ \bigcap_{n\ge k} E_n
=\{x\in X:\ x\in E_n\ \text{for all but finitely many } n\}.
$$

*Proof.*

**Proof of the $\limsup$ characterization.**

We establish both the forward and reverse inclusions.

**Forward inclusion ($\subseteq$):** Take $x\in\bigcap_{k\ge1}\bigcup_{n\ge k}E_n$. For each $k \in \mathbb{N}$, since $x \in \bigcup_{n \ge k} E_n$, we can choose an index $n_k\ge k$ such that $x\in E_{n_k}$. Since $k$ ranges over all natural numbers, we obtain a sequence of indices $(n_k)_{k=1}^{\infty}$ with $n_k \ge k$ for all $k$. This sequence is unbounded: if only finitely many distinct values appeared, say $n_k \in \{m_1, \ldots, m_J\}$ for all $k$, then for $k > \max\{m_1, \ldots, m_J\}$, we would need $n_k \ge k > \max\{m_i\}$, contradicting $n_k \in \{m_1, \ldots, m_J\}$. Thus infinitely many distinct indices must appear, so $x$ is in $E_n$ for infinitely many $n$.

**Reverse inclusion ($\supseteq$):** Conversely, suppose $x$ belongs to $E_n$ for infinitely many $n$. For any fixed $k \in \mathbb{N}$, the set $\{n \ge k : x \in E_n\}$ is non-empty (since $x$ is in infinitely many $E_n$, at least one such index must be $\ge k$). Therefore there exists $n\ge k$ with $x\in E_n$, which means $x\in\bigcup_{n\ge k}E_n$. Since this holds for every $k$, we have $x\in\bigcap_{k\ge1}\bigcup_{n\ge k}E_n$.

**Proof of the $\liminf$ characterization.**

**Forward inclusion ($\subseteq$):** Take $x\in\bigcup_{k\ge1}\bigcap_{n\ge k}E_n$. Then for some $k_0 \in \mathbb{N}$, we have $x\in\bigcap_{n\ge k_0}E_n$. This means $x\in E_n$ for all $n\ge k_0$, which is precisely the definition of "$x$ is in $E_n$ for all but finitely many $n$" (the finite exceptions being $n < k_0$).

**Reverse inclusion ($\supseteq$):** Conversely, if $x$ is in $E_n$ for all but finitely many $n$, then there exists $N \in \mathbb{N}$ such that $x\in E_n$ for all $n\ge N$. Thus $x\in\bigcap_{n\ge N}E_n$, which implies $x\in\bigcup_{k\ge1}\bigcap_{n\ge k}E_n$.
$\square$

### Complementary Results

**Proposition 1.2 (De Morgan Laws for Limits).**
$$
(\limsup E_n)^c=\liminf(E_n^{\,c}),\qquad
(\liminf E_n)^c=\limsup(E_n^{\,c}).
$$

*Proof.* These follow directly from De Morgan's laws for unions and intersections applied to the definitions. For example,
$$
(\limsup E_n)^c = \left(\bigcap_{k=1}^{\infty} \bigcup_{n\ge k} E_n\right)^c = \bigcup_{k=1}^{\infty} \bigcap_{n\ge k} E_n^c = \liminf(E_n^c).
$$
The second equality is analogous. $\square$

**Why this is useful:** In probability, $(\limsup E_n)^c$ is the event "eventually, $E_n$ stops occurring," which is precisely $\liminf E_n^c$.

### Connection to Numerical Limits

The set-theoretic limits $\limsup E_n$ and $\liminf E_n$ have an elegant connection to numerical limits via indicator functions. This perspective bridges set limits and numerical convergence, and is essential for probability theory—particularly when proving almost-sure convergence results in stochastic approximation (Weeks 34-39).

**Proposition 1.3 (Indicator Function Characterization).** For a sequence of sets $(E_n)_{n \ge 1}$ in a measurable space $(X, \mathcal{F})$, define the indicator function $\mathbf{1}_{E_n}: X \to \{0,1\}$ by $\mathbf{1}_{E_n}(x) = 1$ if $x \in E_n$ and $\mathbf{1}_{E_n}(x) = 0$ otherwise. Then for each $x \in X$:
$$
\mathbf{1}_{\limsup E_n}(x)=\limsup_{n\to\infty} \mathbf{1}_{E_n}(x),\qquad
\mathbf{1}_{\liminf E_n}(x)=\liminf_{n\to\infty} \mathbf{1}_{E_n}(x),
$$
where $\limsup_{n} a_n = \lim_{k \to \infty} \sup_{n \ge k} a_n$ and $\liminf_{n} a_n = \lim_{k \to \infty} \inf_{n \ge k} a_n$ for sequences of real numbers.

*Proof.* We prove the $\limsup$ characterization; the $\liminf$ case is analogous.

**Step 1 (Forward direction: $\mathbf{1}_{\limsup E_n}(x) = 1 \Rightarrow \limsup_n \mathbf{1}_{E_n}(x) = 1$).**

If $\mathbf{1}_{\limsup E_n}(x) = 1$, then $x \in \limsup E_n = \{x : x \in E_n \text{ for infinitely many } n\}$ by Proposition 1.1. Thus for every $k \in \mathbb{N}$, there exists $n \ge k$ such that $x \in E_n$, which means $\mathbf{1}_{E_n}(x) = 1$. Therefore $\sup_{n \ge k} \mathbf{1}_{E_n}(x) = 1$ for all $k$, which implies $\limsup_n \mathbf{1}_{E_n}(x) = \lim_{k \to \infty} \sup_{n \ge k} \mathbf{1}_{E_n}(x) = 1$.

**Step 2 (Reverse direction: $\limsup_n \mathbf{1}_{E_n}(x) = 1 \Rightarrow \mathbf{1}_{\limsup E_n}(x) = 1$).**

If $\limsup_n \mathbf{1}_{E_n}(x) = 1$, then $\sup_{n \ge k} \mathbf{1}_{E_n}(x) = 1$ for all $k$. This means for every $k$, there exists $n \ge k$ with $\mathbf{1}_{E_n}(x) = 1$, i.e., $x \in E_n$. Thus $x$ belongs to $E_n$ for infinitely many $n$, so $x \in \limsup E_n$, which gives $\mathbf{1}_{\limsup E_n}(x) = 1$.

**Step 3 (Case when $\mathbf{1}_{\limsup E_n}(x) = 0$).**

If $\mathbf{1}_{\limsup E_n}(x) = 0$, then $x \notin \limsup E_n$, so $x$ is in $E_n$ for only finitely many $n$ (the negation of "infinitely often"). Thus there exists $k_0$ such that $x \notin E_n$ for all $n \ge k_0$, which means $\mathbf{1}_{E_n}(x) = 0$ for all $n \ge k_0$. Therefore $\sup_{n \ge k_0} \mathbf{1}_{E_n}(x) = 0$, so $\limsup_n \mathbf{1}_{E_n}(x) = \lim_{k \to \infty} \sup_{n \ge k} \mathbf{1}_{E_n}(x) = 0$.

The proof for $\liminf$ follows the same pattern, using the characterization "$x \in \liminf E_n$ if and only if $x \in E_n$ for all but finitely many $n$." $\square$

**Why this connection matters (Preview for Probability and RL):**

In stochastic approximation (Weeks 34-39), proving a learning algorithm converges almost surely often reduces to showing $\liminf_{n \to \infty} \mathbf{1}_{E_n} = 1$ almost surely, where $E_n = \{\text{error}_n < \varepsilon\}$. The indicator viewpoint allows us to:
- Apply numerical convergence theorems (Fatou's lemma, dominated convergence) to sequences of indicators
- Use martingale convergence results (Week 6) to prove $\liminf \mathbf{1}_{E_n} = 1$ a.s.
- Connect set-theoretic "eventually always in $E_n$" to numerical "$\liminf \mathbf{1}_{E_n} = 1$"

This unification of set limits and numerical limits is a fundamental bridge between measure theory and probability that we exploit heavily in convergence analysis.

---

## Exercise 2: $\sigma$-Finite and Semifinite Measures

### Motivation

Not all measures are created equal. The behavior of integrals and the validity of powerful convergence theorems depend critically on certain regularity properties. $\sigma$-Finiteness and semifiniteness are not mere technicalities—they determine when we can apply essential tools.

**Where $\sigma$-finiteness is required in RL:**

1. **Fubini-Tonelli Theorem (Week 2):** For **stochastic policies** $\pi(a|s)$ (formalized Week 23), computing expectations over the joint state-action space $(s, a) \sim \rho(s) \pi(a|s)$—as in policy gradient objectives
   $$\mathbb{E}_{s \sim \rho, a \sim \pi(\cdot|s)}[\nabla \log \pi(a|s) Q(s,a)] = \int_{\mathcal{S}} \int_{\mathcal{A}} \nabla \log \pi(a|s) Q(s,a) \, \pi(da|s) \, \rho(ds)$$
   requires Fubini-Tonelli to interchange integration order (from $\int_{\mathcal{S}} \int_{\mathcal{A}}$ to $\int_{\mathcal{A}} \int_{\mathcal{S}}$ when needed for derivations), which demands $\sigma$-finiteness of both $\mathcal{S}$ and $\mathcal{A}$ [@folland:real_analysis:1999, §2.4]. This is essential for deriving the policy gradient theorem (Week 35).

   **Clarification on deterministic vs. stochastic policies:** For **deterministic policies** $\pi: \mathcal{S} \to \mathcal{A}$, we compute expectations as $\mathbb{E}_{s \sim \rho}[f(s, \pi(s))] = \int_{\mathcal{S}} f(s, \pi(s)) \, \rho(ds)$, which is a single integral over $\mathcal{S}$ only—no product measure is involved, and $\sigma$-finiteness is not required for this operation. The subtlety arises only for **stochastic policies**, where $\pi(\cdot|s)$ is a transition kernel (a family of probability measures on $\mathcal{A}$ indexed by $s$). The joint expectation over $(s,a)$ involves product measure structure, and Fubini-Tonelli's applicability depends on $\sigma$-finiteness of the underlying spaces. This distinction becomes critical when deriving policy gradient theorems for stochastic policies (Week 35).

2. **Radon-Nikodym Theorem (Week 3):** Existence of probability densities—likelihood ratios for importance sampling (Week 38), policy gradient theorems [@sutton:policy_gradient:2000] (Week 35)—requires $\sigma$-finiteness [@folland:real_analysis:1999, §3.2].

3. **Product Measures (Weeks 2-4):** Finite product measures are introduced in **Week 2** (Fubini-Tonelli). Constructing probability measures on **infinite** trajectory spaces $(\mathcal{S} \times \mathcal{A})^{\mathbb{N}}$ requires the Kolmogorov extension theorem (**Week 4** preview; full treatment in Week 10 for general state spaces).

Most RL theory assumes $\sigma$-finite measure spaces (e.g., Lebesgue measure on $\mathbb{R}^n$ for continuous states, counting measure on finite/countable state spaces). Understanding the boundaries of this assumption clarifies when our theorems apply.

### Core Theory

We recall key definitions from Day 1 §II-III:

**Definition 2.1 (Measure).** Let $(X, \mathcal{F})$ be a measurable space. A function $\mu: \mathcal{F} \to [0, \infty]$ is a **measure** if:
1.  $\mu(\emptyset) = 0$.
2.  (Countable Additivity) For any countable collection $\{A_n\}_{n=1}^{\infty}$ of pairwise disjoint sets in $\mathcal{F}$,
    $$ \mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n) $$

**Definition 2.2 ($\sigma$-Finite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **$\sigma$-finite** if there exists a countable collection $\{E_n\}_{n=1}^{\infty} \subseteq \mathcal{F}$ such that:
$$ X = \bigcup_{n=1}^{\infty} E_n \quad \text{and} \quad \mu(E_n) < \infty \text{ for all } n \in \mathbb{N} $$

In essence, a $\sigma$-finite space can be exhausted by a countable sequence of finite-measure "pieces."

**Example 2.1 (Lebesgue Measure on $\mathbb{R}^n$).** The standard Lebesgue measure $\lambda$ on $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$ is $\sigma$-finite [@folland:real_analysis:1999, §1.4]. For $n=1$, write $\mathbb{R} = \bigcup_{k=1}^{\infty} [-k, k]$ with $\lambda([-k, k]) = 2k < \infty$. For general $n$, use $\mathbb{R}^n = \bigcup_{k=1}^{\infty} [-k, k]^n$ with $\lambda([-k,k]^n) = (2k)^n < \infty$. This is the canonical measure for continuous state spaces in RL.

**Definition 2.3 (Semifinite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **semifinite** if for every set $A \in \mathcal{F}$ with $\mu(A) = \infty$, there exists a subset $B \in \mathcal{F}$ such that $B \subseteq A$ and $0 < \mu(B) < \infty$.

A semifinite measure does not permit "purely infinite" measurable sets that contain no measurable subsets of finite, non-zero measure.

### The Relationship Between Classifications

**Proposition 2.1 (Proven in Day 1 FINAL §III.A).** Let $(X, \mathcal{F}, \mu)$ be a measure space. If $\mu$ is $\sigma$-finite, then $\mu$ is semifinite. However, the converse is not true: there exist semifinite measures that are not $\sigma$-finite.

The proof is given in Day 1 §III.A, Proposition 1.1. The key idea:
- **$\sigma$-finite ⇒ semifinite:** Decompose any infinite-measure set $A$ using the $\sigma$-finite covering $X = \bigcup E_n$. By subadditivity, at least one $A \cap E_n$ has positive finite measure.
- **Counterexample:** Counting measure on $\mathbb{R}$ (assigning $|A|$ to finite sets, $\infty$ otherwise) is semifinite but not $\sigma$-finite, since $\mathbb{R}$ cannot be covered by countably many finite sets.

**Remark.** The pathological counting measure on uncountable spaces is precisely the type of measure we avoid in RL by restricting to **Polish spaces** (complete separable metric spaces) with Radon measures (finite on compact sets). Standard RL state spaces—finite sets, $\mathbb{R}^n$, or Polish spaces like $[0,1]^{\infty}$—all admit natural $\sigma$-finite measures.

---

## Exercise 3: Measurability of Arithmetic Operations and Compositions

### Motivation

In reinforcement learning, we constantly combine and compose functions:
- **Arithmetic operations:** Value functions are combined: $V(s) = R(s) + \gamma \mathbb{E}[V(s')]$
- **State features:** A measurable function $\phi: \mathcal{S} \to \mathbb{R}^d$ extracts features from raw states
- **Neural networks:** A function approximator maps features to value estimates

We must ensure these operations preserve measurability, so that expectations remain well-defined.

### Part A: Closure under Arithmetic Operations

**Proposition 3.1 (From Day 1 FINAL, Proposition 1.3).** Let $f, g: (X, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ be measurable. Then the sum $f+g$ and product $f \cdot g$ are measurable.

*Proof.*

**(i) Sum is measurable:**
We show $\{x \mid f(x)+g(x) < a\} \in \mathcal{F}$ for any $a \in \mathbb{R}$.

**Why this suffices:** The collection $\{(-\infty, a) : a \in \mathbb{R}\}$ of open rays generates the Borel $\sigma$-algebra $\mathcal{B}(\mathbb{R})$ (as noted in Day 1 §I.A, Remark on Generating Classes). By the **generating class criterion** (Lemma 3.1 below), checking preimages for this generating class suffices to prove measurability. We formalize this principle rigorously in Part B.

The key insight: $f(x) + g(x) < a$ if and only if there exists $q \in \mathbb{Q}$ with $f(x) < q$ and $g(x) < a-q$. Thus:
$$
\{x \mid f(x) + g(x) < a\} = \bigcup_{q \in \mathbb{Q}} (\{x \mid f(x) < q\} \cap \{x \mid g(x) < a-q\})
$$

For each $q$, both sets in the intersection are measurable (by measurability of $f$ and $g$), so their intersection is measurable. The result is a countable union of measurable sets, hence measurable.

**(ii) Product is measurable:**
We first show $f^2$ is measurable. For $a \ge 0$:
$$
\{x \mid f(x)^2 < a\} = \{x \mid -\sqrt{a} < f(x) < \sqrt{a}\}
= \{x \mid f(x) < \sqrt{a}\} \cap \{x \mid f(x) > -\sqrt{a}\}
$$

For $a < 0$, the set $\{x \mid f(x)^2 < a\} = \emptyset$ (empty set) since squares are non-negative. In both cases, the preimage is measurable.

Both sets are measurable, so $f^2$ is measurable. By (i), $f+g$ is measurable, so $(f+g)^2$ is measurable. Using the identity:
$$
f \cdot g = \frac{1}{2}((f+g)^2 - f^2 - g^2)
$$
we conclude $f \cdot g$ is measurable as a linear combination of measurable functions.
$\square$

*Remark (Extension to $\mathbb{R}^n$).* The proof above applies **verbatim** to functions $f, g: (X, \mathcal{F}) \to (\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$ by working component-wise: if $f = (f_1, \ldots, f_n)$ and $g = (g_1, \ldots, g_n)$ are measurable, then $f + g = (f_1 + g_1, \ldots, f_n + g_n)$ is measurable since each component $f_i + g_i$ is measurable by the scalar case. This is crucial for feature maps $\phi: \mathcal{S} \to \mathbb{R}^d$ in deep RL (Week 34-35).

*Remark (On Generality).* The proof uses only the density of $\mathbb{Q}$ in $\mathbb{R}$ and basic set operations.

**For addition and scalar multiplication**, the result extends immediately to measurable functions taking values in any **second-countable topological vector space** (e.g., $\mathbb{R}^n$, $\ell^2$, $C([0,1])$), where these operations are continuous.

**For products**, we must restrict to spaces with compatible algebraic structure: **topological algebras** where a continuous bilinear multiplication map $m: X \times X \to X$ is defined. Examples include:
- $\mathbb{R}^n$ with componentwise product
- $C(K)$ (continuous functions on compact $K$) with pointwise product
- $L^\infty$ with pointwise product

In a general topological vector space like $\ell^2$, pointwise multiplication need not map $\ell^2 \times \ell^2 \to \ell^2$ (the product of two square-summable sequences need not be square-summable). More precisely, whenever a continuous **bilinear** map $m: X \times X \to Y$ is given, the composition $(f,g) \mapsto m(f,g)$ preserves measurability. For reinforcement learning—where state spaces are subsets of $\mathbb{R}^n$ and value functions are real-valued—the statement above is the natural form. We will revisit this generality in **Week 12** when developing Banach-valued measurable functions for operator-theoretic approaches to MDPs.

### Part B: Closure under Composition with Continuous Functions

**Proposition 3.2.** Let $(X, \mathcal{F})$ be a measurable space. Let $g: X \to \mathbb{R}$ be measurable (with respect to $\mathcal{B}(\mathbb{R})$), and let $f: \mathbb{R} \to \mathbb{R}$ be continuous. Then the composition $h = f \circ g: X \to \mathbb{R}$ is measurable.

### Proof Strategy

To prove $h$ is measurable, we must show $h^{-1}(B) \in \mathcal{F}$ for all $B \in \mathcal{B}(\mathbb{R})$. Since $\mathcal{B}(\mathbb{R})$ contains uncountably many sets, checking this directly is impossible. The key insight is that we only need to check preimages for a *generating class*.

**Lemma 3.1 (Measurability Criterion via Generators).** Let $(X, \mathcal{F})$ and $(Y, \mathcal{G})$ be measurable spaces. Suppose $\mathcal{C} \subseteq 2^Y$ generates $\mathcal{G}$ (i.e., $\sigma(\mathcal{C}) = \mathcal{G}$). Then a function $\phi: X \to Y$ is measurable if and only if $\phi^{-1}(C) \in \mathcal{F}$ for every $C \in \mathcal{C}$.

*Proof.* The "only if" direction is immediate: if $\phi$ is measurable and $\mathcal{C} \subseteq \mathcal{G}$, then $\phi^{-1}(C) \in \mathcal{F}$ for all $C \in \mathcal{C}$.

For the "if" direction, define:
$$ \mathcal{G}' = \{B \subseteq Y \mid \phi^{-1}(B) \in \mathcal{F}\} $$

We verify that $\mathcal{G}'$ is a $\sigma$-algebra:
1. $Y \in \mathcal{G}'$ since $\phi^{-1}(Y) = X \in \mathcal{F}$.
2. If $B \in \mathcal{G}'$, then $\phi^{-1}(B^c) = (\phi^{-1}(B))^c \in \mathcal{F}$ (since $\mathcal{F}$ is closed under complements), so $B^c \in \mathcal{G}'$.
3. If $\{B_n\}_{n=1}^{\infty} \subseteq \mathcal{G}'$, then $\phi^{-1}(\bigcup_{n=1}^{\infty} B_n) = \bigcup_{n=1}^{\infty} \phi^{-1}(B_n) \in \mathcal{F}$ (since $\mathcal{F}$ is closed under countable unions), so $\bigcup_{n=1}^{\infty} B_n \in \mathcal{G}'$.

By hypothesis, $\mathcal{C} \subseteq \mathcal{G}'$. Since $\mathcal{G}'$ is a $\sigma$-algebra containing $\mathcal{C}$, and $\mathcal{G} = \sigma(\mathcal{C})$ is the *smallest* such $\sigma$-algebra, we have $\mathcal{G} \subseteq \mathcal{G}'$. Thus for any $B \in \mathcal{G}$, we have $\phi^{-1}(B) \in \mathcal{F}$, proving $\phi$ is measurable. $\square$

**Remark (The Good Sets Principle).** The proof above exemplifies a fundamental technique in measure theory: to prove a property holds for all sets in a generated $\sigma$-algebra $\sigma(\mathcal{C})$, we define the collection of "good" sets (those with the desired property), verify it forms a $\sigma$-algebra, and show it contains the generating class $\mathcal{C}$. By minimality of $\sigma(\mathcal{C})$, we conclude the property holds for all sets in $\sigma(\mathcal{C})$.

This strategy is called the **good sets principle** (or **Dynkin class method**) and is formalized rigorously via the **$\pi-\lambda$ theorem** in Appendix A2.1 ([THM-2.2.A1], Week 2, Day 2). The proof above is self-contained and requires no knowledge of the $\pi-\lambda$ theorem. However, recognizing this proof pattern will help you navigate similar arguments throughout measure theory and probability—it recurs constantly when working with generated $\sigma$-algebras.

*Proof of Proposition 3.2.*

Let $\mathcal{O}(\mathbb{R})$ denote the collection of open sets in $\mathbb{R}$. It is well-known that $\sigma(\mathcal{O}(\mathbb{R})) = \mathcal{B}(\mathbb{R})$. By the generator criterion (Lemma 3.1), it suffices to check preimages of open sets. That is, we need only show $h^{-1}(U) \in \mathcal{F}$ for every open set $U \subseteq \mathbb{R}$.

**Step 1:** Express the preimage using composition.

For any set $U \subseteq \mathbb{R}$, we have $h^{-1}(U) = (f \circ g)^{-1}(U) = g^{-1}(f^{-1}(U))$.

**Step 2:** Analyze $f^{-1}(U)$ for open $U$.

Let $U \subseteq \mathbb{R}$ be open. Since $f: \mathbb{R} \to \mathbb{R}$ is continuous, the preimage $V = f^{-1}(U)$ is open (by the topological definition of continuity).

**Step 3:** Analyze $g^{-1}(V)$ for open $V$.

From Step 2, $V$ is open, hence $V \in \mathcal{B}(\mathbb{R})$. Since $g: X \to \mathbb{R}$ is measurable, we have $g^{-1}(V) \in \mathcal{F}$.

**Step 4:** Conclude.

From Steps 1-3, for any open set $U \subseteq \mathbb{R}$:
$$ h^{-1}(U) = g^{-1}(f^{-1}(U)) = g^{-1}(V) \in \mathcal{F} $$
where $V = f^{-1}(U)$ is open by continuity of $f$, and $g^{-1}(V) \in \mathcal{F}$ by measurability of $g$.

Since $h^{-1}(U) \in \mathcal{F}$ for all $U \in \mathcal{O}(\mathbb{R})$, and $\mathcal{O}(\mathbb{R})$ generates $\mathcal{B}(\mathbb{R})$, Lemma 3.1 implies $h$ is measurable. $\square$

### Application to Neural Networks

  **Notation.** Throughout RL theory, we use the following standard notation for neural network function approximators:
  - $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}$ denotes a **neural network** with parameters $\theta$ (weights and biases), mapping $d$-dimensional feature vectors to scalar outputs (e.g., value function estimates)
  - For Q-functions (state-action value functions): $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}^{|\mathcal{A}|}$ outputs a vector of Q-values, where $\mathcal{A}$ denotes the action space and $|\mathcal{A}|$ is the number of available actions (e.g., for Atari games with 18 actions, $|\mathcal{A}| = 18$, so the network outputs $\mathbb{R}^{18}$)
  - The subscript $\theta$ emphasizes the parametrization, distinguishing different network instantiations during training

**Corollary 3.3 (Measurability of Neural Network Value Functions).** Let $(\mathcal{S}, \mathcal{F}_\mathcal{S})$ be a measurable state space. If $\phi: \mathcal{S} \to \mathbb{R}^d$ is measurable and the neural network $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}$ is continuous, then the composed value function $V_\theta = \text{NN}_\theta \circ \phi: \mathcal{S} \to \mathbb{R}$ is measurable.

**Why neural networks are measurable (addressing ReLU non-differentiability):**

Modern deep RL uses neural networks with ReLU activations. A common question arises: "Is ReLU continuous?" The answer is **yes**—ReLU is continuous everywhere, though it is **non-differentiable** at a single point (0).

**Clarifying ReLU structure in layers:**

The **scalar ReLU function** $\text{ReLU}(x) = \max(0, x)$ on $\mathbb{R}$ is continuous at every point, including $x=0$ (left and right limits both equal 0). However, ReLU layers apply this element-wise to vectors:
$$ \text{ReLU}(\mathbf{x}) = (\max(0, x_1), \ldots, \max(0, x_d)) $$

A feedforward ReLU network is a composition:
$$ \text{NN}_\theta = \text{Linear}_L \circ \text{ReLU}_{L-1} \circ \text{Linear}_{L-1} \circ \cdots \circ \text{ReLU}_1 \circ \text{Linear}_1 $$

where each $\text{Linear}_k$ is an affine map (matrix multiplication + bias), which is continuous. Each ReLU layer is continuous (as the componentwise max of continuous functions).

**Why measurability holds:**
- Each affine layer $\text{Linear}_k: \mathbb{R}^{n_k} \to \mathbb{R}^{n_{k+1}}$ is continuous, hence Borel measurable
- Each ReLU layer $\text{ReLU}_k: \mathbb{R}^{n_k} \to \mathbb{R}^{n_k}$ is continuous (continuous in each component), hence Borel measurable
- By Proposition 3.2, a composition of continuous functions is continuous, hence measurable
- The full network $\text{NN}_\theta$ is therefore continuous and Borel measurable
- Composing the measurable feature map $\phi$ with the continuous network $\text{NN}_\theta$ (via Proposition 3.2) yields a measurable value function $V_\theta$

**Non-differentiability vs. continuity:**
While ReLU is **non-differentiable** at points where the pre-activation equals zero (forming hyperplanes $\{x \in \mathbb{R}^d : w^T x + b = 0\}$ in the input space), these sets have **Lebesgue measure zero** in $\mathbb{R}^d$. However, for measurability purposes, this is irrelevant—ReLU networks are **everywhere continuous**, not merely "continuous almost everywhere." Continuity is strictly stronger than Borel measurability, so the argument is even simpler than an "a.e. continuity" approach would suggest.

**Practical implication:** Modern deep RL uses ReLU networks with $10^4$–$10^6$ neurons (e.g., Atari DQN has ~$10^6$ parameters). While these networks are non-differentiable on a union of measure-zero hyperplanes (one per neuron), they remain **continuous everywhere**. Measurability is preserved, ensuring that expectations like $\mathbb{E}_{s \sim \rho}[V_\theta(s)]$ are well-defined.

**Technical note:** Even if we had discontinuities on a measure-positive set, compositions of measurable functions remain measurable (though continuity is not preserved). Measurability is preserved under far more general operations than continuity, which is why it is the correct framework for RL function approximators.

**Concrete example (DQN [@mnih:dqn:2015]):**

In deep Q-learning:
- States $s \in \mathcal{S}$ (e.g., $84 \times 84$ grayscale images) define a measurable space with Borel $\sigma$-algebra.
- The pixel representation $s \mapsto \text{pixels}(s) \in [0,255]^{84 \times 84}$ is measurable (identity map on a Borel space).
- The Q-network $Q_\theta: [0,255]^{84 \times 84} \to \mathbb{R}^{|\mathcal{A}|}$ (convolutional layers + ReLU + linear layers) is Borel measurable.

**Why $Q_\theta$ is measurable:** The DQN architecture is a composition:
   $$Q_\theta = \text{Linear}_3 \circ \text{ReLU}_2 \circ \text{Conv}_2 \circ \text{ReLU}_1 \circ \text{Conv}_1$$
   Each convolutional layer $\text{Conv}_k: \mathbb{R}^{n×m×c} \to \mathbb{R}^{n'×m'×c'}$ is a **linear map** (matrix multiplication in tensor form) followed by bias addition—hence continuous, therefore Borel measurable. Each ReLU layer is continuous everywhere (non-differentiable on measure-zero sets, but still continuous). By Proposition 3.2 applied iteratively:
   - $\text{Conv}_1$ is continuous (hence measurable)
   - $\text{ReLU}_1$ is continuous (hence measurable)
   - $\text{Conv}_2 \circ \text{ReLU}_1$ is measurable (Proposition 3.2: continuous ∘ measurable)
   - Continuing this composition, $Q_\theta$ is measurable

   **Key insight:** Proposition 3.2 (continuous ∘ measurable = measurable) applies to **each layer**, ensuring the full network is measurable.

- By Proposition 3.2, $s \mapsto Q_\theta(s, a)$ is measurable for each action $a$.
- This ensures the expected Q-value $\mathbb{E}_{s \sim \rho}[Q_\theta(s,a)]$ is well-defined (integration of a measurable function with respect to a probability measure).

**Extension to policy gradients:** Stochastic policies in actor-critic methods (e.g., PPO [@schulman:ppo:2017], SAC [@haarnoja:sac:2018]) use neural networks to output distribution parameters (e.g., mean and variance of a Gaussian). As long as the network $\pi_\theta: \mathcal{S} \to \mathbb{R}^{2|\mathcal{A}|}$ (outputting $\mu, \sigma$ per action) is measurable and the Gaussian density $(a, \mu, \sigma) \mapsto \mathcal{N}(a; \mu, \sigma^2)$ is continuous in $(\mu, \sigma)$ (which it is), the policy density $\pi_\theta(a|s)$ is jointly measurable in $(s, a)$. This ensures policy gradient objectives are well-defined expectations.

---

## Summary

We have developed three foundational tools:

1. **$\limsup$ and $\liminf$ of sets** (Exercise 1) characterize asymptotic behavior of events, essential for analyzing exploration, recurrence, and almost-sure convergence in stochastic approximation (Weeks 34-39).

2. **$\sigma$-Finite measures** (Exercise 2) enable application of Fubini-Tonelli (Week 2), Radon-Nikodym (Week 3), and product measure constructions (Weeks 2-4)—the theoretical bedrock for computing expectations in RL. We proved that $\sigma$-finiteness is stronger than semifiniteness and identified pathological counterexamples.

3. **Measurability under operations** (Exercise 3) guarantees that:
   - Arithmetic combinations of measurable functions (like Bellman updates) remain measurable
   - Neural network policies and value functions (continuous, but non-differentiable at measure-zero sets) are well-defined probabilistic objects
   - Expectations like $\mathbb{E}[V_\theta(S)]$ are mathematically meaningful

These techniques recur throughout measure-theoretic RL. Mastering them now provides the foundation for rigorous convergence analysis in later weeks.
[[Day_1_FINAL]]

# Day 1 Exercises: Foundational Tools for Measure-Theoretic RL

These exercises develop essential technical skills for working with measure spaces and measurable functions. Having established the foundational definitions in Day 1, we now build computational fluency and proof techniques. We focus on three foundational skills: characterizing asymptotic set behavior, understanding measure regularity conditions, and ensuring function compositions preserve measurability. Each exercise illuminates concepts that recur throughout reinforcement learning theory.

**Relationship to Segment 2 (Day 1.md):**
- **Exercise 3** is the **primary task** for Segment 2 (30 minutes)
- **Exercise 1** is the **stretch goal**
- **Exercise 2** provides additional depth for those who complete the primary tasks early or wish to explore measure-theoretic subtleties further. This exercise is optional enrichment that clarifies when key theorems (Fubini-Tonelli, Radon-Nikodym) apply in Weeks 3-4.

---

## Exercise 1: Characterizations of Set $\limsup$ and $\liminf$

### Motivation

In reinforcement learning, we constantly reason about asymptotic behavior: Does a learning algorithm visit every state infinitely often? Do policy iterates converge almost surely? Does exploration decay appropriately? The mathematical language for such questions is the $\limsup$ and $\liminf$ of sequences of sets.

**Concrete RL application (Week 8 preview):**

Consider a finite-state Markov chain with states $\{s_1, s_2, s_3\}$. For each time $n$, define the event:
$$E_n = \{X_n = s_1\} \quad \text{(the chain visits state } s_1 \text{ at time } n\text{)}$$

The $\limsup$ and $\liminf$ of this sequence characterize asymptotic behavior:

$$
\limsup_{n \to \infty} E_n = \{\text{visit } s_1 \text{ infinitely often}\}
$$
$$
\liminf_{n \to \infty} E_n = \{\text{visit } s_1 \text{ for all but finitely many } n\}
$$

**Key relationship:** $\liminf E_n \subseteq \limsup E_n$ always holds. The $\liminf$ is the **smaller** set (stronger condition):
- **Trajectories in $\liminf E_n$:** Eventually, the chain **never leaves** $s_1$ (it stays there forever after some finite time $N$)
- **Trajectories in $\limsup E_n$:** The chain **returns** to $s_1$ infinitely often, but may also leave it infinitely often

**Example distinguishing the two:**
- Trajectory $\omega_1$: $s_1, s_2, s_1, s_3, s_1, s_1, s_1, s_1, \ldots$ (stays in $s_1$ after time 4)
  $\to$ $\omega_1 \in \liminf E_n$ (hence also in $\limsup E_n$)

- Trajectory $\omega_2$: $s_1, s_2, s_1, s_2, s_1, s_2, \ldots$ (alternates forever)
  $\to$ $\omega_2 \in \limsup E_n$ but $\omega_2 \notin \liminf E_n$

**Full exploration in RL:**

In RL, we care whether a policy $\pi$ ensures **full exploration** of the state space. For **finite or countable state spaces** (our focus in Weeks 7-12), this means visiting every state infinitely often:

For each state $s \in \mathcal{S}$, define $E_n(s) = \{S_n = s\}$. Full exploration requires:
$$\mathbb{P}_\pi\left(\text{visit every } s \in \mathcal{S} \text{ infinitely often}\right) = \mathbb{P}_\pi\left(\bigcap_{s \in \mathcal{S}} \limsup_{n \to \infty} E_n(s)\right) = 1$$

**Key observation:** The intersection $\bigcap_{s \in \mathcal{S}}$ means we want a **single trajectory** that visits **all** states infinitely often. For finite $\mathcal{S}$, this is achievable (e.g., via $\varepsilon$-greedy exploration with $\varepsilon > 0$).

> **Note on continuous state spaces:** For **uncountable** $\mathcal{S}$ (e.g., $\mathbb{R}^n$ in continuous control), visiting every individual state is impossible—the trajectory is countable while $\mathbb{R}^n$ is uncountable. We instead require **recurrence** on regions or **ergodicity** (Weeks 9-10, 17-22). This distinction is subtle but crucial, and we develop the proper framework for continuous spaces when we study ergodic theory (Week 9-10). For now, focus on finite/countable spaces where the $\limsup$ characterization is exact.

**Why this matters:** Q-learning convergence (Week 34) requires visiting every state-action pair $(s,a)$ infinitely often. Characterizing this event precisely is where the $\limsup$ machinery becomes essential [@tsitsiklis:q_learning:1994].

**Additional applications** (to be developed later):
- Q-learning convergence (Week 34): requires visiting all $(s,a)$ infinitely often
- Stochastic approximation almost-sure convergence (Weeks 34-39): formalized via lim sup of error events

These concepts arise in exploration analysis, Markov chain recurrence theory, and almost-sure convergence results that we develop throughout the course.

### Statement and Proof

**Proposition 1.1.** For a sequence of sets $(E_n)_{n\ge1}$ in a measurable space $(X, \mathcal{F})$,
$$
\limsup_{n\to\infty} E_n=\bigcap_{k=1}^{\infty}\ \bigcup_{n\ge k} E_n
=\{x\in X:\ x\in E_n\ \text{for infinitely many } n\},
$$
$$
\liminf_{n\to\infty} E_n=\bigcup_{k=1}^{\infty}\ \bigcap_{n\ge k} E_n
=\{x\in X:\ x\in E_n\ \text{for all but finitely many } n\}.
$$

*Proof.*

**Proof of the $\limsup$ characterization.**

We establish both the forward and reverse inclusions.

**Forward inclusion ($\subseteq$):** Take $x\in\bigcap_{k\ge1}\bigcup_{n\ge k}E_n$. For each $k \in \mathbb{N}$, since $x \in \bigcup_{n \ge k} E_n$, we can choose an index $n_k\ge k$ such that $x\in E_{n_k}$. Since $k$ ranges over all natural numbers, we obtain a sequence of indices $(n_k)_{k=1}^{\infty}$ with $n_k \ge k$ for all $k$. This sequence is unbounded: if only finitely many distinct values appeared, say $n_k \in \{m_1, \ldots, m_J\}$ for all $k$, then for $k > \max\{m_1, \ldots, m_J\}$, we would need $n_k \ge k > \max\{m_i\}$, contradicting $n_k \in \{m_1, \ldots, m_J\}$. Thus infinitely many distinct indices must appear, so $x$ is in $E_n$ for infinitely many $n$.

**Reverse inclusion ($\supseteq$):** Conversely, suppose $x$ belongs to $E_n$ for infinitely many $n$. For any fixed $k \in \mathbb{N}$, the set $\{n \ge k : x \in E_n\}$ is non-empty (since $x$ is in infinitely many $E_n$, at least one such index must be $\ge k$). Therefore there exists $n\ge k$ with $x\in E_n$, which means $x\in\bigcup_{n\ge k}E_n$. Since this holds for every $k$, we have $x\in\bigcap_{k\ge1}\bigcup_{n\ge k}E_n$.

**Proof of the $\liminf$ characterization.**

**Forward inclusion ($\subseteq$):** Take $x\in\bigcup_{k\ge1}\bigcap_{n\ge k}E_n$. Then for some $k_0 \in \mathbb{N}$, we have $x\in\bigcap_{n\ge k_0}E_n$. This means $x\in E_n$ for all $n\ge k_0$, which is precisely the definition of "$x$ is in $E_n$ for all but finitely many $n$" (the finite exceptions being $n < k_0$).

**Reverse inclusion ($\supseteq$):** Conversely, if $x$ is in $E_n$ for all but finitely many $n$, then there exists $N \in \mathbb{N}$ such that $x\in E_n$ for all $n\ge N$. Thus $x\in\bigcap_{n\ge N}E_n$, which implies $x\in\bigcup_{k\ge1}\bigcap_{n\ge k}E_n$.
$\square$

### Complementary Results

**Proposition 1.2 (De Morgan Laws for Limits).**
$$
(\limsup E_n)^c=\liminf(E_n^{\,c}),\qquad
(\liminf E_n)^c=\limsup(E_n^{\,c}).
$$

*Proof.* These follow directly from De Morgan's laws for unions and intersections applied to the definitions. For example,
$$
(\limsup E_n)^c = \left(\bigcap_{k=1}^{\infty} \bigcup_{n\ge k} E_n\right)^c = \bigcup_{k=1}^{\infty} \bigcap_{n\ge k} E_n^c = \liminf(E_n^c).
$$
The second equality is analogous. $\square$

**Why this is useful:** In probability, $(\limsup E_n)^c$ is the event "eventually, $E_n$ stops occurring," which is precisely $\liminf E_n^c$.

### Connection to Numerical Limits

The set-theoretic limits $\limsup E_n$ and $\liminf E_n$ have an elegant connection to numerical limits via indicator functions. This perspective bridges set limits and numerical convergence, and is essential for probability theory—particularly when proving almost-sure convergence results in stochastic approximation (Weeks 34-39).

**Proposition 1.3 (Indicator Function Characterization).** For a sequence of sets $(E_n)_{n \ge 1}$ in a measurable space $(X, \mathcal{F})$, define the indicator function $\mathbf{1}_{E_n}: X \to \{0,1\}$ by $\mathbf{1}_{E_n}(x) = 1$ if $x \in E_n$ and $\mathbf{1}_{E_n}(x) = 0$ otherwise. Then for each $x \in X$:
$$
\mathbf{1}_{\limsup E_n}(x)=\limsup_{n\to\infty} \mathbf{1}_{E_n}(x),\qquad
\mathbf{1}_{\liminf E_n}(x)=\liminf_{n\to\infty} \mathbf{1}_{E_n}(x),
$$
where $\limsup_{n} a_n = \lim_{k \to \infty} \sup_{n \ge k} a_n$ and $\liminf_{n} a_n = \lim_{k \to \infty} \inf_{n \ge k} a_n$ for sequences of real numbers.

*Proof.* We prove the $\limsup$ characterization; the $\liminf$ case is analogous.

**Step 1 (Forward direction: $\mathbf{1}_{\limsup E_n}(x) = 1 \Rightarrow \limsup_n \mathbf{1}_{E_n}(x) = 1$).**

If $\mathbf{1}_{\limsup E_n}(x) = 1$, then $x \in \limsup E_n = \{x : x \in E_n \text{ for infinitely many } n\}$ by Proposition 1.1. Thus for every $k \in \mathbb{N}$, there exists $n \ge k$ such that $x \in E_n$, which means $\mathbf{1}_{E_n}(x) = 1$. Therefore $\sup_{n \ge k} \mathbf{1}_{E_n}(x) = 1$ for all $k$, which implies $\limsup_n \mathbf{1}_{E_n}(x) = \lim_{k \to \infty} \sup_{n \ge k} \mathbf{1}_{E_n}(x) = 1$.

**Step 2 (Reverse direction: $\limsup_n \mathbf{1}_{E_n}(x) = 1 \Rightarrow \mathbf{1}_{\limsup E_n}(x) = 1$).**

If $\limsup_n \mathbf{1}_{E_n}(x) = 1$, then $\sup_{n \ge k} \mathbf{1}_{E_n}(x) = 1$ for all $k$. This means for every $k$, there exists $n \ge k$ with $\mathbf{1}_{E_n}(x) = 1$, i.e., $x \in E_n$. Thus $x$ belongs to $E_n$ for infinitely many $n$, so $x \in \limsup E_n$, which gives $\mathbf{1}_{\limsup E_n}(x) = 1$.

**Step 3 (Case when $\mathbf{1}_{\limsup E_n}(x) = 0$).**

If $\mathbf{1}_{\limsup E_n}(x) = 0$, then $x \notin \limsup E_n$, so $x$ is in $E_n$ for only finitely many $n$ (the negation of "infinitely often"). Thus there exists $k_0$ such that $x \notin E_n$ for all $n \ge k_0$, which means $\mathbf{1}_{E_n}(x) = 0$ for all $n \ge k_0$. Therefore $\sup_{n \ge k_0} \mathbf{1}_{E_n}(x) = 0$, so $\limsup_n \mathbf{1}_{E_n}(x) = \lim_{k \to \infty} \sup_{n \ge k} \mathbf{1}_{E_n}(x) = 0$.

The proof for $\liminf$ follows the same pattern, using the characterization "$x \in \liminf E_n$ if and only if $x \in E_n$ for all but finitely many $n$." $\square$

**Why this connection matters (Preview for Probability and RL):**

In stochastic approximation (Weeks 34-39), proving a learning algorithm converges almost surely often reduces to showing $\liminf_{n \to \infty} \mathbf{1}_{E_n} = 1$ almost surely, where $E_n = \{\text{error}_n < \varepsilon\}$. The indicator viewpoint allows us to:
- Apply numerical convergence theorems (Fatou's lemma, dominated convergence) to sequences of indicators
- Use martingale convergence results (Week 6) to prove $\liminf \mathbf{1}_{E_n} = 1$ a.s.
- Connect set-theoretic "eventually always in $E_n$" to numerical "$\liminf \mathbf{1}_{E_n} = 1$"

This unification of set limits and numerical limits is a fundamental bridge between measure theory and probability that we exploit heavily in convergence analysis.

---

## Exercise 2: $\sigma$-Finite and Semifinite Measures

### Motivation

Not all measures are created equal. The behavior of integrals and the validity of powerful convergence theorems depend critically on certain regularity properties. $\sigma$-Finiteness and semifiniteness are not mere technicalities—they determine when we can apply essential tools.

**Where $\sigma$-finiteness is required in RL:**

1. **Fubini-Tonelli Theorem (Week 2):** For **stochastic policies** $\pi(a|s)$ (formalized Week 23), computing expectations over the joint state-action space $(s, a) \sim \rho(s) \pi(a|s)$—as in policy gradient objectives
   $$\mathbb{E}_{s \sim \rho, a \sim \pi(\cdot|s)}[\nabla \log \pi(a|s) Q(s,a)] = \int_{\mathcal{S}} \int_{\mathcal{A}} \nabla \log \pi(a|s) Q(s,a) \, \pi(da|s) \, \rho(ds)$$
   requires Fubini-Tonelli to interchange integration order (from $\int_{\mathcal{S}} \int_{\mathcal{A}}$ to $\int_{\mathcal{A}} \int_{\mathcal{S}}$ when needed for derivations), which demands $\sigma$-finiteness of both $\mathcal{S}$ and $\mathcal{A}$ [@folland:real_analysis:1999, §2.4]. This is essential for deriving the policy gradient theorem (Week 35).

   **Clarification on deterministic vs. stochastic policies:** For **deterministic policies** $\pi: \mathcal{S} \to \mathcal{A}$, we compute expectations as $\mathbb{E}_{s \sim \rho}[f(s, \pi(s))] = \int_{\mathcal{S}} f(s, \pi(s)) \, \rho(ds)$, which is a single integral over $\mathcal{S}$ only—no product measure is involved, and $\sigma$-finiteness is not required for this operation. The subtlety arises only for **stochastic policies**, where $\pi(\cdot|s)$ is a transition kernel (a family of probability measures on $\mathcal{A}$ indexed by $s$). The joint expectation over $(s,a)$ involves product measure structure, and Fubini-Tonelli's applicability depends on $\sigma$-finiteness of the underlying spaces. This distinction becomes critical when deriving policy gradient theorems for stochastic policies (Week 35).

2. **Radon-Nikodym Theorem (Week 3):** Existence of probability densities—likelihood ratios for importance sampling (Week 38), policy gradient theorems [@sutton:policy_gradient:2000] (Week 35)—requires $\sigma$-finiteness [@folland:real_analysis:1999, §3.2].

3. **Product Measures (Weeks 2-4):** Finite product measures are introduced in **Week 2** (Fubini-Tonelli). Constructing probability measures on **infinite** trajectory spaces $(\mathcal{S} \times \mathcal{A})^{\mathbb{N}}$ requires the Kolmogorov extension theorem (**Week 4** preview; full treatment in Week 10 for general state spaces).

Most RL theory assumes $\sigma$-finite measure spaces (e.g., Lebesgue measure on $\mathbb{R}^n$ for continuous states, counting measure on finite/countable state spaces). Understanding the boundaries of this assumption clarifies when our theorems apply.

### Core Theory

We recall key definitions from Day 1 §II-III:

**Definition 2.1 (Measure).** Let $(X, \mathcal{F})$ be a measurable space. A function $\mu: \mathcal{F} \to [0, \infty]$ is a **measure** if:
1.  $\mu(\emptyset) = 0$.
2.  (Countable Additivity) For any countable collection $\{A_n\}_{n=1}^{\infty}$ of pairwise disjoint sets in $\mathcal{F}$,
    $$ \mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n) $$

**Definition 2.2 ($\sigma$-Finite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **$\sigma$-finite** if there exists a countable collection $\{E_n\}_{n=1}^{\infty} \subseteq \mathcal{F}$ such that:
$$ X = \bigcup_{n=1}^{\infty} E_n \quad \text{and} \quad \mu(E_n) < \infty \text{ for all } n \in \mathbb{N} $$

In essence, a $\sigma$-finite space can be exhausted by a countable sequence of finite-measure "pieces."

**Example 2.1 (Lebesgue Measure on $\mathbb{R}^n$).** The standard Lebesgue measure $\lambda$ on $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$ is $\sigma$-finite [@folland:real_analysis:1999, §1.4]. For $n=1$, write $\mathbb{R} = \bigcup_{k=1}^{\infty} [-k, k]$ with $\lambda([-k, k]) = 2k < \infty$. For general $n$, use $\mathbb{R}^n = \bigcup_{k=1}^{\infty} [-k, k]^n$ with $\lambda([-k,k]^n) = (2k)^n < \infty$. This is the canonical measure for continuous state spaces in RL.

**Definition 2.3 (Semifinite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **semifinite** if for every set $A \in \mathcal{F}$ with $\mu(A) = \infty$, there exists a subset $B \in \mathcal{F}$ such that $B \subseteq A$ and $0 < \mu(B) < \infty$.

A semifinite measure does not permit "purely infinite" measurable sets that contain no measurable subsets of finite, non-zero measure.

### The Relationship Between Classifications

**Proposition 2.1 (Proven in Day 1 FINAL §III.A).** Let $(X, \mathcal{F}, \mu)$ be a measure space. If $\mu$ is $\sigma$-finite, then $\mu$ is semifinite. However, the converse is not true: there exist semifinite measures that are not $\sigma$-finite.

The proof is given in Day 1 §III.A, Proposition 1.1. The key idea:
- **$\sigma$-finite ⇒ semifinite:** Decompose any infinite-measure set $A$ using the $\sigma$-finite covering $X = \bigcup E_n$. By subadditivity, at least one $A \cap E_n$ has positive finite measure.
- **Counterexample:** Counting measure on $\mathbb{R}$ (assigning $|A|$ to finite sets, $\infty$ otherwise) is semifinite but not $\sigma$-finite, since $\mathbb{R}$ cannot be covered by countably many finite sets.

**Remark.** The pathological counting measure on uncountable spaces is precisely the type of measure we avoid in RL by restricting to **Polish spaces** (complete separable metric spaces) with Radon measures (finite on compact sets). Standard RL state spaces—finite sets, $\mathbb{R}^n$, or Polish spaces like $[0,1]^{\infty}$—all admit natural $\sigma$-finite measures.

---

## Exercise 3: Measurability of Arithmetic Operations and Compositions

### Motivation

In reinforcement learning, we constantly combine and compose functions:
- **Arithmetic operations:** Value functions are combined: $V(s) = R(s) + \gamma \mathbb{E}[V(s')]$
- **State features:** A measurable function $\phi: \mathcal{S} \to \mathbb{R}^d$ extracts features from raw states
- **Neural networks:** A function approximator maps features to value estimates

We must ensure these operations preserve measurability, so that expectations remain well-defined.

### Part A: Closure under Arithmetic Operations

**Proposition 3.1 (From Day 1 FINAL, Proposition 1.3).** Let $f, g: (X, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ be measurable. Then the sum $f+g$ and product $f \cdot g$ are measurable.

*Proof.*

**(i) Sum is measurable:**
We show $\{x \mid f(x)+g(x) < a\} \in \mathcal{F}$ for any $a \in \mathbb{R}$.

**Why this suffices:** The collection $\{(-\infty, a) : a \in \mathbb{R}\}$ of open rays generates the Borel $\sigma$-algebra $\mathcal{B}(\mathbb{R})$ (as noted in Day 1 §I.A, Remark on Generating Classes). By the **generating class criterion** (Lemma 3.1 below), checking preimages for this generating class suffices to prove measurability. We formalize this principle rigorously in Part B.

The key insight: $f(x) + g(x) < a$ if and only if there exists $q \in \mathbb{Q}$ with $f(x) < q$ and $g(x) < a-q$. Thus:
$$
\{x \mid f(x) + g(x) < a\} = \bigcup_{q \in \mathbb{Q}} (\{x \mid f(x) < q\} \cap \{x \mid g(x) < a-q\})
$$

For each $q$, both sets in the intersection are measurable (by measurability of $f$ and $g$), so their intersection is measurable. The result is a countable union of measurable sets, hence measurable.

**(ii) Product is measurable:**
We first show $f^2$ is measurable. For $a \ge 0$:
$$
\{x \mid f(x)^2 < a\} = \{x \mid -\sqrt{a} < f(x) < \sqrt{a}\}
= \{x \mid f(x) < \sqrt{a}\} \cap \{x \mid f(x) > -\sqrt{a}\}
$$

For $a < 0$, the set $\{x \mid f(x)^2 < a\} = \emptyset$ (empty set) since squares are non-negative. In both cases, the preimage is measurable.

Both sets are measurable, so $f^2$ is measurable. By (i), $f+g$ is measurable, so $(f+g)^2$ is measurable. Using the identity:
$$
f \cdot g = \frac{1}{2}((f+g)^2 - f^2 - g^2)
$$
we conclude $f \cdot g$ is measurable as a linear combination of measurable functions.
$\square$

*Remark (Extension to $\mathbb{R}^n$).* The proof above applies **verbatim** to functions $f, g: (X, \mathcal{F}) \to (\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$ by working component-wise: if $f = (f_1, \ldots, f_n)$ and $g = (g_1, \ldots, g_n)$ are measurable, then $f + g = (f_1 + g_1, \ldots, f_n + g_n)$ is measurable since each component $f_i + g_i$ is measurable by the scalar case. This is crucial for feature maps $\phi: \mathcal{S} \to \mathbb{R}^d$ in deep RL (Week 34-35).

*Remark (On Generality).* The proof uses only the density of $\mathbb{Q}$ in $\mathbb{R}$ and basic set operations.

**For addition and scalar multiplication**, the result extends immediately to measurable functions taking values in any **second-countable topological vector space** (e.g., $\mathbb{R}^n$, $\ell^2$, $C([0,1])$), where these operations are continuous.

**For products**, we must restrict to spaces with compatible algebraic structure: **topological algebras** where a continuous bilinear multiplication map $m: X \times X \to X$ is defined. Examples include:
- $\mathbb{R}^n$ with componentwise product
- $C(K)$ (continuous functions on compact $K$) with pointwise product
- $L^\infty$ with pointwise product

In a general topological vector space like $\ell^2$, pointwise multiplication need not map $\ell^2 \times \ell^2 \to \ell^2$ (the product of two square-summable sequences need not be square-summable). More precisely, whenever a continuous **bilinear** map $m: X \times X \to Y$ is given, the composition $(f,g) \mapsto m(f,g)$ preserves measurability. For reinforcement learning—where state spaces are subsets of $\mathbb{R}^n$ and value functions are real-valued—the statement above is the natural form. We will revisit this generality in **Week 12** when developing Banach-valued measurable functions for operator-theoretic approaches to MDPs.

### Part B: Closure under Composition with Continuous Functions

**Proposition 3.2.** Let $(X, \mathcal{F})$ be a measurable space. Let $g: X \to \mathbb{R}$ be measurable (with respect to $\mathcal{B}(\mathbb{R})$), and let $f: \mathbb{R} \to \mathbb{R}$ be continuous. Then the composition $h = f \circ g: X \to \mathbb{R}$ is measurable.

### Proof Strategy

To prove $h$ is measurable, we must show $h^{-1}(B) \in \mathcal{F}$ for all $B \in \mathcal{B}(\mathbb{R})$. Since $\mathcal{B}(\mathbb{R})$ contains uncountably many sets, checking this directly is impossible. The key insight is that we only need to check preimages for a *generating class*.

**Lemma 3.1 (Measurability Criterion via Generators).** Let $(X, \mathcal{F})$ and $(Y, \mathcal{G})$ be measurable spaces. Suppose $\mathcal{C} \subseteq 2^Y$ generates $\mathcal{G}$ (i.e., $\sigma(\mathcal{C}) = \mathcal{G}$). Then a function $\phi: X \to Y$ is measurable if and only if $\phi^{-1}(C) \in \mathcal{F}$ for every $C \in \mathcal{C}$.

*Proof.* The "only if" direction is immediate: if $\phi$ is measurable and $\mathcal{C} \subseteq \mathcal{G}$, then $\phi^{-1}(C) \in \mathcal{F}$ for all $C \in \mathcal{C}$.

For the "if" direction, define:
$$ \mathcal{G}' = \{B \subseteq Y \mid \phi^{-1}(B) \in \mathcal{F}\} $$

We verify that $\mathcal{G}'$ is a $\sigma$-algebra:
1. $Y \in \mathcal{G}'$ since $\phi^{-1}(Y) = X \in \mathcal{F}$.
2. If $B \in \mathcal{G}'$, then $\phi^{-1}(B^c) = (\phi^{-1}(B))^c \in \mathcal{F}$ (since $\mathcal{F}$ is closed under complements), so $B^c \in \mathcal{G}'$.
3. If $\{B_n\}_{n=1}^{\infty} \subseteq \mathcal{G}'$, then $\phi^{-1}(\bigcup_{n=1}^{\infty} B_n) = \bigcup_{n=1}^{\infty} \phi^{-1}(B_n) \in \mathcal{F}$ (since $\mathcal{F}$ is closed under countable unions), so $\bigcup_{n=1}^{\infty} B_n \in \mathcal{G}'$.

By hypothesis, $\mathcal{C} \subseteq \mathcal{G}'$. Since $\mathcal{G}'$ is a $\sigma$-algebra containing $\mathcal{C}$, and $\mathcal{G} = \sigma(\mathcal{C})$ is the *smallest* such $\sigma$-algebra, we have $\mathcal{G} \subseteq \mathcal{G}'$. Thus for any $B \in \mathcal{G}$, we have $\phi^{-1}(B) \in \mathcal{F}$, proving $\phi$ is measurable. $\square$

**Remark (The Good Sets Principle).** The proof above exemplifies a fundamental technique in measure theory: to prove a property holds for all sets in a generated $\sigma$-algebra $\sigma(\mathcal{C})$, we define the collection of "good" sets (those with the desired property), verify it forms a $\sigma$-algebra, and show it contains the generating class $\mathcal{C}$. By minimality of $\sigma(\mathcal{C})$, we conclude the property holds for all sets in $\sigma(\mathcal{C})$.

This strategy is called the **good sets principle** (or **Dynkin class method**) and is formalized rigorously via the **$\pi-\lambda$ theorem** in Appendix A2.1 ([THM-2.2.A1], Week 2, Day 2). The proof above is self-contained and requires no knowledge of the $\pi-\lambda$ theorem. However, recognizing this proof pattern will help you navigate similar arguments throughout measure theory and probability—it recurs constantly when working with generated $\sigma$-algebras.

*Proof of Proposition 3.2.*

Let $\mathcal{O}(\mathbb{R})$ denote the collection of open sets in $\mathbb{R}$. It is well-known that $\sigma(\mathcal{O}(\mathbb{R})) = \mathcal{B}(\mathbb{R})$. By the generator criterion (Lemma 3.1), it suffices to check preimages of open sets. That is, we need only show $h^{-1}(U) \in \mathcal{F}$ for every open set $U \subseteq \mathbb{R}$.

**Step 1:** Express the preimage using composition.

For any set $U \subseteq \mathbb{R}$, we have $h^{-1}(U) = (f \circ g)^{-1}(U) = g^{-1}(f^{-1}(U))$.

**Step 2:** Analyze $f^{-1}(U)$ for open $U$.

Let $U \subseteq \mathbb{R}$ be open. Since $f: \mathbb{R} \to \mathbb{R}$ is continuous, the preimage $V = f^{-1}(U)$ is open (by the topological definition of continuity).

**Step 3:** Analyze $g^{-1}(V)$ for open $V$.

From Step 2, $V$ is open, hence $V \in \mathcal{B}(\mathbb{R})$. Since $g: X \to \mathbb{R}$ is measurable, we have $g^{-1}(V) \in \mathcal{F}$.

**Step 4:** Conclude.

From Steps 1-3, for any open set $U \subseteq \mathbb{R}$:
$$ h^{-1}(U) = g^{-1}(f^{-1}(U)) = g^{-1}(V) \in \mathcal{F} $$
where $V = f^{-1}(U)$ is open by continuity of $f$, and $g^{-1}(V) \in \mathcal{F}$ by measurability of $g$.

Since $h^{-1}(U) \in \mathcal{F}$ for all $U \in \mathcal{O}(\mathbb{R})$, and $\mathcal{O}(\mathbb{R})$ generates $\mathcal{B}(\mathbb{R})$, Lemma 3.1 implies $h$ is measurable. $\square$

### Application to Neural Networks

  **Notation.** Throughout RL theory, we use the following standard notation for neural network function approximators:
  - $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}$ denotes a **neural network** with parameters $\theta$ (weights and biases), mapping $d$-dimensional feature vectors to scalar outputs (e.g., value function estimates)
  - For Q-functions (state-action value functions): $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}^{|\mathcal{A}|}$ outputs a vector of Q-values, where $\mathcal{A}$ denotes the action space and $|\mathcal{A}|$ is the number of available actions (e.g., for Atari games with 18 actions, $|\mathcal{A}| = 18$, so the network outputs $\mathbb{R}^{18}$)
  - The subscript $\theta$ emphasizes the parametrization, distinguishing different network instantiations during training

**Corollary 3.3 (Measurability of Neural Network Value Functions).** Let $(\mathcal{S}, \mathcal{F}_\mathcal{S})$ be a measurable state space. If $\phi: \mathcal{S} \to \mathbb{R}^d$ is measurable and the neural network $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}$ is continuous, then the composed value function $V_\theta = \text{NN}_\theta \circ \phi: \mathcal{S} \to \mathbb{R}$ is measurable.

**Why neural networks are measurable (addressing ReLU non-differentiability):**

Modern deep RL uses neural networks with ReLU activations. A common question arises: "Is ReLU continuous?" The answer is **yes**—ReLU is continuous everywhere, though it is **non-differentiable** at a single point (0).

**Clarifying ReLU structure in layers:**

The **scalar ReLU function** $\text{ReLU}(x) = \max(0, x)$ on $\mathbb{R}$ is continuous at every point, including $x=0$ (left and right limits both equal 0). However, ReLU layers apply this element-wise to vectors:
$$ \text{ReLU}(\mathbf{x}) = (\max(0, x_1), \ldots, \max(0, x_d)) $$

A feedforward ReLU network is a composition:
$$ \text{NN}_\theta = \text{Linear}_L \circ \text{ReLU}_{L-1} \circ \text{Linear}_{L-1} \circ \cdots \circ \text{ReLU}_1 \circ \text{Linear}_1 $$

where each $\text{Linear}_k$ is an affine map (matrix multiplication + bias), which is continuous. Each ReLU layer is continuous (as the componentwise max of continuous functions).

**Why measurability holds:**
- Each affine layer $\text{Linear}_k: \mathbb{R}^{n_k} \to \mathbb{R}^{n_{k+1}}$ is continuous, hence Borel measurable
- Each ReLU layer $\text{ReLU}_k: \mathbb{R}^{n_k} \to \mathbb{R}^{n_k}$ is continuous (continuous in each component), hence Borel measurable
- By Proposition 3.2, a composition of continuous functions is continuous, hence measurable
- The full network $\text{NN}_\theta$ is therefore continuous and Borel measurable
- Composing the measurable feature map $\phi$ with the continuous network $\text{NN}_\theta$ (via Proposition 3.2) yields a measurable value function $V_\theta$

**Non-differentiability vs. continuity:**
While ReLU is **non-differentiable** at points where the pre-activation equals zero (forming hyperplanes $\{x \in \mathbb{R}^d : w^T x + b = 0\}$ in the input space), these sets have **Lebesgue measure zero** in $\mathbb{R}^d$. However, for measurability purposes, this is irrelevant—ReLU networks are **everywhere continuous**, not merely "continuous almost everywhere." Continuity is strictly stronger than Borel measurability, so the argument is even simpler than an "a.e. continuity" approach would suggest.

**Practical implication:** Modern deep RL uses ReLU networks with $10^4$–$10^6$ neurons (e.g., Atari DQN has ~$10^6$ parameters). While these networks are non-differentiable on a union of measure-zero hyperplanes (one per neuron), they remain **continuous everywhere**. Measurability is preserved, ensuring that expectations like $\mathbb{E}_{s \sim \rho}[V_\theta(s)]$ are well-defined.

**Technical note:** Even if we had discontinuities on a measure-positive set, compositions of measurable functions remain measurable (though continuity is not preserved). Measurability is preserved under far more general operations than continuity, which is why it is the correct framework for RL function approximators.

**Concrete example (DQN [@mnih:dqn:2015]):**

In deep Q-learning:
- States $s \in \mathcal{S}$ (e.g., $84 \times 84$ grayscale images) define a measurable space with Borel $\sigma$-algebra.
- The pixel representation $s \mapsto \text{pixels}(s) \in [0,255]^{84 \times 84}$ is measurable (identity map on a Borel space).
- The Q-network $Q_\theta: [0,255]^{84 \times 84} \to \mathbb{R}^{|\mathcal{A}|}$ (convolutional layers + ReLU + linear layers) is Borel measurable.

**Why $Q_\theta$ is measurable:** The DQN architecture is a composition:
   $$Q_\theta = \text{Linear}_3 \circ \text{ReLU}_2 \circ \text{Conv}_2 \circ \text{ReLU}_1 \circ \text{Conv}_1$$
   Each convolutional layer $\text{Conv}_k: \mathbb{R}^{n$\times$m$\times$c} \to \mathbb{R}^{n'$\times$m'$\times$c'}$ is a **linear map** (matrix multiplication in tensor form) followed by bias addition—hence continuous, therefore Borel measurable. Each ReLU layer is continuous everywhere (non-differentiable on measure-zero sets, but still continuous). By Proposition 3.2 applied iteratively:
   - $\text{Conv}_1$ is continuous (hence measurable)
   - $\text{ReLU}_1$ is continuous (hence measurable)
   - $\text{Conv}_2 \circ \text{ReLU}_1$ is measurable (Proposition 3.2: continuous ∘ measurable)
   - Continuing this composition, $Q_\theta$ is measurable

   **Key insight:** Proposition 3.2 (continuous ∘ measurable = measurable) applies to **each layer**, ensuring the full network is measurable.

- By Proposition 3.2, $s \mapsto Q_\theta(s, a)$ is measurable for each action $a$.
- This ensures the expected Q-value $\mathbb{E}_{s \sim \rho}[Q_\theta(s,a)]$ is well-defined (integration of a measurable function with respect to a probability measure).

**Extension to policy gradients:** Stochastic policies in actor-critic methods (e.g., PPO [@schulman:ppo:2017], SAC [@haarnoja:sac:2018]) use neural networks to output distribution parameters (e.g., mean and variance of a Gaussian). As long as the network $\pi_\theta: \mathcal{S} \to \mathbb{R}^{2|\mathcal{A}|}$ (outputting $\mu, \sigma$ per action) is measurable and the Gaussian density $(a, \mu, \sigma) \mapsto \mathcal{N}(a; \mu, \sigma^2)$ is continuous in $(\mu, \sigma)$ (which it is), the policy density $\pi_\theta(a|s)$ is jointly measurable in $(s, a)$. This ensures policy gradient objectives are well-defined expectations.

---

## Summary

We have developed three foundational tools:

1. **$\limsup$ and $\liminf$ of sets** (Exercise 1) characterize asymptotic behavior of events, essential for analyzing exploration, recurrence, and almost-sure convergence in stochastic approximation (Weeks 34-39).

2. **$\sigma$-Finite measures** (Exercise 2) enable application of Fubini-Tonelli (Week 2), Radon-Nikodym (Week 3), and product measure constructions (Weeks 2-4)—the theoretical bedrock for computing expectations in RL. We proved that $\sigma$-finiteness is stronger than semifiniteness and identified pathological counterexamples.

3. **Measurability under operations** (Exercise 3) guarantees that:
   - Arithmetic combinations of measurable functions (like Bellman updates) remain measurable
   - Neural network policies and value functions (continuous, but non-differentiable at measure-zero sets) are well-defined probabilistic objects
   - Expectations like $\mathbb{E}[V_\theta(S)]$ are mathematically meaningful

These techniques recur throughout measure-theoretic RL. Mastering them now provides the foundation for rigorous convergence analysis in later weeks.
