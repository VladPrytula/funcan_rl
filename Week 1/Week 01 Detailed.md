# Week 1 Detailed: Measure Theory Foundations

**Duration**: 5 days (Monday-Friday), 90 minutes per day  
**Phase**: I - Measure-Theoretic Foundations  
**Primary References**: Folland §1.1-2.4, Durrett Ch 1

---

## Week 1 Overview

**Learning Objectives**:
1. Master σ-algebras as formalization of observability in stochastic systems
2. Understand measures and their regularity properties (σ-finite, complete)
3. Prove measurability closure under arithmetic and composition
4. Construct the Lebesgue integral from first principles
5. Prove and apply the three fundamental convergence theorems (MCT, Fatou, DCT)
6. Connect measure theory to RL: policies as measurable functions, expectations as integrals

**Bridge to RL**: Measure theory provides the rigorous foundation for probability spaces in MDPs. The σ-algebra defines what's observable; measurable functions are physically realizable policies; convergence theorems enable iterative algorithms like value iteration and TD learning.

---

## Day 1 (Monday) — σ-Algebras, Measures, and Measurability

**Status**: ✅ COMPLETED

### Summary of Work Completed

**Topics Covered**:
- σ-algebras: definition, properties, and the Borel σ-algebra on $\mathbb{R}$
- Measures: definition, probability spaces
- Classification of measures: σ-finite vs semifinite (complete proof with counterexample)
- Completeness of measure spaces (Cantor set construction, cardinality argument)
- Measurable functions: definition and closure properties
- Set limits: $\limsup$ and $\liminf$ with indicator function viewpoint

**Proofs Completed**:
1. ✅ Relationship between σ-finite and semifinite measures
   - σ-finite ⇒ semifinite (constructive proof)
   - Counterexample: counting measure on uncountable set is semifinite but not σ-finite
2. ✅ Incompleteness of Borel-Lebesgue space via Cantor set cardinality
3. ✅ Completion of measure spaces (full constructive proof)
4. ✅ Measurability of composition $f \circ g$ when $g$ measurable and $f$ continuous
   - Included Lemma A.1 (criterion for measurability via generating sets)
   - Full four-step proof with preimage decomposition

**Depth Achieved**: Publication-quality mathematical exposition with complete proofs. Significantly exceeded typical Day 1 scope—covered Day 1 + portions of Day 2 material.

**Files produced**:
- `Day_1.md`: Full lecture notes with motivation, definitions, theorems
- `Day_1_exercises.md`: Detailed proofs of all anchor exercises

**RL Connections Established**:
- σ-algebra as formalization of observability in control systems
- Measurable policies as physically realizable control laws
- Vitali set example: non-measurable policies require infinite information
- Composition theorem: neural network policies are measurable (compositions of continuous functions)

---

## Day 2 (Tuesday) — The Lebesgue Integral and Monotone Convergence

**Total time**: ~90 minutes

### 📖 Segment 1 (40 min) — Reading

**Topic**: Construction of the Lebesgue integral

**Primary Reference**: Folland §2.1-2.2

**Reading Goals**:
- Construction pathway: simple functions → non-negative measurable → general measurable
- For simple function $\varphi = \sum_i a_i \mathbf{1}_{A_i}$, define $\int \varphi \, d\mu = \sum_i a_i \mu(A_i)$
- For $f \geq 0$ measurable: $\int f \, d\mu = \sup\{\int \varphi \, d\mu : 0 \leq \varphi \leq f, \varphi \text{ simple}\}$
- For general $f$: $\int f \, d\mu = \int f^+ \, d\mu - \int f^- \, d\mu$ when both finite
- Monotone Convergence Theorem (MCT) statement: If $0 \leq f_1 \leq f_2 \leq \ldots$ and $f_n \to f$ a.e., then $\int f_n \to \int f$

**Key Conceptual Question**: Why does the order of operations matter? In Riemann integration, we approximate the domain (partition into intervals). In Lebesgue integration, we partition the range. This reversal is what enables handling discontinuous functions and proves convergence theorems.

**Reading Strategy**:
- First 15 min: Construction for simple functions (definition, linearity, monotonicity)
- Next 15 min: Extension to non-negative functions via supremum
- Final 10 min: General functions via $f = f^+ - f^-$; MCT statement and intuition

---

### ✏️ Segment 2 (40 min) — Proof

**Exercise**: Prove the Monotone Convergence Theorem

