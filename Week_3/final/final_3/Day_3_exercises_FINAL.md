### 📘 Week 3, Day 3: Exercises on Weak Convergence and Dual Topologies

**Companion to:** [[Day_3_draft_revised_all]] — Weak Convergence, Dual Topologies, and RL Applications

**Total time:** ~90-120 minutes (can extend to Thursday if needed)
- **Core exercises** (3.3.1-3.3.3): ~60 minutes
- **Extended RL exercises** (3.3.4-3.3.5): ~60 minutes
- **Recommended split:** Wednesday core + 1 RL exercise (90 min), Thursday remaining RL exercise (30 min)

**Focus:** Understanding weak vs. strong convergence, Banach-Alaoglu compactness, applications to RL (distribution shift, optimal policy existence, finite-state approximation)

**Notation convention:** Following the theory file, $\mu$ denotes abstract measures, $\rho$ denotes state distributions in MDPs.

---

## **Exercise Set 3.3: Weak Convergence and Applications**

### **Exercise 3.3.1 (Weak vs. Strong Convergence in $L^2$)** {#EX-3.3.1} **[20 min]**

Consider the sequence $f_n(x) = \sqrt{2}\sin(2\pi nx)$ on $[0,1]$ with Lebesgue measure.

**(a)** Compute $\|f_n\|_2$ for all $n \geq 1$. Does $f_n \to 0$ in $L^2$ norm?

**(b)** For any $g \in L^2([0,1])$, show that:
$$
\int_0^1 f_n(x) g(x) \, dx \to 0 \quad \text{as } n \to \infty
$$
(Hint: Use Riemann-Lebesgue lemma [LEM-3.24], or for smooth $g$, integrate by parts.)

**(c)** Conclude that $f_n \rightharpoonup 0$ weakly in $L^2([0,1])$ but $f_n \not\to 0$ strongly.

**(d)** Verify the norm lower semicontinuity [PROP-3.17]: $\|0\|_2 \leq \liminf_{n \to \infty} \|f_n\|_2$.

---

**Solution 3.3.1:**

**(a) Computing $\|f_n\|_2$:**

