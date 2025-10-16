### 📝 Exercises — Week 3, Day 1: Completeness of $L^p$ Spaces

**Correspondence:** These exercises complement **[[Day_1_draft]]** (Riesz-Fischer theorem and completeness of $L^p$ spaces).

**Learning Objectives:**
- Master the proof technique: subsequence extraction + pointwise convergence + Fatou → $L^p$ convergence
- Construct explicit counterexamples showing that incomplete spaces exist
- Apply completeness to Bellman operators and value iteration convergence
- Understand why Banach space structure is essential for RL theory

---

## **Exercise 1: Riesz-Fischer for $L^1$ (Anchor Exercise)** {#EX-3.1.1}

**Statement:** Prove that $L^1(\mu)$ is complete by adapting the proof of Theorem 3.4 to the case $p = 1$.

**Guidance:** (**Expected time: 45-55 minutes** for independent solution)
- Follow the six-step proof in Section II of Day_1_draft.md
- **Simplification for $p = 1$:** In Step 2, the bound $\|S_K\|_1 \leq \|g_1\|_1 + \sum_{k=1}^\infty 2^{-k}$ follows directly from Minkowski for $p = 1$ (which is just the triangle inequality for integrals: $\int |f + g| \leq \int |f| + \int |g|$)
- In Step 4, Fatou's lemma applied to $|g_K|$ (not $|g_K|^p$) gives $\int |f| \leq \liminf_K \int |g_K|$

---

**Solution:**

**Proof of $L^1$ Completeness.**

Let $\{f_n\} \subseteq L^1(\mu)$ be Cauchy in $L^1$ norm.

**Step 1 (Subsequence extraction):** As in the general case, **by the Cauchy property** (formally justified in Exercise 4 below), extract a subsequence $g_k = f_{N_k}$ with:
$$
\|g_{k+1} - g_k\|_1 < 2^{-k} \quad \text{for all } k \geq 1
$$

**Step 2 (Pointwise a.e. convergence):** Define the telescoping sum:
$$
S_K(x) = |g_1(x)| + \sum_{k=1}^{K-1} |g_{k+1}(x) - g_k(x)|
$$

