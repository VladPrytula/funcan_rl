[[Day_2_REVISED]]

# Week 2, Day 2: Exercises on Tonelli's Theorem

**Total time allocation: 40 minutes** (from 90-minute session)

---

## Exercise 1: Tonelli for Product of Non-Negative Functions (15 minutes)

**Problem Statement:**

Let $(X, \mathcal{F}_X, \mu)$ and $(Y, \mathcal{F}_Y, \nu)$ be σ-finite measure spaces. Let $f: X \to [0, \infty]$ be $\mathcal{F}_X$-measurable and $g: Y \to [0, \infty]$ be $\mathcal{F}_Y$-measurable.

Define $h: X \times Y \to [0, \infty]$ by $h(x,y) = f(x) \cdot g(y)$.

(a) Show that $h$ is $(\mathcal{F}_X \otimes \mathcal{F}_Y)$-measurable.

(b) Use Tonelli's theorem to prove:
$$
\int_{X \times Y} h \, d(\mu \times \nu) = \left(\int_X f \, d\mu\right) \cdot \left(\int_Y g \, d\nu\right)
$$

(c) Interpret this result in the context of **independent random variables** in probability theory.

---

### Solution

**(a) Measurability of $h(x,y) = f(x) \cdot g(y)$**

**Strategy:** We'll show $h$ is the composition of measurable functions, hence measurable.

**Step 1:** Consider the product map $\tilde{f} \times \tilde{g}: X \times Y \to [0,\infty] \times [0,\infty]$ defined by:
$$
(\tilde{f} \times \tilde{g})(x,y) = (f(x), g(y))
$$

**Claim:** This map is measurable.

**Proof:** By Day 1, Proposition 2.5, if $f: X \to [0,\infty]$ and $g: Y \to [0,\infty]$ are measurable, then the product map $(x,y) \mapsto (f(x), g(y))$ is measurable with respect to the product σ-algebras. Specifically:

For any rectangle $A \times B \in \mathcal{B}([0,\infty]) \otimes \mathcal{B}([0,\infty])$:
$$
(\tilde{f} \times \tilde{g})^{-1}(A \times B) = \{(x,y) : f(x) \in A, g(y) \in B\} = f^{-1}(A) \times g^{-1}(B)
$$

Since $f$ is measurable, $f^{-1}(A) \in \mathcal{F}_X$. Since $g$ is measurable, $g^{-1}(B) \in \mathcal{F}_Y$. Therefore, the preimage is a measurable rectangle in $\mathcal{F}_X \otimes \mathcal{F}_Y$. ✓

**Step 2:** The multiplication map $m: [0,\infty] \times [0,\infty] \to [0,\infty]$ defined by $m(a,b) = a \cdot b$ is continuous (hence Borel measurable) with respect to the standard topology on $[0,\infty]$ extended by the one-point compactification (where $[0,\infty] = [0,\infty) \cup \{\infty\}$ with $\infty$ as an isolated point in the relative topology induced by $[-\infty, \infty]$). By convention, $0 \cdot \infty = 0$.

**To verify continuity:** For any $a_n \to a$ and $b_n \to b$ in $[0,\infty]$, we have $a_n b_n \to ab$ (with the usual conventions). This follows from the product topology on $[0,\infty]$ where $[0,\infty]$ is the one-point compactification of $[0,\infty)$. ✓

**Step 3:** The composition $h = m \circ (\tilde{f} \times \tilde{g})$ is measurable.

By the general principle (Week 1, Day 1): composition of measurable functions is measurable. Thus $h$ is $(\mathcal{F}_X \otimes \mathcal{F}_Y, \mathcal{B}([0,\infty]))$-measurable. □

---

**(b) Proof of product formula using Tonelli**

We apply Tonelli's theorem to $h(x,y) = f(x) \cdot g(y)$.

**Step 1: Compute the inner integral over $Y$.**

