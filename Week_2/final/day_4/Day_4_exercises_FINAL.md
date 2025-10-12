# Week 2, Day 4: Exercises on $L^p$ Spaces and Fundamental Inequalities

**Date:** Week 2, Day 4 (Thursday)
**Topic:** $L^p$ spaces, Young's inequality, Hölder's inequality, Minkowski's inequality
**Time allocation:** Exercises completed during 60-minute extended proof session

---

## **Anchor Exercises** (Required for Week 2 Syllabus Completion)

### **Exercise 1 (Anchor Exercise 3): Prove Hölder's Inequality** {#EX-2.4.1}

**Statement:** Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $1 < p, q < \infty$ be conjugate exponents: $1/p + 1/q = 1$. Prove that if $f \in L^p(\mu)$ and $g \in L^q(\mu)$, then $fg \in L^1(\mu)$ and:
$$
\int_X |fg| \, d\mu \leq \|f\|_p \|g\|_q
$$

**Guidance:**
1. Assume $\|f\|_p > 0$ and $\|g\|_q > 0$ (trivial cases handled separately)
2. Normalize: Define $F = |f|/\|f\|_p$ and $G = |g|/\|g\|_q$
3. Apply Young's inequality pointwise: $F(x)G(x) \leq F(x)^p/p + G(x)^q/q$
4. Integrate both sides
5. Use $\int F^p = 1$ and $\int G^q = 1$ (normalization) plus $1/p + 1/q = 1$
6. Substitute back to get the result for $f$ and $g$

---

**Solution:**

**Proof.** (As presented in Day 4, Section III)

**Step 0: Trivial cases.**
- If $\|f\|_p = 0$, then $f = 0$ $\mu$-a.e., so $fg = 0$ $\mu$-a.e., giving $\int |fg| = 0 \leq 0 \cdot \|g\|_q = 0$. ✓
- Similarly, if $\|g\|_q = 0$, the inequality holds trivially. ✓

Assume henceforth that $\|f\|_p > 0$ and $\|g\|_q > 0$.

**Step 1: Normalization.**

Define:
$$
F = \frac{|f|}{\|f\|_p}, \quad G = \frac{|g|}{\|g\|_q}
$$

Then:
$$
\|F\|_p = \frac{1}{\|f\|_p} \|f\|_p = 1, \quad \|G\|_q = \frac{1}{\|g\|_q} \|g\|_q = 1
$$

It suffices to prove Hölder for $F$ and $G$:
$$
\int_X FG \, d\mu \leq 1
$$

Once established, multiplying both sides by $\|f\|_p \|g\|_q$ recovers the full inequality for $f$ and $g$.

**Step 2: Apply Young's inequality pointwise.**

For each $x \in X$, Young's inequality (Theorem 2.5 from Day 4) states:
$$
F(x) G(x) \leq \frac{F(x)^p}{p} + \frac{G(x)^q}{q}
$$

since $F(x), G(x) \geq 0$ and $1/p + 1/q = 1$.

**Step 3: Integrate both sides.**

Integrating over $X$:
$$
\int_X F(x) G(x) \, d\mu(x) \leq \int_X \left[\frac{F(x)^p}{p} + \frac{G(x)^q}{q}\right] d\mu(x)
$$

By linearity of the integral:
$$
\int_X FG \, d\mu \leq \frac{1}{p} \int_X F^p \, d\mu + \frac{1}{q} \int_X G^q \, d\mu
$$

**Step 4: Use normalization and conjugacy.**

Since $\|F\|_p = 1$ and $\|G\|_q = 1$:
$$
\int_X F^p \, d\mu = \|F\|_p^p = 1, \quad \int_X G^q \, d\mu = \|G\|_q^q = 1
$$

Thus:
$$
\int_X FG \, d\mu \leq \frac{1}{p} \cdot 1 + \frac{1}{q} \cdot 1 = \frac{1}{p} + \frac{1}{q} = 1
$$