$$
\begin{align}
\|f_n\|_2^2 &= \int_0^1 |f_n(x)|^2 \, dx = \int_0^1 |(\sqrt{2}\sin(2\pi nx)|^2 \, dx \\
&= 2 \int_0^1 \sin^2(2\pi nx) \, dx
\end{align}
$$

**Substitution:** Let $u = 2\pi nx$, so $du = 2\pi n \, dx$. When $x = 0$, $u = 0$; when $x = 1$, $u = 2\pi n$. Thus:
$$
\int_0^1 \sin^2(2\pi nx) \, dx = \frac{1}{2\pi n} \int_0^{2\pi n} \sin^2(u) \, du
$$

**Periodicity:** Since $\sin^2(u)$ has period $\pi$, we have:
$$
\int_0^{2\pi n} \sin^2(u) \, du = 2n \int_0^\pi \sin^2(u) \, du = 2n \cdot \frac{\pi}{2} = \pi n
$$
(using $\int_0^\pi \sin^2(u) du = \pi/2$, standard integral).

Thus:
$$
\int_0^1 \sin^2(2\pi nx) \, dx = \frac{1}{2\pi n} \cdot \pi n = \frac{1}{2}
$$

Therefore:
$$
\|f_n\|_2^2 = 2 \cdot \frac{1}{2} = 1 \quad \Rightarrow \quad \|f_n\|_2 = 1 \quad \text{for all } n \geq 1
$$

**Conclusion:** $\|f_n - 0\|_2 = \|f_n\|_2 = 1 \not\to 0$, so $f_n \not\to 0$ in $L^2$ norm (no strong convergence). ✓

---

**(b) Weak convergence: $\int f_n g \to 0$ for all $g \in L^2$:**

We need to show:
$$
I_n := \int_0^1 \sqrt{2}\sin(2\pi nx) g(x) \, dx \to 0 \quad \text{as } n \to \infty
$$

**Case 1: $g$ is continuously differentiable ($g \in C^1([0,1])$).**

**Integration by parts:** Since $g \in C^1$, we can integrate by parts. Let $u = g(x)$, $dv = \sin(2\pi nx) dx$. Then $du = g'(x) dx$, $v = -\frac{1}{2\pi n}\cos(2\pi nx)$. Thus:
$$
\begin{align}
\int_0^1 \sin(2\pi nx) g(x) \, dx &= \left[-\frac{g(x)}{2\pi n}\cos(2\pi nx)\right]_0^1 + \frac{1}{2\pi n}\int_0^1 \cos(2\pi nx) g'(x) \, dx \\
&= -\frac{g(1)\cos(2\pi n) - g(0)}{2\pi n} + \frac{1}{2\pi n}\int_0^1 \cos(2\pi nx) g'(x) \, dx
\end{align}
$$

Since $\cos(2\pi n) = 1$ for all $n$:
$$
= -\frac{g(1) - g(0)}{2\pi n} + O\left(\frac{1}{n}\right) = O\left(\frac{1}{n}\right) \to 0
$$
(the integral term is bounded by $\|g'\|_1/(2\pi n) \to 0$). ✓

**Case 2: General $g \in L^2$ (by density).**

Continuous functions $C([0,1])$ are dense in $L^2([0,1])$ (standard fact; see [@folland:real_analysis:1999, Proposition 2.10]). For any $g \in L^2$ and $\epsilon > 0$, choose $g_\epsilon \in C([0,1])$ with $\|g - g_\epsilon\|_2 < \epsilon$.

Then:
$$
\begin{align}
|I_n| &= \left|\int_0^1 \sqrt{2}\sin(2\pi nx) g(x) \, dx\right| \\
&\leq \left|\int \sqrt{2}\sin(2\pi nx) g_\epsilon(x) \, dx\right| + \left|\int \sqrt{2}\sin(2\pi nx) (g - g_\epsilon)(x) \, dx\right| \\
&\leq |I_n^{(\epsilon)}| + \|f_n\|_2 \|g - g_\epsilon\|_2 \quad \text{(Cauchy-Schwarz)} \\
&\leq |I_n^{(\epsilon)}| + 1 \cdot \epsilon = |I_n^{(\epsilon)}| + \epsilon
\end{align}
$$

By Case 1, $I_n^{(\epsilon)} \to 0$ as $n \to \infty$ (for fixed $\epsilon$). Thus:
$$
\limsup_{n \to \infty} |I_n| \leq 0 + \epsilon = \epsilon
$$

Since $\epsilon > 0$ was arbitrary, $\limsup |I_n| \leq 0$, hence $I_n \to 0$. ✓

**Alternative (Riemann-Lebesgue Lemma [LEM-3.24]):** For any $g \in L^2([0,1])$, since $L^2 \subset L^1$ on finite measure spaces (by Hölder's inequality: $\|g\|_1 \leq \|g\|_2 \|1\|_2 = \|g\|_2 \cdot 1$), we have $g \in L^1$. By [LEM-3.24]:
$$
\int_0^1 g(x) \sin(2\pi nx) \, dx \to 0 \quad \text{as } n \to \infty
$$

Taking imaginary part: $\int_0^1 g(x) \sin(2\pi nx) dx \to 0$. Thus $I_n \to 0$. □

---

**(c) Conclusion:**

By definition [DEF-3.13-EXPLICIT], $f_n \rightharpoonup 0$ weakly in $L^2([0,1])$ since:
$$
\int f_n g \, dx \to \int 0 \cdot g \, dx = 0 \quad \text{for all } g \in L^2
$$

But $\|f_n - 0\|_2 = 1 \not\to 0$, so $f_n \not\to 0$ strongly. This shows **weak convergence does not imply strong convergence** in infinite dimensions. ✓

---

**(d) Norm lower semicontinuity:**

By [PROP-3.17]:
$$
\|0\|_2 \leq \liminf_{n \to \infty} \|f_n\|_2
$$

Computing:
$$
\|0\|_2 = 0, \quad \liminf \|f_n\|_2 = \liminf 1 = 1
$$

Thus $0 \leq 1$ ✓ (strict inequality, as expected for non-strong convergence).

**Remark:** This example shows why norm lower semicontinuity is the best we can hope for: weak limits can have strictly smaller norm than the $\liminf$ of norms.

---

### **Exercise 3.3.2 (Weak Convergence in $\ell^2$ Sequences)** {#EX-3.3.2} **[15 min]**

Let $e^{(n)} = (0, 0, \ldots, 0, 1, 0, \ldots)$ be the $n$-th standard basis vector in $\ell^2$ (with $1$ in position $n$, zeros elsewhere).

**(a)** Show that $e^{(n)} \rightharpoonup 0$ weakly in $\ell^2$ as $n \to \infty$.

**(b)** Show that $\|e^{(n)}\|_2 = 1$ for all $n$, so $e^{(n)} \not\to 0$ in norm.

**(c)** **RL Connection:** In tabular RL with $|\mathcal{S}| = \infty$ (countable state space), value functions $V \in \ell^\infty(\mathcal{S})$ can be approximated by finite-support functions $V_n$ (zero outside first $n$ states). Explain why weak convergence $V_n \rightharpoonup V$ is sufficient for $\mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V]$ under any probability distribution $\rho$.

---

**Solution 3.3.2:**

**(a) Weak convergence $e^{(n)} \rightharpoonup 0$ in $\ell^2$:**

By [DEF-3.13] with Riesz Representation [THM-3.9], weak convergence in $\ell^2$ means:
$$
\langle e^{(n)}, y \rangle := \sum_{k=1}^\infty e_k^{(n)} y_k \to 0 \quad \text{for all } y = (y_k) \in \ell^2
$$

Since $e^{(n)} = (0, \ldots, 0, 1, 0, \ldots)$ with $1$ in position $n$:
$$
\langle e^{(n)}, y \rangle = \sum_{k=1}^\infty e_k^{(n)} y_k = y_n \quad \text{(only $k=n$ term is nonzero)}
$$

**Claim:** $y_n \to 0$ as $n \to \infty$ for any $y \in \ell^2$.

**Proof of claim:** By definition of $\ell^2$, $\sum_{k=1}^\infty |y_k|^2 < \infty$. For the series to converge, the terms must vanish: $y_k \to 0$ as $k \to \infty$ (necessary condition for convergence of series). Thus $y_n \to 0$. □

Therefore:
$$
\langle e^{(n)}, y \rangle = y_n \to 0 \quad \text{for all } y \in \ell^2
$$

By definition, $e^{(n)} \rightharpoonup 0$ weakly in $\ell^2$. ✓

---

**(b) No strong convergence:**

$$
\|e^{(n)}\|_2^2 = \sum_{k=1}^\infty |e_k^{(n)}|^2 = 1 \quad \text{(only $k=n$ term equals $1^2 = 1$)}
$$

Thus $\|e^{(n)}\|_2 = 1$ for all $n$. Hence:
$$
\|e^{(n)} - 0\|_2 = 1 \not\to 0
$$

So $e^{(n)} \not\to 0$ in norm (no strong convergence). ✓

**Geometric interpretation:** The sequence $\{e^{(n)}\}$ consists of orthonormal vectors in $\ell^2$ (since $\langle e^{(m)}, e^{(n)} \rangle = \delta_{mn}$). They are "spreading apart" in the space—no two are close in norm ($\|e^{(m)} - e^{(n)}\|_2 = \sqrt{2}$ for $m \neq n$). But weakly, they converge to $0$ because they become "more and more orthogonal" to all fixed vectors $y \in \ell^2$.

---

**(c) RL Connection: Finite-Support Approximation of Value Functions:**

**Setup:** Let $\mathcal{S} = \{1, 2, 3, \ldots\}$ (countable infinite state space). Value function $V \in \ell^\infty(\mathcal{S})$ (bounded). Approximate $V$ by finite-support functions:
$$
V_n(s) := \begin{cases} V(s) & \text{if } s \leq n \\ 0 & \text{if } s > n \end{cases}
$$

**Question:** Does $\mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V]$ for a probability distribution $\rho$ on $\mathcal{S}$?

**Answer:** Yes, and weak convergence suffices.

**Step 1: $V_n \to V$ pointwise.**
For each fixed $s \in \mathcal{S}$, once $n \geq s$, we have $V_n(s) = V(s)$. Thus $V_n(s) \to V(s)$ pointwise for all $s$.

**Step 2: Bounded convergence (DCT).**
$|V_n(s)| \leq |V(s)| \leq \|V\|_\infty < \infty$ for all $n, s$. By Dominated Convergence Theorem [DCT-1.3.1]:
$$
\mathbb{E}_\rho[V_n] = \sum_{s \in \mathcal{S}} V_n(s) \rho(s) \to \sum_{s \in \mathcal{S}} V(s) \rho(s) = \mathbb{E}_\rho[V]
$$

**Step 3: Weak convergence interpretation.**
The functional $\phi_\rho(V) = \mathbb{E}_\rho[V] = \sum_s V(s)\rho(s)$ is a continuous linear functional on $\ell^\infty$. Since $\rho$ is a probability distribution, $\rho \in \ell^1$, and we can identify $\rho$ with the functional $\phi_\rho \in (\ell^\infty)^*$ via:
$$
\phi_\rho(V) = \sum_{s \in \mathcal{S}} V(s) \rho(s)
$$

This defines an **embedding** $\ell^1 \hookrightarrow (\ell^\infty)^*$ (though $(\ell^\infty)^*$ is strictly larger than $\ell^1$; the dual also contains finitely additive measures that are not countably additive).

If $V_n \rightharpoonup V$ weakly in $\ell^\infty$, then by definition:
$$
\phi_\rho(V_n) \to \phi_\rho(V) \quad \Rightarrow \quad \mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V]
$$

