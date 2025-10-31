### 📘 Week 3, Day 2: Exercises on $L^p$ Duality and Riesz Representation

**Companion to:** [[Day_2_revised_math+rl]] — Duality of $L^p$ Spaces

**Total time:** ~40 minutes (part of 90-minute Tuesday session)

**Focus:** Understanding conjugate exponents, dual space structure, and applications to RL (value-distribution duality, importance sampling)

---

## **Exercise Set 3.2: $L^p$ Duality and Riesz Representation**

### **Exercise 3.2.1 (Conjugate Exponent Arithmetic)** {#EX-3.2.1}

**(a)** For each $p \in \{1, 4/3, 3/2, 2, 3, 4, 6, \infty\}$, compute the conjugate exponent $q$ satisfying:
$$
\frac{1}{p} + \frac{1}{q} = 1
$$

**(b)** Verify that the conjugate relation is **symmetric**: if $q$ is conjugate to $p$, then $p$ is conjugate to $q$.

**(c)** Show that for $1 < p < \infty$, the formula $q = p/(p-1)$ is equivalent to $1/p + 1/q = 1$.

**(d)** What happens to $q$ as $p \to 1^+$? As $p \to \infty$?

---

**Solution 3.2.1:**

**(a) Conjugate Exponent Table:**

| $p$ | $q = p/(p-1)$ | Verification $1/p + 1/q$ |
|-----|---------------|--------------------------|
| $1$ | $\infty$ | $1/1 + 1/\infty = 1 + 0 = 1$ ✓ |
| $4/3$ | $4$ | $3/4 + 1/4 = 1$ ✓ |
| $3/2$ | $3$ | $2/3 + 1/3 = 1$ ✓ |
| $2$ | $2$ | $1/2 + 1/2 = 1$ ✓ |
| $3$ | $3/2$ | $1/3 + 2/3 = 1$ ✓ |
| $4$ | $4/3$ | $1/4 + 3/4 = 1$ ✓ |
| $6$ | $6/5$ | $1/6 + 5/6 = 1$ ✓ |
| $\infty$ | $1$ | $0 + 1 = 1$ ✓ |

**Calculation for $p = 4/3$:**
$$
q = \frac{p}{p-1} = \frac{4/3}{4/3 - 1} = \frac{4/3}{1/3} = 4
$$

**Verification:**
$$
\frac{1}{p} + \frac{1}{q} = \frac{3}{4} + \frac{1}{4} = 1 \quad \checkmark
$$

**(b) Symmetry:**

If $1/p + 1/q = 1$, then:
$$
\frac{1}{q} = 1 - \frac{1}{p} \quad \Rightarrow \quad \frac{1}{q} + \frac{1}{p} = 1
$$

Thus the relation is symmetric (commutative addition). □

**(c) Equivalence of Formulas:**

Starting from $1/p + 1/q = 1$, solve for $q$:
$$
\frac{1}{q} = 1 - \frac{1}{p} = \frac{p - 1}{p} \quad \Rightarrow \quad q = \frac{p}{p - 1}
$$

Conversely, if $q = p/(p-1)$, then:
$$
\frac{1}{q} = \frac{p-1}{p} \quad \Rightarrow \quad \frac{1}{p} + \frac{1}{q} = \frac{1}{p} + \frac{p-1}{p} = \frac{1 + p - 1}{p} = 1 \quad \checkmark
$$

**(d) Limiting Behavior:**

- **As $p \to 1^+$:**
  $$
  q = \frac{p}{p-1} = \frac{1 + \epsilon}{\epsilon} \to \infty \quad \text{as } \epsilon \to 0^+
  $$
  (The conjugate of $L^1$ is $L^\infty$.)

- **As $p \to \infty$:**
  $$
  q = \frac{p}{p-1} = \frac{1}{1 - 1/p} \to \frac{1}{1} = 1 \quad \text{as } p \to \infty
  $$
  (The conjugate of $L^\infty$ is $L^1$.)

**Geometric interpretation:** The curve $1/p + 1/q = 1$ in the $(p, q)$-plane is a hyperbola in the first quadrant. The point $(2, 2)$ lies on the line $p = q$ (self-dual case). The endpoints are $(1, \infty)$ and $(\infty, 1)$.

---

### **Exercise 3.2.2 (Verifying Riesz Representation for $L^2$)** {#EX-3.2.2}

Let $(X, \mathcal{F}, \mu)$ be a measure space and $\phi \in (L^2(\mu))^*$ a continuous linear functional.

**(a)** State the Riesz representation theorem for $(L^2)^*$ [THM-3.9 with $p = 2$].

**(b)** Verify that $\phi(f) = \langle f, g \rangle := \int_X f g \, d\mu$ defines a continuous linear functional on $L^2$ for any $g \in L^2$, with $\|\phi\| = \|g\|_2$.

**(c)** **Inner product structure:** Show that $\langle \cdot, \cdot \rangle$ satisfies the properties of an inner product on $L^2$:
   - **Linearity:** $\langle af_1 + bf_2, g \rangle = a\langle f_1, g \rangle + b\langle f_2, g \rangle$ for $a, b \in \mathbb{R}$
   - **Symmetry:** $\langle f, g \rangle = \langle g, f \rangle$
   - **Positive definiteness:** $\langle f, f \rangle \geq 0$, with equality iff $f = 0$ (a.e.)

**(d)** **Cauchy-Schwarz inequality:** Use Hölder's inequality [THM-2.4] to prove:
   $$
   |\langle f, g \rangle| \leq \|f\|_2 \|g\|_2
   $$

---

**Solution 3.2.2:**

**(a) Riesz Representation for $(L^2)^*$:**

By [THM-3.9] with $p = q = 2$ (since $1/2 + 1/2 = 1$), every $\phi \in (L^2)^*$ has the form:
$$
\phi(f) = \int_X f g \, d\mu \quad \text{for some unique } g \in L^2
$$
with $\|\phi\| = \|g\|_2$ (isometric isomorphism). Thus $(L^2)^* \cong L^2$ (self-dual).

**(b) Verification that $\phi(f) = \int fg$ is Continuous:**

**Linearity:** For $f_1, f_2 \in L^2$ and $a, b \in \mathbb{R}$:
$$
\phi(af_1 + bf_2) = \int (af_1 + bf_2)g \, d\mu = a\int f_1 g \, d\mu + b\int f_2 g \, d\mu = a\phi(f_1) + b\phi(f_2)
$$
(by linearity of integration). ✓

**Continuity (boundedness):** By Hölder's inequality with $p = q = 2$ (Cauchy-Schwarz):
$$
|\phi(f)| = \left|\int f g \, d\mu\right| \leq \int |f| |g| \, d\mu \leq \|f\|_2 \|g\|_2
$$

Thus $|\phi(f)| \leq \|g\|_2 \|f\|_2$, so $\phi$ is bounded with $\|\phi\| \leq \|g\|_2$.

**Equality $\|\phi\| = \|g\|_2$:** Take the test function $f = g$ (assuming $g \neq 0$):
$$
\phi(g) = \int g \cdot g \, d\mu = \int |g|^2 \, d\mu = \|g\|_2^2
$$

Thus:
$$
\|\phi\| = \sup_{\|f\|_2 \leq 1} |\phi(f)| \geq \frac{|\phi(g)|}{\|g\|_2} = \frac{\|g\|_2^2}{\|g\|_2} = \|g\|_2
$$

Combined with $\|\phi\| \leq \|g\|_2$, we get $\|\phi\| = \|g\|_2$. ✓

**(c) Inner Product Axioms:**

Define $\langle f, g \rangle = \int fg \, d\mu$.

**(i) Linearity in first argument:**
$$
\langle af_1 + bf_2, g \rangle = \int (af_1 + bf_2)g \, d\mu = a\int f_1 g + b\int f_2 g = a\langle f_1, g \rangle + b\langle f_2, g \rangle \quad \checkmark
$$

**(ii) Symmetry:**
$$
\langle f, g \rangle = \int fg \, d\mu = \int gf \, d\mu = \langle g, f \rangle \quad \text{(commutativity of multiplication)} \quad \checkmark
$$

**(iii) Positive definiteness:**
$$
\langle f, f \rangle = \int f \cdot f \, d\mu = \int |f|^2 \, d\mu = \|f\|_2^2 \geq 0
$$

Equality $\langle f, f \rangle = 0$ holds iff $\int |f|^2 = 0$ iff $f = 0$ $\mu$-almost everywhere (since $|f|^2 \geq 0$ and integration of non-negative function vanishes iff function is zero a.e.). ✓

**Conclusion:** $L^2$ with $\langle \cdot, \cdot \rangle$ is an **inner product space** (Week 14: Hilbert space).

**(d) Cauchy-Schwarz Inequality:**

Apply Hölder's inequality [THM-2.4] with $p = q = 2$:
$$
\int |fg| \, d\mu \leq \|f\|_2 \|g\|_2
$$

Thus:
$$
|\langle f, g \rangle| = \left|\int fg \, d\mu\right| \leq \int |fg| \, d\mu \leq \|f\|_2 \|g\|_2 \quad \checkmark
$$

**Remark:** The Cauchy-Schwarz inequality is the $p = 2$ case of Hölder. In the context of inner product spaces, it's usually stated as:
$$
|\langle x, y \rangle| \leq \|x\| \|y\|
$$
with equality iff $x$ and $y$ are linearly dependent.

---

### **Exercise 3.2.3 (Dual Space of $\ell^p$ Sequences)** {#EX-3.2.3}

Let $\ell^p = \{(x_n)_{n=1}^\infty : \sum_{n=1}^\infty |x_n|^p < \infty\}$ be the space of $p$-summable sequences with norm $\|(x_n)\|_p = \left(\sum |x_n|^p\right)^{1/p}$ for $1 \leq p < \infty$.

**(a)** Show that for $1 < p < \infty$, the dual space $(\ell^p)^*$ is isometrically isomorphic to $\ell^q$ (where $1/p + 1/q = 1$) via the pairing:
$$
\phi_a(x) = \sum_{n=1}^\infty a_n x_n \quad \text{for } a = (a_n) \in \ell^q, \, x = (x_n) \in \ell^p
$$

**(b)** Verify that $\|\phi_a\| = \|a\|_q$ (isometry).

**(c)** **RL Application:** In **tabular RL** with finite state space $\mathcal{S} = \{s_1, \ldots, s_n\}$, the value function is a vector $V = (V_1, \ldots, V_n) \in \mathbb{R}^n = \ell^\infty(\{1, \ldots, n\})$. The reward function $r = (r_1, \ldots, r_n)$ defines a functional $\phi_r(V) = \sum_{i=1}^n r_i V_i$. Show:
   - $\phi_r \in (\ell^\infty)^*$
   - $\|\phi_r\| = \|r\|_1$ (since $(\ell^\infty)^* \cong \ell^1$ for finite spaces)

---

**Solution 3.2.3:**

**(a) Duality $(\ell^p)^* \cong \ell^q$:**

**Step 1: Show $\phi_a$ is well-defined and continuous.**

