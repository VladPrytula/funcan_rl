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

**Concrete RL applications:**
- **Exploration in Q-learning:** Convergence theorems (Week 37) require that each state-action pair $(s,a)$ is visited infinitely often almost surely, formalized as $P(\limsup_t \{(S_t, A_t) = (s,a)\}) = 1$.
- **Markov chain recurrence:** A state $s$ is recurrent (Week 7) if the event "return to $s$" occurs infinitely often with probability 1.
- **Almost-sure convergence:** Stochastic approximation algorithms (Weeks 34-39) converge if the event "error exceeds $\epsilon$" occurs only finitely often for every $\epsilon > 0$.

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

**Forward inclusion ($\subseteq$):** Take $x\in\bigcap_{k\ge1}\bigcup_{n\ge k}E_n$. For each $k \in \mathbb{N}$, since $x \in \bigcup_{n \ge k} E_n$, we can choose an index $n_k\ge k$ such that $x\in E_{n_k}$. Since $k$ ranges over all natural numbers, we obtain infinitely many indices $n_k$ (not necessarily distinct). As $n_k \ge k$ and $k \to \infty$, the indices are unbounded, so infinitely many distinct values appear among them. Hence $x$ is in $E_n$ for infinitely many $n$.

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

**Remark (Indicator Function Viewpoint).** For each $x\in X$, the indicator function $\mathbf{1}_{E_n}(x)$ takes values in $\{0,1\}$. The numerical $\limsup$ and $\liminf$ of this sequence satisfy:
$$
\mathbf{1}_{\limsup E_n}(x)=\limsup_{n\to\infty} \mathbf{1}_{E_n}(x),\qquad
\mathbf{1}_{\liminf E_n}(x)=\liminf_{n\to\infty} \mathbf{1}_{E_n}(x),
$$
where $\limsup_{n} a_n = \lim_{k \to \infty} \sup_{n \ge k} a_n$ for sequences of real numbers. This connection is immediate from the characterizations: $\limsup \mathbf{1}_{E_n}(x)=1$ if and only if $\sup_{n \ge k} \mathbf{1}_{E_n}(x) = 1$ for all $k$, which holds if and only if $x\in E_n$ infinitely often.

---

## Exercise 2: σ-Finite and Semifinite Measures

### Motivation

Not all measures are created equal. The behavior of integrals and the validity of powerful convergence theorems depend critically on certain regularity properties. σ-Finiteness and semifiniteness are not mere technicalities—they determine when we can apply essential tools.

**Where σ-finiteness is required in RL:**
1. **Fubini-Tonelli Theorem (Week 3):** Interchanging order of integration in $\mathbb{E}[V^\pi(S_0)] = \int \left(\int V^\pi(s') P(ds'|s_0, a)\right) \pi(da|s_0)$ requires σ-finiteness of the state and action spaces [@folland:real_analysis:1999, §2.4], where $P(\cdot|s_0, a)$ is the transition kernel and $\pi(\cdot|s_0)$ is the policy distribution.
2. **Radon-Nikodym Theorem (Week 4):** Existence of probability densities—likelihood ratios for importance sampling (Week 40), policy gradient theorems [@sutton:policy_gradient:2000] (Week 37-38)—requires σ-finiteness [@folland:real_analysis:1999, §3.2].
3. **Product Measures (Week 3):** Constructing probability measures on trajectory spaces $(\mathcal{S} \times \mathcal{A})^{\mathbb{N}}$ requires σ-finite marginals.

Most RL theory assumes σ-finite measure spaces (e.g., Lebesgue measure on $\mathbb{R}^n$ for continuous states, counting measure on finite/countable state spaces). Understanding the boundaries of this assumption clarifies when our theorems apply.

### Core Theory

We recall key definitions from Day 1 §II-III:

**Definition 2.1 (Measure).** Let $(X, \mathcal{F})$ be a measurable space. A function $\mu: \mathcal{F} \to [0, \infty]$ is a **measure** if:
1.  $\mu(\emptyset) = 0$.
2.  (Countable Additivity) For any countable collection $\{A_n\}_{n=1}^{\infty}$ of pairwise disjoint sets in $\mathcal{F}$,
    $$ \mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n) $$

