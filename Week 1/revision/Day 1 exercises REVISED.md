[[Day 1]]

# Day 1 Exercises: Foundational Tools for Measure-Theoretic RL

These exercises develop essential technical skills for working with measure spaces and measurable functions. Having established the foundational definitions in Day 1, we now build computational fluency and proof techniques. We focus on three foundational skills: characterizing asymptotic set behavior, understanding measure regularity conditions, and ensuring function compositions preserve measurability. Each exercise illuminates concepts that recur throughout reinforcement learning theory.

---

## Exercise 1: Characterizations of Set $\limsup$ and $\liminf$

### Motivation

In reinforcement learning, we constantly reason about asymptotic behavior: Does a learning algorithm visit every state infinitely often? Do policy iterates converge almost surely? Does exploration decay appropriately? The mathematical language for such questions is the $\limsup$ and $\liminf$ of sequences of sets.

**Concrete RL applications:**
- **Exploration in Q-learning:** Convergence theorems require that each state-action pair $(s,a)$ is visited infinitely often almost surely, formalized as $P(\limsup_t \{(S_t, A_t) = (s,a)\}) = 1$.
- **Markov chain recurrence:** A state $s$ is recurrent if the event "return to $s$" occurs infinitely often with probability 1.
- **Almost-sure convergence:** Stochastic approximation algorithms converge if the event "error exceeds $\epsilon$" occurs only finitely often for every $\epsilon > 0$.

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

*Forward inclusion* $(\subseteq)$: Take $x\in\bigcap_{k\ge1}\bigcup_{n\ge k}E_n$. For each $k \in \mathbb{N}$, since $x \in \bigcup_{n \ge k} E_n$, we can choose an index $n_k\ge k$ such that $x\in E_{n_k}$. Since $k$ ranges over all natural numbers, we obtain infinitely many indices $n_k$ (not necessarily distinct). As $n_k \ge k$ and $k \to \infty$, the indices are unbounded, so infinitely many distinct values appear among them. Hence $x$ is in $E_n$ for infinitely many $n$.

*Reverse inclusion* $(\supseteq)$: Conversely, suppose $x$ belongs to $E_n$ for infinitely many $n$. For any fixed $k \in \mathbb{N}$, the set $\{n \ge k : x \in E_n\}$ is non-empty (since $x$ is in infinitely many $E_n$, at least one such index must be $\ge k$). Therefore there exists $n\ge k$ with $x\in E_n$, which means $x\in\bigcup_{n\ge k}E_n$. Since this holds for every $k$, we have $x\in\bigcap_{k\ge1}\bigcup_{n\ge k}E_n$.

**Proof of the $\liminf$ characterization.**

*Forward inclusion* $(\subseteq)$: Take $x\in\bigcup_{k\ge1}\bigcap_{n\ge k}E_n$. Then for some $k_0 \in \mathbb{N}$, we have $x\in\bigcap_{n\ge k_0}E_n$. This means $x\in E_n$ for all $n\ge k_0$, which is precisely the definition of "$x$ is in $E_n$ for all but finitely many $n$" (the finite exceptions being $n < k_0$).

*Reverse inclusion* $(\supseteq)$: Conversely, if $x$ is in $E_n$ for all but finitely many $n$, then there exists $N \in \mathbb{N}$ such that $x\in E_n$ for all $n\ge N$. Thus $x\in\bigcap_{n\ge N}E_n$, which implies $x\in\bigcup_{k\ge1}\bigcap_{n\ge k}E_n$.
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

**Remark (Indicator Function Viewpoint).** For each $x\in X$, the indicator function $\mathbf{1}_{E_n}(x)$ takes values in $\{0,1\}$. The numerical $\limsup$ and $\liminf$ of this sequence satisfy:
$$
\mathbf{1}_{\limsup E_n}(x)=\limsup_{n\to\infty} \mathbf{1}_{E_n}(x),\qquad
\mathbf{1}_{\liminf E_n}(x)=\liminf_{n\to\infty} \mathbf{1}_{E_n}(x),
$$
where $\limsup_{n} a_n = \lim_{k \to \infty} \sup_{n \ge k} a_n$ for sequences of real numbers. This connection is immediate from the characterizations: $\limsup \mathbf{1}_{E_n}(x)=1$ if and only if $\sup_{n \ge k} \mathbf{1}_{E_n}(x) = 1$ for all $k$, which holds if and only if $x\in E_n$ infinitely often.

---

## Exercise 2: σ-Finite and Semifinite Measures

### Motivation

Not all measures are created equal. The behavior of integrals and the validity of powerful convergence theorems depend critically on certain regularity properties. σ-Finiteness and semifiniteness are not mere technicalities—they determine when we can apply essential tools:

**Where σ-finiteness is required in RL:**
1. **Fubini-Tonelli Theorem:** Interchanging order of integration in $\mathbb{E}[V^\pi(S_0)] = \int \left(\int V^\pi(s) P(ds|s_0, a)\right) \pi(da|s_0)$ requires σ-finiteness of the state and action spaces, where $P(\cdot|s_0, a)$ is the transition kernel and $\pi(\cdot|s_0)$ is the policy distribution.
2. **Radon-Nikodym Theorem:** Existence of probability densities (likelihood ratios for importance sampling, policy gradient theorems) requires σ-finiteness.
3. **Product Measures:** Constructing probability measures on trajectory spaces $(\mathcal{S} \times \mathcal{A})^{\mathbb{N}}$ requires σ-finite marginals.

Most RL theory assumes σ-finite measure spaces (e.g., Lebesgue measure on $\mathbb{R}^n$ for continuous states, counting measure on finite/countable state spaces). Understanding the boundaries of this assumption clarifies when our theorems apply.

### Core Theory

We recall key definitions from Day 1:

**Definition 2.1 (Measure).** Let $(X, \mathcal{F})$ be a measurable space. A function $\mu: \mathcal{F} \to [0, \infty]$ is a **measure** if:
1.  $\mu(\emptyset) = 0$.
2.  (Countable Additivity) For any countable collection $\{A_n\}_{n=1}^{\infty}$ of pairwise disjoint sets in $\mathcal{F}$,
    $$ \mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n) $$