**Setup**: Let $(X, \mathcal{F}, \mu)$ be a measure space. Suppose $\{f_n\}_{n=1}^\infty$ is a sequence of measurable functions with:
1. $0 \leq f_1(x) \leq f_2(x) \leq \ldots$ for all $x \in X$
2. $f_n(x) \to f(x)$ for all $x \in X$

Then $f$ is measurable and $\lim_{n\to\infty} \int f_n \, d\mu = \int f \, d\mu$.

**Proof Structure**:

**Step 1 (Measurability of $f$)** (~5 min):  
Since $f = \sup_n f_n$ and each $f_n$ is measurable, verify that:
$$\{x : f(x) > a\} = \bigcup_n \{x : f_n(x) > a\} \in \mathcal{F}$$
for any $a \in \mathbb{R}$. Thus $f$ is measurable.

**Step 2 (Show $\lim \int f_n \leq \int f$)** (~5 min):  
By monotonicity of the integral, $\int f_n \leq \int f_{n+1} \leq \int f$ for all $n$. Thus the sequence $\{\int f_n\}$ is increasing and bounded above by $\int f$. Therefore:
$$\lim_{n\to\infty} \int f_n \text{ exists and } \lim_{n\to\infty} \int f_n \leq \int f$$

**Step 3 (The hard direction: $\int f \leq \lim \int f_n$)** (~25 min):  
This requires showing that for any simple function $0 \leq \varphi \leq f$, we have:
$$\int \varphi \, d\mu \leq \lim_{n\to\infty} \int f_n \, d\mu$$

Choose $\alpha \in (0,1)$ and define:
$$E_n = \{x : f_n(x) \geq \alpha\varphi(x)\}$$

Then $E_1 \subseteq E_2 \subseteq \ldots$ and $\bigcup_n E_n = X$ (since $f_n \to f \geq \varphi$ pointwise).

For each $n$:
$$\int f_n \, d\mu \geq \int_{E_n} f_n \, d\mu \geq \alpha \int_{E_n} \varphi \, d\mu$$

Taking limits and using continuity of measure ($\mu(E_n) \uparrow \mu(X)$):
$$\lim_{n\to\infty} \int f_n \, d\mu \geq \alpha \int \varphi \, d\mu$$

Since this holds for all $\alpha < 1$, let $\alpha \to 1$:
$$\lim_{n\to\infty} \int f_n \, d\mu \geq \int \varphi \, d\mu$$

Taking supremum over all simple $\varphi \leq f$:
$$\lim_{n\to\infty} \int f_n \, d\mu \geq \int f \, d\mu$$

Combining with Step 2: $\lim \int f_n = \int f$. ∎

**Step 4 (Reflect on technique)** (~5 min):  
Write brief notes on:
1. Where precisely did we use the monotonicity assumption $f_n \leq f_{n+1}$?
2. What breaks if we only assume $f_n \to f$ without monotonicity?
3. Why is the $\alpha$-trick necessary? (Handles case where $\varphi = f$ on a set of infinite measure)

---

### 📝 Segment 3 (10 min) — Reflection Note

**Format**: Brief written note addressing:

**Mathematical Insight**:  
The MCT proof hinges on two facts: (1) monotone sequences of real numbers converge if bounded, and (2) measure is continuous along increasing sequences of sets. The $\alpha$-trick handles the case where $\varphi$ might equal $f$ on a set of infinite measure—we can't directly use $E_n = \{x : f_n(x) \geq \varphi(x)\}$ because the last set might have infinite measure and the inequality might be tight.

**RL Connection**:  
MCT justifies computing expectations via limits: $\mathbb{E}[V_n] \to \mathbb{E}[V]$ when value functions converge monotonically. In policy evaluation, if we iterate $V_{n+1} = T^\pi V_n$ starting from $V_0 = 0$, the sequence is increasing (assuming rewards are non-negative), and MCT guarantees:
$$\int V_n \, dP \to \int V^\pi \, dP$$
This underpins the correctness of value iteration and policy evaluation algorithms.

**Open Question**:  
Can MCT be extended to handle "almost monotone" sequences, where the monotonicity fails on a null set? (Answer: Yes, since integration ignores null sets, but worth thinking through carefully.)

---

## Day 3 (Wednesday) — Fatou's Lemma and Dominated Convergence Theorem

**Total time**: ~90 minutes

### 📖 Segment 1 (40 min) — Reading

**Topic**: The triumvirate of convergence theorems

**Primary Reference**: Folland §2.3