Fix $x \in X$. By Tonelli (parts 1 and 2), the section $h(x, \cdot): Y \to [0,\infty]$ defined by $y \mapsto f(x) \cdot g(y)$ is measurable, and:
$$
\int_Y h(x,y) \, d\nu(y) = \int_Y f(x) \cdot g(y) \, d\nu(y) = f(x) \int_Y g(y) \, d\nu(y) = f(x) \cdot \left(\int_Y g \, d\nu\right)
$$

(Here we used that $f(x)$ is constant with respect to $y$, so it factors out of the integral.)

**Step 2: Compute the outer integral over $X$.**

Now integrate over $x$:
$$
\int_X \left(\int_Y h(x,y) \, d\nu(y)\right) d\mu(x) = \int_X f(x) \cdot \left(\int_Y g \, d\nu\right) d\mu(x) = \left(\int_Y g \, d\nu\right) \int_X f(x) \, d\mu(x)
$$

(Again, $\int_Y g \, d\nu$ is constant with respect to $x$, so it factors out.)

Thus:
$$
\int_X \left(\int_Y h(x,y) \, d\nu(y)\right) d\mu(x) = \left(\int_X f \, d\mu\right) \cdot \left(\int_Y g \, d\nu\right)
$$

**Step 3: Apply Tonelli to equate with double integral.**

By Tonelli's theorem (part 3), since $h \geq 0$ is measurable:
$$
\int_{X \times Y} h \, d(\mu \times \nu) = \int_X \left(\int_Y h(x,y) \, d\nu(y)\right) d\mu(x)
$$

Combining with Step 2:
$$
\int_{X \times Y} h \, d(\mu \times \nu) = \left(\int_X f \, d\mu\right) \cdot \left(\int_Y g \, d\nu\right)
$$

□

---

**(c) Interpretation: Independence of Random Variables**

**Probability theory context:** Let $(X, \mathcal{F}_X, \mu)$ and $(Y, \mathcal{F}_Y, \nu)$ be probability spaces (i.e., $\mu(X) = \nu(Y) = 1$). Let $\xi: X \to [0,\infty]$ and $\eta: Y \to [0,\infty]$ be non-negative random variables.

The product space $(X \times Y, \mathcal{F}_X \otimes \mathcal{F}_Y, \mu \times \nu)$ models the joint distribution of **independent random variables** $\xi$ and $\eta$.

**Question:** What is $\mathbb{E}[\xi \cdot \eta]$ when $\xi$ and $\eta$ are independent?

**Answer via part (b):** Define $h(x,y) = \xi(x) \cdot \eta(y)$. Then:
$$
\mathbb{E}[\xi \cdot \eta] = \int_{X \times Y} \xi(x) \cdot \eta(y) \, d(\mu \times \nu)(x,y) = \left(\int_X \xi \, d\mu\right) \cdot \left(\int_Y \eta \, d\nu\right) = \mathbb{E}[\xi] \cdot \mathbb{E}[\eta]
$$

**Conclusion:** For **independent non-negative random variables**, the expectation of the product equals the product of expectations:
$$
\mathbb{E}[\xi \cdot \eta] = \mathbb{E}[\xi] \cdot \mathbb{E}[\eta]
$$

This is the defining property of independence for random variables in probability theory.

