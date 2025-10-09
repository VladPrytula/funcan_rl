### Agenda:

##### 📘 Day 1 — Week 1: Measure Theory Foundations & RL Motivation
**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (30 min) — Reading**

**Topic:** _Sigma-algebras and measurable functions_

- Read from **Folland, "Real Analysis" §1.1–1.2** or equivalent in R. Durrett Ch.1.
- Focus on:
    - **Definitions**: σ-algebra, measurable function
    - **Examples**: Borel σ-algebra on ℝ
    - **Tools**: Monotone class argument (intuition only, no proof yet)
- _Key takeaway:_ Understand how measurable sets generalize intervals and why measurable functions are those compatible with "integration".

---

#### **⏱️ Segment 2 (30 min) — Proof/Exercise**

**Primary Task:** Work through **Exercise 3** (Composition of measurable and continuous functions) in the companion exercise file `Day 1 exercises REVISION_V2.md`. This establishes a key tool for neural network value functions in RL.

**Guidance:**
- Start with the generating class criterion (Lemma 3.1 in the exercise file)
- Use the fact that continuous functions pull back open sets to open sets
- Remember that open sets generate the Borel σ-algebra

**Stretch Goal:** Attempt **Exercise 1** (limsup/liminf characterizations). This formalizes "infinitely often" and "eventually always"—concepts essential for convergence theorems in stochastic approximation (Weeks 34-39).

---

#### **⏱️ Segment 3 (30 min) — Reflection / Reading Ahead**

**Reflection Questions:**
1. Why must policies and value functions be measurable? What breaks if we allow arbitrary functions?
2. How does the σ-algebra formalize "observability" in a physical system?
3. What role does completeness play in identifying value functions that differ only on null sets?

**Preview for Day 2:** Tomorrow we develop **Lebesgue integration**, which transforms measurable functions into expectations—the central operation in reinforcement learning.

---

#### **💡 Conceptual bridge to RL**

- Measure theory gives the formal underpinning of **probability spaces** used in MDPs.
- The σ-algebra defines _what's observable_ in a system — essential when defining policies as measurable functions over states.
- Integration with respect to measures (Day 2) will formalize **expectation**, enabling rigorous treatment of value functions and Bellman equations.

---

📅 Tomorrow (Day 2): we'll move to **measures, probability spaces, and integrals**, connecting Lebesgue integration with expectation operators in RL.

### **Chapter 1: Foundations in Measure and Probability Theory**

#### **1.1 The Structure of Observability: σ-Algebras and Measurable Functions**

**Motivation:** The ultimate ambition of this text is to develop a rigorous mathematical framework for optimal sequential decision-making under uncertainty, a problem epitomized by the modern field of Reinforcement Learning (RL). At its core, this is a problem of optimal control. Whether we are navigating a robot through a dynamic environment or managing a financial portfolio, we must contend with a stream of information from a "state space," which is often a continuum (e.g., $\mathbb{R}^n$).

Before we can speak of probabilities, expectations, or stochastic dynamics, we must first answer a more fundamental question (we will see shortly via a concrete counterexample why this question is not optional): **What constitutes a "reasonable" subset of our state space?** If the state of our system is a vector in $\mathbb{R}^n$, can we assign a probability to *any* arbitrary, pathological subset of this space?

The answer, a cornerstone of 20th-century mathematics, is no. We must restrict our attention to a well-behaved collection of subsets, those for which concepts like volume, or more generally "measure," are well-defined. This collection is known as a $\sigma$-algebra.

**Why this restriction is not optional:** Consider a control problem where the state $s \in [0,1]$ and we have actions $\mathcal{A} = \{\text{Accelerate}, \text{Brake}\}$. Using the axiom of choice, one can construct a **Vitali set** $V \subset [0,1]$—a subset that is provably non-measurable with respect to Lebesgue measure. Now consider the policy:
$$ \pi^*(s) = \begin{cases} \text{Accelerate} & \text{if } s \in V \\ \text{Brake} & \text{if } s \notin V \end{cases} $$