**Reading Goals**:
- **Fatou's Lemma**: For $f_n \geq 0$ measurable, $\int (\liminf f_n) \leq \liminf \int f_n$
- **Dominated Convergence Theorem**: If $|f_n| \leq g$ with $\int g < \infty$ and $f_n \to f$ a.e., then $\int f_n \to \int f$
- Understand the hierarchy: MCT (monotone + non-negative) → Fatou (non-negative only) → DCT (domination condition)
- Each theorem relaxes hypotheses but requires additional structure

**Conceptual Framework**:  
These three theorems form a ladder:
- **MCT**: Strongest hypothesis (monotonicity), strongest conclusion (equality)
- **Fatou**: Weaker hypothesis (only non-negativity), weaker conclusion (inequality)
- **DCT**: Different hypothesis (domination replaces monotonicity), strong conclusion (equality)

**Key Examples to Study**:
- Example where Fatou's inequality is strict: $f_n = \mathbf{1}_{[n, n+1]}$ on $\mathbb{R}$ with Lebesgue measure
  - $\liminf f_n = 0$ everywhere, so $\int (\liminf f_n) = 0$
  - But $\int f_n = 1$ for all $n$, so $\liminf \int f_n = 1$
  - Strict inequality: $0 < 1$
- Example showing necessity of domination in DCT: $f_n = n \mathbf{1}_{[0,1/n]}$ on $[0,1]$
  - $f_n \to 0$ pointwise, but $\int f_n = 1$ for all $n$
  - No integrable dominating function exists

**Reading Strategy**:
- First 15 min: Fatou's Lemma statement, proof strategy, examples
- Next 15 min: DCT statement, role of dominating function, examples
- Final 10 min: Compare all three theorems—create a table of hypotheses vs conclusions

---

### ✏️ Segment 2 (40 min) — Proof

**Exercise 1**: Prove Fatou's Lemma (~20 min)

**Statement**: Let $f_n \geq 0$ be measurable functions. Then:
$$\int \left(\liminf_{n\to\infty} f_n\right) d\mu \leq \liminf_{n\to\infty} \int f_n \, d\mu$$

**Proof**:  
Let $g_n = \inf_{k\geq n} f_k$. Then:
1. Each $g_n$ is measurable (as infimum of measurable functions)
2. $0 \leq g_1 \leq g_2 \leq \ldots$ (increasing sequence)
3. $g_n \to \liminf_{n\to\infty} f_n$ pointwise

By MCT:
$$\int \left(\liminf_{n\to\infty} f_n\right) d\mu = \int \left(\lim_{n\to\infty} g_n\right) d\mu = \lim_{n\to\infty} \int g_n \, d\mu = \liminf_{n\to\infty} \int g_n \, d\mu$$

Since $g_n \leq f_n$ for all $n$ (by definition of infimum), we have:
$$\int g_n \, d\mu \leq \int f_n \, d\mu$$

Therefore:
$$\liminf_{n\to\infty} \int g_n \, d\mu \leq \liminf_{n\to\infty} \int f_n \, d\mu$$

Combining:
$$\int \left(\liminf_{n\to\infty} f_n\right) d\mu \leq \liminf_{n\to\infty} \int f_n \, d\mu$$
∎

**Exercise 2**: Prove DCT using Fatou (~20 min)

**Statement**: Let $f_n$ be measurable with $|f_n| \leq g$ where $\int g \, d\mu < \infty$. If $f_n \to f$ a.e., then:
$$\lim_{n\to\infty} \int f_n \, d\mu = \int f \, d\mu$$

**Proof Sketch**:  
Given $|f_n| \leq g$ and $f_n \to f$, we have $|f| \leq g$ a.e.

Apply Fatou to the non-negative sequence $h_n = g + f_n \geq 0$:
$$\int (g + f) \, d\mu = \int \left(\liminf_{n\to\infty} (g + f_n)\right) d\mu \leq \liminf_{n\to\infty} \int (g + f_n) \, d\mu$$

Since $\int g < \infty$, we can subtract it:
$$\int f \, d\mu \leq \liminf_{n\to\infty} \int f_n \, d\mu$$

Similarly, apply Fatou to $h_n' = g - f_n \geq 0$:
$$\int (g - f) \, d\mu \leq \liminf_{n\to\infty} \int (g - f_n) \, d\mu$$

This gives:
$$\int f \, d\mu \geq \limsup_{n\to\infty} \int f_n \, d\mu$$

