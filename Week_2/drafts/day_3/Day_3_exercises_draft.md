[[Day_3_draft]]

## **Week 2, Day 3 — Exercises: Fubini's Theorem and Counterexamples**

**Theme:** Extending iterated integration to signed functions; understanding failure modes when hypotheses are violated

---

### **Exercise 1: Prove Fubini's Theorem via Reduction to Tonelli** {#EX-2.3.1}

**Difficulty:** ★★☆☆☆ (Standard proof, following lecture structure)

**Statement:** Let $(X, \mathcal{F}_X, \mu)$ and $(Y, \mathcal{F}_Y, \nu)$ be σ-finite measure spaces. Let $f: X \times Y \to \mathbb{R}$ be measurable with $\int_{X \times Y} |f| \, d(\mu \times \nu) < \infty$. Prove that:
$$
\int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f \, d(\mu \times \nu) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y)
$$

**Guidance:**

1. **Decompose:** Write $f = f^+ - f^-$ where $f^+ = \max(f, 0)$ and $f^- = \max(-f, 0)$
2. **Verify integrability:** Show that $\int f^+ < \infty$ and $\int f^- < \infty$ using $|f| = f^+ + f^-$
3. **Apply Tonelli:** Use Tonelli (Theorem 2.3) separately to $f^+$ and $f^-$ to establish:
   $$
   \int_X \left(\int_Y f^+(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f^+ \, d(\mu \times \nu)
   $$
   and similarly for $f^-$
4. **Subtract:** Use linearity of the integral to combine:
   $$
   \int_X \left(\int_Y f \, d\nu\right) d\mu = \int_X \left(\int_Y f^+ \, d\nu\right) d\mu - \int_X \left(\int_Y f^- \, d\nu\right) d\mu = \int f^+ - \int f^- = \int f
   $$
5. **Symmetry:** Repeat for the other order $\int_Y (\int_X f \, d\mu) d\nu$

**Key Lemma (Fubini's Lemma - Optional Verification):**

Show that for $\mu$-almost every $x \in X$, the section $f(x, \cdot): Y \to \mathbb{R}$ is $\nu$-integrable. *(Hint: Apply Tonelli to $|f|$ to show $\int_Y |f(x,y)| \, d\nu(y) < \infty$ for $\mu$-a.e. $x$.)*

**Solution Sketch:**

*Proof.*

**Step 1:** Decompose $f = f^+ - f^-$ where both $f^+, f^- \geq 0$ are measurable.

From $\int |f| = \int (f^+ + f^-) < \infty$, we obtain:
$$
\int_{X \times Y} f^+ \, d(\mu \times \nu) < \infty \quad \text{and} \quad \int_{X \times Y} f^- \, d(\mu \times \nu) < \infty
$$

**Step 2:** Apply Tonelli to $f^+ \geq 0$:
$$
\int_X \left(\int_Y f^+(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f^+ \, d(\mu \times \nu)
$$

Apply Tonelli to $f^- \geq 0$:
$$
\int_X \left(\int_Y f^-(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f^- \, d(\mu \times \nu)
$$

**Step 3:** Subtract (valid since both integrals are finite):
$$
\begin{align}
\int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) &= \int_X \left(\int_Y [f^+ - f^-] \, d\nu\right) d\mu \\
&= \int_X \left[\int_Y f^+ \, d\nu - \int_Y f^- \, d\nu\right] d\mu \\
&= \int_X \left(\int_Y f^+ \, d\nu\right) d\mu - \int_X \left(\int_Y f^- \, d\nu\right) d\mu \\
&= \int_{X \times Y} f^+ \, d(\mu \times \nu) - \int_{X \times Y} f^- \, d(\mu \times \nu) \\
&= \int_{X \times Y} (f^+ - f^-) \, d(\mu \times \nu) = \int_{X \times Y} f \, d(\mu \times \nu)
\end{align}
$$

By symmetry, the same holds for $\int_Y (\int_X f \, d\mu) d\nu$. □

---

### **Exercise 2: Counterexample to Fubini Without Integrability** {#EX-2.3.2}

**Difficulty:** ★★★☆☆ (Requires careful accounting of signs and sums)

**Statement:** Consider the function $f: \mathbb{N} \times \mathbb{N} \to \mathbb{R}$ defined by:
$$
f(i,j) = \begin{cases}
1 & \text{if } j = i \\
-1 & \text{if } j = i + 1 \\
0 & \text{otherwise}
\end{cases}
$$

Let $\mu = \nu = $ counting measure on $\mathbb{N}$.

(a) Compute both iterated sums $\sum_i \sum_j f(i,j)$ and $\sum_j \sum_i f(i,j)$.

(b) Show that $\sum_{i,j} |f(i,j)| = \infty$, confirming $f \notin L^1(\text{counting} \times \text{counting})$.

(c) Explain geometrically why the iterated sums differ.

**Solution:**

**(a) Iterated sums:**

**Order 1: Outer $i$, inner $j$**

For fixed $i \in \mathbb{N}$:
$$
\sum_{j=1}^\infty f(i,j) = f(i,i) + f(i,i+1) + \sum_{\substack{j \neq i \\ j \neq i+1}} f(i,j) = 1 + (-1) + 0 = 0
$$

(Each row has exactly one $+1$ at column $i$ and one $-1$ at column $i+1$.)

Sum over $i$:
$$
\sum_{i=1}^\infty \left(\sum_{j=1}^\infty f(i,j)\right) = \sum_{i=1}^\infty 0 = 0
$$

**Order 2: Outer $j$, inner $i$**

For fixed $j \in \mathbb{N}$:
$$
\sum_{i=1}^\infty f(i,j)
$$

- If $j = 1$: $f(1,1) = 1$, all other terms 0. Sum: $1$
- If $j \geq 2$: $f(j-1, j) = -1$, $f(j,j) = 1$, all other terms 0. Sum: $0$

Thus:
$$
\sum_{i=1}^\infty f(i,j) = \begin{cases} 1 & \text{if } j = 1 \\ 0 & \text{if } j \geq 2 \end{cases}
$$

Sum over $j$:
$$
\sum_{j=1}^\infty \left(\sum_{i=1}^\infty f(i,j)\right) = 1 + 0 + 0 + \cdots = 1
$$

**Conclusion:** $\sum_i \sum_j f(i,j) = 0 \neq 1 = \sum_j \sum_i f(i,j)$. ✓

**(b) Non-integrability:**

$$
\sum_{i=1}^\infty \sum_{j=1}^\infty |f(i,j)| = \sum_{i=1}^\infty [|f(i,i)| + |f(i,i+1)|] = \sum_{i=1}^\infty [1 + 1] = \sum_{i=1}^\infty 2 = \infty
$$

Thus $f \notin L^1(\mu \times \nu)$ because $\int_{X \times Y} |f| = \infty$. ✓

**(c) Geometric interpretation:**

Visualize the infinite grid $\mathbb{N} \times \mathbb{N}$ with $f$ having:
- **Diagonal entries** $(i,i)$: value $+1$
- **Super-diagonal entries** $(i, i+1)$: value $-1$
- All other entries: $0$

**Row-wise sum (outer $i$, inner $j$):**
Each row $i$ contains exactly one $+1$ and one $-1$, which cancel. Summing over rows gives $0$.

**Column-wise sum (outer $j$, inner $i$):**
- **Column 1:** Contains only $f(1,1) = 1$. Sum: $1$
- **Column $j \geq 2$:** Contains $f(j-1, j) = -1$ (from row $j-1$) and $f(j,j) = 1$ (from row $j$), which cancel. Sum: $0$

Summing over columns gives $1 + 0 + 0 + \cdots = 1$.

**Why the discrepancy?** The function $f$ exhibits **conditional convergence** (like the alternating harmonic series $\sum (-1)^n/n$). Positive and negative contributions cancel in order-dependent ways. When summing row-by-row, the initial $+1$ in the first column is "balanced" by subsequent $-1$'s within each row. When summing column-by-column, the first column has an "unbalanced" $+1$ that is never fully canceled.

This is analogous to **rearrangement of conditionally convergent series** (Riemann series theorem): changing the order of summation changes the limit. Fubini requires **absolute convergence** ($\int |f| < \infty$) to prevent this pathology. ✓

**RL Connection:** In importance sampling with unbounded ratios, computing $\mathbb{E}_\mu[\rho \cdot R]$ via different sampling orders (first sample states, then actions vs. first sample actions, then states) can yield different estimates if $\mathbb{E}[|\rho \cdot R|] = \infty$. This is precisely the Fubini failure mode.

---

### **Exercise 3: Off-Policy Policy Evaluation with Clipped Importance Ratios** {#EX-2.3.3}

**Difficulty:** ★★★★☆ (Combines Fubini with RL concepts; requires understanding bias-variance trade-off)

**Setting:** Consider an MDP with finite state space $\mathcal{S}$ and finite action space $\mathcal{A}$. Let $\pi$ be the target policy and $\mu$ be the behavior policy. The Q-function under $\pi$ is $Q^\pi: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$, assumed bounded: $|Q^\pi(s,a)| \leq Q_{\max}$ for all $(s,a)$.

We wish to estimate:
$$
\mathbb{E}_{\mu}[\rho(s,a) Q^\pi(s,a)] \quad \text{where } \rho(s,a) = \frac{\pi(a|s)}{\mu(a|s)}
$$

**(a) Integrability Check:** Show that if $\mu(a|s) \geq \epsilon > 0$ for all $(s,a)$ (i.e., $\mu$ has full support with minimum probability $\epsilon$), then:
$$
\mathbb{E}_\mu[|\rho(s,a) Q^\pi(s,a)|] \leq \frac{Q_{\max}}{\epsilon} < \infty
$$
confirming that Fubini applies.

**(b) Clipped Ratios:** In practice, we often clip importance ratios to control variance:
$$
\bar{\rho}(s,a) = \min(\rho(s,a), \rho_{\max})
$$
where $\rho_{\max} > 0$ is a clipping threshold.

Show that with clipped ratios:
$$
\mathbb{E}_\mu[|\bar{\rho}(s,a) Q^\pi(s,a)|] \leq \rho_{\max} Q_{\max} < \infty
$$
so Fubini applies regardless of whether $\mu$ has full support.

**(c) Bias Analysis:** Define the clipping bias as:
$$
\text{Bias} = \mathbb{E}_\mu[\rho(s,a) Q^\pi(s,a)] - \mathbb{E}_\mu[\bar{\rho}(s,a) Q^\pi(s,a)]
$$

Express the bias in terms of the expectation over the set $\{\rho(s,a) > \rho_{\max}\}$. Under what condition is the bias zero?

**(d) RL Interpretation:** Explain why PPO (Proximal Policy Optimization) clips importance ratios to $[1-\epsilon, 1+\epsilon]$ with $\epsilon \approx 0.2$. What does this achieve in terms of:
1. Ensuring Fubini applies
2. Controlling variance
3. Introducing bias

**Solution:**

**(a) Integrability with full support:**

Given $\mu(a|s) \geq \epsilon$ for all $(s,a)$, we have:
$$
\rho(s,a) = \frac{\pi(a|s)}{\mu(a|s)} \leq \frac{1}{\epsilon}
$$

since $\pi(a|s) \leq 1$.

Thus:
$$
\mathbb{E}_\mu[|\rho(s,a) Q^\pi(s,a)|] \leq \mathbb{E}_\mu\left[\frac{1}{\epsilon} |Q^\pi(s,a)|\right] \leq \frac{1}{\epsilon} \cdot Q_{\max} < \infty
$$

Since the expectation is finite, Fubini applies, and we can compute the iterated expectation:
$$
\mathbb{E}_\mu[\rho \cdot Q] = \mathbb{E}_{s \sim \mu_s}\left[\mathbb{E}_{a \sim \mu(\cdot|s)}[\rho(s,a) Q^\pi(s,a)]\right]
$$
via either order of integration. ✓

**(b) Integrability with clipped ratios:**

By definition, $\bar{\rho}(s,a) = \min(\rho(s,a), \rho_{\max}) \leq \rho_{\max}$.

Thus:
$$
\mathbb{E}_\mu[|\bar{\rho}(s,a) Q^\pi(s,a)|] \leq \mathbb{E}_\mu[\rho_{\max} |Q^\pi(s,a)|] = \rho_{\max} \mathbb{E}_\mu[|Q^\pi(s,a)|] \leq \rho_{\max} Q_{\max} < \infty
$$

This holds **regardless of whether $\mu$ has full support**. Even if $\mu(a|s)$ can be arbitrarily small (making $\rho$ arbitrarily large), clipping ensures $\bar{\rho}$ is bounded. ✓

**(c) Bias expression:**

$$
\begin{align}
\text{Bias} &= \mathbb{E}_\mu[\rho \cdot Q] - \mathbb{E}_\mu[\bar{\rho} \cdot Q] \\
&= \mathbb{E}_\mu[(\rho - \bar{\rho}) \cdot Q] \\
&= \mathbb{E}_\mu[(\rho - \rho_{\max}) \cdot Q \cdot \mathbf{1}_{\{\rho > \rho_{\max}\}}]
\end{align}
$$

where $\mathbf{1}_{\{\rho > \rho_{\max}\}}$ is the indicator of the event $\rho(s,a) > \rho_{\max}$.

**Key observation:** $\rho - \bar{\rho} = 0$ when $\rho \leq \rho_{\max}$, and $\rho - \bar{\rho} = \rho - \rho_{\max}$ when $\rho > \rho_{\max}$.

**Bias is zero when:**
- $\mathbb{P}_\mu(\rho(s,a) > \rho_{\max}) = 0$ (i.e., $\rho$ never exceeds the threshold), OR
- $Q^\pi(s,a) = 0$ whenever $\rho(s,a) > \rho_{\max}$ (unlikely in practice)

**Bias increases when:**
- $\pi$ and $\mu$ differ significantly (large $\rho$)
- $\rho_{\max}$ is set too small (aggressive clipping)
- $|Q^\pi(s,a)|$ is large in the clipping region

**(d) PPO interpretation:**

**PPO objective (simplified):**
$$
L^{\text{CLIP}}(\theta) = \mathbb{E}_{s,a \sim \mu}\left[\min\left(\rho_\theta(s,a) A^\pi(s,a), \, \text{clip}(\rho_\theta, 1-\epsilon, 1+\epsilon) A^\pi(s,a)\right)\right]
$$

where $\rho_\theta(s,a) = \pi_\theta(a|s)/\mu(a|s)$ is the importance ratio.

**1. Ensuring Fubini applies:**

By clipping $\rho_\theta \in [1-\epsilon, 1+\epsilon]$, PPO ensures:
$$
|\rho_\theta| \leq 1 + \epsilon
$$

This makes:
$$
\mathbb{E}[|\rho_\theta \cdot A|] \leq (1 + \epsilon) \mathbb{E}[|A|] < \infty
$$

(assuming advantages are bounded, which holds when rewards and values are bounded).

Thus Fubini applies, and the policy gradient $\mathbb{E}_{s}[\mathbb{E}_{a}[\nabla \log \pi \cdot A]]$ is well-defined. ✓

**2. Controlling variance:**

Importance sampling suffers from high variance when $\rho$ is large (the behavior policy rarely samples actions that the target policy prefers). Clipping reduces variance by capping the contribution of rare events.

**Variance reduction:** $\text{Var}(\bar{\rho} \cdot A) \leq \text{Var}(\rho \cdot A)$ because $\bar{\rho}$ has a smaller range.

**3. Introducing bias:**

Clipping introduces bias when $\rho > 1 + \epsilon$ (the target policy assigns higher probability than the behavior policy). The clipped estimate:
$$
\mathbb{E}[\bar{\rho} \cdot A]
$$
underestimates the true advantage $\mathbb{E}[\rho \cdot A]$ in this region.

**PPO trade-off:**
- **Pro:** Reduced variance, stable training, guaranteed integrability (Fubini applies)
- **Con:** Biased gradient estimates, slower convergence to optimal policy

In practice, $\epsilon = 0.2$ is chosen empirically to balance bias and variance. The clip range $[0.8, 1.2]$ is narrow enough to control variance but wide enough to allow meaningful policy updates.

**Connection to Fubini:** Without clipping (and without full-support $\mu$), the policy gradient:
$$
\nabla_\theta J(\pi_\theta) = \mathbb{E}_{s,a \sim \mu}\left[\rho_\theta(s,a) \nabla_\theta \log \pi_\theta(a|s) A^\pi(s,a)\right]
$$
may not be well-defined (iterated expectations depend on order) if $\mathbb{E}[|\rho \cdot A|] = \infty$. Clipping ensures integrability, making the gradient rigorously defined. ✓

**Reference:** Schulman et al. (2017), "Proximal Policy Optimization Algorithms," *arXiv:1707.06347*.

---

### **Exercise 4: Bellman Error and Integrability in TD Learning** {#EX-2.3.4}

**Difficulty:** ★★★★☆ (Advanced; connects Fubini to TD convergence theory)

**Setting:** Consider temporal-difference (TD) learning with linear function approximation:
$$
V_\theta(s) = \theta^\top \phi(s)
$$

where $\phi: \mathcal{S} \to \mathbb{R}^d$ is a feature map and $\theta \in \mathbb{R}^d$ are parameters.

The **Bellman error** at state $s$ is:
$$
\delta(s; \theta) = V_\theta(s) - \mathbb{E}_{a \sim \pi(\cdot|s)}\left[\mathbb{E}_{s' \sim P(\cdot|s,a)}[R(s,a,s') + \gamma V_\theta(s')]\right]
$$

**(a) Iterated Expectation:** Using Fubini, show that if $\mathbb{E}[|\delta|] < \infty$, then:
$$
\mathbb{E}_{s \sim d^\pi}[\delta(s; \theta)] = \mathbb{E}_{s \sim d^\pi}\left[\mathbb{E}_{a,s'}[V_\theta(s) - R(s,a,s') - \gamma V_\theta(s')]\right]
$$

can be computed via iterated integrals in any order.

**(b) Integrability Condition:** Suppose:
- Rewards are bounded: $|R(s,a,s')| \leq R_{\max}$
- Features are bounded: $\|\phi(s)\| \leq \phi_{\max}$
- Parameters are bounded: $\|\theta\| \leq \theta_{\max}$

Show that $\mathbb{E}[|\delta(s; \theta)|] \leq C$ for some constant $C$, confirming integrability.

**(c) Failure Mode (Baird's Counterexample):** In off-policy TD with linear function approximation, $\theta$ can diverge (Baird, 1995). Explain how this violates the integrability condition for Fubini. What happens to the iterated expectation when $\|\theta\| \to \infty$?

**Solution Sketch:**

**(a) Iterated expectation via Fubini:**

The Bellman error can be written as:
$$
\delta(s; \theta) = V_\theta(s) - \int_{\mathcal{A}} \pi(a|s) \left(\int_{\mathcal{S}} P(s'|s,a) [R(s,a,s') + \gamma V_\theta(s')] ds'\right) da
$$

This is an **iterated integral of a signed function**. If $\delta \in L^1(d^\pi)$, Fubini applies, allowing us to interchange integration over $s, a, s'$ in any order.

For example:
$$
\mathbb{E}_{s \sim d^\pi}[\delta(s; \theta)] = \int_{\mathcal{S}} d^\pi(s) \left[V_\theta(s) - \int_{\mathcal{A}} \int_{\mathcal{S}} \pi(a|s) P(s'|s,a) [R + \gamma V_\theta(s')] ds' da\right] ds
$$

Fubini guarantees this equals:
$$
\int_{\mathcal{S}} \int_{\mathcal{A}} \int_{\mathcal{S}} d^\pi(s) \pi(a|s) P(s'|s,a) [V_\theta(s) - R - \gamma V_\theta(s')] ds' da ds
$$

which can be computed via Monte Carlo sampling in any order (e.g., sample $s$, then $a$, then $s'$). ✓

**(b) Integrability:**

$$
|\delta(s; \theta)| = \left|V_\theta(s) - \mathbb{E}_{a,s'}[R + \gamma V_\theta(s')]\right|
$$

By triangle inequality:
$$
|\delta(s; \theta)| \leq |V_\theta(s)| + \mathbb{E}_{a,s'}[|R + \gamma V_\theta(s')|] \leq |V_\theta(s)| + \mathbb{E}_{a,s'}[|R| + \gamma |V_\theta(s')|]
$$

Using $V_\theta(s) = \theta^\top \phi(s)$ and Cauchy-Schwarz:
$$
|V_\theta(s)| \leq \|\theta\| \|\phi(s)\| \leq \theta_{\max} \phi_{\max}
$$

And $|R| \leq R_{\max}$. Thus:
$$
|\delta(s; \theta)| \leq \theta_{\max} \phi_{\max} + R_{\max} + \gamma \theta_{\max} \phi_{\max} = (1 + \gamma) \theta_{\max} \phi_{\max} + R_{\max}
$$

Taking expectation:
$$
\mathbb{E}[|\delta|] \leq (1 + \gamma) \theta_{\max} \phi_{\max} + R_{\max} =: C < \infty
$$

So $\delta \in L^1(d^\pi)$, and Fubini applies. ✓

**(c) Baird's counterexample and Fubini failure:**

In **Baird's star-shaped counterexample** (1995), off-policy TD with linear function approximation causes $\|\theta_n\| \to \infty$ as $n \to \infty$ (divergence).

**What goes wrong:**

As $\|\theta\| \to \infty$, the value function $V_\theta(s) = \theta^\top \phi(s)$ grows unbounded. The Bellman error:
$$
\delta(s; \theta) = V_\theta(s) - \mathbb{E}[R + \gamma V_\theta(s')]
$$

also diverges.

**Fubini failure:**

When $\mathbb{E}[|\delta|] = \infty$ (due to unbounded $V_\theta$), Fubini does not apply. The iterated expectation:
$$
\mathbb{E}_{s \sim d^\pi}\left[\mathbb{E}_{a,s'}[\delta(s; \theta)]\right]
$$

may depend on the order of integration, or may not be well-defined at all (yielding $\infty - \infty$ indeterminate forms).

**Practical consequence:**

In off-policy TD with linear function approximation, the **temporal-difference updates**:
$$
\theta_{n+1} = \theta_n + \alpha_n \delta(s_n; \theta_n) \phi(s_n)
$$

can diverge because $\delta(s_n; \theta_n)$ grows unbounded. The iterated expectation formulation used in convergence proofs (e.g., Tsitsiklis & Van Roy, 1997) assumes $\mathbb{E}[|\delta|] < \infty$, which Baird's counterexample violates.

**Fix:** Use **gradient TD** (GTD, GTD2, TDC) which minimizes the **projected Bellman error**:
$$
\text{MSPBE}(\theta) = \|\Pi (T^\pi V_\theta - V_\theta)\|^2
$$

where $\Pi$ is the projection onto the feature subspace. This formulation ensures convergence even off-policy by maintaining bounded $\theta$ (see Sutton et al., 2009, "Fast Gradient-Descent Methods for Temporal-Difference Learning with Linear Function Approximation," *ICML*).

**RL Lesson:** Ensuring integrability ($\mathbb{E}[|\delta|] < \infty$) is not just a mathematical nicety—it is **necessary for convergence** of TD algorithms. When integrability fails (as in Baird's counterexample), algorithms diverge, and Fubini-based proofs break down. ✓

---

### **Exercise 5: Research Question — Uniform Integrability and Fubini** {#EX-2.3.5}

**Difficulty:** ★★★★★ (Open-ended; requires reading ahead)

**Background:** Fubini requires $\int |f| < \infty$ (integrability). In probability theory, a weaker condition called **uniform integrability** (UI) is often used to control expectations in limit theorems.

A family of random variables $\{X_\alpha\}_{\alpha \in \mathcal{I}}$ is **uniformly integrable** if:
$$
\lim_{M \to \infty} \sup_{\alpha \in \mathcal{I}} \mathbb{E}[|X_\alpha| \cdot \mathbf{1}_{\{|X_\alpha| > M\}}] = 0
$$

**Question:** Can uniform integrability replace integrability in Fubini's theorem? Specifically:

**(a)** If $f_n: X \times Y \to \mathbb{R}$ is a sequence of measurable functions such that:
- $f_n \to f$ pointwise
- $\{f_n\}$ is uniformly integrable with respect to $\mu \times \nu$

Can we conclude that $\int_X (\int_Y f \, d\nu) d\mu = \int_{X \times Y} f \, d(\mu \times \nu)$?

**(b)** In RL, suppose a sequence of policies $\{\pi_n\}$ converges to $\pi^*$, and the importance ratios $\rho_n(s,a) = \pi_n(a|s)/\mu(a|s)$ are uniformly integrable. Does this guarantee convergence of off-policy estimates $\mathbb{E}_\mu[\rho_n Q] \to \mathbb{E}_{\pi^*}[Q]$?

**Guidance:**

- Consult [@durrett:probability:2019, §5.4] on uniform integrability
- Investigate the **Vitali convergence theorem** (a UI version of dominated convergence)
- Consider whether Fubini-like results can be formulated using UI

**This is an open research question connecting measure theory to RL convergence proofs. A complete answer would constitute a small research note.**

---

### **Summary of Exercises**

1. ✅ **Exercise 1:** Prove Fubini via reduction to Tonelli (standard proof technique)
2. ✅ **Exercise 2:** Construct counterexample to Fubini without integrability (conditionally convergent double series)
3. ✅ **Exercise 3:** Analyze clipped importance ratios in off-policy RL (PPO connection)
4. ✅ **Exercise 4:** Connect Bellman error integrability to TD convergence (Baird's counterexample)
5. 🔬 **Exercise 5:** Research question on uniform integrability and Fubini (open-ended)

**Anchor Exercises for Syllabus (Week 2, Day 3):**
- Exercise 2 (Counterexample without integrability)
- Exercise 3 (Off-policy RL with clipped ratios)

---

**End of Exercises**