For $a \in \ell^q$ and $x \in \ell^p$, the series $\sum a_n x_n$ converges absolutely by Hölder's inequality (discrete version):
$$
\sum_{n=1}^\infty |a_n x_n| \leq \left(\sum_{n=1}^\infty |a_n|^q\right)^{1/q} \left(\sum_{n=1}^\infty |x_n|^p\right)^{1/p} = \|a\|_q \|x\|_p < \infty
$$

Thus $\phi_a(x) = \sum a_n x_n$ is well-defined for all $x \in \ell^p$.

**Linearity:**
$$
\phi_a(cx + dy) = \sum a_n(cx_n + dy_n) = c\sum a_n x_n + d\sum a_n y_n = c\phi_a(x) + d\phi_a(y) \quad \checkmark
$$

**Boundedness:** By Hölder:
$$
|\phi_a(x)| \leq \sum |a_n x_n| \leq \|a\|_q \|x\|_p
$$

Thus $\phi_a \in (\ell^p)^*$ with $\|\phi_a\| \leq \|a\|_q$. ✓

**Step 2: Show every $\phi \in (\ell^p)^*$ has this form.**

Let $e^{(k)} = (0, \ldots, 0, 1, 0, \ldots)$ (standard basis vector with $1$ in position $k$). Define:
$$
a_k := \phi(e^{(k)}) \quad \text{for } k = 1, 2, 3, \ldots
$$

For any $x = (x_1, x_2, \ldots) \in \ell^p$, the finite sum $x^{(N)} = \sum_{k=1}^N x_k e^{(k)}$ satisfies $x^{(N)} \to x$ in $\ell^p$ norm (by definition of $\ell^p$). By continuity of $\phi$:
$$
\phi(x) = \phi\left(\lim_{N \to \infty} x^{(N)}\right) = \lim_{N \to \infty} \phi(x^{(N)}) = \lim_{N \to \infty} \sum_{k=1}^N x_k \phi(e^{(k)}) = \sum_{k=1}^\infty x_k a_k
$$

Now we need to show $a = (a_k) \in \ell^q$. Define the test sequence:
$$
y_k = \text{sgn}(a_k) |a_k|^{q-1} \quad \text{for } k = 1, \ldots, N
$$
(truncated to finite support). Then $y \in \ell^p$ (since $|y_k|^p = |a_k|^{p(q-1)} = |a_k|^q$ by conjugate relation $p(q-1) = q$), and:
$$
\phi(y) = \sum_{k=1}^N a_k y_k = \sum_{k=1}^N |a_k|^q
$$

By boundedness of $\phi$:
$$
\left|\sum_{k=1}^N |a_k|^q\right| = |\phi(y)| \leq \|\phi\| \|y\|_p = \|\phi\| \left(\sum_{k=1}^N |a_k|^q\right)^{1/p}
$$

If $\sum_{k=1}^N |a_k|^q > 0$, divide by $\left(\sum |a_k|^q\right)^{1/p}$:
$$
\left(\sum_{k=1}^N |a_k|^q\right)^{1 - 1/p} \leq \|\phi\|
$$

Since $1 - 1/p = 1/q$:
$$
\left(\sum_{k=1}^N |a_k|^q\right)^{1/q} \leq \|\phi\|
$$

Taking $N \to \infty$:
$$
\|a\|_q = \left(\sum_{k=1}^\infty |a_k|^q\right)^{1/q} \leq \|\phi\| < \infty
$$

Thus $a \in \ell^q$. ✓

**(b) Isometry $\|\phi_a\| = \|a\|_q$:**

From Step 1: $|\phi_a(x)| \leq \|a\|_q \|x\|_p$, so $\|\phi_a\| \leq \|a\|_q$.

For the reverse inequality, take the test sequence $x_k = \text{sgn}(a_k) |a_k|^{q-1} / \|a\|_q^{q-1}$ (normalized). Then $\|x\|_p = 1$ (by conjugate relation) and:
$$
\phi_a(x) = \frac{1}{\|a\|_q^{q-1}} \sum_{k=1}^\infty a_k \cdot \text{sgn}(a_k) |a_k|^{q-1} = \frac{1}{\|a\|_q^{q-1}} \sum_{k=1}^\infty |a_k|^q = \frac{\|a\|_q^q}{\|a\|_q^{q-1}} = \|a\|_q
$$

Thus:
$$
\|\phi_a\| = \sup_{\|x\|_p \leq 1} |\phi_a(x)| \geq |\phi_a(x)| = \|a\|_q
$$

Combined with $\|\phi_a\| \leq \|a\|_q$:
$$
\|\phi_a\| = \|a\|_q \quad \checkmark
$$

**(c) RL Application: Finite State Space Duality:**

**Setup:** $\mathcal{S} = \{s_1, \ldots, s_n\}$ (finite state space), $V = (V_1, \ldots, V_n) \in \mathbb{R}^n$, $r = (r_1, \ldots, r_n)$ (reward vector).

Define functional:
$$
\phi_r(V) = \sum_{i=1}^n r_i V_i = r^\top V \quad \text{(inner product in $\mathbb{R}^n$)}
$$

**(i) $\phi_r \in (\ell^\infty)^*$:**

**Linearity:** $\phi_r(aV_1 + bV_2) = r^\top(aV_1 + bV_2) = ar^\top V_1 + br^\top V_2 = a\phi_r(V_1) + b\phi_r(V_2)$ ✓

**Boundedness:** For $V \in \ell^\infty(\{1, \ldots, n\})$ (i.e., $\|V\|_\infty = \max_i |V_i|$):
$$
|\phi_r(V)| = \left|\sum_{i=1}^n r_i V_i\right| \leq \sum_{i=1}^n |r_i| |V_i| \leq \|V\|_\infty \sum_{i=1}^n |r_i| = \|V\|_\infty \|r\|_1
$$

Thus $\phi_r$ is bounded with $\|\phi_r\| \leq \|r\|_1$. ✓

**(ii) $\|\phi_r\| = \|r\|_1$:**

**Equality via test function:** Define $V^* \in \mathbb{R}^n$ by:
$$
V_i^* = \text{sgn}(r_i) = \begin{cases} +1 & \text{if } r_i > 0 \\ 0 & \text{if } r_i = 0 \\ -1 & \text{if } r_i < 0 \end{cases}
$$

Then $\|V^*\|_\infty = 1$ and:
$$
\phi_r(V^*) = \sum_{i=1}^n r_i \cdot \text{sgn}(r_i) = \sum_{i=1}^n |r_i| = \|r\|_1
$$

Thus:
$$
\|\phi_r\| = \sup_{\|V\|_\infty \leq 1} |\phi_r(V)| \geq |\phi_r(V^*)| = \|r\|_1
$$

Combined with $\|\phi_r\| \leq \|r\|_1$:
$$
\|\phi_r\| = \|r\|_1 \quad \checkmark
$$

**Interpretation for RL:**

- **Value function space:** $V \in \ell^\infty(\mathcal{S})$ (bounded values)
- **Reward functional:** $\phi_r(V) = \sum_{s \in \mathcal{S}} r(s) V(s)$ (expected immediate reward)
- **Duality:** $(\ell^\infty)^* \cong \ell^1$ on finite spaces, so rewards $r \in \ell^1$ define functionals on value functions
- **Norm interpretation:** $\|r\|_1 = \sum_s |r(s)|$ is the "total absolute reward," and $\|\phi_r\| = \|r\|_1$ says this is the maximum possible value of $\phi_r$ over unit ball in $\ell^\infty$

**Generalization:** For **infinite state spaces**, $(\ell^\infty)^*$ is larger than $\ell^1$ (see [THM-3.12] in theory file), but the functionals arising in RL (expectations under probability distributions) still lie in $\ell^1$ (or more generally, are given by measures).

---

### **Exercise 3.2.4 (Importance Sampling and Radon-Nikodym Preview)** {#EX-3.2.4}

In **off-policy RL**, we collect data under behavior policy $\mu$ but want to estimate the value function $V^\pi$ under target policy $\pi$. The correction uses **importance sampling ratios**.

**(a)** Let $\mathcal{S}$ be a finite state space with $|\mathcal{S}| = n$. Suppose $\mu$ and $\pi$ are two probability distributions on $\mathcal{S}$ (i.e., $\mu_s, \pi_s \geq 0$ and $\sum_s \mu_s = \sum_s \pi_s = 1$). Define the **importance sampling ratio**:
$$
\rho(s) := \frac{\pi(s)}{\mu(s)} \quad \text{if } \mu(s) > 0
$$
(and $\rho(s) = 0$ if $\mu(s) = 0$ and $\pi(s) = 0$; undefined if $\mu(s) = 0$ but $\pi(s) > 0$).

Show that for any function $f: \mathcal{S} \to \mathbb{R}$:
$$
\mathbb{E}_\pi[f(s)] = \mathbb{E}_\mu[\rho(s) f(s)]
$$
provided $\pi(s) = 0$ whenever $\mu(s) = 0$ (i.e., $\pi \ll \mu$, absolute continuity).

**(b)** **Variance of importance sampling:** Suppose $\mu$ and $\pi$ differ significantly on some states. Show that $\text{Var}_\mu[\rho(s)]$ can be arbitrarily large, explaining why importance sampling has **high variance** in off-policy RL.

**(c)** **Connection to Radon-Nikodym (Day 4 preview):** The ratio $\rho(s) = \pi(s)/\mu(s)$ is the **Radon-Nikodym derivative** $d\pi/d\mu$. On Thursday, we prove the Radon-Nikodym theorem, which characterizes when such a derivative exists (when $\pi \ll \mu$, absolute continuity). Additionally, provide a counterexample showing when the derivative does **not** exist (failure of absolute continuity).

---

**Solution 3.2.4:**

**(a) Importance Sampling Formula:**

**Given:** $\mu$ and $\pi$ are probability distributions on $\mathcal{S}$, and $\pi \ll \mu$ (i.e., $\pi(s) > 0 \Rightarrow \mu(s) > 0$, so $\rho(s) = \pi(s)/\mu(s)$ is well-defined for all $s$ with $\pi(s) > 0$).

**To show:** $\mathbb{E}_\pi[f(s)] = \mathbb{E}_\mu[\rho(s) f(s)]$.

**Proof:**
$$
\begin{align}
\mathbb{E}_\pi[f(s)] &= \sum_{s \in \mathcal{S}} \pi(s) f(s) \\
&= \sum_{s: \mu(s) > 0} \pi(s) f(s) + \sum_{s: \mu(s) = 0} \pi(s) f(s) \\
&= \sum_{s: \mu(s) > 0} \pi(s) f(s) + 0 \quad \text{(since $\pi \ll \mu \Rightarrow \pi(s) = 0$ when $\mu(s) = 0$)} \\
&= \sum_{s: \mu(s) > 0} \frac{\pi(s)}{\mu(s)} \mu(s) f(s) \\
&= \sum_{s \in \mathcal{S}} \rho(s) \mu(s) f(s) \quad \text{(extend sum to all $s$; terms with $\mu(s) = 0$ contribute zero)} \\
&= \mathbb{E}_\mu[\rho(s) f(s)] \quad \checkmark
\end{align}
$$