Thus:
$$\limsup_{n\to\infty} \int f_n \, d\mu \leq \int f \, d\mu \leq \liminf_{n\to\infty} \int f_n \, d\mu$$

Which forces:
$$\lim_{n\to\infty} \int f_n \, d\mu = \int f \, d\mu$$
∎

---

### 📝 Segment 3 (10 min) — Reflection Note

**Mathematical Insight**:  
Fatou's Lemma is the bridge between MCT and DCT. Its power lies in requiring minimal hypotheses (just non-negativity) while providing an inequality that's often sufficient. The DCT proof demonstrates a beautiful technique: apply Fatou twice to sequences that are non-negative by construction ($g + f_n$ and $g - f_n$). The dominating function $g$ serves two roles: (1) ensures integrability of limits, (2) enables "shifting" to make sequences non-negative.

**RL Connection**:  
DCT is essential for gradient-based RL. When we compute $\nabla_\theta \mathbb{E}_\pi[R]$ by swapping $\nabla$ and $\mathbb{E}$, we're implicitly invoking DCT. The dominating function ensures the gradient is integrable. Without DCT, policy gradient theorems would lack rigorous justification. Specifically, if policy $\pi_\theta$ is Lipschitz in $\theta$ and rewards are bounded, then $\nabla_\theta \log \pi_\theta(a|s)$ is dominated by a constant, enabling:
$$\nabla_\theta \mathbb{E}_{\pi_\theta}[R] = \mathbb{E}_{\pi_\theta}[\nabla_\theta \log \pi_\theta(a|s) \cdot R]$$

**Open Question**: What is the minimal regularity on $\pi_\theta$ required for DCT to apply in policy gradients? Does Lipschitz continuity suffice, or do we need stronger conditions?

---

## Day 4 (Thursday) — Extended Proof: The π-λ Theorem

**Total time**: ~90 minutes (30 min reading + 60 min extended proof)

### 📖 Segment 1 (30 min) — Reading

**Topic**: Generating σ-algebras efficiently

**Primary Reference**: Folland §1.3, or Billingsley "Probability and Measure" Appendix

**Reading Goals**:
- **π-system**: Collection $\mathcal{P}$ closed under finite intersections (if $A, B \in \mathcal{P}$, then $A \cap B \in \mathcal{P}$)
- **λ-system** (Dynkin system): Collection $\mathcal{L}$ satisfying:
  1. $X \in \mathcal{L}$
  2. If $A \in \mathcal{L}$, then $A^c \in \mathcal{L}$
  3. If $\{A_n\}$ are pairwise disjoint in $\mathcal{L}$, then $\bigcup_n A_n \in \mathcal{L}$
- **π-λ Theorem**: If $\mathcal{P}$ is a π-system and $\mathcal{L}$ is a λ-system with $\mathcal{P} \subseteq \mathcal{L}$, then $\sigma(\mathcal{P}) \subseteq \mathcal{L}$

**Why This Matters**:  
The Borel σ-algebra $\mathcal{B}(\mathbb{R})$ is enormous (uncountably infinite). To prove two measures are equal on $\mathcal{B}(\mathbb{R})$, we don't want to check equality on every Borel set. The π-λ theorem says: just check equality on a π-system that generates the σ-algebra (e.g., intervals), and you're done.

**Application to RL**:  
When defining transition kernels $P(\cdot|s,a)$, we only need to specify them on a generating π-system (e.g., rectangles in $\mathbb{R}^n$), and they extend uniquely to the entire Borel σ-algebra.

**Reading Strategy**:
- First 10 min: Definitions of π-system and λ-system with examples
- Next 10 min: Statement of π-λ theorem and intuition
- Final 10 min: Example applications (uniqueness of measures)

---

### ✏️ Segment 2 (60 min) — Extended Proof

**Theorem (π-λ)**: Let $\mathcal{P}$ be a π-system and $\mathcal{L}$ be a λ-system on $X$. If $\mathcal{P} \subseteq \mathcal{L}$, then $\sigma(\mathcal{P}) \subseteq \mathcal{L}$.

**Proof Strategy**: We'll show that $\sigma(\mathcal{P})$ is the smallest λ-system containing $\mathcal{P}$. Since $\mathcal{L}$ is a λ-system containing $\mathcal{P}$, this will imply $\sigma(\mathcal{P}) \subseteq \mathcal{L}$.

**Preliminary Lemmas** (~15 min):

**Lemma 1**: Every σ-algebra is a λ-system.