**RL Application:** In model-based RL with factored dynamics (e.g., $s' = (s_1', s_2')$ where $s_1'$ and $s_2'$ are independent given $s,a$), computing feature expectations $\mathbb{E}[\phi_1(s_1') \cdot \phi_2(s_2')]$ reduces to $\mathbb{E}[\phi_1(s_1')] \cdot \mathbb{E}[\phi_2(s_2')]$ by this result, simplifying Bellman backups.

---

## Exercise 2: Tonelli for Infinite Sums (Anchor Exercise — 20 minutes)

**Problem Statement:**

Let $\{a_{ij}\}_{i,j \in \mathbb{N}}$ be a double sequence of **non-negative** real numbers.

(a) Prove that the order of summation does not matter:
$$
\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{ij} = \sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{ij}
$$

(b) Construct an example where $\{a_{ij}\}$ has terms of both signs, and the two iterated sums give different values.

(c) **RL Application:** In tabular policy evaluation, we compute $V^{\pi}(s) = \sum_{a} \pi(a|s) \sum_{s'} P(s'|s,a)[R(s,a,s') + \gamma V^{\pi}(s')]$. Under what conditions does Tonelli guarantee this is well-defined?

---

### Solution

**(a) Interchange of summation order for non-negative terms**

**Strategy:** Apply Tonelli's theorem to the counting measure on $\mathbb{N} \times \mathbb{N}$.

**Step 1: Set up the measure-theoretic framework.**

Let $X = Y = \mathbb{N}$ with σ-algebras $\mathcal{F}_X = \mathcal{F}_Y = 2^{\mathbb{N}}$ (power set). Define $\mu = \nu = $ **counting measure**:
$$
\mu(A) = \begin{cases} |A| & \text{if } A \text{ is finite} \\ \infty & \text{if } A \text{ is infinite} \end{cases}
$$

For singletons, $\mu(\{i\}) = 1$ for all $i \in \mathbb{N}$.

The **product measure** $\mu \times \nu$ on $\mathbb{N} \times \mathbb{N}$ is also the counting measure: $(\mu \times \nu)(\{(i,j)\}) = 1$ for all $i,j$.

**Step 2: Define the function $f: \mathbb{N} \times \mathbb{N} \to [0, \infty]$.**

Set $f(i,j) = a_{ij}$. Since $a_{ij} \geq 0$, the function $f$ is non-negative and measurable (all functions on $(\mathbb{N}, 2^{\mathbb{N}})$ are measurable, as every subset is measurable).

**Step 3: Apply Tonelli's theorem.**

By Tonelli (Theorem 2.3):
$$
\int_{\mathbb{N} \times \mathbb{N}} f \, d(\mu \times \nu) = \int_{\mathbb{N}} \left(\int_{\mathbb{N}} f(i,j) \, d\nu(j)\right) d\mu(i) = \int_{\mathbb{N}} \left(\int_{\mathbb{N}} f(i,j) \, d\mu(i)\right) d\nu(j)
$$

**Step 4: Translate integrals to sums.**

For counting measure, integrals become sums:
$$
\int_{\mathbb{N}} g(i) \, d\mu(i) = \sum_{i=1}^{\infty} g(i)
$$

Thus:
$$
\begin{align}
\int_{\mathbb{N}} \left(\int_{\mathbb{N}} f(i,j) \, d\nu(j)\right) d\mu(i) &= \sum_{i=1}^{\infty} \left(\sum_{j=1}^{\infty} a_{ij}\right) = \sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{ij} \\
\int_{\mathbb{N}} \left(\int_{\mathbb{N}} f(i,j) \, d\mu(i)\right) d\nu(j) &= \sum_{j=1}^{\infty} \left(\sum_{i=1}^{\infty} a_{ij}\right) = \sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{ij}
\end{align}
$$

By Tonelli, both equal the double integral (which is the double sum over $\mathbb{N} \times \mathbb{N}$):
$$
\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{ij} = \sum_{(i,j) \in \mathbb{N} \times \mathbb{N}} a_{ij} = \sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{ij}
$$

□

**Remark:** This is the classical result from real analysis that non-negative double series can be summed in any order. Tonelli reveals this as a special case of the general theorem on product measures.

---

**(b) Counterexample with signed terms**

**Construction:** Define the array:
$$
a_{ij} = \begin{cases}
1 & \text{if } i = j = 1 \\
-1 & \text{if } i = 1, j = 2 \\
\frac{(-1)^{i+1}}{2^{i-1}} & \text{if } j = 1 \text{ and } i \geq 2 \\
0 & \text{otherwise}
\end{cases}
$$

**Visualization of the array:**
```
      j=1    j=2    j=3    j=4    ...
i=1    1     -1      0      0     ...
i=2   1/2     0      0      0     ...
i=3  -1/4     0      0      0     ...
i=4   1/8     0      0      0     ...
...
```

**Sum by rows first (i, then j):**

For $i = 1$:
$$
\sum_{j=1}^{\infty} a_{1j} = 1 + (-1) + 0 + \cdots = 0
$$

For $i \geq 2$:
$$
\sum_{j=1}^{\infty} a_{ij} = \frac{(-1)^{i+1}}{2^{i-1}} + 0 + 0 + \cdots = \frac{(-1)^{i+1}}{2^{i-1}}
$$

Thus:
$$
\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{ij} = 0 + \sum_{i=2}^{\infty} \frac{(-1)^{i+1}}{2^{i-1}} = \frac{1}{2} - \frac{1}{4} + \frac{1}{8} - \cdots = \frac{1/2}{1 + 1/2} = \frac{1}{3}
$$

(This is a geometric series with first term $a = 1/2$ and ratio $r = -1/2$, so sum is $a/(1-r) = (1/2)/(3/2) = 1/3$.)

**Sum by columns first (j, then i):**

For $j = 1$:
$$
\sum_{i=1}^{\infty} a_{i,1} = 1 + \frac{1}{2} - \frac{1}{4} + \frac{1}{8} - \cdots = 1 + \sum_{i=2}^{\infty} \frac{(-1)^{i+1}}{2^{i-1}} = 1 + \frac{1}{3} = \frac{4}{3}
$$

For $j = 2$:
$$
\sum_{i=1}^{\infty} a_{i,2} = -1 + 0 + 0 + \cdots = -1
$$

For $j \geq 3$:
$$
\sum_{i=1}^{\infty} a_{i,j} = 0
$$

Thus:
$$
\sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{ij} = \frac{4}{3} + (-1) + 0 + \cdots = \frac{1}{3}
$$

**Wait—both sums equal $1/3$!** Let me construct a better counterexample.

**Correct Counterexample (Standard):** Consider the array where row $n$ consists of $+1$ in position $(n, n)$ and $-1$ in position $(n, n+1)$:

$$
a_{ij} = \begin{cases}
1 & \text{if } j = i \\
-1 & \text{if } j = i+1 \\
0 & \text{otherwise}
\end{cases}
$$

**Visualization:**
```
      j=1    j=2    j=3    j=4    ...
i=1    1     -1      0      0     ...
i=2    0      1     -1      0     ...
i=3    0      0      1     -1     ...
i=4    0      0      0      1     ...
...
```

**Sum by rows first:**
$$
\sum_{j=1}^{\infty} a_{ij} = 1 + (-1) = 0 \quad \text{for all } i
$$

Thus:
$$
\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{ij} = \sum_{i=1}^{\infty} 0 = 0
$$

**Sum by columns first:**

For $j = 1$:
$$
\sum_{i=1}^{\infty} a_{i,1} = 1 + 0 + 0 + \cdots = 1
$$

For $j \geq 2$:
$$
\sum_{i=1}^{\infty} a_{i,j} = -1 + 1 + 0 + \cdots = 0
$$

(The $-1$ comes from row $j-1$, the $+1$ from row $j$.)

Thus:
$$
\sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{ij} = 1 + 0 + 0 + \cdots = 1
$$

**Conclusion:** $\sum_i \sum_j a_{ij} = 0$ but $\sum_j \sum_i a_{ij} = 1$. The iterated sums **differ** when terms have mixed signs and the series is not absolutely convergent. ✓

**Key observation:** Note that $\sum_{i,j} |a_{ij}| = \sum_{i=1}^{\infty} (1 + 1) = \infty$ (not absolutely convergent). This confirms that **absolute convergence** (integrability $\int |f| < \infty$) is required for Fubini's theorem (Day 3).

---

**(c) RL Application: Tonelli in Tabular Policy Evaluation**

**Setting:** Finite MDP with $\mathcal{S} = \{1, \ldots, n_s\}$, $\mathcal{A} = \{1, \ldots, n_a\}$. Policy evaluation computes:
$$
V^{\pi}(s) = \sum_{a \in \mathcal{A}} \pi(a|s) \sum_{s' \in \mathcal{S}} P(s'|s,a) \left[R(s,a,s') + \gamma V^{\pi}(s')\right]
$$

**Question:** When does Tonelli apply to justify this iterated sum?

**Answer:**

**Case 1: Non-negative rewards and values.**

If $R(s,a,s') \geq 0$ and $V^{\pi}(s') \geq 0$ for all $s,a,s'$ (e.g., non-negative rewards with $\gamma \in [0,1)$, which forces $V^{\pi} \geq 0$), then the summand:
$$
f(a, s') = P(s'|s,a) [R(s,a,s') + \gamma V^{\pi}(s')] \geq 0
$$

By Exercise 2(a) (Tonelli for counting measure):
$$
\sum_{a} \pi(a|s) \sum_{s'} f(a,s') = \sum_{s'} \sum_{a} \pi(a|s) f(a,s')
$$

The order doesn't matter, and the sum is well-defined (possibly $+\infty$).

**Case 2: General signed rewards.**

If $R$ can be negative, we **cannot apply Tonelli directly**. Instead:

**Strategy:** Decompose $R = R^+ - R^-$ (positive and negative parts). Then:
$$
V^{\pi}(s) = \sum_{a} \pi(a|s) \sum_{s'} P(s'|s,a) \left[R^+(s,a,s') + \gamma V^{\pi}(s')\right] - \sum_{a} \pi(a|s) \sum_{s'} P(s'|s,a) R^-(s,a,s')
$$

Each term is non-negative, so Tonelli applies to each separately. However, we need **both sums to be finite** for $V^{\pi}(s)$ to be well-defined.

**Conclusion (Sufficient Condition):** If $\sum_{a,s'} \pi(a|s) P(s'|s,a) |R(s,a,s')| < \infty$, then Fubini applies (Day 3), guaranteeing the iterated sum equals the joint sum and is well-defined.

**Practical Note:** In tabular finite-state MDPs, all sums are finite (finite number of terms), so convergence is automatic. Tonelli/Fubini subtleties arise in:
- **Continuous state/action spaces** (integrals replace sums)
- **Infinite-horizon sums** (e.g., $\sum_{t=0}^{\infty} \gamma^t R_t$)
- **Importance sampling with unbounded ratios** (Week 37: off-policy policy gradients)

---

## Exercise 3: Application to Policy Gradient (Bonus - if time permits)

**Problem Statement:**

In policy gradient methods, we compute:
$$
\nabla_{\theta} J(\theta) = \mathbb{E}_{s \sim d^{\pi}}[\mathbb{E}_{a \sim \pi_{\theta}(\cdot|s)}[\nabla_{\theta} \log \pi_{\theta}(a|s) \cdot Q^{\pi}(s,a)]]
$$

Assume:
- State visitation distribution $d^{\pi}$ is a probability measure on $\mathcal{S}$
- Policy $\pi_{\theta}(a|s)$ is a conditional probability on $\mathcal{A}$ given $s$
- Q-function $Q^{\pi}(s,a) \geq 0$ (e.g., in episodic tasks with non-negative rewards and no discounting)

(a) Rewrite the gradient as an integral over the product space $\mathcal{S} \times \mathcal{A}$.

(b) Use Tonelli to justify interchanging the order of expectations.

(c) What happens if $Q^{\pi}$ can be negative? (Preview of Fubini.)

---

### Solution (Sketch)

**(a) Gradient as product-space integral:**

Define the joint measure $\rho$ on $\mathcal{S} \times \mathcal{A}$ by:
$$
\rho(ds, da) = d^{\pi}(ds) \cdot \pi_{\theta}(da|s)
$$

(This is the **state-action visitation measure** under policy $\pi_{\theta}$, constructed via disintegration of $d^\pi$ with conditional distribution $\pi_\theta(\cdot|s)$.)

Then:
$$
\nabla_{\theta} J(\theta) = \int_{\mathcal{S} \times \mathcal{A}} \nabla_{\theta} \log \pi_{\theta}(a|s) \cdot Q^{\pi}(s,a) \, \rho(ds, da)
$$

**(b) Tonelli application:**

If $Q^{\pi}(s,a) \geq 0$, define $f(s,a) = \nabla_{\theta} \log \pi_{\theta}(a|s) \cdot Q^{\pi}(s,a)$. (Assume for simplicity that $\nabla_{\theta} \log \pi_{\theta} \geq 0$, which holds for certain parameterizations such as softmax policies with positive features.)

By definition of $\rho$ as a disintegration of $d^\pi$ with conditional distribution $\pi_\theta(\cdot|s)$, we can write (using the disintegration theorem, Kallenberg Theorem 6.4, or conditional expectation theory from Week 4):

$$
\int_{\mathcal{S} \times \mathcal{A}} f(s,a) \, \rho(ds, da) = \int_{\mathcal{S}} \left(\int_{\mathcal{A}} f(s,a) \, \pi_{\theta}(da|s)\right) d^{\pi}(ds)
$$

This justifies computing the gradient via **sample-based estimation**: sample $s \sim d^{\pi}$, then $a \sim \pi_{\theta}(\cdot|s)$, compute the gradient term, and average.

**Important technical note:** The measure $\rho$ is NOT a product measure in the sense of Day 1—it's a conditional measure (disintegration). The correct framework for iterated integration with conditional measures requires the **disintegration theorem** or conditional expectation (Week 4, Day 4). For the purposes of this exercise, we assume the disintegration is well-defined and invoke the iterated integral formula.

When $f \geq 0$, Tonelli-type arguments apply to disintegrations (this is a generalization covered in advanced probability, e.g., Kallenberg §6.3). The key insight: **non-negativity allows interchange**, which is the essence of Tonelli.

**(c) When $Q^{\pi}$ can be negative:**

We must verify **integrability**:
$$
\int_{\mathcal{S} \times \mathcal{A}} |\nabla_{\theta} \log \pi_{\theta}(a|s) \cdot Q^{\pi}(s,a)| \, \rho(ds, da) < \infty
$$

If this holds, **Fubini** (Day 3) applies, allowing interchange. If not, the gradient may be undefined or require variance reduction techniques (baselines, control variates).

**Reference:** Sutton et al. (2000), "Policy Gradient Methods for Reinforcement Learning with Function Approximation," *NeurIPS*.

---

## Reflection and Connection to Tomorrow

**What We've Established Today:**

1. **Tonelli's theorem** justifies iterated integration for non-negative functions: order doesn't matter, and double integral equals both iterated integrals
2. **MCT is the key mechanism:** Non-negativity enables monotone approximation without domination hypotheses
3. **Computational power:** Tonelli enables practical computation of expectations via sequential sampling (sample $s$, then $a$, then compute)
4. **Limitation:** When functions have mixed signs, Tonelli fails—we need **Fubini** (integrability condition)

**Preview for Day 3:**

Tomorrow we prove **Fubini's theorem** for integrable functions $f \in L^1(\mu \times \nu)$:
$$
\int |f| < \infty \implies \int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f \, d(\mu \times \nu) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y)
$$

**Counterexamples to construct:**
1. **Without σ-finiteness:** Counting measure on uncountable set makes product measure non-unique
2. **Without integrability:** We constructed one today in Exercise 2(b)—iterated sums differ when $\sum |a_{ij}| = \infty$

**RL connection:** Importance sampling ratios $\pi(a|s)/\mu(a|s)$ in off-policy learning require integrability to apply Fubini—when unbounded, policy gradient variance explodes.

---

**End of Day 2 Exercises**
