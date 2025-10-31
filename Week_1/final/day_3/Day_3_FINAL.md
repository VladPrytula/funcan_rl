[[Day_2_FINAL#]]

### Agenda:

##### 📘 Day 3 – Week 1: Fatou's Lemma and Dominated Convergence (FINAL_V2)
**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (40 min) – Reading**

**Topic:** _Fatou's Lemma and Dominated Convergence Theorem_

- Read from [@folland:real_analysis:1999, §2.3] or [@durrett:probability:2019, Ch. 1].
- Focus on:
    - Statement of Fatou's Lemma and its relationship to MCT
    - Dominated Convergence Theorem (DCT) complete statement
    - Why domination is essential for limit interchange
    - Examples where DCT applies vs. fails
- _Key takeaway:_ DCT is the workhorse theorem for RL—it enables interchange of expectation and limits in policy evaluation, value iteration, and temporal difference learning.

---

#### **⏱️ Segment 2 (40 min) – Proof/Exercise**

**Exercise:**
Understand the proof of Fatou's Lemma and its role in proving DCT. Work through the chain:
1. Fatou's Lemma (proof via MCT)
2. DCT (proof via Fatou applied to $g \pm f_n$)

**Hints:**
- For Fatou: Consider $\inf_{k \geq n} f_k$ and apply MCT
- For DCT: Use $g - f_n \geq 0$ and $g + f_n \geq 0$ to apply Fatou in both directions
- Reflect on where the dominating function $g$ is essential

---

#### **⏱️ Segment 3 (10 min) – Reflection**

**Conceptual bridge to RL:**
- DCT justifies computing $\lim_{n \to \infty} \mathbb{E}[V_n] = \mathbb{E}[\lim_{n \to \infty} V_n]$ in policy evaluation
- The dominating function corresponds to bounding value functions: $|V_n| \leq V_{\max}$
- Without domination, convergence of value iteration could fail
- Essential for proving correctness of TD($\lambda$), Q-learning, and policy gradient methods

**Open question for tomorrow:**
How does the requirement of a dominating function translate to boundedness assumptions in MDP theory? Where in the Carathéodory extension does countable additivity of the outer measure get promoted to countable additivity of the extended measure? Identify the exact proof step that requires the σ-algebra structure.

---

📅 Tomorrow (Day 4): **Extended proof of Carathéodory extension theorem** (Thursday long proof session).

---

### **Chapter 1: Foundations in Measure and Probability Theory**

#### **1.4 The Convergence Hierarchy: Fatou, Domination, and the Algebra of Limits**

**Motivation:** The Monotone Convergence Theorem, established in §1.3, is a powerful tool—but its scope is limited. It requires monotonicity, a condition that is often too strong for applications. Consider the iterative algorithms at the heart of reinforcement learning: value iteration, policy iteration, temporal difference learning. While we can sometimes engineer monotone sequences (e.g., $V_0 \leq V_1 \leq \cdots \leq V^*$ when initialized appropriately), in general the value function estimates $V_n(s)$ may oscillate before converging. The policy evaluation operator $T^\pi$ need not preserve monotonicity under arbitrary initialization.

Moreover, when we move from tabular settings to function approximation with neural networks, the sequence of value function approximations $V_{\theta_n}$ produced by gradient descent is decidedly non-monotone. Yet we still need to guarantee that $\mathbb{E}[V_{\theta_n}] \to \mathbb{E}[V^*]$ as $n \to \infty$. How can we justify this interchange of limit and expectation when monotonicity is absent?

The answer lies in the **Dominated Convergence Theorem** (DCT), the crown jewel of Lebesgue integration theory. DCT states that if a sequence of functions $f_n \to f$ pointwise and is **dominated** by an integrable function $g$ (meaning $|f_n| \leq g$ for all $n$), then $\int f_n \to \int f$. The hypothesis of domination replaces monotonicity, vastly expanding the theorem's applicability. Nearly every convergence argument in RL theory—from proving policy improvement to establishing convergence of stochastic approximation algorithms—rests on DCT or its probability-theoretic cousin, the Dominated Convergence Theorem for expectations.

But DCT does not appear from thin air. It is built upon a more primitive result, **Fatou's Lemma**, which handles lim inf of integrals. Fatou's Lemma is to DCT what MCT is to the Lebesgue integral: the foundational stone upon which the edifice is constructed. This section develops the convergence hierarchy in full: from MCT to Fatou to DCT, establishing the complete machinery for limit interchange that will be invoked hundreds of times in the chapters to come.

**Learning Objectives:**
* State and prove Fatou's Lemma, understanding its asymmetric nature (lim inf, not lim)
* Master the proof of DCT via Fatou's Lemma applied in both directions
* Identify where domination is essential through counterexamples
* Recognize DCT as the foundation for convergence proofs in RL algorithms

---

### **I. Core Theory: Fatou's Lemma**

We begin with a result that, while less celebrated than DCT, is logically prior and equally fundamental.

**Theorem 1.7 (Fatou's Lemma).** {#THM-1.3.1} Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^{\infty}$ be a sequence of non-negative measurable functions $f_n: X \to [0, \infty]$. Then:
$$
\int \liminf_{n \to \infty} f_n \, d\mu \leq \liminf_{n \to \infty} \int f_n \, d\mu \tag{1.4}
$$

**Remark 1.7 (The Asymmetry of Fatou).** Observe that Fatou's Lemma is a one-sided inequality. It asserts that the integral of the limit inferior cannot exceed the limit inferior of the integrals—integration preserves the lim inf inequality, but makes no claim about lim sup. Indeed, the reverse inequality generally fails. This asymmetry is not a defect—it reflects a deep fact: integration is a continuous operation from below (by MCT), but not necessarily from above. Fatou's Lemma captures precisely what survives when we relax monotonicity to mere non-negativity.

**Remark 1.8 (Why "lim inf"?).** Recall from analysis that for any sequence of real numbers $\{a_n\}$:
$$
\liminf_{n \to \infty} a_n = \lim_{n \to \infty} \left(\inf_{k \geq n} a_k\right) = \sup_{n \geq 1} \inf_{k \geq n} a_k.
$$
The sequence $\{\inf_{k \geq n} a_k\}$ is increasing in $n$ (as we throw away fewer terms, the infimum can only increase). Thus $\liminf$ is always the limit of an increasing sequence, even when the original sequence $\{a_n\}$ does not converge. This monotonicity is what allows us to apply MCT in the proof. The equivalence of the two definitions follows from the fact that $\{\inf_{k \geq n} a_k\}$ is increasing, hence its limit equals its supremum.

*Proof of Theorem 1.7.*

**Step 1: Define an increasing sequence.**
For each $n \in \mathbb{N}$, define:
$$
g_n(x) = \inf_{k \geq n} f_k(x).
$$
By the definition of infimum over a tail of the sequence, we have $g_1 \leq g_2 \leq g_3 \leq \cdots$, i.e., $\{g_n\}$ is an increasing sequence. Each $g_n$ is measurable since the infimum of a countable family of measurable functions is measurable [@folland:real_analysis:1999, §2.1].

**Step 2: Identify the limit of $\{g_n\}$.**
By the definition of $\liminf$:
$$
\liminf_{n \to \infty} f_n(x) = \lim_{n \to \infty} g_n(x) \quad \text{pointwise}.
$$

**Step 3: Apply MCT to $\{g_n\}$.**
Since $g_n \uparrow \liminf f_n$ and each $g_n \geq 0$ is measurable, the Monotone Convergence Theorem yields:
$$
\int \liminf_{n \to \infty} f_n \, d\mu = \lim_{n \to \infty} \int g_n \, d\mu.
$$

**Step 4: Bound the integrals of $g_n$.**
For each $n$ and each $k \geq n$, $g_n \leq f_k$. Hence:
$$
\int g_n \, d\mu \leq \inf_{k \geq n} \int f_k \, d\mu.
$$

**Step 5: Take the limit as $n \to \infty$.**
Combining Steps 3–4:
$$
\int \liminf_{n \to \infty} f_n \, d\mu \leq \lim_{n \to \infty} \left(\inf_{k \geq n} \int f_k \, d\mu\right) = \liminf_{n \to \infty} \int f_n \, d\mu.
$$
This is precisely (1.4). □

**Remark 1.9 (The Mechanism: MCT in Disguise).** The proof of Fatou is merely MCT applied to the auxiliary sequence $g_n = \inf_{k \geq n} f_k$. To handle a general sequence, we construct from it a monotone sequence (running infima), apply the monotone theorem, and then estimate. Fatou’s Lemma is MCT for non‑monotone sequences, at the cost of replacing $\lim$ with $\liminf$.

---

### **II. The Dominated Convergence Theorem**

Fatou’s lemma handles non‑negative functions but yields only a one‑sided inequality. To obtain full limit interchange for signed functions, we require an additional hypothesis—domination—which we now introduce.

**Theorem 1.8 (Dominated Convergence Theorem, DCT).** {#THM-1.3.2} Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n \ge 1}$ be measurable functions $f_n: X \to \mathbb{R}$ such that:
1. (Pointwise convergence) $f_n(x) \to f(x)$ for $\mu$-almost every $x$, where $f$ is measurable.
2. (Domination) There exists $g \in L^1(\mu)$ with $g \ge 0$ and $|f_n| \le g$ $\mu$-a.e. for all $n$.

Then $f \in L^1(\mu)$ and
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu = \int \lim_{n \to \infty} f_n \, d\mu. \tag{1.5}
$$

**Preliminary observation.** Since $|f_n| \le g \in L^1$, each $f_n \in L^1$ and the expressions $\int(g \pm f_n)\, d\mu = \int g\, d\mu \pm \int f_n\, d\mu$ are well‑defined. Moreover, by pointwise convergence and $|f_n| \le g$, we have $|f| \le g$ a.e., hence $f \in L^1$ and $\int |f| \le \int g$.

**Remark 1.10 (Why "Dominated"?).** The name derives from the hypothesis that $|f_n|$ is bounded above by an integrable function $g$. Without such control, $\int f_n$ could diverge even when $f_n \to f$ pointwise.

**Remark 1.11 (Sharpness of Hypotheses).** Both hypotheses are necessary. We demonstrate this with precise counterexamples in §III below (Examples 1.3–1.4) and systematically in Exercise 2 (Week_1/final/day_3/Day_3_exercises_FINAL_V2.md), where we construct counterexamples for MCT without monotonicity, DCT without pointwise convergence, and DCT without domination.

*Proof of Theorem 1.8.* Apply Fatou’s Lemma twice—to $g - f_n$ and to $g + f_n$.

**Step 1: Apply Fatou to $g - f_n$.**
Set $h_n = g - f_n \ge 0$. Since $f_n \to f$ a.e., $h_n \to g - f$ a.e. Fatou yields
$$
\int (g - f) \, d\mu \le \liminf_{n \to \infty} \int (g - f_n) \, d\mu = \int g \, d\mu - \limsup_{n \to \infty} \int f_n \, d\mu.
$$
Rearranging,
$$
\int f \, d\mu \ge \limsup_{n \to \infty} \int f_n \, d\mu. \tag{1.6}
$$

**Step 2: Apply Fatou to $g + f_n$.**
Set $k_n = g + f_n \ge 0$. Then $k_n \to g + f$ a.e., and Fatou gives
$$
\int (g + f) \, d\mu \le \liminf_{n \to \infty} \int (g + f_n) \, d\mu = \int g \, d\mu + \liminf_{n \to \infty} \int f_n \, d\mu.
$$
Rearranging,
$$
\int f \, d\mu \le \liminf_{n \to \infty} \int f_n \, d\mu. \tag{1.7}
$$

**Step 3: Conclude.** From (1.6)–(1.7), $\lim \int f_n$ exists and equals $\int f$.

**Remark 1.12 (The Proof Strategy: Fatou as Pliers).** We squeeze $\int f$ between $\limsup \int f_n$ and $\liminf \int f_n$ by applying Fatou twice—once to $g - f_n$ and once to $g + f_n$. The dominating function $g$ is the fulcrum that lifts the sequence into the non‑negative cone, where Fatou applies.

---

### **III. The Necessity Gallery: Counterexamples**

To appreciate DCT fully, we must see where it fails. The following examples establish the necessity of each hypothesis.

**Example 1.3 (Failure Without Domination: Escaping Mass).** {#EX-1.3.1}
Let $(X, \mathcal{F}, \mu) = (\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. Define $f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x)$. Then $f_n \to 0$ pointwise everywhere, but
$$
\int f_n \, d\lambda = \frac{1}{n} \cdot \lambda([0, n]) = 1.
$$
Any dominator must satisfy $g(x) \ge 1/\lceil x \rceil$ for $x>0$, hence $\int_{[1,\infty)} g \, d\lambda \ge \sum_{k=2}^\infty \frac{1}{k} = \infty$. No integrable dominator exists.

**Example 1.4 (Failure Without Pointwise Convergence: The Typewriter Sequence).** {#EX-1.3.2}
On $([0, 1], \mathcal{B}([0,1]), \lambda)$, enumerate dyadic intervals by level and set $f_n = \mathbf{1}_{I_n}$. Then $|f_n| \le 1$ (dominated), $\int f_n \to 0$, but for every $x$, $f_n(x)$ takes both values 0 and 1 infinitely often; no pointwise limit exists.

**Remark 1.13 (Synthesis).** These examples show the hypotheses of DCT are sharp: domination and pointwise convergence are both indispensable.

---

### **IV. Why DCT Matters for RL: Three Essential Applications**

**Remark 1.14 (Forward Connection: DCT in Probability and RL).** In probability, DCT reads: if $X_n \to X$ a.s. and $|X_n| \le Y$ with $Y \in L^1$, then $\mathbb{E}[X_n] \to \mathbb{E}[X]$. This appears throughout RL—policy evaluation, convergence of stochastic approximation, and policy gradient differentiation.

We now examine three essential applications.

**Application 1: Policy Evaluation and the Bellman Operator**

In policy evaluation, $V^\pi$ satisfies the Bellman equation
$$
V^\pi(s) = \mathbb{E}^\pi\big[ R_t + \gamma V^\pi(S_{t+1}) \mid S_t = s \big].
$$
The iterative scheme $V_{n+1} = T^\pi V_n := r^\pi + \gamma P^\pi V_n$ converges in $\|\cdot\|_\infty$ to $V^\pi$ when rewards are bounded and $\gamma<1$, with $|V_n| \le V_{\max} := R_{\max}/(1-\gamma)$. Uniform (hence pointwise) convergence $V_n \to V^\pi$ combined with domination by $V_{\max}$ yields, by DCT,
$$
\lim_{n \to \infty} \mathbb{E}_\mu[V_n] = \mathbb{E}_\mu[V^\pi]
$$
for any initial state distribution $\mu$.

**Application 2: Temporal Difference Learning**

For TD(0):
$$
V_{t+1}(S_t) = V_t(S_t) + \alpha_t \big[ R_t + \gamma V_t(S_{t+1}) - V_t(S_t) \big].
$$
Under standard conditions (Robbins–Monro stepsizes, bounded rewards, stability/ergodicity), the ODE method shows $V_t \to V^\pi$ a.s. DCT, with domination by $V_{\max}$ (or via reward clipping in deep RL), justifies $\mathbb{E}[V_t] \to \mathbb{E}[V^\pi]$.

**Application 3: Policy Gradient Methods**

For REINFORCE:
$$
\nabla_\theta J(\theta) = \nabla_\theta \mathbb{E}_{\tau \sim \pi_\theta}[G(\tau)] = \int [\nabla_\theta \pi_\theta(\tau)] \, G(\tau)\, d\tau,
$$
we justify interchanging $\nabla_\theta$ and $\int$ by DCT via a dominated difference quotient. Sufficient conditions include bounded returns and a uniformly Lipschitz policy gradient, or, in the unbounded case, uniform moment bounds that render the difference quotient integrable.

**Summary.** DCT underwrites virtually every rigorous interchange of limit and expectation in RL—convergence of value iteration, stochastic approximation, and the differentiation of expected returns.

---

### **V. Reflection and Forward Glances**

We have now completed the convergence hierarchy:
- **MCT (Theorem 1.2.1):** Monotone sequences $f_n \uparrow f$.
- **Fatou's Lemma (Theorem 1.7):** Non‑negative sequences; lim inf inequality.
- **DCT (Theorem 1.8):** General sequences under domination; full limit interchange.

**Open Question for Day 4.** In the proof of the Carathéodory extension theorem, isolate the step where countable additivity is promoted from the outer measure to the extended measure, and explain precisely where the σ‑algebra structure is used.

**Looking Ahead.**
- **Week 2, Day 1:** DCT in the proof that $L^1$ convergence implies a.e. convergence along a subsequence.
- **Week 6, Day 3:** Conditional expectation as an $L^2$ projection; extending properties from indicators via the functional monotone class theorem.
- **Week 36:** ODE method for stochastic approximation: controlled limit passages via DCT.

---

**End of Day 3 (FINAL_V2)**
[[Day_2_FINAL#]]

### Agenda:

##### 📘 Day 3 – Week 1: Fatou's Lemma and Dominated Convergence (FINAL_V2)
**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (40 min) – Reading**

**Topic:** _Fatou's Lemma and Dominated Convergence Theorem_

- Read from [@folland:real_analysis:1999, §2.3] or [@durrett:probability:2019, Ch. 1].
- Focus on:
    - Statement of Fatou's Lemma and its relationship to MCT
    - Dominated Convergence Theorem (DCT) complete statement
    - Why domination is essential for limit interchange
    - Examples where DCT applies vs. fails
- _Key takeaway:_ DCT is the workhorse theorem for RL—it enables interchange of expectation and limits in policy evaluation, value iteration, and temporal difference learning.

---

#### **⏱️ Segment 2 (40 min) – Proof/Exercise**

**Exercise:**
Understand the proof of Fatou's Lemma and its role in proving DCT. Work through the chain:
1. Fatou's Lemma (proof via MCT)
2. DCT (proof via Fatou applied to $g \pm f_n$)

**Hints:**
- For Fatou: Consider $\inf_{k \geq n} f_k$ and apply MCT
- For DCT: Use $g - f_n \geq 0$ and $g + f_n \geq 0$ to apply Fatou in both directions
- Reflect on where the dominating function $g$ is essential

---

#### **⏱️ Segment 3 (10 min) – Reflection**

**Conceptual bridge to RL:**
- DCT justifies computing $\lim_{n \to \infty} \mathbb{E}[V_n] = \mathbb{E}[\lim_{n \to \infty} V_n]$ in policy evaluation
- The dominating function corresponds to bounding value functions: $|V_n| \leq V_{\max}$
- Without domination, convergence of value iteration could fail
- Essential for proving correctness of TD($\lambda$), Q-learning, and policy gradient methods

**Open question for tomorrow:**
How does the requirement of a dominating function translate to boundedness assumptions in MDP theory? Where in the Carathéodory extension does countable additivity of the outer measure get promoted to countable additivity of the extended measure? Identify the exact proof step that requires the $\sigma$-algebra structure.

---

📅 Tomorrow (Day 4): **Extended proof of Carathéodory extension theorem** (Thursday long proof session).

---

### **Chapter 1: Foundations in Measure and Probability Theory**

#### **1.4 The Convergence Hierarchy: Fatou, Domination, and the Algebra of Limits**

**Motivation:** The Monotone Convergence Theorem, established in §1.3, is a powerful tool—but its scope is limited. It requires monotonicity, a condition that is often too strong for applications. Consider the iterative algorithms at the heart of reinforcement learning: value iteration, policy iteration, temporal difference learning. While we can sometimes engineer monotone sequences (e.g., $V_0 \leq V_1 \leq \cdots \leq V^*$ when initialized appropriately), in general the value function estimates $V_n(s)$ may oscillate before converging. The policy evaluation operator $T^\pi$ need not preserve monotonicity under arbitrary initialization.

Moreover, when we move from tabular settings to function approximation with neural networks, the sequence of value function approximations $V_{\theta_n}$ produced by gradient descent is decidedly non-monotone. Yet we still need to guarantee that $\mathbb{E}[V_{\theta_n}] \to \mathbb{E}[V^*]$ as $n \to \infty$. How can we justify this interchange of limit and expectation when monotonicity is absent?

The answer lies in the **Dominated Convergence Theorem** (DCT), the crown jewel of Lebesgue integration theory. DCT states that if a sequence of functions $f_n \to f$ pointwise and is **dominated** by an integrable function $g$ (meaning $|f_n| \leq g$ for all $n$), then $\int f_n \to \int f$. The hypothesis of domination replaces monotonicity, vastly expanding the theorem's applicability. Nearly every convergence argument in RL theory—from proving policy improvement to establishing convergence of stochastic approximation algorithms—rests on DCT or its probability-theoretic cousin, the Dominated Convergence Theorem for expectations.

But DCT does not appear from thin air. It is built upon a more primitive result, **Fatou's Lemma**, which handles lim inf of integrals. Fatou's Lemma is to DCT what MCT is to the Lebesgue integral: the foundational stone upon which the edifice is constructed. This section develops the convergence hierarchy in full: from MCT to Fatou to DCT, establishing the complete machinery for limit interchange that will be invoked hundreds of times in the chapters to come.

**Learning Objectives:**
* State and prove Fatou's Lemma, understanding its asymmetric nature (lim inf, not lim)
* Master the proof of DCT via Fatou's Lemma applied in both directions
* Identify where domination is essential through counterexamples
* Recognize DCT as the foundation for convergence proofs in RL algorithms

---

### **I. Core Theory: Fatou's Lemma**

We begin with a result that, while less celebrated than DCT, is logically prior and equally fundamental.

**Theorem 1.7 (Fatou's Lemma).** {#THM-1.3.1} Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^{\infty}$ be a sequence of non-negative measurable functions $f_n: X \to [0, \infty]$. Then:
$$
\int \liminf_{n \to \infty} f_n \, d\mu \leq \liminf_{n \to \infty} \int f_n \, d\mu \tag{1.4}
$$

**Remark 1.7 (The Asymmetry of Fatou).** Observe that Fatou's Lemma is a one-sided inequality. It asserts that the integral of the limit inferior cannot exceed the limit inferior of the integrals—integration preserves the lim inf inequality, but makes no claim about lim sup. Indeed, the reverse inequality generally fails. This asymmetry is not a defect—it reflects a deep fact: integration is a continuous operation from below (by MCT), but not necessarily from above. Fatou's Lemma captures precisely what survives when we relax monotonicity to mere non-negativity.

**Remark 1.8 (Why "lim inf"?).** Recall from analysis that for any sequence of real numbers $\{a_n\}$:
$$
\liminf_{n \to \infty} a_n = \lim_{n \to \infty} \left(\inf_{k \geq n} a_k\right) = \sup_{n \geq 1} \inf_{k \geq n} a_k.
$$
The sequence $\{\inf_{k \geq n} a_k\}$ is increasing in $n$ (as we throw away fewer terms, the infimum can only increase). Thus $\liminf$ is always the limit of an increasing sequence, even when the original sequence $\{a_n\}$ does not converge. This monotonicity is what allows us to apply MCT in the proof. The equivalence of the two definitions follows from the fact that $\{\inf_{k \geq n} a_k\}$ is increasing, hence its limit equals its supremum.

*Proof of Theorem 1.7.*

**Step 1: Define an increasing sequence.**
For each $n \in \mathbb{N}$, define:
$$
g_n(x) = \inf_{k \geq n} f_k(x).
$$
By the definition of infimum over a tail of the sequence, we have $g_1 \leq g_2 \leq g_3 \leq \cdots$, i.e., $\{g_n\}$ is an increasing sequence. Each $g_n$ is measurable since the infimum of a countable family of measurable functions is measurable [@folland:real_analysis:1999, §2.1].

**Step 2: Identify the limit of $\{g_n\}$.**
By the definition of $\liminf$:
$$
\liminf_{n \to \infty} f_n(x) = \lim_{n \to \infty} g_n(x) \quad \text{pointwise}.
$$

**Step 3: Apply MCT to $\{g_n\}$.**
Since $g_n \uparrow \liminf f_n$ and each $g_n \geq 0$ is measurable, the Monotone Convergence Theorem yields:
$$
\int \liminf_{n \to \infty} f_n \, d\mu = \lim_{n \to \infty} \int g_n \, d\mu.
$$

**Step 4: Bound the integrals of $g_n$.**
For each $n$ and each $k \geq n$, $g_n \leq f_k$. Hence:
$$
\int g_n \, d\mu \leq \inf_{k \geq n} \int f_k \, d\mu.
$$

**Step 5: Take the limit as $n \to \infty$.**
Combining Steps 3–4:
$$
\int \liminf_{n \to \infty} f_n \, d\mu \leq \lim_{n \to \infty} \left(\inf_{k \geq n} \int f_k \, d\mu\right) = \liminf_{n \to \infty} \int f_n \, d\mu.
$$
This is precisely (1.4). □

**Remark 1.9 (The Mechanism: MCT in Disguise).** The proof of Fatou is merely MCT applied to the auxiliary sequence $g_n = \inf_{k \geq n} f_k$. To handle a general sequence, we construct from it a monotone sequence (running infima), apply the monotone theorem, and then estimate. Fatou’s Lemma is MCT for non‑monotone sequences, at the cost of replacing $\lim$ with $\liminf$.

---

### **II. The Dominated Convergence Theorem**

Fatou’s lemma handles non‑negative functions but yields only a one‑sided inequality. To obtain full limit interchange for signed functions, we require an additional hypothesis—domination—which we now introduce.

**Theorem 1.8 (Dominated Convergence Theorem, DCT).** {#THM-1.3.2} Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n \ge 1}$ be measurable functions $f_n: X \to \mathbb{R}$ such that:
1. (Pointwise convergence) $f_n(x) \to f(x)$ for $\mu$-almost every $x$, where $f$ is measurable.
2. (Domination) There exists $g \in L^1(\mu)$ with $g \ge 0$ and $|f_n| \le g$ $\mu$-a.e. for all $n$.

Then $f \in L^1(\mu)$ and
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu = \int \lim_{n \to \infty} f_n \, d\mu. \tag{1.5}
$$

**Preliminary observation.** Since $|f_n| \le g \in L^1$, each $f_n \in L^1$ and the expressions $\int(g \pm f_n)\, d\mu = \int g\, d\mu \pm \int f_n\, d\mu$ are well‑defined. Moreover, by pointwise convergence and $|f_n| \le g$, we have $|f| \le g$ a.e., hence $f \in L^1$ and $\int |f| \le \int g$.

**Remark 1.10 (Why "Dominated"?).** The name derives from the hypothesis that $|f_n|$ is bounded above by an integrable function $g$. Without such control, $\int f_n$ could diverge even when $f_n \to f$ pointwise.

**Remark 1.11 (Sharpness of Hypotheses).** Both hypotheses are necessary. We demonstrate this with precise counterexamples in §III below (Examples 1.3–1.4) and systematically in Exercise 2 (Week_1/final/day_3/Day_3_exercises_FINAL_V2.md), where we construct counterexamples for MCT without monotonicity, DCT without pointwise convergence, and DCT without domination.

*Proof of Theorem 1.8.* Apply Fatou’s Lemma twice—to $g - f_n$ and to $g + f_n$.

**Step 1: Apply Fatou to $g - f_n$.**
Set $h_n = g - f_n \ge 0$. Since $f_n \to f$ a.e., $h_n \to g - f$ a.e. Fatou yields
$$
\int (g - f) \, d\mu \le \liminf_{n \to \infty} \int (g - f_n) \, d\mu = \int g \, d\mu - \limsup_{n \to \infty} \int f_n \, d\mu.
$$
Rearranging,
$$
\int f \, d\mu \ge \limsup_{n \to \infty} \int f_n \, d\mu. \tag{1.6}
$$

**Step 2: Apply Fatou to $g + f_n$.**
Set $k_n = g + f_n \ge 0$. Then $k_n \to g + f$ a.e., and Fatou gives
$$
\int (g + f) \, d\mu \le \liminf_{n \to \infty} \int (g + f_n) \, d\mu = \int g \, d\mu + \liminf_{n \to \infty} \int f_n \, d\mu.
$$
Rearranging,
$$
\int f \, d\mu \le \liminf_{n \to \infty} \int f_n \, d\mu. \tag{1.7}
$$

**Step 3: Conclude.** From (1.6)–(1.7), $\lim \int f_n$ exists and equals $\int f$.

**Remark 1.12 (The Proof Strategy: Fatou as Pliers).** We squeeze $\int f$ between $\limsup \int f_n$ and $\liminf \int f_n$ by applying Fatou twice—once to $g - f_n$ and once to $g + f_n$. The dominating function $g$ is the fulcrum that lifts the sequence into the non‑negative cone, where Fatou applies.

---

### **III. The Necessity Gallery: Counterexamples**

To appreciate DCT fully, we must see where it fails. The following examples establish the necessity of each hypothesis.

**Example 1.3 (Failure Without Domination: Escaping Mass).** {#EX-1.3.1}
Let $(X, \mathcal{F}, \mu) = (\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. Define $f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x)$. Then $f_n \to 0$ pointwise everywhere, but
$$
\int f_n \, d\lambda = \frac{1}{n} \cdot \lambda([0, n]) = 1.
$$
Any dominator must satisfy $g(x) \ge 1/\lceil x \rceil$ for $x>0$, hence $\int_{[1,\infty)} g \, d\lambda \ge \sum_{k=2}^\infty \frac{1}{k} = \infty$. No integrable dominator exists.

**Example 1.4 (Failure Without Pointwise Convergence: The Typewriter Sequence).** {#EX-1.3.2}
On $([0, 1], \mathcal{B}([0,1]), \lambda)$, enumerate dyadic intervals by level and set $f_n = \mathbf{1}_{I_n}$. Then $|f_n| \le 1$ (dominated), $\int f_n \to 0$, but for every $x$, $f_n(x)$ takes both values 0 and 1 infinitely often; no pointwise limit exists.

**Remark 1.13 (Synthesis).** These examples show the hypotheses of DCT are sharp: domination and pointwise convergence are both indispensable.

---

### **IV. Why DCT Matters for RL: Three Essential Applications**

**Remark 1.14 (Forward Connection: DCT in Probability and RL).** In probability, DCT reads: if $X_n \to X$ a.s. and $|X_n| \le Y$ with $Y \in L^1$, then $\mathbb{E}[X_n] \to \mathbb{E}[X]$. This appears throughout RL—policy evaluation, convergence of stochastic approximation, and policy gradient differentiation.

We now examine three essential applications.

**Application 1: Policy Evaluation and the Bellman Operator**

In policy evaluation, $V^\pi$ satisfies the Bellman equation
$$
V^\pi(s) = \mathbb{E}^\pi\big[ R_t + \gamma V^\pi(S_{t+1}) \mid S_t = s \big].
$$
The iterative scheme $V_{n+1} = T^\pi V_n := r^\pi + \gamma P^\pi V_n$ converges in $\|\cdot\|_\infty$ to $V^\pi$ when rewards are bounded and $\gamma<1$, with $|V_n| \le V_{\max} := R_{\max}/(1-\gamma)$. Uniform (hence pointwise) convergence $V_n \to V^\pi$ combined with domination by $V_{\max}$ yields, by DCT,
$$
\lim_{n \to \infty} \mathbb{E}_\mu[V_n] = \mathbb{E}_\mu[V^\pi]
$$
for any initial state distribution $\mu$.

**Application 2: Temporal Difference Learning**

For TD(0):
$$
V_{t+1}(S_t) = V_t(S_t) + \alpha_t \big[ R_t + \gamma V_t(S_{t+1}) - V_t(S_t) \big].
$$
Under standard conditions (Robbins–Monro stepsizes, bounded rewards, stability/ergodicity), the ODE method shows $V_t \to V^\pi$ a.s. DCT, with domination by $V_{\max}$ (or via reward clipping in deep RL), justifies $\mathbb{E}[V_t] \to \mathbb{E}[V^\pi]$.

**Application 3: Policy Gradient Methods**

For REINFORCE:
$$
\nabla_\theta J(\theta) = \nabla_\theta \mathbb{E}_{\tau \sim \pi_\theta}[G(\tau)] = \int [\nabla_\theta \pi_\theta(\tau)] \, G(\tau)\, d\tau,
$$
we justify interchanging $\nabla_\theta$ and $\int$ by DCT via a dominated difference quotient. Sufficient conditions include bounded returns and a uniformly Lipschitz policy gradient, or, in the unbounded case, uniform moment bounds that render the difference quotient integrable.

**Summary.** DCT underwrites virtually every rigorous interchange of limit and expectation in RL—convergence of value iteration, stochastic approximation, and the differentiation of expected returns.

---

### **V. Reflection and Forward Glances**

We have now completed the convergence hierarchy:
- **MCT (Theorem 1.2.1):** Monotone sequences $f_n \uparrow f$.
- **Fatou's Lemma (Theorem 1.7):** Non‑negative sequences; lim inf inequality.
- **DCT (Theorem 1.8):** General sequences under domination; full limit interchange.

**Open Question for Day 4.** In the proof of the Carathéodory extension theorem, isolate the step where countable additivity is promoted from the outer measure to the extended measure, and explain precisely where the σ‑algebra structure is used.

**Looking Ahead.**
- **Week 2, Day 1:** DCT in the proof that $L^1$ convergence implies a.e. convergence along a subsequence.
- **Week 6, Day 3:** Conditional expectation as an $L^2$ projection; extending properties from indicators via the functional monotone class theorem.
- **Week 36:** ODE method for stochastic approximation: controlled limit passages via DCT.

---

**End of Day 3 (FINAL_V2)**
