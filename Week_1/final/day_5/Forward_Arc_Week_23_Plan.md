# Week 23 Architectural Plan: MDP Formalism and Bellman Equations

**Phase**: V (Markov Decision Processes and Dynamic Programming)
**Primary References**: Puterman Ch 3-4, Bertsekas Vol I Ch 1-2
**Prerequisites**: Week 1 (Measure theory), Week 10 (Markov kernels), Week 16 (Banach fixed-point), Week 22 (HJB equations)

---

## Overview: The Synthesis

For 22 weeks, we have been building mathematical infrastructure:
- **Week 1**: σ-algebras, measurable functions, Dominated Convergence, Carathéodory extension
- **Weeks 2-4**: $L^p$ spaces, Radon-Nikodym, conditional expectation
- **Weeks 5-10**: Markov chains (finite, countable, general state spaces)
- **Weeks 11-16**: Functional analysis (Banach spaces, contraction mappings)
- **Weeks 17-22**: Sobolev spaces, PDEs, Hamilton-Jacobi-Bellman equations

This week, **everything converges**. We construct the **Markov Decision Process** formalism where:
- States live in a measurable space $(\mathcal{S}, \mathcal{F})$ (Week 1)
- Transition kernels are Markov kernels $P(\cdot \mid s,a): \mathcal{F} \to [0,1]$ (Week 10)
- Value functions live in Banach space $\mathcal{B}(\mathcal{S})$ or $C_b(\mathcal{S})$ (Week 11)
- The Bellman operator $T$ is a contraction mapping (Week 16)
- Optimal policies exist via the Measurable Selection Theorem (proved this week)

**Central Thesis**: The MDP is not a collection of ad-hoc assumptions. It is the **unique rigorous framework** where all our measure-theoretic and functional-analytic machinery applies to sequential decision-making.

---

## Narrative Arc: From Week 1 to Week 23

### **What We Built (Week 1)**

Recall the **central thesis of Week 1**, Day 5:

> "Measure theory is not a prerequisite to RL—it **is** the mathematical language of RL. Without σ-algebras, we cannot define transition kernels. Without measurable functions, we cannot define policies. Without DCT, we cannot prove convergence of value iteration."

We made four **promissory notes**:

1. **Measurable functions as policies** (Day 1, Definition 1.8): "A policy $\pi: \mathcal{S} \to \mathcal{A}$ must be measurable to ensure the decision 'which action to take' depends only on observable information."

2. **Carathéodory for transition kernels** (Day 4, Theorem 1.10): "The transition kernel $P(\cdot \mid s,a)$ in continuous-state MDPs is constructed via Carathéodory: start with probabilities on simple sets, extend to all Borel sets via outer measure."

3. **DCT for Bellman consistency** (Day 3, Theorem 1.8): "Nearly every convergence proof in RL—value iteration, policy iteration, TD learning, Q-learning—relies on DCT to justify $\lim_{n \to \infty} \mathbb{E}_\mu[V_n] = \mathbb{E}_\mu[\lim_{n \to \infty} V_n]$."

4. **Measurable Selection for optimal policies** (Day 5, Open Question 3): "Is $\pi^*(s) = \arg\max_a Q(s,a)$ a measurable function? We will prove this in **Week 23** using the Measurable Selection Theorem."

**This week redeems all four promissory notes.**

---

### **What We Added (Weeks 2-22)**

Before formalizing MDPs, we needed:

- **Week 2**: Product measures $\mu \times \nu$ on $\mathcal{S} \times \mathcal{A}$ to define joint state-action distributions
- **Week 4**: Conditional expectation $\mathbb{E}[R \mid s,a]$ to formalize expected rewards
- **Week 10**: Transition kernels $P(\cdot \mid s,a)$ on general state spaces, Feller property for continuity
- **Week 16**: Contraction Mapping Theorem: If $T: X \to X$ satisfies $d(Tx, Ty) \leq \gamma d(x,y)$ with $\gamma < 1$, then $T$ has a unique fixed point
- **Week 22**: Hamilton-Jacobi-Bellman equation $V_t + H(x, \nabla V) = 0$ in continuous time (connection to infinite-horizon Bellman equation)

**The MDP formalizes the discrete-time, stochastic analog of HJB optimal control.**

---

## The MDP Structure: A Measured Septuple

### **Definition 23.1 (Markov Decision Process)**

A **Markov Decision Process** is a 7-tuple:
$$
(\mathcal{S}, \mathcal{F}, \mathcal{A}, \mathcal{G}, P, R, \gamma)
$$

where:

1. **State space**: $(\mathcal{S}, \mathcal{F})$ is a measurable space
   - $\mathcal{F}$ is a σ-algebra on $\mathcal{S}$ (Week 1, Definition 1.1)
   - **Typical case**: $\mathcal{S} \subseteq \mathbb{R}^n$ with Borel σ-algebra $\mathcal{F} = \mathcal{B}(\mathcal{S})$ (Week 1, Day 1)

2. **Action space**: $(\mathcal{A}, \mathcal{G})$ is a measurable space
   - **Typical case**: $\mathcal{A}$ compact metric space (e.g., $\mathcal{A} = [-1, 1]^d$ for bounded control)
   - Compactness required for Measurable Selection Theorem (Day 4)

3. **Transition kernel**: $P: \mathcal{S} \times \mathcal{A} \times \mathcal{F} \to [0,1]$ satisfies:
   - For each $(s,a) \in \mathcal{S} \times \mathcal{A}$: $P(\cdot \mid s,a)$ is a probability measure on $(\mathcal{S}, \mathcal{F})$
   - For each $A \in \mathcal{F}$: $(s,a) \mapsto P(A \mid s,a)$ is $\mathcal{F} \otimes \mathcal{G}$-measurable

   **Week 1 Connection**: $P(\cdot \mid s,a)$ constructed via Carathéodory (Week 1, Day 4, Theorem 1.10) from a density $p(s' \mid s,a)$ or from a stochastic differential equation.

   **Week 10 Connection**: $P$ is a Markov kernel. If $P$ is Feller (maps $C_b(\mathcal{S}) \to C_b(\mathcal{S})$), then value functions inherit continuity. Under **compact action sets** and **continuous rewards** $R$, and for $V \in C_b(\mathcal{S})$, the Bellman operator $T$ maps $C_b(\mathcal{S})$ to $C_b(\mathcal{S})$ (Berge's maximum theorem applied to $Q(s,a)$).

4. **Reward function**: $R: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ is measurable and bounded: $|R(s,a)| \leq R_{\max} < \infty$

   **Boundedness is essential**: Ensures Bellman operator is well-defined and DCT applies (Week 1, Day 3).

5. **Discount factor**: $\gamma \in [0, 1)$
   - Ensures geometric convergence of infinite sums: $\sum_{t=0}^\infty \gamma^t R_{\max} = R_{\max}/(1-\gamma) < \infty$

**Remark 23.1 (Why This Structure?)**

Every component has a **measure-theoretic reason**:
- σ-algebras $\mathcal{F}, \mathcal{G}$: Define observable events (Week 1, Day 5, "observability = measurability")
- Measurable $P, R$: Ensure expectations $\mathbb{E}_{s' \sim P}[V(s')]$ are well-defined
- Bounded $R$: Guarantees DCT applies to justify $\lim \mathbb{E} = \mathbb{E} \lim$
- Compact $\mathcal{A}$: Ensures $\max_{a \in \mathcal{A}}$ attains its maximum (Weierstrass)

---

## Daily Breakdown (90 minutes/day)

### **Day 1 (Monday): Policies and Value Functions**

**⏱️ Segment 1 (40 min) – Reading**

**Topic**: _Policies, Trajectories, and Value Functions_

**Primary Reference**: Puterman §3.1-3.2, Bertsekas Vol I §1.1-1.2

**Content**:

1. **Definition 23.2 (Stationary Policy)**: A **stationary Markov policy** is a measurable function:
   $$
   \pi: (\mathcal{S}, \mathcal{F}) \to (\mathcal{A}, \mathcal{G})
   $$
   i.e., $\pi^{-1}(B) \in \mathcal{F}$ for all $B \in \mathcal{G}$.

   **Week 1 Connection**: Measurability ensures $\pi(s)$ depends only on **observable** information about $s$ (Week 1, Day 5, Section IV: "A policy measurable with respect to $\mathcal{F}$ can be implemented based on observable information").

   **Example**: Neural network policy $\pi_\theta: \mathbb{R}^n \to [-1,1]^d$ is measurable (composition of continuous affine maps + activations, Week 1, Proposition 1.4).

2. **Stochastic Policies**: More generally, $\pi(da \mid s)$ is a **randomized policy**:
   $$
   \pi: \mathcal{S} \times \mathcal{G} \to [0,1]
   $$
   - For each $s$: $\pi(\cdot \mid s)$ is a probability measure on $(\mathcal{A}, \mathcal{G})$
   - For each $B \in \mathcal{G}$: $s \mapsto \pi(B \mid s)$ is $\mathcal{F}$-measurable

   **Example**: Gaussian policy $\pi(a \mid s) = \mathcal{N}(a; \mu_\theta(s), \Sigma)$ for continuous control.

3. **State-Value Function**: For policy $\pi$, the **state-value function** is:
   $$
   V^\pi(s) = \mathbb{E}^\pi\left[\sum_{t=0}^\infty \gamma^t R(S_t, A_t) \,\Big|\, S_0 = s\right]
   $$

   where $A_t \sim \pi(\cdot \mid S_t)$, $S_{t+1} \sim P(\cdot \mid S_t, A_t)$.

   **Week 4 Connection**: This is a conditional expectation $\mathbb{E}[\cdot \mid S_0 = s]$ (Week 4, Monday-Wednesday).

4. **Action-Value Function (Q-function)**:
   $$
   Q^\pi(s,a) = R(s,a) + \gamma \int_{\mathcal{S}} V^\pi(s') \, P(ds' \mid s,a)
   $$

   **Week 1 Connection**: The integral is well-defined by Carathéodory (Week 1, Day 4): $P(\cdot \mid s,a)$ is a probability measure on $(\mathcal{S}, \mathcal{F})$, and $V^\pi$ is measurable.

**⏱️ Segment 2 (40 min) – Proof Exercise**

**Exercise 23.1 (Value Function is Measurable)**:

Prove that if $R: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ is measurable and bounded, and $P$ is a Markov kernel, then the state-value function $V^\pi: \mathcal{S} \to \mathbb{R}$ is $\mathcal{F}$-measurable.

**Proof Sketch**:

**Step 1**: Write $V^\pi$ as a telescoping sum.
$$
V^\pi(s) = R(s, \pi(s)) + \gamma \int V^\pi(s') \, P(ds' \mid s, \pi(s)) + \gamma^2 \int \left(\int V^\pi(s'') \, P(ds'' \mid s', \pi(s'))\right) P(ds' \mid s, \pi(s)) + \cdots
$$

**Step 2**: Define the **iterate sequence**.

Let $V_0(s) = 0$. Define recursively:
$$
V_{n+1}(s) = R(s, \pi(s)) + \gamma \int V_n(s') \, P(ds' \mid s, \pi(s))
$$

**Claim**: Each $V_n$ is measurable.

**Proof by induction**:
- Base case: $V_0 = 0$ is constant, hence measurable.
- Inductive step: Assume $V_n$ measurable. Then:
  - $s \mapsto R(s, \pi(s))$ is measurable (composition: $R \circ (\text{id}, \pi)$)
  - $s \mapsto \int V_n(s') P(ds' \mid s, \pi(s))$ is measurable by the Markov kernel property (Week 10, Exercise 10.1)

Therefore $V_{n+1}$ is a sum of measurable functions, hence measurable.

**Step 3**: Apply pointwise convergence.

Since $|R| \leq R_{\max}$ and $\gamma < 1$:
$$
|V_n(s)| \leq R_{\max} \sum_{k=0}^{n-1} \gamma^k \leq \frac{R_{\max}}{1-\gamma}
$$

By geometric series convergence, $V_n(s) \to V^\pi(s)$ pointwise.

By **Week 1, Proposition 1.3** (pointwise limits of measurable functions are measurable):
$$
V^\pi = \lim_{n \to \infty} V_n \quad \text{is measurable.}
$$

□

**Remark**: This proof directly applies Week 1 machinery: composition closure (Proposition 1.4), kernel measurability (Week 10), and limit closure (Proposition 1.3). The boundedness assumption on $R$ is **essential**—without it, the geometric series may diverge.

**⏱️ Segment 3 (10 min) – Reflection**

**Question**: Why must policies be measurable?

**Answer**: Non-measurable policies would make value functions non-measurable, rendering expectations $\mathbb{E}[V^\pi]$ undefined. Measurability is not a technicality—it's the requirement that decisions be based on observable information.

---

### **Day 2 (Tuesday): Bellman Consistency Equations**

**⏱️ Segment 1 (40 min) – Reading**

**Topic**: _Bellman Equations as Fixed-Point Equations_

**Primary Reference**: Puterman §4.1-4.2

**Content**:

1. **Bellman Consistency Equation (Policy Evaluation)**:

   For a fixed policy $\pi$, the value function $V^\pi$ satisfies:
   $$
   V^\pi(s) = R(s, \pi(s)) + \gamma \int_{\mathcal{S}} V^\pi(s') \, P(ds' \mid s, \pi(s))
   $$

   **Compact operator notation**:
   $$
   V^\pi = T^\pi V^\pi
   $$

   where $(T^\pi V)(s) = R(s, \pi(s)) + \gamma \int V(s') P(ds' \mid s, \pi(s))$.

2. **Theorem 23.1 (Tower Property $\iff$ Bellman Consistency)**:

   The Bellman equation is a direct consequence of the **tower property** of conditional expectation (Week 4, Wednesday):
   $$
   \mathbb{E}[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}] = \mathbb{E}[X \mid \mathcal{H}] \quad \text{when } \mathcal{H} \subseteq \mathcal{G}
   $$

   **Proof**:

   Recall $V^\pi(s) = \mathbb{E}^\pi[\sum_{t=0}^\infty \gamma^t R(S_t, A_t) \mid S_0 = s]$.

   **Step 1**: Separate the first reward.
   $$
   V^\pi(s) = \mathbb{E}^\pi\left[R(S_0, A_0) + \sum_{t=1}^\infty \gamma^t R(S_t, A_t) \,\Big|\, S_0 = s\right]
   $$

   **Step 2**: Factor out $\gamma$ from the tail.
   $$
   V^\pi(s) = \mathbb{E}^\pi[R(S_0, A_0) \mid S_0 = s] + \gamma \mathbb{E}^\pi\left[\sum_{t=0}^\infty \gamma^t R(S_{t+1}, A_{t+1}) \,\Big|\, S_0 = s\right]
   $$

   **Step 3**: Apply tower property.

   Let $\mathcal{F}_1 = \sigma(S_1)$ (σ-algebra generated by $S_1$). By the tower property:
   $$
   \mathbb{E}^\pi\left[\sum_{t=0}^\infty \gamma^t R(S_{t+1}, A_{t+1}) \,\Big|\, S_0 = s\right] = \mathbb{E}^\pi\left[\mathbb{E}^\pi\left[\sum_{t=0}^\infty \gamma^t R(S_{t+1}, A_{t+1}) \,\Big|\, \mathcal{F}_1\right] \,\Big|\, S_0 = s\right]
   $$

   **Step 4**: Recognize inner expectation as $V^\pi(S_1)$.

   By the Markov property:
   $$
   \mathbb{E}^\pi\left[\sum_{t=0}^\infty \gamma^t R(S_{t+1}, A_{t+1}) \,\Big|\, S_1 = s'\right] = V^\pi(s')
   $$

   Therefore:
   $$
   V^\pi(s) = R(s, \pi(s)) + \gamma \mathbb{E}^\pi[V^\pi(S_1) \mid S_0 = s] = R(s, \pi(s)) + \gamma \int V^\pi(s') P(ds' \mid s, \pi(s))
   $$

   □

   **Week 4 Callback**: Week 4's tower property ("abstract nonsense") becomes the **Bellman consistency equation** (the heart of dynamic programming).