By linearity of the integral (and Minkowski's inequality $\|f+g\|_1 \leq \|f\|_1 + \|g\|_1$ for the bound):
$$
\begin{align}
\|S_K\|_1 &= \int_X S_K \, d\mu \\
&= \int_X \left(|g_1| + \sum_{k=1}^{K-1} |g_{k+1} - g_k|\right) d\mu \\
&= \int_X |g_1| \, d\mu + \sum_{k=1}^{K-1} \int_X |g_{k+1} - g_k| \, d\mu \quad \text{(linearity)} \\
&= \|g_1\|_1 + \sum_{k=1}^{K-1} \|g_{k+1} - g_k\|_1 \\
&< \|g_1\|_1 + \sum_{k=1}^{K-1} 2^{-k} \\
&< \|g_1\|_1 + 1
\end{align}
$$

Since $S_K \nearrow S = \lim_K S_K$ (increasing, so limit exists in $[0, \infty]$), apply **Monotone Convergence Theorem**:
$$
\|S\|_1 = \int_X S \, d\mu = \lim_{K \to \infty} \int_X S_K \, d\mu = \lim_{K \to \infty} \|S_K\|_1 \leq \|g_1\|_1 + 1 < \infty
$$

Thus $S \in L^1$, which implies $S(x) < \infty$ for $\mu$-almost every $x$ (if $S(x) = \infty$ on a set $E$ with $\mu(E) > 0$, then $\int_E S = \infty$, contradiction).

Therefore, the series $\sum_{k=1}^\infty |g_{k+1}(x) - g_k(x)|$ converges absolutely for $\mu$-a.e. $x$, so:
$$
f(x) = g_1(x) + \sum_{k=1}^\infty (g_{k+1}(x) - g_k(x)) = \lim_{K \to \infty} g_K(x)
$$

exists and is finite for $\mu$-a.e. $x$. ✓

**Step 3 (Measurability):** $f = \lim_K g_K$ is measurable as a pointwise limit of measurable functions. ✓

**Step 4 ($f \in L^1$ via Fatou):** Apply Fatou's lemma to the non-negative functions $|g_K|$:
$$
\int_X |f| \, d\mu = \int_X \lim_{K \to \infty} |g_K| \, d\mu = \int_X \liminf_{K \to \infty} |g_K| \, d\mu \leq \liminf_{K \to \infty} \int_X |g_K| \, d\mu = \liminf_{K \to \infty} \|g_K\|_1
$$

Since $\{g_K\}$ is Cauchy (hence bounded): $\|g_K\|_1 \leq M < \infty$ for all $K$. Thus:
$$
\|f\|_1 \leq \liminf_{K \to \infty} \|g_K\|_1 \leq M < \infty
$$

So $f \in L^1$. ✓

**Step 5 ($\|g_K - f\|_1 \to 0$ via Fatou):** For each $K$:
$$
|g_K(x) - f(x)| = |g_K(x) - \lim_{M \to \infty} g_M(x)| = \lim_{M \to \infty} |g_K(x) - g_M(x)|
$$

Apply Fatou to $|g_K - g_M|$ (viewing $M$ as varying):
$$
\int_X |g_K - f| \, d\mu = \int_X \liminf_{M \to \infty} |g_K - g_M| \, d\mu \leq \liminf_{M \to \infty} \int_X |g_K - g_M| \, d\mu = \liminf_{M \to \infty} \|g_K - g_M\|_1
$$

Since $\{g_K\}$ is Cauchy: for any $\epsilon > 0$, there exists $K_0$ such that $K, M \geq K_0$ implies $\|g_K - g_M\|_1 < \epsilon$. Thus:
$$
\|g_K - f\|_1 \leq \liminf_{M \to \infty} \|g_K - g_M\|_1 < \epsilon \quad \text{for } K \geq K_0
$$

So $\|g_K - f\|_1 \to 0$. ✓

**Step 6 (Extend to full sequence):** For $\epsilon > 0$, choose $K$ large such that $\|g_K - f\|_1 < \epsilon/2$ and $N_K$ large such that $n \geq N_K$ implies $\|f_n - f_{N_K}\|_1 < \epsilon/2$ (by Cauchy property). Then:
$$
\|f_n - f\|_1 \leq \|f_n - f_{N_K}\|_1 + \|f_{N_K} - f\|_1 = \|f_n - g_K\|_1 + \|g_K - f\|_1 < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
$$

Thus $\|f_n - f\|_1 \to 0$. ✓

This proves $L^1(\mu)$ is complete. □

---

**Remark:** The proof for $p = 1$ is **simpler** than the general case because:
- Minkowski for $p = 1$ is just the triangle inequality for integrals (no power $p$ complication)
- Fatou applies directly to $|g_K|$ (not $|g_K|^p$), avoiding fractional powers

However, the **same structure** (six steps: extract → pointwise → measurable → in $L^p$ → norm convergence → extend) applies to all $1 \leq p < \infty$.

---

## **Exercise 2: Incomplete Space Counterexample** {#EX-3.1.2}

**Statement:** Show that the space $(C([0,1]), \|\cdot\|_1)$ of continuous functions on $[0,1]$ with the $L^1$ norm:
$$
\|f\|_1 = \int_0^1 |f(x)| \, dx
$$

is **not complete** by constructing an explicit Cauchy sequence $\{f_n\} \subseteq C([0,1])$ that converges in $L^1$ to a **discontinuous function**.

**Guidance:**
- Consider the "ramp" functions $f_n(x) = \min(nx, 1)$ for $x \in [0,1]$
- Show $f_n$ is continuous for each $n$
- Show $\{f_n\}$ is Cauchy in $L^1$ norm
- Compute the pointwise limit: $f(x) = \lim_n f_n(x) = \mathbf{1}_{(0,1]}(x)$ (indicator function)
- Observe $f$ is discontinuous at $x = 0$
- Conclude: $\{f_n\}$ is Cauchy in $(C([0,1]), \|\cdot\|_1)$ but has no limit in $C([0,1])$—the space is incomplete

---

**Solution:**

**Construction:** Define:
$$
f_n(x) = \begin{cases}
nx & \text{if } 0 \leq x \leq 1/n \\
1 & \text{if } x > 1/n
\end{cases}
$$

for $n \in \mathbb{N}$.

**Step 1: $f_n$ is continuous.**

For each $n$, $f_n$ is continuous on $[0, 1/n)$ (linear), continuous on $(1/n, 1]$ (constant), and continuous at $x = 1/n$ (both one-sided limits equal 1). Thus $f_n \in C([0,1])$. ✓

**Step 2: Compute pointwise limit.**

For each $x \in [0,1]$:
- If $x = 0$: $f_n(0) = 0$ for all $n$, so $\lim_n f_n(0) = 0$
- If $x > 0$: For $n > 1/x$, we have $x > 1/n$, so $f_n(x) = 1$. Thus $\lim_n f_n(x) = 1$

Therefore:
$$
f(x) = \lim_{n \to \infty} f_n(x) = \begin{cases}
0 & \text{if } x = 0 \\
1 & \text{if } x \in (0, 1]
\end{cases} = \mathbf{1}_{(0,1]}(x)
$$

This is the **indicator function** of $(0,1]$, which is **discontinuous** at $x = 0$ (right limit is 1, value at 0 is 0). ✓

**Step 3: Show $f_n \to f$ in $L^1$ norm.**

Compute:
$$
\|f_n - f\|_1 = \int_0^1 |f_n(x) - f(x)| \, dx
$$

For $x \in (0, 1/n]$: $f_n(x) = nx$ and $f(x) = 1$, so $|f_n(x) - f(x)| = |nx - 1|$. Since $x \leq 1/n$, we have $nx \leq 1$, so $|nx - 1| = 1 - nx$ (the expression is non-negative).

For $x \in (1/n, 1]$: $f_n(x) = 1$ and $f(x) = 1$, so $|f_n(x) - f(x)| = 0$.

At $x = 0$: $f_n(0) = 0$ and $f(0) = 0$, so the contribution is 0.

Thus:
$$
\begin{align}
\|f_n - f\|_1 &= \int_0^{1/n} (1 - nx) \, dx \\
&= \left[x - \frac{nx^2}{2}\right]_0^{1/n} \\
&= \frac{1}{n} - \frac{1}{2n} = \frac{1}{2n} \to 0 \quad \text{as } n \to \infty
\end{align}
$$

So $f_n \to f$ in $L^1$ norm. ✓

**Step 4: $\{f_n\}$ is Cauchy.**

For $n \geq m$, by similar computation (or triangle inequality $\|f_n - f_m\|_1 \leq \|f_n - f\|_1 + \|f - f_m\|_1 < 1/(2n) + 1/(2m) \to 0$ as $n, m \to \infty$), $\{f_n\}$ is Cauchy in $L^1$ norm. ✓

**Step 5: No limit in $C([0,1])$.**

We've shown $f_n \to f$ in $L^1$, where $f = \mathbf{1}_{(0,1]}$ is **discontinuous**. But every element of $C([0,1])$ is continuous. Thus $f \notin C([0,1])$.

**Conclusion:** $\{f_n\}$ is Cauchy in $(C([0,1]), \|\cdot\|_1)$ but has **no limit in $C([0,1])$**. The space is **incomplete**. □

---

**Remark 1 (Completion):** The **completion** of $(C([0,1]), \|\cdot\|_1)$ is $L^1([0,1])$ (Lebesgue integrable functions), which includes discontinuous functions like $\mathbf{1}_{(0,1]}$. This is why **Lebesgue integration is necessary**—it "fills in" the limits of Cauchy sequences that Riemann integration misses.

**Remark 2 (Contrast with $\|\cdot\|_\infty$):** If we equip $C([0,1])$ with the **sup norm** $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$, then $(C([0,1]), \|\cdot\|_\infty)$ **is complete** (a well-known theorem). The issue is that $\|\cdot\|_1$ is a **weaker norm** (convergence in $L^1$ does not imply uniform convergence), so Cauchy sequences in $L^1$ can have discontinuous limits.

**Remark 3 (RL Implication):** If we tried to use **continuous value functions** $C(\mathcal{S})$ with $L^1$ norm in RL, value iteration might generate Cauchy sequences that don't converge to continuous functions—algorithms would break down. This is why we use $L^\infty(\mathcal{S})$ or $L^2(\mathcal{S})$ (both complete) instead.

---

## **Exercise 3: Bellman Contraction and Value Iteration (RL Application)** {#EX-3.1.3}

**Statement:** Let $\mathcal{S}$ be a finite state space with $|\mathcal{S}| = n$. Consider the **Bellman policy evaluation operator** $T^\pi: \mathbb{R}^n \to \mathbb{R}^n$ defined by:
$$
(T^\pi V)_s = r_s + \gamma \sum_{s' \in \mathcal{S}} P_{ss'}^\pi V_{s'}
$$

where:
- $r_s$ is the expected reward at state $s$
- $P_{ss'}^\pi = \mathbb{P}(s' | s, \pi)$ is the transition probability under policy $\pi$
- $\gamma \in [0,1)$ is the discount factor

**Tasks:**
1. Show that $T^\pi$ is a **$\gamma$-contraction** in the $\|\cdot\|_\infty$ norm: for all $V, W \in \mathbb{R}^n$,
   $$
   \|T^\pi V - T^\pi W\|_\infty \leq \gamma \|V - W\|_\infty
   $$

2. Use the Banach Fixed-Point Theorem (stated below) to conclude that $T^\pi$ has a **unique fixed point** $V^\pi = T^\pi V^\pi$.

3. Show that the **value iteration** sequence $V_{k+1} = T^\pi V_k$ (starting from any $V_0 \in \mathbb{R}^n$) converges to $V^\pi$ geometrically:
   $$
   \|V_k - V^\pi\|_\infty \leq \gamma^k \|V_0 - V^\pi\|_\infty
   $$

4. Estimate: How many iterations $k$ are needed to achieve $\|V_k - V^\pi\|_\infty < \epsilon$ for given $\epsilon > 0$?

**Banach Fixed-Point Theorem (Statement):** Let $(X, d)$ be a **complete metric space** and $T: X \to X$ a contraction (i.e., $d(Tx, Ty) \leq L \cdot d(x, y)$ for some $L < 1$ and all $x, y \in X$). Then:
1. $T$ has a **unique fixed point** $x^* \in X$ (i.e., $Tx^* = x^*$)
2. For any starting point $x_0 \in X$, the iteration $x_{k+1} = Tx_k$ converges to $x^*$ geometrically: $d(x_k, x^*) \leq L^k d(x_0, x^*)$

(We will prove this in Week 16.)

---

**Solution:**

**Task 1: $T^\pi$ is a $\gamma$-contraction.**

**Proof:** Let $V, W \in \mathbb{R}^n$. For each state $s \in \mathcal{S}$:
$$
\begin{align}
|(T^\pi V)_s - (T^\pi W)_s| &= \left|r_s + \gamma \sum_{s'} P_{ss'}^\pi V_{s'} - r_s - \gamma \sum_{s'} P_{ss'}^\pi W_{s'}\right| \\
&= \left|\gamma \sum_{s'} P_{ss'}^\pi (V_{s'} - W_{s'})\right| \\
&= \gamma \left|\sum_{s'} P_{ss'}^\pi (V_{s'} - W_{s'})\right| \\
&\leq \gamma \left|\sum_{s'} P_{ss'}^\pi (V_{s'} - W_{s'})\right| \\
&\leq \gamma \sum_{s'} P_{ss'}^\pi |V_{s'} - W_{s'}| \quad \text{(triangle inequality; } P_{ss'}^\pi \geq 0 \text{ allows absolute value inside sum)} \\
&\leq \gamma \sum_{s'} P_{ss'}^\pi \|V - W\|_\infty \quad \text{(since } |V_{s'} - W_{s'}| \leq \|V - W\|_\infty) \\
&= \gamma \|V - W\|_\infty \sum_{s'} P_{ss'}^\pi \\
&= \gamma \|V - W\|_\infty \quad \text{(since } \sum_{s'} P_{ss'}^\pi = 1)
\end{align}
$$

Taking the supremum over $s \in \mathcal{S}$:
$$
\|T^\pi V - T^\pi W\|_\infty = \sup_{s \in \mathcal{S}} |(T^\pi V)_s - (T^\pi W)_s| \leq \gamma \|V - W\|_\infty
$$

Since $\gamma < 1$, $T^\pi$ is a contraction with modulus $\gamma$. ✓

---

**Task 2: Unique fixed point via Banach Fixed-Point Theorem.**

**Proof:** The space $(\mathbb{R}^n, \|\cdot\|_\infty)$ is a **complete metric space** (finite-dimensional spaces are always complete). By Task 1, $T^\pi: \mathbb{R}^n \to \mathbb{R}^n$ is a $\gamma$-contraction with $\gamma < 1$.

By the **Banach Fixed-Point Theorem**, $T^\pi$ has a **unique fixed point** $V^\pi \in \mathbb{R}^n$ satisfying:
$$
T^\pi V^\pi = V^\pi
$$

This is the **value function** for policy $\pi$ in RL. ✓

---

**Task 3: Geometric convergence of value iteration.**

**Proof:** Let $V_0 \in \mathbb{R}^n$ be arbitrary. Define the value iteration sequence:
$$
V_{k+1} = T^\pi V_k \quad \text{for } k = 0, 1, 2, \ldots
$$

By the Banach Fixed-Point Theorem, $V_k \to V^\pi$ (the unique fixed point) geometrically:
$$
\|V_k - V^\pi\|_\infty \leq \gamma^k \|V_0 - V^\pi\|_\infty
$$

**Alternative direct proof (without citing Banach):** By the contraction property:
$$
\begin{align}
\|V_{k+1} - V^\pi\|_\infty &= \|T^\pi V_k - T^\pi V^\pi\|_\infty \quad \text{(since } V^\pi = T^\pi V^\pi) \\
&\leq \gamma \|V_k - V^\pi\|_\infty \quad \text{(contraction with modulus } \gamma)
\end{align}
$$

Iterating:
$$
\begin{align}
\|V_k - V^\pi\|_\infty &\leq \gamma \|V_{k-1} - V^\pi\|_\infty \\
&\leq \gamma^2 \|V_{k-2} - V^\pi\|_\infty \\
&\quad \vdots \\
&\leq \gamma^k \|V_0 - V^\pi\|_\infty
\end{align}
$$

Since $\gamma < 1$, $\gamma^k \to 0$ exponentially fast, so $V_k \to V^\pi$ **geometrically** (faster than any polynomial rate). ✓

---

**Task 4: Iteration count for $\epsilon$-accuracy.**

**Question:** How many iterations $k$ are needed to achieve $\|V_k - V^\pi\|_\infty < \epsilon$ for given $\epsilon > 0$?

**Solution:** From Task 3:
$$
\|V_k - V^\pi\|_\infty \leq \gamma^k \|V_0 - V^\pi\|_\infty
$$

We want:
$$
\gamma^k \|V_0 - V^\pi\|_\infty < \epsilon
$$

Rearranging:
$$
\gamma^k < \frac{\epsilon}{\|V_0 - V^\pi\|_\infty}
$$

Since $\gamma < 1$, we have $\log \gamma < 0$. Taking logarithms:
$$
k \log \gamma < \log \left(\frac{\epsilon}{\|V_0 - V^\pi\|_\infty}\right)
$$

Dividing both sides by $\log \gamma$ (and reversing inequality since $\log \gamma < 0$):
$$
k > \frac{\log(\epsilon / \|V_0 - V^\pi\|_\infty)}{\log \gamma}
  = \frac{\log(\epsilon) - \log(\|V_0 - V^\pi\|_\infty)}{\log \gamma}
$$

Multiplying numerator and denominator by $-1$:
$$
k > \frac{\log(\|V_0 - V^\pi\|_\infty / \epsilon)}{-\log \gamma}
$$

**Thus, the minimum number of iterations is:**
$$
k = \left\lceil \frac{\log(\|V_0 - V^\pi\|_\infty / \epsilon)}{-\log \gamma} \right\rceil
$$

(where $\lceil \cdot \rceil$ denotes the ceiling function).

**Complexity:** This is $O(\log(1/\epsilon))$ iterations—**logarithmic** in the desired accuracy $\epsilon$.

**Comparison:** For $\epsilon = 10^{-6}$:
- **Geometric convergence** ($\gamma$-contraction): $O(\log(10^6)) \approx O(14)$ iterations
- **Linear convergence** (rate $\rho < 1$): $O(10^6)$ iterations
- **Sublinear convergence** (rate $O(1/k)$): $O(10^{12})$ iterations

This is **exponentially faster** than polynomial convergence rates.

**Numerical example:** Suppose $\gamma = 0.9$, $\|V_0 - V^\pi\|_\infty = 10$, and we want $\epsilon = 0.01$ accuracy.
$$
k = \left\lceil \frac{\log(10 / 0.01)}{-\log 0.9} \right\rceil = \left\lceil \frac{\log 1000}{-\log 0.9} \right\rceil = \left\lceil \frac{6.91}{0.1054} \right\rceil = \lceil 65.6 \rceil = 66 \text{ iterations}
$$

**Conclusion:** Value iteration achieves $\epsilon$-accuracy in $O(\log(1/\epsilon))$ iterations, thanks to the **geometric convergence** guaranteed by the Banach Fixed-Point Theorem (which requires **completeness** of $\mathbb{R}^n$, a special case of Riesz-Fischer). ✓

---

**Remark 1 (Why completeness matters):** If $\mathbb{R}^n$ were **not complete** (which never happens—finite-dimensional normed spaces are always complete), the Banach Fixed-Point Theorem would **fail**, and we could not guarantee that $V_k$ converges to any value function. In finite dimensions this is automatic, but in **infinite-dimensional continuous state spaces** (where $V^\pi \in L^\infty(\mathcal{S})$), completeness must be **proven** via Riesz-Fischer (Theorem 3.4). Without Riesz-Fischer, we cannot run value iteration in continuous spaces—this is why the theorem matters for RL.

**Remark 2 (Extension to continuous state spaces):** For continuous state spaces $\mathcal{S} = \mathbb{R}^d$, the Bellman operator acts on $L^\infty(\mathcal{S})$:
$$
(T^\pi V)(s) = \mathbb{E}_{a \sim \pi(s), s' \sim P(s'|s,a)}[r(s,a) + \gamma V(s')]
$$

**Technical requirements (compared to finite case):**
1. **Measurability:** Must verify $T^\pi V$ is measurable when $V$ is measurable. This holds if $r$ and $P$ satisfy standard measurability conditions (see [@puterman:mdps:2005, Theorem 6.2.6]).
2. **Boundedness:** Must ensure $\|T^\pi V\|_\infty < \infty$ when $\|V\|_\infty < \infty$. This requires $\sup_s r(s) < \infty$ (bounded rewards).
3. **Contraction proof:** For each $s$, the contraction property follows by Jensen's inequality (or linearity of expectation + triangle inequality):
   $$
   \begin{align}
   |(T^\pi V)(s) - (T^\pi W)(s)| &= \left|\mathbb{E}_{s'}[\gamma(V(s') - W(s'))]\right| \\
   &\leq \mathbb{E}_{s'}[|\gamma(V(s') - W(s'))|] \quad \text{(Jensen; or linearity + abs value)} \\
   &= \gamma \mathbb{E}_{s'}[|V(s') - W(s')|] \\
   &\leq \gamma \mathbb{E}_{s'}[\|V - W\|_\infty] \quad \text{(since } |V(s') - W(s')| \leq \|V - W\|_\infty) \\
   &= \gamma \|V - W\|_\infty \quad \text{(expectation of constant)}
   \end{align}
   $$

   Taking $\sup_s$ on both sides yields $\|T^\pi V - T^\pi W\|_\infty \leq \gamma \|V - W\|_\infty$. This is the same contraction argument as in the finite case, using linearity of expectation rather than finite sums.

**Conclusion:** The contraction property holds in continuous state spaces, and by **Riesz-Fischer** [LEM-3.5], $L^\infty(\mathcal{S})$ is complete, so Banach Fixed-Point Theorem guarantees $V^\pi$ exists.

---

**Remark 2b (Measurability Conditions in Detail):**

For the Bellman operator $T^\pi: L^\infty(\mathcal{S}) \to L^\infty(\mathcal{S})$ defined by:
$$
(T^\pi V)(s) = \mathbb{E}_{a \sim \pi(s), s' \sim P(s'|s,a)}[r(s,a) + \gamma V(s')]
$$

to be well-defined on continuous state spaces $\mathcal{S} \subseteq \mathbb{R}^d$, we need:

1. **State space measurability:** $\mathcal{S}$ is a measurable space with Borel $\sigma$-algebra $\mathcal{B}(\mathcal{S})$
2. **Reward measurability:** $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ is $(\mathcal{B}(\mathcal{S}) \otimes \mathcal{B}(\mathcal{A}))$-measurable
3. **Transition kernel measurability:** $P(\cdot | s, a): \mathcal{B}(\mathcal{S}) \to [0,1]$ is a probability measure for each $(s,a)$, and $(s,a) \mapsto P(B|s,a)$ is measurable for each Borel set $B$
4. **Policy measurability:** $\pi(\cdot | s): \mathcal{B}(\mathcal{A}) \to [0,1]$ is a probability measure, and $s \mapsto \pi(B|s)$ is measurable for each $B$
5. **Bounded rewards:** $\sup_{s,a} |r(s,a)| < \infty$ (ensures $T^\pi$ maps $L^\infty$ to $L^\infty$)

Under these conditions (standard in MDP theory; see [@puterman:mdps:2005, §4.1-4.2] or [@bertsekas:rl_optimal_control:2019, §1.2]):

- **Measurability of $T^\pi V$:** For measurable $V$, the function $(T^\pi V)(s)$ is measurable as a composition of measurable functions (by Fubini-Tonelli, the expectation $\mathbb{E}[\cdots]$ is a measurable function of $s$)

- **Boundedness of $T^\pi V$:** If $\|V\|_\infty < \infty$ and $\sup_{s,a} |r(s,a)| =: R < \infty$, then:
  $$
  |(T^\pi V)(s)| \leq \mathbb{E}[|r(s,a)| + \gamma|V(s')|] \leq R + \gamma\|V\|_\infty < \infty
  $$
  Thus $T^\pi V \in L^\infty(\mathcal{S})$ ✓

- **Contraction property:** Same proof as Remark 2 item 3 (expectation commutes with absolute value via Jensen; sums become integrals)

**Example where measurability matters:** Consider a transition kernel $P(ds'|s,a) = \delta_{f(s,a)}(ds')$ (deterministic dynamics $s' = f(s,a)$). For $T^\pi V$ to be measurable, we need $f: \mathcal{S} \times \mathcal{A} \to \mathcal{S}$ to be measurable (Borel-to-Borel). If $f$ is continuous, this holds automatically. If $f$ is not Borel measurable (e.g., pathological functions constructed via axiom of choice), measurability can fail. However, in standard MDP theory we assume all transition kernels and dynamics are Borel measurable by construction (see [@puterman:mdps:2005, §4.1]), so this pathology does not arise in practice.

**Practical implication:** In RL implementations, we typically assume:
- State space is $\mathbb{R}^d$ (Euclidean, with Borel $\sigma$-algebra)
- Dynamics and rewards are given by neural networks or simulators (measurable by construction)
- These conditions are "automatic" and never checked explicitly

**When measurability matters in practice:**
- **Hybrid systems** (discrete + continuous state): Ensuring Borel measurability at mode switches
- **Black-box simulators** (e.g., game engines): Verifying deterministic dynamics (reproducible given seed)
- **Learned models** (model-based RL): Neural network dynamics are Borel measurable (continuous functions on $\mathbb{R}^d$), but discretization/quantization can break measurability if not handled carefully

In standard RL (tabular, continuous control with smooth dynamics), these issues never arise. But in **hybrid/stochastic switched systems** (robotics, multi-modal control), measurability can fail, and the theory breaks down.

In **theoretical RL** (continuous state spaces, abstract MDPs), measurability conditions are crucial. Without them, statements like "$V^\pi \in L^\infty$" are meaningless.

---

## **Exercise 4: Subsequence Extraction (Proof Technique)** {#EX-3.1.4}

**Statement:** Prove the following lemma used in Step 1 of the Riesz-Fischer proof:

**Lemma (Subsequence Extraction with Rapid Convergence):**
Let $(X, d)$ be a metric space and $\{x_n\}$ a Cauchy sequence in $X$. Then there exists a subsequence $\{x_{n_k}\}$ such that:
$$
\forall k \in \mathbb{N}, \quad d(x_{n_{k+1}}, x_{n_k}) < 2^{-k}
$$

(Rapid convergence rate: the distance between consecutive terms decays geometrically.)

**Guidance:**
- Use the definition of Cauchy: for each $\epsilon > 0$, there exists $N$ such that $n, m \geq N$ implies $d(x_n, x_m) < \epsilon$
- Set $\epsilon = 2^{-k}$ and choose $N_k$ such that $n, m \geq N_k$ implies $d(x_n, x_m) < 2^{-k}$
- Ensure $N_1 < N_2 < N_3 < \ldots$ (strictly increasing)
- Define $x_{n_k} = x_{N_k}$

---

**Solution:**

**Proof of Lemma.**

Let $\{x_n\}$ be Cauchy in $(X, d)$.

**Step 1: Choose indices $N_k$.**

For each $k \in \mathbb{N}$, set $\epsilon_k = 2^{-k}$. By the Cauchy property, there exists $N_k \in \mathbb{N}$ such that:
$$
n, m \geq N_k \Rightarrow d(x_n, x_m) < 2^{-k}
$$

**Step 2: Make indices strictly increasing.**

We may assume (without loss of generality) that $N_1 < N_2 < N_3 < \ldots$ by replacing $N_k$ with $\max(N_1, N_2, \ldots, N_k) + k$ if necessary. (If $N_k \leq N_{k-1}$, increase $N_k$ to $N_{k-1} + 1$; this preserves the Cauchy property since $n, m \geq N_k$ still implies $n, m \geq N_{k-1}$, so $d(x_n, x_m) < 2^{-(k-1)} < 2^{-k}$.)

**Step 3: Define subsequence.**

Define:
$$
x_{n_k} = x_{N_k} \quad \text{for } k = 1, 2, 3, \ldots
$$

**Step 4: Verify rapid convergence.**

For each $k \geq 1$, we have $N_{k+1} > N_k$ (strictly increasing), so $N_{k+1}, N_k \geq N_k$. By the choice of $N_k$:
$$
d(x_{N_{k+1}}, x_{N_k}) < 2^{-k}
$$

Substituting $x_{n_k} = x_{N_k}$:
$$
d(x_{n_{k+1}}, x_{n_k}) < 2^{-k} \quad \text{for all } k \geq 1
$$

This completes the proof. □

---

**Remark 1 (Why geometric decay is essential).**

The geometric decay rate $2^{-k}$ enables the bound:
$$
\sum_{k=1}^\infty \|g_{k+1} - g_k\|_p < \sum_{k=1}^\infty 2^{-k} = 1 < \infty
$$

This is **crucial** for showing $S = |g_1| + \sum_k |g_{k+1} - g_k| \in L^p$ via MCT.

**What if we used slower decay?**
Suppose we only had $\|g_{k+1} - g_k\|_p < 1/k$ (harmonic decay). Then:
$$
\sum_{k=1}^\infty \|g_{k+1} - g_k\|_p < \sum_{k=1}^\infty \frac{1}{k} = \infty
$$

This sum **diverges**, so we couldn't bound $\|S\|_p$, and the proof would fail. We couldn't conclude $S \in L^p$, hence couldn't prove pointwise convergence a.e.

**Lesson:** The Cauchy property alone gives "eventually small" differences $\|g_m - g_n\|_p < \epsilon$ for large $m,n$. But we need **summable** differences $\sum_k \|g_{k+1} - g_k\|_p < \infty$ to prove convergence. Subsequence extraction converts "eventually small" to "summable."

**Remark 2 (General technique):** Subsequence extraction is a **standard technique** in analysis for converting "eventually small" (Cauchy) to "always small" (geometric decay). It appears in:
- Riesz-Fischer theorem (today)
- Proofs of compactness (Arzelà-Ascoli, Banach-Alaoglu, Week 15)
- Stochastic approximation theory (Week 32: subsequence extraction to prove convergence of $\theta_n$ in RL algorithms)

**Remark 3 (Comparison with finite dimensions):** In finite-dimensional spaces $\mathbb{R}^n$, Cauchy sequences **always converge** (by compactness of closed bounded sets), so we don't need to extract subsequences—the full sequence converges. But in **infinite dimensions**, Cauchy sequences may fail to converge without completeness, so subsequence extraction is essential for proving completeness.

---

## **Exercise 5: Reflection on Convergence Modes** {#EX-3.1.5}

**Question:** In the Riesz-Fischer proof, we showed:
1. **Pointwise a.e. convergence:** $g_K(x) \to f(x)$ for $\mu$-almost every $x$ (Step 2)
2. **$L^p$ norm convergence:** $\|g_K - f\|_p \to 0$ (Step 5)

Are these two modes of convergence **equivalent**? That is, does pointwise a.e. convergence imply $L^p$ convergence, and vice versa?

**Tasks:**
1. Construct an example showing pointwise a.e. convergence does **not** imply $L^1$ convergence (counterexample on $\mathbb{R}$).
2. Construct an example showing $L^1$ convergence does **not** imply pointwise a.e. convergence (counterexample on $[0,1]$).
3. State a sufficient condition under which pointwise a.e. convergence **does** imply $L^p$ convergence (hint: Dominated Convergence Theorem).

---

**Solution:**

**Task 1: Pointwise a.e. convergence $\not\Rightarrow$ $L^1$ convergence.**

**Counterexample (on $\mathbb{R}$):** Define $f_n(x) = \frac{1}{n} \mathbf{1}_{[0,n]}(x)$ (indicator function of $[0,n]$).

- **Pointwise a.e. convergence:** For each fixed $x \in \mathbb{R}$, if $x > 0$, then $f_n(x) = 1/n \to 0$ as $n \to \infty$. If $x \leq 0$, $f_n(x) = 0$ for all $n$. Thus $f_n(x) \to 0$ for all $x \in \mathbb{R}$ (pointwise everywhere, hence a.e.).

- **$L^1$ convergence:** Compute:
  $$
  \|f_n - 0\|_1 = \int_\mathbb{R} |f_n(x)| \, dx = \int_0^n \frac{1}{n} \, dx = \frac{1}{n} \cdot n = 1 \quad \text{for all } n
  $$

  Thus $\|f_n\|_1 = 1$ for all $n$, so $\|f_n\|_1 \not\to 0$. Hence $f_n \not\to 0$ in $L^1$ norm.

**Conclusion:** $f_n \to 0$ pointwise a.e., but $f_n \not\to 0$ in $L^1$. ✓

**Intuition (visualize the mass):**
- At time $n=1$: $f_1$ is a rectangle of height 1 over $[0,1]$, with area (mass) = 1.
- At time $n=10$: $f_{10}$ is a rectangle of height 0.1 over $[0,10]$, with area = 1.
- At time $n=100$: $f_{100}$ is a rectangle of height 0.01 over $[0,100]$, with area = 1.

The mass is **constant** (always 1), but it spreads over an ever-wider region. At each fixed point $x$, the height $f_n(x) = 1/n \to 0$, but the integral $\int f_n = 1$ never vanishes.

---

**Task 2: $L^1$ convergence $\not\Rightarrow$ Pointwise a.e. convergence.**

**Counterexample (on $[0,1]$):** Define the "typewriter sequence":
$$
f_n(x) = \mathbf{1}_{I_n}(x)
$$

where $I_n$ is a sequence of intervals in $[0,1]$ that "sweep" across $[0,1]$ repeatedly. Specifically, for $n = 2^k + j$ where $0 \leq j < 2^k$ (i.e., $n$ corresponds to level $k$ and position $j$ in a binary tree):
$$
I_n = [j/2^k, (j+1)/2^k]
$$

**Typewriter sequence visualization:**

| $n$ | Level $k$ | Position $j$ | Interval $I_n$ | $\|I_n\|$ |
|-----|-----------|--------------|----------------|-----------|
| 1   | 0         | 0            | $[0,1]$        | 1         |
| 2   | 1         | 0            | $[0,1/2]$      | 1/2       |
| 3   | 1         | 1            | $[1/2,1]$      | 1/2       |
| 4   | 2         | 0            | $[0,1/4]$      | 1/4       |
| 5   | 2         | 1            | $[1/4,1/2]$    | 1/4       |
| 6   | 2         | 2            | $[1/2,3/4]$    | 1/4       |
| 7   | 2         | 3            | $[3/4,1]$      | 1/4       |
| 8   | 3         | 0            | $[0,1/8]$      | 1/8       |
| ... | ...       | ...          | ...            | ...       |

At level $k$, there are $2^k$ intervals, each of width $2^{-k}$.

**Key observation:** For any fixed $x \in [0,1]$, $x$ appears in exactly one interval at each level $k$. Thus $f_n(x)$ oscillates between 0 and 1 infinitely often—no convergence!

**Properties:**
- **$L^1$ convergence:** $\|f_n\|_1 = \int_0^1 \mathbf{1}_{I_n} \, dx = |I_n| = 2^{-k} \to 0$ as $n \to \infty$ (since $k \to \infty$ as $n \to \infty$). Thus $\|f_n - 0\|_1 = \|f_n\|_1 \to 0$, so $f_n \to 0$ in $L^1$.

- **Pointwise convergence:** For each fixed $x \in [0,1]$, the subsequence $\{f_n(x)\}$ **does not converge**. Why? Because for each $x$, there are infinitely many $n$ such that $x \in I_n$ (so $f_n(x) = 1$) and infinitely many $n$ such that $x \notin I_n$ (so $f_n(x) = 0$). Thus $\{f_n(x)\}$ oscillates between 0 and 1 forever, never settling down.

  **Precisely:** For any $x \in [0,1]$ and any level $k$, there exists a unique $j \in \{0,1,\ldots,2^k-1\}$ such that $x \in [j/2^k, (j+1)/2^k] = I_{2^k+j}$. Thus $f_{2^k+j}(x) = 1$. But for other $j' \neq j$ at the same level, $x \notin I_{2^k+j'}$, so $f_{2^k+j'}(x) = 0$. As $k$ increases, $x$ alternates between being inside and outside the intervals, so $\limsup_n f_n(x) = 1$ and $\liminf_n f_n(x) = 0$—the limit does not exist.

**Conclusion:** $f_n \to 0$ in $L^1$ norm, but $\{f_n(x)\}$ does not converge for **any** $x \in [0,1]$ (not even at a single point). ✓

**Intuition:** The functions $f_n$ have **support** (the set where they're nonzero) that "sweeps" across $[0,1]$, with the width shrinking to 0. The total mass $\|f_n\|_1$ goes to 0, but at each fixed point $x$, the function oscillates between 0 and 1 infinitely often, never settling down.

---

**Task 3: When does pointwise a.e. convergence imply $L^p$ convergence?**

**Answer:** The **Dominated Convergence Theorem** [THM-1.3.2] (Week 1, Day 3) provides a sufficient condition:

**Dominated Convergence Theorem:** Let $f_n \to f$ pointwise $\mu$-a.e., and suppose there exists $g \in L^1(\mu)$ such that $|f_n| \leq g$ $\mu$-a.e. for all $n$ (**domination**). Then:
$$
\lim_{n \to \infty} \int_X f_n \, d\mu = \int_X f \, d\mu
$$

and in particular, $\|f_n - f\|_1 \to 0$ (i.e., $f_n \to f$ in $L^1$).

**Extension to $L^p$:** If $|f_n|^p \leq g$ for some $g \in L^1$, then by DCT applied to $|f_n - f|^p$, we get $\|f_n - f\|_p \to 0$ (i.e., $f_n \to f$ in $L^p$).

**Example where domination saves us:** Consider $f_n(x) = \frac{1}{n} \mathbf{1}_{[0,1]}(x)$ on $[0,1]$.
- Pointwise: $f_n(x) \to 0$ for all $x \in [0,1]$
- Domination: $|f_n(x)| \leq 1 = g(x)$ for all $n$ and all $x \in [0,1]$, where $g \equiv 1 \in L^1([0,1])$
- DCT: $\|f_n\|_1 = \int_0^1 f_n \to \int_0^1 0 = 0$, so $f_n \to 0$ in $L^1$ ✓

**Comparison with counterexample in Task 1:** In Task 1, $f_n(x) = \frac{1}{n} \mathbf{1}_{[0,n]}(x)$ on $\mathbb{R}$, there is **no dominating function** $g \in L^1(\mathbb{R})$ with $f_n \leq g$ for all $n$ (because $f_n$ is supported on $[0,n]$, which grows unboundedly). Thus DCT does not apply, and indeed $f_n \not\to 0$ in $L^1$.

**Summary Table:**

| Mode of Convergence | Implies $L^p$ Convergence? | Counterexample |
|---------------------|----------------------------|----------------|
| Pointwise a.e. alone | ❌ NO | Task 1 (Escaping Mass) |
| $L^p$ convergence alone | ❌ NO (not even pointwise) | Task 2 (Typewriter) |
| **Pointwise a.e. + Domination** | ✅ **YES** (by DCT) | — |

**Key Insight:** DCT = Pointwise convergence + Bounded by integrable function.

**Summary:**
- Pointwise a.e. convergence **alone** does not imply $L^p$ convergence (Task 1 counterexample)
- $L^p$ convergence does not imply pointwise a.e. convergence (Task 2 counterexample)
- **Dominated Convergence** (pointwise a.e. convergence + domination) **does** imply $L^p$ convergence (DCT)

This is why DCT is so powerful—it's the bridge between pointwise and norm convergence.

---

**End of Exercises — Week 3, Day 1**

**Summary:**
- **Exercise 1:** Proved Riesz-Fischer for $L^1$ (completeness via subsequence extraction + Fatou)
- **Exercise 2:** Constructed explicit counterexample showing $(C([0,1]), \|\cdot\|_1)$ is incomplete
- **Exercise 3:** Applied completeness to Bellman operator: proved value iteration converges geometrically in $O(\log(1/\epsilon))$ iterations
- **Exercise 4:** Proved subsequence extraction lemma (key technique in Riesz-Fischer proof)
- **Exercise 5:** Contrasted pointwise a.e. vs. $L^p$ convergence; stated DCT as the bridge

**Key Takeaway:** Completeness of $L^p$ spaces (Riesz-Fischer) is the **bedrock** for RL convergence theory. Without it, value iteration, least-squares TD, and policy gradient methods would lack theoretical guarantees.