**Conclusion:** Weak convergence $V_n \rightharpoonup V$ is sufficient for expected value convergence under any distribution $\rho$. In practice, RL algorithms often only require this weaker form of convergence—we don't need $\|V_n - V\|_\infty \to 0$ uniformly over all states.

**Practical note:** For **approximate dynamic programming** with function approximation, value functions $V_\theta$ (e.g., neural networks) may not converge uniformly but can converge weakly or in expectation under the data distribution. This is why empirical performance ($\mathbb{E}_\rho[V_\theta]$) can improve even without uniform convergence guarantees.

---

### **Exercise 3.3.3 (Banach-Alaoglu Application to $\ell^2$)** {#EX-3.3.3} **[20 min]**

**(a)** State the Banach-Alaoglu theorem [THM-3.18] for the dual space $(\ell^2)^*$.

**(b)** Let $\{x_n\}$ be a bounded sequence in $\ell^2$ (i.e., $\sup_n \|x_n\|_2 \leq C < \infty$). Show that there exists a subsequence $\{x_{n_k}\}$ and $x \in \ell^2$ such that $x_{n_k} \rightharpoonup x$ weakly in $\ell^2$.

**(c)** **RL Connection:** In policy iteration for countable-state MDPs, value functions $\{V^{\pi_k}\}$ are bounded ($\|V^{\pi_k}\|_\infty \leq R_{\max}/(1-\gamma)$ for discounted reward $|r(s,a)| \leq R_{\max}$). In **infinite-state MDPs** where policy iteration may not terminate (e.g., no finite optimal policy exists), explain how Banach-Alaoglu guarantees existence of a weak* convergent subsequence.

---

**Solution 3.3.3:**

**(a) Banach-Alaoglu for $(\ell^2)^*$:**

By [THM-3.18], the **closed unit ball** in $(\ell^2)^*$:
$$
B_{(\ell^2)^*} = \{\phi \in (\ell^2)^* : \|\phi\| \leq 1\}
$$
is **weak* compact**.

Since $(\ell^2)^* \cong \ell^2$ (self-dual by [COR-3.10]), this translates to:
$$
B_{\ell^2} = \{x \in \ell^2 : \|x\|_2 \leq 1\} \quad \text{is weakly compact}
$$

**Explicit consequence:** Every bounded sequence $\{x_n\}$ in $\ell^2$ (i.e., $\sup_n \|x_n\|_2 \leq C$) has a subsequence $\{x_{n_k}\}$ that converges weakly to some $x \in \ell^2$.

---

**(b) Extracting weakly convergent subsequence:**

**Given:** $\{x_n\}$ bounded in $\ell^2$, i.e., $\|x_n\|_2 \leq C$ for all $n$.

**Step 1: Normalize.** Define $\tilde{x}_n = x_n / C$. Then $\|\tilde{x}_n\|_2 \leq 1$, so $\tilde{x}_n \in B_{\ell^2}$ (closed unit ball).

**Step 2: Apply Banach-Alaoglu [THM-3.18].** By weak compactness of $B_{\ell^2}$, there exists a subsequence $\{\tilde{x}_{n_k}\}$ and $\tilde{x} \in B_{\ell^2}$ such that:
$$
\tilde{x}_{n_k} \rightharpoonup \tilde{x} \quad \text{(weakly in $\ell^2$)}
$$

**Step 3: Rescale.** Define $x = C\tilde{x}$ and $x_{n_k} = C\tilde{x}_{n_k}$. Then:
$$
\langle x_{n_k}, y \rangle = C\langle \tilde{x}_{n_k}, y \rangle \to C\langle \tilde{x}, y \rangle = \langle x, y \rangle \quad \text{for all } y \in \ell^2
$$
(by linearity of weak convergence). Thus $x_{n_k} \rightharpoonup x$ weakly in $\ell^2$. ✓