3. **Bellman Optimality Equation**:

   The **optimal value function** $V^*$ satisfies:
   $$
   V^*(s) = \max_{a \in \mathcal{A}} \left\{R(s,a) + \gamma \int_{\mathcal{S}} V^*(s') \, P(ds' \mid s,a)\right\}
   $$

   Define the **Bellman optimality operator**:
   $$
   (T V)(s) = \max_{a \in \mathcal{A}} \left\{R(s,a) + \gamma \int V(s') \, P(ds' \mid s,a)\right\}
   $$

   Then $V^*$ is the unique fixed point: $V^* = T V^*$.

**⏱️ Segment 2 (40 min) – Proof Exercise**

**Exercise 23.2 (Bellman Operator is a Contraction)**:

Prove that $T: \mathcal{B}(\mathcal{S}) \to \mathcal{B}(\mathcal{S})$ is a $\gamma$-contraction in the supremum norm:
$$
\|T V_1 - T V_2\|_\infty \leq \gamma \|V_1 - V_2\|_\infty
$$

**Proof**:

Fix $V_1, V_2 \in \mathcal{B}(\mathcal{S})$ (bounded measurable functions).

**Step 1**: Bound the difference pointwise.

For any $s \in \mathcal{S}$:
$$
|(TV_1)(s) - (TV_2)(s)| = \left|\max_a Q_1(s,a) - \max_a Q_2(s,a)\right|
$$

