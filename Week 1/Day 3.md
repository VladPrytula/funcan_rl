[[Day 2]]

### Agenda:

##### 📘 Day 3 – Week 1: Fatou's Lemma and Dominated Convergence
**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (40 min) – Reading**

**Topic:** _Fatou's Lemma and Dominated Convergence Theorem_

- Read from **Folland, "Real Analysis" §2.3** or Durrett Ch. 1.
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
- Essential for proving correctness of TD(λ), Q-learning, and policy gradient methods

**Open question for tomorrow:**
How does the requirement of a dominating function translate to boundedness assumptions in MDP theory?

---

📅 Tomorrow (Day 4): **Extended proof of Carathéodory extension theorem** (Thursday long proof session).

---

### **Chapter 1: Foundations in Measure and Probability Theory**

#### **1.4 The Convergence Hierarchy: Fatou, Domination, and the Algebra of Limits**

**Motivation:** The Monotone Convergence Theorem, established in §1.3, is a powerful tool—but its scope is limited. It requires monotonicity, a condition that is often too strong for applications. Consider the iterative algorithms at the heart of reinforcement learning: value iteration, policy iteration, temporal difference learning. While we can sometimes engineer monotone sequences (e.g., $V_0 \leq V_1 \leq \cdots \leq V^*$ when initialized appropriately), in general the value function estimates $V_n(s)$ may oscillate before converging. The policy evaluation operator $T^\pi$ need not preserve monotonicity under arbitrary initialization.

Moreover, when we move from tabular settings to function approximation with neural networks, the sequence of value function approximations $V_{\theta_n}$ produced by gradient descent is decidedly non-monotone. Yet we still need to guarantee that $\mathbb{E}[V_{\theta_n}] \to \mathbb{E}[V^*]$ as $n \to \infty$. How can we justify this interchange of limit and expectation when monotonicity is absent?

The answer lies in the **Dominated Convergence Theorem** (DCT), the crown jewel of Lebesgue integration theory. DCT states that if a sequence of functions $f_n \to f$ pointwise and is **dominated** by an integrable function $g$ (meaning $|f_n| \leq g$ for all $n$), then $\int f_n \to \int f$. The hypothesis of domination replaces monotonicity, vastly expanding the theorem's applicability. Nearly every convergence argument in RL theory—from proving policy improvement to establishing convergence of stochastic approximation algorithms—rests on DCT or its probability-theoretic cousin, the Dominated Convergence Theorem for expectations.

But DCT does not appear from thin air. It is built upon a more primitive result, **Fatou's Lemma**, which handles *lim inf* of integrals. Fatou's Lemma is to DCT what MCT is to the Lebesgue integral: the foundational stone upon which the edifice is constructed. This section develops the convergence hierarchy in full: from MCT to Fatou to DCT, establishing the complete machinery for limit interchange that will be invoked hundreds of times in the chapters to come.

**Learning Objectives:**
* State and prove Fatou's Lemma, understanding its asymmetric nature (lim inf, not lim)
* Master the proof of DCT via Fatou's Lemma applied in both directions
* Identify where domination is essential through counterexamples
* Recognize DCT as the foundation for convergence proofs in RL algorithms

---

### **I. Core Theory: Fatou's Lemma**

We begin with a result that, while less celebrated than DCT, is logically prior and equally fundamental.

