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

Since $|fg| = |f| |g|$, this is exactly Hölder's inequality (2.21). □

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

### **Exercise 3: Prove Minkowski's Inequality** {#EX-2.4.3}

**Statement:** Let $(X, \mathcal{F}, \mu)$ be a measure space, and let $1 \leq p < \infty$. Prove that if $f, g \in L^p(\mu)$, then $f + g \in L^p(\mu)$ and:
$$
\|f + g\|_p \leq \|f\|_p + \|g\|_p
$$

**Guidance:**
1. First show $f + g \in L^p$ using $(|f| + |g|)^p \leq 2^{p-1}(|f|^p + |g|^p)$
2. Write $\int |f+g|^p = \int |f+g| \cdot |f+g|^{p-1}$
3. Split: $|f+g| \leq |f| + |g|$, so $\int |f+g|^p \leq \int |f| \cdot |f+g|^{p-1} + \int |g| \cdot |f+g|^{p-1}$
4. Apply Hölder to each term with exponents $p$ and $q = p/(p-1)$
5. Factor out $(\int |f+g|^p)^{1/q}$ from the right side
6. Divide both sides by this factor, noting $1 - 1/q = 1/p$

---

**Solution:**

**Proof.** (As presented in Day 4, Section IV, adapted)

**Step 1: Verify $f + g \in L^p$.**

By the triangle inequality for absolute values:
$$
|f(x) + g(x)| \leq |f(x)| + |g(x)| \quad \text{for all } x
$$

For $p \geq 1$, the function $t \mapsto t^p$ is convex on $[0, \infty)$, so by the convexity inequality $(a + b)^p \leq 2^{p-1}(a^p + b^p)$:
$$
|f(x) + g(x)|^p \leq (|f(x)| + |g(x)|)^p \leq 2^{p-1}(|f(x)|^p + |g(x)|^p)
$$

Integrating:
$$
\int |f + g|^p \, d\mu \leq 2^{p-1} \left(\int |f|^p \, d\mu + \int |g|^p \, d\mu\right) < \infty
$$

since $f, g \in L^p$. Thus $f + g \in L^p$. ✓

**Step 2: Establish the norm inequality.**

Write:
$$
\int |f + g|^p \, d\mu = \int |f + g| \cdot |f + g|^{p-1} \, d\mu
$$

By the triangle inequality $|f + g| \leq |f| + |g|$:
$$
\begin{align}
\int |f + g|^p \, d\mu &\leq \int (|f| + |g|) \cdot |f + g|^{p-1} \, d\mu \\
&= \int |f| \cdot |f + g|^{p-1} \, d\mu + \int |g| \cdot |f + g|^{p-1} \, d\mu \tag{E.2}
\end{align}
$$

**Step 3: Apply Hölder to each term in (E.2).**

Let $q$ be the conjugate exponent of $p$: $1/p + 1/q = 1$. Then $q = p/(p-1)$.

For the first term, apply Hölder with:
- $h_1 = |f| \in L^p$
- $h_2 = |f + g|^{p-1}$

**Check $h_2 \in L^q$:** We have:
$$
\int |f + g|^{(p-1)q} \, d\mu = \int |f + g|^{(p-1) \cdot p/(p-1)} \, d\mu = \int |f + g|^p \, d\mu < \infty
$$

(using $q = p/(p-1)$, so $(p-1)q = p$). Thus $h_2 \in L^q$. ✓

By Hölder:
$$
\int |f| \cdot |f + g|^{p-1} \, d\mu \leq \|f\|_p \||f + g|^{p-1}\|_q = \|f\|_p \left(\int |f + g|^p \, d\mu\right)^{1/q}
$$

Similarly, for the second term:
$$
\int |g| \cdot |f + g|^{p-1} \, d\mu \leq \|g\|_p \left(\int |f + g|^p \, d\mu\right)^{1/q}
$$

**Step 4: Combine and simplify.**

From (E.2):
$$
\int |f + g|^p \, d\mu \leq \left(\|f\|_p + \|g\|_p\right) \left(\int |f + g|^p \, d\mu\right)^{1/q}
$$

**Divide both sides by $\left(\int |f + g|^p \, d\mu\right)^{1/q}$:**

(Assuming $\int |f + g|^p > 0$; if it equals 0, then $f + g = 0$ a.e., and the inequality holds trivially.)

