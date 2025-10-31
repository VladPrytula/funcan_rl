### Agenda:

##### 📘 Day 5 — Week 2: Weekly Synthesis – Product Measures, Fubini, and $L^p$ Spaces

**Total time: 90 minutes (Friday synthesis session)**

---

#### **⏱️ Segment 1 (20 min) — Reading & Review**

**Topic:** _Synthesizing Week 2: From Product Measures to Function Spaces_

- Review key results from Monday-Thursday:
    - **Product measures** (Days 1-2): Construction of $\mu \times \nu$ via Carathéodory extension
    - **Fubini-Tonelli** (Days 2-3): When iterated integrals equal double integrals
    - **$L^p$ spaces** (Day 4): Hölder and Minkowski inequalities establish normed space structure
- Reflection: How do these tools enable RL theory?
    - Product measures → trajectory spaces in MDPs
    - Fubini → computing expectations over state-action pairs
    - $L^p$ norms → function space framework for Bellman operators

---

#### **⏱️ Segment 2 (30 min) — Proof Technique Review**

**Primary Task:**
1. **Synthesis Exercise:** Compare and contrast the proof strategies for Tonelli, Hölder, and Minkowski
   - What role does monotonicity play? (Tonelli via MCT)
   - What role does convexity play? (Young's inequality → Hölder)
   - How do we build norms from integrals? (Minkowski establishes triangle inequality)

2. **Conceptual Exercise:** Identify the key mechanism in each major theorem
   - Tonelli: MCT + product measure uniqueness
   - Hölder: Normalization + Young's inequality
   - Minkowski: Splitting $|f+g|^p$ and applying Hölder twice

---

#### **⏱️ Segment 3 (40 min) — Computational Synthesis**

**Coding Tasks:**
1. **Fubini Verification (15 min):**
   - Compute $\iint f(x,y) \, dx \, dy$ via both orders of integration
   - Test functions: (a) $f(x,y) = xy$ on $[0,1]^2$, (b) $f(x,y) = e^{-(x+y)}$ on $[0,\infty)^2$
   - Verify equality numerically (within tolerance)

2. **$L^p$ Unit Ball Visualization (20 min):**
   - Plot unit balls $\{(x,y) : \|(x,y)\|_p \leq 1\}$ in $\mathbb{R}^2$ for $p = 1, 2, \infty$
   - Observe: $p=1$ is diamond, $p=2$ is circle, $p=\infty$ is square
   - Reflection: As $p \to \infty$, the unit ball approaches a square (sup norm focuses on peak magnitude)

3. **RL Connection Exercise (5 min):**
   - Reflect: How does Fubini enable computing $\mathbb{E}_{s,a}[V^\pi(s')]$ in policy evaluation?
   - Write: Formalize the double integral $\int \int V^\pi(s') P(s'|s,a) \, ds' \, d\rho(s,a)$ where $\rho$ is the state-action visitation measure

---

#### **💡 Weekly Reflection: Week 2 in Context**

This is our first **Friday synthesis session**. We step back from the day-to-day theorem-proving to:
1. **Consolidate** the week's mathematical machinery
2. **Verify** theorems computationally
3. **Bridge** to RL applications explicitly

Week 2 established the **geometric structure of integration**: product measures provide the canvas, Fubini enables computation, and $L^p$ norms organize functions into analyzable spaces. Next week (Week 3), we prove these spaces are **complete** (Riesz-Fischer) and study their **duality** ($(L^p)^* \cong L^q$), culminating in the **Radon-Nikodym theorem**—the measure-theoretic foundation for importance sampling.

---

## **Chapter 2.5: Friday Synthesis – Computational Exploration and Weekly Reflection**

### **Motivation: From Theory to Intuition**

Over the past four days, we have constructed a formidable theoretical architecture:
- **Product measures** (Days 1-2) enable integration over multi-dimensional spaces
- **Fubini-Tonelli theorems** (Days 2-3) justify computing double integrals via iterated integrals
- **$L^p$ spaces** (Day 4) organize integrable functions into normed vector spaces with geometric structure

Today, we pause theorem-proving to **verify** these abstractions computationally and **reflect** on their necessity for reinforcement learning. This is the first of many **Friday synthesis sessions**—a weekly rhythm where we:
1. Consolidate the week's proof techniques
2. Numerically validate key theorems
3. Explicitly bridge mathematics to RL algorithms

**Why computation matters:** Abstract theorems like Fubini guarantee equality of iterated integrals *in principle*, but numerical experiments build **geometric intuition**. When we later study policy evaluation operators $T^\pi V(s) = \mathbb{E}_{a,s'}[r(s,a) + \gamma V(s')]$, the mechanics of "swapping expectation and summation" will feel natural—because we've seen Fubini work in practice.

**Why reflection matters:** In the intensity of rigorous proof-writing, we risk losing sight of the **ultimate goal**: using these tools to reason about RL algorithms. Friday reflections anchor abstract mathematics to concrete RL problems, ensuring every theorem earns its place in our journey.

**What we'll accomplish today:**

**Learning Objectives:**
* Synthesize proof strategies from Tonelli, Hölder, and Minkowski
* Verify Fubini's theorem numerically for test functions
* Visualize $L^p$ unit balls in $\mathbb{R}^2$ to understand norm geometry
* Formalize how Fubini enables computing $\mathbb{E}_{s,a}[V^\pi(s')]$ in MDPs
* Reflect on Week 2's role in the 48-week journey

**Time allocation (90 min Friday):**
- 20 min reading/review: Synthesize Week 2 material
- 30 min proof technique review: Compare proof strategies
- 40 min computational synthesis: Code verification and visualization

---

### **I. Week 2 in Retrospect: The Geometry of Integration**

#### **A. Product Measures: Constructing Multi-Dimensional Integration**

**Recall from Week 1 Day 1 (Section IV, "Synthesis: Toward MDPs"):** We stated that the value function
$$V^{\pi}(s) = \mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \,\bigg|\, s_0 = s\right]$$
is an expectation over the **trajectory space** of state-action sequences $(s_0, a_0, s_1, a_1, \ldots)$. To make this rigorous, we need a σ-algebra on this infinite-dimensional space. We promised to develop the mathematical machinery to construct it using the **Kolmogorov extension theorem**. We now deliver on that promise.

**Days 1-2 Achievement:** Given measure spaces $(X, \mathcal{F}, \mu)$ and $(Y, \mathcal{G}, \nu)$, we constructed the **product measure** $\mu \times \nu$ on $(X \times Y, \mathcal{F} \otimes \mathcal{G})$ via the Carathéodory extension theorem.

**Key Mechanism:** The product σ-algebra $\mathcal{F} \otimes \mathcal{G}$ is generated by measurable rectangles $A \times B$, and the product measure is uniquely determined by $(\mu \times \nu)(A \times B) = \mu(A) \nu(B)$.

**RL Connection:** In Markov Decision Processes, the **trajectory space** $\Omega = (\mathcal{S} \times \mathcal{A})^\infty$ is a countable product space, with the joint measure over state-action sequences determined by the policy $\pi$ and transition kernel $P$. Product measures formalize how individual transition probabilities $P(s'|s,a)$ compose to give probabilities over entire trajectories.

**Concrete Example (MDP Trajectory Measure):** Consider an MDP with state space $\mathcal{S}$, action space $\mathcal{A}$, policy $\pi$, and transition kernel $P$. A single-step state-action-state transition $(s_t, a_t, s_{t+1})$ has probability measure:
$$
d\rho_1(s_t, a_t, s_{t+1}) = \mu_0(s_t) \, \pi(a_t|s_t) \, P(s_{t+1}|s_t, a_t)
$$
where $\mu_0$ is the initial state distribution.

For a trajectory of length $T$, the joint measure over $(s_0, a_0, s_1, a_1, \ldots, s_T)$ involves **conditional products** (also called disintegrations):
$$
d\rho_T(s_0, a_0, \ldots, s_T) = \mu_0(s_0) \prod_{t=0}^{T-1} \pi(a_t|s_t) P(s_{t+1}|s_t, a_t)
$$

**Technical Note:** This is not a standard product measure $\mu \times \nu$ from Week 2, because each factor $P(s_{t+1}|s_t, a_t)$ depends on previous variables. The rigorous framework is **disintegration of measures**: given a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ and a sub-σ-algebra $\mathcal{G} \subseteq \mathcal{F}$, the conditional measure $\mathbb{P}(\cdot | \mathcal{G})$ is a family of probability measures indexed by $\mathcal{G}$-measurable outcomes. For MDPs, the disintegration formula above defines the trajectory measure uniquely given $\mu_0, \pi, P$. The formal development appears in Week 4 (conditional expectation) and Week 23 (MDP measure theory). For now, we note that the formula is correct and implementable, even though its mathematical justification requires tools beyond Week 2.

**Reference:** Kallenberg "Foundations of Modern Probability" (2002), Chapter 6 (Regular conditional probabilities and disintegration) [@kallenberg2002].

**Theorem 2.11 (Kolmogorov Extension Theorem - Statement).** {#THM-2.5.2}
Let $(X_n, \mathcal{F}_n)_{n=1}^{\infty}$ be a sequence of measurable spaces. Suppose for each finite $n \geq 1$, we have a probability measure $\mu_n$ on $\prod_{i=1}^n X_i$ (equipped with the product σ-algebra $\bigotimes_{i=1}^n \mathcal{F}_i$) satisfying the **consistency condition**:
$$
\mu_n = \mu_{n+1} \circ \pi_n^{-1}
$$
where $\pi_n: \prod_{i=1}^{n+1} X_i \to \prod_{i=1}^n X_i$ is the canonical projection discarding the last coordinate.

Then there exists a **unique** probability measure $\mu$ on the infinite product space $\prod_{n=1}^{\infty} X_n$ (equipped with the cylinder σ-algebra) such that the marginal of $\mu$ on the first $n$ coordinates equals $\mu_n$ for all $n$.

*Proof:* Deferred to Week 4 (conditional expectation and disintegration), where we develop the machinery for defining conditional probabilities on infinite product spaces. The proof uses cylinder sets, outer measure construction, and the π-λ theorem. See [@billingsley:probability:2012, Theorem 36.4] or [@kallenberg2002, Theorem 6.16] for complete details. □

**Remark 2.36** (Cylinder Sets and Infinite Products): The **cylinder σ-algebra** on $\prod_{n=1}^{\infty} X_n$ is the σ-algebra generated by cylinder sets of the form $C = B_1 \times \cdots \times B_k \times X_{k+1} \times X_{k+2} \times \cdots$ where $B_i \in \mathcal{F}_i$ and only finitely many factors are proper subsets (i.e., not equal to $X_i$). This construction generalizes the finite product σ-algebra [DEF-2.1.2] to infinite products. The rigorous development appears in Week 4, Day 4 (conditional expectations and infinite products).

**Application to MDP Trajectory Spaces:**

For an MDP with initial distribution $\mu_0$, policy $\pi$, and transition kernel $P$, define the trajectory space as $\Omega = (\mathcal{S} \times \mathcal{A})^{\mathbb{N}}$ with:
- $X_t = \mathcal{S} \times \mathcal{A}$ for each $t \geq 0$
- Finite-dimensional distributions on the first $n$ state-action pairs:
  $$
  \mu_n(s_0, a_0, \ldots, s_{n-1}, a_{n-1}) = \mu_0(s_0) \prod_{t=0}^{n-2} \pi(a_t|s_t) P(s_{t+1}|s_t, a_t)
  $$

**Verification of consistency:** For the projection $\pi_n: \prod_{i=0}^{n} (S \times A) \to \prod_{i=0}^{n-1} (S \times A)$ discarding the last state-action pair, we need to show $\mu_n = \mu_{n+1} \circ \pi_n^{-1}$.

Integrating $\mu_{n+1}$ over the last pair $(s_n, a_n)$:
$$
(\mu_{n+1} \circ \pi_n^{-1})(s_0, a_0, \ldots, s_{n-1}, a_{n-1}) = \int_{\mathcal{S} \times \mathcal{A}} \mu_{n+1}(s_0, a_0, \ldots, s_{n-1}, a_{n-1}, s_n, a_n) \, ds_n \, da_n
$$
$$
= \mu_0(s_0) \prod_{t=0}^{n-2} \pi(a_t|s_t) P(s_{t+1}|s_t, a_t) \underbrace{\int_{\mathcal{S}} P(s_n|s_{n-1}, a_{n-1}) \left[\int_{\mathcal{A}} \pi(a_n|s_n) \, da_n\right] ds_n}_{= \int_{\mathcal{S}} P(s_n|s_{n-1}, a_{n-1}) \cdot 1 \, ds_n = 1}
$$
$$
= \mu_n(s_0, a_0, \ldots, s_{n-1}, a_{n-1}) \quad \checkmark
$$

By Kolmogorov Extension [THM-2.5.2], there exists a unique probability measure $\mathbb{P}_{\pi}$ on the trajectory space $\Omega = (\mathcal{S} \times \mathcal{A})^{\mathbb{N}}$ inducing these marginals.

This measure makes rigorous the expectation from Week 1 Day 1:
$$
V^{\pi}(s_0) = \mathbb{E}_{\mathbb{P}_{\pi}}\left[\sum_{t=0}^{\infty} \gamma^t R(s_t, a_t)\right]
$$

**Thus, we have fulfilled the Week 1 promise:** The trajectory space σ-algebra is the infinite product σ-algebra, and the measure $\mathbb{P}_{\pi}$ is constructed via Kolmogorov Extension. ✓

**Computational Note:** While the Kolmogorov extension theorem guarantees existence of the measure over infinite trajectories $(\mathcal{S} \times \mathcal{A})^\infty$, computing expectations $\mathbb{E}_\pi[G_0]$ over infinite trajectories requires approximation:
- **Monte Carlo sampling:** Estimate $\mathbb{E}[G] \approx (1/N) \sum_{i=1}^N G_i$ from $N$ trajectory samples. By the Law of Large Numbers (Week 9), this converges as $N \to \infty$.
- **Truncation:** Finite-horizon approximation $G_0^T = \sum_{t=0}^T \gamma^t r_t$ has error $|\mathbb{E}[G_0] - \mathbb{E}[G_0^T]| \leq \gamma^{T+1} R_{\max}/(1-\gamma)$ for bounded rewards $|r| \leq R_{\max}$.

In practice, RL algorithms never work with the full infinite-dimensional trajectory space—they either sample finite trajectories or use recursive Bellman equations to avoid explicit trajectory summation.

**Forward References:**
- **Week 4, Day 4:** Conditional expectation and disintegration (formalizes tower property for trajectory integrals)
- **Week 7-10:** Markov chain theory (transition kernels for finite/countable/general state spaces)
- **Week 23, Days 1-2:** Full MDP formalism (trajectory measure $\mathbb{P}_{\pi}$ becomes operational tool)
- **Week 34:** Monte Carlo methods as empirical averaging over sampled trajectories from $\mathbb{P}_{\pi}$

---

#### **B. Fubini-Tonelli: Computing Double Integrals via Iteration**

**Days 2-3 Achievement:** We proved:
- **Tonelli's Theorem [THM-2.2.1]:** For non-negative measurable $f \geq 0$ on $X \times Y$, the iterated integrals equal the double integral:
  $$
  \int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f \, d(\mu \times \nu) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y)
  $$
- **Fubini's Theorem [THM-2.3.1]:** For $f \in L^1(\mu \times \nu)$ (integrable), the same equality holds.

**Key Mechanism:**
- **Tonelli:** Uses **Monotone Convergence Theorem [THM-1.2.3]** to extend from simple functions (where rectangles make integration trivial) to non-negative measurable functions
- **Fubini:** Splits $f = f^+ - f^-$ (positive/negative parts) and applies Tonelli to each, using integrability $\int |f| < \infty$ to ensure both parts are finite

**Why Both Theorems?** Tonelli handles non-negative functions without integrability, enabling proofs by MCT. Fubini requires integrability but permits signed functions, enabling practical computation.

**RL Connection:** In policy evaluation, computing the expected value function $V^\pi(s) = \mathbb{E}_{a \sim \pi(s), s' \sim P(\cdot|s,a)}[r(s,a) + \gamma V^\pi(s')]$ requires "swapping" the order of expectations. Formally:
$$
V^\pi(s) = \int_\mathcal{A} \pi(a|s) \left[\int_\mathcal{S} P(s'|s,a) \left(r(s,a) + \gamma V^\pi(s')\right) ds'\right] da
$$

By Fubini (assuming $V^\pi$ is integrable), we can rearrange this as:
$$
V^\pi(s) = \int_{\mathcal{A} \times \mathcal{S}} \left(r(s,a) + \gamma V^\pi(s')\right) P(s'|s,a) \pi(a|s) \, da \, ds'
$$

This is the **Bellman expectation equation** in integral form. Fubini guarantees the two formulations are equivalent—no approximation, no assumption beyond integrability.

---

#### **C. $L^p$ Spaces: The Geometry of Function Spaces**

**Day 4 Achievement:** We established $L^p(\mu)$ as **normed vector spaces** via:
- **Young's inequality [THM-2.4.1]:** $ab \leq a^p/p + b^q/q$ for conjugate exponents $1/p + 1/q = 1$
- **Hölder's inequality [THM-2.4.2]:** $\|fg\|_1 \leq \|f\|_p \|g\|_q$ (generalizes Cauchy-Schwarz)
- **Minkowski's inequality [THM-2.4.3]:** $\|f+g\|_p \leq \|f\|_p + \|g\|_p$ (triangle inequality)

**Key Mechanism:**
- **Hölder:** Normalization reduces to proving $\int FG \leq 1$ for $\|F\|_p = \|G\|_q = 1$, then apply Young pointwise
- **Minkowski:** Write $\int |f+g|^p = \int |f+g| \cdot |f+g|^{p-1}$, split via triangle inequality, apply Hölder to each term, simplify using conjugacy

**Geometric Intuition:** The $L^p$ norm $\|f\|_p = (\int |f|^p)^{1/p}$ measures "size" of functions:
- $p=1$: Total mass ($\|f\|_1 = \int |f|$)
- $p=2$: Energy ($\|f\|_2 = \sqrt{\int |f|^2}$, related to variance)
- $p=\infty$: Peak magnitude ($\|f\|_\infty = \text{ess sup} |f|$)

As $p$ increases, the $L^p$ norm increasingly focuses on the **largest values** of $f$, until at $p=\infty$ it ignores everything except the peak.

**RL Connection:** Value functions in continuous RL live in $L^p$ spaces:
- **$L^\infty$:** Bellman operators are $\gamma$-contractions in sup norm (Week 23)
- **$L^2$:** Least-squares TD minimizes projected Bellman error in $L^2$ norm (Week 35)
- **Duality:** Linear value function approximation exploits $(L^2)^* \cong L^2$ (Week 14)

---

### **II. Proof Technique Synthesis: Three Strategies, One Goal**

This week introduced three distinct proof paradigms:

#### **A. Monotone Approximation (Tonelli)**

**Strategy:** Prove for simple functions (where the result is obvious), extend to non-negative measurable functions via Monotone Convergence Theorem.

**Mechanism:**
1. **Simple functions:** Rectangles $A \times B$ satisfy $\int_{A \times B} 1 = \mu(A)\nu(B)$ trivially
2. **Monotone sequences:** Approximate $f$ by simple functions $\phi_n \uparrow f$ pointwise
3. **MCT:** Take limits inside the integral: $\int \lim \phi_n = \lim \int \phi_n$ (by [THM-1.2.3])

**Why it works:** Non-negative functions permit monotone approximation without losing mass. The limit operation preserves order, so MCT applies cleanly.

**When it fails:** Signed functions lack monotonicity. We must split $f = f^+ - f^-$ and apply Tonelli separately (this is Fubini).

**Generalization:** This "simple → monotone → general" paradigm recurs throughout measure theory (Week 1 for Lebesgue integral construction, Week 9 for ergodic theorems).

---

#### **B. Convexity and Pointwise Inequalities (Hölder)**

**Strategy:** Reduce an integral inequality to a pointwise inequality, integrate both sides.

**Mechanism:**
1. **Pointwise bound:** Young's inequality gives $F(x)G(x) \leq F(x)^p/p + G(x)^q/q$ at every $x$
2. **Integrate:** Linearity of integral preserves inequality
3. **Normalize:** Use conjugacy $1/p + 1/q = 1$ to simplify

**Why it works:** Convexity of $t \mapsto t^p$ (for $p > 1$) implies the weighted AM-GM inequality, from which Young's inequality follows. Integrating a pointwise bound is "free" by linearity.

**Key Insight:** Hölder is fundamentally a statement about **pairing** $L^p$ and $L^q$ spaces. The conjugacy relation $1/p + 1/q = 1$ is not arbitrary—it's the unique pairing that makes the product integrable.

---

#### **C. Decomposition and Duality (Minkowski)**

**Strategy:** Write the quantity of interest ($\|f+g\|_p^p$) in a form that exposes structure, then apply Hölder.

**Mechanism:**
1. **Splitting:** $\int |f+g|^p = \int |f+g| \cdot |f+g|^{p-1}$ (factor out one power)
2. **Triangle inequality:** $|f+g| \leq |f| + |g|$ (pointwise)
3. **Hölder:** Apply to $|f| \cdot |f+g|^{p-1}$ and $|g| \cdot |f+g|^{p-1}$ separately
4. **Conjugacy:** Verify $|f+g|^{p-1} \in L^q$ where $q = p/(p-1)$ (by computing $(p-1)q = p$)
5. **Simplify:** Cancel $(\int |f+g|^p)^{1/q}$ from both sides

**Why it works:** The factorization $|f+g|^p = |f+g| \cdot |f+g|^{p-1}$ creates a product where Hölder applies. The exponent $p-1$ is chosen precisely so that the conjugate exponent integrates to give back $\int |f+g|^p$.

**Key Insight:** Minkowski's proof is a **duality argument**: we use the fact that $L^p$ and $L^q$ are dual spaces (to be formalized in Week 3) to "lift" a pointwise bound to a norm inequality.

---

#### **D. Unifying Principle: Three Pillars of Measure-Theoretic Arguments**

The three proofs illustrate distinct but complementary techniques:

1. **Approximation (Tonelli):** Extend from simple cases (simple functions, rectangles) to general cases via monotone or dominated convergence. **Foundation:** Convergence theorems (MCT, DCT, Fatou).

2. **Convexity (Hölder):** Deduce integral inequalities from pointwise inequalities via linearity of integration. **Foundation:** Convex analysis (Young's inequality, Jensen's inequality).

3. **Duality (Minkowski):** Exploit pairing between $L^p$ and $L^q$ to "lift" pointwise bounds to norm bounds. **Foundation:** Functional analysis (dual spaces, Riesz representation).

**Meta-observation:** Measure theory synthesizes **order** (MCT), **linearity** (integration), and **geometry** (norms) into a unified framework. This is why $L^p$ spaces are the natural home for RL value functions.

---

### **III. Computational Verification: Theory Meets Practice**

We now verify Fubini's theorem and visualize $L^p$ unit balls numerically.

#### **A. Fubini Verification: Iterated Integrals**

**Theorem [THM-2.3.1] (Fubini, Recalled):** If $f \in L^1(\mu \times \nu)$, then:
$$
\int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y)
$$

**Test Case 1:** $f(x,y) = xy$ on $[0,1]^2$ with Lebesgue measure.

**Analytic Computation:**
$$
\int_0^1 \left(\int_0^1 xy \, dy\right) dx = \int_0^1 x \left[\frac{y^2}{2}\right]_0^1 dx = \int_0^1 \frac{x}{2} \, dx = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}
$$

Reversing order:
$$
\int_0^1 \left(\int_0^1 xy \, dx\right) dy = \int_0^1 y \left[\frac{x^2}{2}\right]_0^1 dy = \int_0^1 \frac{y}{2} \, dy = \frac{1}{4}
$$

**Verification:** Both orders give $1/4$. ✓

**Numerical Check (Python code in accompanying exercise file):**

**Test Case 2:** $f(x,y) = e^{-(x+y)}$ on $[0,\infty)^2$.

**Analytic Computation:**
$$
\int_0^\infty \left(\int_0^\infty e^{-(x+y)} \, dy\right) dx = \int_0^\infty e^{-x} \left[\int_0^\infty e^{-y} \, dy\right] dx = \int_0^\infty e^{-x} \cdot 1 \, dx = 1
$$

(using $\int_0^\infty e^{-y} \, dy = 1$ and $\int_0^\infty e^{-x} \, dx = 1$).

**Verification:** Both orders give $1$. ✓

**Pedagogical Note:** These examples demonstrate Fubini on **simple** functions where we can compute analytically. For more complex integrands (e.g., $f(x,y) = \sin(xy)/(1+x^2+y^2)$), numerical integration is essential. The key lesson: Fubini guarantees the orders of integration commute, freeing us to choose the computationally convenient order.

---

#### **B. Visualizing $L^p$ Unit Balls**

**Goal:** Plot the unit balls $\mathcal{B}_p = \{(x,y) \in \mathbb{R}^2 : \|(x,y)\|_p \leq 1\}$ for $p = 1, 2, \infty$.

**Definitions:**
- $\|(x,y)\|_1 = |x| + |y|$
- $\|(x,y)\|_2 = \sqrt{x^2 + y^2}$
- $\|(x,y)\|_\infty = \max\{|x|, |y|\}$

**Geometric Shapes:**
- **$p=1$ (diamond):** Boundary satisfies $|x| + |y| = 1$, giving vertices at $(\pm 1, 0)$ and $(0, \pm 1)$
- **$p=2$ (circle):** Boundary is $x^2 + y^2 = 1$, the unit circle
- **$p=\infty$ (square):** Boundary is $\max\{|x|, |y|\} = 1$, the square $[-1,1]^2$

**Observation:** As $p$ increases from 1 to $\infty$, the unit ball "inflates" from the diamond (most compact) through the circle to the square (most expansive). This reflects how the $L^p$ norm increasingly focuses on **peak values** as $p$ grows.

**Interpretation:**
- The **$L^1$ ball** is smallest (tightest constraint: sum of absolute values ≤ 1)
- The **$L^2$ ball** is intermediate (Euclidean distance)
- The **$L^\infty$ ball** is largest (loosest constraint: only peak value ≤ 1)

In RL, the choice of norm determines which value functions are "close":
- **$\|\cdot\|_\infty$:** Focuses on worst-case error (uniform convergence)
- **$\|\cdot\|_2$:** Focuses on average error (least-squares methods)
- **$\|\cdot\|_1$:** Focuses on total variation (distribution distances)

---

### **IV. RL Application Bridge: Fubini and the Bellman Equation**

We now formalize how Fubini enables computing $\mathbb{E}_{s,a}[V^\pi(s')]$ in policy evaluation.

#### **A. The Bellman Expectation Equation**

**Definition 2.15** (Value Function, Informal Preview) {#DEF-2.5.1}
For a Markov Decision Process (to be formalized rigorously in Week 23), the **state value function** $V^\pi: \mathcal{S} \to \mathbb{R}$ under policy $\pi$ satisfies the **Bellman expectation equation**:
$$
V^\pi(s) = \mathbb{E}_{a \sim \pi(s), s' \sim P(\cdot|s,a)}\left[r(s,a) + \gamma V^\pi(s')\right] \tag{2.24}
$$

*Notation (informal):*
- $\mathcal{S}$: state space, $\mathcal{A}$: action space (assume finite or countable for this discussion)
- $\pi: \mathcal{S} \times \mathcal{A} \to [0,1]$: policy (conditional probability distribution)
- $P: \mathcal{S} \times \mathcal{A} \times \mathcal{S} \to [0,1]$: transition kernel
- $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$: reward function (assumed bounded)
- $\gamma \in [0,1)$: discount factor

*This definition is heuristic; a complete measure-theoretic formulation will be provided in Week 23, Days 1-2.*

In integral form:
$$
V^\pi(s) = \int_\mathcal{A} \pi(a|s) \left[r(s,a) + \gamma \int_\mathcal{S} P(s'|s,a) V^\pi(s') \, ds'\right] da \tag{2.25}
$$

**Question:** Can we rearrange (2.25) to a single double integral over $\mathcal{A} \times \mathcal{S}$?

**Answer:** Yes, by Fubini's theorem.

---

#### **B. Applying Fubini to Policy Evaluation**

**Setup:** Define the integrand:
$$
f(a, s') = \pi(a|s) P(s'|s,a) \left[r(s,a) + \gamma V^\pi(s')\right]
$$

This is a function on $\mathcal{A} \times \mathcal{S}$ (with $s$ fixed as a parameter).

**Integrability:** Assume:
1. $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ is measurable and bounded: $|r(s,a)| \leq R_{\max}$
2. $V^\pi: \mathcal{S} \to \mathbb{R}$ is measurable and bounded: $|V^\pi(s)| \leq V_{\max}$ (true for discounted MDPs with bounded rewards; will be proven in Week 23)

Then:
$$
|f(a, s')| \leq \pi(a|s) P(s'|s,a) \left(R_{\max} + \gamma V_{\max}\right) \leq \pi(a|s) P(s'|s,a) (R_{\max} + V_{\max})
$$

Integrating:
$$
\int_{\mathcal{A} \times \mathcal{S}} |f(a, s')| \, da \, ds' \leq (R_{\max} + V_{\max}) \int_\mathcal{A} \pi(a|s) \left[\int_\mathcal{S} P(s'|s,a) \, ds'\right] da
$$

Since $\int_\mathcal{S} P(s'|s,a) \, ds' = 1$ (probability measure) and $\int_\mathcal{A} \pi(a|s) \, da = 1$, we have:
$$
\int_{\mathcal{A} \times \mathcal{S}} |f(a, s')| \, da \, ds' \leq R_{\max} + V_{\max} < \infty
$$

Thus $f \in L^1(\mathcal{A} \times \mathcal{S})$ with respect to the joint distribution $\rho(da \, ds') = \pi(da|s) P(ds'|s,a)$.

**Remark 2.37** (Conditional Fubini): The version of Fubini needed for Bellman equations is **Fubini for conditional expectations**, not the product measure Fubini from [THM-2.3.1]. For fixed state $s$, the joint distribution over $(a, s')$ is:
$$
\rho(da \times ds' | s) = \pi(da|s) P(ds'|s,a)
$$
The second factor $P(\cdot|s,a)$ depends on $a$, so this is not a product $\mu \otimes \nu$ of fixed marginals. However, the **tower property of conditional expectation** (Week 4) implies:
$$
\mathbb{E}_{a, s'}[g(a,s')] = \mathbb{E}_{a}[\mathbb{E}_{s'}[g(a, s') | a]]
$$
which justifies interchanging the order of integration. The full theory appears in Week 4 (conditional expectation) and Week 23 (MDP formalism). For now, we accept this as a rigorous but deferred justification.

---

**Theorem 2.10** (Fubini for Bellman Equation) {#THM-2.5.1}
Assume:
1. $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ is measurable and bounded: $|r(s,a)| \leq R_{\max}$
2. $V^\pi: \mathcal{S} \to \mathbb{R}$ is measurable and bounded: $|V^\pi(s)| \leq V_{\max}$

Then the Bellman expectation equation (2.25) can be written as:
$$
V^\pi(s) = \int_{\mathcal{A} \times \mathcal{S}} \left[r(s,a) + \gamma V^\pi(s')\right] P(s'|s,a) \pi(a|s) \, da \, ds' \tag{2.26}
$$
and the order of integration over $a$ and $s'$ can be freely interchanged.

*Proof.* By Fubini for conditional expectations (Remark 2.37), since $f \in L^1(\mathcal{A} \times \mathcal{S})$:
$$
\int_\mathcal{A} \left[\int_\mathcal{S} f(a, s') \, ds'\right] da = \int_{\mathcal{A} \times \mathcal{S}} f(a, s') \, da \, ds' = \int_\mathcal{S} \left[\int_\mathcal{A} f(a, s') \, da\right] ds'
$$

Substituting the definition of $f$ into the leftmost expression recovers (2.25), while the middle expression is (2.26). The rightmost expression shows we could equivalently compute by integrating over $a$ first, then $s'$. □

---

**Remark 2.38** (Computational Significance): In tabular RL with finite state-action spaces, (2.26) becomes:
$$
V^\pi(s) = \sum_{a \in \mathcal{A}} \sum_{s' \in \mathcal{S}} \pi(a|s) P(s'|s,a) \left[r(s,a) + \gamma V^\pi(s')\right]
$$

The order of summation (over $a$ then $s'$, or $s'$ then $a$) is irrelevant. In **continuous** state-action spaces, Fubini guarantees the same commutativity for integrals. This is not a "minor technical point"—without it, computing expectations via Monte Carlo sampling (RL's workhorse) would lack a rigorous justification.

**Remark 2.39** (Product Measures in Trajectory Spaces): For multi-step returns $G_t = \sum_{k=0}^\infty \gamma^k r_{t+k}$, we integrate over the entire trajectory space $\Omega = (\mathcal{S} \times \mathcal{A})^\infty$. The measure over trajectories uses the disintegration structure described in Section I.A. Fubini extends to these conditional products (via the tower property of conditional expectation, Week 4), enabling us to compute $\mathbb{E}_\pi[G_0]$ by summing/integrating over individual time steps.

**Remark 2.40** (Extension to Unbounded Rewards): Theorem 2.10 requires bounded rewards for simplicity. For unbounded rewards, two approaches exist:

**1. Weighted norms (Hernández-Lerma & Lasserre, 1996) [@hernandez1996]:** Define $\|V\|_w = \sup_s |V(s)|/w(s)$ for a weight function $w: \mathcal{S} \to [1, \infty)$ that grows with $\|s\|$. If $|r(s,a)| \leq C w(s)$ and $\mathbb{E}_{s' \sim P(\cdot|s,a)}[w(s')] \leq \alpha w(s)$ for some $\alpha < 1/\gamma$, then the Bellman operator $T^\pi$ is a contraction in $\|\cdot\|_w$ (Week 23, Day 3).

**2. Exponential discounting suffices (Bertsekas & Shreve, 1978) [@bertsekas1978]:** If $|r(s,a)| \leq C(1 + \|s\|^k)$ (polynomial growth) and $\gamma < 1$, then $\mathbb{E}[\sum_{t=0}^\infty \gamma^t |r_t|] < \infty$ under mild conditions on $P$ (e.g., $\mathbb{E}[\|s'\|^k | s,a] \leq D(1 + \|s\|^k)$ for some $D < \infty$). The discounting $\gamma^t$ provides sufficient decay.

**Practice vs. Theory:** Most deep RL implementations (PPO, SAC, TD3) use bounded reward clipping $r \mapsto \text{clip}(r, -R_{\max}, R_{\max})$ to avoid numerical instability, even when the true reward is unbounded. This is an engineering choice that sidesteps the measure-theoretic subtleties.

---

### **V. Weekly Reflection: Week 2 in the 48-Week Journey**

#### **Mathematical Insight**

This week established the **geometric structure of integration** in three phases:

1. **Product measures** (Days 1-2) extend measure theory from one dimension to products $X \times Y$, using the Carathéodory extension theorem to define $\mu \times \nu$ uniquely from its values on rectangles $A \times B$. The key insight: measures on simple sets (rectangles) determine measures on all Borel sets via outer measure approximation.

2. **Fubini-Tonelli theorems** (Days 2-3) justify computing double integrals via iterated integrals. Tonelli handles non-negative functions via Monotone Convergence, while Fubini extends to signed integrable functions by splitting into positive and negative parts. The distinction between the two is pedagogically crucial: Tonelli enables *proofs* (using MCT), while Fubini enables *computation* (practical evaluation).

3. **$L^p$ spaces** (Day 4) organize integrable functions into normed vector spaces. Hölder's inequality $\|fg\|_1 \leq \|f\|_p \|g\|_q$ establishes duality between $L^p$ and $L^q$ (conjugate exponents $1/p + 1/q = 1$), while Minkowski's inequality $\|f+g\|_p \leq \|f\|_p + \|g\|_p$ establishes the triangle inequality, completing the norm axioms.

**Central Theorem:** The interplay between **product measures**, **Fubini**, and **$L^p$ norms** reveals a deep principle: *integration is geometric*. Measures provide coordinates (via σ-algebras), integrals compute "volumes" in these coordinates, and norms organize functions into analyzable spaces where operators (like Bellman $T^\pi$) can be studied via functional analysis.

**Historical Context:** This material synthesizes work spanning 1902-1950:
- **Henri Lebesgue** (1902): Lebesgue measure and integration
- **Guido Fubini** (1907): Fubini's theorem for rectangles
- **Leonida Tonelli** (1909): Tonelli's theorem for non-negative functions
- **Frigyes Riesz** (1910): $L^p$ spaces and Hölder's inequality
- **Hermann Minkowski** (1910): Geometric interpretation of norms

These tools transformed analysis from a collection of ad-hoc techniques into a unified theory of integration and function spaces—the foundation for modern probability, PDE theory, and control.

---

#### **RL Connection**

In reinforcement learning, **measure theory is not optional**—it is the rigorous language in which RL theory is written:

1. **Product measures formalize trajectory spaces:** An MDP trajectory $(s_0, a_0, s_1, a_1, \ldots)$ is a sequence of random variables with joint distribution determined by $\pi$ and $P$. The disintegration machinery we introduced enables computing probabilities over entire trajectories: $\mathbb{P}_\pi(\tau \in \Omega)$ where $\Omega$ is an event in trajectory space.

2. **Fubini enables the Bellman equation:** The Bellman expectation equation $V^\pi(s) = \mathbb{E}_{a,s'}[r + \gamma V^\pi(s')]$ requires swapping order of integration over $a$ (action) and $s'$ (next state). Fubini for conditional expectations guarantees this is valid, turning the Bellman equation from a heuristic into a theorem [THM-2.5.1].

3. **$L^p$ spaces are where value functions live:** In continuous RL, value functions are not finite-dimensional vectors but elements of infinite-dimensional function spaces:
   - **Bellman operators** $T^\pi: L^\infty \to L^\infty$ are $\gamma$-contractions (Week 23)
   - **Least-squares TD** projects onto $L^2$ subspaces (Week 35)
   - **Policy gradients** use $L^2$ duality $(L^2)^* \cong L^2$ (Week 37)

Without $L^p$ theory, statements like "$T^\pi$ is a contraction" or "LSTD converges to the projected fixed point" are meaningless—we'd lack the normed space structure needed to define "contraction" and "projection."

**Concrete Example (Week 23 Preview):** The Bellman policy evaluation operator $T^\pi V = R + \gamma P^\pi V$ (where $P^\pi$ is the transition operator under policy $\pi$) satisfies:
$$
\|T^\pi V_1 - T^\pi V_2\|_\infty = \gamma \|P^\pi(V_1 - V_2)\|_\infty \leq \gamma \|V_1 - V_2\|_\infty
$$
**in the following settings:**

**1. Tabular MDPs (finite state-action spaces):** $P^\pi$ is a stochastic matrix with $\sum_{s'} P^\pi(s'|s) = 1$. Then $\|P^\pi V\|_\infty \leq \|V\|_\infty$ by the probabilistic interpretation: $\max_s |\sum_{s'} P^\pi(s'|s) V(s')| \leq \max_s \sum_{s'} P^\pi(s'|s) \max_{s''} |V(s'')| = \|V\|_\infty$. ✓

**2. Continuous state spaces with bounded kernels:** If $P^\pi$ is a Markov kernel (Week 10, Day 1) satisfying $\int_\mathcal{S} P^\pi(ds'|s) = 1$ for all $s$, then $\|T^\pi V_1 - T^\pi V_2\|_\infty \leq \gamma \|V_1 - V_2\|_\infty$ still holds by the same argument. ✓

**3. Function approximation (neural networks):** If $V_\theta(s) = \text{NN}_\theta(s)$ is a neural network approximation, then $T^\pi$ is **not** an operator on $L^\infty(\mathcal{S})$—it's an operator on a finite-dimensional parameter space $\mathbb{R}^d$ (the weights $\theta$). The contraction property in $L^\infty$ **does not imply** convergence of neural TD learning, because the projection step $\Pi: L^\infty \to \{\text{NN}_\theta : \theta \in \mathbb{R}^d\}$ is **non-expansive** only in specific norms (e.g., $L^2$ weighted by the state distribution). This is the **deadly triad** (Sutton & Barto, 2018, Section 11.3) [@sutton2018]: function approximation + bootstrapping + off-policy learning can diverge. ✗

**Theory-Practice Gap:** The clean $L^\infty$ contraction result for tabular MDPs does **not** extend to deep RL without additional assumptions (e.g., target networks, experience replay, gradient clipping). Week 35 (TD with function approximation) and Week 40 (deep RL theory) address this gap rigorously.

---

#### **Open Questions**

1. **When does Fubini fail in RL?** We required boundedness of $r$ and $V^\pi$ to ensure integrability. For unbounded rewards (e.g., $r(s,a) = s^2$ in continuous control), when does the Bellman equation remain well-defined? Does the discount factor $\gamma$ provide sufficient "damping" to ensure convergence of $\mathbb{E}[G_0] = \mathbb{E}[\sum_t \gamma^t r_t]$?

   **Preview:** Remark 2.40 above provides two approaches (weighted norms, polynomial growth with exponential discounting), to be developed fully in Week 23.

2. **Completeness of $L^p$ spaces:** We proved $L^p$ is a **normed space** (Minkowski establishes the triangle inequality), but is it **complete**? That is, does every Cauchy sequence in $L^p$ converge to an element of $L^p$? This is the **Riesz-Fischer theorem**, to be proven in Week 3, Day 1 using the Dominated Convergence Theorem. Completeness is essential for applying the Banach Fixed-Point Theorem to Bellman operators.

3. **Duality and linear approximation:** We stated that $(L^p)^* \cong L^q$ (the dual of $L^p$ is isomorphic to $L^q$ for conjugate $q$), but have not proven it. This is the **Riesz Representation Theorem for $L^p$ spaces** (Week 3, Days 2-3). Why does this matter for RL? Because **linear value function approximation** $V_\theta(s) = \theta^\top \phi(s)$ defines a linear functional on the space of state distributions, and duality theory characterizes exactly which functionals can be represented this way.

---

### **VI. Looking Ahead: Week 3 Preview**

Next week, we deepen our understanding of $L^p$ spaces by proving:

- **Monday (Day 1):** **Riesz-Fischer Theorem**: $L^p$ is complete (every Cauchy sequence converges)
- **Tuesday-Wednesday (Days 2-3):** **$L^p$ Duality**: $(L^p)^* \cong L^q$ for conjugate exponents (Riesz Representation)
- **Thursday (Day 4):** **Radon-Nikodym Theorem**: Characterizing absolutely continuous measures via densities $d\mu/d\nu$
- **Friday (Day 5):** Coding synthesis: Visualize importance sampling ratios, numerically verify Radon-Nikodym

**RL Preview:** The Radon-Nikodym theorem formalizes **importance sampling** in off-policy RL. When the behavior policy $\mu$ differs from the target policy $\pi$, the importance ratio $\rho = \pi/\mu$ is precisely the Radon-Nikodym derivative $d\pi/d\mu$. Week 3 will make this rigorous, including the **chain rule** for densities (crucial for policy gradient derivations).

---

### **Code Implementation**

Detailed Python code implementing:
1. Fubini verification (Test Cases 1 & 2)
2. $L^p$ unit ball visualization
3. Bellman equation computation for a simple MDP

is provided in the companion file:
**[[Day_5_exercises_revised_rl]]**

---

**End of Day 5 – Weekly Synthesis**

**Time Investment:** ~90-120 minutes (reading 20 min, proof review 30 min, coding 40 min, reflection 10-30 min)

**Deliverables:**
- ✓ Synthesized Week 2 proof strategies
- ✓ Verified Fubini numerically
- ✓ Visualized $L^p$ unit balls
- ✓ Formalized Bellman equation via Fubini [THM-2.5.1]
- ✓ Weekly reflection completed

**Next Session:** Week 3, Day 1 (Monday) – Riesz-Fischer Theorem: Completeness of $L^p$ Spaces
### Agenda:

##### 📘 Day 5 — Week 2: Weekly Synthesis – Product Measures, Fubini, and $L^p$ Spaces

**Total time: 90 minutes (Friday synthesis session)**

---

#### **⏱️ Segment 1 (20 min) — Reading & Review**

**Topic:** _Synthesizing Week 2: From Product Measures to Function Spaces_

- Review key results from Monday-Thursday:
    - **Product measures** (Days 1-2): Construction of $\mu \times \nu$ via Carathéodory extension
    - **Fubini-Tonelli** (Days 2-3): When iterated integrals equal double integrals
    - **$L^p$ spaces** (Day 4): Hölder and Minkowski inequalities establish normed space structure
- Reflection: How do these tools enable RL theory?
    - Product measures $\to$ trajectory spaces in MDPs
    - Fubini $\to$ computing expectations over state-action pairs
    - $L^p$ norms $\to$ function space framework for Bellman operators

---

#### **⏱️ Segment 2 (30 min) — Proof Technique Review**

**Primary Task:**
1. **Synthesis Exercise:** Compare and contrast the proof strategies for Tonelli, Hölder, and Minkowski
   - What role does monotonicity play? (Tonelli via MCT)
   - What role does convexity play? (Young's inequality $\to$ Hölder)
   - How do we build norms from integrals? (Minkowski establishes triangle inequality)

2. **Conceptual Exercise:** Identify the key mechanism in each major theorem
   - Tonelli: MCT + product measure uniqueness
   - Hölder: Normalization + Young's inequality
   - Minkowski: Splitting $|f+g|^p$ and applying Hölder twice

---

#### **⏱️ Segment 3 (40 min) — Computational Synthesis**

**Coding Tasks:**
1. **Fubini Verification (15 min):**
   - Compute $\iint f(x,y) \, dx \, dy$ via both orders of integration
   - Test functions: (a) $f(x,y) = xy$ on $[0,1]^2$, (b) $f(x,y) = e^{-(x+y)}$ on $[0,\infty)^2$
   - Verify equality numerically (within tolerance)

2. **$L^p$ Unit Ball Visualization (20 min):**
   - Plot unit balls $\{(x,y) : \|(x,y)\|_p \leq 1\}$ in $\mathbb{R}^2$ for $p = 1, 2, \infty$
   - Observe: $p=1$ is diamond, $p=2$ is circle, $p=\infty$ is square
   - Reflection: As $p \to \infty$, the unit ball approaches a square (sup norm focuses on peak magnitude)

3. **RL Connection Exercise (5 min):**
   - Reflect: How does Fubini enable computing $\mathbb{E}_{s,a}[V^\pi(s')]$ in policy evaluation?
   - Write: Formalize the double integral $\int \int V^\pi(s') P(s'|s,a) \, ds' \, d\rho(s,a)$ where $\rho$ is the state-action visitation measure

---

#### **💡 Weekly Reflection: Week 2 in Context**

This is our first **Friday synthesis session**. We step back from the day-to-day theorem-proving to:
1. **Consolidate** the week's mathematical machinery
2. **Verify** theorems computationally
3. **Bridge** to RL applications explicitly

Week 2 established the **geometric structure of integration**: product measures provide the canvas, Fubini enables computation, and $L^p$ norms organize functions into analyzable spaces. Next week (Week 3), we prove these spaces are **complete** (Riesz-Fischer) and study their **duality** ($(L^p)^* \cong L^q$), culminating in the **Radon-Nikodym theorem**—the measure-theoretic foundation for importance sampling.

---

## **Chapter 2.5: Friday Synthesis – Computational Exploration and Weekly Reflection**

### **Motivation: From Theory to Intuition**

Over the past four days, we have constructed a formidable theoretical architecture:
- **Product measures** (Days 1-2) enable integration over multi-dimensional spaces
- **Fubini-Tonelli theorems** (Days 2-3) justify computing double integrals via iterated integrals
- **$L^p$ spaces** (Day 4) organize integrable functions into normed vector spaces with geometric structure

Today, we pause theorem-proving to **verify** these abstractions computationally and **reflect** on their necessity for reinforcement learning. This is the first of many **Friday synthesis sessions**—a weekly rhythm where we:
1. Consolidate the week's proof techniques
2. Numerically validate key theorems
3. Explicitly bridge mathematics to RL algorithms

**Why computation matters:** Abstract theorems like Fubini guarantee equality of iterated integrals *in principle*, but numerical experiments build **geometric intuition**. When we later study policy evaluation operators $T^\pi V(s) = \mathbb{E}_{a,s'}[r(s,a) + \gamma V(s')]$, the mechanics of "swapping expectation and summation" will feel natural—because we've seen Fubini work in practice.

**Why reflection matters:** In the intensity of rigorous proof-writing, we risk losing sight of the **ultimate goal**: using these tools to reason about RL algorithms. Friday reflections anchor abstract mathematics to concrete RL problems, ensuring every theorem earns its place in our journey.

**What we'll accomplish today:**

**Learning Objectives:**
* Synthesize proof strategies from Tonelli, Hölder, and Minkowski
* Verify Fubini's theorem numerically for test functions
* Visualize $L^p$ unit balls in $\mathbb{R}^2$ to understand norm geometry
* Formalize how Fubini enables computing $\mathbb{E}_{s,a}[V^\pi(s')]$ in MDPs
* Reflect on Week 2's role in the 48-week journey

**Time allocation (90 min Friday):**
- 20 min reading/review: Synthesize Week 2 material
- 30 min proof technique review: Compare proof strategies
- 40 min computational synthesis: Code verification and visualization

---

### **I. Week 2 in Retrospect: The Geometry of Integration**

#### **A. Product Measures: Constructing Multi-Dimensional Integration**

**Recall from Week 1 Day 1 (Section IV, "Synthesis: Toward MDPs"):** We stated that the value function
$$V^{\pi}(s) = \mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \,\bigg|\, s_0 = s\right]$$
is an expectation over the **trajectory space** of state-action sequences $(s_0, a_0, s_1, a_1, \ldots)$. To make this rigorous, we need a $\sigma$-algebra on this infinite-dimensional space. We promised to develop the mathematical machinery to construct it using the **Kolmogorov extension theorem**. We now deliver on that promise.

**Days 1-2 Achievement:** Given measure spaces $(X, \mathcal{F}, \mu)$ and $(Y, \mathcal{G}, \nu)$, we constructed the **product measure** $\mu \times \nu$ on $(X \times Y, \mathcal{F} \otimes \mathcal{G})$ via the Carathéodory extension theorem.

**Key Mechanism:** The product $\sigma$-algebra $\mathcal{F} \otimes \mathcal{G}$ is generated by measurable rectangles $A \times B$, and the product measure is uniquely determined by $(\mu \times \nu)(A \times B) = \mu(A) \nu(B)$.

**RL Connection:** In Markov Decision Processes, the **trajectory space** $\Omega = (\mathcal{S} \times \mathcal{A})^\infty$ is a countable product space, with the joint measure over state-action sequences determined by the policy $\pi$ and transition kernel $P$. Product measures formalize how individual transition probabilities $P(s'|s,a)$ compose to give probabilities over entire trajectories.

**Concrete Example (MDP Trajectory Measure):** Consider an MDP with state space $\mathcal{S}$, action space $\mathcal{A}$, policy $\pi$, and transition kernel $P$. A single-step state-action-state transition $(s_t, a_t, s_{t+1})$ has probability measure:
$$
d\rho_1(s_t, a_t, s_{t+1}) = \mu_0(s_t) \, \pi(a_t|s_t) \, P(s_{t+1}|s_t, a_t)
$$
where $\mu_0$ is the initial state distribution.

For a trajectory of length $T$, the joint measure over $(s_0, a_0, s_1, a_1, \ldots, s_T)$ involves **conditional products** (also called disintegrations):
$$
d\rho_T(s_0, a_0, \ldots, s_T) = \mu_0(s_0) \prod_{t=0}^{T-1} \pi(a_t|s_t) P(s_{t+1}|s_t, a_t)
$$

**Technical Note:** This is not a standard product measure $\mu \times \nu$ from Week 2, because each factor $P(s_{t+1}|s_t, a_t)$ depends on previous variables. The rigorous framework is **disintegration of measures**: given a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ and a sub-$\sigma$-algebra $\mathcal{G} \subseteq \mathcal{F}$, the conditional measure $\mathbb{P}(\cdot | \mathcal{G})$ is a family of probability measures indexed by $\mathcal{G}$-measurable outcomes. For MDPs, the disintegration formula above defines the trajectory measure uniquely given $\mu_0, \pi, P$. The formal development appears in Week 4 (conditional expectation) and Week 23 (MDP measure theory). For now, we note that the formula is correct and implementable, even though its mathematical justification requires tools beyond Week 2.

**Reference:** Kallenberg "Foundations of Modern Probability" (2002), Chapter 6 (Regular conditional probabilities and disintegration) [@kallenberg2002].

**Theorem 2.11 (Kolmogorov Extension Theorem - Statement).** {#THM-2.5.2}
Let $(X_n, \mathcal{F}_n)_{n=1}^{\infty}$ be a sequence of measurable spaces. Suppose for each finite $n \geq 1$, we have a probability measure $\mu_n$ on $\prod_{i=1}^n X_i$ (equipped with the product $\sigma$-algebra $\bigotimes_{i=1}^n \mathcal{F}_i$) satisfying the **consistency condition**:
$$
\mu_n = \mu_{n+1} \circ \pi_n^{-1}
$$
where $\pi_n: \prod_{i=1}^{n+1} X_i \to \prod_{i=1}^n X_i$ is the canonical projection discarding the last coordinate.

Then there exists a **unique** probability measure $\mu$ on the infinite product space $\prod_{n=1}^{\infty} X_n$ (equipped with the cylinder $\sigma$-algebra) such that the marginal of $\mu$ on the first $n$ coordinates equals $\mu_n$ for all $n$.

*Proof:* Deferred to Week 4 (conditional expectation and disintegration), where we develop the machinery for defining conditional probabilities on infinite product spaces. The proof uses cylinder sets, outer measure construction, and the π-λ theorem. See [@billingsley:probability:2012, Theorem 36.4] or [@kallenberg2002, Theorem 6.16] for complete details. □

**Remark 2.36** (Cylinder Sets and Infinite Products): The **cylinder $\sigma$-algebra** on $\prod_{n=1}^{\infty} X_n$ is the $\sigma$-algebra generated by cylinder sets of the form $C = B_1 \times \cdots \times B_k \times X_{k+1} \times X_{k+2} \times \cdots$ where $B_i \in \mathcal{F}_i$ and only finitely many factors are proper subsets (i.e., not equal to $X_i$). This construction generalizes the finite product $\sigma$-algebra [DEF-2.1.2] to infinite products. The rigorous development appears in Week 4, Day 4 (conditional expectations and infinite products).

**Application to MDP Trajectory Spaces:**

For an MDP with initial distribution $\mu_0$, policy $\pi$, and transition kernel $P$, define the trajectory space as $\Omega = (\mathcal{S} \times \mathcal{A})^{\mathbb{N}}$ with:
- $X_t = \mathcal{S} \times \mathcal{A}$ for each $t \geq 0$
- Finite-dimensional distributions on the first $n$ state-action pairs:
  $$
  \mu_n(s_0, a_0, \ldots, s_{n-1}, a_{n-1}) = \mu_0(s_0) \prod_{t=0}^{n-2} \pi(a_t|s_t) P(s_{t+1}|s_t, a_t)
  $$

**Verification of consistency:** For the projection $\pi_n: \prod_{i=0}^{n} (S \times A) \to \prod_{i=0}^{n-1} (S \times A)$ discarding the last state-action pair, we need to show $\mu_n = \mu_{n+1} \circ \pi_n^{-1}$.

Integrating $\mu_{n+1}$ over the last pair $(s_n, a_n)$:
$$
(\mu_{n+1} \circ \pi_n^{-1})(s_0, a_0, \ldots, s_{n-1}, a_{n-1}) = \int_{\mathcal{S} \times \mathcal{A}} \mu_{n+1}(s_0, a_0, \ldots, s_{n-1}, a_{n-1}, s_n, a_n) \, ds_n \, da_n
$$
$$
= \mu_0(s_0) \prod_{t=0}^{n-2} \pi(a_t|s_t) P(s_{t+1}|s_t, a_t) \underbrace{\int_{\mathcal{S}} P(s_n|s_{n-1}, a_{n-1}) \left[\int_{\mathcal{A}} \pi(a_n|s_n) \, da_n\right] ds_n}_{= \int_{\mathcal{S}} P(s_n|s_{n-1}, a_{n-1}) \cdot 1 \, ds_n = 1}
$$
$$
= \mu_n(s_0, a_0, \ldots, s_{n-1}, a_{n-1}) \quad \checkmark
$$

By Kolmogorov Extension [THM-2.5.2], there exists a unique probability measure $\mathbb{P}_{\pi}$ on the trajectory space $\Omega = (\mathcal{S} \times \mathcal{A})^{\mathbb{N}}$ inducing these marginals.

This measure makes rigorous the expectation from Week 1 Day 1:
$$
V^{\pi}(s_0) = \mathbb{E}_{\mathbb{P}_{\pi}}\left[\sum_{t=0}^{\infty} \gamma^t R(s_t, a_t)\right]
$$

**Thus, we have fulfilled the Week 1 promise:** The trajectory space $\sigma$-algebra is the infinite product $\sigma$-algebra, and the measure $\mathbb{P}_{\pi}$ is constructed via Kolmogorov Extension. ✓

**Computational Note:** While the Kolmogorov extension theorem guarantees existence of the measure over infinite trajectories $(\mathcal{S} \times \mathcal{A})^\infty$, computing expectations $\mathbb{E}_\pi[G_0]$ over infinite trajectories requires approximation:
- **Monte Carlo sampling:** Estimate $\mathbb{E}[G] \approx (1/N) \sum_{i=1}^N G_i$ from $N$ trajectory samples. By the Law of Large Numbers (Week 9), this converges as $N \to \infty$.
- **Truncation:** Finite-horizon approximation $G_0^T = \sum_{t=0}^T \gamma^t r_t$ has error $|\mathbb{E}[G_0] - \mathbb{E}[G_0^T]| \leq \gamma^{T+1} R_{\max}/(1-\gamma)$ for bounded rewards $|r| \leq R_{\max}$.

In practice, RL algorithms never work with the full infinite-dimensional trajectory space—they either sample finite trajectories or use recursive Bellman equations to avoid explicit trajectory summation.

**Forward References:**
- **Week 4, Day 4:** Conditional expectation and disintegration (formalizes tower property for trajectory integrals)
- **Week 7-10:** Markov chain theory (transition kernels for finite/countable/general state spaces)
- **Week 23, Days 1-2:** Full MDP formalism (trajectory measure $\mathbb{P}_{\pi}$ becomes operational tool)
- **Week 34:** Monte Carlo methods as empirical averaging over sampled trajectories from $\mathbb{P}_{\pi}$

---

#### **B. Fubini-Tonelli: Computing Double Integrals via Iteration**

**Days 2-3 Achievement:** We proved:
- **Tonelli's Theorem [THM-2.2.1]:** For non-negative measurable $f \geq 0$ on $X \times Y$, the iterated integrals equal the double integral:
  $$
  \int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f \, d(\mu \times \nu) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y)
  $$
- **Fubini's Theorem [THM-2.3.1]:** For $f \in L^1(\mu \times \nu)$ (integrable), the same equality holds.

**Key Mechanism:**
- **Tonelli:** Uses **Monotone Convergence Theorem [THM-1.2.3]** to extend from simple functions (where rectangles make integration trivial) to non-negative measurable functions
- **Fubini:** Splits $f = f^+ - f^-$ (positive/negative parts) and applies Tonelli to each, using integrability $\int |f| < \infty$ to ensure both parts are finite

**Why Both Theorems?** Tonelli handles non-negative functions without integrability, enabling proofs by MCT. Fubini requires integrability but permits signed functions, enabling practical computation.

**RL Connection:** In policy evaluation, computing the expected value function $V^\pi(s) = \mathbb{E}_{a \sim \pi(s), s' \sim P(\cdot|s,a)}[r(s,a) + \gamma V^\pi(s')]$ requires "swapping" the order of expectations. Formally:
$$
V^\pi(s) = \int_\mathcal{A} \pi(a|s) \left[\int_\mathcal{S} P(s'|s,a) \left(r(s,a) + \gamma V^\pi(s')\right) ds'\right] da
$$

By Fubini (assuming $V^\pi$ is integrable), we can rearrange this as:
$$
V^\pi(s) = \int_{\mathcal{A} \times \mathcal{S}} \left(r(s,a) + \gamma V^\pi(s')\right) P(s'|s,a) \pi(a|s) \, da \, ds'
$$

This is the **Bellman expectation equation** in integral form. Fubini guarantees the two formulations are equivalent—no approximation, no assumption beyond integrability.

---

#### **C. $L^p$ Spaces: The Geometry of Function Spaces**

**Day 4 Achievement:** We established $L^p(\mu)$ as **normed vector spaces** via:
- **Young's inequality [THM-2.4.1]:** $ab \leq a^p/p + b^q/q$ for conjugate exponents $1/p + 1/q = 1$
- **Hölder's inequality [THM-2.4.2]:** $\|fg\|_1 \leq \|f\|_p \|g\|_q$ (generalizes Cauchy-Schwarz)
- **Minkowski's inequality [THM-2.4.3]:** $\|f+g\|_p \leq \|f\|_p + \|g\|_p$ (triangle inequality)

**Key Mechanism:**
- **Hölder:** Normalization reduces to proving $\int FG \leq 1$ for $\|F\|_p = \|G\|_q = 1$, then apply Young pointwise
- **Minkowski:** Write $\int |f+g|^p = \int |f+g| \cdot |f+g|^{p-1}$, split via triangle inequality, apply Hölder to each term, simplify using conjugacy

**Geometric Intuition:** The $L^p$ norm $\|f\|_p = (\int |f|^p)^{1/p}$ measures "size" of functions:
- $p=1$: Total mass ($\|f\|_1 = \int |f|$)
- $p=2$: Energy ($\|f\|_2 = \sqrt{\int |f|^2}$, related to variance)
- $p=\infty$: Peak magnitude ($\|f\|_\infty = \text{ess sup} |f|$)

As $p$ increases, the $L^p$ norm increasingly focuses on the **largest values** of $f$, until at $p=\infty$ it ignores everything except the peak.

**RL Connection:** Value functions in continuous RL live in $L^p$ spaces:
- **$L^\infty$:** Bellman operators are $\gamma$-contractions in sup norm (Week 23)
- **$L^2$:** Least-squares TD minimizes projected Bellman error in $L^2$ norm (Week 35)
- **Duality:** Linear value function approximation exploits $(L^2)^* \cong L^2$ (Week 14)

---

### **II. Proof Technique Synthesis: Three Strategies, One Goal**

This week introduced three distinct proof paradigms:

#### **A. Monotone Approximation (Tonelli)**

**Strategy:** Prove for simple functions (where the result is obvious), extend to non-negative measurable functions via Monotone Convergence Theorem.

**Mechanism:**
1. **Simple functions:** Rectangles $A \times B$ satisfy $\int_{A \times B} 1 = \mu(A)\nu(B)$ trivially
2. **Monotone sequences:** Approximate $f$ by simple functions $\phi_n \uparrow f$ pointwise
3. **MCT:** Take limits inside the integral: $\int \lim \phi_n = \lim \int \phi_n$ (by [THM-1.2.3])

**Why it works:** Non-negative functions permit monotone approximation without losing mass. The limit operation preserves order, so MCT applies cleanly.

**When it fails:** Signed functions lack monotonicity. We must split $f = f^+ - f^-$ and apply Tonelli separately (this is Fubini).

**Generalization:** This "simple $\to$ monotone $\to$ general" paradigm recurs throughout measure theory (Week 1 for Lebesgue integral construction, Week 9 for ergodic theorems).

---

#### **B. Convexity and Pointwise Inequalities (Hölder)**

**Strategy:** Reduce an integral inequality to a pointwise inequality, integrate both sides.

**Mechanism:**
1. **Pointwise bound:** Young's inequality gives $F(x)G(x) \leq F(x)^p/p + G(x)^q/q$ at every $x$
2. **Integrate:** Linearity of integral preserves inequality
3. **Normalize:** Use conjugacy $1/p + 1/q = 1$ to simplify

**Why it works:** Convexity of $t \mapsto t^p$ (for $p > 1$) implies the weighted AM-GM inequality, from which Young's inequality follows. Integrating a pointwise bound is "free" by linearity.

**Key Insight:** Hölder is fundamentally a statement about **pairing** $L^p$ and $L^q$ spaces. The conjugacy relation $1/p + 1/q = 1$ is not arbitrary—it's the unique pairing that makes the product integrable.

---

#### **C. Decomposition and Duality (Minkowski)**

**Strategy:** Write the quantity of interest ($\|f+g\|_p^p$) in a form that exposes structure, then apply Hölder.

**Mechanism:**
1. **Splitting:** $\int |f+g|^p = \int |f+g| \cdot |f+g|^{p-1}$ (factor out one power)
2. **Triangle inequality:** $|f+g| \leq |f| + |g|$ (pointwise)
3. **Hölder:** Apply to $|f| \cdot |f+g|^{p-1}$ and $|g| \cdot |f+g|^{p-1}$ separately
4. **Conjugacy:** Verify $|f+g|^{p-1} \in L^q$ where $q = p/(p-1)$ (by computing $(p-1)q = p$)
5. **Simplify:** Cancel $(\int |f+g|^p)^{1/q}$ from both sides

**Why it works:** The factorization $|f+g|^p = |f+g| \cdot |f+g|^{p-1}$ creates a product where Hölder applies. The exponent $p-1$ is chosen precisely so that the conjugate exponent integrates to give back $\int |f+g|^p$.

**Key Insight:** Minkowski's proof is a **duality argument**: we use the fact that $L^p$ and $L^q$ are dual spaces (to be formalized in Week 3) to "lift" a pointwise bound to a norm inequality.

---

#### **D. Unifying Principle: Three Pillars of Measure-Theoretic Arguments**

The three proofs illustrate distinct but complementary techniques:

1. **Approximation (Tonelli):** Extend from simple cases (simple functions, rectangles) to general cases via monotone or dominated convergence. **Foundation:** Convergence theorems (MCT, DCT, Fatou).

2. **Convexity (Hölder):** Deduce integral inequalities from pointwise inequalities via linearity of integration. **Foundation:** Convex analysis (Young's inequality, Jensen's inequality).

3. **Duality (Minkowski):** Exploit pairing between $L^p$ and $L^q$ to "lift" pointwise bounds to norm bounds. **Foundation:** Functional analysis (dual spaces, Riesz representation).

**Meta-observation:** Measure theory synthesizes **order** (MCT), **linearity** (integration), and **geometry** (norms) into a unified framework. This is why $L^p$ spaces are the natural home for RL value functions.

---

### **III. Computational Verification: Theory Meets Practice**

We now verify Fubini's theorem and visualize $L^p$ unit balls numerically.

#### **A. Fubini Verification: Iterated Integrals**

**Theorem [THM-2.3.1] (Fubini, Recalled):** If $f \in L^1(\mu \times \nu)$, then:
$$
\int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y)
$$

**Test Case 1:** $f(x,y) = xy$ on $[0,1]^2$ with Lebesgue measure.

**Analytic Computation:**
$$
\int_0^1 \left(\int_0^1 xy \, dy\right) dx = \int_0^1 x \left[\frac{y^2}{2}\right]_0^1 dx = \int_0^1 \frac{x}{2} \, dx = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}
$$

Reversing order:
$$
\int_0^1 \left(\int_0^1 xy \, dx\right) dy = \int_0^1 y \left[\frac{x^2}{2}\right]_0^1 dy = \int_0^1 \frac{y}{2} \, dy = \frac{1}{4}
$$

**Verification:** Both orders give $1/4$. ✓

**Numerical Check (Python code in accompanying exercise file):**

**Test Case 2:** $f(x,y) = e^{-(x+y)}$ on $[0,\infty)^2$.

**Analytic Computation:**
$$
\int_0^\infty \left(\int_0^\infty e^{-(x+y)} \, dy\right) dx = \int_0^\infty e^{-x} \left[\int_0^\infty e^{-y} \, dy\right] dx = \int_0^\infty e^{-x} \cdot 1 \, dx = 1
$$

(using $\int_0^\infty e^{-y} \, dy = 1$ and $\int_0^\infty e^{-x} \, dx = 1$).

**Verification:** Both orders give $1$. ✓

**Pedagogical Note:** These examples demonstrate Fubini on **simple** functions where we can compute analytically. For more complex integrands (e.g., $f(x,y) = \sin(xy)/(1+x^2+y^2)$), numerical integration is essential. The key lesson: Fubini guarantees the orders of integration commute, freeing us to choose the computationally convenient order.

---

#### **B. Visualizing $L^p$ Unit Balls**

**Goal:** Plot the unit balls $\mathcal{B}_p = \{(x,y) \in \mathbb{R}^2 : \|(x,y)\|_p \leq 1\}$ for $p = 1, 2, \infty$.

**Definitions:**
- $\|(x,y)\|_1 = |x| + |y|$
- $\|(x,y)\|_2 = \sqrt{x^2 + y^2}$
- $\|(x,y)\|_\infty = \max\{|x|, |y|\}$

**Geometric Shapes:**
- **$p=1$ (diamond):** Boundary satisfies $|x| + |y| = 1$, giving vertices at $(\pm 1, 0)$ and $(0, \pm 1)$
- **$p=2$ (circle):** Boundary is $x^2 + y^2 = 1$, the unit circle
- **$p=\infty$ (square):** Boundary is $\max\{|x|, |y|\} = 1$, the square $[-1,1]^2$

**Observation:** As $p$ increases from 1 to $\infty$, the unit ball "inflates" from the diamond (most compact) through the circle to the square (most expansive). This reflects how the $L^p$ norm increasingly focuses on **peak values** as $p$ grows.

**Interpretation:**
- The **$L^1$ ball** is smallest (tightest constraint: sum of absolute values $\le$ 1)
- The **$L^2$ ball** is intermediate (Euclidean distance)
- The **$L^\infty$ ball** is largest (loosest constraint: only peak value $\le$ 1)

In RL, the choice of norm determines which value functions are "close":
- **$\|\cdot\|_\infty$:** Focuses on worst-case error (uniform convergence)
- **$\|\cdot\|_2$:** Focuses on average error (least-squares methods)
- **$\|\cdot\|_1$:** Focuses on total variation (distribution distances)

---

### **IV. RL Application Bridge: Fubini and the Bellman Equation**

We now formalize how Fubini enables computing $\mathbb{E}_{s,a}[V^\pi(s')]$ in policy evaluation.

#### **A. The Bellman Expectation Equation**

**Definition 2.15** (Value Function, Informal Preview) {#DEF-2.5.1}
For a Markov Decision Process (to be formalized rigorously in Week 23), the **state value function** $V^\pi: \mathcal{S} \to \mathbb{R}$ under policy $\pi$ satisfies the **Bellman expectation equation**:
$$
V^\pi(s) = \mathbb{E}_{a \sim \pi(s), s' \sim P(\cdot|s,a)}\left[r(s,a) + \gamma V^\pi(s')\right] \tag{2.24}
$$

*Notation (informal):*
- $\mathcal{S}$: state space, $\mathcal{A}$: action space (assume finite or countable for this discussion)
- $\pi: \mathcal{S} \times \mathcal{A} \to [0,1]$: policy (conditional probability distribution)
- $P: \mathcal{S} \times \mathcal{A} \times \mathcal{S} \to [0,1]$: transition kernel
- $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$: reward function (assumed bounded)
- $\gamma \in [0,1)$: discount factor

*This definition is heuristic; a complete measure-theoretic formulation will be provided in Week 23, Days 1-2.*

In integral form:
$$
V^\pi(s) = \int_\mathcal{A} \pi(a|s) \left[r(s,a) + \gamma \int_\mathcal{S} P(s'|s,a) V^\pi(s') \, ds'\right] da \tag{2.25}
$$

**Question:** Can we rearrange (2.25) to a single double integral over $\mathcal{A} \times \mathcal{S}$?

**Answer:** Yes, by Fubini's theorem.

---

#### **B. Applying Fubini to Policy Evaluation**

**Setup:** Define the integrand:
$$
f(a, s') = \pi(a|s) P(s'|s,a) \left[r(s,a) + \gamma V^\pi(s')\right]
$$

This is a function on $\mathcal{A} \times \mathcal{S}$ (with $s$ fixed as a parameter).

**Integrability:** Assume:
1. $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ is measurable and bounded: $|r(s,a)| \leq R_{\max}$
2. $V^\pi: \mathcal{S} \to \mathbb{R}$ is measurable and bounded: $|V^\pi(s)| \leq V_{\max}$ (true for discounted MDPs with bounded rewards; will be proven in Week 23)

Then:
$$
|f(a, s')| \leq \pi(a|s) P(s'|s,a) \left(R_{\max} + \gamma V_{\max}\right) \leq \pi(a|s) P(s'|s,a) (R_{\max} + V_{\max})
$$

Integrating:
$$
\int_{\mathcal{A} \times \mathcal{S}} |f(a, s')| \, da \, ds' \leq (R_{\max} + V_{\max}) \int_\mathcal{A} \pi(a|s) \left[\int_\mathcal{S} P(s'|s,a) \, ds'\right] da
$$

Since $\int_\mathcal{S} P(s'|s,a) \, ds' = 1$ (probability measure) and $\int_\mathcal{A} \pi(a|s) \, da = 1$, we have:
$$
\int_{\mathcal{A} \times \mathcal{S}} |f(a, s')| \, da \, ds' \leq R_{\max} + V_{\max} < \infty
$$

Thus $f \in L^1(\mathcal{A} \times \mathcal{S})$ with respect to the joint distribution $\rho(da \, ds') = \pi(da|s) P(ds'|s,a)$.

**Remark 2.37** (Conditional Fubini): The version of Fubini needed for Bellman equations is **Fubini for conditional expectations**, not the product measure Fubini from [THM-2.3.1]. For fixed state $s$, the joint distribution over $(a, s')$ is:
$$
\rho(da \times ds' | s) = \pi(da|s) P(ds'|s,a)
$$
The second factor $P(\cdot|s,a)$ depends on $a$, so this is not a product $\mu \otimes \nu$ of fixed marginals. However, the **tower property of conditional expectation** (Week 4) implies:
$$
\mathbb{E}_{a, s'}[g(a,s')] = \mathbb{E}_{a}[\mathbb{E}_{s'}[g(a, s') | a]]
$$
which justifies interchanging the order of integration. The full theory appears in Week 4 (conditional expectation) and Week 23 (MDP formalism). For now, we accept this as a rigorous but deferred justification.

---

**Theorem 2.10** (Fubini for Bellman Equation) {#THM-2.5.1}
Assume:
1. $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ is measurable and bounded: $|r(s,a)| \leq R_{\max}$
2. $V^\pi: \mathcal{S} \to \mathbb{R}$ is measurable and bounded: $|V^\pi(s)| \leq V_{\max}$

Then the Bellman expectation equation (2.25) can be written as:
$$
V^\pi(s) = \int_{\mathcal{A} \times \mathcal{S}} \left[r(s,a) + \gamma V^\pi(s')\right] P(s'|s,a) \pi(a|s) \, da \, ds' \tag{2.26}
$$
and the order of integration over $a$ and $s'$ can be freely interchanged.

*Proof.* By Fubini for conditional expectations (Remark 2.37), since $f \in L^1(\mathcal{A} \times \mathcal{S})$:
$$
\int_\mathcal{A} \left[\int_\mathcal{S} f(a, s') \, ds'\right] da = \int_{\mathcal{A} \times \mathcal{S}} f(a, s') \, da \, ds' = \int_\mathcal{S} \left[\int_\mathcal{A} f(a, s') \, da\right] ds'
$$

Substituting the definition of $f$ into the leftmost expression recovers (2.25), while the middle expression is (2.26). The rightmost expression shows we could equivalently compute by integrating over $a$ first, then $s'$. □

---

**Remark 2.38** (Computational Significance): In tabular RL with finite state-action spaces, (2.26) becomes:
$$
V^\pi(s) = \sum_{a \in \mathcal{A}} \sum_{s' \in \mathcal{S}} \pi(a|s) P(s'|s,a) \left[r(s,a) + \gamma V^\pi(s')\right]
$$

The order of summation (over $a$ then $s'$, or $s'$ then $a$) is irrelevant. In **continuous** state-action spaces, Fubini guarantees the same commutativity for integrals. This is not a "minor technical point"—without it, computing expectations via Monte Carlo sampling (RL's workhorse) would lack a rigorous justification.

**Remark 2.39** (Product Measures in Trajectory Spaces): For multi-step returns $G_t = \sum_{k=0}^\infty \gamma^k r_{t+k}$, we integrate over the entire trajectory space $\Omega = (\mathcal{S} \times \mathcal{A})^\infty$. The measure over trajectories uses the disintegration structure described in Section I.A. Fubini extends to these conditional products (via the tower property of conditional expectation, Week 4), enabling us to compute $\mathbb{E}_\pi[G_0]$ by summing/integrating over individual time steps.

**Remark 2.40** (Extension to Unbounded Rewards): Theorem 2.10 requires bounded rewards for simplicity. For unbounded rewards, two approaches exist:

**1. Weighted norms (Hernández-Lerma & Lasserre, 1996) [@hernandez1996]:** Define $\|V\|_w = \sup_s |V(s)|/w(s)$ for a weight function $w: \mathcal{S} \to [1, \infty)$ that grows with $\|s\|$. If $|r(s,a)| \leq C w(s)$ and $\mathbb{E}_{s' \sim P(\cdot|s,a)}[w(s')] \leq \alpha w(s)$ for some $\alpha < 1/\gamma$, then the Bellman operator $T^\pi$ is a contraction in $\|\cdot\|_w$ (Week 23, Day 3).

**2. Exponential discounting suffices (Bertsekas & Shreve, 1978) [@bertsekas1978]:** If $|r(s,a)| \leq C(1 + \|s\|^k)$ (polynomial growth) and $\gamma < 1$, then $\mathbb{E}[\sum_{t=0}^\infty \gamma^t |r_t|] < \infty$ under mild conditions on $P$ (e.g., $\mathbb{E}[\|s'\|^k | s,a] \leq D(1 + \|s\|^k)$ for some $D < \infty$). The discounting $\gamma^t$ provides sufficient decay.

**Practice vs. Theory:** Most deep RL implementations (PPO, SAC, TD3) use bounded reward clipping $r \mapsto \text{clip}(r, -R_{\max}, R_{\max})$ to avoid numerical instability, even when the true reward is unbounded. This is an engineering choice that sidesteps the measure-theoretic subtleties.

---

### **V. Weekly Reflection: Week 2 in the 48-Week Journey**

#### **Mathematical Insight**

This week established the **geometric structure of integration** in three phases:

1. **Product measures** (Days 1-2) extend measure theory from one dimension to products $X \times Y$, using the Carathéodory extension theorem to define $\mu \times \nu$ uniquely from its values on rectangles $A \times B$. The key insight: measures on simple sets (rectangles) determine measures on all Borel sets via outer measure approximation.

2. **Fubini-Tonelli theorems** (Days 2-3) justify computing double integrals via iterated integrals. Tonelli handles non-negative functions via Monotone Convergence, while Fubini extends to signed integrable functions by splitting into positive and negative parts. The distinction between the two is pedagogically crucial: Tonelli enables *proofs* (using MCT), while Fubini enables *computation* (practical evaluation).

3. **$L^p$ spaces** (Day 4) organize integrable functions into normed vector spaces. Hölder's inequality $\|fg\|_1 \leq \|f\|_p \|g\|_q$ establishes duality between $L^p$ and $L^q$ (conjugate exponents $1/p + 1/q = 1$), while Minkowski's inequality $\|f+g\|_p \leq \|f\|_p + \|g\|_p$ establishes the triangle inequality, completing the norm axioms.

**Central Theorem:** The interplay between **product measures**, **Fubini**, and **$L^p$ norms** reveals a deep principle: *integration is geometric*. Measures provide coordinates (via $\sigma$-algebras), integrals compute "volumes" in these coordinates, and norms organize functions into analyzable spaces where operators (like Bellman $T^\pi$) can be studied via functional analysis.

**Historical Context:** This material synthesizes work spanning 1902-1950:
- **Henri Lebesgue** (1902): Lebesgue measure and integration
- **Guido Fubini** (1907): Fubini's theorem for rectangles
- **Leonida Tonelli** (1909): Tonelli's theorem for non-negative functions
- **Frigyes Riesz** (1910): $L^p$ spaces and Hölder's inequality
- **Hermann Minkowski** (1910): Geometric interpretation of norms

These tools transformed analysis from a collection of ad-hoc techniques into a unified theory of integration and function spaces—the foundation for modern probability, PDE theory, and control.

---

#### **RL Connection**

In reinforcement learning, **measure theory is not optional**—it is the rigorous language in which RL theory is written:

1. **Product measures formalize trajectory spaces:** An MDP trajectory $(s_0, a_0, s_1, a_1, \ldots)$ is a sequence of random variables with joint distribution determined by $\pi$ and $P$. The disintegration machinery we introduced enables computing probabilities over entire trajectories: $\mathbb{P}_\pi(\tau \in \Omega)$ where $\Omega$ is an event in trajectory space.

2. **Fubini enables the Bellman equation:** The Bellman expectation equation $V^\pi(s) = \mathbb{E}_{a,s'}[r + \gamma V^\pi(s')]$ requires swapping order of integration over $a$ (action) and $s'$ (next state). Fubini for conditional expectations guarantees this is valid, turning the Bellman equation from a heuristic into a theorem [THM-2.5.1].

3. **$L^p$ spaces are where value functions live:** In continuous RL, value functions are not finite-dimensional vectors but elements of infinite-dimensional function spaces:
   - **Bellman operators** $T^\pi: L^\infty \to L^\infty$ are $\gamma$-contractions (Week 23)
   - **Least-squares TD** projects onto $L^2$ subspaces (Week 35)
   - **Policy gradients** use $L^2$ duality $(L^2)^* \cong L^2$ (Week 37)

Without $L^p$ theory, statements like "$T^\pi$ is a contraction" or "LSTD converges to the projected fixed point" are meaningless—we'd lack the normed space structure needed to define "contraction" and "projection."

**Concrete Example (Week 23 Preview):** The Bellman policy evaluation operator $T^\pi V = R + \gamma P^\pi V$ (where $P^\pi$ is the transition operator under policy $\pi$) satisfies:
$$
\|T^\pi V_1 - T^\pi V_2\|_\infty = \gamma \|P^\pi(V_1 - V_2)\|_\infty \leq \gamma \|V_1 - V_2\|_\infty
$$
**in the following settings:**

**1. Tabular MDPs (finite state-action spaces):** $P^\pi$ is a stochastic matrix with $\sum_{s'} P^\pi(s'|s) = 1$. Then $\|P^\pi V\|_\infty \leq \|V\|_\infty$ by the probabilistic interpretation: $\max_s |\sum_{s'} P^\pi(s'|s) V(s')| \leq \max_s \sum_{s'} P^\pi(s'|s) \max_{s''} |V(s'')| = \|V\|_\infty$. ✓

**2. Continuous state spaces with bounded kernels:** If $P^\pi$ is a Markov kernel (Week 10, Day 1) satisfying $\int_\mathcal{S} P^\pi(ds'|s) = 1$ for all $s$, then $\|T^\pi V_1 - T^\pi V_2\|_\infty \leq \gamma \|V_1 - V_2\|_\infty$ still holds by the same argument. ✓

**3. Function approximation (neural networks):** If $V_\theta(s) = \text{NN}_\theta(s)$ is a neural network approximation, then $T^\pi$ is **not** an operator on $L^\infty(\mathcal{S})$—it's an operator on a finite-dimensional parameter space $\mathbb{R}^d$ (the weights $\theta$). The contraction property in $L^\infty$ **does not imply** convergence of neural TD learning, because the projection step $\Pi: L^\infty \to \{\text{NN}_\theta : \theta \in \mathbb{R}^d\}$ is **non-expansive** only in specific norms (e.g., $L^2$ weighted by the state distribution). This is the **deadly triad** (Sutton & Barto, 2018, Section 11.3) [@sutton2018]: function approximation + bootstrapping + off-policy learning can diverge. ✗

**Theory-Practice Gap:** The clean $L^\infty$ contraction result for tabular MDPs does **not** extend to deep RL without additional assumptions (e.g., target networks, experience replay, gradient clipping). Week 35 (TD with function approximation) and Week 40 (deep RL theory) address this gap rigorously.

---

#### **Open Questions**

1. **When does Fubini fail in RL?** We required boundedness of $r$ and $V^\pi$ to ensure integrability. For unbounded rewards (e.g., $r(s,a) = s^2$ in continuous control), when does the Bellman equation remain well-defined? Does the discount factor $\gamma$ provide sufficient "damping" to ensure convergence of $\mathbb{E}[G_0] = \mathbb{E}[\sum_t \gamma^t r_t]$?

   **Preview:** Remark 2.40 above provides two approaches (weighted norms, polynomial growth with exponential discounting), to be developed fully in Week 23.

2. **Completeness of $L^p$ spaces:** We proved $L^p$ is a **normed space** (Minkowski establishes the triangle inequality), but is it **complete**? That is, does every Cauchy sequence in $L^p$ converge to an element of $L^p$? This is the **Riesz-Fischer theorem**, to be proven in Week 3, Day 1 using the Dominated Convergence Theorem. Completeness is essential for applying the Banach Fixed-Point Theorem to Bellman operators.

3. **Duality and linear approximation:** We stated that $(L^p)^* \cong L^q$ (the dual of $L^p$ is isomorphic to $L^q$ for conjugate $q$), but have not proven it. This is the **Riesz Representation Theorem for $L^p$ spaces** (Week 3, Days 2-3). Why does this matter for RL? Because **linear value function approximation** $V_\theta(s) = \theta^\top \phi(s)$ defines a linear functional on the space of state distributions, and duality theory characterizes exactly which functionals can be represented this way.

---

### **VI. Looking Ahead: Week 3 Preview**

Next week, we deepen our understanding of $L^p$ spaces by proving:

- **Monday (Day 1):** **Riesz-Fischer Theorem**: $L^p$ is complete (every Cauchy sequence converges)
- **Tuesday-Wednesday (Days 2-3):** **$L^p$ Duality**: $(L^p)^* \cong L^q$ for conjugate exponents (Riesz Representation)
- **Thursday (Day 4):** **Radon-Nikodym Theorem**: Characterizing absolutely continuous measures via densities $d\mu/d\nu$
- **Friday (Day 5):** Coding synthesis: Visualize importance sampling ratios, numerically verify Radon-Nikodym

**RL Preview:** The Radon-Nikodym theorem formalizes **importance sampling** in off-policy RL. When the behavior policy $\mu$ differs from the target policy $\pi$, the importance ratio $\rho = \pi/\mu$ is precisely the Radon-Nikodym derivative $d\pi/d\mu$. Week 3 will make this rigorous, including the **chain rule** for densities (crucial for policy gradient derivations).

---

### **Code Implementation**

Detailed Python code implementing:
1. Fubini verification (Test Cases 1 & 2)
2. $L^p$ unit ball visualization
3. Bellman equation computation for a simple MDP

is provided in the companion file:
**[[Day_5_exercises_revised_rl]]**

---

**End of Day 5 – Weekly Synthesis**

**Time Investment:** ~90-120 minutes (reading 20 min, proof review 30 min, coding 40 min, reflection 10-30 min)

**Deliverables:**
- ✓ Synthesized Week 2 proof strategies
- ✓ Verified Fubini numerically
- ✓ Visualized $L^p$ unit balls
- ✓ Formalized Bellman equation via Fubini [THM-2.5.1]
- ✓ Weekly reflection completed

**Next Session:** Week 3, Day 1 (Monday) – Riesz-Fischer Theorem: Completeness of $L^p$ Spaces
