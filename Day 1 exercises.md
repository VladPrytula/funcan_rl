[[Day 1]]
# Characterizations of set $\limsup$ and $\liminf$

**Claim.** For sets $(E_n)_{n\ge1}$ in a universe $X$,
$$
\limsup_{n\to\infty} E_n=\bigcap_{k=1}^{\infty}\ \bigcup_{n\ge k} E_n
=\{x\in X:\ x\in E_n\ \text{for infinitely many } n\},
$$
$$
\liminf_{n\to\infty} E_n=\bigcup_{k=1}^{\infty}\ \bigcap_{n\ge k} E_n
=\{x\in X:\ x\in E_n\ \text{for all but finitely many } n\}.
$$

**Proof of the $\limsup$ characterization.**
- $(\subseteq)$ Take $x\in\bigcap_{k\ge1}\bigcup_{n\ge k}E_n$. For each $k$ choose $n_k\ge k$ with $x\in E_{n_k}$. Passing to a strictly increasing subsequence if needed gives infinitely many indices with $x\in E_{n_k}$. Hence $x$ is in $E_n$ infinitely often.
- $(\supseteq)$ If $x$ belongs to $E_n$ for infinitely many $n$, then for each $k$ there exists $n\ge k$ with $x\in E_n$, so $x\in\bigcup_{n\ge k}E_n$ for every $k$, i.e. $x\in\bigcap_{k\ge1}\bigcup_{n\ge k}E_n$.

**Proof of the $\liminf$ characterization.**
- $(\subseteq)$ Take $x\in\bigcup_{k\ge1}\bigcap_{n\ge k}E_n$. Then for some $k$, $x\in E_n$ for all $n\ge k$, therefore $x$ is in $E_n$ for all but finitely many $n$.
- $(\supseteq)$ If $x$ is in $E_n$ for all but finitely many $n$, then there is $N$ with $x\in E_n$ for all $n\ge N$, so $x\in\bigcap_{n\ge N}E_n\subseteq\bigcup_{k\ge1}\bigcap_{n\ge k}E_n$.

**Useful relation.**
$$
(\limsup E_n)^c=\liminf(E_n^{\,c}),\qquad
(\liminf E_n)^c=\limsup(E_n^{\,c}).
$$

**Indicator-function viewpoint (optional).** For each $x\in X$ let $I_n(x)=\mathbf{1}_{E_n}(x)$. Then
$$
\mathbf{1}_{\limsup E_n}(x)=\limsup_{n\to\infty} I_n(x),\qquad
\mathbf{1}_{\liminf E_n}(x)=\liminf_{n\to\infty} I_n(x),
$$
and $\limsup I_n(x)=1$ iff $x\in E_n$ infinitely often, while $\liminf I_n(x)=1$ iff $x\in E_n$ for all but finitely many $n$.

---
Not all measures are created equal. The behavior of integrals and the validity of powerful convergence theorems depend critically on certain regularity properties of the measure. Classifications such as σ-finiteness and semifiniteness are not mere technical pedantry; they are the gatekeepers for the application of essential analytical tools like the Fubini-Tonelli and Radon-Nikodym theorems. These theorems, in turn, are the bedrock upon which the theory of expectation operators and stochastic processes is built. Understanding these classifications is essential for delineating the universe of problems for which our learning algorithms are guaranteed to be well-behaved.

---

### **I. Core Theory** ( revised for convenience )

**Definition 1.3 (Measure).** Let $(X, \mathcal{F})$ be a measurable space. A function $\mu: \mathcal{F} \to [0, \infty]$ is a **measure** if it satisfies two conditions:
1.  $\mu(\emptyset) = 0$.
2.  (Countable Additivity) For any countable collection $\{A_n\}_{n=1}^{\infty}$ of pairwise disjoint sets in $\mathcal{F}$ (i.e., $A_i \cap A_j = \emptyset$ for $i \neq j$),
    $$ \mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n) $$

The triple $(X, \mathcal{F}, \mu)$ is called a **measure space**.