**Interpretation:** To estimate $\mathbb{E}_\pi[f]$ using samples $s \sim \mu$, compute the empirical average:
$$
\widehat{\mathbb{E}}_\pi[f] = \frac{1}{N} \sum_{i=1}^N \rho(s_i) f(s_i) \quad \text{where } s_i \sim \mu
$$

This is the **off-policy Monte Carlo estimator** (Week 36).

**(b) High Variance of Importance Sampling:**

**Example:** Suppose $|\mathcal{S}| = 2$ with states $\{s_1, s_2\}$. Let:
- $\mu(s_1) = 0.99$, $\mu(s_2) = 0.01$ (behavior policy rarely visits $s_2$)
- $\pi(s_1) = 0.5$, $\pi(s_2) = 0.5$ (target policy visits both equally)

Then:
$$
\rho(s_1) = \frac{0.5}{0.99} \approx 0.505, \quad \rho(s_2) = \frac{0.5}{0.01} = 50
$$

**Mean of $\rho$ under $\mu$:**
$$
\mathbb{E}_\mu[\rho(s)] = \mu(s_1)\rho(s_1) + \mu(s_2)\rho(s_2) = 0.99 \cdot 0.505 + 0.01 \cdot 50 \approx 1.0
$$
(This always equals $1$ since $\sum_s \mu(s) \rho(s) = \sum_s \pi(s) = 1$.)

**Variance of $\rho$ under $\mu$:**
$$
\text{Var}_\mu[\rho] = \mathbb{E}_\mu[\rho^2] - (\mathbb{E}_\mu[\rho])^2
$$

Compute $\mathbb{E}_\mu[\rho^2]$:
$$
\mathbb{E}_\mu[\rho^2] = \mu(s_1)\rho(s_1)^2 + \mu(s_2)\rho(s_2)^2 = 0.99 \cdot (0.505)^2 + 0.01 \cdot (50)^2 \approx 0.25 + 25 = 25.25
$$

Thus:
$$
\text{Var}_\mu[\rho] = 25.25 - 1^2 = 24.25 \quad \text{(very high!)}
$$

**Standard deviation:** $\sigma_\rho = \sqrt{24.25} \approx 4.9$ (larger than the mean!).

**Implication:** Estimating $\mathbb{E}_\pi[f]$ via $\mathbb{E}_\mu[\rho f]$ requires averaging over many samples to reduce variance. For trajectories of length $T$, the cumulative importance weight is:
$$
\rho_{0:T-1} = \prod_{t=0}^{T-1} \rho_t = \prod_{t=0}^{T-1} \frac{\pi(a_t|s_t)}{\mu(a_t|s_t)}
$$

If $\text{Var}[\rho_t] \approx 25$ for each step, then $\text{Var}[\rho_{0:T-1}] \approx 25^T$ (exponential growth!). This is the **curse of horizon** in off-policy RL.

**Variance Reduction Techniques:**
- **Clipping:** $\rho_t^{\text{clip}} = \min(\rho_t, c)$ for some constant $c$ (reduces variance but introduces bias)
- **Truncation:** $\rho_{0:T-1}^{\text{trunc}} = \min(\rho_{0:T-1}, c)$ (less aggressive clipping)
- **Self-normalization:** $\hat{\rho}_t = \rho_t / \left(\sum_{i=1}^N \rho_{t,i}\right)$ (removes bias when $\pi = \mu$ on average)
- **Control variates:** Use baseline $b(s)$ to reduce $\text{Var}[\rho(s)f(s) - b(s)]$

**Modern approach (PPO, TRPO):** Constrain $\pi$ to stay close to $\mu$ via KL divergence penalty $D_{\text{KL}}(\pi \| \mu) \leq \delta$. This ensures $\rho(s,a) \in [1-\epsilon, 1+\epsilon]$ (bounded importance weights), drastically reducing variance.

**(c) Connection to Radon-Nikodym:**

The importance sampling ratio $\rho(s) = \pi(s)/\mu(s)$ is the **Radon-Nikodym derivative** $d\pi/d\mu$. More formally:

**Definition (Discrete Radon-Nikodym):** For probability measures $\pi$ and $\mu$ on finite $\mathcal{S}$, if $\pi \ll \mu$ (i.e., $\pi(A) = 0$ whenever $\mu(A) = 0$ for measurable $A \subseteq \mathcal{S}$), then there exists a function $\rho: \mathcal{S} \to [0, \infty)$ such that:
$$
\pi(A) = \sum_{s \in A} \rho(s) \mu(s) = \mathbb{E}_\mu[\rho(s) \mathbf{1}_A(s)] \quad \text{for all } A \subseteq \mathcal{S}
$$

We write $\rho = d\pi/d\mu$ (density of $\pi$ with respect to $\mu$).

**Theorem (Radon-Nikodym, Discrete Case):** If $\pi \ll \mu$, then $d\pi/d\mu$ exists and is unique $\mu$-almost everywhere.

**Proof (for finite $\mathcal{S}$):** Define $\rho(s) = \pi(s)/\mu(s)$ if $\mu(s) > 0$, and $\rho(s) = 0$ if $\mu(s) = 0$. Then:
$$
\sum_{s \in A} \rho(s) \mu(s) = \sum_{s \in A: \mu(s) > 0} \frac{\pi(s)}{\mu(s)} \mu(s) = \sum_{s \in A: \mu(s) > 0} \pi(s) = \pi(A)
$$
(using $\pi \ll \mu \Rightarrow \pi(s) = 0$ when $\mu(s) = 0$). Uniqueness: if $\rho_1$ and $\rho_2$ both satisfy the above, then $\sum_{s \in \{s_0\}} (\rho_1(s_0) - \rho_2(s_0))\mu(s_0) = 0$ for all $s_0$, so $\rho_1(s_0) = \rho_2(s_0)$ for all $s_0$ with $\mu(s_0) > 0$ (uniqueness $\mu$-a.e.). □

**When does $d\pi/d\mu$ NOT exist?**

The Radon-Nikodym derivative $\rho = d\pi/d\mu$ exists **if and only if** $\pi \ll \mu$ (absolute continuity). If $\pi$ places mass where $\mu$ does not, the derivative is undefined (or infinite).

**Counterexample (finite state space):**
- $\mathcal{S} = \{s_1, s_2, s_3\}$
- $\mu = (0.5, 0.5, 0)$ (behavior policy never visits $s_3$)
- $\pi = (0.4, 0.4, 0.2)$ (target policy visits $s_3$ with probability 0.2)

Then $\pi \not\ll \mu$ (since $\mu(\{s_3\}) = 0$ but $\pi(\{s_3\}) = 0.2 > 0$). The importance sampling ratio:
$$
\rho(s_3) = \frac{\pi(s_3)}{\mu(s_3)} = \frac{0.2}{0} = \text{undefined}
$$

**Practical implication for off-policy RL:** If the behavior policy $\mu$ never visits state $s_3$, we **cannot** use importance sampling to estimate $\mathbb{E}_\pi[f(s_3)]$. The data from $\mu$ provides **no information** about states where $\mu$ has zero mass. This is called the **support mismatch problem** in off-policy learning.

**Solution:** Use **exploration policies** that ensure $\mu(s) > 0$ for all $s$ where $\pi(s) > 0$ (e.g., $\epsilon$-greedy with $\epsilon > 0$, Gaussian noise with full support). This guarantees $\pi \ll \mu$ and thus $d\pi/d\mu$ exists.

**Day 4 Preview:** On Thursday, we generalize this to continuous spaces and prove the Radon-Nikodym theorem: if $\mu \ll \nu$ and both are σ-finite, then $d\mu/d\nu \in L^1(\nu)$ exists and satisfies $\mu(E) = \int_E (d\mu/d\nu) \, d\nu$ for all measurable $E$.

This formalizes the change-of-measure formulas used throughout RL (importance sampling, off-policy evaluation, inverse propensity scoring).

---

### **Exercise 3.2.5 (Actor-Critic as Dual Spaces)** {#EX-3.2.5}

In **actor-critic methods** (Week 37), the **actor** $\pi_\theta$ (policy) induces a state distribution $\mu_\pi$, while the **critic** $V_w$ (value function approximator) lives in a function space. This exercise explores the duality.

**(a)** Let $\mathcal{S}$ be a finite state space with $|\mathcal{S}| = n$. The actor $\pi_\theta$ defines a policy distribution, which induces a **stationary state distribution** $\mu_\pi \in \Delta^{n-1}$ (probability simplex in $\mathbb{R}^n$). The critic is a value function $V_w \in \mathbb{R}^n$ parameterized by $w \in \mathbb{R}^d$ (e.g., $V_w(s) = w^\top \phi(s)$ for features $\phi$).

The **performance objective** is:
$$
J(\theta) = \mathbb{E}_{\mu_\pi}[V_w(s)] = \sum_{s \in \mathcal{S}} \mu_\pi(s) V_w(s) = \langle \mu_\pi, V_w \rangle
$$

Show that this is the **dual pairing** between $\mu_\pi \in (\ell^\infty)^* \cong \ell^1$ (probability distribution) and $V_w \in \ell^\infty$ (value function).

**(b)** **Policy gradient theorem:** The gradient of $J(\theta)$ with respect to $\theta$ is:
$$
\nabla_\theta J(\theta) = \mathbb{E}_{\mu_\pi}\left[\nabla_\theta \log \pi_\theta(a|s) Q^\pi(s,a)\right]
$$

This involves:
- **Actor gradient:** $\nabla_\theta \log \pi_\theta(a|s)$ (score function)
- **Critic evaluation:** $Q^\pi(s,a)$ (action-value function)
- **Integration against $\mu_\pi$:** Expectation under state distribution

Explain why this is a **dual gradient**: the gradient of a functional (pairing with $\mu_\pi$) with respect to the function space variable ($V$ or $Q$).

**(c)** **Natural policy gradient:** The natural gradient replaces the Euclidean gradient $\nabla_\theta J$ with the **Fisher-Rao gradient**:
$$
\tilde{\nabla}_\theta J = F(\theta)^{-1} \nabla_\theta J
$$
where $F(\theta) = \mathbb{E}_{\mu_\pi}[\nabla_\theta \log \pi_\theta(a|s) \nabla_\theta \log \pi_\theta(a|s)^\top]$ is the **Fisher information matrix**.

This uses the **$L^2$ metric** on the policy space (KL divergence geometry). Explain the connection to Riesz representation: the natural gradient is the unique element of $L^2$ that represents the functional gradient (via the $L^2$ inner product).

---

**Solution 3.2.5:**

**(a) Dual Pairing in Actor-Critic:**

**Setup:**
- State space: $\mathcal{S}$ with $|\mathcal{S}| = n$
- State distribution: $\mu_\pi \in \Delta^{n-1} \subset \mathbb{R}^n$ (probability distribution, $\mu_\pi(s) \geq 0$, $\sum_s \mu_\pi(s) = 1$)
- Value function: $V_w \in \mathbb{R}^n$ (bounded, $\|V_w\|_\infty < \infty$)