**Alternative proof (diagonal argument):** For bounded sequences in $\ell^2$, one can also use a **diagonal argument** (Cantor's diagonal trick) to extract a subsequence converging pointwise, then show weak convergence. See [@brezis:functional_analysis:2011, §3.5] for details.

---

**(c) RL Connection: Existence of Convergent Subsequence in Infinite-State Policy Iteration:**

**Setup:** Consider an MDP with countable state space $\mathcal{S} = \{1, 2, 3, \ldots\}$, discount $\gamma < 1$, and bounded rewards $|r(s,a)| \leq R_{\max}$.

**Policy iteration generates:** Sequence of value functions $\{V^{\pi_k}\}_{k=0}^\infty$ where $V^{\pi_k}$ is the unique solution to:
$$
V^{\pi_k} = T^{\pi_k} V^{\pi_k} = R^{\pi_k} + \gamma P^{\pi_k} V^{\pi_k}
$$

**Boundedness:** By contraction mapping (to be covered in detail in Weeks 13-18):
$$
\|V^{\pi_k}\|_\infty \leq \frac{\|R^{\pi_k}\|_\infty}{1 - \gamma} \leq \frac{R_{\max}}{1 - \gamma} =: C
$$
(uniform bound independent of $k$).

**Finite-state MDPs (correction to earlier draft):** For **finite state/action spaces**, policy iteration **terminates in finite time** (Howard 1960)—there are only finitely many deterministic policies, and policy improvement is strictly monotone (assuming unique optimal policy or consistent tie-breaking). The sequence $\{V^{\pi_k}\}$ converges to $V^*$ in finite steps, so compactness arguments are not needed.

**Infinite-state MDPs (where compactness matters):** For **infinite (countable or continuous) state spaces**, policy iteration may not terminate:
- No finite optimal policy may exist
- Policy improvement may cycle (with pathological tie-breaking)
- Strong convergence $\|V^{\pi_k} - V^*\|_\infty \to 0$ may fail even when an optimal policy exists

In this setting, Banach-Alaoglu provides the key tool:

**Apply Banach-Alaoglu:** The sequence $\{V^{\pi_k}\}$ is bounded in $\ell^\infty(\mathcal{S})$ (with $\|V^{\pi_k}\|_\infty \leq C$). By Banach-Alaoglu [THM-3.18], there exists a subsequence $\{V^{\pi_{k_j}}\}$ and $V^* \in \ell^\infty$ such that:
$$
V^{\pi_{k_j}} \overset{*}{\rightharpoonup} V^* \quad \text{(weak* convergence in $\ell^\infty$)}
$$

**Interpretation:** Even if policy iteration doesn't converge in norm (e.g., no strong convergence), we can extract a weak* convergent subsequence. This weak* limit $V^*$ is a candidate optimal value function (though additional arguments are needed to verify it's actually optimal—see [@bertsekas-tsitsiklis:neuro-dp:1996, Chapter 2] for detailed analysis).

**Why this matters:**
1. **Existence of optimal policies:** Banach-Alaoglu guarantees that $\sup_\pi J(\pi)$ is attained (maximum exists, not just supremum)—provided the objective $J(\pi)$ is weak* continuous (see [THM-3.22]).
2. **Approximate DP:** In function approximation, value iterates $V_\theta^k$ may not converge strongly but can converge weakly or weak*.
3. **Convergence diagnostics:** In practice, monitor $\mathbb{E}_\rho[V^{\pi_k}]$ (expected value under data distribution) rather than $\|V^{\pi_k} - V^*\|_\infty$ (uniform error, harder to achieve in infinite-dimensional settings).

**Modern deep RL:** Neural network policies $\pi_\theta$ with bounded weights $\|\theta\| \leq R$ form a weakly* compact set (by Banach-Alaoglu, since $\theta$ lies in a bounded subset of a Banach space). This ensures gradient descent on $J(\theta)$ can converge to a local optimum (though global optimality is not guaranteed due to non-convexity of neural network parameterizations).

---

### **Exercise 3.3.4 (Distribution Shift and Weak* Convergence)** {#EX-3.3.4} **[30 min]**

In policy gradient methods, the state distribution $\rho_{\pi_\theta}$ changes as $\theta$ is updated via gradient descent.

**(a)** Let $\mathcal{S} = \{1, 2, \ldots, n\}$ (finite state space). Define what it means for a sequence of probability distributions $\{\rho_k\}$ on $\mathcal{S}$ to converge **weak*** to $\rho$.

**(b)** Suppose $\rho_k \overset{*}{\rightharpoonup} \rho$ (weak*) and $V_k \to V$ uniformly ($\|V_k - V\|_\infty \to 0$). Prove [PROP-3.21]:
$$
\mathbb{E}_{\rho_k}[V_k(s)] \to \mathbb{E}_\rho[V(s)]
$$

**(c)** **RL Application:** In practice, policy gradient descent $\theta_{k+1} = \theta_k + \alpha \nabla_\theta J(\theta_k)$ induces $\rho_{\pi_\theta}$. If $\theta_k \to \theta^*$, explain why $\rho_{\pi_{\theta_k}} \overset{*}{\rightharpoonup} \rho_{\pi_{\theta^*}}$ (under continuity assumptions on $\pi_\theta$).

---

**Solution 3.3.4:**

**(a) Weak* Convergence of Probability Distributions (Finite $\mathcal{S}$):**

**Definition:** A sequence of probability distributions $\{\rho_k\}$ on finite $\mathcal{S} = \{1, \ldots, n\}$ converges **weak*** to $\rho$ if:
$$
\sum_{s \in \mathcal{S}} f(s) \rho_k(s) \to \sum_{s \in \mathcal{S}} f(s) \rho(s) \quad \text{for all } f: \mathcal{S} \to \mathbb{R} \tag{3.46}
$$

