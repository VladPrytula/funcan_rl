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