(using the conjugacy relation $1/p + 1/q = 1$).

**Step 5: Substitute back.**

From Step 1, $FG = |f| |g| / (\|f\|_p \|g\|_q)$, so:
$$
\int_X \frac{|f| |g|}{\|f\|_p \|g\|_q} \, d\mu \leq 1
$$

Multiplying both sides by $\|f\|_p \|g\|_q$:
$$
\int_X |f| |g| \, d\mu \leq \|f\|_p \|g\|_q
$$

Since $|fg| = |f| |g|$, this is exactly Hölder's inequality. □

**Remark (Equality Case).** Equality holds in Hölder iff equality holds in Young's inequality at almost every $x$. From Theorem 2.5, this occurs iff $F(x)^p = G(x)^q$ $\mu$-a.e., which means $|f|^p$ and $|g|^q$ are proportional:
$$
\frac{|f(x)|^p}{\|f\|_p^p} = \frac{|g(x)|^q}{\|g\|_q^q} \quad \mu\text{-a.e.}
$$

---

## **Supplementary Exercises** (Deepening Understanding)

### **Exercise 2: Prove Young's Inequality via Convexity** {#EX-2.4.2}

**Statement:** Let $p, q \in (1, \infty)$ be conjugate exponents: $1/p + 1/q = 1$. Prove that for any $a, b \geq 0$:
$$
ab \leq \frac{a^p}{p} + \frac{b^q}{q}
$$

with equality iff $a^p = b^q$.

**Method:** Use the weighted arithmetic-geometric mean inequality:
$$
x^\lambda y^{1-\lambda} \leq \lambda x + (1-\lambda) y \quad \text{for } x, y > 0, \lambda \in (0,1)
$$

Set $\lambda = 1/p$ (so $1 - \lambda = 1/q$), $x = a^p$, $y = b^q$.

---

**Solution:**

**Proof.**

**Step 1: Weighted AM-GM inequality.**