Since $\mathcal{S}$ is finite, every function $f: \mathcal{S} \to \mathbb{R}$ is bounded, so this definition coincides with **weak convergence of measures** in probability theory (see [DEF-3.15] for the general continuous-state version).

**Equivalent characterization (finite case):** For finite $\mathcal{S}$, weak* convergence is equivalent to **pointwise convergence**:
$$
\rho_k(s) \to \rho(s) \quad \text{for all } s \in \mathcal{S}
$$

**Proof of equivalence:** ($\Leftarrow$) If $\rho_k(s) \to \rho(s)$ for all $s$, then:
$$
\sum_{s} f(s) \rho_k(s) \to \sum_s f(s) \rho(s) \quad \text{(finite sum, continuity of linear combination)}
$$

($\Rightarrow$) Conversely, if $\sum_s f(s) \rho_k(s) \to \sum_s f(s) \rho(s)$ for all $f$, take $f = \mathbf{1}_{\{s_0\}}$ (indicator of state $s_0$). Then:
$$
\rho_k(s_0) = \sum_s \mathbf{1}_{\{s_0\}}(s) \rho_k(s) \to \sum_s \mathbf{1}_{\{s_0\}}(s) \rho(s) = \rho(s_0)
$$

Thus pointwise convergence holds. □

**Remark:** For **infinite or continuous** $\mathcal{S}$, weak* convergence of measures is **weaker** than pointwise convergence (e.g., $\delta_{1/n} \overset{*}{\rightharpoonup} \delta_0$ in the Dirac sense, but $\delta_{1/n}(\{0\}) = 0 \not\to 1 = \delta_0(\{0\})$ pointwise).

---

**(b) Proof of [PROP-3.21]: Objective Convergence Under Weak* + Uniform:**

**Given:**
1. $\rho_k \overset{*}{\rightharpoonup} \rho$ (weak* convergence of distributions)
2. $V_k \to V$ uniformly (i.e., $\|V_k - V\|_\infty \to 0$)

**To prove:** $\mathbb{E}_{\rho_k}[V_k] \to \mathbb{E}_\rho[V]$.

**Proof:**

Write:
$$
\begin{align}
\left|\mathbb{E}_{\rho_k}[V_k] - \mathbb{E}_\rho[V]\right| &= \left|\sum_{s \in \mathcal{S}} V_k(s) \rho_k(s) - \sum_s V(s) \rho(s)\right| \\
&\leq \underbrace{\left|\sum_s V_k(s) \rho_k(s) - \sum_s V(s) \rho_k(s)\right|}_{\text{Term A}} + \underbrace{\left|\sum_s V(s) \rho_k(s) - \sum_s V(s) \rho(s)\right|}_{\text{Term B}}
\end{align}
$$

**Bounding Term A (Uniform Convergence):**
$$
\text{Term A} = \left|\sum_s (V_k(s) - V(s)) \rho_k(s)\right| \leq \sum_s |V_k(s) - V(s)| \rho_k(s)
$$

By uniform convergence $\|V_k - V\|_\infty \to 0$:
$$
\leq \|V_k - V\|_\infty \sum_s \rho_k(s) = \|V_k - V\|_\infty \cdot 1 \to 0
$$
(since $\sum_s \rho_k(s) = 1$ for probability distributions). ✓

**Bounding Term B (Weak* Convergence):**
$$
\text{Term B} = \left|\sum_s V(s) \rho_k(s) - \sum_s V(s) \rho(s)\right| = \left|\mathbb{E}_{\rho_k}[V] - \mathbb{E}_\rho[V]\right|
$$

By weak* convergence $\rho_k \overset{*}{\rightharpoonup} \rho$ (definition (3.46)) and boundedness of $V$ (since $\|V\|_\infty < \infty$):
$$
\mathbb{E}_{\rho_k}[V] \to \mathbb{E}_\rho[V] \quad \Rightarrow \quad \text{Term B} \to 0
$$
✓

**Conclusion:** Both Term A and Term B $\to 0$, so:
$$
\left|\mathbb{E}_{\rho_k}[V_k] - \mathbb{E}_\rho[V]\right| \to 0 \quad \Rightarrow \quad \mathbb{E}_{\rho_k}[V_k] \to \mathbb{E}_\rho[V] \quad \square
$$

**Remark:** This proof generalizes to infinite $\mathcal{S}$ (e.g., continuous state spaces) as long as:
1. $V_k \to V$ uniformly (or in $L^\infty$ norm)
2. $\rho_k \overset{*}{\rightharpoonup} \rho$ in the weak* topology of measures

The key is separating the "function convergence" (Term A, uniform) from "measure convergence" (Term B, weak*).

---

**(c) RL Application: Continuity of State Distribution in Policy Gradients:**

**Setup:** Policy $\pi_\theta: \mathcal{S} \times \mathcal{A} \to [0,1]$ (parameterized by $\theta \in \mathbb{R}^d$). State distribution $\rho_{\pi_\theta}$ is the stationary distribution of the Markov chain induced by $\pi_\theta$ (for discounted infinite-horizon MDPs, $\rho_{\pi_\theta}$ is the normalized discounted visitation frequency).

**Claim:** If $\theta_k \to \theta^*$ (parameter convergence) and $\pi_\theta$ is continuous in $\theta$, then:
$$
\rho_{\pi_{\theta_k}} \overset{*}{\rightharpoonup} \rho_{\pi_{\theta^*}} \quad \text{(weak* convergence of distributions)}
$$

**Proof sketch:**