*Proof*: Let $\mathcal{A}$ be a σ-algebra.
1. $X \in \mathcal{A}$ by definition of σ-algebra.
2. If $A \in \mathcal{A}$, then $A^c \in \mathcal{A}$ by closure under complements.
3. If $\{A_n\}$ are disjoint in $\mathcal{A}$, then $\bigcup_n A_n \in \mathcal{A}$ by countable unions.

Thus $\mathcal{A}$ is a λ-system. ∎

**Lemma 2**: If $\mathcal{L}$ is a λ-system that is also closed under finite intersections (i.e., is a π-system), then $\mathcal{L}$ is a σ-algebra.

*Proof*: We need to show $\mathcal{L}$ is closed under countable unions (not necessarily disjoint).

Let $\{A_n\} \subseteq \mathcal{L}$. Define:
$$B_1 = A_1, \quad B_2 = A_2 \setminus A_1, \quad B_3 = A_3 \setminus (A_1 \cup A_2), \ldots$$

Each $B_n$ can be written as intersections and complements of sets in $\mathcal{L}$:
$$B_n = A_n \cap \left(\bigcap_{k=1}^{n-1} A_k^c\right)$$

Since $\mathcal{L}$ is a π-system (closed under $\cap$) and a λ-system (closed under complements and finite intersections with complements), each $B_n \in \mathcal{L}$.

The $B_n$ are pairwise disjoint and $\bigcup_n B_n = \bigcup_n A_n$. Since $\mathcal{L}$ is a λ-system:
$$\bigcup_n B_n \in \mathcal{L} \implies \bigcup_n A_n \in \mathcal{L}$$

Therefore $\mathcal{L}$ is a σ-algebra. ∎

**Main Proof** (~40 min):

**Step 1**: Let $\mathcal{L}_0$ be the smallest λ-system containing $\mathcal{P}$. Since $\mathcal{L}$ is a λ-system containing $\mathcal{P}$, we have $\mathcal{L}_0 \subseteq \mathcal{L}$.

**Step 2**: We'll prove $\mathcal{L}_0$ is closed under finite intersections, making it a σ-algebra by Lemma 2.

**Step 3** (Good sets principle): For $A \in \mathcal{L}_0$, define:
$$\mathcal{L}_A = \{B \in \mathcal{L}_0 : A \cap B \in \mathcal{L}_0\}$$

**Claim**: $\mathcal{L}_A$ is a λ-system.

*Proof of claim*:
- $X \in \mathcal{L}_A$ since $A \cap X = A \in \mathcal{L}_0$ ✓
- If $B \in \mathcal{L}_A$, then $A \cap B \in \mathcal{L}_0$. We have:
  $$A \cap B^c = A \setminus (A \cap B) = A \setminus C$$
  where $C = A \cap B \in \mathcal{L}_0$. Since $\mathcal{L}_0$ is a λ-system, $A \setminus C \in \mathcal{L}_0$. Thus $B^c \in \mathcal{L}_A$ ✓
- If $\{B_n\}$ are pairwise disjoint in $\mathcal{L}_A$, then $\{A \cap B_n\}$ are pairwise disjoint in $\mathcal{L}_0$. Thus:
  $$\bigcup_n (A \cap B_n) = A \cap \left(\bigcup_n B_n\right) \in \mathcal{L}_0$$
  So $\bigcup_n B_n \in \mathcal{L}_A$ ✓

Therefore $\mathcal{L}_A$ is a λ-system. ∎

**Step 4**: For any $P \in \mathcal{P}$, consider $\mathcal{L}_P$. Since $\mathcal{P}$ is a π-system, for any $Q \in \mathcal{P}$, we have:
$$P \cap Q \in \mathcal{P} \subseteq \mathcal{L}_0$$

Thus $Q \in \mathcal{L}_P$ for all $Q \in \mathcal{P}$. Therefore $\mathcal{P} \subseteq \mathcal{L}_P$.

Since $\mathcal{L}_P$ is a λ-system and $\mathcal{L}_0$ is the smallest λ-system containing $\mathcal{P}$:
$$\mathcal{L}_0 \subseteq \mathcal{L}_P$$

This means: for all $A \in \mathcal{L}_0$ and all $P \in \mathcal{P}$, we have $P \cap A \in \mathcal{L}_0$.