**Definition 2.2 (σ-Finite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **σ-finite** if there exists a countable collection $\{E_n\}_{n=1}^{\infty} \subseteq \mathcal{F}$ such that:
$$ X = \bigcup_{n=1}^{\infty} E_n \quad \text{and} \quad \mu(E_n) < \infty \text{ for all } n \in \mathbb{N} $$

In essence, a σ-finite space can be exhausted by a countable sequence of finite-measure "pieces."

**Example 2.1 (Lebesgue Measure on $\mathbb{R}^n$).** The standard Lebesgue measure $\lambda$ on $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$ is σ-finite. For $n=1$, write $\mathbb{R} = \bigcup_{k=1}^{\infty} [-k, k]$ with $\lambda([-k, k]) = 2k < \infty$. For general $n$, use $\mathbb{R}^n = \bigcup_{k=1}^{\infty} [-k, k]^n$ with $\lambda([-k,k]^n) = (2k)^n < \infty$. This is the canonical measure for continuous state spaces in RL.

**Definition 2.3 (Semifinite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **semifinite** if for every set $A \in \mathcal{F}$ with $\mu(A) = \infty$, there exists a subset $B \in \mathcal{F}$ such that $B \subseteq A$ and $0 < \mu(B) < \infty$.

A semifinite measure does not permit "purely infinite" measurable sets that contain no measurable subsets of finite, non-zero measure.

### The Relationship Between Classifications

**Proposition 2.1.** Let $(X, \mathcal{F}, \mu)$ be a measure space. If $\mu$ is σ-finite, then $\mu$ is semifinite. However, the converse is not true: there exist semifinite measures that are not σ-finite.

*Proof.*

**(i) σ-finiteness implies semifiniteness.**

Suppose $\mu$ is σ-finite. Then there exists a sequence $\{E_n\}_{n=1}^{\infty} \subseteq \mathcal{F}$ with $X = \bigcup_{n=1}^{\infty} E_n$ and $\mu(E_n) < \infty$ for all $n$.

Let $A \in \mathcal{F}$ with $\mu(A) = \infty$. We seek a measurable subset $B \subseteq A$ with $0 < \mu(B) < \infty$.

Since $A \subseteq X$, we can decompose:
$$ A = A \cap X = A \cap \left(\bigcup_{n=1}^{\infty} E_n\right) = \bigcup_{n=1}^{\infty} (A \cap E_n) $$

By countable subadditivity (which follows from countable additivity and monotonicity),
$$ \mu(A) \le \sum_{n=1}^{\infty} \mu(A \cap E_n) $$

Since $\mu(A) = \infty$ and the sum $\sum_{n=1}^{\infty} \mu(A \cap E_n)$ is infinite (each term is non-negative), there must exist $n_0 \in \mathbb{N}$ such that $\mu(A \cap E_{n_0}) > 0$.

Define $B = A \cap E_{n_0}$. We verify:
1.  $B \subseteq A$ by construction.
2.  $B \in \mathcal{F}$ since σ-algebras are closed under finite intersections.
3.  $\mu(B) = \mu(A \cap E_{n_0}) > 0$ by our choice of $n_0$.
4.  By monotonicity, $\mu(B) = \mu(A \cap E_{n_0}) \le \mu(E_{n_0}) < \infty$ (using σ-finiteness of $E_{n_0}$).

Thus $B$ satisfies the definition of semifiniteness. Since $A$ was arbitrary, $\mu$ is semifinite.

**(ii) Counterexample: Semifinite but not σ-finite.**

We construct the **counting measure on an uncountable set.**

Let $X = \mathbb{R}$ (any uncountable set suffices). Let $\mathcal{F} = 2^X$ (the power set—all subsets are measurable). Define:
$$ \mu_c(A) = \begin{cases} |A| & \text{if } A \text{ is finite} \\ \infty & \text{if } A \text{ is infinite} \end{cases} $$

**Claim 1:** $\mu_c$ is semifinite.

Let $A \in \mathcal{F}$ with $\mu_c(A) = \infty$. Then $A$ is infinite, hence non-empty. Choose any $x \in A$ and let $B = \{x\}$. Then:
- $B \subseteq A$ and $B \in \mathcal{F}$.
- $\mu_c(B) = |\{x\}| = 1 \in (0, \infty)$.

Thus $\mu_c$ is semifinite.

**Claim 2:** $\mu_c$ is not σ-finite.

Assume for contradiction that $\mu_c$ is σ-finite. Then there exist sets $\{E_n\}_{n=1}^{\infty} \subseteq \mathcal{F}$ with $X = \bigcup_{n=1}^{\infty} E_n$ and $\mu_c(E_n) < \infty$ for all $n$.

The condition $\mu_c(E_n) < \infty$ forces each $E_n$ to be finite. Thus:
$$ X = \bigcup_{n=1}^{\infty} E_n \quad \text{where each } E_n \text{ is finite} $$

**Lemma (Set Theory).** A countable union of finite sets is at most countable.

*Proof of Lemma.* For each finite set $E_n$, let $|E_n| = k_n < \infty$. We define an injection $\iota: \bigcup_{n=1}^{\infty} E_n \to \mathbb{N} \times \mathbb{N}$ as follows: for $x \in \bigcup_n E_n$, let $n_0 = \min\{n : x \in E_n\}$ and choose an enumeration of $E_{n_0} = \{x_1, \ldots, x_{k_{n_0}}\}$ with $x = x_i$ for some $i$. Then $\iota(x) = (n_0, i)$. Since $\mathbb{N} \times \mathbb{N}$ is countable, so is $\bigcup_{n=1}^{\infty} E_n$. $\square$

By the lemma, $X$ is at most countable. But $X = \mathbb{R}$ is uncountable—a contradiction. Therefore, $\mu_c$ is not σ-finite.

We have constructed a measure that is semifinite but not σ-finite. $\square$

**Remark.** The pathological counting measure on uncountable spaces is precisely the type of measure we avoid in RL by restricting to Polish spaces (complete separable metric spaces) with Radon measures (finite on compact sets). Standard RL state spaces—finite sets, $\mathbb{R}^n$, or Polish spaces like $[0,1]^{\infty}$—all admit natural σ-finite measures.

---

## Exercise 3: Composition of Measurable and Continuous Functions

### Motivation

In reinforcement learning, we frequently compose measurable functions with continuous functions:
- **State features:** A measurable function $\phi: \mathcal{S} \to \mathbb{R}^d$ extracts features from raw states.
- **Neural networks:** A continuous function $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}$ (or $\to \mathbb{R}^{|\mathcal{A}|}$) maps features to value estimates or policy logits.
- **Policy/value functions:** The composition $V_\theta = \text{NN}_\theta \circ \phi$ must be measurable for expectations like $\mathbb{E}_\pi[V_\theta(S_t)]$ to be well-defined.

The following result guarantees that such compositions preserve measurability, ensuring that our function approximators remain valid probabilistic objects.

### Statement

**Proposition 3.1.** Let $(X, \mathcal{F})$ be a measurable space. Let $g: X \to \mathbb{R}$ be measurable (with respect to $\mathcal{B}(\mathbb{R})$), and let $f: \mathbb{R} \to \mathbb{R}$ be continuous. Then the composition $h = f \circ g: X \to \mathbb{R}$ is measurable.

### Proof Strategy

To prove $h$ is measurable, we must show $h^{-1}(B) \in \mathcal{F}$ for all $B \in \mathcal{B}(\mathbb{R})$. Since $\mathcal{B}(\mathbb{R})$ contains uncountably many sets, checking this directly is impossible. The key insight is that we only need to check preimages for a *generating class*.

**Lemma 3.1 (Measurability Criterion via Generators).** Let $(X, \mathcal{F})$ and $(Y, \mathcal{G})$ be measurable spaces. Suppose $\mathcal{C} \subseteq 2^Y$ generates $\mathcal{G}$ (i.e., $\sigma(\mathcal{C}) = \mathcal{G}$). Then a function $\phi: X \to Y$ is measurable if and only if $\phi^{-1}(C) \in \mathcal{F}$ for every $C \in \mathcal{C}$.

*Proof of Lemma.* The "only if" direction is immediate: if $\phi$ is measurable and $\mathcal{C} \subseteq \mathcal{G}$, then $\phi^{-1}(C) \in \mathcal{F}$ for all $C \in \mathcal{C}$.

For the "if" direction, we use the *good sets principle.* Define:
$$ \mathcal{G}' = \{B \subseteq Y \mid \phi^{-1}(B) \in \mathcal{F}\} $$

We claim $\mathcal{G}'$ is a σ-algebra:
1. $Y \in \mathcal{G}'$ since $\phi^{-1}(Y) = X \in \mathcal{F}$.
2. If $B \in \mathcal{G}'$, then $\phi^{-1}(B^c) = (\phi^{-1}(B))^c \in \mathcal{F}$ (since $\mathcal{F}$ is closed under complements), so $B^c \in \mathcal{G}'$.
3. If $\{B_n\}_{n=1}^{\infty} \subseteq \mathcal{G}'$, then $\phi^{-1}(\bigcup_{n=1}^{\infty} B_n) = \bigcup_{n=1}^{\infty} \phi^{-1}(B_n) \in \mathcal{F}$ (since $\mathcal{F}$ is closed under countable unions), so $\bigcup_{n=1}^{\infty} B_n \in \mathcal{G}'$.

By hypothesis, $\mathcal{C} \subseteq \mathcal{G}'$. Since $\mathcal{G}'$ is a σ-algebra containing $\mathcal{C}$, and $\mathcal{G} = \sigma(\mathcal{C})$ is the *smallest* such σ-algebra, we have $\mathcal{G} \subseteq \mathcal{G}'$. Thus for any $B \in \mathcal{G}$, we have $\phi^{-1}(B) \in \mathcal{F}$, proving $\phi$ is measurable. $\square$

*Proof of Proposition 3.1.*

Let $\mathcal{O}(\mathbb{R})$ denote the collection of open sets in $\mathbb{R}$. It is well-known that $\sigma(\mathcal{O}(\mathbb{R})) = \mathcal{B}(\mathbb{R})$. By Lemma 3.1, it suffices to show $h^{-1}(U) \in \mathcal{F}$ for every open set $U \subseteq \mathbb{R}$.

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

**Corollary 3.1.** Let $(\mathcal{S}, \mathcal{F}_\mathcal{S})$ be a measurable state space. If $\phi: \mathcal{S} \to \mathbb{R}^d$ is measurable and $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}$ is continuous, then $V_\theta = \text{NN}_\theta \circ \phi: \mathcal{S} \to \mathbb{R}$ is measurable.