**Step 1: Policy continuity.** Assume $\pi_\theta(a|s)$ is continuous in $\theta$ for each fixed $(s,a)$. Then:
$$
\theta_k \to \theta^* \quad \Rightarrow \quad \pi_{\theta_k}(a|s) \to \pi_{\theta^*}(a|s) \quad \text{for all } (s,a)
$$

**Step 2: Transition kernel continuity.** The transition kernel $P^{\pi_\theta}(s'|s) = \sum_a \pi_\theta(a|s) P(s'|s,a)$ is continuous in $\theta$ (composition of continuous functions).

**Step 3: Stationary distribution continuity.** For finite $\mathcal{S}$, the stationary distribution $\rho_\pi$ solves:
$$
\rho_\pi = \rho_\pi P^{\pi} \quad \text{(eigenvector of $P^\pi$ with eigenvalue $1$)}
$$

By **continuity of stationary distributions** (see [@levin-peres:markov_chains:2017, Theorem 1.8]), if $P^{(k)} \to P$ entrywise and all chains are irreducible aperiodic, then:
$$
\rho^{(k)} \to \rho \quad \text{(pointwise convergence of stationary distributions)}
$$

**Proof sketch:** The stationary distribution is the normalized Perron-Frobenius eigenvector of $P$ (eigenvalue $\lambda = 1$). Eigenvectors vary continuously with matrix entries by perturbation theory for simple eigenvalues (see [@horn-johnson:matrix_analysis:2013, Theorem 6.3.12]). □

Thus:
$$
P^{\pi_{\theta_k}} \to P^{\pi_{\theta^*}} \quad \Rightarrow \quad \rho_{\pi_{\theta_k}} \to \rho_{\pi_{\theta^*}} \quad \text{(pointwise)}
$$

By (a), pointwise convergence of distributions on finite $\mathcal{S}$ is equivalent to weak* convergence. □