**Definition 2.2 (σ-Finite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **σ-finite** if there exists a countable collection $\{E_n\}_{n=1}^{\infty} \subseteq \mathcal{F}$ such that:
$$ X = \bigcup_{n=1}^{\infty} E_n \quad \text{and} \quad \mu(E_n) < \infty \text{ for all } n \in \mathbb{N} $$

In essence, a σ-finite space can be exhausted by a countable sequence of finite-measure "pieces."

**Example 2.1 (Lebesgue Measure on $\mathbb{R}^n$).** The standard Lebesgue measure $\lambda$ on $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$ is σ-finite [@folland:real_analysis:1999, §1.4]. For $n=1$, write $\mathbb{R} = \bigcup_{k=1}^{\infty} [-k, k]$ with $\lambda([-k, k]) = 2k < \infty$. For general $n$, use $\mathbb{R}^n = \bigcup_{k=1}^{\infty} [-k, k]^n$ with $\lambda([-k,k]^n) = (2k)^n < \infty$. This is the canonical measure for continuous state spaces in RL.

**Definition 2.3 (Semifinite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **semifinite** if for every set $A \in \mathcal{F}$ with $\mu(A) = \infty$, there exists a subset $B \in \mathcal{F}$ such that $B \subseteq A$ and $0 < \mu(B) < \infty$.

A semifinite measure does not permit "purely infinite" measurable sets that contain no measurable subsets of finite, non-zero measure.

### The Relationship Between Classifications

**Proposition 2.1 (Proven in Day 1 FINAL §III.A).** Let $(X, \mathcal{F}, \mu)$ be a measure space. If $\mu$ is σ-finite, then $\mu$ is semifinite. However, the converse is not true: there exist semifinite measures that are not σ-finite.

The proof is given in Day 1 §III.A, Proposition 1.1. The key idea:
- **σ-finite ⇒ semifinite:** Decompose any infinite-measure set $A$ using the σ-finite covering $X = \bigcup E_n$. By subadditivity, at least one $A \cap E_n$ has positive finite measure.
- **Counterexample:** Counting measure on $\mathbb{R}$ (assigning $|A|$ to finite sets, $\infty$ otherwise) is semifinite but not σ-finite, since $\mathbb{R}$ cannot be covered by countably many finite sets.

**Remark.** The pathological counting measure on uncountable spaces is precisely the type of measure we avoid in RL by restricting to **Polish spaces** (complete separable metric spaces) with Radon measures (finite on compact sets). Standard RL state spaces—finite sets, $\mathbb{R}^n$, or Polish spaces like $[0,1]^{\infty}$—all admit natural σ-finite measures.

---

## Exercise 3: Measurability of Arithmetic Operations and Compositions

### Motivation

In reinforcement learning, we constantly combine and compose functions:
- **Arithmetic operations:** Value functions are combined: $V(s) = R(s) + \gamma \mathbb{E}[V(s')]$
- **State features:** A measurable function $\phi: \mathcal{S} \to \mathbb{R}^d$ extracts features from raw states
- **Neural networks:** A function $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}$ maps features to value estimates

We must ensure these operations preserve measurability, so that expectations remain well-defined.

### Part A: Closure under Arithmetic Operations

**Proposition 3.1 (From Day 1 FINAL, Proposition 1.3).** Let $f, g: (X, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ be measurable. Then the sum $f+g$ and product $f \cdot g$ are measurable.

*Proof.*

**(i) Sum is measurable:**
We show $\{x \mid f(x)+g(x) < a\} \in \mathcal{F}$ for any $a \in \mathbb{R}$.

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

Both sets are measurable, so $f^2$ is measurable. By (i), $f+g$ is measurable, so $(f+g)^2$ is measurable. Using the identity:
$$
f \cdot g = \frac{1}{2}((f+g)^2 - f^2 - g^2)
$$
we conclude $f \cdot g$ is measurable as a linear combination of measurable functions.
$\square$

### Part B: Closure under Composition with Continuous Functions

**Proposition 3.2.** Let $(X, \mathcal{F})$ be a measurable space. Let $g: X \to \mathbb{R}$ be measurable (with respect to $\mathcal{B}(\mathbb{R})$), and let $f: \mathbb{R} \to \mathbb{R}$ be continuous. Then the composition $h = f \circ g: X \to \mathbb{R}$ is measurable.

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

*Proof of Proposition 3.2.*

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

**Corollary 3.3.** Let $(\mathcal{S}, \mathcal{F}_\mathcal{S})$ be a measurable state space. If $\phi: \mathcal{S} \to \mathbb{R}^d$ is measurable and $\text{NN}_\theta: \mathbb{R}^d \to \mathbb{R}$ is continuous almost everywhere, then $V_\theta = \text{NN}_\theta \circ \phi: \mathcal{S} \to \mathbb{R}$ is measurable.

**Why neural networks are measurable (addressing ReLU discontinuities):**

Modern deep RL uses neural networks with ReLU activations. A common misconception is that "ReLU is continuous except at a single point (0)." This statement applies to the **scalar function** $\text{ReLU}(x) = \max(0, x)$ on $\mathbb{R}$. However, ReLU layers apply this element-wise to vectors:
$$ \text{ReLU}(\mathbf{x}) = (\max(0, x_1), \ldots, \max(0, x_d)) $$

Each neuron in a ReLU network introduces discontinuities on a hyperplane $\{x \in \mathbb{R}^d : w^T x + b = 0\}$, which has Lebesgue measure zero in $\mathbb{R}^d$. A composition of ReLU layers thus has discontinuities on **countably many hyperplanes** (one per neuron across all layers), each of measure zero.

**Why measurability still holds:**
- **Fact from real analysis** [@folland:real_analysis:1999, Proposition 2.8]: A function $f: \mathbb{R}^d \to \mathbb{R}$ that is continuous except on a set of Lebesgue measure zero is Borel measurable.
- Each hyperplane of ReLU discontinuity $\{x : w^T x + b = 0\}$ has measure zero in $\mathbb{R}^d$ (it is a $(d-1)$-dimensional affine subspace).
- A feedforward ReLU network with $N$ neurons has discontinuities on at most $N$ hyperplanes (one per neuron).
- The countable union of measure-zero sets has measure zero.
- Therefore, ReLU networks are continuous almost everywhere, hence Borel measurable.
- By Proposition 3.2, their composition with measurable feature maps yields measurable value/policy functions.

**Technical note:** Even if we had discontinuities on a measure-positive set, compositions of measurable functions remain measurable (though continuity is not preserved). Measurability is preserved under far more general operations than continuity, which is why it is the correct framework for RL function approximators.

**Concrete example (DQN):** In deep Q-learning [@mnih:dqn:2015]:
- States $s \in \mathcal{S}$ (e.g., $84 \times 84$ grayscale images) define a measurable space with Borel σ-algebra.
- The pixel representation $s \mapsto \text{pixels}(s) \in [0,255]^{84 \times 84}$ is measurable (identity map on a Borel space).
- The Q-network $Q_\theta: [0,255]^{84 \times 84} \to \mathbb{R}^{|\mathcal{A}|}$ (convolutional layers + ReLU + linear layers) is Borel measurable.
- By Proposition 3.2, $s \mapsto Q_\theta(s, a)$ is measurable for each action $a$.
- This ensures the expected Q-value $\mathbb{E}_{s \sim \rho}[Q_\theta(s,a)]$ is well-defined (integration of a measurable function with respect to a probability measure).

**Extension to policy gradients:** Stochastic policies in actor-critic methods (e.g., PPO [@schulman:ppo:2017], SAC [@haarnoja:sac:2018]) use neural networks to output distribution parameters (e.g., mean and variance of a Gaussian). As long as the network $\pi_\theta: \mathcal{S} \to \mathbb{R}^{2|\mathcal{A}|}$ (outputting $\mu, \sigma$ per action) is measurable and the Gaussian density $(a, \mu, \sigma) \mapsto \mathcal{N}(a; \mu, \sigma^2)$ is continuous in $(\mu, \sigma)$ (which it is), the policy density $\pi_\theta(a|s)$ is jointly measurable in $(s, a)$. This ensures policy gradient objectives are well-defined expectations.

---

## Summary

We have developed three foundational tools:

1. **$\limsup$ and $\liminf$ of sets** (Exercise 1) characterize asymptotic behavior of events, essential for analyzing exploration, recurrence, and almost-sure convergence in stochastic approximation (Weeks 34-39).

2. **σ-Finite measures** (Exercise 2) enable application of Fubini-Tonelli (Week 3), Radon-Nikodym (Week 4), and product measure constructions (Week 3)—the theoretical bedrock for computing expectations in RL. We proved that σ-finiteness is stronger than semifiniteness and identified pathological counterexamples.

3. **Measurability under operations** (Exercise 3) guarantees that:
   - Arithmetic combinations of measurable functions (like Bellman updates) remain measurable
   - Neural network policies and value functions (even with ReLU discontinuities) are well-defined probabilistic objects
   - Expectations like $\mathbb{E}[V_\theta(S)]$ are mathematically meaningful

These techniques recur throughout measure-theoretic RL. Mastering them now provides the foundation for rigorous convergence analysis in later weeks.