**Step 5**: Now fix arbitrary $A \in \mathcal{L}_0$. From Step 4, we know $\mathcal{P} \subseteq \mathcal{L}_A$. Since $\mathcal{L}_A$ is a λ-system:
$$\mathcal{L}_0 \subseteq \mathcal{L}_A$$

This means: for all $A, B \in \mathcal{L}_0$, we have $A \cap B \in \mathcal{L}_0$.

**Step 6**: Therefore $\mathcal{L}_0$ is a π-system. By Lemma 2, $\mathcal{L}_0$ is a σ-algebra.

Since $\mathcal{L}_0$ is:
- The smallest λ-system containing $\mathcal{P}$
- A σ-algebra

It must equal $\sigma(\mathcal{P})$.

Since $\mathcal{L}_0 \subseteq \mathcal{L}$, we conclude:
$$\sigma(\mathcal{P}) \subseteq \mathcal{L}$$
∎

**Reflection** (~5 min):  
This proof is a masterclass in bootstrapping. We start with minimal structure (π-system, λ-system) and carefully construct increasingly rich collections until we've built a σ-algebra. The key trick is defining $\mathcal{L}_A$ and proving it's a λ-system—this is the "good sets principle" in action. By showing that "sets that intersect nicely with $A$" form a λ-system, we bootstrap closure under intersections from a π-system to the full σ-algebra.

---

## Day 5 (Friday) — Integration, Review, and Computation

**Total time**: ~90 minutes (20 min reading + 30 min review + 40 min coding)

### 📖 Segment 1 (20 min) — Reading

**Topic**: Quick preview of $L^p$ spaces

**Primary Reference**: Folland §6.1 (skim)

**Reading Goals**: 
- Understand $\|f\|_p = \left(\int |f|^p \, d\mu\right)^{1/p}$ defines a "norm" on equivalence classes $[f]$ where $f \sim g$ if $f = g$ a.e.
- The triangle inequality (Minkowski) and Hölder inequality will come next week
- $L^p(\mu) = \{f : \|f\|_p < \infty\} / {\sim}$ is a normed space
- Preview: $L^\infty$ is where value functions live; $L^2$ is where TD projections happen

**Reading Strategy**:
- 10 min: Definition of $L^p$ spaces and $\|\cdot\|_p$ norm
- 10 min: Examples: $L^1$ (integrable), $L^2$ (square-integrable), $L^\infty$ (essentially bounded)

---

### ✏️ Segment 2 (30 min) — Proof Review

**Exercise**: Write a one-page proof summary document

Create a structured summary of this week's major results:

**1. Monotone Convergence Theorem**
- **Hypothesis**: $0 \leq f_1 \leq f_2 \leq \ldots \to f$ a.e.
- **Conclusion**: $\int f_n \to \int f$
- **Key technique**: $\alpha$-trick with simple functions to handle sets of infinite measure
- **Why it works**: Monotonicity + measure continuity on increasing sets

**2. Fatou's Lemma**
- **Hypothesis**: $f_n \geq 0$ (no monotonicity!)
- **Conclusion**: $\int(\liminf f_n) \leq \liminf \int f_n$ (inequality, not equality)
- **Key technique**: Apply MCT to $g_n = \inf_{k\geq n} f_k$
- **Why weaker**: Relaxed hypothesis gives weaker conclusion

**3. Dominated Convergence Theorem**
- **Hypothesis**: $|f_n| \leq g \in L^1$, $f_n \to f$ a.e. (domination replaces monotonicity)
- **Conclusion**: $\int f_n \to \int f$ (equality restored!)
- **Key technique**: Apply Fatou to $g \pm f_n \geq 0$
- **Critical role of $g$**: Ensures integrability + enables shifting to non-negative

**4. π-λ Theorem**
- **Purpose**: Uniqueness of measures on generated σ-algebras
- **Key technique**: Good sets principle via $\mathcal{L}_A$ construction
- **Bootstrapping**: π-system + λ-system → σ-algebra via closure under intersections
- **Why powerful**: Check measure equality on small generating set (e.g., intervals), get equality on entire Borel σ-algebra

**Connections**: All three convergence theorems build on each other:
$$\text{MCT (monotone)} \implies \text{Fatou (non-negative)} \implies \text{DCT (dominated)}$$

---

### 💻 Segment 3 (40 min) — Coding Synthesis

**Task**: Numerical verification of convergence theorems