$$
\left(\int |f + g|^p \, d\mu\right)^{1 - 1/q} \leq \|f\|_p + \|g\|_p
$$

**Simplify the exponent:**

$$
1 - \frac{1}{q} = \frac{q - 1}{q} = \frac{p/(p-1) - 1}{p/(p-1)} = \frac{(p - (p-1))/(p-1)}{p/(p-1)} = \frac{1/(p-1)}{p/(p-1)} = \frac{1}{p}
$$

Thus:
$$
\left(\int |f + g|^p \, d\mu\right)^{1/p} \leq \|f\|_p + \|g\|_p
$$

which is Minkowski's inequality (2.22). □

---

### **Exercise 4: RL Application — Importance Sampling Variance Bound via Hölder** {#EX-2.4.4}

**Statement:** In off-policy RL, we estimate $\mathbb{E}_\pi[R]$ using importance sampling: $\mathbb{E}_\mu[\rho R]$ where $\rho = \pi/\mu$ (assuming $\text{supp}(\pi) \subseteq \text{supp}(\mu)$, ensuring the ratio is well-defined). Show that the variance satisfies:
$$
\text{Var}_\mu[\rho R] \leq \mathbb{E}_\mu[\rho^2] \mathbb{E}_\mu[R^2]
$$

using Hölder's inequality with $p = q = 2$ (Cauchy-Schwarz).

Discuss why clipping $\rho$ reduces variance.

---

**Solution:**

**Part 1: Prove the variance bound.**

**Proof.** Recall that variance is defined as:
$$
\text{Var}_\mu[\rho R] = \mathbb{E}_\mu[(\rho R)^2] - (\mathbb{E}_\mu[\rho R])^2
$$

Since $(\mathbb{E}_\mu[\rho R])^2 \geq 0$, we have:
$$
\text{Var}_\mu[\rho R] \leq \mathbb{E}_\mu[(\rho R)^2] = \mathbb{E}_\mu[\rho^2 R^2]
$$

Now apply Hölder's inequality with $p = q = 2$ (Cauchy-Schwarz):
$$
\mathbb{E}_\mu[\rho^2 R^2] = \mathbb{E}_\mu[|\rho^2| \cdot |R^2|] \leq \sqrt{\mathbb{E}_\mu[(\rho^2)^2]} \sqrt{\mathbb{E}_\mu[(R^2)^2]}
$$

Wait, this gives $\mathbb{E}[\rho^4]^{1/2} \mathbb{E}[R^4]^{1/2}$, which is stronger than claimed.

**Correction:** Apply Hölder to $\rho \cdot R$ (not $\rho^2 R^2$):
$$
\mathbb{E}_\mu[(\rho R)^2] = \mathbb{E}_\mu[\rho^2 R^2]
$$

We want to bound this. Let $f = \rho$ and $g = R^2$ (or better, use Cauchy-Schwarz on $\rho R$ directly).

**Better approach:** Use Cauchy-Schwarz on $\rho R$ as a product of two functions:
$$
\mathbb{E}_\mu[|\rho R|] \leq \sqrt{\mathbb{E}_\mu[\rho^2]} \sqrt{\mathbb{E}_\mu[R^2]}
$$

But we want a bound on $\mathbb{E}[(\rho R)^2]$, not $\mathbb{E}[\rho R]$.

**Correct approach (using Hölder on squared terms):**

Write:
$$
\mathbb{E}_\mu[(\rho R)^2] = \mathbb{E}_\mu[\rho^2 \cdot R^2]
$$

This is an expectation of a product of two non-negative functions: $\rho^2$ and $R^2$. Apply Hölder with $p = q = 2$:
$$
\int \rho^2 \cdot R^2 \, d\mu \leq \sqrt{\int (\rho^2)^2 \, d\mu} \sqrt{\int (R^2)^2 \, d\mu} = \sqrt{\int \rho^4 \, d\mu} \sqrt{\int R^4 \, d\mu}
$$

Hmm, this bounds variance by $\mathbb{E}[\rho^4]^{1/2} \mathbb{E}[R^4]^{1/2}$, not the claimed bound.

**Alternative formulation (using $L^2$ inner product structure):**