Recall the weighted arithmetic-geometric mean inequality (derived from Jensen's inequality for the concave function $\log$):
$$
x^\lambda y^{1-\lambda} \leq \lambda x + (1-\lambda) y \quad \text{for } x, y > 0, \lambda \in (0,1) \tag{E.1}
$$

with equality iff $x = y$.

**Step 2: Specialize to $\lambda = 1/p$.**

Set $\lambda = 1/p$. Then $1 - \lambda = 1 - 1/p = (p-1)/p = 1/q$ (using $1/p + 1/q = 1$).

Set $x = a^p$ and $y = b^q$ in (E.1):
$$
(a^p)^{1/p} (b^q)^{1/q} \leq \frac{1}{p} a^p + \frac{1}{q} b^q
$$

**Step 3: Simplify exponents.**

$(a^p)^{1/p} = a$ and $(b^q)^{1/q} = b$, so:
$$
ab \leq \frac{a^p}{p} + \frac{b^q}{q}
$$

This is Young's inequality.

**Equality condition:** From (E.1), equality holds iff $x = y$, i.e., $a^p = b^q$. □

---

### **Exercise 3: Alternative Proof Task—Minkowski for Boundary Cases** {#EX-2.4.3}

**Statement:** The main text proves Minkowski's inequality for $1 < p < \infty$ using Hölder's inequality. Prove Minkowski's inequality for the boundary cases:
(a) $p = 1$
(b) $p = \infty$

**Guidance:**
- For $p = 1$: Use the triangle inequality $|f + g| \leq |f| + |g|$ and linearity of the integral
- For $p = \infty$: Use $|f| \leq \|f\|_\infty$ $\mu$-a.e. and $|g| \leq \|g\|_\infty$ $\mu$-a.e., then take essential supremum

---

**Solution:**

**Part (a): $p = 1$**

**Proof.** For $p = 1$, Minkowski states:
$$
\int |f + g| \, d\mu \leq \int |f| \, d\mu + \int |g| \, d\mu
$$

By the triangle inequality for absolute values, for all $x$:
$$
|f(x) + g(x)| \leq |f(x)| + |g(x)|
$$

Integrating both sides:
$$
\int |f + g| \, d\mu \leq \int (|f| + |g|) \, d\mu
$$

By linearity of the integral:
$$
\int (|f| + |g|) \, d\mu = \int |f| \, d\mu + \int |g| \, d\mu
$$

Thus:
$$
\int |f + g| \, d\mu \leq \int |f| \, d\mu + \int |g| \, d\mu
$$

which is Minkowski for $p = 1$. □

---

**Part (b): $p = \infty$**

**Proof.** For $p = \infty$, Minkowski states:
$$
\|f + g\|_\infty \leq \|f\|_\infty + \|g\|_\infty
$$

Since $|f(x)| \leq \|f\|_\infty$ $\mu$-a.e. and $|g(x)| \leq \|g\|_\infty$ $\mu$-a.e., we have:
$$
|f(x) + g(x)| \leq |f(x)| + |g(x)| \leq \|f\|_\infty + \|g\|_\infty \quad \mu\text{-a.e.}
$$

By definition of essential supremum:
$$
\|f + g\|_\infty = \inf\{M : |f + g| \leq M \text{ } \mu\text{-a.e.}\}
$$

Since $|f + g| \leq \|f\|_\infty + \|g\|_\infty$ $\mu$-a.e., the constant $M = \|f\|_\infty + \|g\|_\infty$ is in the set over which we take the infimum. Therefore:
$$
\|f + g\|_\infty \leq \|f\|_\infty + \|g\|_\infty
$$

which is Minkowski for $p = \infty$. □

---

### **Exercise 4: RL Application — Importance Sampling Variance Bound via Hölder** {#EX-2.4.4}

**Statement:** In off-policy RL, we estimate $\mathbb{E}_\pi[R]$ using importance sampling: $\mathbb{E}_\mu[\rho R]$ where $\rho = \pi/\mu$ (assuming $\text{supp}(\pi) \subseteq \text{supp}(\mu)$).

**(a)** Using Hölder's inequality with $p = q = 2$ applied to $\rho^2$ and $R^2$, derive a bound on $\mathbb{E}_\mu[(\rho R)^2]$ in terms of fourth moments.

**(b)** Assuming the importance ratio is **bounded**: $|\rho| \leq \rho_{\max}$ almost surely, derive a simpler variance bound in terms of second moments.

**(c)** Discuss why clipping $\rho$ reduces variance in practice (PPO, V-trace).

---

**Solution:**

**Part (a): Fourth-moment bound via Hölder.**

**Proof.** The variance satisfies:
$$
\text{Var}_\mu[\rho R] = \mathbb{E}_\mu[(\rho R)^2] - (\mathbb{E}_\mu[\rho R])^2 \leq \mathbb{E}_\mu[(\rho R)^2]
$$

since $(\mathbb{E}[\rho R])^2 \geq 0$.

Now, $\mathbb{E}_\mu[(\rho R)^2] = \mathbb{E}_\mu[\rho^2 R^2]$ is an expectation of a product of two non-negative functions: $\rho^2$ and $R^2$.

We apply Hölder's inequality to the functions $f(s,a) = \rho(s,a)^2 \in L^2(\mu)$ and $g(s,a) = R(s,a)^2 \in L^2(\mu)$ on the state-action space with measure $\mu$, using conjugate exponents $p = q = 2$:
$$
\int_{(s,a)} \rho^2(s,a) R^2(s,a) \, d\mu(s,a) = \mathbb{E}_\mu[\rho^2 R^2] \leq \|\rho^2\|_2 \|R^2\|_2 = \sqrt{\mathbb{E}_\mu[\rho^4]} \sqrt{\mathbb{E}_\mu[R^4]}
$$

In expectation notation:
$$
\mathbb{E}_\mu[(\rho R)^2] = \mathbb{E}_\mu[\rho^2 R^2] \leq \sqrt{\mathbb{E}_\mu[\rho^4]} \sqrt{\mathbb{E}_\mu[R^4]}
$$

Therefore:
$$
\text{Var}_\mu[\rho R] \leq \sqrt{\mathbb{E}_\mu[\rho^4]} \sqrt{\mathbb{E}_\mu[R^4]}
$$

This is a **fourth-moment bound**: if the importance ratio has heavy tails ($\mathbb{E}[\rho^4]$ is large), variance can be very large. □

---

**Part (b): Second-moment bound with bounded ratios.**

**Proof.** Assume $|\rho(x)| \leq \rho_{\max}$ for $\mu$-almost every $x$ (achieved via clipping or inherent boundedness).

Then:
$$
\rho^2(x) R^2(x) \leq \rho_{\max}^2 R^2(x) \quad \mu\text{-a.e.}
$$

Integrating:
$$
\mathbb{E}_\mu[(\rho R)^2] = \int \rho^2 R^2 \, d\mu \leq \rho_{\max}^2 \int R^2 \, d\mu = \rho_{\max}^2 \mathbb{E}_\mu[R^2]
$$

Thus:
$$
\text{Var}_\mu[\rho R] \leq \mathbb{E}_\mu[(\rho R)^2] \leq \rho_{\max}^2 \mathbb{E}_\mu[R^2]
$$

This bound depends only on **second moments** and is finite as long as $R$ has finite variance. □

---

**Part (c): Why clipping reduces variance.**

**Discussion:**

**Unclipped importance sampling:** If $\rho$ is unbounded (e.g., when behavior policy $\mu$ is nearly deterministic and target policy $\pi$ is stochastic), the fourth moment $\mathbb{E}[\rho^4]$ can be extremely large or even infinite. From part (a), this causes variance explosion:
$$
\text{Var}[\rho R] \leq \sqrt{\mathbb{E}[\rho^4]} \sqrt{\mathbb{E}[R^4]}
$$

If $\mathbb{E}[\rho^4] = \infty$, the bound is vacuous.

**Clipped importance sampling:** Define the clipped ratio:
$$
\bar{\rho} = \min(\rho, \rho_{\max})
$$

for some threshold $\rho_{\max} > 0$ (e.g., $\rho_{\max} = 1$ in V-trace, $\rho_{\max} = 1 + \epsilon$ in PPO with $\epsilon \approx 0.2$).

By construction, $|\bar{\rho}| \leq \rho_{\max}$, so by part (b):
$$
\text{Var}_\mu[\bar{\rho} R] \leq \rho_{\max}^2 \mathbb{E}_\mu[R^2] < \infty
$$

This variance is **guaranteed finite** regardless of the tail behavior of the original $\rho$.

**Trade-off:** Clipping introduces **bias**:
$$
\mathbb{E}_\mu[\bar{\rho} R] \neq \mathbb{E}_\pi[R] \quad \text{(in general)}
$$

because $\bar{\rho} \neq \rho$ when $\rho > \rho_{\max}$. However, this bias is often small in practice, and the **bias-variance trade-off** favors clipping:
- **Unclipped:** Unbiased but potentially infinite variance
- **Clipped:** Small bias but finite, controlled variance

**Practical algorithms:**
- **PPO (Proximal Policy Optimization):** Clips $\rho_t = \pi_\theta(a_t|s_t) / \pi_{\text{old}}(a_t|s_t)$ to $[1-\epsilon, 1+\epsilon]$ with $\epsilon \approx 0.2$
- **V-trace:** Clips per-timestep ratios $\bar{\rho}_t = \min(\rho_t, \bar{\rho}_{\max})$ and $\bar{c}_t = \min(\rho_t, \bar{c}_{\max})$ to prevent product explosion over trajectories
- **AWR (Advantage-Weighted Regression):** Uses $\exp(\beta A(s,a))$ with bounded advantage, implicitly controlling the effective importance weight

All enforce bounded importance ratios, ensuring Hölder-based variance bounds hold with finite constants. □

---

### **Exercise 5: Visualize $L^p$ Unit Balls** {#EX-2.4.5}

**Statement:** Consider $\mathbb{R}^2$ with the standard $\ell^p$ norms (discrete analog of $L^p$). For $p = 1, 2, \infty$, describe (and sketch if possible) the unit ball:
$$
B_p = \{(x, y) \in \mathbb{R}^2 : \|(x, y)\|_p \leq 1\}
$$

where $\|(x, y)\|_p = (|x|^p + |y|^p)^{1/p}$ for $p < \infty$, and $\|(x, y)\|_\infty = \max(|x|, |y|)$.

**Hint:**
- $p = 1$: Diamond shape (Manhattan norm)
- $p = 2$: Circle (Euclidean norm)
- $p = \infty$: Square (Chebyshev norm)

---

**Solution:**

**Geometric Description:**

**$p = 1$ (Manhattan / Taxicab norm):**
$$
\|(x, y)\|_1 = |x| + |y| \leq 1
$$

The unit ball $B_1$ is the set of points $(x, y)$ satisfying $|x| + |y| \leq 1$. This is a **diamond** (square rotated 45°) with vertices at $(1, 0)$, $(0, 1)$, $(-1, 0)$, $(0, -1)$.

**$p = 2$ (Euclidean norm):**
$$
\|(x, y)\|_2 = \sqrt{x^2 + y^2} \leq 1
$$

The unit ball $B_2$ is the **unit circle** $x^2 + y^2 \leq 1$ (standard Euclidean disk).

**$p = \infty$ (Chebyshev / Maximum norm):**
$$
\|(x, y)\|_\infty = \max(|x|, |y|) \leq 1
$$

The unit ball $B_\infty$ is the **unit square** $[-1, 1] \times [-1, 1]$ (all points where both coordinates are in $[-1, 1]$).

**Sketch:** (Textual description)

```
     y
     |
   1 +---●--- (p=∞ square)
     |   /\   (p=1 diamond)
     |  /  \  (p=2 circle)
     | /    \
     |/      \
  ---+--------+--- x
     |\      /
     | \    /
     |  \  /
     |   \/
  -1 +---●---
     |
```

**Observations:**
1. All three unit balls are **convex** and **symmetric** about the origin
2. As $p$ increases from 1 to $\infty$, the unit ball transitions from diamond → circle → square
3. **Inclusion (on bounded sets):** On $\mathbb{R}^n$ with Lebesgue measure restricted to a bounded set (e.g., $[0,1]^n$), we have $B_\infty \subseteq B_2 \subseteq B_1$
4. For general $1 \leq p_1 < p_2 \leq \infty$ on bounded sets: $B_{p_2} \subseteq B_{p_1}$ (smaller $p$ gives "fatter" balls)

**Note on infinite measure spaces:** On **unbounded sets** like $\mathbb{R}$ with Lebesgue measure, these inclusions can fail. For example:
- $f(x) = \mathbf{1}_{[0,1]}(x)$ is in $L^\infty(\mathbb{R})$ and $L^2(\mathbb{R})$ and $L^1(\mathbb{R})$
- $f(x) = 1/\sqrt{x}$ on $(0,1]$, $0$ elsewhere is in $L^2(\mathbb{R})$ but not $L^\infty(\mathbb{R})$ (unbounded near $0$)
- $f(x) = 1$ for all $x$ is in $L^\infty(\mathbb{R})$ but not $L^1(\mathbb{R})$ (infinite integral)

Thus, inclusion relationships depend on whether the measure space is finite or infinite.

**RL Connection:** In value function approximation, the choice of norm $\|\cdot\|_p$ affects the geometry of the function space:
- **$L^\infty$ norm:** Bellman operators are contractions (uniform convergence)
- **$L^2$ norm:** Least-squares TD minimizes squared error (energy minimization)
- **$L^1$ norm:** Importance sampling ratios must have finite $L^1$ norm (integrability)

The geometric intuition from $\mathbb{R}^2$ extends to infinite-dimensional $L^p$ spaces, where "unit balls" determine convergence properties. □

---

## **Reflection Questions**

1. **Why do we need conjugate exponents?** In Hölder's inequality, why must $1/p + 1/q = 1$? What happens if we try to prove Hölder with non-conjugate exponents (e.g., $p = 2, q = 3$)?

   *Hint:* The conjugacy ensures $1/p + 1/q = 1$ in the final step of the Hölder proof when we use normalized functions. Try setting $p = 2, q = 3$ (so $1/2 + 1/3 = 5/6 \neq 1$) and see where the proof breaks down in Step 4.

2. **Cauchy-Schwarz as a special case.** Show that Hölder with $p = q = 2$ recovers the Cauchy-Schwarz inequality. Why is $L^2$ the only $L^p$ space with an inner product?

   *Hint:* Inner products satisfy the parallelogram law $\|f + g\|^2 + \|f - g\|^2 = 2(\|f\|^2 + \|g\|^2)$. Check if this holds for $\|\cdot\|_p$ when $p \neq 2$ by trying simple examples in $\mathbb{R}^2$.

3. **Minkowski for $p < 1$.** For $0 < p < 1$, the inequality $\|f + g\|_p \geq \|f\|_p + \|g\|_p$ can hold (reverse inequality!) for functions with disjoint support. Why does the proof of Minkowski fail for $p < 1$?

   *Hint:* The proof uses the convexity of $t \mapsto t^p$. For $p < 1$, this function is **concave**, not convex. The inequality $(a+b)^p \leq 2^{p-1}(a^p + b^p)$ fails.

4. **Bellman contraction in $L^\infty$ vs. $L^2$.** The Bellman operator $T^\pi V = R + \gamma P^\pi V$ is a $\gamma$-contraction in $\|\cdot\|_\infty$ (Week 23). Is it also a contraction in $\|\cdot\|_2$?

   *Hint:* Try computing $\|T^\pi V_1 - T^\pi V_2\|_2 = \gamma \|P^\pi (V_1 - V_2)\|_2$. Does $\|P^\pi W\|_2 \leq \|W\|_2$ for all $W$? Consider a 2-state MDP with transition matrix $P^\pi = \begin{pmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{pmatrix}$ and check if $\|P^\pi W\|_2 \leq \|W\|_2$ for general vectors $W$.

---

## **Summary**

**What we accomplished today:**
- Proved **Young's inequality** (pointwise bound for products via weighted AM-GM)
- Proved **Hölder's inequality** (the $L^p$ Cauchy-Schwarz) using normalization + Young + integration
- Proved **Minkowski's inequality** (triangle inequality for $\|\cdot\|_p$) using Hölder
- Applied Hölder correctly to bound importance sampling variance (fourth moments or via boundedness)
- Visualized $L^p$ unit balls in $\mathbb{R}^2$ for $p = 1, 2, \infty$

**Key insights:**
- Conjugate exponents $1/p + 1/q = 1$ encode duality between $L^p$ and $L^q$
- Young's inequality is the pointwise foundation; Hölder integrates it
- Minkowski establishes that $L^p$ is a normed space (enabling functional analysis)
- RL applications: variance bounds (via fourth moments or boundedness), gradient bounds, error decomposition

**Connection to Week 2 Anchor Exercise 3:** Exercise 1 above **is** the anchor exercise for Week 2 (proving Hölder's inequality from the syllabus).

---

**End of Day 4 Exercises**