**Why neural networks are continuous:**
- Linear layers $x \mapsto Wx + b$ are continuous.
- Common activations (sigmoid, tanh, softmax) are continuous everywhere.
- ReLU is continuous except at a single point (0), hence Borel measurable (functions with countably many discontinuities are Borel measurable).

**Concrete example (DQN):** In deep Q-learning:
- States $s \in \mathcal{S}$ (e.g., $84 \times 84$ grayscale images) define a measurable space with Borel σ-algebra.
- The pixel representation $s \mapsto \text{pixels}(s) \in [0,255]^{84 \times 84}$ is measurable.
- The Q-network $Q_\theta: [0,255]^{84 \times 84} \to \mathbb{R}^{|\mathcal{A}|}$ (convolutional layers + ReLU + linear layers) is continuous (ReLU's single discontinuity point has no effect on measurability).
- By Proposition 3.1, $s \mapsto Q_\theta(s, a)$ is measurable for each action $a$.
- This ensures the expected Q-value $\mathbb{E}_{s \sim \rho}[Q_\theta(s,a)]$ is well-defined.

**Remark on Discontinuous Activations.** Even if a neural network contains discontinuous operations (e.g., ReLU is discontinuous at 0, argmax is discontinuous everywhere), the resulting function is still Borel measurable. This is because:
1. Functions with countably many discontinuities are Borel measurable (a fact from real analysis).
2. Compositions of measurable functions are measurable (though continuity is not preserved).

The key takeaway: **measurability is preserved under far more general operations than continuity**, which is why it is the correct framework for RL function approximators.

---

## Summary

We have developed three foundational tools:

1. **$\limsup$ and $\liminf$ of sets** characterize asymptotic behavior of events, essential for analyzing exploration, recurrence, and almost-sure convergence.

2. **σ-Finite measures** enable application of Fubini-Tonelli, Radon-Nikodym, and product measure constructions—the theoretical bedrock for computing expectations in RL.

3. **Composition of measurable and continuous functions** guarantees that neural network policies and value functions are well-defined probabilistic objects.

These techniques recur throughout measure-theoretic RL. Mastering them now provides the foundation for rigorous convergence analysis in later weeks.