```python
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Part 1: Monotone Convergence Theorem
# ============================================================

def verify_MCT():
    """
    Verify MCT with f_n(x) = x(1 - x^{1/n}) on [0,1]
    f_n increases to f(x) = x
    """
    x = np.linspace(0, 1, 1000)
    dx = x[1] - x[0]
    
    integrals = []
    for n in range(1, 51):
        f_n = x * (1 - x**(1/n))
        integral_n = np.sum(f_n) * dx  # Riemann approximation
        integrals.append(integral_n)
    
    true_integral = 1/2  # ∫x dx from 0 to 1
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(integrals, 'b.-', label='$\\int f_n$')
    plt.axhline(true_integral, color='r', linestyle='--', label='$\\int f$')
    plt.xlabel('n')
    plt.ylabel('Integral value')
    plt.title('MCT: $\\int f_n \\to \\int f$')
    plt.legend()
    plt.grid(True)
    
    # Plot some f_n
    plt.subplot(1, 2, 2)
    for n in [1, 3, 10, 50]:
        f_n = x * (1 - x**(1/n))
        plt.plot(x, f_n, label=f'$f_{{{n}}}$')
    plt.plot(x, x, 'k--', linewidth=2, label='$f(x)=x$')
    plt.xlabel('x')
    plt.ylabel('$f_n(x)$')
    plt.title('Monotone convergence of functions')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/Week1_MCT_verification.png', dpi=150)
    print(f"MCT: Final integral = {integrals[-1]:.6f}, True = {true_integral:.6f}")

# ============================================================
# Part 2: Fatou's Lemma (strict inequality example)
# ============================================================

def verify_Fatou():
    """
    Example where Fatou's inequality is strict:
    f_n = 1_{[n, n+1]} on R with Lebesgue measure
    lim inf f_n = 0, but ∫f_n = 1 for all n
    """
    print(f"\nFatou's Lemma:")
    print(f"Example: f_n = 1_{{[n, n+1]}} on R")
    print(f"∫(lim inf f_n) = ∫0 = 0")
    print(f"lim inf ∫f_n = 1 (since ∫f_n = 1 for all n)")
    print(f"Inequality: 0 < 1 ✓")
    print(f"Strict inequality demonstrates Fatou can be non-equality")
    print(f"Intuition: Mass 'escapes to infinity'")

# ============================================================
# Part 3: DCT necessity of domination
# ============================================================

def verify_DCT_necessity():
    """
    Show DCT fails without domination:
    f_n(x) = n * 1_{[0, 1/n]}
    f_n → 0 pointwise, but ∫f_n = 1 ↛ 0
    """
    x = np.linspace(0, 1, 10000)
    dx = x[1] - x[0]
    
    integrals = []
    n_values = [10, 20, 50, 100, 200, 500]
    for n in n_values:
        f_n = np.where(x <= 1/n, n, 0)
        integral_n = np.sum(f_n) * dx
        integrals.append(integral_n)
    
    plt.figure(figsize=(10, 5))
    plt.plot(n_values, integrals, 'ro-', markersize=8)
    plt.axhline(0, color='b', linestyle='--', label='$\\int f = 0$')
    plt.axhline(1, color='g', linestyle='--', alpha=0.5, label='$\\int f_n = 1$')
    plt.xlabel('n')
    plt.ylabel('$\\int f_n$')
    plt.title('DCT fails without domination: $\\int f_n = 1$ but $f_n \\to 0$')
    plt.legend()
    plt.grid(True)
    plt.savefig('/mnt/user-data/outputs/Week1_DCT_counterexample.png', dpi=150)
    print(f"\nDCT Counterexample:")
    print(f"f_n = n·1_{{[0,1/n]}}, f_n → 0 pointwise")
    print(f"All integrals ≈ 1: {integrals}")
    print(f"No integrable dominating function exists!")
    print(f"Conclusion: Domination hypothesis is necessary")

# ============================================================
# Part 4: RL Connection - Value Iteration Convergence
# ============================================================

def value_iteration_convergence():
    """
    Simple gridworld: 5×5 grid, goal at (4,4), rewards r(goal)=1, else 0
    V_{n+1}(s) = max_a [r(s,a) + γ Σ P(s'|s,a)V_n(s')]
    This is monotone increasing from V_0 = 0, so MCT applies
    """
    gamma = 0.9
    grid_size = 5
    goal = (4, 4)
    
    V = np.zeros((grid_size, grid_size))
    V_history = [V.copy()]
    
    for iteration in range(50):
        V_new = np.zeros_like(V)
        for i in range(grid_size):
            for j in range(grid_size):
                if (i, j) == goal:
                    V_new[i, j] = 1.0  # Terminal state
                else:
                    # Actions: up, down, left, right
                    values = []
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < grid_size and 0 <= nj < grid_size:
                            values.append(gamma * V[ni, nj])
                        else:
                            values.append(gamma * V[i, j])  # Stay in place
                    V_new[i, j] = max(values)
        V = V_new
        V_history.append(V.copy())
    
    # Plot convergence
    plt.figure(figsize=(10, 5))
    goal_values = [V[2, 2] for V in V_history]  # Track a non-goal state
    plt.plot(goal_values, 'b.-')
    plt.xlabel('Iteration n')
    plt.ylabel('$V_n(s)$ at state (2,2)')
    plt.title('Value Iteration: Monotone convergence to $V^*$ via MCT')
    plt.grid(True)
    plt.savefig('/mnt/user-data/outputs/Week1_value_iteration_MCT.png', dpi=150)
    
    print(f"\nRL Connection: Value Iteration")
    print(f"Starting from V_0 = 0, sequence V_n is monotone increasing")
    print(f"MCT guarantees: ∫V_n dP → ∫V^* dP")
    print(f"V_50(2,2) = {V_history[-1][2, 2]:.4f}")
    print(f"Convergence is exponential with rate γ = {gamma}")

# ============================================================
# Run all verifications
# ============================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Week 1 Synthesis: Convergence Theorems in Action")
    print("=" * 70)
    
    verify_MCT()
    verify_Fatou()
    verify_DCT_necessity()
    value_iteration_convergence()
    
    print("\n" + "=" * 70)
    print("All verifications complete. Check generated plots in outputs folder.")
    print("=" * 70)
    
    plt.show()
```