**Theorem 1.7 (Fatou's Lemma).** Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^{\infty}$ be a sequence of non-negative measurable functions $f_n: X \to [0, \infty]$. Then:
$$
\int \liminf_{n \to \infty} f_n \, d\mu \leq \liminf_{n \to \infty} \int f_n \, d\mu \tag{1.4}
$$

**Remark 1.7 (The Asymmetry of Fatou).** Observe that Fatou's Lemma is a one-sided inequality. It asserts that "integration pulls down lim inf," but it makes no claim about lim sup. Indeed, the reverse inequality generally fails. This asymmetry is not a defect—it reflects a deep fact: integration is a *continuous* operation from below (by MCT), but not necessarily from above. Fatou's Lemma captures precisely what survives when we relax monotonicity to mere non-negativity.

**Remark 1.8 (Why "lim inf"?).** Recall from analysis that for any sequence of real numbers $\{a_n\}$:
$$
\liminf_{n \to \infty} a_n = \lim_{n \to \infty} \left(\inf_{k \geq n} a_k\right) = \sup_{n \geq 1} \inf_{k \geq n} a_k
$$
The sequence $\{\inf_{k \geq n} a_k\}$ is *increasing* in $n$ (as we throw away fewer terms, the infimum can only increase). Thus $\liminf$ is always the limit of an increasing sequence, even when the original sequence $\{a_n\}$ does not converge. This monotonicity is what allows us to apply MCT in the proof.

*Proof of Theorem 1.7.*

**Step 1: Define an increasing sequence.**
For each $n \in \mathbb{N}$, define:
$$
g_n(x) = \inf_{k \geq n} f_k(x)
$$
By the definition of infimum over a tail of the sequence, we have:
$$
g_1(x) \leq g_2(x) \leq g_3(x) \leq \cdots
$$
That is, $\{g_n\}$ is an increasing sequence of functions. Moreover, each $g_n$ is measurable (as the infimum of a countable collection of measurable functions; see §1.1, Proposition 1.2).

**Step 2: Identify the limit of $\{g_n\}$.**
By the definition of $\liminf$:
$$
\liminf_{n \to \infty} f_n(x) = \lim_{n \to \infty} g_n(x)
$$
This holds pointwise for each $x \in X$.

**Step 3: Apply MCT to the increasing sequence $\{g_n\}$.**
Since $g_n \uparrow \liminf_{n \to \infty} f_n$ and each $g_n \geq 0$ is measurable, the Monotone Convergence Theorem (Theorem 1.6) yields:
$$
\int \liminf_{n \to \infty} f_n \, d\mu = \int \lim_{n \to \infty} g_n \, d\mu = \lim_{n \to \infty} \int g_n \, d\mu
$$

**Step 4: Bound the integrals of $g_n$.**
For each $n$, we have $g_n(x) = \inf_{k \geq n} f_k(x) \leq f_k(x)$ for all $k \geq n$. Therefore:
$$
\int g_n \, d\mu \leq \int f_k \, d\mu \quad \text{for all } k \geq n
$$
Taking the infimum over all $k \geq n$:
$$
\int g_n \, d\mu \leq \inf_{k \geq n} \int f_k \, d\mu
$$

**Step 5: Take the limit as $n \to \infty$.**
From Step 3, we have:
$$
\int \liminf_{n \to \infty} f_n \, d\mu = \lim_{n \to \infty} \int g_n \, d\mu
$$
From Step 4:
$$
\lim_{n \to \infty} \int g_n \, d\mu \leq \lim_{n \to \infty} \left(\inf_{k \geq n} \int f_k \, d\mu\right) = \liminf_{n \to \infty} \int f_n \, d\mu
$$
Combining these, we obtain:
$$
\int \liminf_{n \to \infty} f_n \, d\mu \leq \liminf_{n \to \infty} \int f_n \, d\mu
$$
as claimed. □

**Remark 1.9 (The Mechanism: MCT in Disguise).** The proof of Fatou is strikingly simple—it is merely MCT applied to the auxiliary sequence $g_n = \inf_{k \geq n} f_k$. This is a common pattern in analysis: to handle a general sequence, we construct from it a monotone sequence (here, by taking running infima), apply the monotone theorem, and then estimate. Fatou's Lemma is MCT for non-monotone sequences, at the cost of replacing $\lim$ with $\liminf$.

---

### **II. The Dominated Convergence Theorem**

We now arrive at the central result of Lebesgue integration theory, the theorem that makes the Lebesgue integral indispensable in modern analysis and probability.

**Theorem 1.8 (Dominated Convergence Theorem, DCT).** Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^{\infty}$ be a sequence of measurable functions $f_n: X \to \mathbb{R}$ such that:
1. **Pointwise convergence:** $f_n(x) \to f(x)$ for $\mu$-almost every $x \in X$, where $f: X \to \mathbb{R}$ is measurable.
2. **Domination:** There exists an integrable function $g: X \to [0, \infty)$ with $\int g \, d\mu < \infty$ such that:
   $$
   |f_n(x)| \leq g(x) \quad \text{for all } n \in \mathbb{N} \text{ and } \mu\text{-almost every } x \in X
   $$

Then $f$ is integrable, and:
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu = \int \lim_{n \to \infty} f_n \, d\mu \tag{1.5}
$$

**Remark 1.10 (Why "Dominated"?).** The name derives from the hypothesis that $|f_n|$ is bounded above by an integrable function $g$. This dominating function $g$ prevents the mass of $f_n$ from "escaping to infinity." Without such control, the integrals $\int f_n$ could diverge even when $f_n \to f$ pointwise. The dominating function is the price we pay for generality—it replaces monotonicity with boundedness.

**Remark 1.11 (Sharpness of Hypotheses).** Both hypotheses are necessary:
- **Pointwise convergence alone is insufficient.** Even if $f_n \to f$ uniformly on a set of infinite measure, the integrals may diverge. Example: Let $f_n = \frac{1}{n} \mathbf{1}_{[0, n]}$ on $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. Then $f_n \to 0$ uniformly, but $\int f_n = 1$ for all $n$, so $\int f_n \not\to 0 = \int f$.
- **Domination alone is insufficient.** We also need pointwise convergence. Example: Let $f_n = \mathbf{1}_{[n, n+1]}$ on $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. Then $|f_n| \leq \mathbf{1}_{\mathbb{R}}$ (dominated by the constant function 1, which is not integrable on $\mathbb{R}$—so this example is imperfect). Better example: On $([0,1], \mathcal{B}([0,1]), \lambda)$, let $f_n = \mathbf{1}_{[0, 1/n]}$. Then $f_n \to \mathbf{1}_{\{0\}}$ in measure but $\int f_n = 1/n \to 0 \neq 0 = \int \mathbf{1}_{\{0\}}$. (This example shows failure when domination holds but pointwise convergence fails.)

We will see precise counterexamples in the exercises.

*Proof of Theorem 1.8.*

The proof is a beautiful application of Fatou's Lemma applied in both directions, using the dominating function to convert the general sequence $\{f_n\}$ into non-negative sequences to which Fatou applies.

**Step 1: Apply Fatou to $g - f_n$.**
Define $h_n = g - f_n$. By hypothesis, $f_n \leq |f_n| \leq g$, so $h_n = g - f_n \geq 0$ for all $n$. Each $h_n$ is measurable and non-negative. By pointwise convergence, $f_n(x) \to f(x)$ almost everywhere, so:
$$
h_n(x) = g(x) - f_n(x) \to g(x) - f(x) \quad \text{a.e.}
$$
Thus:
$$
\liminf_{n \to \infty} h_n = g - f \quad \text{a.e.}
$$
Applying Fatou's Lemma (Theorem 1.7):
$$
\int (g - f) \, d\mu = \int \liminf_{n \to \infty} h_n \, d\mu \leq \liminf_{n \to \infty} \int h_n \, d\mu = \liminf_{n \to \infty} \int (g - f_n) \, d\mu
$$
Since $g$ is integrable, we can write:
$$
\int g \, d\mu - \int f \, d\mu \leq \int g \, d\mu - \limsup_{n \to \infty} \int f_n \, d\mu
$$
Subtracting $\int g \, d\mu$ from both sides (permissible since $\int g < \infty$):
$$
-\int f \, d\mu \leq -\limsup_{n \to \infty} \int f_n \, d\mu
$$
Multiplying by $-1$:
$$
\int f \, d\mu \geq \limsup_{n \to \infty} \int f_n \, d\mu \tag{1.6}
$$

**Step 2: Apply Fatou to $g + f_n$.**
Now define $k_n = g + f_n$. By hypothesis, $-f_n \leq |f_n| \leq g$, so $k_n = g + f_n \geq 0$. By pointwise convergence:
$$
k_n(x) \to g(x) + f(x) \quad \text{a.e.}
$$
Applying Fatou's Lemma:
$$
\int (g + f) \, d\mu \leq \liminf_{n \to \infty} \int (g + f_n) \, d\mu
$$
Thus:
$$
\int g \, d\mu + \int f \, d\mu \leq \int g \, d\mu + \liminf_{n \to \infty} \int f_n \, d\mu
$$
Subtracting $\int g \, d\mu$:
$$
\int f \, d\mu \leq \liminf_{n \to \infty} \int f_n \, d\mu \tag{1.7}
$$

**Step 3: Combine the inequalities.**
From (1.6) and (1.7), we have:
$$
\limsup_{n \to \infty} \int f_n \, d\mu \leq \int f \, d\mu \leq \liminf_{n \to \infty} \int f_n \, d\mu
$$
But for any sequence of real numbers $\{a_n\}$, we always have $\liminf a_n \leq \limsup a_n$. Therefore, the inequalities above can hold only if:
$$
\limsup_{n \to \infty} \int f_n \, d\mu = \liminf_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu
$$
which implies that $\lim_{n \to \infty} \int f_n \, d\mu$ exists and equals $\int f \, d\mu$. □

**Remark 1.12 (The Proof Strategy: Fatou as Pliers).** The proof is elegant: we "squeeze" $\int f$ between $\limsup \int f_n$ and $\liminf \int f_n$ by applying Fatou's Lemma twice—once to $g - f_n$ and once to $g + f_n$. The dominating function $g$ serves as the "fulcrum" for this operation, converting the sequence $\{f_n\}$, which may take both positive and negative values, into non-negative sequences $g \pm f_n$ to which Fatou applies. This is a standard trick in real analysis: to handle signed functions, add a non-negative function large enough to make everything positive, apply the non-negative result, then subtract.

**Remark 1.13 (Forward Connection: DCT in Probability and RL).** In probability theory, where the measure $\mu$ is a probability measure $\mathbb{P}$, DCT takes the form:
$$
\lim_{n \to \infty} \mathbb{E}[X_n] = \mathbb{E}\left[\lim_{n \to \infty} X_n\right]
$$
provided $X_n \to X$ almost surely and $|X_n| \leq Y$ for some integrable random variable $Y$. This is invoked constantly:
- **Policy evaluation:** If value functions $V_n \to V^*$ and are uniformly bounded ($|V_n| \leq V_{\max}$), then $\mathbb{E}_{\mu}[V_n] \to \mathbb{E}_{\mu}[V^*]$.
- **Temporal difference learning:** Convergence of TD(0) relies on DCT applied to the sequence of TD errors.
- **Policy gradient methods:** REINFORCE and actor-critic algorithms require DCT to justify $\nabla_\theta \mathbb{E}[G_t] = \mathbb{E}[\nabla_\theta \log \pi_\theta \cdot G_t]$.

Nearly every convergence proof in RL theory appeals to DCT, either explicitly or implicitly. This theorem is the reason we can trust that iterative algorithms, which produce sequences of value functions or policies, will converge in expectation.

---

### **III. Counterexamples: The Necessity of Hypotheses**

To appreciate DCT fully, we must see where it fails. The following examples illustrate the necessity of each hypothesis.

**Example 1.3 (Failure of Pointwise Convergence Without Domination).**
Let $(X, \mathcal{F}, \mu) = (\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ be the real line with Lebesgue measure. Define:
$$
f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x)
$$
Then:
- **Pointwise convergence:** For any $x \in \mathbb{R}$, $f_n(x) = \frac{1}{n} \to 0 = f(x)$.
- **Integrals:** $\int f_n \, d\lambda = \frac{1}{n} \cdot n = 1$ for all $n$, so $\int f_n \not\to 0 = \int f$.
- **Why DCT fails:** There is no integrable dominating function. If $g$ dominates all $f_n$, then $g(x) \geq \frac{1}{n}$ for all $x \in [0, n]$ and all $n$. Taking $n \to \infty$, we would need $g(x) > 0$ for all $x \geq 0$, but then $\int_{[0, \infty)} g \, d\lambda = \infty$.

**Example 1.4 (Failure Without Pointwise Convergence: The Sliding Hump).**
On $([0, 1], \mathcal{B}([0,1]), \lambda)$, define:
$$
f_n = \mathbf{1}_{[0, 1/n]}
$$
Then:
- **Pointwise behavior:** For $x > 0$, eventually $x > 1/n$ so $f_n(x) = 0$. For $x = 0$, $f_n(0) = 1$ always. Thus $f_n \to \mathbf{1}_{\{0\}}$ pointwise.
- **Integrals:** $\int f_n = 1/n \to 0$, but $\int \mathbf{1}_{\{0\}} = 0$. So the conclusion $\int f_n \to \int f$ does hold.
- This is not a counterexample; it actually confirms DCT (with dominating function $g = 1$).

A better example for failure without pointwise convergence:

**Example 1.5 (The Typewriter Sequence).**
On $([0, 1], \mathcal{B}([0,1]), \lambda)$, enumerate the dyadic intervals $I_n$ of length $1/2^k$ for $k = 0, 1, 2, \ldots$ in some order. Define $f_n = \mathbf{1}_{I_n}$. Then:
- **Domination:** $|f_n| \leq 1$ for all $n$, so domination holds.
- **Pointwise convergence fails:** For any $x \in [0, 1]$, the sequence $f_n(x)$ oscillates between 0 and 1 infinitely often (as $x$ is contained in infinitely many dyadic intervals and excluded from infinitely many). Thus $f_n$ does not converge pointwise anywhere.
- **Integrals:** $\int f_n = \text{length}(I_n) \to 0$ as $n \to \infty$ (since $I_n$ are finer and finer intervals).
- **Failure of DCT:** The sequence $\{f_n\}$ has no pointwise limit, so the conclusion $\int f_n \to \int f$ is meaningless—there is no $f = \lim f_n$.

---

### **IV. Application Bridge to Reinforcement Learning**

**Connection 1: Policy Evaluation and the Bellman Operator**

In policy evaluation, we seek the value function $V^\pi$ satisfying the Bellman equation:
$$
V^\pi(s) = \mathbb{E}^\pi\left[R_t + \gamma V^\pi(S_{t+1}) \mid S_t = s\right]
$$
Iterative policy evaluation produces a sequence $V_0, V_1, V_2, \ldots$ via:
$$
V_{n+1}(s) = \mathbb{E}^\pi\left[R_t + \gamma V_n(S_{t+1}) \mid S_t = s\right]
$$
If the reward is bounded ($|R_t| \leq R_{\max}$) and the discount factor satisfies $\gamma < 1$, then one can show $|V_n(s)| \leq V_{\max} := R_{\max}/(1-\gamma)$ for all $n$ and $s$. Moreover, under the contraction property of the Bellman operator (Week 18, Banach Fixed Point Theorem), $V_n \to V^\pi$ pointwise.

To prove that the expected value converges, i.e., $\mathbb{E}_\mu[V_n] \to \mathbb{E}_\mu[V^\pi]$ for some initial state distribution $\mu$, we invoke DCT:
- Pointwise convergence: $V_n(s) \to V^\pi(s)$ for all $s$.
- Domination: $|V_n(s)| \leq V_{\max}$ for all $n$ and $s$.
- Integrable dominating function: $g(s) = V_{\max}$ is constant, hence integrable on any probability space.

Therefore, by DCT:
$$
\lim_{n \to \infty} \mathbb{E}_\mu[V_n] = \mathbb{E}_\mu\left[\lim_{n \to \infty} V_n\right] = \mathbb{E}_\mu[V^\pi]
$$

**Connection 2: Temporal Difference Learning**

In TD(0), the value function update is:
$$
V_{t+1}(S_t) = V_t(S_t) + \alpha_t \left[R_t + \gamma V_t(S_{t+1}) - V_t(S_t)\right]
$$
The sequence $\{V_t\}$ is a stochastic approximation. Under appropriate conditions (Robbins-Monro step sizes $\sum \alpha_t = \infty$, $\sum \alpha_t^2 < \infty$; boundedness of rewards and states), one can prove $V_t \to V^\pi$ almost surely.

To conclude that $\mathbb{E}[V_t(s)] \to V^\pi(s)$, we need DCT. The dominating function is again $g(s) = V_{\max}$, derived from reward boundedness. The pointwise convergence $V_t(s) \to V^\pi(s)$ follows from stochastic approximation theory (Week 34-36).

**Connection 3: Policy Gradient Methods**

The REINFORCE algorithm computes the policy gradient:
$$
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}\left[\nabla_\theta \log \pi_\theta(\tau) \cdot G(\tau)\right]
$$
where $\tau$ is a trajectory and $G(\tau)$ is the return. To justify interchanging $\nabla_\theta$ and $\mathbb{E}$, we use a variant of DCT (technically, Leibniz integral rule for differentiation under the integral sign, which is proven via DCT).