**Definition 1.4 (Probability Space).** A measure space $(X, \mathcal{F}, \mu)$ is a **probability space** if $\mu(X) = 1$. In this context, the measure $\mu$ is often denoted by $P$ and is called a probability measure.

We now introduce the key classifications of measure spaces.

**Definition 1.5 (σ-Finite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **σ-finite** if there exists a countable collection of sets $\{E_n\}_{n=1}^{\infty} \subseteq \mathcal{F}$ such that:
$$ X = \bigcup_{n=1}^{\infty} E_n \quad \text{and} \quad \mu(E_n) < \infty \text{ for all } n \in \mathbb{N} $$
In essence, a σ-finite space can be exhausted by a countable sequence of finite-measure "pieces."

**Example 1.2 (Lebesgue Measure is σ-finite).** The standard Lebesgue measure $\lambda$ on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ is not finite, as $\lambda(\mathbb{R})=\infty$. However, it is σ-finite, because we can write $\mathbb{R} = \bigcup_{n=1}^{\infty} [-n, n]$, and for each $n$, $\lambda([-n, n]) = 2n < \infty$.

**Definition 1.6 (Semifinite Measure).** A measure $\mu$ on $(X, \mathcal{F})$ is **semifinite** if for every set $A \in \mathcal{F}$ with $\mu(A) = \infty$, there exists a subset $B \in \mathcal{F}$ such that $B \subseteq A$ and $0 < \mu(B) < \infty$.
A semifinite measure, therefore, does not permit "purely infinite" measurable sets that contain no measurable subsets of finite, non-zero size.

---

### **II. Key Properties & Proofs**

These two properties are closely related, but one is strictly stronger than the other. This relationship is a fundamental piece of the theory.

**Proposition 1.3 (The Relationship between σ-Finite and Semifinite Measures).**
Every σ-finite measure is semifinite. However, the converse is not true; there exist semifinite measures that are not σ-finite.

*Proof.*

**(i) σ-finiteness implies semifiniteness.**
Let $\mu$ be a σ-finite measure on $(X, \mathcal{F})$. By definition, there exists a sequence of sets $\{E_n\}_{n=1}^{\infty}$ in $\mathcal{F}$ such that $X = \bigcup_{n=1}^{\infty} E_n$ and $\mu(E_n) < \infty$ for all $n$.

Now, let $A \in \mathcal{F}$ be any set with $\mu(A) = \infty$. We must find a measurable subset $B \subseteq A$ with $0 < \mu(B) < \infty$.
We can write $A$ as:
$$ A = A \cap X = A \cap \left(\bigcup_{n=1}^{\infty} E_n\right) = \bigcup_{n=1}^{\infty} (A \cap E_n) $$
By the countable subadditivity property of measures (which follows from countable additivity), we have:
$$ \mu(A) \le \sum_{n=1}^{\infty} \mu(A \cap E_n) $$
Since $\mu(A) = \infty$, the sum on the right-hand side must also be infinite. A sum of non-negative terms can only be infinite if at least one of the terms is positive. Therefore, there must exist at least one index $n_0 \in \mathbb{N}$ such that $\mu(A \cap E_{n_0}) > 0$.

Let us define our candidate set as $B = A \cap E_{n_0}$.
1.  $B \subseteq A$ by construction.
2.  Since $A \in \mathcal{F}$ and $E_{n_0} \in \mathcal{F}$, their intersection $B$ is also in $\mathcal{F}$.
3.  We have established that $\mu(B) = \mu(A \cap E_{n_0}) > 0$.
4.  By the monotonicity of measures (i.e., if $C \subseteq D$, then $\mu(C) \le \mu(D)$), we have $\mu(B) = \mu(A \cap E_{n_0}) \le \mu(E_{n_0})$. By the σ-finiteness assumption, $\mu(E_{n_0}) < \infty$.

We have thus constructed a set $B \subseteq A$ such that $B \in \mathcal{F}$ and $0 < \mu(B) < \infty$. This satisfies the definition of a semifinite measure.

**(ii) A counterexample to the converse.**
We must construct a measure space $(X, \mathcal{F}, \mu)$ where $\mu$ is semifinite but not σ-finite. The canonical example is the **counting measure on an uncountable set.**

Let $X$ be an uncountable set (for instance, $X = \mathbb{R}$). Let the σ-algebra be the power set, $\mathcal{F} = 2^X$. Define the counting measure $\mu_c$ as:
$$ \mu_c(A) = \begin{cases} |A| & \text{if } A \text{ is a finite set} \\ \infty & \text{if } A \text{ is an infinite set} \end{cases} $$
We now verify the two properties for this measure.

*   **$\mu_c$ is semifinite.** Let $A \in \mathcal{F}$ be a set with $\mu_c(A) = \infty$. By definition, this means $A$ is an infinite set. Since $A$ is not empty, we can choose an element $x \in A$. Consider the singleton set $B = \{x\}$.
    *   $B \subseteq A$ and $B \in \mathcal{F} = 2^X$.
    *   The measure of $B$ is $\mu_c(B) = |\{x\}| = 1$.
    *   Thus, we have found a subset $B$ of $A$ such that $0 < \mu_c(B) < \infty$.
    *   Therefore, the counting measure $\mu_c$ on $X$ is semifinite.

*   **$\mu_c$ is not σ-finite.** Assume, for the sake of contradiction, that $\mu_c$ is σ-finite. Then there must exist a countable collection of sets $\{E_n\}_{n=1}^{\infty}$ such that $X = \bigcup_{n=1}^{\infty} E_n$ and $\mu_c(E_n) < \infty$ for all $n$.
    *   The condition $\mu_c(E_n) < \infty$ means that each set $E_n$ must be a finite set.
    *   This implies that $X$ is a countable union of finite sets.
    *   A fundamental result of set theory states that a countable union of finite sets is, at most, a countable set.
    *   But we chose $X$ to be an uncountable set. This is a contradiction.
    *   Therefore, our initial assumption must be false, and $\mu_c$ is not σ-finite.

We have successfully constructed a measure that is semifinite but not σ-finite, completing the proof.
$\square$


***

### **Stretch goal: On the Measurability of Function Compositions**

This appendix provides a detailed, step-by-step proof of Proposition 1.4 concerning the composition of a measurable function with a continuous function. This result is of paramount importance, as it guarantees that many standard transformations preserve the essential property of measurability.

**Proposition 1.4 (Restated).** Let $(X, \mathcal{F})$ be a measurable space. Let $g: X \to \mathbb{R}$ be a measurable function (with respect to the Borel σ-algebra $\mathcal{B}(\mathbb{R})$ on its codomain), and let $f: \mathbb{R} \to \mathbb{R}$ be a continuous function. Then the composition $h = f \circ g: X \to \mathbb{R}$ is a measurable function.

Before proceeding with the proof, let us recall the essential definitions and a key lemma.

---

#### **Prerequisites**

1.  **Measurable Space:** A pair $(X, \mathcal{F})$, where $X$ is a set and $\mathcal{F}$ is a σ-algebra of subsets of $X$.

2.  **Borel σ-Algebra, $\mathcal{B}(\mathbb{R})$:** The smallest σ-algebra on $\mathbb{R}$ that contains all open subsets of $\mathbb{R}$. We say that the open sets *generate* the Borel σ-algebra.

3.  **Measurable Function:** A function $g: (X, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ is measurable if for every set $B$ in the codomain's σ-algebra, its preimage is in the domain's σ-algebra. Formally:
    $$ \forall B \in \mathcal{B}(\mathbb{R}), \quad g^{-1}(B) = \{x \in X \mid g(x) \in B\} \in \mathcal{F} $$

4.  **Continuous Function (Topological Definition):** A function $f: \mathbb{R} \to \mathbb{R}$ is continuous if and only if the preimage of every *open set* is an *open set*. Formally:
    $$ \forall U \subseteq \mathbb{R} \text{ such that } U \text{ is open}, \quad f^{-1}(U) = \{y \in \mathbb{R} \mid f(y) \in U\} \text{ is also an open set.} $$

5.  **Key Lemma for Verifying Measurability:** To prove that a function $h: (X, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ is measurable, it is *sufficient* to show that the preimage $h^{-1}(C)$ is in $\mathcal{F}$ for every set $C$ in a collection $\mathcal{C}$ that generates the codomain σ-algebra $\mathcal{B}(\mathbb{R})$. Since the collection of all open sets generates $\mathcal{B}(\mathbb{R})$, our task simplifies: we only need to prove that the preimage of any *open set* under $h$ is measurable.

---

#### **Detailed Proof**

Our goal is to demonstrate that the composite function $h = f \circ g$ is measurable. Following the Key Lemma above, we must show that for any arbitrary open set $U \subseteq \mathbb{R}$, the preimage $h^{-1}(U)$ is an element of the σ-algebra $\mathcal{F}$.

Let us proceed in a structured manner.

**Step 1: Express the preimage of the composition.**
Let $h(x) = (f \circ g)(x) = f(g(x))$. By the definition of a function composition, the preimage of a set $U$ under $h$ can be written as:
$$ h^{-1}(U) = (f \circ g)^{-1}(U) = g^{-1}(f^{-1}(U)) $$
This identity is the algebraic heart of the proof. It translates the problem into a two-stage process: first, find the preimage under $f$, and second, find the preimage of that resulting set under $g$.

**Step 2: Analyze the inner preimage, $f^{-1}(U)$.**
*   We begin by choosing an arbitrary open set $U \subseteq \mathbb{R}$.
*   The function $f: \mathbb{R} \to \mathbb{R}$ is given to be **continuous**.
*   By the topological definition of continuity (Prerequisite 4), the preimage of any open set under $f$ is itself an open set.
*   Therefore, the set $V = f^{-1}(U)$ is an open subset of $\mathbb{R}$.

**Step 3: Analyze the outer preimage, $g^{-1}(V)$.**
*   From Step 2, we have established that $V$ is an open set.
*   By the definition of the Borel σ-algebra $\mathcal{B}(\mathbb{R})$ (Prerequisite 2), every open set in $\mathbb{R}$ is an element of $\mathcal{B}(\mathbb{R})$. Thus, $V \in \mathcal{B}(\mathbb{R})$.
*   The function $g: X \to \mathbb{R}$ is given to be **measurable**.
*   By the definition of a measurable function (Prerequisite 3), the preimage of any set in $\mathcal{B}(\mathbb{R})$ under $g$ must be an element of $\mathcal{F}$.
*   Since $V \in \mathcal{B}(\mathbb{R})$, it follows directly that its preimage, $g^{-1}(V)$, must be an element of $\mathcal{F}$.

**Step 4: Synthesize and Conclude.**
By combining our steps, we have shown:
$$ h^{-1}(U) = g^{-1}(\underbrace{f^{-1}(U)}_{\text{This is an open set } V}) = g^{-1}(V) \in \mathcal{F} $$
We started with an arbitrary open set $U \subseteq \mathbb{R}$ and have rigorously proven that its preimage under $h = f \circ g$ is a member of the σ-algebra $\mathcal{F}$.

Since this holds for *every* open set in $\mathbb{R}$, and the collection of open sets generates the Borel σ-algebra $\mathcal{B}(\mathbb{R})$, we have satisfied the sufficient condition stated in our Key Lemma (Prerequisite 5).

We can therefore conclude that the function $h = f \circ g$ is $(\mathcal{F}, \mathcal{B}(\mathbb{R}))$-measurable.

$\square$

---

#### **Remark on Significance**

In reinforcement learning, for example, a state representation may be given by a measurable function $g: \mathcal{S} \to \mathbb{R}^d$ that extracts a vector of features. A policy or value function, often represented by a neural network, is then applied to this feature vector. The network itself is a grand composition of linear transformations (which are continuous) and activation functions (e.g., sigmoid, tanh, ReLU, which are also continuous). This proposition is the first and most crucial step in guaranteeing that the final output of the neural network—the policy or value—is a measurable function of the original state, a necessary condition for the entire theoretical framework to be sound.
