[[Day_3_exercises_revised_pedagogy]]

### Agenda:

##### 📘 Day 3 — Week 2: Fubini's Theorem and Counterexamples

**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (40 min) — Reading**

**Topic:** _Fubini's theorem: extending Tonelli to integrable functions, and understanding failure modes_

- Read from **Folland §2.4** (Fubini's theorem) or **Durrett §1.8** (Fubini-Tonelli)
- Focus on:
    - **Fubini's theorem statement**: For $f \in L^1(\mu \times \nu)$, iterated integrals equal the double integral
    - **Key difference from Tonelli**: Integrability hypothesis $\int |f| < \infty$ is essential
    - **Positive and negative parts**: $f = f^+ - f^-$ where both $f^+, f^- \in L^1$
    - **Counterexamples**: When can Fubini fail?
      1. Without σ-finiteness (counting measure on uncountable sets)
      2. Without integrability (mixed-sign functions where cancellation depends on order)
- _Key takeaway:_ Fubini is the full generalization—it handles signed functions by controlling total variation via integrability. Tonelli (non-negative) was the warm-up; Fubini is the workhorse for RL where value functions and importance sampling ratios can be negative.

---

#### **⏱️ Segment 2 (40 min) — Proof/Exercise**

**Primary Task:**
1. **Prove Fubini's theorem** by reduction to Tonelli (apply Tonelli to $f^+$ and $f^-$ separately)
2. **Construct two counterexamples**:
   - **Counterexample 1 (σ-finiteness)**: Show product measure is not unique on $\mathbb{R} \times \mathbb{R}$ when using counting measure on uncountable set
   - **Counterexample 2 (integrability)**: Construct $f: \mathbb{N} \times \mathbb{N} \to \mathbb{R}$ where $\sum_i \sum_j f(i,j) \neq \sum_j \sum_i f(i,j)$ due to lack of absolute convergence

**Guidance:**
- For Fubini proof: Use $f = f^+ - f^-$, apply Tonelli to each part, subtract
- For counterexample 1: Consider $\mathbb{R}$ with counting measure—what goes wrong?
- For counterexample 2: Use alternating series that converges conditionally but not absolutely

---

#### **⏱️ Segment 3 (10 min) — Reflection**

**Reflection Questions:**
1. Why does integrability ($\int |f| < \infty$) prevent the pathology in Counterexample 2?
2. In off-policy RL, importance sampling ratios $\rho(s,a) = \pi(a|s)/\mu(a|s)$ (assuming $\text{supp}(\pi(\cdot|s)) \subseteq \text{supp}(\mu(\cdot|s))$ for all $s$) can be unbounded. When does Fubini apply to $\mathbb{E}_\mu[\rho \cdot R]$? What goes wrong if $\mathbb{E}[|\rho|] = \infty$?
3. How does Fubini enable us to compute $\mathbb{E}_{s,a}[Q^\pi(s,a) - V^\pi(s)]$ (the advantage function) via iterated expectations, even though $Q - V$ can be negative?

**Preview for Day 4 (Thursday):** Tomorrow we introduce **$L^p$ spaces** as function spaces equipped with the $p$-norm $\|f\|_p = (\int |f|^p)^{1/p}$. We prove **Hölder's inequality** (the generalization of Cauchy-Schwarz) and **Minkowski's inequality** (triangle inequality for $\|\cdot\|_p$), establishing that $L^p$ is a normed vector space. This framework will be essential for functional analysis (Weeks 11-16) and understanding where Bellman operators act.

---

#### **💡 Conceptual bridge to RL**

- **Fubini in policy evaluation**: Value functions $V^\pi(s)$ can be negative (consider cost minimization). Fubini ensures $\mathbb{E}_{a \sim \pi}[\mathbb{E}_{s' \sim P}[R(s,a,s') + \gamma V^\pi(s')]]$ is well-defined when $R + \gamma V^\pi \in L^1$.
- **Importance sampling ratios**: In off-policy learning, we compute $\mathbb{E}_{\mu}[\rho(s,a) Q^\pi(s,a)]$ where $\rho = \pi/\mu$ (assuming $\text{supp}(\pi(\cdot|s)) \subseteq \text{supp}(\mu(\cdot|s))$ for all $s$, ensuring the ratio is well-defined). Fubini applies only when $\mathbb{E}_\mu[|\rho \cdot Q|] < \infty$—if $\rho$ has heavy tails, this fails.
- **Advantage functions**: $A^\pi(s,a) = Q^\pi(s,a) - V^\pi(s)$ is signed. Computing $\mathbb{E}_{a \sim \pi}[A^\pi(s,a)] = 0$ (identity used in policy gradients) requires Fubini when $A$ can be negative.
- **Necessity of integrability**: Deep RL algorithms enforce bounded ratios through various mechanisms:
  - **PPO:** Clips importance ratios to $[1-\epsilon, 1+\epsilon]$ (explicit)
  - **IMPALA/V-trace:** Truncates per-timestep ratios $\bar{\rho}_t = \min(\rho_t, \rho_{\max})$
  - **AWR (Advantage-Weighted Regression):** Uses $\exp(\beta A(s,a))$ with bounded advantage (implicit)
  - **TRPO:** Constrains KL divergence $D_{KL}(\pi_{\text{old}} \| \pi_{\text{new}}) \leq \delta$, which bounds $\rho = \pi_{\text{new}}/\pi_{\text{old}}$ indirectly

  These mechanisms implicitly enforce $\mathbb{E}[|\rho \cdot A|] < \infty$, ensuring Fubini applies.

---

📅 Tomorrow (Day 4): **$L^p$ spaces**: definition, Hölder's inequality (complete proof), Minkowski's inequality (triangle inequality).

---

## **Chapter 2.3: Fubini's Theorem and the Necessity of Integrability**

### **Motivation: From Non-Negative to Signed Functions**

Yesterday we proved **Tonelli's theorem**: for non-negative measurable functions $f: X \times Y \to [0, \infty]$, iterated integrals equal the double integral, and the order of integration does not matter. The proof hinged on the **Monotone Convergence Theorem** (MCT), which applies automatically to increasing sequences of non-negative functions.

But what happens when $f$ can be **negative**? Consider the **advantage function** in reinforcement learning:
$$
A^\pi(s,a) = Q^\pi(s,a) - V^\pi(s)
$$

The advantage measures how much better action $a$ is compared to the average action under policy $\pi$. By definition, advantages can be positive or negative—they encode the relative merit of actions. When computing policy gradients (Week 37), we integrate advantage functions over state-action spaces:
$$
\nabla_\theta J(\pi_\theta) = \mathbb{E}_{s \sim d^\pi}\left[\mathbb{E}_{a \sim \pi_\theta(\cdot|s)}\left[\nabla_\theta \log \pi_\theta(a|s) \cdot A^\pi(s,a)\right]\right]
$$

This is an **iterated expectation of a signed function**. Tonelli does not apply (since $A$ can be negative). We need **Fubini's theorem**, which extends Tonelli to integrable functions—functions for which $\int |f| < \infty$.

**Bridge from Day 2:** Yesterday we saw that Tonelli requires only non-negativity, with no integrability hypothesis. Today, we confront the necessity of integrability when functions can change sign. The key insight: **cancellation** between positive and negative regions can depend on the order of integration, leading to pathological behavior unless we control the **total variation** $\int |f|$ to be finite.

**Why this matters for RL:** Value functions and importance sampling ratios in off-policy learning are typically signed. Ensuring integrability is essential for:
1. Policy gradient estimation (advantage functions)
2. Importance sampling corrections (off-policy policy evaluation)
3. Bellman error minimization (signed errors in function approximation)

When integrability fails, algorithms can diverge or produce biased estimates. In tabular/linear RL, this is a practical concern (e.g., Baird's counterexample). In deep RL, modern architectures mitigate this via:
- **Value clipping:** DQN, A3C clip $V(s) \in [V_{\min}, V_{\max}]$
- **Bounded activations:** Tanh or sigmoid output layers
- **Target networks:** Slowly-updated $\theta^-$ stabilizes Bellman targets

However, unbounded policies (Gaussian policies with unbounded support in continuous control) can still violate integrability when combined with off-policy sampling, requiring careful importance ratio clipping.

**What we'll accomplish today:**

**Learning Objectives:**
* State and prove Fubini's theorem via reduction to Tonelli
* Understand why integrability $\int |f| < \infty$ is necessary for signed functions
* Construct counterexamples showing failure without σ-finiteness or integrability
* Identify when Fubini applies in RL contexts: verify integrability conditions for importance sampling ratios, advantage functions, and Bellman errors
* Appreciate the distinction: Tonelli for non-negative, Fubini for integrable

---

### **I. Core Theory: Fubini's Theorem**

#### **A. Statement and Hypotheses**

**Theorem 2.4 (Fubini's Theorem).** Let $(X, \mathcal{F}_X, \mu)$ and $(Y, \mathcal{F}_Y, \nu)$ be σ-finite measure spaces. Let $f: X \times Y \to \mathbb{R}$ (or $\mathbb{C}$) be a measurable function such that:
$$
\int_{X \times Y} |f| \, d(\mu \times \nu) < \infty \tag{2.7}
$$

Then:

1. **Sections are integrable:** For $\mu$-almost every $x \in X$, the section $f(x, \cdot): Y \to \mathbb{R}$ is $\nu$-integrable. Similarly, for $\nu$-almost every $y \in Y$, the section $f(\cdot, y): X \to \mathbb{R}$ is $\mu$-integrable.

2. **Iterated integrals are integrable:** The functions
   $$
   \begin{align}
   F_1(x) &= \int_Y f(x,y) \, d\nu(y) \quad \text{(defined } \mu\text{-a.e.)} \tag{2.8} \\
   F_2(y) &= \int_X f(x,y) \, d\mu(x) \quad \text{(defined } \nu\text{-a.e.)} \tag{2.9}
   \end{align}
   $$
   are integrable: $F_1 \in L^1(\mu)$ and $F_2 \in L^1(\nu)$.

3. **Iterated integrals equal double integral:**
   $$
   \int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f \, d(\mu \times \nu) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y) \tag{2.10}
   $$

**Remark 2.16 (Key Difference from Tonelli).** Fubini requires the **integrability hypothesis** (2.7): $\int |f| < \infty$. This is strictly stronger than non-negativity. When $f \geq 0$, Tonelli applies automatically (no integrability check needed). When $f$ can be negative, we must verify (2.7) before applying Fubini.

**Remark 2.17 (Why "Almost Everywhere"?).** The sections $F_1(x)$ and $F_2(y)$ are defined only almost everywhere because the inner integrals may fail to exist for a measure-zero set of $x$ or $y$. This is a subtle point: even though $f$ is integrable on $X \times Y$, individual sections might not be integrable—but the set of "bad" sections has measure zero. This is formalized via **Fubini's lemma**, which we will justify in the proof by applying Tonelli to $|f|$. Specifically, since $|f| = f^+ + f^-$ is non-negative and $\int_{X \times Y} |f| \, d(\mu \times \nu) < \infty$, Tonelli (Theorem 2.3, Day 2) guarantees that for $\mu$-almost every $x$, the integral $\int_Y |f(x,y)| \, d\nu(y) < \infty$, meaning the section $f(x,\cdot)$ is $\nu$-integrable. The rigorous treatment of this measurability issue is **Fubini's lemma** ([@folland:real_analysis:1999, §2.4, Lemma 2.37]), which is essentially Tonelli applied to $|f|$. We incorporate this justification into the proof below.

**Remark 2.18 (Integrability in Complex-Valued Case).** For $f: X \times Y \to \mathbb{C}$, integrability means $\int |f| < \infty$ where $|f| = \sqrt{(\Re f)^2 + (\Im f)^2}$ is the modulus. Fubini applies by splitting $f = \Re f + i \Im f$ and applying the real-valued version to each part.

---

#### **B. Proof of Fubini's Theorem**

**Proof.**

The strategy is to **reduce to Tonelli** by decomposing $f$ into positive and negative parts.

**Step 1: Decomposition into positive and negative parts.**

Since $f: X \times Y \to \mathbb{R}$ is measurable, we can write:
$$
f = f^+ - f^- \quad \text{where} \quad f^+(x,y) = \max(f(x,y), 0), \quad f^-(x,y) = \max(-f(x,y), 0)
$$

Both $f^+$ and $f^-$ are **non-negative measurable functions** (as compositions of measurable $f$ with continuous functions).

**Observation:** We have $|f| = f^+ + f^-$, so the integrability hypothesis (2.7) gives:
$$
\int_{X \times Y} (f^+ + f^-) \, d(\mu \times \nu) = \int_{X \times Y} |f| \, d(\mu \times \nu) < \infty
$$

By additivity of the integral:
$$
\int_{X \times Y} f^+ \, d(\mu \times \nu) < \infty \quad \text{and} \quad \int_{X \times Y} f^- \, d(\mu \times \nu) < \infty \tag{2.11}
$$

**Why both integrals are finite:** Since $0 \leq f^+ \leq |f|$ and $0 \leq f^- \leq |f|$, we have by monotonicity of the integral (Week 1, Day 2, Proposition 1.7):
$$
\int_{X \times Y} f^+ \, d(\mu \times \nu) \leq \int_{X \times Y} |f| \, d(\mu \times \nu) < \infty
$$
and similarly for $f^-$. Thus both integrals are finite (not just their sum), allowing us to apply Tonelli separately to each. This ensures both $f^+$ and $f^-$ are **integrable** (not just non-negative, but with finite integral).

**Justification of almost-everywhere integrability (Fubini's Lemma):** By Tonelli applied to $f^+ \geq 0$, for $\mu$-almost every $x$, the section $f^+(x,\cdot)$ is $\nu$-integrable and $F_1^+(x) = \int_Y f^+(x,y) \, d\nu(y)$ is finite. Similarly, $F_1^-(x) = \int_Y f^-(x,y) \, d\nu(y)$ is finite for $\mu$-a.e. $x$. The set where either $F_1^+$ or $F_1^-$ is infinite has $\mu$-measure zero (since $\int_X F_1^+ \, d\mu < \infty$ and $\int_X F_1^- \, d\mu < \infty$ by (2.11)). For $x$ outside this null set, we define $F_1(x) = F_1^+(x) - F_1^-(x)$, which is well-defined and finite. This is the content of **Fubini's lemma** ([@folland:real_analysis:1999, §2.4, Lemma 2.37]).

**Step 2: Apply Tonelli to $f^+$ and $f^-$.**

Since $f^+ \geq 0$ and $f^- \geq 0$ are measurable, **Tonelli's theorem (Theorem 2.3)** applies to each:

For $f^+$:
$$
\int_X \left(\int_Y f^+(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f^+ \, d(\mu \times \nu) = \int_Y \left(\int_X f^+(x,y) \, d\mu(x)\right) d\nu(y)
$$

For $f^-$:
$$
\int_X \left(\int_Y f^-(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f^- \, d(\mu \times \nu) = \int_Y \left(\int_X f^-(x,y) \, d\mu(x)\right) d\nu(y)
$$

Both equalities hold because Tonelli guarantees them for non-negative functions.

**Step 3: Subtract to recover $f = f^+ - f^-$.**

Since both $f^+$ and $f^-$ have finite integrals (by (2.11)), we can subtract the integrals:

$$
\begin{align}
\int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) &= \int_X \left(\int_Y [f^+(x,y) - f^-(x,y)] \, d\nu(y)\right) d\mu(x) \\
&= \int_X \left[\int_Y f^+(x,y) \, d\nu(y) - \int_Y f^-(x,y) \, d\nu(y)\right] d\mu(x) \\
&\quad \text{(linearity of inner integral, valid since both } f^+, f^- \text{ integrable)} \\
&= \int_X \left(\int_Y f^+(x,y) \, d\nu(y)\right) d\mu(x) - \int_X \left(\int_Y f^-(x,y) \, d\nu(y)\right) d\mu(x) \\
&\quad \text{(linearity of outer integral)} \\
&= \int_{X \times Y} f^+ \, d(\mu \times \nu) - \int_{X \times Y} f^- \, d(\mu \times \nu) \\
&\quad \text{(by Tonelli for } f^+ \text{ and } f^-) \\
&= \int_{X \times Y} (f^+ - f^-) \, d(\mu \times \nu) \\
&= \int_{X \times Y} f \, d(\mu \times \nu)
\end{align}
$$

By symmetry, the same argument shows:
$$
\int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y) = \int_{X \times Y} f \, d(\mu \times \nu)
$$

Thus all three integrals in (2.10) are equal. □

**Pedagogical Remark:** This proof illustrates a **fundamental reduction strategy** in analysis: to handle signed functions, decompose into non-negative parts $f^+, f^-$, apply known results (here, Tonelli), then subtract. We will see this pattern repeatedly:
- **Week 3:** Radon-Nikodym theorem (decompose signed measures into $\nu^+, \nu^-$)
- **Week 4:** Conditional expectation (project onto positive and negative components)
- **Week 34:** TD learning convergence (separate positive/negative Bellman errors)

The key requirement: both parts must be **integrable** (finite integrals), not just their sum. Integrability ensures subtraction is well-defined.

**Remark 2.19 (Why Integrability Is Essential).** The proof critically relies on (2.11): both $f^+$ and $f^-$ have finite integrals, allowing us to subtract them. If we only knew that the iterated integrals of $f^+$ and $f^-$ exist separately (but possibly infinite), subtracting them could yield an indeterminate form $\infty - \infty$. The integrability hypothesis (2.7) ensures this does not occur.

**Remark 2.20 (Fubini's Lemma as a Corollary of Tonelli).** The claim that "sections are integrable almost everywhere" follows from **Tonelli applied to $|f|$**. Since $|f| = f^+ + f^-$ is non-negative and $\int_{X \times Y} |f| \, d(\mu \times \nu) < \infty$, Tonelli (Theorem 2.3, Day 2) guarantees that for $\mu$-almost every $x$, the integral $\int_Y |f(x,y)| \, d\nu(y) < \infty$, meaning the section $f(x,\cdot)$ is $\nu$-integrable. This justifies Step 1 of the proof. The rigorous treatment of this measurability issue is **Fubini's lemma** ([@folland:real_analysis:1999, §2.4, Lemma 2.37]), which is essentially Tonelli applied to $|f|$. We omit the detailed verification here to focus on the reduction argument, but the interested reader should consult the reference.

---

### **II. Counterexamples: When Fubini Fails**

Having established Fubini's theorem, we now explore its **necessity**—what goes wrong when hypotheses are violated? We construct two canonical counterexamples:

1. **Counterexample 1 (Failure without σ-finiteness):** Product measure is not unique when spaces are not σ-finite
2. **Counterexample 2 (Failure without integrability):** Iterated integrals depend on order when $\int |f| = \infty$

These counterexamples are not merely pathological curiosities—they reveal fundamental limitations and guide algorithm design in RL (e.g., ensuring bounded importance sampling ratios).

---

#### **A. Counterexample 1: Failure Without σ-Finiteness**

**Setting:** Let $X = Y = \mathbb{R}$ equipped with **counting measure** $\mu = \nu = \text{counting}$. Recall that counting measure assigns to each set $A$ the value:
$$
\mu(A) = \begin{cases}
|A| & \text{if } A \text{ is finite} \\
\infty & \text{if } A \text{ is infinite}
\end{cases}
$$

Counting measure on $\mathbb{R}$ is **not σ-finite** because $\mathbb{R}$ is uncountable and cannot be written as a countable union of finite-measure sets.

**Claim:** The product measure $\mu \times \nu$ on $\mathbb{R} \times \mathbb{R}$ is **not uniquely defined** under counting measure. Different extensions can yield different values on the same set.

**Construction:**

Consider the diagonal set:
$$
\Delta = \{(x,x) : x \in \mathbb{R}\} \subseteq \mathbb{R} \times \mathbb{R}
$$

We will show that iterated integrals of $\mathbf{1}_\Delta$ (the indicator function of the diagonal) depend on the order of integration:

**Iterated integral (outer $x$, inner $y$):**

For fixed $x \in \mathbb{R}$, the section is:
$$
\mathbf{1}_\Delta(x, y) = \begin{cases} 1 & \text{if } y = x \\ 0 & \text{otherwise} \end{cases}
$$

The inner integral over $Y = \mathbb{R}$ (with counting measure $\nu$) is:
$$
\int_\mathbb{R} \mathbf{1}_\Delta(x,y) \, d\nu(y) = \nu(\{x\}) = 1
$$

(because the set $\{y : \mathbf{1}_\Delta(x,y) = 1\} = \{x\}$ is a singleton).

The outer integral over $X = \mathbb{R}$ (with counting measure $\mu$) is:
$$
\int_\mathbb{R} \left(\int_\mathbb{R} \mathbf{1}_\Delta(x,y) \, d\nu(y)\right) d\mu(x) = \int_\mathbb{R} 1 \, d\mu(x) = \mu(\mathbb{R}) = \infty
$$

**Iterated integral (outer $y$, inner $x$):**

By symmetry of the diagonal, we get:
$$
\int_\mathbb{R} \left(\int_\mathbb{R} \mathbf{1}_\Delta(x,y) \, d\mu(x)\right) d\nu(y) = \infty
$$

**Attempt at product measure:**

So far, both iterated integrals equal $\infty$—no contradiction yet. But now consider the **complement of the diagonal**:
$$
\Delta^c = (\mathbb{R} \times \mathbb{R}) \setminus \Delta
$$

For the indicator $\mathbf{1}_{\Delta^c}$:

**Iterated integral (outer $x$, inner $y$):**

For fixed $x$, the section $\mathbf{1}_{\Delta^c}(x, \cdot)$ is 1 everywhere except at $y = x$. Thus:
$$
\int_\mathbb{R} \mathbf{1}_{\Delta^c}(x,y) \, d\nu(y) = \nu(\mathbb{R} \setminus \{x\}) = \infty
$$

(because $\mathbb{R} \setminus \{x\}$ is uncountable, hence has counting measure $\infty$).

So:
$$
\int_\mathbb{R} \left(\int_\mathbb{R} \mathbf{1}_{\Delta^c}(x,y) \, d\nu(y)\right) d\mu(x) = \int_\mathbb{R} \infty \, d\mu(x) = \infty
$$

By symmetry, the other order also gives $\infty$.

**The Pathology:**

Now, observe that $\Delta$ and $\Delta^c$ partition $\mathbb{R} \times \mathbb{R}$:
$$
(\mathbb{R} \times \mathbb{R}) = \Delta \sqcup \Delta^c
$$

If a product measure $\mu \times \nu$ existed uniquely, we would have:
$$
(\mu \times \nu)(\mathbb{R} \times \mathbb{R}) = (\mu \times \nu)(\Delta) + (\mu \times \nu)(\Delta^c)
$$

But both iterated integrals of $\mathbf{1}_\Delta$ and $\mathbf{1}_{\Delta^c}$ equal $\infty$, giving no meaningful constraint on the individual measures $(\mu \times \nu)(\Delta)$ and $(\mu \times \nu)(\Delta^c)$.

**Explicit failure:** The rectangle formula $(\mu \times \nu)(A \times B) = \mu(A)\nu(B)$ does not uniquely determine $(\mu \times \nu)(\Delta)$. For instance, we could define one extension with $(\mu \times \nu)_1(\Delta) = 0$ and another with $(\mu \times \nu)_2(\Delta) = \infty$, and both would satisfy the rectangle formula (since $\Delta$ is not a rectangle). The Carathéodory construction (Day 1, Theorem 2.2) requires σ-finiteness to ensure uniqueness (Day 1, Remark 2.6); without it, multiple extensions are possible. See [@folland:real_analysis:1999, §2.6] for the full pathology.

**Consequence:** Fubini's theorem statement does not even make sense without σ-finiteness, because there is no unique "double integral" $\int_{X \times Y} f \, d(\mu \times \nu)$ to compare iterated integrals against.

**Remark 2.21 (Relevance to RL).** This counterexample is unlikely to arise in RL practice, as state and action spaces are typically:
- Finite (tabular RL)
- Countable (discrete infinite-horizon MDPs)
- Euclidean with Lebesgue/Borel measures (continuous control)

All of these are σ-finite. However, certain POMDPs with continuous observation spaces and unusual measure structures might exhibit non-σ-finite behavior, requiring care in formulating trajectory distributions.

---

#### **B. Counterexample 2: Failure Without Integrability**

**Reader Challenge (Optional):** Before reading further, try to construct your own example of a function $f: \mathbb{N} \times \mathbb{N} \to \mathbb{R}$ where:
1. Both iterated sums $\sum_i \sum_j f$ and $\sum_j \sum_i f$ converge
2. But they converge to **different values**

*Hint:* Think about conditionally convergent series like $\sum (-1)^n/n$. Can you arrange +1's and -1's on a grid so that row-wise and column-wise summations differ?

**Solution:** We construct the following elegant example:

**Setting:** Let $X = Y = \mathbb{N}$ (positive integers) with **counting measure** $\mu = \nu = \text{counting}$. This is σ-finite (since $\mathbb{N} = \bigcup_{n=1}^\infty \{n\}$ with $\mu(\{n\}) = 1 < \infty$).

**Convention:** We use $\mathbb{N} = \{1, 2, 3, \ldots\}$ (positive integers) throughout this counterexample.

Consider the function $f: \mathbb{N} \times \mathbb{N} \to \mathbb{R}$ defined by:
$$
f(i,j) = \begin{cases}
1 & \text{if } j = i \\
-1 & \text{if } j = i + 1 \\
0 & \text{otherwise}
\end{cases} \tag{2.12}
$$

**Visualization:** The values of $f$ on the grid $\mathbb{N} \times \mathbb{N}$:

$$
\begin{array}{c|ccccc}
j \backslash i & 1 & 2 & 3 & 4 & \cdots \\
\hline
1 & 1 & 0 & 0 & 0 & \cdots \\
2 & -1 & 1 & 0 & 0 & \cdots \\
3 & 0 & -1 & 1 & 0 & \cdots \\
4 & 0 & 0 & -1 & 1 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{array}
$$

(The diagonal has 1's, the super-diagonal has -1's, all else is 0.)

**Iterated sum (outer $i$, inner $j$):**

For fixed $i$, sum over $j$:
$$
\sum_{j=1}^\infty f(i,j) = f(i,i) + f(i,i+1) + \sum_{\substack{j \neq i \\ j \neq i+1}} f(i,j) = 1 + (-1) + 0 = 0
$$

(Each row has exactly one 1 at column $i$ and one -1 at column $i+1$, summing to 0.)

Now sum over $i$:
$$
\sum_{i=1}^\infty \left(\sum_{j=1}^\infty f(i,j)\right) = \sum_{i=1}^\infty 0 = 0 \tag{2.13}
$$

**Iterated sum (outer $j$, inner $i$):**

For fixed $j$, sum over $i$:
$$
\sum_{i=1}^\infty f(i,j)
$$

Let's compute this for each $j$:
- **$j = 1$:** $f(1,1) = 1$, all other terms 0. Sum: $1$
- **$j = 2$:** $f(1,2) = -1$, $f(2,2) = 1$, all other terms 0. Sum: $0$
- **$j = 3$:** $f(2,3) = -1$, $f(3,3) = 1$, all other terms 0. Sum: $0$
- **$j = 4$:** $f(3,4) = -1$, $f(4,4) = 1$, all other terms 0. Sum: $0$
- **General $j \geq 2$:** $f(j-1, j) = -1$, $f(j,j) = 1$, sum: $0$

Thus:
$$
\sum_{i=1}^\infty f(i,j) = \begin{cases} 1 & \text{if } j = 1 \\ 0 & \text{if } j \geq 2 \end{cases}
$$

Now sum over $j$:
$$
\sum_{j=1}^\infty \left(\sum_{i=1}^\infty f(i,j)\right) = 1 + 0 + 0 + \cdots = 1 \tag{2.14}
$$

**Contradiction:** The two iterated sums differ:
$$
\sum_{i=1}^\infty \sum_{j=1}^\infty f(i,j) = 0 \neq 1 = \sum_{j=1}^\infty \sum_{i=1}^\infty f(i,j)
$$

**Diagnosis:** The function $f$ is **not integrable**. To see why, compute $\sum_{i,j} |f(i,j)|$:
$$
\sum_{i=1}^\infty \sum_{j=1}^\infty |f(i,j)| = \sum_{i=1}^\infty [|f(i,i)| + |f(i,i+1)|] = \sum_{i=1}^\infty [1 + 1] = \sum_{i=1}^\infty 2 = \infty
$$

Thus $f \notin L^1(\text{counting} \times \text{counting})$ because $\int |f| = \infty$.

**Interpretation:** This is analogous to **conditionally convergent series** in calculus. The series $\sum_{i,j} f(i,j)$ converges conditionally (in certain orders) but not absolutely. Rearranging the order of summation changes the value—the Riemann series theorem for double series.

Fubini requires **absolute convergence** (integrability $\int |f| < \infty$) to prevent this pathology.

**Remark 2.22 (Connection to RL: Importance Sampling).** In off-policy reinforcement learning, we estimate expectations under a target policy $\pi$ using data from a behavior policy $\mu$ via importance sampling. The importance sampling ratio $\rho(s,a) = \pi(a|s)/\mu(a|s)$ (assuming $\text{supp}(\pi(\cdot|s)) \subseteq \text{supp}(\mu(\cdot|s))$ for all $s$, ensuring the ratio is well-defined) can be unbounded if $\mu(a|s)$ is small:
$$
\mathbb{E}_\pi[f(s,a)] = \mathbb{E}_\mu\left[\frac{\pi(a|s)}{\mu(a|s)} f(s,a)\right]
$$

If $\mathbb{E}_\mu[|\rho \cdot f|] = \infty$, Fubini does not apply, and computing the expectation via iterated integrals (first over $a$, then over $s$, or vice versa) may yield different—or undefined—results.

In importance sampling with unbounded ratios, computing $\mathbb{E}_\mu[\rho \cdot R]$ via different sampling orders (first sample states, then actions vs. first sample actions, then states) can yield different estimates if $\mathbb{E}[|\rho \cdot R|] = \infty$. This is precisely the Fubini failure mode in RL practice.

**Practical RL mitigation:**
- **Clip importance ratios:** Truncate $\rho$ to $[\rho_{\min}, \rho_{\max}]$ (e.g., PPO clips ratios)
- **Weighted importance sampling:** Use self-normalized ratios $\rho/(\sum \rho)$ (reduces variance, introduces bias)
- **Ensure bounded $\pi/\mu$:** Design behavior policy $\mu$ with sufficient exploration (e.g., $\epsilon$-greedy ensures $\mu(a|s) \geq \epsilon/|\mathcal{A}|$)

These heuristics implicitly enforce integrability for Fubini to apply rigorously.

---

### **III. When Does Fubini Apply in Reinforcement Learning?**

**Synthesis:** Counterexamples 1 and 2 reveal the necessity of Fubini's hypotheses:
- **σ-finiteness** ensures product measure is uniquely defined (Counterexample 1)
- **Integrability** prevents order-dependent summation (Counterexample 2)

These are not merely technical conditions—they have **algorithmic consequences** in RL. When hypotheses fail, algorithms diverge (Baird's counterexample, Exercise 4) or produce biased estimates (clipped importance sampling, Exercise 3).

**From pathology to practice:** Having identified what can go wrong, we now ask: **When do RL algorithms satisfy Fubini's hypotheses?** The next section provides a systematic checklist for three core scenarios.

---

We examine three canonical RL computations involving signed integrands:

**Quick Reference: Integrability Checklist for RL**

| Scenario | Integrand | Sufficient Condition | Failure Mode | Practical Fix |
|----------|-----------|---------------------|--------------|---------------|
| **Advantage functions** | $A^\pi(s,a)$ | Bounded rewards | Unbounded $R$ → $\|A\| = \infty$ | Reward clipping |
| **Importance sampling** | $\rho(s,a) Q^\pi$ | $\mu(a\|s) \geq \epsilon$ | Deterministic $\pi$, stochastic $\mu$ | Clip $\rho$ (PPO, V-trace) |
| **Bellman error** | $\delta(s; \theta)$ | Bounded $V_\theta$ | Unbounded $\theta$ (Baird) | Target networks, GTD |

**Detailed analysis follows.** Use this table as a mental checklist when encountering iterated expectations in RL papers.

---

#### **A. Policy Evaluation with Advantage Functions**

**Setting:** Compute the expected advantage under a policy:
$$
\mathbb{E}_{s \sim d^\pi}\left[\mathbb{E}_{a \sim \pi(\cdot|s)}[A^\pi(s,a)]\right]
$$

where $A^\pi(s,a) = Q^\pi(s,a) - V^\pi(s)$ is signed.

**Fubini applicability:**

1. **Non-negativity?** No—$A^\pi$ can be positive or negative.
2. **Integrability?** We need:
   $$
   \mathbb{E}_{s,a}[|A^\pi(s,a)|] = \int_\mathcal{S} \int_\mathcal{A} |A^\pi(s,a)| \, \pi(da|s) \, d^\pi(s) < \infty
   $$

   **When is this satisfied?**
   - **Bounded rewards:** If $|R(s,a,s')| \leq R_{\max}$, then $|Q^\pi(s,a)| \leq R_{\max}/(1-\gamma)$ and $|V^\pi(s)| \leq R_{\max}/(1-\gamma)$, so $|A^\pi(s,a)| \leq 2R_{\max}/(1-\gamma) < \infty$.
   - **Bounded state-action space:** If $\mathcal{S}$ and $\mathcal{A}$ are finite, integrability is automatic (sum of finitely many terms).
   - **Sub-Gaussian tails:** If $\mathbb{P}(|A^\pi| > t)$ decays exponentially, integrability holds.

   **When does it fail?**
   - Unbounded rewards with no exponential decay (e.g., Gaussian noise with variance growing in state)
   - Continuous spaces with heavy-tailed value distributions (rare in practice)

**Conclusion:** In standard RL settings (bounded rewards, finite horizons, or discounting), Fubini applies to advantage functions.

**Identity used in policy gradients:**

The identity $\mathbb{E}_{a \sim \pi}[A^\pi(s,a)] = 0$ for each $s$ follows from the definition $V^\pi(s) = \mathbb{E}_{a \sim \pi}[Q^\pi(s,a)]$, which gives $\mathbb{E}_{a \sim \pi}[A^\pi(s,a)] = \mathbb{E}_{a \sim \pi}[Q^\pi(s,a) - V^\pi(s)] = V^\pi(s) - V^\pi(s) = 0$ for each $s$. Fubini is needed to justify that the **iterated expectation** in policy gradient estimation
$$
\nabla_\theta J(\pi_\theta) = \mathbb{E}_{s}[\mathbb{E}_{a}[\nabla \log \pi_\theta(a|s) \cdot A^\pi(s,a)]]
$$
is well-defined when $A$ can be negative—requiring $\mathbb{E}[|A|] < \infty$.

---

#### **B. Importance Sampling in Off-Policy Learning**

**Setting:** Estimate $\mathbb{E}_\pi[Q^\pi(s,a)]$ using samples from behavior policy $\mu$. The importance sampling ratio $\rho(s,a) = \pi(a|s)/\mu(a|s)$ (assuming $\text{supp}(\pi(\cdot|s)) \subseteq \text{supp}(\mu(\cdot|s))$ for all $s$, ensuring the ratio is well-defined):
$$
\mathbb{E}_\pi[Q^\pi(s,a)] = \mathbb{E}_\mu\left[\frac{\pi(a|s)}{\mu(a|s)} Q^\pi(s,a)\right]
$$

**Fubini applicability:**

1. **Integrability of $\rho \cdot Q$?** We need:
   $$
   \mathbb{E}_\mu\left[\left|\frac{\pi(a|s)}{\mu(a|s)} Q^\pi(s,a)\right|\right] < \infty
   $$

   **Sufficient conditions:**
   - **Bounded importance ratio:** $\pi(a|s)/\mu(a|s) \leq C$ for all $(s,a)$ (e.g., $\mu$ is $\epsilon$-greedy with $\epsilon > 0$)
   - **Bounded $Q$:** $|Q^\pi(s,a)| \leq Q_{\max}$ (follows from bounded rewards)

   **When does it fail?**
   - **Deterministic $\pi$ and stochastic $\mu$:** If $\pi$ is deterministic and $\mu$ has small probability on the greedy action, $\rho = \pi/\mu$ can be arbitrarily large
   - **Heavy-tailed behavior policy:** If $\mu(a|s)$ can be very small (e.g., Gaussian exploration with unbounded variance), $\rho$ is unbounded

**Practical failure mode in deep RL:**
- In off-policy actor-critic (e.g., V-trace, IMPALA), importance ratios $\prod_{t=0}^n \pi(a_t|s_t)/\mu(a_t|s_t)$ grow exponentially in trajectory length $n$
- If $\mathbb{E}[\prod \rho_t] = \infty$, Fubini fails, and off-policy correction is biased or divergent
- **Solution:** Truncate products (V-trace uses $\bar{\rho}_t = \min(\rho_t, \rho_{\max})$) or use per-step corrections

**V-trace algorithm:** IMPALA uses V-trace off-policy correction (Espeholt et al., 2018), which truncates importance ratios at each timestep:
$$\bar{\rho}_t = \min(\rho_t, \bar{\rho})$$
where $\bar{\rho} = 1$ is common. This per-timestep truncation prevents the product $\prod_{t=0}^n \rho_t$ from exploding, ensuring $\mathbb{E}[|\bar{\rho}_t A_t|] < \infty$.

**Reference:** Espeholt et al. (2018), 'IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures,' *ICML 2018*.

**Concrete Example (Illustrative):**

Consider a simple MDP with $\mathcal{S} = \{s_1, s_2\}$, $\mathcal{A} = \{a_1, a_2\}$. Suppose:
- **Target policy:** $\pi(a_1|s_1) = 0.9$, $\pi(a_2|s_1) = 0.1$
- **Behavior policy (ε-greedy):** $\mu(a_1|s_1) = 0.55$, $\mu(a_2|s_1) = 0.45$ (uniform exploration)
- **Behavior policy (near-greedy):** $\mu'(a_1|s_1) = 0.99$, $\mu'(a_2|s_1) = 0.01$ (minimal exploration)

**Importance ratios:**
- With ε-greedy $\mu$: $\rho(s_1,a_1) = 0.9/0.55 \approx 1.64$, $\rho(s_1,a_2) = 0.1/0.45 \approx 0.22$ (bounded)
- With near-greedy $\mu'$: $\rho(s_1,a_1) = 0.9/0.99 \approx 0.91$, $\rho(s_1,a_2) = 0.1/0.01 = 10$ (large!)

**Integrability check (assuming $|Q| \leq 1$):**
- With $\mu$: $\mathbb{E}_\mu[|\rho \cdot Q|] \leq \max(\rho) \cdot Q_{\max} \approx 1.64 \cdot 1 < \infty$ ✓
- With $\mu'$: $\mathbb{E}_{\mu'}[|\rho \cdot Q|] \leq 10 \cdot 1 = 10$ (still finite, but high variance)

**Lesson:** Even with bounded $\rho$, poor exploration ($\mu'$ assigns low probability to $a_2$) causes **high variance** in importance-weighted estimates. Fubini applies in both cases (integrability holds), but variance considerations motivate clipping even when integrability is satisfied.

---

#### **C. Bellman Error Minimization (Function Approximation)**

**Setting:** In temporal-difference learning with function approximation, we minimize the mean-squared Bellman error:
$$
\text{MSBE}(\theta) = \mathbb{E}_{s \sim d^\pi}\left[\left(V_\theta(s) - \mathbb{E}_{a,s'}[R(s,a,s') + \gamma V_\theta(s')]\right)^2\right]
$$

The Bellman error $\delta(s) = V_\theta(s) - \mathbb{E}[R + \gamma V_\theta(s')]$ is signed.

**Fubini applicability:**

1. **Integrability of $\delta^2$?** We need:
   $$
   \mathbb{E}_{s \sim d^\pi}[\delta(s)^2] < \infty
   $$

   **When is this satisfied?**
   - **Bounded value approximations:** If $V_\theta$ is parameterized (e.g., neural network with bounded activation at output), $|V_\theta(s)| \leq V_{\max}$
   - **Bounded rewards and transitions:** If $|R(s,a,s')| \leq R_{\max}$ and $\mathbb{E}[V_\theta(s')]$ is bounded, then $|\delta(s)| \leq 2V_{\max} + R_{\max}$, so $\delta^2 < \infty$

   **When does it fail?**
   - **Off-policy TD with linear function approximation:** Even with bounded features and rewards, $\theta_n$ can diverge to infinity (Baird's counterexample, 1995). The issue is that the semi-gradient update $\theta_{n+1} = \theta_n + \alpha_n [R + \gamma \theta^\top \phi(s') - \theta^\top \phi(s)] \phi(s)$ does not follow the true gradient of any objective function when the sampling distribution differs from $d^\pi$. As $\|\theta\| \to \infty$, the Bellman error $\delta$ grows unbounded, violating $\mathbb{E}[|\delta|] < \infty$.
   - **Unbounded function approximators:** If $V_\theta$ has no output bounds (e.g., deep networks without value clipping), divergence can occur even on-policy in pathological cases.

**Practical safeguards:**
- **Value clipping:** Constrain $V_\theta$ to $[V_{\min}, V_{\max}]$ (common in DQN, A3C)
- **Target networks:** Stabilize TD targets $R + \gamma V_{\theta^-}(s')$ using slowly-updated $\theta^-$
- **Gradient clipping:** Bound $\|\nabla_\theta \text{MSBE}\|$ to prevent explosive updates

These heuristics implicitly ensure Bellman errors remain integrable, allowing Fubini to apply when interchanging expectations.

---

### **IV. Mathematical Insight and Forward Connections**

**Mathematical Insight:**

Fubini's theorem reveals a fundamental principle: **iterated integration is well-defined for signed functions only when total variation is controlled**. The integrability hypothesis $\int |f| < \infty$ ensures that positive and negative contributions do not cancel in order-dependent ways.

Tonelli (non-negative functions) was the "easy case"—no cancellation, so MCT applies directly. Fubini (integrable signed functions) is the "full story"—we decompose $f = f^+ - f^-$, apply Tonelli to each part, and subtract. The key mechanism: **absolute convergence prevents rearrangement paradoxes**.

This mirrors a deep theme in analysis: absolute convergence (integrability) is the price of commutativity (order independence). We saw this in:
- Series: $\sum a_n$ converges absolutely iff every rearrangement converges to the same limit (Riemann series theorem)
- Double integrals: Fubini holds iff $\int |f| < \infty$ (today's result)
- Stochastic integration: Dominated convergence requires $\sup_n |X_n|$ integrable (Week 1, Day 3)

**RL Connection:**

Fubini is the mathematical guarantee that **iterated expectations in RL are order-independent**—provided integrability holds. This is essential for:
1. **Policy evaluation:** Computing $V^\pi(s) = \mathbb{E}_a[\mathbb{E}_{s'}[R + \gamma V^\pi]]$ via nested loops
2. **Importance sampling:** Estimating $\mathbb{E}_\pi[Q]$ from $\mathbb{E}_\mu[\rho Q]$ requires $\mathbb{E}[|\rho Q|] < \infty$
3. **Gradient estimation:** Policy gradient $\nabla J = \mathbb{E}_s[\mathbb{E}_a[\nabla \log \pi \cdot A]]$ requires $A$ integrable

When integrability fails, algorithms can:
- Produce order-dependent estimates (different results from different sampling orders)
- Diverge (unbounded importance weights cause variance explosion)
- Yield biased estimates (clipping ratios introduces bias)

Deep RL practitioners often treat these issues heuristically (clipping, normalization, value bounds). Fubini provides the rigorous foundation explaining *why* these heuristics work—they implicitly enforce integrability.

**Open Questions:**

1. **Relaxing Integrability:** Can we weaken $\int |f| < \infty$ to some weaker notion of "controlled growth"? In probability theory, **uniform integrability** (Week 4, Day 3) provides a subtler condition for the **Vitali convergence theorem** (a UI version of DCT). However, UI does **not** directly replace integrability in Fubini—the product structure introduces additional complexity.

   **RL Example:** Consider a sequence of policies $\{\pi_n\}$ converging to $\pi^*$. The importance ratios $\rho_n(s,a) = \pi_n(a|s)/\mu(a|s)$ (assuming $\text{supp}(\pi_n(\cdot|s)) \subseteq \text{supp}(\mu(\cdot|s))$ for all $s,n$) may have $\sup_n \mathbb{E}[|\rho_n|] = \infty$ (non-integrability), but if $\{\rho_n\}$ is uniformly integrable, convergence $\mathbb{E}_\mu[\rho_n Q] \to \mathbb{E}_{\pi^*}[Q]$ may still hold. This is relevant for policy gradient methods where $\pi_\theta$ changes continuously during training. See Metelli et al. (2018, AAAI) for truncated importance sampling with UI guarantees.

2. **Infinite-Dimensional Extensions:** In function space RL (where policies are infinite-dimensional objects), does Fubini extend to Banach-space-valued functions? This leads to **Bochner integration** (Week 11, optional topic).

3. **Non-σ-Finite RL Scenarios:** Are there RL problems naturally formulated on non-σ-finite spaces? Certain POMDPs with continuous observation spaces and counting-type measures might exhibit this—when does it arise, and how to handle it?

---

**Looking Ahead:**

- **Day 4 (Tomorrow):** We introduce **$L^p$ spaces**, the function space framework where integrability $\int |f|^p < \infty$ defines a norm $\|f\|_p$. We prove **Hölder's inequality** (the $L^p$ generalization of Cauchy-Schwarz) and **Minkowski's inequality** (triangle inequality for $\|\cdot\|_p$), establishing that $L^p$ is a normed vector space. This is the foundation for functional analysis (Weeks 11-16), where Bellman operators act on $L^\infty$ or $L^2$.

- **Week 3:** We continue $L^p$ theory with completeness (Riesz-Fischer theorem) and duality $(L^p)^* \cong L^q$. Then we prove the **Radon-Nikodym theorem**, formalizing "changing measures" via densities $d\mu/d\nu$—the rigorous foundation for importance sampling.

- **Week 4:** Probability spaces and **conditional expectation** as orthogonal projection in $L^2$. The tower property $\mathbb{E}[\mathbb{E}[X|\mathcal{G}]|\mathcal{H}] = \mathbb{E}[X|\mathcal{H}]$ is a Fubini-like result for conditional measures.

Fubini is the bridge from "measure theory for non-negative functions" (Tonelli, Day 2) to "integration theory for general signed functions" (today). Tomorrow, we organize integrable functions into normed spaces $L^p$, the geometric framework where all of functional analysis unfolds.

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_3_exercises_revised_pedagogy]]**

**Anchor Exercises Preview:**
1. **Prove Fubini's theorem** by reduction to Tonelli (as in Section I.B)
2. **Construct Counterexample 2** explicitly: define $f(i,j)$ as in (2.12), verify iterated sums differ, compute $\sum |f|$ to confirm non-integrability
3. **RL Application:** For off-policy policy evaluation with clipped importance ratios $\bar{\rho}_t = \min(\rho_t, \rho_{\max})$, show that $\mathbb{E}_\mu[|\bar{\rho} \cdot Q|] \leq \rho_{\max} Q_{\max}$, ensuring Fubini applies. Discuss bias introduced by clipping.

---

**Reflection Questions:**

1. **Integrability vs. Non-negativity:** Why does Tonelli require only $f \geq 0$, while Fubini requires $\int |f| < \infty$? What does integrability control that non-negativity does not?

   *Hint:* Consider the positive and negative parts $f^+ = \max(f, 0)$ and $f^- = \max(-f, 0)$. Tonelli applies to each separately, but subtracting them requires both integrals to be finite to avoid $\infty - \infty$.

2. **Importance Sampling in Deep RL:** In PPO (Proximal Policy Optimization), importance ratios are clipped to $[1-\epsilon, 1 + \epsilon]$ where $\epsilon \approx 0.2$. How does this ensure Fubini applies? What is the trade-off between ensuring integrability and introducing bias?

   *Hint:* Clipping ensures $|\rho| \leq 1 + \epsilon$, making $\mathbb{E}[|\rho \cdot A|] \leq (1+\epsilon) \mathbb{E}[|A|] < \infty$ (when advantages are bounded). But clipping introduces bias when the true ratio exceeds the clip threshold.

3. **Value Function Divergence:** In Baird's counterexample (1995), off-policy TD with linear function approximation causes $V_\theta$ to diverge to $\pm \infty$. How does this relate to the failure of Fubini? What integrability condition is violated?

   *Hint:* As $\|V_\theta\|$ grows unbounded, the Bellman error $\delta(s) = V_\theta(s) - \mathbb{E}[R + \gamma V_\theta(s')]$ also diverges, causing $\mathbb{E}[\delta^2] \to \infty$. Fubini fails because the Bellman target involves an iterated expectation over $(s, a, s')$, and $|R + \gamma V_\theta(s')| = \infty$ for some trajectories.

---

**Daily Study Note:**

**What I learned today:**
- Fubini's theorem extends Tonelli to signed functions by requiring integrability $\int |f| < \infty$
- Counterexamples show Fubini fails without σ-finiteness (non-unique product measure) or without integrability (order-dependent sums)
- In RL, integrability ensures importance sampling, advantage functions, and Bellman errors are well-defined
- Practical deep RL heuristics (clipping, value bounds, target networks) implicitly enforce integrability for Fubini to apply

**Connection to previous material:**
- Builds on Tonelli (Day 2): Fubini = Tonelli for $f^+$ and $f^-$, then subtract
- Uses MCT and DCT (Week 1, Days 2-3) implicitly in the proof of Fubini's lemma
- Connects to product measures (Day 1): σ-finiteness was needed for uniqueness; today we saw it's also needed for Fubini

**Looking forward:**
- Tomorrow: $L^p$ spaces organize integrable functions into normed vector spaces
- Week 3: Radon-Nikodym theorem formalizes importance sampling densities $d\pi/d\mu$
- Week 4: Conditional expectation as orthogonal projection (tower property is a Fubini-like result)

**Time spent:** 90 minutes (reading Folland §2.4, proving Fubini, constructing counterexamples)

---

**End of Day 3**