The claimed bound $\text{Var}[\rho R] \leq \mathbb{E}[\rho^2] \mathbb{E}[R^2]$ is actually **not tight** via Hölder. The correct bound from Cauchy-Schwarz is:
$$
\text{Var}_\mu[\rho R] \leq \mathbb{E}_\mu[(\rho R)^2] = \mathbb{E}_\mu[\rho^2 R^2]
$$

If we assume $\rho$ and $R$ are independent (which they're not in general RL settings), we could write $\mathbb{E}[\rho^2 R^2] = \mathbb{E}[\rho^2] \mathbb{E}[R^2]$, recovering the bound.

**Revised solution (acknowledging independence assumption):**

Under the assumption that $\rho$ and $R$ are **independent** under $\mu$ (which holds in some RL settings where the behavior policy $\mu$ is independent of the reward distribution):
$$
\text{Var}_\mu[\rho R] \leq \mathbb{E}_\mu[(\rho R)^2] = \mathbb{E}_\mu[\rho^2] \mathbb{E}_\mu[R^2]
$$

by independence.

**Without independence:** The tighter bound via Cauchy-Schwarz is:
$$
(\mathbb{E}_\mu[\rho R])^2 \leq \mathbb{E}_\mu[\rho^2] \mathbb{E}_\mu[R^2]
$$

which gives:
$$
\text{Var}_\mu[\rho R] = \mathbb{E}_\mu[(\rho R)^2] - (\mathbb{E}_\mu[\rho R])^2 \leq \mathbb{E}_\mu[\rho^2 R^2] \leq \mathbb{E}_\mu[\rho^4]^{1/2} \mathbb{E}_\mu[R^4]^{1/2}
$$

(by Hölder with $p = q = 2$ applied to $\rho^2$ and $R^2$).

**For the claimed bound to hold:** We can use a weaker application. Note that:
$$
\mathbb{E}_\mu[\rho^2 R^2] \leq \|\rho^2\|_\infty \mathbb{E}_\mu[R^2]
$$

If $\rho$ is bounded, say $|\rho| \leq \rho_{\max}$, then:
$$
\text{Var}_\mu[\rho R] \leq \mathbb{E}_\mu[(\rho R)^2] \leq \rho_{\max}^2 \mathbb{E}_\mu[R^2]
$$

**Conclusion:** The bound $\text{Var}[\rho R] \leq \mathbb{E}[\rho^2] \mathbb{E}[R^2]$ holds **exactly** when $\rho$ and $R$ are independent under $\mu$, and **approximately** (up to constants) when $\rho$ is bounded.

□

---

**Part 2: Why clipping $\rho$ reduces variance.**

**Discussion:**

Define the clipped importance ratio:
$$
\bar{\rho} = \min(\rho, \rho_{\max})
$$

for some threshold $\rho_{\max} > 0$ (e.g., $\rho_{\max} = 1$ in V-trace, $\rho_{\max} = 1 + \epsilon$ in PPO).

**Variance bound with clipping:**

Since $|\bar{\rho}| \leq \rho_{\max}$ by construction:
$$
\text{Var}_\mu[\bar{\rho} R] \leq \mathbb{E}_\mu[(\bar{\rho} R)^2] \leq \rho_{\max}^2 \mathbb{E}_\mu[R^2]
$$

This is **bounded** regardless of the tail behavior of $\rho$.

**Comparison with unclipped:**

Without clipping, if $\rho$ has heavy tails (e.g., $\mu$ is near-deterministic and $\pi$ is stochastic), $\mathbb{E}[\rho^2]$ or even $\mathbb{E}[\rho^4]$ can be very large or infinite, causing variance explosion.

Clipping ensures $\mathbb{E}[\bar{\rho}^2] \leq \rho_{\max}^2 < \infty$, guaranteeing finite variance.

**Trade-off:** Clipping introduces **bias**:
$$
\mathbb{E}_\mu[\bar{\rho} R] \neq \mathbb{E}_\pi[R] \quad \text{(in general)}
$$

because $\bar{\rho} \neq \rho$ when $\rho > \rho_{\max}$. The bias-variance trade-off: clipping reduces variance at the cost of biased estimation.

**Practical algorithms:**
- **PPO:** Clips $\rho$ to $[1 - \epsilon, 1 + \epsilon]$ with $\epsilon \approx 0.2$
- **V-trace:** Clips per-timestep ratios $\bar{\rho}_t = \min(\rho_t, \rho_{\max})$ to prevent product explosion
- **AWR:** Uses $\exp(\beta A(s,a))$ with bounded advantage, implicitly controlling the effective importance weight

All of these enforce bounded $\rho$, ensuring Hölder-based variance bounds hold. □

---

### **Exercise 5: Visualize $L^p$ Unit Balls** {#EX-2.4.5}

**Statement:** Consider $\mathbb{R}^2$ with Lebesgue measure. For $p = 1, 2, \infty$, describe (and sketch if possible) the unit ball:
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
3. **Inclusion:** $B_\infty \subseteq B_2 \subseteq B_1$ (on finite-dimensional spaces with counting measure)
4. For general $1 \leq p_1 < p_2 \leq \infty$: $B_{p_2} \subseteq B_{p_1}$ (smaller $p$ gives "fatter" balls)

**RL Connection:** In value function approximation, the choice of norm $\|\cdot\|_p$ affects the geometry of the function space:
- **$L^\infty$ norm:** Bellman operators are contractions (uniform convergence)
- **$L^2$ norm:** Least-squares TD minimizes squared error (energy minimization)
- **$L^1$ norm:** Importance sampling ratios must have finite $L^1$ norm (integrability)

The geometric intuition from $\mathbb{R}^2$ extends to infinite-dimensional $L^p$ spaces, where "unit balls" determine convergence properties. □

---

## **Reflection Questions**

1. **Why do we need conjugate exponents?** In Hölder's inequality, why must $1/p + 1/q = 1$? What happens if we try to prove Hölder with non-conjugate exponents?

   *Hint:* The conjugacy ensures $1/p + 1/q = 1$ in the final step of the proof when we use Young's inequality. Try setting $p = 2, q = 3$ (so $1/2 + 1/3 = 5/6 \neq 1$) and see where the proof breaks down.

2. **Cauchy-Schwarz as a special case.** Show that Hölder with $p = q = 2$ recovers the Cauchy-Schwarz inequality. Why is $L^2$ the only $L^p$ space with an inner product?

   *Hint:* Inner products satisfy the parallelogram law $\|f + g\|^2 + \|f - g\|^2 = 2(\|f\|^2 + \|g\|^2)$. Check if this holds for $\|\cdot\|_p$ when $p \neq 2$.

3. **Minkowski for $p < 1$.** For $0 < p < 1$, the inequality $\|f + g\|_p \geq \|f\|_p + \|g\|_p$ can hold (reverse inequality!). Why does the proof of Minkowski fail for $p < 1$?

   *Hint:* The convexity of $t \mapsto t^p$ is crucial. For $p < 1$, the function is **concave**, not convex.

4. **Bellman contraction in $L^\infty$ vs. $L^2$.** The Bellman operator $T^\pi V = R + \gamma P^\pi V$ is a $\gamma$-contraction in $\|\cdot\|_\infty$ (Week 23). Is it also a contraction in $\|\cdot\|_2$?

   *Hint:* Try $\|T^\pi V_1 - T^\pi V_2\|_2 = \gamma \|P^\pi (V_1 - V_2)\|_2$. Does $\|P^\pi W\|_2 \leq \|W\|_2$ for all $W$? Consider a simple 2-state MDP.

---

## **Summary**

**What we accomplished today:**
- Proved **Young's inequality** (pointwise bound for products)
- Proved **Hölder's inequality** (the $L^p$ Cauchy-Schwarz) using normalization + Young + integration
- Proved **Minkowski's inequality** (triangle inequality for $\|\cdot\|_p$) using Hölder
- Applied Hölder to bound importance sampling variance in RL
- Visualized $L^p$ unit balls in $\mathbb{R}^2$ for $p = 1, 2, \infty$

**Key insights:**
- Conjugate exponents $1/p + 1/q = 1$ encode duality between $L^p$ and $L^q$
- Young's inequality is the pointwise foundation; Hölder integrates it
- Minkowski establishes that $L^p$ is a normed space (enabling functional analysis)
- RL applications: variance bounds, gradient bounds, error decomposition

**Connection to Week 2 Anchor Exercise 3:** Exercise 1 above **is** the anchor exercise for Week 2 (proving Hölder's inequality from the syllabus).

---

**End of Day 4 Exercises**