**For continuous $\mathcal{S}$:** The argument generalizes using **weak convergence of Markov kernels** [@billingsley:convergence:1999, Theorem 6.7]. The key requirement is that $P^\pi(s'|s)$ depends continuously on $\pi$ in a suitable topology (e.g., total variation or weak).

**Why this matters in RL:**

1. **Objective continuity:** If $\rho_{\pi_\theta}$ converges weak* and $V^{\pi_\theta}$ converges uniformly, then $J(\theta) = \mathbb{E}_{\rho_{\pi_\theta}}[V^{\pi_\theta}]$ is continuous (by (b)). This justifies gradient descent on $J(\theta)$.

2. **Distribution shift:** In off-policy RL, the data distribution $\rho_{\text{data}}$ may differ from $\rho_{\pi_\theta}$. If $\rho_{\text{data}}$ converges weak* to $\rho_{\pi_\theta}$, then empirical estimates $\hat{J} = \frac{1}{N}\sum_{i=1}^N V(s_i)$ (with $s_i \sim \rho_{\text{data}}$) converge to $J(\theta) = \mathbb{E}_{\rho_{\pi_\theta}}[V]$.

3. **Distribution mismatch and importance sampling:**

**Experience replay** [@mnih:dqn:2015] stores transitions $(s, a, r, s')$ in a buffer and samples uniformly for training. This creates a **distribution mismatch**:
- Data distribution: $\rho_{\text{replay}} = \text{Uniform}(\mathcal{D})$ (uniform over buffer)
- Target distribution: $\rho_{\pi_\theta}$ (on-policy state-action visitation)

**Theory-practice gap:** Q-learning theory ([@watkins:qlearning:1992]) is inherently **off-policy** (learns $Q^*$ under behavior policy $\epsilon$-greedy). However, classical convergence proofs assume samples from a **fixed distribution**. With experience replay, the data distribution is **non-stationary** (a changing mixture of past policies), violating this assumption.

**Why DQN works despite this:**
- **Contraction:** The Bellman operator $T^* Q = \max_a (r + \gamma P Q)$ is a contraction in $\|\cdot\|_\infty$ (uniform convergence), **independent of the sampling distribution** (Weeks 16-18). This robustness to distribution mismatch is why off-policy Q-learning works.
- **Exploration:** $\epsilon$-greedy ensures sufficient coverage of the state-action space, mitigating the staleness of replay buffer data.
- **Target networks:** Slow-moving target $Q_{\theta^-}$ reduces non-stationarity (targets update every $C$ steps).

**Proper off-policy methods use importance sampling corrections:**
- **Off-policy actor-critic** [@degris:off_policy_ac:2012]: Multiply gradient by $\pi_\theta(a|s)/\mu(a|s)$ (importance ratio) to correct for distribution mismatch
- **Retrace** [@munos:retrace:2016]: Multi-step off-policy correction with bounded importance weights for variance reduction
- **V-trace** [@espeholt:impala:2018]: Clipped importance weights $\min(c, \pi_\theta/\mu)$ for stability in distributed training

These methods **do** rely on weak* convergence: as the behavior policy $\mu$ approaches the target policy $\pi_\theta$, the importance ratio $\pi_\theta/\mu \to 1$ and variance decreases. This is closely related to $\mu \overset{*}{\rightharpoonup} \pi_\theta$ (weak* convergence of policies).

---

### **Exercise 3.3.5 (Projection Continuity in LSTD)** {#EX-3.3.5} **[30 min, optional—can defer to Friday]**

In least-squares temporal difference learning (LSTD), we project the Bellman operator onto a feature subspace.

**(a)** Let $\mathcal{V} = \text{span}(\phi_1, \ldots, \phi_d) \subset L^2(\mu)$ be a finite-dimensional subspace of $L^2(\mu)$. Define the **orthogonal projection** $\Pi: L^2 \to \mathcal{V}$ as:
$$
\Pi V = \arg\min_{W \in \mathcal{V}} \|V - W\|_2
$$
Show that $\Pi$ is a **bounded linear operator** with $\|\Pi\| \leq 1$.

**(b)** Prove [PROP-3.23]: If $V_n \rightharpoonup V$ weakly in $L^2$, then $\Pi V_n \rightharpoonup \Pi V$ weakly.

**(c)** **RL Application:** In LSTD, the projected Bellman equation is:
$$
\Pi T^\pi V_\theta = V_\theta
$$
If approximate value functions $\tilde{V}_n$ converge weakly to $V^{\pi}$, discuss the relationship between $\Pi \tilde{V}_n$ and the LSTD fixed point. What are the limitations of this weak convergence perspective for practical LSTD?

---

**Solution 3.3.5:**

**(a) Projection is Bounded Linear Operator:**

**Linearity:** For any $V_1, V_2 \in L^2$ and $a, b \in \mathbb{R}$:
$$
\Pi(aV_1 + bV_2) = \arg\min_{W \in \mathcal{V}} \|aV_1 + bV_2 - W\|_2
$$

By uniqueness of the projection (orthogonal projection onto a closed convex set in Hilbert space is unique; this is the **Projection Theorem**, which we will prove when we study Hilbert spaces in Weeks 13-18; by the Projection Theorem, to be proved in Week 14):
$$
\Pi(aV_1 + bV_2) = a\Pi V_1 + b\Pi V_2
$$
(linear combination of projections equals projection of linear combination). ✓

**Boundedness:** For any $V \in L^2$:
$$
\|\Pi V\|_2 = \|\Pi V - 0\|_2 \leq \|V - 0\|_2 = \|V\|_2
$$
(since $0 \in \mathcal{V}$ is a candidate for the minimizer, and the projection minimizes distance to $\mathcal{V}$). Thus:
$$
\|\Pi V\|_2 \leq \|V\|_2 \quad \Rightarrow \quad \|\Pi\| = \sup_{\|V\|_2 \leq 1} \|\Pi V\|_2 \leq 1
$$

**Conclusion:** $\Pi$ is a bounded linear operator with $\|\Pi\| \leq 1$. ✓

---

**(b) Proof of [PROP-3.23]: Weak Continuity of Projection:**

**Given:** $V_n \rightharpoonup V$ weakly in $L^2$.

**To prove:** $\Pi V_n \rightharpoonup \Pi V$ weakly.

**Proof:** By definition of weak convergence [DEF-3.13], we need to show:
$$
\langle \Pi V_n, g \rangle \to \langle \Pi V, g \rangle \quad \text{for all } g \in L^2
$$

**Key property:** The projection $\Pi: L^2 \to L^2$ is **self-adjoint** (i.e., $\Pi^* = \Pi$, where $\Pi^*$ is the adjoint operator). This follows from the orthogonal projection theorem: for orthogonal projections, $\langle \Pi f, g \rangle = \langle f, \Pi g \rangle$ for all $f, g \in L^2$ (see [@brezis:functional_analysis:2011, Theorem 5.2 and Corollary 5.4] for proof that orthogonal projections are self-adjoint).

Using self-adjointness:
$$
\langle \Pi V_n, g \rangle = \langle V_n, \Pi^* g \rangle = \langle V_n, \Pi g \rangle
$$

By weak convergence $V_n \rightharpoonup V$:
$$
\langle V_n, \Pi g \rangle \to \langle V, \Pi g \rangle \quad \text{(since $\Pi g \in L^2$)}
$$

By self-adjointness again:
$$
\langle V, \Pi g \rangle = \langle \Pi V, g \rangle
$$

Combining:
$$
\langle \Pi V_n, g \rangle = \langle V_n, \Pi g \rangle \to \langle V, \Pi g \rangle = \langle \Pi V, g \rangle
$$

Thus $\langle \Pi V_n, g \rangle \to \langle \Pi V, g \rangle$ for all $g \in L^2$, so $\Pi V_n \rightharpoonup \Pi V$ weakly. □

**Remark:** This proof crucially uses that $\Pi$ is self-adjoint (orthogonal projection). For non-orthogonal projections, weak continuity may fail.

---

**(c) RL Application: LSTD Convergence and Limitations of Weak Convergence Analysis:**

**Setup:** In LSTD, we solve the projected Bellman equation:
$$
\Pi T^\pi V_\theta = V_\theta \tag{3.47}
$$
where $\Pi$ is the orthogonal projection onto the feature space $\mathcal{V} = \text{span}(\phi_1, \ldots, \phi_d) \subset L^2(\mu)$, and $T^\pi V = R^\pi + \gamma P^\pi V$ is the Bellman operator.

**Question:** Suppose we have approximate value functions $\tilde{V}_n$ (e.g., from Monte Carlo rollouts or TD updates) that converge weakly to the true value $V^{\pi}$:
$$
\tilde{V}_n \rightharpoonup V^\pi \quad \text{(weakly in $L^2(\mu)$)}
$$

What is the relationship between $\Pi \tilde{V}_n$ and the LSTD fixed point?

**Answer:** The LSTD solution $V_\theta^*$ is the unique fixed point of the **projected Bellman operator** $\Pi T^\pi$:
$$
V_\theta^* = \Pi T^\pi V_\theta^*
$$

This is **distinct** from $\Pi V^\pi$ (the orthogonal projection of the true value function) unless $V^\pi$ lies in the feature space $\mathcal{V}$. In general:
$$
\|\Pi V^\pi - V^\pi\|_2 = 0 \quad \text{iff } V^\pi \in \mathcal{V} \quad \text{(rare in function approximation)}
$$

**Error bound:** By [@tsitsiklis-vanroy:lstd:1997, Theorem 3], the LSTD approximation error satisfies:
$$
\|V_\theta^* - V^\pi\|_\mu \leq \frac{1}{\sqrt{1 - \gamma^2}} \min_{V \in \mathcal{V}} \|V - V^\pi\|_\mu
$$
where $\|\cdot\|_\mu$ is the weighted $L^2(\mu)$ norm under the **on-policy state distribution** $\mu = \rho^\pi$ (stationary distribution of the Markov chain induced by $\pi$). For off-policy learning with data distribution $\rho_{\text{data}} \neq \rho^\pi$, the bound involves importance sampling corrections (see [@precup-sutton-singh:off_policy_td:2001]).

**Why weak convergence matters (and why it's not enough):** If $\tilde{V}_n \rightharpoonup V^\pi$ weakly, then by [PROP-3.23], $\Pi \tilde{V}_n \rightharpoonup \Pi V^\pi$ weakly. However:
1. The LSTD iterate $({\Pi T^\pi})^k V_0$ converges to $V_\theta^* = \Pi T^\pi V_\theta^*$, **not** $\Pi V^\pi$ (unless $T^\pi V^\pi = V^\pi$ and $V^\pi \in \mathcal{V}$, which would require $V^\pi$ to be in the feature space and satisfy the Bellman equation—a very strong condition rarely met in practice).
2. LSTD convergence in practice depends on the **contraction properties of $\Pi T^\pi$**, not primarily on weak continuity of $\Pi$. The operator $\Pi T^\pi$ is a contraction in the weighted $L^2(\rho^\pi)$ norm with modulus $\gamma$ ([@bertsekas-tsitsiklis:neuro-dp:1996, Proposition 4.2]), which guarantees strong convergence of LSTD iterates.

**Limitations of weak convergence perspective:**
- Weak convergence $\tilde{V}_n \rightharpoonup V^\pi$ doesn't directly imply convergence of TD/LSTD iterates to the fixed point $V_\theta^*$.
- The bottleneck in LSTD is not weak continuity of $\Pi$ but rather:
  - Sample complexity (finite data, estimation error in projections)
  - Contraction rate $\gamma$ (controls convergence speed)
  - Off-policy corrections (importance sampling variance)

**Why weak convergence still matters:**
1. **Robustness to approximation error:** LSTD doesn't require $\tilde{V}_n \to V^\pi$ in norm (strong convergence). Weak convergence suffices for some theoretical guarantees (e.g., consistency of empirical projections).
2. **Sample efficiency:** With finite samples, empirical estimates $\hat{V}_n = \frac{1}{N}\sum_{i=1}^N r_i + \gamma V(s_i')$ converge weakly to $V^\pi$ (by Law of Large Numbers). Weak continuity of $\Pi$ ensures $\Pi \hat{V}_n$ has good limiting behavior.
3. **Neural network features:** When features $\phi_\theta$ come from a neural network (deep RL), exact projections are intractable. Weak convergence analysis suggests that approximate projections (e.g., SGD on $\|\tilde{V} - V_\theta\|_2^2$) may suffice, though formal convergence guarantees remain elusive for neural network function approximation.

**Practical note:** Modern deep RL algorithms (e.g., DQN [@mnih:dqn:2015], Rainbow [@hessel:rainbow:2018]) use neural networks $V_\theta$ without explicit projection operators. Weak convergence analysis provides conceptual insight into why approximate projections might work, but does **not** provide formal convergence guarantees. The theory-practice gap here is substantial: empirical success of deep RL far outpaces our theoretical understanding.

**Additional references needed:**
- [@tsitsiklis-vanroy:lstd:1997] for LSTD error bounds
- [@bertsekas-tsitsiklis:neuro-dp:1996, Section 6.3] for projected Bellman equations and contraction properties

---

### **Reflection Questions:**

1. **Why is Banach-Alaoglu (weak* compactness) more useful than norm compactness in RL?**
   *Hint:* Norm compactness fails in infinite dimensions (unit ball in $L^2$ is not norm-compact). But weak* compactness (Banach-Alaoglu) always holds, enabling existence proofs for optimal policies even in infinite-dimensional settings.

2. **When is strong convergence necessary in RL, and when does weak convergence suffice?**
   *Hint:* Strong convergence $\|V_n - V^*\|_\infty \to 0$ needed for uniform error bounds (all states). Weak convergence $\mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V^*]$ suffices for objective convergence (expected value under a distribution).

3. **How does weak* convergence of distributions formalize "distribution shift" in policy gradients?**
   *Hint:* As $\theta_k \to \theta^*$, the state distribution $\rho_{\pi_{\theta_k}}$ changes. Weak* convergence $\rho_{\pi_{\theta_k}} \overset{*}{\rightharpoonup} \rho_{\pi_{\theta^*}}$ ensures $J(\theta_k) = \mathbb{E}_{\rho_{\pi_{\theta_k}}}[V^{\pi_{\theta_k}}] \to J(\theta^*)$ (objective continuity).

---

**Summary:**

**What we learned:**
- Weak convergence $f_n \rightharpoonup f$ in $L^p$: convergence tested by all $g \in L^q$ (conjugate)
- Weak* convergence $\phi_n \overset{*}{\rightharpoonup} \phi$ in $(L^p)^*$: convergence tested by all $f \in L^p$
- Strong $\Rightarrow$ weak, but not conversely (Example: $\sin(2\pi nx) \rightharpoonup 0$ weakly but not strongly)
- Banach-Alaoglu [THM-3.18]: Bounded sequences in $(L^p)^*$ have weak* convergent subsequences (compactness)
- RL applications:
  - Infinite-state value iteration: weak convergence sufficient for expectation convergence
  - Distribution shift: $\rho_{\pi_\theta}$ converges weak* under policy continuity
  - Existence of optimal policies: compactness via Banach-Alaoglu
  - LSTD: projection weakly continuous, but contraction properties more fundamental

**Time allocation:** ~90-120 minutes total
- Core exercises (3.3.1-3.3.3): ~60 min
- Extended RL exercises (3.3.4-3.3.5): ~60 min
- **Recommended:** Wednesday core + Exercise 3.3.4 (90 min), Thursday Exercise 3.3.5 (30 min)

---

**End of Exercises**