**Post-Coding Reflection**:
- **MCT** guarantees value iteration converges (monotone increasing from $V_0 = 0$)
- **DCT** enables policy gradient: $\nabla \mathbb{E}[R] = \mathbb{E}[\nabla R]$ when gradients are dominated
- **Fatou** provides robustness: even without monotonicity, we get an inequality that's often sufficient for analysis

---

## Week 1 Completion Checklist

✅ **Mathematical Foundations**:
- [ ] σ-algebras: definition, properties, Borel σ-algebra
- [ ] Measures: definition, σ-finite, complete
- [ ] Measurable functions: closure under arithmetic and composition
- [ ] Lebesgue integral: construction via simple functions
- [ ] MCT: full proof with $\alpha$-trick
- [ ] Fatou's Lemma: proof via MCT on $g_n = \inf_{k \geq n} f_k$
- [ ] DCT: proof via Fatou applied to $g \pm f_n$
- [ ] π-λ theorem: full proof with good sets principle

✅ **RL Connections Established**:
- [ ] σ-algebras formalize observability in MDPs
- [ ] Measurable policies are physically realizable
- [ ] MCT justifies value iteration convergence
- [ ] DCT enables policy gradient theorems
- [ ] Completeness ensures $L^p$ spaces well-behaved

✅ **Code Implementations**:
- [ ] MCT numerical verification
- [ ] Fatou strict inequality example
- [ ] DCT counterexample (necessity of domination)
- [ ] Value iteration with MCT convergence

✅ **Learning Log Entry**:
- [ ] Mathematical insight: Key proof technique learned
- [ ] RL connection: How this week's math appears in algorithms
- [ ] Open questions: What to explore deeper later

---

## Bridge to Week 2

**What You've Mastered**:
1. σ-algebras as formalization of observability
2. Measures and their regularity properties (σ-finite, complete)
3. Measurable functions and closure properties
4. The Lebesgue integral construction
5. The three fundamental convergence theorems (MCT, Fatou, DCT)
6. The π-λ theorem for proving uniqueness of measures

**Next Week Preview**: Product measures and Fubini's theorem (critical for understanding transition kernels $P(s'|s,a)$ as measures), followed by Radon-Nikodym theorem (foundation for importance sampling and likelihood ratios in off-policy RL).

**Postponed Generalizations**:
- General Carathéodory extension (from arbitrary algebras) → covered rectangles-to-Lebesgue only
- Full Birkhoff ergodic theorem → will encounter in Week 11 for Markov chains

---

**End of Week 1 Detailed Plan**

*Total time: 5 days × 90 minutes = 7.5 hours*  
*Depth: Rigorous proofs with RL connections throughout*  
*Outcome: Solid measure-theoretic foundation for probability and MDPs*