The key is bounding $|\nabla_\theta \log \pi_\theta(\tau)|$ uniformly in $\theta$ near the current parameter value. If this gradient is dominated by an integrable function (typically ensured by Lipschitz continuity of $\log \pi_\theta$ in $\theta$), then DCT allows:
$$
\nabla_\theta \mathbb{E}_{\tau \sim \pi_\theta}[G(\tau)] = \mathbb{E}_{\tau \sim \pi_\theta}\left[\nabla_\theta \log \pi_\theta(\tau) \cdot G(\tau)\right]
$$

Without DCT, we cannot rigorously justify the policy gradient estimator.

**Summary:** DCT is the unsung hero of reinforcement learning theory. It appears in every convergence proof, every interchange of limit and expectation, every gradient computation. When we write $\lim \mathbb{E} = \mathbb{E} \lim$ in an RL paper, we are implicitly invoking Theorem 1.8. The dominating function corresponds to boundedness assumptions on rewards, value functions, or policy gradients—conditions that are standard in RL theory precisely because DCT requires them.

---

### **V. Reflection and Forward Glances**

We have now completed the convergence hierarchy:
- **MCT (Theorem 1.6):** Handles monotone sequences. Requires $f_n \uparrow f$.
- **Fatou's Lemma (Theorem 1.7):** Handles non-negative sequences. Requires $f_n \geq 0$, gives lim inf inequality.
- **DCT (Theorem 1.8):** Handles general sequences. Requires domination $|f_n| \leq g$, gives full limit.

This progression—from the restrictive but powerful MCT, through the one-sided Fatou, to the general DCT—mirrors the historical development of integration theory. Each theorem is proved using the previous one as a tool.

**Open Question for Day 4:** In the proof of the Carathéodory extension theorem (tomorrow's extended proof), we will construct Lebesgue measure on $\mathbb{R}^n$ from outer measure. Where in that construction do we use countable additivity? How does the σ-algebra structure ensure that Lebesgue measure is well-defined?

**Looking Ahead:**
- **Week 2, Day 1:** We will apply DCT to prove that $L^1$ convergence implies almost-everywhere convergence of a subsequence, a result essential for stochastic approximation (Week 34).
- **Week 6, Day 3:** Conditional expectation is defined as an orthogonal projection in $L^2$. DCT will be used to show that $\mathbb{E}[X | \mathcal{G}]$ is well-defined when $X$ is dominated.
- **Week 36:** The ODE method for stochastic approximation relies on DCT to justify that the discrete-time trajectory $\theta_n$ tracks the continuous ODE $\dot{\theta} = h(\theta)$.

DCT is not merely a theorem—it is a *method*, a way of thinking about limits and integrals. Mastering it now will pay compounding dividends throughout the 48-week journey.

---

**End of Day 3**