This is a perfectly well-defined function set-theoretically. But suppose the initial state $s_0$ is drawn uniformly from $[0,1]$. We ask: **What is the probability that the controller chooses to accelerate?** The answer should be $\lambda(V)$, where $\lambda$ is Lebesgue measure. But $\lambda(V)$ is **undefined**—the question has no answer. Our model has shattered before we have taken a single step.

More deeply, for a device to implement $\pi^*$, it must determine whether $s \in V$. A physical sensor can only perform finite measurements—checking if $s$ lies in intervals, or countable combinations thereof. It can at best determine membership in **Borel sets**. The question "is $s \in V$?" requires access to information about the real line that is physically unobtainable.

---
**The central insight:** The σ-algebra $\mathcal{F}_{\mathcal{S}}$ represents the set of all questions about the state that a physical observer can answer. A policy $\pi$ is measurable if and only if the decision it makes can be determined by asking a countable sequence of physically answerable questions. A non-measurable policy is not merely complex—it is a fiction, requiring information that cannot exist.

---

The $\sigma$-algebra, therefore, is the mathematical formalization of **observability**. It defines the universe of events to which we can assign a probability. Consequently, any function that represents a quantity of interest—be it a policy $\pi: \mathcal{S} \to \mathcal{A}$ mapping states to actions, or a value function $V: \mathcal{S} \to \mathbb{R}$—must be compatible with this structure of observability. Such functions are termed **measurable**. They are the only functions we can meaningfully integrate to compute expectations, which is the central operation in evaluating and improving policies. This section establishes this fundamental grammar.

**Learning Objectives:**
*   Define $\sigma$-algebras and measures, and articulate their role in constructing a formal probability space.
*   Understand the properties of measurable functions and prove their closure under arithmetic operations and composition with continuous functions.
*   Recognize why measurability is an indispensable prerequisite for a coherent theory of stochastic control and reinforcement learning.
---

### **I. Core Theory Part A: σ-Algebras**

We begin by defining the collection of sets that will serve as our domain for assigning probabilities or sizes.

**Definition 1.1 (σ-Algebra).** Let $X$ be a non-empty set. A collection of subsets $\mathcal{F} \subseteq 2^X$ is a **σ-algebra** on $X$ if it satisfies the following three properties:
1.  (Contains the whole set) $X \in \mathcal{F}$.
2.  (Closure under complementation) If $A \in \mathcal{F}$, then its complement $A^c = X \setminus A$ is also in $\mathcal{F}$.
3.  (Closure under countable unions) If $\{A_n\}_{n=1}^{\infty}$ is a countable collection of sets in $\mathcal{F}$, then their union $\bigcup_{n=1}^{\infty} A_n$ is also in $\mathcal{F}$.

The pair $(X, \mathcal{F})$ is called a **measurable space**. The elements of $\mathcal{F}$ are called **measurable sets**.

**Immediate Consequences.** Two crucial properties follow directly from these axioms:

(i) **The empty set is measurable.** From Axiom 1, $X \in \mathcal{F}$. By Axiom 2, its complement $X^c = \emptyset$ must also be in $\mathcal{F}$.

(ii) **Closure under countable intersections.** This property is deduced from the axioms via **De Morgan's laws**. For a collection of sets $\{A_n\}_{n=1}^{\infty}$, these laws state: $\left(\bigcup A_n\right)^c = \bigcap A_n^c$. To prove closure, let $\{A_n\}_{n=1}^{\infty}$ be a sequence of sets in $\mathcal{F}$. By Axiom 2, each complement $A_n^c$ is in $\mathcal{F}$. By Axiom 3, their countable union $\bigcup A_n^c$ is in $\mathcal{F}$. By Axiom 2 again, the complement of this union, $\left(\bigcup A_n^c\right)^c$, is in $\mathcal{F}$. Applying De Morgan's law, this final set is precisely the countable intersection $\bigcap A_n$.

**Example 1.1 (The Borel σ-Algebra).** For our purposes, the most important measurable space is $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. The **Borel σ-algebra**, $\mathcal{B}(\mathbb{R})$, is defined as the *smallest* σ-algebra on $\mathbb{R}$ that contains all open sets. It contains all sets of practical interest: open, closed, intervals, and countable combinations thereof.