where $Q_i(s,a) = R(s,a) + \gamma \int V_i(s') P(ds' \mid s,a)$.

**Step 2**: Use max inequality.

Recall: $|\max_a f(a) - \max_a g(a)| \leq \max_a |f(a) - g(a)|$.

Therefore:
$$
|(TV_1)(s) - (TV_2)(s)| \leq \max_a |Q_1(s,a) - Q_2(s,a)|
$$

**Step 3**: Bound $|Q_1 - Q_2|$.

$$
|Q_1(s,a) - Q_2(s,a)| = \gamma \left|\int (V_1(s') - V_2(s')) P(ds' \mid s,a)\right| \leq \gamma \int |V_1(s') - V_2(s')| P(ds' \mid s,a)
$$

Since $P(ds' \mid s,a)$ is a probability measure:
$$
\int |V_1(s') - V_2(s')| P(ds' \mid s,a) \leq \|V_1 - V_2\|_\infty \cdot \int P(ds' \mid s,a) = \|V_1 - V_2\|_\infty
$$

**Step 4**: Conclude.

$$
|(TV_1)(s) - (TV_2)(s)| \leq \gamma \|V_1 - V_2\|_\infty
$$

Taking supremum over $s$:
$$
\|TV_1 - TV_2\|_\infty \leq \gamma \|V_1 - V_2\|_\infty
$$

Since $\gamma < 1$, $T$ is a contraction. □

**Remark**: By the **Banach Fixed-Point Theorem** (Week 16, Theorem 16.1), $T$ has a unique fixed point $V^* \in \mathcal{B}(\mathcal{S})$, and value iteration $V_{n+1} = TV_n$ converges geometrically: $\|V_n - V^*\|_\infty \leq \gamma^n \|V_0 - V^*\|_\infty$.

**⏱️ Segment 3 (10 min) – Reflection**

**Question**: Why does the contraction depend on $\gamma < 1$?

**Answer**: The discount factor $\gamma$ propagates the error from $V$ to $TV$. Without discounting ($\gamma = 1$), the Bellman operator may not be a contraction (average-reward MDPs require different techniques; see Week 26).

---

### **Day 3 (Wednesday): Measurability of the Maximum Operation**

**⏱️ Segment 1 (40 min) – Reading**

**Topic**: _When is $\max_{a \in \mathcal{A}} f(s,a)$ Measurable in $s$?_

**Primary Reference**: Puterman §A.4 (Appendix), Bertsekas Vol I §1.3

**Content**:

1. **The Problem**: The Bellman optimality operator involves:
   $$
   (TV)(s) = \max_{a \in \mathcal{A}} Q(s,a)
   $$

   We need two properties:
   - **(P1)**: The maximum exists (attained by some $a^* \in \mathcal{A}$)
   - **(P2)**: The function $s \mapsto \max_a Q(s,a)$ is measurable

   **Week 1 Callback**: We asked in Day 5, Open Question 3:
   > "Is the argmax operation measurable? That is, if $Q(s, \cdot): \mathcal{A} \to \mathbb{R}$ is measurable for each $s$, is $\pi^*(s) = \arg\max_a Q(s,a)$ a measurable function?"

   **This week provides the answer.**

2. **Theorem 23.2 (Maximum Theorem / Berge)**:

   Let $\mathcal{A}$ be a **compact metric space**, and $f: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ satisfy:
   - (i) For each $s \in \mathcal{S}$: $a \mapsto f(s,a)$ is continuous
   - (ii) For each $a \in \mathcal{A}$: $s \mapsto f(s,a)$ is measurable

   Then:
   - The function $\phi(s) = \max_{a \in \mathcal{A}} f(s,a)$ is **measurable**

   **Proof Sketch**:

   **Step 1**: The maximum exists by Weierstrass (compactness + continuity).

   **Step 2**: To show $\phi$ is measurable, verify $\{\phi \geq c\} \in \mathcal{F}$ for all $c \in \mathbb{R}$.

   Note that:
   $$
   \phi(s) \geq c \iff \exists a \in \mathcal{A}: f(s,a) \geq c
   $$

   **Step 3**: Use separability of $\mathcal{A}$.

   Since $\mathcal{A}$ is a compact metric space, it is separable: there exists a countable dense subset $\{a_1, a_2, \ldots\} \subseteq \mathcal{A}$.

   For continuous $f(s, \cdot)$:
   $$
   \max_{a \in \mathcal{A}} f(s,a) = \sup_{n \geq 1} f(s, a_n)
   $$

   **Step 4**: Conclude measurability.

   Each $s \mapsto f(s, a_n)$ is measurable by hypothesis (ii). The supremum of a countable family of measurable functions is measurable (Week 1, Proposition 1.3).

   Therefore $\phi(s) = \sup_n f(s, a_n)$ is measurable. □

3. **Corollary 23.3 (Bellman Operator Preserves Measurability)**:

   If $V \in \mathcal{B}(\mathcal{S})$, then $TV \in \mathcal{B}(\mathcal{S})$.

   **Proof**: Apply Theorem 23.2 with $f(s,a) = R(s,a) + \gamma \int V(s') P(ds' \mid s,a)$.
   - Continuity in $a$: If $P$ is Feller and $R$ is continuous in $a$, then $f(s, \cdot)$ is continuous (Week 10, Feller property)
   - Measurability in $s$: Week 10, Exercise 10.1

   Therefore $(TV)(s) = \max_a f(s,a)$ is measurable. Moreover, if $R$ is continuous in $(s,a)$, $P$ is **Feller** in $s$ for each fixed $a$, and $V \in C_b(\mathcal{S})$, then $f$ is continuous in $(s,a)$; by Berge's theorem on compact $\mathcal{A}$, $s \mapsto (TV)(s)$ is continuous. Hence $T: C_b(\mathcal{S}) \to C_b(\mathcal{S})$ under these hypotheses. □

**⏱️ Segment 2 (40 min) – Proof Exercise**

**Exercise 23.3 (Supremum of Countable Family is Measurable)**:

Let $f_n: \mathcal{S} \to \mathbb{R}$ be measurable functions for $n = 1, 2, \ldots$. Prove that:
$$
g(s) = \sup_{n \geq 1} f_n(s)
$$
is measurable. (Recall: This is Week 1, Proposition 1.3, part (3). Provide a complete proof.)

**Proof**:

We must show $\{g > c\} \in \mathcal{F}$ for all $c \in \mathbb{R}$.

**Step 1**: Characterize the event.
$$
\{s : g(s) > c\} = \{s : \sup_n f_n(s) > c\} = \{s : \exists n \text{ with } f_n(s) > c\}
$$

**Step 2**: Write as countable union.
$$
\{g > c\} = \bigcup_{n=1}^\infty \{f_n > c\}
$$

**Step 3**: Apply measurability of $f_n$.

Each $f_n$ is measurable, so $\{f_n > c\} \in \mathcal{F}$.

**Step 4**: Use σ-algebra closure.

$\mathcal{F}$ is closed under countable unions (Week 1, Definition 1.1), so:
$$
\{g > c\} = \bigcup_{n=1}^\infty \{f_n > c\} \in \mathcal{F}
$$

Therefore $g$ is measurable. □

**⏱️ Segment 3 (10 min) – Reflection**

**Question**: Why do we need $\mathcal{A}$ to be compact?

**Answer**: Compactness ensures (via Weierstrass) that the maximum is **attained**. Without compactness, $\sup$ may not equal $\max$ (e.g., $\sup_{x \in (0,1)} x = 1$ but maximum doesn't exist in $(0,1)$). For unbounded action spaces, we need coercivity conditions.

---

### **Day 4 (Thursday): Measurable Selection Theorem (Extended Proof)**

**⏱️ Segment 1 (30 min) – Theorem Statement**

**Theorem 23.4 (Measurable Selection Theorem / Kuratowski-Ryll-Nardzewski)**:

Let $(\mathcal{S}, \mathcal{F})$ be a measurable space, $\mathcal{A}$ a compact metric space, and $f: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ satisfy:
- (i) For each $s$: $a \mapsto f(s,a)$ is continuous
- (ii) For each $a$: $s \mapsto f(s,a)$ is measurable

Then there exists a **measurable function** $\pi^*: \mathcal{S} \to \mathcal{A}$ such that:
$$
f(s, \pi^*(s)) = \max_{a \in \mathcal{A}} f(s,a) \quad \text{for all } s \in \mathcal{S}
$$

**Intuition**: Not only is the maximum value measurable (Theorem 23.2), but we can **select** a maximizer measurably.

**Week 1 Callback**: This redeems the promissory note from Week 1, Day 5, Open Question 3. The optimal policy $\pi^*(s) = \arg\max_a Q(s,a)$ is indeed measurable.

**⏱️ Segment 2 (60 min) – Proof Sketch**

**Proof** (Outline; full proof requires advanced techniques beyond this course):

**Step 1**: Approximate $f$ uniformly by simple functions.

Since $\mathcal{A}$ is compact metric, it admits a countable dense subset $D = \{a_1, a_2, \ldots\}$.

Define the **ε-approximate argmax**:
$$
\pi_\varepsilon(s) = \text{some } a_n \in D \text{ with } f(s, a_n) \geq \max_{a \in \mathcal{A}} f(s,a) - \varepsilon
$$

Since $D$ is countable, we can construct $\pi_\varepsilon$ measurably by choosing the first $a_n$ (in enumeration order) satisfying the inequality.

**Step 2**: Compactness ensures convergence.

For $\varepsilon_k \to 0$, the sequence $\{\pi_{\varepsilon_k}(s)\}$ has a convergent subsequence in the compact space $\mathcal{A}$.

**Step 3**: Define the limit.

By a diagonal argument (requires some care), we can extract a measurable $\pi^*$ such that:
$$
f(s, \pi^*(s)) = \lim_{k \to \infty} f(s, \pi_{\varepsilon_k}(s)) = \max_a f(s,a)
$$

The measurability of $\pi^*$ follows from the measurable approximations $\pi_{\varepsilon_k}$ and closure under pointwise limits.

□ (Sketch complete; rigorous proof uses Kuratowski-Ryll-Nardzewski theorem from descriptive set theory.)

**Remark**: For our purposes (MDPs with compact action spaces and continuous Q-functions), this theorem guarantees **optimal policies exist and are measurable**. In practice (neural network policies), we approximate $\pi^*$ numerically.

**⏱️ Segment 3** – Reflection: Why is measurability of $\pi^*$ essential?

---

### **Day 5 (Friday): Computational Synthesis**

**⏱️ Segment 1 (20 min) – Review**

Recap the week:
1. MDPs formalized as 6-tuple with measurability requirements throughout
2. Bellman consistency equation = tower property of conditional expectation
3. Bellman optimality operator is a $\gamma$-contraction (Banach fixed-point theorem)
4. Maximum operation preserves measurability (Berge's Maximum Theorem)
5. Optimal policies exist and are measurable (Measurable Selection Theorem)

**Promissory Notes Redeemed**:
- Week 1, Day 1: Policies are measurable functions ✅
- Week 1, Day 4: Transition kernels via Carathéodory ✅
- Week 1, Day 3: DCT justifies $\lim \mathbb{E} = \mathbb{E} \lim$ ✅
- Week 1, Day 5: Measurable Selection Theorem for $\pi^* = \arg\max$ ✅

**⏱️ Segment 2 (30 min) – Proof Review**

Review Exercise 23.2 (Bellman operator is contraction) and Theorem 23.4 (Measurable Selection).

**⏱️ Segment 3 (40 min) – Coding Synthesis**

**Implementation**: Value iteration for a simple continuous-state MDP.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# MDP: S = [0,1], A = {-0.1, 0, +0.1}, Gaussian transitions, quadratic cost

# State grid
N = 101
S = np.linspace(0, 1, N)
ds = S[1] - S[0]

# Actions
A = np.array([-0.1, 0.0, 0.1])

# Reward: R(s,a) = -s² (cost to deviate from 0)
def reward(s, a):
    return -s**2

# Transition kernel: P(s' | s, a) = N(s', s+a, σ²) truncated to [0,1]
sigma = 0.05

def transition_prob(s_prime, s, a):
    """Probability density at s' given (s,a)."""
    return norm.pdf(s_prime, loc=s + a, scale=sigma)

# Discretize transition kernel
P = np.zeros((len(A), N, N))  # P[action_idx, s_idx, s_prime_idx]
for a_idx, a in enumerate(A):
    for s_idx, s in enumerate(S):
        P[a_idx, s_idx, :] = transition_prob(S, s, a)
        P[a_idx, s_idx, :] /= P[a_idx, s_idx, :].sum() * ds  # Normalize

# Value iteration
gamma = 0.95
V = np.zeros(N)
tolerance = 1e-6
max_iter = 1000

for iteration in range(max_iter):
    V_old = V.copy()

    # Bellman optimality operator
    Q = np.zeros((N, len(A)))
    for a_idx, a in enumerate(A):
        for s_idx, s in enumerate(S):
            Q[s_idx, a_idx] = reward(s, a) + gamma * np.sum(P[a_idx, s_idx, :] * V * ds)

    V = np.max(Q, axis=1)

    # Check convergence
    if np.max(np.abs(V - V_old)) < tolerance:
        print(f"Converged in {iteration+1} iterations")
        break

# Optimal policy
pi_star = A[np.argmax(Q, axis=1)]

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(S, V, linewidth=2)
ax1.set_xlabel('State $s$')
ax1.set_ylabel('Optimal Value $V^*(s)$')
ax1.set_title('Value Function (Value Iteration)')
ax1.grid(True, alpha=0.3)

ax2.plot(S, pi_star, linewidth=2, color='green')
ax2.set_xlabel('State $s$')
ax2.set_ylabel('Optimal Action $\pi^*(s)$')
ax2.set_title('Optimal Policy')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('week23_value_iteration.png', dpi=150)
plt.show()

print(f"→ Bellman operator is γ={gamma}-contraction")
print(f"→ V* is unique fixed point (Banach)")
print(f"→ π* = argmax Q(s,·) is measurable (Measurable Selection Theorem)")
```

**Expected Output**: $V^*$ is smooth (continuous), $\pi^*$ is piecewise constant (discrete action set). The policy drives the state toward $s = 0$ (minimizes cost).

**RL Connection**: This is the foundation of Deep Q-Networks (DQN): replace tabular $Q(s,a)$ with neural network $Q_\theta(s,a)$, use value iteration via gradient descent.

---

## Anchor Exercises (Week 23)

1. **Exercise 23.1**: Prove value function is measurable (Day 1) ✅ **ANCHOR**
2. **Exercise 23.2**: Prove Bellman operator is $\gamma$-contraction (Day 2) ✅ **ANCHOR**
3. **Exercise 23.3**: Prove supremum of countable family is measurable (Day 3)
4. **Theorem 23.4**: Measurable Selection Theorem (sketch proof, Day 4) ✅ **ANCHOR**

---

## Postponed Generalizations (Week 23)

| **What Was Postponed** | **Why Postponed** | **Where Proven** | **When It Matters** |
|------------------------|-------------------|------------------|---------------------|
| Unbounded rewards | Requires weighted supremum norms | Week 26 | Average-reward MDPs with unbounded $R$ |
| Non-compact action spaces | Requires coercivity/growth conditions | Advanced topic | Continuous control with $\mathcal{A} = \mathbb{R}^d$ unbounded |
| POMDPs (partial observability) | Requires belief-state MDP construction | Week 28 (research topic) | Real-world robotics with sensor uncertainty |
| Continuous-time MDPs | Requires Kolmogorov backward equation | Week 38 | High-frequency trading, queueing systems |

---

## Forward Connections

- **Week 24**: Value iteration convergence rates, policy iteration, linear programming formulation
- **Week 26**: Average-reward MDPs (remove discounting, require ergodic theory from Week 9)
- **Week 34**: TD learning as stochastic approximation for solving Bellman equation
- **Week 37**: Policy gradient theorem: $\nabla J(\theta) = \mathbb{E}[\nabla \log \pi_\theta \cdot Q^\pi]$ (Radon-Nikodym for likelihood ratios, Week 3)
- **Week 40**: Deep RL theory (neural network function approximation, generalization bounds)

---

## Cross-References to Week 1

| Week 1 Result | Week 23 Application |
|---------------|---------------------|
| σ-algebras define observability (Day 1) | State/action spaces $(\mathcal{S}, \mathcal{F})$, $(\mathcal{A}, \mathcal{G})$ must be measurable |
| Measurable functions (Definition 1.8) | Policies $\pi: \mathcal{S} \to \mathcal{A}$ must be measurable |
| Carathéodory Extension (Day 4, Theorem 1.10) | Transition kernels $P(\cdot \mid s,a)$ constructed as probability measures |
| Dominated Convergence (Day 3, Theorem 1.8) | Justifies $\lim_{n \to \infty} (T^n V)(s) = V^*(s)$ in value iteration |
| Closure under supremum (Proposition 1.3) | Maximum theorem: $\max_a Q(s,a)$ is measurable |
| Pointwise limits (Proposition 1.3) | Value iteration $V_{n+1} = TV_n$ converges to measurable $V^*$ |

**Central Callback**: "Measure theory is the language of RL" (Week 1, Day 5) is now fully justified.

---

## Assessment Criteria

By the end of Week 23, you should be able to:

✅ Define an MDP formally with all measurability requirements
✅ Prove the Bellman consistency equation from the tower property
✅ Prove the Bellman operator is a $\gamma$-contraction
✅ Verify that optimal policies exist (Weierstrass) and are measurable (Measurable Selection Theorem)
✅ Implement value iteration for discrete/continuous MDPs
✅ Articulate how Week 1 machinery (σ-algebras, measurability, Carathéodory, DCT) underpins every MDP definition

---

**Milestone**: MDP formalism complete. Ready for algorithms (value iteration, policy iteration, linear programming) in Week 24.

**Next Week (Week 24)**: Optimal Policies and Value Iteration. We prove convergence rates, study policy improvement, and connect to linear programming duality (Week 3, Radon-Nikodym).

---

📅 **Prepared**: October 2025
📍 **Context**: Architectural plan drafted in Week 1 to show narrative arc
🔗 **Cross-links**: Week 1 (all days), Week 4 (conditional expectation), Week 10 (Markov kernels), Week 16 (Banach fixed-point)