**Pairing:**
$$
J(\theta) = \langle \mu_\pi, V_w \rangle := \sum_{s \in \mathcal{S}} \mu_\pi(s) V_w(s) = \mathbb{E}_{\mu_\pi}[V_w(s)]
$$

**Duality interpretation:**

1. **Value functions live in $\ell^\infty$:** Since $V_w(s)$ is bounded for all $s$, $V_w \in \ell^\infty(\mathcal{S})$.

2. **State distributions live in $(\ell^\infty)^*$:** The functional $\phi_\mu(V) = \sum_s \mu(s) V(s)$ is continuous on $\ell^\infty$ (by boundedness):
   $$
   |\phi_\mu(V)| = \left|\sum_s \mu(s) V(s)\right| \leq \sum_s \mu(s) |V(s)| \leq \|V\|_\infty \sum_s \mu(s) = \|V\|_\infty
   $$
   (since $\sum_s \mu(s) = 1$). Thus $\phi_\mu \in (\ell^\infty)^*$ with $\|\phi_\mu\| \leq 1$.

3. **Duality $(\ell^\infty)^* \cong \ell^1$:** By [THM-3.11], on finite spaces, $(\ell^\infty)^* \cong \ell^1$ isometrically. Since $\mu$ is a probability distribution, $\mu \in \ell^1$ (in fact, $\|\mu\|_1 = \sum_s |\mu(s)| = \sum_s \mu(s) = 1$ since $\mu \geq 0$).

**Conclusion:** The actor-critic objective $J(\theta) = \langle \mu_\pi, V_w \rangle$ is the **canonical dual pairing** between:
- **Critic** $V_w \in \ell^\infty$ (value function space)
- **Actor-induced distribution** $\mu_\pi \in (\ell^\infty)^*$ (dual space, identified with $\ell^1$ via probability measures)

This duality formalizes why actor-critic methods alternate between:
- **Policy evaluation (critic update):** Estimate $V_w \approx V^\pi$ (element of $\ell^\infty$)
- **Policy improvement (actor update):** Update $\theta$ to maximize $J(\theta) = \langle \mu_\pi, V_w \rangle$ (functional on $\ell^\infty$)

**(b) Policy Gradient as Dual Gradient:**

The **policy gradient theorem** [@sutton:policy_gradient:2000] states:
$$
\nabla_\theta J(\theta) = \mathbb{E}_{\mu_\pi}\left[\nabla_\theta \log \pi_\theta(a|s) Q^\pi(s,a)\right]
$$

**Interpretation as dual gradient:**

1. **$J(\theta)$ is a functional:** $J: \Theta \to \mathbb{R}$ where $\Theta$ is the policy parameter space. For fixed $\theta$, $J(\theta) = \langle \mu_\pi, V_w \rangle$ is a **linear functional** on the value function space $V_w$.

2. **Gradient via chain rule:** The gradient $\nabla_\theta J$ involves:
   $$
   \nabla_\theta J(\theta) = \nabla_\theta \langle \mu_\pi, V^\pi \rangle = \langle \nabla_\theta \mu_\pi, V^\pi \rangle + \langle \mu_\pi, \nabla_\theta V^\pi \rangle
   $$
   (ignoring the second term, which vanishes for discounted MDPs by envelope theorem; see [@sutton:policy_gradient:2000, Theorem 1]).

3. **First term:** $\langle \nabla_\theta \mu_\pi, V^\pi \rangle$ involves the gradient of the state distribution $\mu_\pi$ (which depends on $\theta$). By the policy gradient theorem, this equals:
   $$
   \mathbb{E}_{\mu_\pi}[\nabla_\theta \log \pi_\theta(a|s) Q^\pi(s,a)]
   $$
   (This is nontrivial and requires the Markov property; see [@sutton:policy_gradient:2000] for proof.)

**Why "dual gradient"?**

- The gradient $\nabla_\theta J$ is computed by integrating $\nabla_\theta \log \pi_\theta$ (score function) **against the value function** $Q^\pi$
- The integration is weighted by $\mu_\pi$ (state distribution in the dual space)
- This is a **Gâteaux derivative** of the functional $J$ with respect to the function $V$ (in the direction of the gradient)

**Practical implication:** Actor-critic methods approximate $\nabla_\theta J$ using:
$$
\nabla_\theta J \approx \frac{1}{N} \sum_{i=1}^N \nabla_\theta \log \pi_\theta(a_i|s_i) Q_w(s_i, a_i)
$$
where samples $(s_i, a_i)$ are drawn from $\mu_\pi$ (on-policy) or corrected via importance sampling (off-policy).

**(c) Natural Policy Gradient and Riesz Representation:**

The **natural policy gradient** [@kakade:natural_policy_gradient:2002; @amari:natural_gradient:1998] replaces the Euclidean gradient $\nabla_\theta J$ with the **Fisher-Rao gradient**:
$$
\tilde{\nabla}_\theta J = F(\theta)^{-1} \nabla_\theta J
$$
where the **Fisher information matrix** is:
$$
F(\theta)_{ij} = \mathbb{E}_{s \sim d_\pi, a \sim \pi_\theta}\left[\frac{\partial \log \pi_\theta(a|s)}{\partial \theta_i} \frac{\partial \log \pi_\theta(a|s)}{\partial \theta_j}\right]
$$

**Connection to Riesz representation:** The Fisher metric defines an **$L^2$ inner product** on the space of score functions $\nabla_\theta \log \pi_\theta(a|s)$:
$$
\langle u, v \rangle_F = \mathbb{E}_{d_\pi}[u(s,a)^\top v(s,a)]
$$
By Riesz representation [THM-3.9], every continuous linear functional $\phi \in (L^2)^*$ corresponds to a unique $g \in L^2$ via $\phi(u) = \langle u, g \rangle_F$. The natural gradient $\tilde{\nabla}_\theta J$ is this unique element: it satisfies:
$$
\langle u, \tilde{\nabla}_\theta J \rangle_F = \langle u, \nabla_\theta J \rangle_{\text{Euclidean}} \quad \text{for all } u
$$
(i.e., $F \tilde{\nabla} J = \nabla J$, hence $\tilde{\nabla} J = F^{-1} \nabla J$).