---

### **II. Core Theory Part B: Measures**

With a structure of events $\mathcal{F}$ in place, we can now assign a notion of size to them.

**Definition 1.2 (Measure).** Let $(X, \mathcal{F})$ be a measurable space. A function $\mu: \mathcal{F} \to [0, \infty]$ is a **measure** if it satisfies two conditions:
1.  $\mu(\emptyset) = 0$.
2.  (Countable Additivity) For any countable collection $\{A_n\}_{n=1}^{\infty}$ of pairwise disjoint sets in $\mathcal{F}$,
    $$
    \mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n).
    $$

The triple $(X, \mathcal{F}, \mu)$ is called a **measure space**.

**Definition 1.3 (Probability Space).** A measure space $(X, \mathcal{F}, \mu)$ is a **probability space** if $\mu(X) = 1$. The measure $\mu$ is then denoted by $P$ and called a probability measure.

**Example 1.2 (Lebesgue Measure).** The canonical measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ is the Lebesgue measure $\lambda$, which generalizes the notion of length. For any interval $(a,b)$, $\lambda((a,b)) = b-a$. Its rigorous construction is a cornerstone of analysis, but we shall take its existence as given.

---

### **III. Classification and Refinement of Measure Spaces**

The applicability of powerful theorems often depends on certain regularity conditions of the measure space. We discuss the most important of these here.

#### **A. σ-Finiteness and Semifiniteness**

These properties relate to whether an infinite space can be understood in terms of finite pieces.

**Definition 1.4 (σ-Finite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **σ-finite** if there exists a countable collection of sets $\{E_n\}_{n=1}^{\infty} \subseteq \mathcal{F}$ such that $X = \bigcup_{n=1}^{\infty} E_n$ and $\mu(E_n) < \infty$ for all $n \in \mathbb{N}$.

The Lebesgue measure is σ-finite, as $\mathbb{R} = \bigcup_{n \in \mathbb{Z}} [n, n+1]$.

**Definition 1.5 (Semifinite Measure).** A measure $\mu$ is **semifinite** if for every set $A \in \mathcal{F}$ with $\mu(A) = \infty$, there exists a subset $B \in \mathcal{F}$ such that $B \subseteq A$ and $0 < \mu(B) < \infty$.

**Proposition 1.1.** Every σ-finite measure is semifinite. The converse is not true.

*Proof.*
(i) **σ-finiteness implies semifiniteness.**
Let $\mu$ be σ-finite, so $X = \bigcup E_n$ with $\mu(E_n) < \infty$. Let $A \in \mathcal{F}$ with $\mu(A) = \infty$. We have $A = \bigcup (A \cap E_n)$. By subadditivity, $\infty = \mu(A) \le \sum \mu(A \cap E_n)$. This implies that for at least one index $n_0$, we must have $\mu(A \cap E_{n_0}) > 0$. Let $B = A \cap E_{n_0}$. Then $B \subseteq A$ and $B \in \mathcal{F}$. Furthermore, $0 < \mu(B) \le \mu(E_{n_0}) < \infty$. This satisfies the definition of semifiniteness.

(ii) **A counterexample to the converse.**
Let $X = \mathbb{R}$ (an uncountable set) and $\mathcal{F} = 2^{\mathbb{R}}$. Define the counting measure $\mu_c(A) = |A|$ if $A$ is finite, and $\mu_c(A)=\infty$ otherwise.
*   **$\mu_c$ is semifinite:** If $\mu_c(A) = \infty$, then $A$ is infinite. Pick any element $x \in A$. The set $B=\{x\}$ is a subset of $A$ with $0 < \mu_c(B) = 1 < \infty$.
*   **$\mu_c$ is not σ-finite:** Assume it were. Then $\mathbb{R} = \bigcup E_n$ where $\mu_c(E_n) < \infty$. This means each $E_n$ must be a finite set. But this would imply $\mathbb{R}$ is a countable union of finite sets, which would make $\mathbb{R}$ countable. This is a contradiction.
$\square$

#### **B. Completeness**

This property refines the σ-algebra to include all subsets of negligible sets.

**Motivation:** Consider the space $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. One can construct the **Cantor set** $C$, which is a Borel set with $\lambda(C) = 0$. However, $C$ contains subsets, say $Z \subset C$, which are provably *not* in the Borel σ-algebra $\mathcal{B}(\mathbb{R})$. This presents a logical deficiency: we have a set $Z$ contained within a set of measure zero, yet we cannot even assign $Z$ a measure. A complete measure space rectifies this.

**Definition 1.6 (Null Set and Completeness).** Let $(X, \mathcal{F}, \mu)$ be a measure space.
1.  A set $N \in \mathcal{F}$ is a **null set** if $\mu(N) = 0$.
2.  The measure space is **complete** if for every null set $N \in \mathcal{F}$, every subset $Z \subseteq N$ is also in $\mathcal{F}$.

The Borel measure space $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ is famously *not* complete. However, any measure space can be extended to its completion.

**Proposition 1.2 (The Incompleteness of the Borel-Lebesgue Space).** The measure space $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, consisting of the Borel σ-algebra and the Lebesgue measure, is not complete.

*Proof.* To prove this, we must construct a specific counterexample. We must exhibit a set $N \in \mathcal{B}(\mathbb{R})$ with $\lambda(N)=0$, and a subset $Z \subseteq N$ such that $Z \notin \mathcal{B}(\mathbb{R})$.

1.  **Constructing the Null Set.** Let $C$ be the standard Cantor middle-thirds set in $[0,1]$. It is constructed by starting with $C_0 = [0,1]$ and iteratively removing the open middle third of each interval remaining at step $k$ to obtain $C_{k+1}$. Each $C_k$ is a finite union of closed intervals, and is therefore a closed set. The Cantor set is the intersection of all these closed sets: $C = \bigcap_{k=0}^{\infty} C_k$. As a countable intersection of closed sets, $C$ is itself a closed set. Since all closed sets belong to the Borel σ-algebra, we have $C \in \mathcal{B}(\mathbb{R})$. The Lebesgue measure of $C$ is given by $\lambda(C) = \lim_{k \to \infty} (2/3)^k = 0$. We have thus found our null set, $N=C$.

2.  **Demonstrating the Existence of a Non-Borel Subset.** The crux of the argument rests upon a cardinality comparison.
    *   It is a foundational result of descriptive set theory that the cardinality of the Borel σ-algebra is equal to the cardinality of the continuum, i.e., $|\mathcal{B}(\mathbb{R})| = |\mathbb{R}| = \mathfrak{c}$.
    *   It is also a standard result that the Cantor set $C$, despite having measure zero, is uncountable and has the cardinality of the continuum, $|C| = \mathfrak{c}$. This can be seen by constructing a bijection between points in $C$ (represented by their ternary expansions using only digits 0 and 2) and points in $[0,1]$ (represented by their binary expansions).
    *   Consider the power set of $C$, denoted $2^C$, which is the collection of *all* subsets of $C$. By **Cantor's theorem** (the power set of any set has strictly greater cardinality than the set itself), we have $|2^C| = 2^{|C|} = 2^{\mathfrak{c}} > \mathfrak{c}$.

3.  **Conclusion.** The collection of all subsets of the Cantor set has cardinality $2^{\mathfrak{c}}$. The collection of all Borel sets has cardinality $\mathfrak{c}$. Since there are strictly more subsets of $C$ than there are Borel sets in total, it is a logical necessity that there must exist subsets of $C$ that are not Borel sets. Let $Z$ be one such subset.
    We have successfully identified a set $C \in \mathcal{B}(\mathbb{R})$ with $\lambda(C)=0$, and a subset $Z \subseteq C$ for which $Z \notin \mathcal{B}(\mathbb{R})$. This violates the definition of a complete measure space.
$\square$

This flaw is not fatal. The fact that our foundational measure space is incomplete simply means it is not yet the correct analytical object for our purposes. As we shall now prove, any measure space can be uniquely extended to its completion, thereby absorbing these pathological subsets of null sets into the framework in a consistent manner.

**Theorem 1.1 (The Completion of a Measure Space).** For any measure space $(X, \mathcal{F}, \mu)$, there exists a complete measure space $(X, \overline{\mathcal{F}}, \overline{\mu})$ such that $\mathcal{F} \subseteq \overline{\mathcal{F}}$ and $\overline{\mu}$ agrees with $\mu$ on $\mathcal{F}$. The σ-algebra $\overline{\mathcal{F}}$ consists of all sets of the form $A \cup Z$, where $A \in \mathcal{F}$ and $Z$ is a subset of some null set in $\mathcal{F}$.

*Proof (Constructive).* The proof proceeds in four steps: we show (i) that $\overline{\mu}$ is well-defined, (ii) that $\overline{\mathcal{F}}$ is a σ-algebra, (iii) that $\overline{\mu}$ is a measure, and finally (iv) that the resulting space is complete.

(i) **$\overline{\mu}$ is well-defined.** We must show that the value of $\overline{\mu}$ for a set $E \in \overline{\mathcal{F}}$ does not depend on its representation. Suppose $E = A_1 \cup Z_1 = A_2 \cup Z_2$, where $A_i \in \mathcal{F}$ and $Z_i \subseteq N_i$ for some $N_i \in \mathcal{N}$. Observe that $A_1 \subseteq E = A_2 \cup Z_2 \subseteq A_2 \cup N_2$. Thus $A_1 \setminus A_2 \subseteq N_2$. Since $A_1, A_2 \in \mathcal{F}$, the set $A_1 \setminus A_2$ is measurable. By the monotonicity of measures, $\mu(A_1 \setminus A_2) \le \mu(N_2) = 0$. Symmetrically, $A_2 \setminus A_1 \subseteq N_1$, so $\mu(A_2 \setminus A_1) = 0$. Since $\mu(A_1) = \mu(A_1 \cap A_2) + \mu(A_1 \setminus A_2)$ and $\mu(A_2) = \mu(A_1 \cap A_2) + \mu(A_2 \setminus A_1)$, we have $\mu(A_1) = \mu(A_1 \cap A_2) + 0$ and $\mu(A_2) = \mu(A_1 \cap A_2) + 0$. Therefore, $\mu(A_1) = \mu(A_2)$, and our definition of $\overline{\mu}$ is unambiguous.

(ii) **$\overline{\mathcal{F}}$ is a σ-algebra.**
1.  $X \in \overline{\mathcal{F}}$ since $X = X \cup \emptyset$, $X \in \mathcal{F}$, and $\emptyset$ is a subset of the null set $\emptyset \in \mathcal{N}$.
2.  (Closure under complementation) Let $E = A \cup Z \in \overline{\mathcal{F}}$, with $A \in \mathcal{F}$ and $Z \subseteq N \in \mathcal{N}$. Its complement is $E^c = (A \cup Z)^c = A^c \cap Z^c$. This form is not immediately useful. The key insight is to write $E^c$ as $(A \cup N)^c \cup (N \setminus Z)$. The set $A' = (A \cup N)^c$ is in $\mathcal{F}$ because $A, N \in \mathcal{F}$. The set $Z' = N \setminus Z$ is a subset of the null set $N$. Thus $E^c = A' \cup Z'$ is of the required form to be in $\overline{\mathcal{F}}$.
3.  (Closure under countable unions) Let $\{E_n\}_{n=1}^{\infty}$ be a sequence in $\overline{\mathcal{F}}$. For each $n$, $E_n = A_n \cup Z_n$ where $A_n \in \mathcal{F}$ and $Z_n \subseteq N_n$ for some $N_n \in \mathcal{N}$. Their union is $\bigcup_{n=1}^\infty E_n = (\bigcup_{n=1}^\infty A_n) \cup (\bigcup_{n=1}^\infty Z_n)$. Let $A = \bigcup A_n$ and $Z = \bigcup Z_n$. Since $\mathcal{F}$ is a σ-algebra, $A \in \mathcal{F}$. Let $N = \bigcup N_n$. As a countable union of null sets, $N$ is itself a null set in $\mathcal{F}$ (since $\mu(N) \le \sum \mu(N_n) = 0$). Since $Z \subseteq N$, the set $\bigcup E_n = A \cup Z$ is of the required form and is therefore in $\overline{\mathcal{F}}$.

(iii) **$\overline{\mu}$ is a measure.** Let $\{E_n\}$ be a disjoint sequence in $\overline{\mathcal{F}}$, with $E_n = A_n \cup Z_n$. From the disjointness of $\{E_n\}$, the sets $\{A_n\}$ must also be disjoint. Then $\overline{\mu}(\bigcup E_n) = \overline{\mu}((\bigcup A_n) \cup (\bigcup Z_n)) = \mu(\bigcup A_n) = \sum \mu(A_n) = \sum \overline{\mu}(A_n \cup Z_n) = \sum \overline{\mu}(E_n)$.
$\square$

**Definition 1.7 (The Lebesgue σ-Algebra).** The **Lebesgue σ-algebra** on $\mathbb{R}$, denoted $\mathcal{L}(\mathbb{R})$, is the completion of the Borel σ-algebra $\mathcal{B}(\mathbb{R})$ with respect to the Lebesgue measure $\lambda$. For the remainder of this text, unless specified otherwise, analysis on $\mathbb{R}^n$ will implicitly use this complete space.

---

### **1.2 Mappings that Preserve Structure: Measurable Functions**

**Motivation:** Having defined the structure of our state space $(\mathcal{S}, \mathcal{F}_{\mathcal{S}})$, we must now consider the functions that act upon it. In reinforcement learning, the key objects—policies $\pi: \mathcal{S} \to \mathcal{A}$, value functions $V: \mathcal{S} \to \mathbb{R}$, and reward functions $R: \mathcal{S} \to \mathbb{R}$—are all functions defined on the state space. For these objects to be compatible with our probabilistic framework, they must respect the underlying structure of observable events. They must be **measurable functions**. A function is measurable if it does not require information that is "finer" than what the σ-algebra provides.

---

### **I. Core Theory: Measurable Functions**

**Definition 1.8 (Measurable Function).** Let $(X, \mathcal{F})$ and $(Y, \mathcal{G})$ be two measurable spaces. A function $f: X \to Y$ is said to be **$(\mathcal{F}, \mathcal{G})$-measurable** if the preimage of every measurable set in $Y$ is a measurable set in $X$:
$$
\forall B \in \mathcal{G}, \quad f^{-1}(B) = \{x \in X \mid f(x) \in B\} \in \mathcal{F}.
$$
For a real-valued function $f: X \to \mathbb{R}$, we assume the codomain is $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.

---

### **II. Key Properties & Proofs**

The class of measurable functions is remarkably stable under common operations. The following results are developed in detail in the companion exercise file `Day 1 exercises REVISION_V2.md`, with guided proofs.

**Proposition 1.3 (Closure under Arithmetic Operations).** Let $f, g: (X, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ be measurable. Then the sum $f+g$ and product $f \cdot g$ are measurable.

*Sketch of Proof.* For the sum, express $\{x \mid f(x) + g(x) < a\}$ as a countable union over rationals: $\bigcup_{q \in \mathbb{Q}} (\{f < q\} \cap \{g < a-q\})$. For the product, note that $f^2$ is measurable (using preimages of intervals), then apply the identity $f \cdot g = \frac{1}{2}((f+g)^2 - f^2 - g^2)$. The full proof is given in Exercise 3 of the companion file.

**Proposition 1.4 (Closure under Composition).** Let $g: (X, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ be measurable and $f: (\mathbb{R}, \mathcal{B}(\mathbb{R})) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ be continuous. Then the composition $f \circ g$ is measurable.

*Sketch of Proof.* For any open set $U \subseteq \mathbb{R}$, we have $(f \circ g)^{-1}(U) = g^{-1}(f^{-1}(U))$. By continuity of $f$, the set $f^{-1}(U)$ is open, hence Borel. By measurability of $g$, the preimage $g^{-1}(f^{-1}(U))$ is in $\mathcal{F}$. Since open sets generate $\mathcal{B}(\mathbb{R})$, this suffices. The complete proof is given in Exercise 3 of the companion file.

The property of completeness has a vital consequence for measurable functions.

**Proposition 1.5 (Measurability of "Almost Everywhere" Equal Functions).** Let $(X, \mathcal{F}, \mu)$ be a **complete** measure space. If $f:X \to \mathbb{R}$ is measurable and $g:X \to \mathbb{R}$ satisfies $f(x)=g(x)$ for all $x$ outside a null set, then $g$ is also measurable.

*Proof.* Let $N \in \mathcal{F}$ be a null set such that $E = \{x \mid f(x) \neq g(x)\} \subseteq N$. As the space is complete, $E \in \mathcal{F}$ and $\mu(E)=0$. For any $a \in \mathbb{R}$:
$$ \{x \mid g(x) < a\} = (\{x \in E^c \mid g(x) < a\}) \cup (\{x \in E \mid g(x) < a\}) $$
The first term is $\{x \in E^c \mid f(x) < a\} = E^c \cap f^{-1}((-\infty,a))$, which is an intersection of measurable sets and hence measurable. The second term is a subset of the null set $E$. By completeness, it is also measurable. The union of two measurable sets is measurable. Thus, $g$ is measurable.
$\square$

---

### **III. Computational Illustration: The Intricacy of Measurable Sets**

Measurability extends far beyond simple sets. The **Cantor function**, $f_c: [0, 1] \to [0, 1]$, provides a stunning example. It is continuous (and thus measurable) but reveals that preimages can have a complex, fractal structure.

```python
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray

def cantor_function(x: float, n: int = 10) -> float:
    """
    Approximate the Cantor function (Devil's Staircase) via recursive construction.

    The Cantor function is continuous, non-decreasing, yet its derivative is zero
    almost everywhere—all growth occurs on the Cantor set, a measure-zero set.

    Args:
        x: Input value in [0, 1]
        n: Number of recursion levels (higher = better approximation)

    Returns:
        The Cantor function value f_C(x) ∈ [0, 1]
    """
    if n == 0 or x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    if 0 < x < 1/3:
        return 0.5 * cantor_function(3 * x, n - 1)
    elif 1/3 <= x <= 2/3:
        return 0.5
    else:
        return 0.5 + 0.5 * cantor_function(3 * x - 2, n - 1)

x_domain: NDArray[np.float64] = np.linspace(0, 1, 2000)
y_values: NDArray[np.float64] = np.vectorize(cantor_function)(x_domain)

plt.figure(figsize=(10, 5))
plt.plot(x_domain, y_values, color='darkred', linewidth=1.5)
plt.title("The Cantor Function (Devil's Staircase)", fontsize=14)
plt.xlabel(r'Domain $x \in [0, 1]$', fontsize=12)
plt.ylabel(r'$f_C(x)$', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

# RL Interpretation: This illustrates that measurable value functions V(s) can have
# intricate structure—discontinuities on fractal sets, flat regions of measure zero—
# yet remain valid for computing expectations E[V(S)]. The Cantor function's growth
# occurs on a set of measure zero, analogous to how value functions in robotics may
# change discontinuously on contact manifolds (codimension-1 sets of measure zero in
# configuration space), yet integration with respect to the state distribution remains
# well-defined under our Lebesgue measure framework.
```

**Interpretation:** This continuous function is non-decreasing yet its derivative is zero "almost everywhere"—all of its growth occurs on the **Cantor set**, a Borel set of Lebesgue measure zero. This illustrates that a measurable function can map a simple codomain interval to a domain set of profound topological complexity. Our theory is robust enough to handle such mappings, which is essential for describing the potentially intricate value functions that arise in complex control landscapes.

---

### **IV. Synthesis: Toward Markov Decision Processes**

We conclude Day 1 by previewing how today's abstractions enable rigorous reinforcement learning.

A **Markov Decision Process** models sequential decision-making under uncertainty. Informally, it consists of:

*   **States** $(\mathcal{S}, \mathcal{F}_{\mathcal{S}})$: a measurable space representing possible configurations of the system. Today's focus has been establishing this structure. For continuous state spaces, we typically use $\mathcal{S} \subseteq \mathbb{R}^n$ with the Lebesgue σ-algebra $\mathcal{L}(\mathbb{R}^n)$.

*   **Actions** $(\mathcal{A}, \mathcal{F}_{\mathcal{A}})$: another measurable space representing available controls.

*   **Transition dynamics**: Given current state $s$ and action $a$, the next state is drawn from a probability distribution. Formally, for each pair $(s,a) \in \mathcal{S} \times \mathcal{A}$, we have a probability measure $P(\cdot \mid s, a)$ on $(\mathcal{S}, \mathcal{F}_{\mathcal{S}})$. This object—a family of probability measures indexed by state-action pairs—is called a **transition kernel**, which we formalize rigorously in Week 7 for discrete chains and Week 11 for general state spaces.

*   **Rewards**: The function $R: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ is a *measurable function* assigning immediate payoff to state-action pairs. Measurability ensures that expected rewards $\mathbb{E}_{s' \sim P(\cdot|s,a)}[R(s,a)]$ are well-defined.

*   **Deterministic policies** $\pi: \mathcal{S} \to \mathcal{A}$: measurable maps from states to actions. This is the mathematical embodiment of a physically realizable control law: the choice of action depends only on observable information about the state.

*   **Stochastic policies**: In modern RL (policy gradients, entropy-regularized methods), we use stochastic policies $\pi(a|s)$ that specify a probability distribution over actions for each state.

    Formally, this requires $\pi$ to be a transition kernel from $\mathcal{S}$ to $\mathcal{A}$, ensuring that for each Borel set $B \subseteq \mathcal{A}$, the map $s \mapsto \pi(B|s)$ is measurable. We defer this generalization to Week 25, where stochastic policies are formalized for the policy gradient theorem.

**Why measurability is non-negotiable:**

The value function of a policy $\pi$ is defined as:
$$
V^\pi(s) = \mathbb{E}_\pi\left[\sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \,\bigg|\, s_0 = s\right]. \tag{1.1}
$$

This is an **expectation**—an integral over the space of trajectories with respect to the probability measure induced by $\pi$ and $P$. Integration requires:
1.  The integrand (cumulative discounted reward) must be a measurable function of the trajectory.
2.  This, in turn, requires $R$ to be measurable and the trajectory space to have a well-defined σ-algebra.
3.  The trajectory space σ-algebra is constructed as a **product σ-algebra** $\mathcal{F}_{\mathcal{S}} \otimes \mathcal{F}_{\mathcal{A}} \otimes \mathcal{F}_{\mathcal{S}} \otimes \cdots$, which we develop in Week 3.

Without measurability, the expression "$\mathbb{E}[V^\pi(S)]$" has no mathematical meaning. It is not an approximation or a technicality—it is undefined.

**What we have achieved today:**

The σ-algebra $\mathcal{F}_{\mathcal{S}}$ defines the universe of observable events. Measurable functions are those compatible with this observability structure. Completeness ensures that functions differing only on null sets (states visited with probability zero) are identified—a crucial equivalence for "almost everywhere" results in stochastic approximation (Weeks 34-39).

**What we postpone:**

*   Formal definition of transition kernels and their measurability properties (Week 7 for finite chains, Week 11 for general state spaces)
*   Construction of product σ-algebras for trajectory spaces (Week 3)
*   Proof that the Bellman operator $T^\pi V(s) = R(s, \pi(s)) + \gamma \int_{\mathcal{S}} V(s') P(ds'|s, \pi(s))$ is well-defined and contractive on appropriate function spaces (Week 25)

Today's foundation—σ-algebras, measures, measurable functions, completeness—makes all of this machinery rigorously well-defined. Tomorrow, we develop **Lebesgue integration**, which transforms measurable functions into expectations and unlocks the door to dynamic programming.

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day 1 exercises REVISION_V2]]**
*(Day 1 exercises REVISION_V2.md)*