**Why natural gradients work:**
- **Coordinate-free:** Invariant to reparameterization $\theta \to \phi(\theta)$ (geometric, not algebraic)
- **Trust region:** Step $\theta + \alpha \tilde{\nabla} J$ satisfies $D_{\text{KL}}(\pi_{\theta'} \| \pi_\theta) \approx \frac{\alpha^2}{2} \|\tilde{\nabla} J\|_F^2$ (second-order KL approximation)
- **Steepest ascent:** Maximizes $J$ locally in the Fisher metric (Riemannian geometry)

**Practical challenges:**

1. **Singular Fisher matrix:** If $\pi_\theta$ is deterministic, $F$ has rank $<d$ (not invertible). Solution: Add entropy regularization $H[\pi_\theta(·|s)]$ to ensure stochasticity.

2. **Computational cost:** Exact natural gradient requires:
   - Computing $F$ (requires $O(d^2)$ samples to estimate, $O(d^3)$ to invert)
   - For neural nets with $d = 10^6$ parameters, this is intractable

3. **Modern approximations:**
   - **TRPO** [@schulman:trpo:2015]: Approximate $F^{-1} \nabla J$ via conjugate gradient (CG) without forming $F$ explicitly. Requires only Hessian-vector products $F v$ (computable via automatic differentiation in $O(d)$ time). Typical: 10-20 CG iterations, total cost $O(20d)$ instead of $O(d^3)$.
   - **PPO** [@schulman:ppo:2017]: Avoid natural gradient entirely; instead clip $\rho_t = \pi_{\theta'}/\pi_\theta$ to $[1-\epsilon, 1+\epsilon]$ (ensures KL stays bounded without computing Fisher). Simpler, nearly as effective.
   - **K-FAC** [@martens:kfac:2015]: Approximate $F$ via Kronecker factorization (block-diagonal structure); reduces inversion to $O(d^{3/2})$ or $O(d \log d)$ depending on architecture.

**When theory breaks:** For **neural network policies**, the Fisher information may be:
- **Ill-conditioned** (large condition number $\kappa(F) \gg 1$; CG converges slowly)
- **Non-stationary** (Fisher changes rapidly during training; preconditioning stale)
- **Empirically approximate** (sample estimates $\hat{F}$ from mini-batches have high variance)

Despite these issues, TRPO/PPO work well in practice by combining:
- Approximate natural gradient (CG, clipping)
- Conservative step sizes (KL constraint, clip threshold)
- Large replay buffers (stabilize Fisher estimates)

**Conclusion:** The natural gradient is a beautiful application of Riesz duality ($L^2$ inner product → unique dual element), but **practical RL requires approximations** that trade mathematical rigor for computational tractability.

---

### **Reflection Questions:**

1. **Why does $(L^2)^* \cong L^2$ (self-duality) make $L^2$ special for least-squares methods?**
   *Hint:* Self-duality means inner product structure $\langle f, g \rangle = \int fg$ is symmetric. The projection $\Pi V$ onto a subspace minimizes $\|V - \Pi V\|_2$, which is the least-squares objective. Other $L^p$ spaces ($p \neq 2$) don't have this symmetry.

2. **What goes wrong with $(L^\infty)^*$ in off-policy RL?**
   *Hint:* $(L^\infty)^* \supsetneq L^1$ (strict containment; see [THM-3.12]). Not all functionals on $L^\infty$ correspond to probability measures. However, the functionals we care about in RL (expectations $\mathbb{E}_\mu[V]$) **do** lie in $L^1$, so this isn't a problem in practice.

3. **How does duality explain why policy gradients integrate against state distributions?**
   *Hint:* The objective $J(\theta) = \langle \mu_\pi, V^\pi \rangle$ is a pairing between dual spaces. The gradient $\nabla_\theta J$ involves $\nabla_\theta \mu_\pi$ (derivative of distribution), which appears as integration $\mathbb{E}_{\mu_\pi}[\cdots]$ in the policy gradient formula.

---

**Summary:**

**What we learned:**
- Conjugate exponents $1/p + 1/q = 1$ characterize duality between $L^p$ and $L^q$
- Riesz representation [THM-3.9]: $(L^p)^* \cong L^q$ for $1 < p < \infty$ via $\phi(f) = \int fg \, d\mu$
- Special cases: $(L^2)^* \cong L^2$ (self-dual), $(L^1)^* \cong L^\infty$ (on σ-finite spaces)
- RL applications:
  - Value functions (critic) and state distributions (actor) are dual
  - Importance sampling ratios $\pi/\mu$ are Radon-Nikodym derivatives (Day 4)
  - Least-squares TD uses $L^2$ projection (Week 14 Hilbert spaces)
  - Natural policy gradient uses Fisher metric ($L^2$ inner product on score functions)

**Time allocation:** ~40 minutes (exercises are part of 90-minute Tuesday session; ~40 min reading + ~40 min exercises from main file + ~10 min reflection)

---

**End of Exercises**
### 📘 Week 3, Day 2: Exercises on $L^p$ Duality and Riesz Representation

**Companion to:** [[Day_2_revised_math+rl]] — Duality of $L^p$ Spaces

**Total time:** ~40 minutes (part of 90-minute Tuesday session)

**Focus:** Understanding conjugate exponents, dual space structure, and applications to RL (value-distribution duality, importance sampling)

---

## **Exercise Set 3.2: $L^p$ Duality and Riesz Representation**

### **Exercise 3.2.1 (Conjugate Exponent Arithmetic)** {#EX-3.2.1}

**(a)** For each $p \in \{1, 4/3, 3/2, 2, 3, 4, 6, \infty\}$, compute the conjugate exponent $q$ satisfying:
$$
\frac{1}{p} + \frac{1}{q} = 1
$$

**(b)** Verify that the conjugate relation is **symmetric**: if $q$ is conjugate to $p$, then $p$ is conjugate to $q$.

**(c)** Show that for $1 < p < \infty$, the formula $q = p/(p-1)$ is equivalent to $1/p + 1/q = 1$.

**(d)** What happens to $q$ as $p \to 1^+$? As $p \to \infty$?

---

**Solution 3.2.1:**

**(a) Conjugate Exponent Table:**

| $p$ | $q = p/(p-1)$ | Verification $1/p + 1/q$ |
|-----|---------------|--------------------------|
| $1$ | $\infty$ | $1/1 + 1/\infty = 1 + 0 = 1$ ✓ |
| $4/3$ | $4$ | $3/4 + 1/4 = 1$ ✓ |
| $3/2$ | $3$ | $2/3 + 1/3 = 1$ ✓ |
| $2$ | $2$ | $1/2 + 1/2 = 1$ ✓ |
| $3$ | $3/2$ | $1/3 + 2/3 = 1$ ✓ |
| $4$ | $4/3$ | $1/4 + 3/4 = 1$ ✓ |
| $6$ | $6/5$ | $1/6 + 5/6 = 1$ ✓ |
| $\infty$ | $1$ | $0 + 1 = 1$ ✓ |

**Calculation for $p = 4/3$:**
$$
q = \frac{p}{p-1} = \frac{4/3}{4/3 - 1} = \frac{4/3}{1/3} = 4
$$

**Verification:**
$$
\frac{1}{p} + \frac{1}{q} = \frac{3}{4} + \frac{1}{4} = 1 \quad \checkmark
$$

**(b) Symmetry:**

If $1/p + 1/q = 1$, then:
$$
\frac{1}{q} = 1 - \frac{1}{p} \quad \Rightarrow \quad \frac{1}{q} + \frac{1}{p} = 1
$$

Thus the relation is symmetric (commutative addition). □

**(c) Equivalence of Formulas:**

Starting from $1/p + 1/q = 1$, solve for $q$:
$$
\frac{1}{q} = 1 - \frac{1}{p} = \frac{p - 1}{p} \quad \Rightarrow \quad q = \frac{p}{p - 1}
$$

Conversely, if $q = p/(p-1)$, then:
$$
\frac{1}{q} = \frac{p-1}{p} \quad \Rightarrow \quad \frac{1}{p} + \frac{1}{q} = \frac{1}{p} + \frac{p-1}{p} = \frac{1 + p - 1}{p} = 1 \quad \checkmark
$$

**(d) Limiting Behavior:**

- **As $p \to 1^+$:**
  $$
  q = \frac{p}{p-1} = \frac{1 + \epsilon}{\epsilon} \to \infty \quad \text{as } \epsilon \to 0^+
  $$
  (The conjugate of $L^1$ is $L^\infty$.)

- **As $p \to \infty$:**
  $$
  q = \frac{p}{p-1} = \frac{1}{1 - 1/p} \to \frac{1}{1} = 1 \quad \text{as } p \to \infty
  $$
  (The conjugate of $L^\infty$ is $L^1$.)

**Geometric interpretation:** The curve $1/p + 1/q = 1$ in the $(p, q)$-plane is a hyperbola in the first quadrant. The point $(2, 2)$ lies on the line $p = q$ (self-dual case). The endpoints are $(1, \infty)$ and $(\infty, 1)$.

---

### **Exercise 3.2.2 (Verifying Riesz Representation for $L^2$)** {#EX-3.2.2}

Let $(X, \mathcal{F}, \mu)$ be a measure space and $\phi \in (L^2(\mu))^*$ a continuous linear functional.

**(a)** State the Riesz representation theorem for $(L^2)^*$ [THM-3.9 with $p = 2$].

**(b)** Verify that $\phi(f) = \langle f, g \rangle := \int_X f g \, d\mu$ defines a continuous linear functional on $L^2$ for any $g \in L^2$, with $\|\phi\| = \|g\|_2$.

**(c)** **Inner product structure:** Show that $\langle \cdot, \cdot \rangle$ satisfies the properties of an inner product on $L^2$:
   - **Linearity:** $\langle af_1 + bf_2, g \rangle = a\langle f_1, g \rangle + b\langle f_2, g \rangle$ for $a, b \in \mathbb{R}$
   - **Symmetry:** $\langle f, g \rangle = \langle g, f \rangle$
   - **Positive definiteness:** $\langle f, f \rangle \geq 0$, with equality iff $f = 0$ (a.e.)

**(d)** **Cauchy-Schwarz inequality:** Use Hölder's inequality [THM-2.4] to prove:
   $$
   |\langle f, g \rangle| \leq \|f\|_2 \|g\|_2
   $$

---

**Solution 3.2.2:**

**(a) Riesz Representation for $(L^2)^*$:**

By [THM-3.9] with $p = q = 2$ (since $1/2 + 1/2 = 1$), every $\phi \in (L^2)^*$ has the form:
$$
\phi(f) = \int_X f g \, d\mu \quad \text{for some unique } g \in L^2
$$
with $\|\phi\| = \|g\|_2$ (isometric isomorphism). Thus $(L^2)^* \cong L^2$ (self-dual).

**(b) Verification that $\phi(f) = \int fg$ is Continuous:**

**Linearity:** For $f_1, f_2 \in L^2$ and $a, b \in \mathbb{R}$:
$$
\phi(af_1 + bf_2) = \int (af_1 + bf_2)g \, d\mu = a\int f_1 g \, d\mu + b\int f_2 g \, d\mu = a\phi(f_1) + b\phi(f_2)
$$
(by linearity of integration). ✓

**Continuity (boundedness):** By Hölder's inequality with $p = q = 2$ (Cauchy-Schwarz):
$$
|\phi(f)| = \left|\int f g \, d\mu\right| \leq \int |f| |g| \, d\mu \leq \|f\|_2 \|g\|_2
$$

Thus $|\phi(f)| \leq \|g\|_2 \|f\|_2$, so $\phi$ is bounded with $\|\phi\| \leq \|g\|_2$.

**Equality $\|\phi\| = \|g\|_2$:** Take the test function $f = g$ (assuming $g \neq 0$):
$$
\phi(g) = \int g \cdot g \, d\mu = \int |g|^2 \, d\mu = \|g\|_2^2
$$

Thus:
$$
\|\phi\| = \sup_{\|f\|_2 \leq 1} |\phi(f)| \geq \frac{|\phi(g)|}{\|g\|_2} = \frac{\|g\|_2^2}{\|g\|_2} = \|g\|_2
$$

Combined with $\|\phi\| \leq \|g\|_2$, we get $\|\phi\| = \|g\|_2$. ✓

**(c) Inner Product Axioms:**

Define $\langle f, g \rangle = \int fg \, d\mu$.

**(i) Linearity in first argument:**
$$
\langle af_1 + bf_2, g \rangle = \int (af_1 + bf_2)g \, d\mu = a\int f_1 g + b\int f_2 g = a\langle f_1, g \rangle + b\langle f_2, g \rangle \quad \checkmark
$$

**(ii) Symmetry:**
$$
\langle f, g \rangle = \int fg \, d\mu = \int gf \, d\mu = \langle g, f \rangle \quad \text{(commutativity of multiplication)} \quad \checkmark
$$

**(iii) Positive definiteness:**
$$
\langle f, f \rangle = \int f \cdot f \, d\mu = \int |f|^2 \, d\mu = \|f\|_2^2 \geq 0
$$

Equality $\langle f, f \rangle = 0$ holds iff $\int |f|^2 = 0$ iff $f = 0$ $\mu$-almost everywhere (since $|f|^2 \geq 0$ and integration of non-negative function vanishes iff function is zero a.e.). ✓

**Conclusion:** $L^2$ with $\langle \cdot, \cdot \rangle$ is an **inner product space** (Week 14: Hilbert space).

**(d) Cauchy-Schwarz Inequality:**

Apply Hölder's inequality [THM-2.4] with $p = q = 2$:
$$
\int |fg| \, d\mu \leq \|f\|_2 \|g\|_2
$$

Thus:
$$
|\langle f, g \rangle| = \left|\int fg \, d\mu\right| \leq \int |fg| \, d\mu \leq \|f\|_2 \|g\|_2 \quad \checkmark
$$

**Remark:** The Cauchy-Schwarz inequality is the $p = 2$ case of Hölder. In the context of inner product spaces, it's usually stated as:
$$
|\langle x, y \rangle| \leq \|x\| \|y\|
$$
with equality iff $x$ and $y$ are linearly dependent.

---

### **Exercise 3.2.3 (Dual Space of $\ell^p$ Sequences)** {#EX-3.2.3}

Let $\ell^p = \{(x_n)_{n=1}^\infty : \sum_{n=1}^\infty |x_n|^p < \infty\}$ be the space of $p$-summable sequences with norm $\|(x_n)\|_p = \left(\sum |x_n|^p\right)^{1/p}$ for $1 \leq p < \infty$.

**(a)** Show that for $1 < p < \infty$, the dual space $(\ell^p)^*$ is isometrically isomorphic to $\ell^q$ (where $1/p + 1/q = 1$) via the pairing:
$$
\phi_a(x) = \sum_{n=1}^\infty a_n x_n \quad \text{for } a = (a_n) \in \ell^q, \, x = (x_n) \in \ell^p
$$

**(b)** Verify that $\|\phi_a\| = \|a\|_q$ (isometry).

**(c)** **RL Application:** In **tabular RL** with finite state space $\mathcal{S} = \{s_1, \ldots, s_n\}$, the value function is a vector $V = (V_1, \ldots, V_n) \in \mathbb{R}^n = \ell^\infty(\{1, \ldots, n\})$. The reward function $r = (r_1, \ldots, r_n)$ defines a functional $\phi_r(V) = \sum_{i=1}^n r_i V_i$. Show:
   - $\phi_r \in (\ell^\infty)^*$
   - $\|\phi_r\| = \|r\|_1$ (since $(\ell^\infty)^* \cong \ell^1$ for finite spaces)

---

**Solution 3.2.3:**

**(a) Duality $(\ell^p)^* \cong \ell^q$:**

**Step 1: Show $\phi_a$ is well-defined and continuous.**

For $a \in \ell^q$ and $x \in \ell^p$, the series $\sum a_n x_n$ converges absolutely by Hölder's inequality (discrete version):
$$
\sum_{n=1}^\infty |a_n x_n| \leq \left(\sum_{n=1}^\infty |a_n|^q\right)^{1/q} \left(\sum_{n=1}^\infty |x_n|^p\right)^{1/p} = \|a\|_q \|x\|_p < \infty
$$

Thus $\phi_a(x) = \sum a_n x_n$ is well-defined for all $x \in \ell^p$.

**Linearity:**
$$
\phi_a(cx + dy) = \sum a_n(cx_n + dy_n) = c\sum a_n x_n + d\sum a_n y_n = c\phi_a(x) + d\phi_a(y) \quad \checkmark
$$

**Boundedness:** By Hölder:
$$
|\phi_a(x)| \leq \sum |a_n x_n| \leq \|a\|_q \|x\|_p
$$

Thus $\phi_a \in (\ell^p)^*$ with $\|\phi_a\| \leq \|a\|_q$. ✓

**Step 2: Show every $\phi \in (\ell^p)^*$ has this form.**

Let $e^{(k)} = (0, \ldots, 0, 1, 0, \ldots)$ (standard basis vector with $1$ in position $k$). Define:
$$
a_k := \phi(e^{(k)}) \quad \text{for } k = 1, 2, 3, \ldots
$$

For any $x = (x_1, x_2, \ldots) \in \ell^p$, the finite sum $x^{(N)} = \sum_{k=1}^N x_k e^{(k)}$ satisfies $x^{(N)} \to x$ in $\ell^p$ norm (by definition of $\ell^p$). By continuity of $\phi$:
$$
\phi(x) = \phi\left(\lim_{N \to \infty} x^{(N)}\right) = \lim_{N \to \infty} \phi(x^{(N)}) = \lim_{N \to \infty} \sum_{k=1}^N x_k \phi(e^{(k)}) = \sum_{k=1}^\infty x_k a_k
$$

Now we need to show $a = (a_k) \in \ell^q$. Define the test sequence:
$$
y_k = \text{sgn}(a_k) |a_k|^{q-1} \quad \text{for } k = 1, \ldots, N
$$
(truncated to finite support). Then $y \in \ell^p$ (since $|y_k|^p = |a_k|^{p(q-1)} = |a_k|^q$ by conjugate relation $p(q-1) = q$), and:
$$
\phi(y) = \sum_{k=1}^N a_k y_k = \sum_{k=1}^N |a_k|^q
$$

By boundedness of $\phi$:
$$
\left|\sum_{k=1}^N |a_k|^q\right| = |\phi(y)| \leq \|\phi\| \|y\|_p = \|\phi\| \left(\sum_{k=1}^N |a_k|^q\right)^{1/p}
$$

If $\sum_{k=1}^N |a_k|^q > 0$, divide by $\left(\sum |a_k|^q\right)^{1/p}$:
$$
\left(\sum_{k=1}^N |a_k|^q\right)^{1 - 1/p} \leq \|\phi\|
$$

Since $1 - 1/p = 1/q$:
$$
\left(\sum_{k=1}^N |a_k|^q\right)^{1/q} \leq \|\phi\|
$$

Taking $N \to \infty$:
$$
\|a\|_q = \left(\sum_{k=1}^\infty |a_k|^q\right)^{1/q} \leq \|\phi\| < \infty
$$

Thus $a \in \ell^q$. ✓

**(b) Isometry $\|\phi_a\| = \|a\|_q$:**

From Step 1: $|\phi_a(x)| \leq \|a\|_q \|x\|_p$, so $\|\phi_a\| \leq \|a\|_q$.

For the reverse inequality, take the test sequence $x_k = \text{sgn}(a_k) |a_k|^{q-1} / \|a\|_q^{q-1}$ (normalized). Then $\|x\|_p = 1$ (by conjugate relation) and:
$$
\phi_a(x) = \frac{1}{\|a\|_q^{q-1}} \sum_{k=1}^\infty a_k \cdot \text{sgn}(a_k) |a_k|^{q-1} = \frac{1}{\|a\|_q^{q-1}} \sum_{k=1}^\infty |a_k|^q = \frac{\|a\|_q^q}{\|a\|_q^{q-1}} = \|a\|_q
$$

Thus:
$$
\|\phi_a\| = \sup_{\|x\|_p \leq 1} |\phi_a(x)| \geq |\phi_a(x)| = \|a\|_q
$$

Combined with $\|\phi_a\| \leq \|a\|_q$:
$$
\|\phi_a\| = \|a\|_q \quad \checkmark
$$

**(c) RL Application: Finite State Space Duality:**

**Setup:** $\mathcal{S} = \{s_1, \ldots, s_n\}$ (finite state space), $V = (V_1, \ldots, V_n) \in \mathbb{R}^n$, $r = (r_1, \ldots, r_n)$ (reward vector).

Define functional:
$$
\phi_r(V) = \sum_{i=1}^n r_i V_i = r^\top V \quad \text{(inner product in $\mathbb{R}^n$)}
$$

**(i) $\phi_r \in (\ell^\infty)^*$:**

**Linearity:** $\phi_r(aV_1 + bV_2) = r^\top(aV_1 + bV_2) = ar^\top V_1 + br^\top V_2 = a\phi_r(V_1) + b\phi_r(V_2)$ ✓

**Boundedness:** For $V \in \ell^\infty(\{1, \ldots, n\})$ (i.e., $\|V\|_\infty = \max_i |V_i|$):
$$
|\phi_r(V)| = \left|\sum_{i=1}^n r_i V_i\right| \leq \sum_{i=1}^n |r_i| |V_i| \leq \|V\|_\infty \sum_{i=1}^n |r_i| = \|V\|_\infty \|r\|_1
$$

Thus $\phi_r$ is bounded with $\|\phi_r\| \leq \|r\|_1$. ✓

**(ii) $\|\phi_r\| = \|r\|_1$:**

**Equality via test function:** Define $V^* \in \mathbb{R}^n$ by:
$$
V_i^* = \text{sgn}(r_i) = \begin{cases} +1 & \text{if } r_i > 0 \\ 0 & \text{if } r_i = 0 \\ -1 & \text{if } r_i < 0 \end{cases}
$$

Then $\|V^*\|_\infty = 1$ and:
$$
\phi_r(V^*) = \sum_{i=1}^n r_i \cdot \text{sgn}(r_i) = \sum_{i=1}^n |r_i| = \|r\|_1
$$

Thus:
$$
\|\phi_r\| = \sup_{\|V\|_\infty \leq 1} |\phi_r(V)| \geq |\phi_r(V^*)| = \|r\|_1
$$

Combined with $\|\phi_r\| \leq \|r\|_1$:
$$
\|\phi_r\| = \|r\|_1 \quad \checkmark
$$

**Interpretation for RL:**

- **Value function space:** $V \in \ell^\infty(\mathcal{S})$ (bounded values)
- **Reward functional:** $\phi_r(V) = \sum_{s \in \mathcal{S}} r(s) V(s)$ (expected immediate reward)
- **Duality:** $(\ell^\infty)^* \cong \ell^1$ on finite spaces, so rewards $r \in \ell^1$ define functionals on value functions
- **Norm interpretation:** $\|r\|_1 = \sum_s |r(s)|$ is the "total absolute reward," and $\|\phi_r\| = \|r\|_1$ says this is the maximum possible value of $\phi_r$ over unit ball in $\ell^\infty$

**Generalization:** For **infinite state spaces**, $(\ell^\infty)^*$ is larger than $\ell^1$ (see [THM-3.12] in theory file), but the functionals arising in RL (expectations under probability distributions) still lie in $\ell^1$ (or more generally, are given by measures).

---

### **Exercise 3.2.4 (Importance Sampling and Radon-Nikodym Preview)** {#EX-3.2.4}

In **off-policy RL**, we collect data under behavior policy $\mu$ but want to estimate the value function $V^\pi$ under target policy $\pi$. The correction uses **importance sampling ratios**.

**(a)** Let $\mathcal{S}$ be a finite state space with $|\mathcal{S}| = n$. Suppose $\mu$ and $\pi$ are two probability distributions on $\mathcal{S}$ (i.e., $\mu_s, \pi_s \geq 0$ and $\sum_s \mu_s = \sum_s \pi_s = 1$). Define the **importance sampling ratio**:
$$
\rho(s) := \frac{\pi(s)}{\mu(s)} \quad \text{if } \mu(s) > 0
$$
(and $\rho(s) = 0$ if $\mu(s) = 0$ and $\pi(s) = 0$; undefined if $\mu(s) = 0$ but $\pi(s) > 0$).

Show that for any function $f: \mathcal{S} \to \mathbb{R}$:
$$
\mathbb{E}_\pi[f(s)] = \mathbb{E}_\mu[\rho(s) f(s)]
$$
provided $\pi(s) = 0$ whenever $\mu(s) = 0$ (i.e., $\pi \ll \mu$, absolute continuity).

**(b)** **Variance of importance sampling:** Suppose $\mu$ and $\pi$ differ significantly on some states. Show that $\text{Var}_\mu[\rho(s)]$ can be arbitrarily large, explaining why importance sampling has **high variance** in off-policy RL.

**(c)** **Connection to Radon-Nikodym (Day 4 preview):** The ratio $\rho(s) = \pi(s)/\mu(s)$ is the **Radon-Nikodym derivative** $d\pi/d\mu$. On Thursday, we prove the Radon-Nikodym theorem, which characterizes when such a derivative exists (when $\pi \ll \mu$, absolute continuity). Additionally, provide a counterexample showing when the derivative does **not** exist (failure of absolute continuity).

---

**Solution 3.2.4:**

**(a) Importance Sampling Formula:**

**Given:** $\mu$ and $\pi$ are probability distributions on $\mathcal{S}$, and $\pi \ll \mu$ (i.e., $\pi(s) > 0 \Rightarrow \mu(s) > 0$, so $\rho(s) = \pi(s)/\mu(s)$ is well-defined for all $s$ with $\pi(s) > 0$).

**To show:** $\mathbb{E}_\pi[f(s)] = \mathbb{E}_\mu[\rho(s) f(s)]$.

**Proof:**
$$
\begin{align}
\mathbb{E}_\pi[f(s)] &= \sum_{s \in \mathcal{S}} \pi(s) f(s) \\
&= \sum_{s: \mu(s) > 0} \pi(s) f(s) + \sum_{s: \mu(s) = 0} \pi(s) f(s) \\
&= \sum_{s: \mu(s) > 0} \pi(s) f(s) + 0 \quad \text{(since $\pi \ll \mu \Rightarrow \pi(s) = 0$ when $\mu(s) = 0$)} \\
&= \sum_{s: \mu(s) > 0} \frac{\pi(s)}{\mu(s)} \mu(s) f(s) \\
&= \sum_{s \in \mathcal{S}} \rho(s) \mu(s) f(s) \quad \text{(extend sum to all $s$; terms with $\mu(s) = 0$ contribute zero)} \\
&= \mathbb{E}_\mu[\rho(s) f(s)] \quad \checkmark
\end{align}
$$

**Interpretation:** To estimate $\mathbb{E}_\pi[f]$ using samples $s \sim \mu$, compute the empirical average:
$$
\widehat{\mathbb{E}}_\pi[f] = \frac{1}{N} \sum_{i=1}^N \rho(s_i) f(s_i) \quad \text{where } s_i \sim \mu
$$

This is the **off-policy Monte Carlo estimator** (Week 36).

**(b) High Variance of Importance Sampling:**

**Example:** Suppose $|\mathcal{S}| = 2$ with states $\{s_1, s_2\}$. Let:
- $\mu(s_1) = 0.99$, $\mu(s_2) = 0.01$ (behavior policy rarely visits $s_2$)
- $\pi(s_1) = 0.5$, $\pi(s_2) = 0.5$ (target policy visits both equally)

Then:
$$
\rho(s_1) = \frac{0.5}{0.99} \approx 0.505, \quad \rho(s_2) = \frac{0.5}{0.01} = 50
$$

**Mean of $\rho$ under $\mu$:**
$$
\mathbb{E}_\mu[\rho(s)] = \mu(s_1)\rho(s_1) + \mu(s_2)\rho(s_2) = 0.99 \cdot 0.505 + 0.01 \cdot 50 \approx 1.0
$$
(This always equals $1$ since $\sum_s \mu(s) \rho(s) = \sum_s \pi(s) = 1$.)

**Variance of $\rho$ under $\mu$:**
$$
\text{Var}_\mu[\rho] = \mathbb{E}_\mu[\rho^2] - (\mathbb{E}_\mu[\rho])^2
$$

Compute $\mathbb{E}_\mu[\rho^2]$:
$$
\mathbb{E}_\mu[\rho^2] = \mu(s_1)\rho(s_1)^2 + \mu(s_2)\rho(s_2)^2 = 0.99 \cdot (0.505)^2 + 0.01 \cdot (50)^2 \approx 0.25 + 25 = 25.25
$$

Thus:
$$
\text{Var}_\mu[\rho] = 25.25 - 1^2 = 24.25 \quad \text{(very high!)}
$$

**Standard deviation:** $\sigma_\rho = \sqrt{24.25} \approx 4.9$ (larger than the mean!).

**Implication:** Estimating $\mathbb{E}_\pi[f]$ via $\mathbb{E}_\mu[\rho f]$ requires averaging over many samples to reduce variance. For trajectories of length $T$, the cumulative importance weight is:
$$
\rho_{0:T-1} = \prod_{t=0}^{T-1} \rho_t = \prod_{t=0}^{T-1} \frac{\pi(a_t|s_t)}{\mu(a_t|s_t)}
$$

If $\text{Var}[\rho_t] \approx 25$ for each step, then $\text{Var}[\rho_{0:T-1}] \approx 25^T$ (exponential growth!). This is the **curse of horizon** in off-policy RL.

**Variance Reduction Techniques:**
- **Clipping:** $\rho_t^{\text{clip}} = \min(\rho_t, c)$ for some constant $c$ (reduces variance but introduces bias)
- **Truncation:** $\rho_{0:T-1}^{\text{trunc}} = \min(\rho_{0:T-1}, c)$ (less aggressive clipping)
- **Self-normalization:** $\hat{\rho}_t = \rho_t / \left(\sum_{i=1}^N \rho_{t,i}\right)$ (removes bias when $\pi = \mu$ on average)
- **Control variates:** Use baseline $b(s)$ to reduce $\text{Var}[\rho(s)f(s) - b(s)]$

**Modern approach (PPO, TRPO):** Constrain $\pi$ to stay close to $\mu$ via KL divergence penalty $D_{\text{KL}}(\pi \| \mu) \leq \delta$. This ensures $\rho(s,a) \in [1-\epsilon, 1+\epsilon]$ (bounded importance weights), drastically reducing variance.

**(c) Connection to Radon-Nikodym:**

The importance sampling ratio $\rho(s) = \pi(s)/\mu(s)$ is the **Radon-Nikodym derivative** $d\pi/d\mu$. More formally:

**Definition (Discrete Radon-Nikodym):** For probability measures $\pi$ and $\mu$ on finite $\mathcal{S}$, if $\pi \ll \mu$ (i.e., $\pi(A) = 0$ whenever $\mu(A) = 0$ for measurable $A \subseteq \mathcal{S}$), then there exists a function $\rho: \mathcal{S} \to [0, \infty)$ such that:
$$
\pi(A) = \sum_{s \in A} \rho(s) \mu(s) = \mathbb{E}_\mu[\rho(s) \mathbf{1}_A(s)] \quad \text{for all } A \subseteq \mathcal{S}
$$

We write $\rho = d\pi/d\mu$ (density of $\pi$ with respect to $\mu$).

**Theorem (Radon-Nikodym, Discrete Case):** If $\pi \ll \mu$, then $d\pi/d\mu$ exists and is unique $\mu$-almost everywhere.

**Proof (for finite $\mathcal{S}$):** Define $\rho(s) = \pi(s)/\mu(s)$ if $\mu(s) > 0$, and $\rho(s) = 0$ if $\mu(s) = 0$. Then:
$$
\sum_{s \in A} \rho(s) \mu(s) = \sum_{s \in A: \mu(s) > 0} \frac{\pi(s)}{\mu(s)} \mu(s) = \sum_{s \in A: \mu(s) > 0} \pi(s) = \pi(A)
$$
(using $\pi \ll \mu \Rightarrow \pi(s) = 0$ when $\mu(s) = 0$). Uniqueness: if $\rho_1$ and $\rho_2$ both satisfy the above, then $\sum_{s \in \{s_0\}} (\rho_1(s_0) - \rho_2(s_0))\mu(s_0) = 0$ for all $s_0$, so $\rho_1(s_0) = \rho_2(s_0)$ for all $s_0$ with $\mu(s_0) > 0$ (uniqueness $\mu$-a.e.). □

**When does $d\pi/d\mu$ NOT exist?**

The Radon-Nikodym derivative $\rho = d\pi/d\mu$ exists **if and only if** $\pi \ll \mu$ (absolute continuity). If $\pi$ places mass where $\mu$ does not, the derivative is undefined (or infinite).

**Counterexample (finite state space):**
- $\mathcal{S} = \{s_1, s_2, s_3\}$
- $\mu = (0.5, 0.5, 0)$ (behavior policy never visits $s_3$)
- $\pi = (0.4, 0.4, 0.2)$ (target policy visits $s_3$ with probability 0.2)

Then $\pi \not\ll \mu$ (since $\mu(\{s_3\}) = 0$ but $\pi(\{s_3\}) = 0.2 > 0$). The importance sampling ratio:
$$
\rho(s_3) = \frac{\pi(s_3)}{\mu(s_3)} = \frac{0.2}{0} = \text{undefined}
$$

**Practical implication for off-policy RL:** If the behavior policy $\mu$ never visits state $s_3$, we **cannot** use importance sampling to estimate $\mathbb{E}_\pi[f(s_3)]$. The data from $\mu$ provides **no information** about states where $\mu$ has zero mass. This is called the **support mismatch problem** in off-policy learning.

**Solution:** Use **exploration policies** that ensure $\mu(s) > 0$ for all $s$ where $\pi(s) > 0$ (e.g., $\epsilon$-greedy with $\epsilon > 0$, Gaussian noise with full support). This guarantees $\pi \ll \mu$ and thus $d\pi/d\mu$ exists.

**Day 4 Preview:** On Thursday, we generalize this to continuous spaces and prove the Radon-Nikodym theorem: if $\mu \ll \nu$ and both are $\sigma$-finite, then $d\mu/d\nu \in L^1(\nu)$ exists and satisfies $\mu(E) = \int_E (d\mu/d\nu) \, d\nu$ for all measurable $E$.

This formalizes the change-of-measure formulas used throughout RL (importance sampling, off-policy evaluation, inverse propensity scoring).

---

### **Exercise 3.2.5 (Actor-Critic as Dual Spaces)** {#EX-3.2.5}

In **actor-critic methods** (Week 37), the **actor** $\pi_\theta$ (policy) induces a state distribution $\mu_\pi$, while the **critic** $V_w$ (value function approximator) lives in a function space. This exercise explores the duality.

**(a)** Let $\mathcal{S}$ be a finite state space with $|\mathcal{S}| = n$. The actor $\pi_\theta$ defines a policy distribution, which induces a **stationary state distribution** $\mu_\pi \in \Delta^{n-1}$ (probability simplex in $\mathbb{R}^n$). The critic is a value function $V_w \in \mathbb{R}^n$ parameterized by $w \in \mathbb{R}^d$ (e.g., $V_w(s) = w^\top \phi(s)$ for features $\phi$).

The **performance objective** is:
$$
J(\theta) = \mathbb{E}_{\mu_\pi}[V_w(s)] = \sum_{s \in \mathcal{S}} \mu_\pi(s) V_w(s) = \langle \mu_\pi, V_w \rangle
$$

Show that this is the **dual pairing** between $\mu_\pi \in (\ell^\infty)^* \cong \ell^1$ (probability distribution) and $V_w \in \ell^\infty$ (value function).

**(b)** **Policy gradient theorem:** The gradient of $J(\theta)$ with respect to $\theta$ is:
$$
\nabla_\theta J(\theta) = \mathbb{E}_{\mu_\pi}\left[\nabla_\theta \log \pi_\theta(a|s) Q^\pi(s,a)\right]
$$

This involves:
- **Actor gradient:** $\nabla_\theta \log \pi_\theta(a|s)$ (score function)
- **Critic evaluation:** $Q^\pi(s,a)$ (action-value function)
- **Integration against $\mu_\pi$:** Expectation under state distribution

Explain why this is a **dual gradient**: the gradient of a functional (pairing with $\mu_\pi$) with respect to the function space variable ($V$ or $Q$).

**(c)** **Natural policy gradient:** The natural gradient replaces the Euclidean gradient $\nabla_\theta J$ with the **Fisher-Rao gradient**:
$$
\tilde{\nabla}_\theta J = F(\theta)^{-1} \nabla_\theta J
$$
where $F(\theta) = \mathbb{E}_{\mu_\pi}[\nabla_\theta \log \pi_\theta(a|s) \nabla_\theta \log \pi_\theta(a|s)^\top]$ is the **Fisher information matrix**.

This uses the **$L^2$ metric** on the policy space (KL divergence geometry). Explain the connection to Riesz representation: the natural gradient is the unique element of $L^2$ that represents the functional gradient (via the $L^2$ inner product).

---

**Solution 3.2.5:**

**(a) Dual Pairing in Actor-Critic:**

**Setup:**
- State space: $\mathcal{S}$ with $|\mathcal{S}| = n$
- State distribution: $\mu_\pi \in \Delta^{n-1} \subset \mathbb{R}^n$ (probability distribution, $\mu_\pi(s) \geq 0$, $\sum_s \mu_\pi(s) = 1$)
- Value function: $V_w \in \mathbb{R}^n$ (bounded, $\|V_w\|_\infty < \infty$)

**Pairing:**
$$
J(\theta) = \langle \mu_\pi, V_w \rangle := \sum_{s \in \mathcal{S}} \mu_\pi(s) V_w(s) = \mathbb{E}_{\mu_\pi}[V_w(s)]
$$

**Duality interpretation:**

1. **Value functions live in $\ell^\infty$:** Since $V_w(s)$ is bounded for all $s$, $V_w \in \ell^\infty(\mathcal{S})$.

2. **State distributions live in $(\ell^\infty)^*$:** The functional $\phi_\mu(V) = \sum_s \mu(s) V(s)$ is continuous on $\ell^\infty$ (by boundedness):
   $$
   |\phi_\mu(V)| = \left|\sum_s \mu(s) V(s)\right| \leq \sum_s \mu(s) |V(s)| \leq \|V\|_\infty \sum_s \mu(s) = \|V\|_\infty
   $$
   (since $\sum_s \mu(s) = 1$). Thus $\phi_\mu \in (\ell^\infty)^*$ with $\|\phi_\mu\| \leq 1$.

3. **Duality $(\ell^\infty)^* \cong \ell^1$:** By [THM-3.11], on finite spaces, $(\ell^\infty)^* \cong \ell^1$ isometrically. Since $\mu$ is a probability distribution, $\mu \in \ell^1$ (in fact, $\|\mu\|_1 = \sum_s |\mu(s)| = \sum_s \mu(s) = 1$ since $\mu \geq 0$).

**Conclusion:** The actor-critic objective $J(\theta) = \langle \mu_\pi, V_w \rangle$ is the **canonical dual pairing** between:
- **Critic** $V_w \in \ell^\infty$ (value function space)
- **Actor-induced distribution** $\mu_\pi \in (\ell^\infty)^*$ (dual space, identified with $\ell^1$ via probability measures)

This duality formalizes why actor-critic methods alternate between:
- **Policy evaluation (critic update):** Estimate $V_w \approx V^\pi$ (element of $\ell^\infty$)
- **Policy improvement (actor update):** Update $\theta$ to maximize $J(\theta) = \langle \mu_\pi, V_w \rangle$ (functional on $\ell^\infty$)

**(b) Policy Gradient as Dual Gradient:**

The **policy gradient theorem** [@sutton:policy_gradient:2000] states:
$$
\nabla_\theta J(\theta) = \mathbb{E}_{\mu_\pi}\left[\nabla_\theta \log \pi_\theta(a|s) Q^\pi(s,a)\right]
$$

**Interpretation as dual gradient:**

1. **$J(\theta)$ is a functional:** $J: \Theta \to \mathbb{R}$ where $\Theta$ is the policy parameter space. For fixed $\theta$, $J(\theta) = \langle \mu_\pi, V_w \rangle$ is a **linear functional** on the value function space $V_w$.

2. **Gradient via chain rule:** The gradient $\nabla_\theta J$ involves:
   $$
   \nabla_\theta J(\theta) = \nabla_\theta \langle \mu_\pi, V^\pi \rangle = \langle \nabla_\theta \mu_\pi, V^\pi \rangle + \langle \mu_\pi, \nabla_\theta V^\pi \rangle
   $$
   (ignoring the second term, which vanishes for discounted MDPs by envelope theorem; see [@sutton:policy_gradient:2000, Theorem 1]).

3. **First term:** $\langle \nabla_\theta \mu_\pi, V^\pi \rangle$ involves the gradient of the state distribution $\mu_\pi$ (which depends on $\theta$). By the policy gradient theorem, this equals:
   $$
   \mathbb{E}_{\mu_\pi}[\nabla_\theta \log \pi_\theta(a|s) Q^\pi(s,a)]
   $$
   (This is nontrivial and requires the Markov property; see [@sutton:policy_gradient:2000] for proof.)

**Why "dual gradient"?**

- The gradient $\nabla_\theta J$ is computed by integrating $\nabla_\theta \log \pi_\theta$ (score function) **against the value function** $Q^\pi$
- The integration is weighted by $\mu_\pi$ (state distribution in the dual space)
- This is a **Gâteaux derivative** of the functional $J$ with respect to the function $V$ (in the direction of the gradient)

**Practical implication:** Actor-critic methods approximate $\nabla_\theta J$ using:
$$
\nabla_\theta J \approx \frac{1}{N} \sum_{i=1}^N \nabla_\theta \log \pi_\theta(a_i|s_i) Q_w(s_i, a_i)
$$
where samples $(s_i, a_i)$ are drawn from $\mu_\pi$ (on-policy) or corrected via importance sampling (off-policy).

**(c) Natural Policy Gradient and Riesz Representation:**

The **natural policy gradient** [@kakade:natural_policy_gradient:2002; @amari:natural_gradient:1998] replaces the Euclidean gradient $\nabla_\theta J$ with the **Fisher-Rao gradient**:
$$
\tilde{\nabla}_\theta J = F(\theta)^{-1} \nabla_\theta J
$$
where the **Fisher information matrix** is:
$$
F(\theta)_{ij} = \mathbb{E}_{s \sim d_\pi, a \sim \pi_\theta}\left[\frac{\partial \log \pi_\theta(a|s)}{\partial \theta_i} \frac{\partial \log \pi_\theta(a|s)}{\partial \theta_j}\right]
$$

**Connection to Riesz representation:** The Fisher metric defines an **$L^2$ inner product** on the space of score functions $\nabla_\theta \log \pi_\theta(a|s)$:
$$
\langle u, v \rangle_F = \mathbb{E}_{d_\pi}[u(s,a)^\top v(s,a)]
$$
By Riesz representation [THM-3.9], every continuous linear functional $\phi \in (L^2)^*$ corresponds to a unique $g \in L^2$ via $\phi(u) = \langle u, g \rangle_F$. The natural gradient $\tilde{\nabla}_\theta J$ is this unique element: it satisfies:
$$
\langle u, \tilde{\nabla}_\theta J \rangle_F = \langle u, \nabla_\theta J \rangle_{\text{Euclidean}} \quad \text{for all } u
$$
(i.e., $F \tilde{\nabla} J = \nabla J$, hence $\tilde{\nabla} J = F^{-1} \nabla J$).

**Why natural gradients work:**
- **Coordinate-free:** Invariant to reparameterization $\theta \to \phi(\theta)$ (geometric, not algebraic)
- **Trust region:** Step $\theta + \alpha \tilde{\nabla} J$ satisfies $D_{\text{KL}}(\pi_{\theta'} \| \pi_\theta) \approx \frac{\alpha^2}{2} \|\tilde{\nabla} J\|_F^2$ (second-order KL approximation)
- **Steepest ascent:** Maximizes $J$ locally in the Fisher metric (Riemannian geometry)

**Practical challenges:**

1. **Singular Fisher matrix:** If $\pi_\theta$ is deterministic, $F$ has rank $<d$ (not invertible). Solution: Add entropy regularization $H[\pi_\theta(·|s)]$ to ensure stochasticity.

2. **Computational cost:** Exact natural gradient requires:
   - Computing $F$ (requires $O(d^2)$ samples to estimate, $O(d^3)$ to invert)
   - For neural nets with $d = 10^6$ parameters, this is intractable

3. **Modern approximations:**
   - **TRPO** [@schulman:trpo:2015]: Approximate $F^{-1} \nabla J$ via conjugate gradient (CG) without forming $F$ explicitly. Requires only Hessian-vector products $F v$ (computable via automatic differentiation in $O(d)$ time). Typical: 10-20 CG iterations, total cost $O(20d)$ instead of $O(d^3)$.
   - **PPO** [@schulman:ppo:2017]: Avoid natural gradient entirely; instead clip $\rho_t = \pi_{\theta'}/\pi_\theta$ to $[1-\epsilon, 1+\epsilon]$ (ensures KL stays bounded without computing Fisher). Simpler, nearly as effective.
   - **K-FAC** [@martens:kfac:2015]: Approximate $F$ via Kronecker factorization (block-diagonal structure); reduces inversion to $O(d^{3/2})$ or $O(d \log d)$ depending on architecture.

**When theory breaks:** For **neural network policies**, the Fisher information may be:
- **Ill-conditioned** (large condition number $\kappa(F) \gg 1$; CG converges slowly)
- **Non-stationary** (Fisher changes rapidly during training; preconditioning stale)
- **Empirically approximate** (sample estimates $\hat{F}$ from mini-batches have high variance)

Despite these issues, TRPO/PPO work well in practice by combining:
- Approximate natural gradient (CG, clipping)
- Conservative step sizes (KL constraint, clip threshold)
- Large replay buffers (stabilize Fisher estimates)

**Conclusion:** The natural gradient is a beautiful application of Riesz duality ($L^2$ inner product $\to$ unique dual element), but **practical RL requires approximations** that trade mathematical rigor for computational tractability.

---

### **Reflection Questions:**

1. **Why does $(L^2)^* \cong L^2$ (self-duality) make $L^2$ special for least-squares methods?**
   *Hint:* Self-duality means inner product structure $\langle f, g \rangle = \int fg$ is symmetric. The projection $\Pi V$ onto a subspace minimizes $\|V - \Pi V\|_2$, which is the least-squares objective. Other $L^p$ spaces ($p \neq 2$) don't have this symmetry.

2. **What goes wrong with $(L^\infty)^*$ in off-policy RL?**
   *Hint:* $(L^\infty)^* \supsetneq L^1$ (strict containment; see [THM-3.12]). Not all functionals on $L^\infty$ correspond to probability measures. However, the functionals we care about in RL (expectations $\mathbb{E}_\mu[V]$) **do** lie in $L^1$, so this isn't a problem in practice.

3. **How does duality explain why policy gradients integrate against state distributions?**
   *Hint:* The objective $J(\theta) = \langle \mu_\pi, V^\pi \rangle$ is a pairing between dual spaces. The gradient $\nabla_\theta J$ involves $\nabla_\theta \mu_\pi$ (derivative of distribution), which appears as integration $\mathbb{E}_{\mu_\pi}[\cdots]$ in the policy gradient formula.

---

**Summary:**

**What we learned:**
- Conjugate exponents $1/p + 1/q = 1$ characterize duality between $L^p$ and $L^q$
- Riesz representation [THM-3.9]: $(L^p)^* \cong L^q$ for $1 < p < \infty$ via $\phi(f) = \int fg \, d\mu$
- Special cases: $(L^2)^* \cong L^2$ (self-dual), $(L^1)^* \cong L^\infty$ (on $\sigma$-finite spaces)
- RL applications:
  - Value functions (critic) and state distributions (actor) are dual
  - Importance sampling ratios $\pi/\mu$ are Radon-Nikodym derivatives (Day 4)
  - Least-squares TD uses $L^2$ projection (Week 14 Hilbert spaces)
  - Natural policy gradient uses Fisher metric ($L^2$ inner product on score functions)

**Time allocation:** ~40 minutes (exercises are part of 90-minute Tuesday session; ~40 min reading + ~40 min exercises from main file + ~10 min reflection)

---

**End of Exercises**
