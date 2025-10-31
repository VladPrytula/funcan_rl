### Agenda:

##### 📘 Day 3 — Week 3: Weak Convergence, Dual Topologies, and RL Applications of $L^p$ Duality

**Total time: ~120-150 minutes (Wednesday, extended)**
- **Theory core**: 90-120 minutes (Sections I-III)
- **Exercises**: 90-120 minutes (can extend to Thursday; see companion exercise file)
- **Realistic total**: 2.5-3 hours for mastery of weak convergence + Banach-Alaoglu

**Note on pacing**: This is dense foundational material. The Syllabus originally allocated 90 minutes, but weak convergence and Banach-Alaoglu are cornerstone results requiring careful study. We recommend:
- **Wednesday (today)**: Theory core (Sections I-II) + 2-3 exercises (90-120 min total)
- **Thursday morning**: Remaining exercises + extended proof review (60 min)
- **Friday**: Synthesis and numerical experiments

**Syllabus alignment note**: The Syllabus.md Week 3 outline described "continuing $(L^p)^*$ duality" on Day 3. We have reorganized to cover **weak/weak* convergence and Banach-Alaoglu** today, as this is the natural continuation of duality (Day 2 identified dual spaces; Day 3 studies topologies on these spaces). The Radon-Nikodym theorem (originally Day 3-4) moves to Thursday as planned. This reorganization improves mathematical flow: completeness (Day 1) → duality (Day 2) → topologies on dual spaces (Day 3) → densities and measures (Day 4).

---

#### **⏱️ Segment 1 (40 min) — Reading**

**Topic:** _Weak and weak* convergence in dual spaces, deeper RL applications of duality_

- Continue from **Folland §6.3-6.4** [@folland:real_analysis:1999, §6.3-6.4] ($L^p$ duality) or **Brezis Ch 3** [@brezis:functional_analysis:2011, Ch 3] (Weak Convergence)
- Focus on:
    - **Weak convergence** $f_n \rightharpoonup f$ in $L^p$: $\phi(f_n) \to \phi(f)$ for all $\phi \in (L^p)^*$
    - **Weak* convergence** $\phi_n \overset{*}{\rightharpoonup} \phi$ in $(L^p)^*$: $\phi_n(f) \to \phi(f)$ for all $f \in L^p$
    - **Relationship to strong convergence**: Weak convergence ⇐ strong convergence ($\|f_n - f\|_p \to 0$)
    - **Non-equivalence**: Sequences can converge weakly but not strongly
    - **Compactness**: Banach-Alaoglu theorem (weak* compactness of unit ball)
    - **RL significance**: Convergence of value function approximations, policy gradient convergence, distribution shift

---

#### **⏱️ Segment 2 (60-80 min) — Theory and Examples**

**Primary Task:**
1. **Define weak and weak* convergence** formally
2. **Understand key examples**:
   - In $L^2$: $f_n(x) = \sin(nx)$ converges weakly to $0$ but not strongly
   - In $(L^\infty)^*$: Dirac delta sequence converging weak*
3. **Banach-Alaoglu theorem**: Unit ball in $(L^p)^*$ is weak* compact (full proof in Appendix 3.A)
4. **Apply to RL**:
   - Infinite-state value iteration: weak convergence when strong fails
   - Distribution shift: state distributions converging weak* in policy gradients
   - Existence of optimal policies via compactness
   - (LSTD discussion deferred to Friday synthesis)

**Guidance:**
- Weak convergence is **strictly weaker** than norm convergence (hence the name)
- In infinite dimensions, bounded sequences need not have convergent subsequences in norm topology
- But bounded sequences in $(L^p)^*$ **always** have weak* convergent subsequences (Banach-Alaoglu)
- This is crucial for existence proofs in RL (e.g., showing optimal policies exist)

---

## **Chapter 3.3: Weak Convergence and Dual Topologies**

### **Motivation: Multiple Notions of Convergence**

Recall from Week 1 that we studied various modes of convergence for functions:
- **Pointwise convergence**: $f_n(x) \to f(x)$ for each $x$
- **Uniform convergence**: $\sup_x |f_n(x) - f(x)| \to 0$
- **$L^p$ convergence** (norm convergence): $\|f_n - f\|_p \to 0$
- **Almost everywhere convergence**: $f_n(x) \to f(x)$ for $\mu$-almost all $x$

Each mode has different strength and implications. Today we add two more notions, crucial for functional analysis and RL:
- **Weak convergence**: Convergence "tested" by all continuous linear functionals
- **Weak* convergence**: Convergence in the dual space topology

**Why do we need these?** Consider a concrete challenge from reinforcement learning: In policy gradient descent, we optimize $J(\theta) = \mathbb{E}_{\rho_{\pi_\theta}}[V^{\pi_\theta}(s)]$ where both the state distribution $\rho$ and the value function $V$ change at each iteration. When does $J(\theta_k)$ converge? The distributions $\{\rho_{\pi_{\theta_k}}\}$ may not converge in total variation distance (strong convergence of measures), yet $J(\theta_k)$ can still converge if the distributions converge in a weaker sense—**weak* convergence**—which turns out to be sufficient for objective convergence.

More broadly: In infinite-dimensional spaces, norm-bounded sequences need not have norm-convergent subsequences. But Banach-Alaoglu guarantees that bounded sequences in dual spaces always have **weak* convergent subsequences**. This compactness result is essential for existence theorems in optimization and RL.

---

### **I. Weak Convergence in $L^p$**

Yesterday we identified the dual spaces $(L^p)^* \cong L^q$ via the Riesz Representation Theorem [THM-3.9]. Today we study the natural topology on these dual spaces.

**Explicit Definition via Riesz Representation.** {#DEF-3.13-EXPLICIT}

Let $(X, \mathcal{F}, \mu)$ be a measure space and $1 < p < \infty$ with conjugate exponent $q$ (where $1/p + 1/q = 1$). By [THM-3.9], every continuous linear functional $\phi \in (L^p)^*$ has the form $\phi(f) = \int fg \, d\mu$ for unique $g \in L^q$.

A sequence $\{f_n\}$ in $L^p(\mu)$ **converges weakly** to $f \in L^p$ if:
$$
\int f_n g \, d\mu \to \int f g \, d\mu \quad \text{for all } g \in L^q \tag{3.35}
$$

We write $f_n \rightharpoonup f$ (weak limit).

**Abstract Definition (General Dual Spaces).** {#DEF-3.13}

More generally, for any normed vector space $X$ and its dual $X^*$, a sequence $\{x_n\}$ in $X$ **converges weakly** to $x \in X$ if:
$$
\phi(x_n) \to \phi(x) \quad \text{for all } \phi \in X^* \tag{3.36}
$$

This abstract definition applies to all Banach spaces (not just $L^p$), and we will use it in Weeks 13-18 when studying Hilbert spaces and general functional analysis.

**Notation convention (critical for RL sections):** Throughout this chapter:
- $\mu$ denotes an abstract measure on $(X, \mathcal{F})$ (as in Definitions 3.13-3.14)
- $\rho$ denotes a state distribution in an MDP (probability measure on state space $\mathcal{S}$)

This distinction prevents confusion when discussing weak* convergence of state distributions $\rho_{\pi_\theta}$ in RL applications (Section III).

**Remark 3.18 (Relation Between Definitions).** For $1 < p < \infty$, the explicit and abstract definitions coincide: $f_n \rightharpoonup f$ in $L^p$ if and only if $\phi(f_n) \to \phi(f)$ for all $\phi \in (L^p)^*$, since every such $\phi$ corresponds to integration against some $g \in L^q$ by [THM-3.9]. We use the explicit form (3.35) for computations and the abstract form (3.36) for conceptual understanding.

**Example 3.5 (Weak vs. Strong Convergence in $L^2([0,1])$).** Consider $f_n(x) = \sqrt{2}\sin(2\pi nx)$ on $[0,1]$.

*Intuition before computation:* As $n$ increases, $f_n$ oscillates faster and faster. When integrated against a smooth function $g$, the positive and negative oscillations cancel out—the integral $\int f_n g$ vanishes in the limit. This is **weak convergence to zero**. However, the functions themselves don't get smaller in norm ($\|f_n\|_2 = 1$ for all $n$), so there's no strong convergence.

1. **No strong convergence:** First, we verify that $\|f_n\|_2$ does not approach zero.
   $$
   \|f_n\|_2^2 = \int_0^1 |f_n(x)|^2 \, dx = 2 \int_0^1 \sin^2(2\pi nx) \, dx
   $$

   **Substitution:** Let $u = 2\pi nx$, so $du = 2\pi n \, dx$. When $x = 0$, $u = 0$; when $x = 1$, $u = 2\pi n$. Thus:
   $$
   \int_0^1 \sin^2(2\pi nx) \, dx = \frac{1}{2\pi n} \int_0^{2\pi n} \sin^2(u) \, du
   $$

   **Periodicity:** Since $\sin^2(u)$ has period $\pi$, we have $\int_0^{2\pi n} \sin^2(u) \, du = 2n \int_0^\pi \sin^2(u) \, du = 2n \cdot \frac{\pi}{2} = \pi n$ (using the standard integral $\int_0^\pi \sin^2(u) du = \pi/2$).

   Therefore:
   $$
   \int_0^1 \sin^2(2\pi nx) \, dx = \frac{1}{2\pi n} \cdot \pi n = \frac{1}{2}
   $$

   Thus $\|f_n\|_2^2 = 2 \cdot (1/2) = 1$, so $\|f_n\|_2 = 1$ for all $n$. Hence $\|f_n - 0\|_2 = 1 \not\to 0$, so $f_n \not\to 0$ in norm.

2. **Weak convergence to zero:** We will show $\int_0^1 f_n(x) g(x) \, dx \to 0$ for any $g \in L^2([0,1])$.

   This follows from the **Riemann-Lebesgue Lemma**, which we state and prove for self-containment:

**Lemma 3.24 (Riemann-Lebesgue Lemma).** {#LEM-3.24}
For any $g \in L^1([0,1])$:
$$
\lim_{n \to \infty} \int_0^1 g(x) \sin(2\pi nx) \, dx = 0 \tag{3.37}
$$

This classical result from Fourier analysis captures the cancellation of rapid oscillations: as the sine wave oscillates faster, its integral against any $L^1$ function vanishes.

*Proof.* By density of continuous functions in $L^1$ ([@folland:real_analysis:1999, Proposition 2.10]), it suffices to prove for $g \in C([0,1])$.

For $g \in C^1([0,1])$ (continuously differentiable), integrate by parts with $u = g(x)$, $dv = \sin(2\pi nx) dx$:
$$
\int_0^1 g(x) \sin(2\pi nx) \, dx = \left[-\frac{g(x)}{2\pi n}\cos(2\pi nx)\right]_0^1 + \frac{1}{2\pi n}\int_0^1 \cos(2\pi nx) g'(x) \, dx
$$

Since $\cos(2\pi n) = 1$ for all $n$:
$$
= -\frac{g(1) - g(0)}{2\pi n} + O\left(\frac{1}{n}\right) = O\left(\frac{1}{n}\right) \to 0
$$
(the integral term is bounded by $\|g'\|_1/(2\pi n) \to 0$).

For general $g \in C([0,1])$, approximate by $C^1$ functions (or use Weierstrass approximation) and apply a standard $\epsilon/3$ argument. □

**Returning to Example 3.5:** For any $g \in L^2([0,1])$, since $L^2 \subset L^1$ on finite measure spaces (by Hölder's inequality: $\|g\|_1 \leq \|g\|_2 \|1\|_2 = \|g\|_2 \cdot 1$), we have $g \in L^1$. By [LEM-3.24]:
$$
\int_0^1 f_n(x) g(x) \, dx = \sqrt{2} \int_0^1 \sin(2\pi nx) g(x) \, dx \to 0
$$

Thus $\int f_n g \to \int 0 \cdot g = 0$ for all $g \in L^2$, so $f_n \rightharpoonup 0$ weakly in $L^2([0,1])$ by [DEF-3.13-EXPLICIT].

**Conclusion:** $f_n \rightharpoonup 0$ weakly but $f_n \not\to 0$ strongly. Weak convergence is **strictly weaker** than strong.

**Remark 3.19 (Geometric Intuition).** Think of $f_n = \sqrt{2}\sin(2\pi nx)$ as "oscillating faster and faster." While the functions don't converge pointwise (they oscillate between $-\sqrt{2}$ and $\sqrt{2}$), their "average effect" when tested against smooth functions $g$ vanishes—the positive and negative oscillations cancel out when integrated. This is the essence of weak convergence: behavior in expectation against test functions, not pointwise behavior.

**Visualization note:** (Fig 3.1: plots of $\sin(2\pi nx)$ for $n = 1, 5, 10$—see Friday coding session for numerical verification.)

---

#### **A. Basic Properties of Weak Convergence**

**Proposition 3.15 (Strong Implies Weak).** {#PROP-3.15}
If $f_n \to f$ in $L^p$ norm (i.e., $\|f_n - f\|_p \to 0$), then $f_n \rightharpoonup f$ weakly.

*Proof.* For any $\phi \in (L^p)^*$ with $\|\phi\| < \infty$:
$$
|\phi(f_n) - \phi(f)| = |\phi(f_n - f)| \leq \|\phi\| \|f_n - f\|_p \to 0
$$
(by boundedness of $\phi$). Thus $\phi(f_n) \to \phi(f)$ for all $\phi$, so $f_n \rightharpoonup f$. □

**Remark 3.20 (Converse Fails).** The converse is false in infinite dimensions, as shown by Example 3.5. In **finite dimensions**, weak and strong convergence are equivalent (by compactness of closed bounded sets in $\mathbb{R}^n$).

---

**Proposition 3.16 (Weak Limits are Unique).** {#PROP-3.16}
If $f_n \rightharpoonup f$ and $f_n \rightharpoonup g$ weakly in $L^p$, then $f = g$ $\mu$-almost everywhere.

*Proof.* By linearity, $f_n \rightharpoonup f$ and $f_n \rightharpoonup g$ imply $0 = f_n - f_n \rightharpoonup f - g$. Thus $\phi(f - g) = 0$ for all $\phi \in (L^p)^*$.

By Riesz Representation [THM-3.9], taking $\phi(h) = \int h \cdot \text{sgn}(f-g)|f-g|^{p-1} \, d\mu$ (test functional corresponding to $g = \text{sgn}(f-g)|f-g|^{p-1} \in L^q$):
$$
0 = \phi(f - g) = \int |f - g|^p \, d\mu
$$

Since $|f-g|^p \geq 0$ and its integral is zero, $|f-g|^p = 0$ $\mu$-a.e., hence $f = g$ $\mu$-a.e. □

---

**Proposition 3.17 (Norm Lower Semicontinuity).** {#PROP-3.17}
If $f_n \rightharpoonup f$ weakly in $L^p$, then:
$$
\|f\|_p \leq \liminf_{n \to \infty} \|f_n\|_p \tag{3.38}
$$

(The limit function has norm no larger than the $\liminf$ of norms.)

*Proof.* By Riesz Representation [THM-3.9], the norm on $L^p$ is given by:
$$
\|f\|_p = \sup_{\|g\|_q \leq 1} \left|\int fg \, d\mu\right|
$$

There exists $g \in L^q$ with $\|g\|_q = 1$ such that $\|f\|_p = |\int fg \, d\mu|$ (this $g$ "tests" the norm of $f$).

By weak convergence, $\int f_n g \to \int fg$ for all $g \in L^q$. In particular, for the $g$ that achieves $\|f\|_p$:
$$
\|f\|_p = \left|\int fg \, d\mu\right| = \lim_{n \to \infty} \left|\int f_n g \, d\mu\right| \leq \liminf_{n \to \infty} \|f_n\|_p \|g\|_q = \liminf_{n \to \infty} \|f_n\|_p
$$
(using Hölder's inequality [THM-2.4] and $\|g\|_q = 1$). □

**Remark 3.21 (Strict Inequality Possible).** In Example 3.5, $f_n \rightharpoonup 0$ with $\|f_n\|_2 = 1$ and $\|0\|_2 = 0$. Thus $\|0\|_2 = 0 < 1 = \liminf \|f_n\|_2$ (strict inequality). This shows the norm is only **lower semicontinuous** in the weak topology, not continuous.

---

### **II. Weak* Convergence in $(L^p)^*$**

**Definition 3.14 (Weak* Convergence).** {#DEF-3.14}
Let $(X, \mathcal{F}, \mu)$ be a measure space and $1 \leq p < \infty$. A sequence $\{\phi_n\}$ in $(L^p)^*$ **converges weak*** (pronounced "weak-star") to $\phi \in (L^p)^*$ if:
$$
\phi_n(f) \to \phi(f) \quad \text{for all } f \in L^p \tag{3.39}
$$

We write $\phi_n \overset{*}{\rightharpoonup} \phi$ (weak* limit).

**Remark 3.22 (Explicit Form via $L^q$).** By Riesz Representation [THM-3.9], $(L^p)^* \cong L^q$ for $1 < p < \infty$. Thus $\phi_n \leftrightarrow g_n \in L^q$ via $\phi_n(f) = \int fg_n \, d\mu$. Weak* convergence becomes:
$$
g_n \overset{*}{\rightharpoonup} g \quad \Leftrightarrow \quad \int f g_n \, d\mu \to \int f g \, d\mu \quad \text{for all } f \in L^p \tag{3.40}
$$

**Relation to Weak Convergence:** If we view $L^q$ as a normed space in its own right (since $(L^p)^* \cong L^q$), then:
- **Weak convergence in $L^q$**: $\int g_n h \, d\mu \to \int gh \, d\mu$ for all $h \in (L^q)^* \cong L^p$ (by duality $(L^q)^{**} \cong L^p$ for reflexive spaces)
- **Weak* convergence in $(L^p)^* \cong L^q$**: $\int f g_n \, d\mu \to \int fg \, d\mu$ for all $f \in L^p$

For reflexive spaces ($1 < p < \infty$), these coincide: weak and weak* convergence in $L^q$ are the same. But for $L^1$ and $L^\infty$ (non-reflexive), weak* is weaker than weak.

---

#### **A. Banach-Alaoglu Theorem**

We now arrive at the central compactness result. The proof is substantial, so we present a detailed sketch here and defer the complete proof to **Appendix 3.A** (see end of this file).

**Why Compactness Matters in RL:** Recall the motivating question from the introduction: In policy gradient descent, does $J(\theta_k) = \mathbb{E}_{\rho_{\pi_{\theta_k}}}[V^{\pi_{\theta_k}}]$ converge? If the sequence of state distributions $\{\rho_{\pi_{\theta_k}}\}$ is bounded but not norm-convergent, can we still extract a convergent subsequence? More broadly:

- **Policy iteration** generates sequences of value functions $\{V^{\pi_k}\}$ that are bounded ($\|V^{\pi_k}\|_\infty \leq R_{\max}/(1-\gamma)$). Do convergent subsequences exist?
- **Policy optimization** searches over the space of policies. Is this space compact in any sense? If so, does $\sup_\pi J(\pi)$ attain its supremum (i.e., does an optimal policy exist)?
- **Function approximation** uses sequences of approximate value functions $\{V_\theta^{(k)}\}$. Can we extract convergent subsequences even when strong convergence fails?

The answer to all these questions is **yes**, provided we use the weak* topology. This is the power of Banach-Alaoglu:

**Theorem 3.18 (Banach-Alaoglu Theorem).** {#THM-3.18}
Let $X$ be a normed vector space and $X^*$ its dual. The **closed unit ball** in $X^*$:
$$
B_{X^*} := \{\phi \in X^* : \|\phi\| \leq 1\} \tag{3.41}
$$
is **compact** in the **weak* topology**.

More explicitly: Every bounded sequence $\{\phi_n\}$ in $X^*$ (i.e., $\sup_n \|\phi_n\| < \infty$) has a subsequence $\{\phi_{n_k}\}$ that converges weak* to some $\phi \in X^*$.

**Proof sketch.** The proof uses Tychonoff's theorem (product of compact spaces is compact in product topology). The key steps are:

1. **Embedding into a product space:** For each $x \in X$ with $\|x\| \leq 1$, we have $|\phi(x)| \leq \|\phi\| \|x\| \leq \|\phi\|$. Thus $\phi \in B_{X^*}$ (unit ball) satisfies $\phi(x) \in [-1, 1]$ for all $x$ with $\|x\| \leq 1$.

   We can view $B_{X^*}$ as a subset of the product space:
   $$
   \prod_{x \in B_X} [-\|\phi\|, \|\phi\|]
   $$
   where $B_X = \{x \in X : \|x\| \leq 1\}$. Each $\phi$ is a function $B_X \to \mathbb{R}$, so we embed $B_{X^*}$ into the space of all such functions.

2. **Product topology and Tychonoff:** By Tychonoff's theorem, the product $\prod_{x \in B_X} [-C, C]$ is compact in the product topology (pointwise convergence topology) for any $C > 0$. For bounded sequences $\{\phi_n\}$ with $\|\phi_n\| \leq C$, the image lies in this compact product.

3. **Weak* topology = subspace of product topology:** The weak* topology on $X^*$ is precisely the subspace topology induced by the embedding $\phi \mapsto (\phi(x))_{x \in X}$. Weak* convergence $\phi_n \overset{*}{\rightharpoonup} \phi$ means $\phi_n(x) \to \phi(x)$ for all $x \in X$ (pointwise convergence).

4. **Closedness in product topology:** We must verify that $B_{X^*}$ is a closed subset of the product space (to apply Tychonoff). This follows from the linearity and boundedness conditions defining $X^*$: if $\phi_n \overset{*}{\rightharpoonup} \phi$ (pointwise) and $\|\phi_n\| \leq 1$, then $\phi$ is linear and $\|\phi\| \leq 1$.

5. **Conclusion:** $B_{X^*}$ is a closed subset of a compact space, hence compact. Thus every sequence in $B_{X^*}$ has a convergent subsequence in the weak* topology. □

**For a complete, rigorous proof with all details**, see **Appendix 3.A: Full Proof of Banach-Alaoglu Theorem** at the end of this file.

**Remark 3.23 (Contrast with Strong Topology).** In the **norm topology**, the unit ball in $X^*$ is **not compact** unless $X$ is finite-dimensional (Riesz's theorem). For example, in $L^2([0,1])$, the sequence $f_n(x) = \sqrt{2}\sin(2\pi nx)$ satisfies $\|f_n\|_2 = 1$ for all $n$, but has no norm-convergent subsequence (it converges weakly to $0$, but $\|f_n\|_2 = 1 \not\to 0$). This is why weak* compactness is so powerful: it restores compactness in infinite dimensions.

---

**Pause and Reflect:** Why is Banach-Alaoglu's weak* compactness more powerful than norm compactness in infinite dimensions?

*Hint:* In $L^2([0,1])$, the unit ball $\{f : \|f\|_2 \leq 1\}$ is not norm-compact (no convergent subsequence in norm for $\sin(2\pi nx)$). But by Banach-Alaoglu, it **is** weakly* compact: every bounded sequence has a weak* convergent subsequence. This is essential for existence theorems in optimization and RL, where we need to extract convergent subsequences from bounded iterates.

---

**Corollary 3.19 (Weak* Compactness in $(L^p)^*$).** {#COR-3.19}
For $1 \leq p < \infty$ and $(X, \mathcal{F}, \mu)$ σ-finite, the closed unit ball in $(L^p)^* \cong L^q$ is weak* compact:
$$
\{g \in L^q : \|g\|_q \leq 1\} \quad \text{is weak* compact} \tag{3.42}
$$

**Proof.** Apply Theorem 3.18 with $X = L^p$. □

---

### **III. RL Applications of Weak Convergence**

We now demonstrate how weak and weak* convergence arise naturally in reinforcement learning. We focus on three applications:

**A.** Value iteration in infinite-state MDPs (weak convergence when strong fails)
**B.** Distribution shift in policy gradients (weak* convergence of state distributions)
**C.** Existence of optimal policies (compactness via Banach-Alaoglu)

**Note:** We originally included a fourth application (least-squares TD and weak continuity of projections), but this connection is more subtle than initially presented. The LSTD fixed point $V_\theta^* = \Pi T^\pi V_\theta^*$ depends on contraction properties of $\Pi T^\pi$, not primarily on weak continuity of $\Pi$. We defer this topic to **Friday's synthesis session**, where we can explore it alongside numerical experiments.

---

#### **A. Value Iteration in Infinite-State MDPs**

**Context:** In **finite-state MDPs**, value iteration enjoys **strong (exponential) convergence** by the Banach Fixed-Point Theorem: $\|V^{(k)} - V^*\|_\infty \leq \gamma^k \|V^{(0)} - V^*\|_\infty$ (geometric rate $\gamma$). This is norm convergence, the strongest form.

However, weak convergence becomes relevant in **infinite-state MDPs** where strong convergence may fail but weak convergence (in a weighted $L^2$ space under the stationary distribution) still holds. This is the setting where Banach-Alaoglu provides convergent subsequences.

**Example 3.6 (Infinite-State MDP with Weak but Not Strong Convergence).** {#EX-3.6}

Consider a countable-state MDP with state space $\mathcal{S} = \{1, 2, 3, \ldots\}$ and the following structure:
- **Transition dynamics:** From state $s$, the agent moves to state $s+1$ with probability $1$ (deterministic rightward drift).
- **Reward:** $r(s, a) = 1/s$ (reward decays as $1/s$).
- **Discount:** $\gamma = 0.9$.

The optimal value function is $V^*(s) = \sum_{k=0}^\infty \gamma^k \cdot \frac{1}{s+k}$ (sum of discounted future rewards). This series converges, so $V^* \in \ell^\infty(\mathcal{S})$ (bounded).

Now consider a sequence of "truncated" approximations:
$$
V_n(s) := \begin{cases} V^*(s) & \text{if } s \leq n \\ 0 & \text{if } s > n \end{cases}
$$

**Strong convergence fails:** $\|V_n - V^*\|_\infty = \sup_{s > n} V^*(s) = V^*(n+1) \not\to 0$ (since $V^*(n+1) \sim 1/n \to 0$ only as $n \to \infty$, but the supremum over $s > n$ doesn't vanish).

**Weak convergence holds:** For any probability distribution $\rho$ on $\mathcal{S}$ (e.g., stationary distribution) with $\sum_s \rho(s) = 1$:
$$
\mathbb{E}_\rho[V_n] = \sum_s V_n(s) \rho(s) = \sum_{s \leq n} V^*(s) \rho(s) \to \sum_s V^*(s) \rho(s) = \mathbb{E}_\rho[V^*]
$$
(by dominated convergence, since $|V_n(s)| \leq V^*(s) \leq \|V^*\|_\infty < \infty$ and $\sum_s \rho(s) < \infty$).

This is weak convergence in the sense of functionals: $\phi_\rho(V_n) := \mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V^*]$ for all probability distributions $\rho$. By the identification $\ell^1 \hookrightarrow (\ell^\infty)^*$, this is weak* convergence in $\ell^\infty$.

**RL significance:** In practice, we often only care about $\mathbb{E}_\rho[V(s)]$ for a specific distribution $\rho$ (e.g., initial state distribution). Weak convergence is sufficient for this purpose—we don't need uniform convergence $\|V_n - V^*\|_\infty \to 0$ over all states. This matters for:
- **Approximate policy iteration**: Errors in policy evaluation may prevent strong convergence but allow weak convergence.
- **Function approximation**: Neural network value functions $V_\theta$ may not converge uniformly but can converge in expectation under the data distribution.

For detailed theory of infinite-state MDPs with weak convergence, see [@meyn-tweedie:markov_chains:2009, Chapter 17].

---

#### **B. Distribution Shift in Policy Gradient Methods**

**Context:** In **policy gradient methods** (Week 37), we optimize:
$$
J(\theta) = \mathbb{E}_{\rho_{\pi_\theta}}[V^{\pi_\theta}(s_0)]
$$
where $\rho_{\pi_\theta}$ is the state visitation distribution under policy $\pi_\theta$, and $s_0 \sim \rho_0$ is the initial state.

During gradient descent $\theta_{k+1} = \theta_k + \alpha \nabla J(\theta_k)$, both $\pi_\theta$ and $\rho_{\pi_\theta}$ change at each iteration. The sequence of distributions $\{\rho_{\pi_{\theta_k}}\}$ may not converge in total variation distance (strong convergence of measures), but it often converges **weak*** (convergence of measures in the weak topology).

**Definition 3.15 (Weak* Convergence of Probability Measures).** {#DEF-3.15}
A sequence of probability measures $\{\rho_n\}$ on $(X, \mathcal{F})$ converges **weak*** to $\rho$ if:
$$
\int_X f \, d\rho_n \to \int_X f \, d\rho \quad \text{for all continuous bounded } f: X \to \mathbb{R} \tag{3.43}
$$

**Remark 3.25 (Terminology).** In probability theory, this is called **weak convergence of probability measures** ([@billingsley:convergence:1999]). In functional analysis, it's **weak* convergence** when viewing measures as elements of $(C_b(X))^*$ (dual of continuous bounded functions). The two notions coincide by the Riesz-Markov theorem [@folland:real_analysis:1999, §7.2].

**Proposition 3.21 (Objective Convergence Under Weak* + Uniform).** {#PROP-3.21}
Suppose $\rho_n \overset{*}{\rightharpoonup} \rho$ (weak* convergence of measures) and $V_n \to V$ uniformly (i.e., $\|V_n - V\|_\infty \to 0$). Then:
$$
\mathbb{E}_{\rho_n}[V_n(s)] \to \mathbb{E}_\rho[V(s)] \tag{3.44}
$$

*Proof.* We decompose the error into two terms corresponding to function convergence and measure convergence:

**Term A (function convergence, uniform):**
$$
\left|\mathbb{E}_{\rho_n}[V_n] - \mathbb{E}_{\rho_n}[V]\right| = \left|\int (V_n - V) \, d\rho_n\right| \leq \int |V_n - V| \, d\rho_n \leq \|V_n - V\|_\infty \underbrace{\rho_n(\mathcal{S})}_{=1} \to 0
$$
(by uniform convergence $V_n \to V$ and $\rho_n$ being a probability measure).

**Term B (measure convergence, weak*):**
$$
\left|\mathbb{E}_{\rho_n}[V] - \mathbb{E}_\rho[V]\right| = \left|\int V \, d\rho_n - \int V \, d\rho\right| \to 0
$$
(by weak* convergence $\rho_n \overset{*}{\rightharpoonup} \rho$ and boundedness of $V$, assuming $V$ is continuous or at least $\rho_n$-uniformly integrable).

**Combining:** By triangle inequality:
$$
\left|\mathbb{E}_{\rho_n}[V_n] - \mathbb{E}_\rho[V]\right| \leq \underbrace{\left|\mathbb{E}_{\rho_n}[V_n] - \mathbb{E}_{\rho_n}[V]\right|}_{\text{Term A} \to 0} + \underbrace{\left|\mathbb{E}_{\rho_n}[V] - \mathbb{E}_\rho[V]\right|}_{\text{Term B} \to 0} \to 0
$$

Thus $\mathbb{E}_{\rho_n}[V_n] \to \mathbb{E}_\rho[V]$. □

**Implication for Policy Gradients:** Even if $\rho_{\pi_{\theta_k}}$ doesn't converge in total variation distance (strong), weak* convergence is sufficient to guarantee $J(\theta_k) = \mathbb{E}_{\rho_{\pi_{\theta_k}}}[V^{\pi_{\theta_k}}] \to J(\theta^*)$ (objective convergence), provided $V^{\pi_{\theta_k}} \to V^{\pi_{\theta^*}}$ uniformly.

**Practical Note:** In practice, neural network policies $\pi_\theta$ are continuous in $\theta$, so $\theta_k \to \theta^*$ implies $\rho_{\pi_{\theta_k}} \overset{*}{\rightharpoonup} \rho_{\pi_{\theta^*}}$ (weak* continuity). This underpins convergence guarantees for actor-critic methods. For formal results, see [@sutton-barto:rl_intro:2018, Chapter 13] and [@kakade:natural_pg:2001].

---

**Pause and Reflect:** When is weak convergence sufficient in RL, and when do we need strong convergence?

*Hint:* Weak convergence of value functions $V_n \rightharpoonup V^*$ suffices for $\mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V^*]$ (objective convergence under a specific distribution $\rho$). But strong convergence $\|V_n - V^*\|_\infty \to 0$ is needed for **uniform error bounds** across all states—critical for safety-critical applications where worst-case guarantees matter.

---

#### **C. Existence of Optimal Policies via Banach-Alaoglu**

**Context:** In general MDPs (infinite state spaces, non-tabular), does an optimal policy $\pi^*$ achieving $J(\pi^*) = \sup_\pi J(\pi)$ always exist? Not necessarily—the supremum might not be attained (e.g., supremum over open set in $\mathbb{R}$).

Banach-Alaoglu provides the compactness needed for existence theorems:

**Theorem 3.22 (Existence of Optimal Policies, Compact Formulation).** {#THM-3.22}
Consider an MDP with:
- Compact state space $\mathcal{S}$ (e.g., $\mathcal{S} = [0,1]^d$)
- Compact action space $\mathcal{A}$
- Continuous reward $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$
- Continuous transition kernel $P(\cdot|s,a)$ (in weak topology of measures)

If the set of policies is **weakly* compact** (e.g., all policies $\pi(\cdot|s)$ with $\|\pi(\cdot|s)\|_1 = 1$, viewed as measures), then there exists an optimal policy $\pi^*$ with $J(\pi^*) = \sup_\pi J(\pi)$.

**Proof sketch.** This is an informal sketch; the full proof requires advanced MDP theory (see [@puterman:mdps:2005, Theorem 6.2.10] for weak continuity of the policy evaluation operator and Theorem 6.2.7 for existence).

**Step 1: Policy set is weakly* compact (Banach-Alaoglu).** Policies $\pi(\cdot|s)$ are probability distributions on $\mathcal{A}$, viewed as elements of $(C(\mathcal{A}))^*$ (dual of continuous functions on $\mathcal{A}$). By the Riesz-Markov theorem [@folland:real_analysis:1999, §7.2], this is the space of signed measures on $\mathcal{A}$. The set of probability measures is a subset of the unit ball in $(C(\mathcal{A}))^*$, hence weak* compact by [THM-3.18].

**Step 2: Objective $J(\pi)$ is weak* continuous.** The objective $J(\pi) = \mathbb{E}_{\rho_\pi}[V^\pi(s_0)]$ depends on the value function $V^\pi$, which solves the Bellman equation $V^\pi = T^\pi V^\pi = R^\pi + \gamma P^\pi V^\pi$ (where $T^\pi$ is the policy evaluation operator).

For weak* convergence $\pi_n \overset{*}{\rightharpoonup} \pi$ to imply $J(\pi_n) \to J(\pi)$, we need:
1. $V^{\pi_n} \to V^\pi$ (convergence of value functions)
2. $\rho_{\pi_n} \overset{*}{\rightharpoonup} \rho_\pi$ (convergence of state distributions)

The first follows from continuity of the policy evaluation operator $\pi \mapsto V^\pi$ in the weak* topology. This requires analysis of the Neumann series $V^\pi = \sum_{k=0}^\infty \gamma^k (P^\pi)^k R^\pi$ and showing that $P^{\pi_n} \to P^\pi$ weakly implies $V^{\pi_n} \to V^\pi$ uniformly (see [@puterman:mdps:2005, Theorem 6.2.10] for full proof).

The second (state distribution convergence) follows from weak continuity of the stationary distribution map $\pi \mapsto \rho_\pi$ (see Exercise 3.3.4(c) for finite-state case; continuous-state version requires [@billingsley:convergence:1999, Theorem 6.7]).

Given (1) and (2), [PROP-3.21] implies $J(\pi_n) \to J(\pi)$ (objective continuity).

**Step 3: Maximum is attained.** By weak* compactness (Step 1), any sequence $\{\pi_n\}$ with $J(\pi_n) \to \sup_\pi J(\pi)$ has a weak* convergent subsequence $\pi_{n_k} \overset{*}{\rightharpoonup} \pi^*$. By weak* continuity (Step 2), $J(\pi^*) = \lim J(\pi_{n_k}) = \sup_\pi J(\pi)$.

Thus $\pi^*$ is optimal. □

**Note on rigor:** The above is an **informal sketch**. The full proof requires:
- Precise definition of **weak continuity of transition kernels** (see [@hernandez-lerma-lasserre:mdps:1996, Definition 4.2.1])
- Verification that $\pi \mapsto V^\pi$ is continuous in weak* topology via Neumann series analysis
- Uniform integrability conditions for interchange of limits

For complete details, see [@puterman:mdps:2005, Chapter 6, §6.2-6.3] (Theorem 6.2.10 on weak continuity and Theorem 6.2.7 on existence of optimal policies).

**Remark 3.26 (Contrast with Finite MDPs).** For **finite state/action spaces**, existence of optimal policies is trivial (the set of policies is finite, so the supremum is attained). But for **continuous control** (e.g., robotic tasks with $\mathcal{S} = \mathbb{R}^d$, $\mathcal{A} = \mathbb{R}^m$), compactness arguments via Banach-Alaoglu are essential.

**Modern Deep RL:** Neural network policies $\pi_\theta$ with bounded weights $\|\theta\| \leq R$ form a weakly* compact set (by Banach-Alaoglu, since $\theta$ lies in a bounded subset of a Banach space). This ensures that gradient descent on $J(\theta)$ can converge to a local maximum (though global optimality is not guaranteed due to non-convexity of neural network parameterizations).

---

**Pause and Reflect:** How does Banach-Alaoglu guarantee existence of optimal policies?

*Hint:* The set of policies (viewed as elements of $(C(\mathcal{A}))^*$) is weakly* compact by Banach-Alaoglu. The objective $J(\pi)$ is weak* continuous (under continuity assumptions on $r$ and $P$). By compactness, the continuous function $J$ attains its supremum on the policy set, so an optimal policy $\pi^* \in \arg\max_\pi J(\pi)$ exists.

---

### **IV. Modern Deep RL: Theory-Practice Gaps**

The three RL applications above (infinite-state value iteration, distribution shift, existence of optimal policies) are grounded in weak convergence theory. However, modern deep RL algorithms operate in regimes where classical theory provides only partial guidance. We briefly survey these gaps:

**Policy Gradients (PPO, TRPO):**
- **Theory:** [PROP-3.21] shows that weak* convergence of state distributions $\rho_{\pi_\theta_k} \overset{*}{\rightharpoonup} \rho_{\pi_{\theta^*}}$ + uniform value convergence $V^{\pi_\theta_k} \to V^{\pi_{\theta^*}}$ implies $J(\theta_k) \to J(\theta^*)$.
- **Practice:** PPO [@schulman:ppo:2017] uses clipped surrogate objectives and finite-horizon rollouts. The finite-horizon setting introduces bias (infinite-horizon theory doesn't directly apply). Empirically, PPO converges reliably, but formal guarantees are limited to tabular or linear function approximation [@agarwal:theory_pg:2021].
- **Gap:** No general convergence theory for PPO with neural network function approximation. Weak convergence analysis suggests robustness to distribution shift, but formal proofs remain open.

**Off-Policy Methods (DQN, Experience Replay):**
- **Theory:** Q-learning is inherently **off-policy** (learns $Q^*$ under behavior policy $\mu \neq \pi$). Classical theory [@watkins:qlearning:1992] assumes samples from a fixed distribution.
- **Practice:** Experience replay [@mnih:dqn:2015] samples from a buffer containing transitions from many past policies. This creates a **non-stationary data distribution** $\rho_{\text{replay}}$ (mixture of past policies), violating the fixed-distribution assumption.
- **Why DQN works despite this:**
  - **Contraction:** The Bellman operator $T^* Q = \max_a (r + \gamma P Q)$ is a contraction in $\|\cdot\|_\infty$ (uniform convergence), **independent of the data distribution** (Weeks 16-18).
  - **Exploration:** $\epsilon$-greedy ensures sufficient coverage of state-action space.
  - **Target networks:** Slow-moving target $Q_{\theta^-}$ reduces non-stationarity.
- **Gap:** No formal convergence proof for DQN with neural networks and experience replay. The non-stationarity is a practical necessity (sample efficiency), but breaks classical theory.

**Importance Sampling for Off-Policy RL:**
- **Theory:** Off-policy actor-critic [@degris:off_policy_ac:2012] multiplies gradient by $\pi_\theta(a|s)/\mu(a|s)$ (importance ratio) to correct for distribution mismatch.
- **Practice:** High-variance importance ratios can destabilize learning. Modern methods use:
  - **Retrace** [@munos:retrace:2016]: Multi-step off-policy correction with bounded importance weights
  - **V-trace** [@espeholt:impala:2018]: Clipped importance weights for stability
  - **Reward-weighted regression** [@peters:rwr:2007]: Implicit importance weighting via weighted supervised learning
- **Connection to weak* convergence:** As behavior policy $\mu$ approaches target policy $\pi_\theta$, the importance ratio $\pi_\theta/\mu \to 1$ and variance decreases. This is closely related to weak* convergence $\mu \overset{*}{\rightharpoonup} \pi_\theta$ (when $\mu$ is close to $\pi_\theta$, the distributions are "close" in weak* topology, reducing importance sampling variance).

**Function Approximation and Weak Convergence:**
- **Theory:** [PROP-3.23] (deferred to Friday) shows orthogonal projections $\Pi: L^2 \to \mathcal{V}$ are weakly continuous. This suggests approximate value functions $V_\theta$ can converge weakly even when strong convergence fails.
- **Practice:** Neural networks $V_\theta$ provide **approximate** projections (not exact orthogonal projections). Weak convergence analysis suggests robustness, but formal convergence guarantees remain elusive [@bertsekas-tsitsiklis:neuro-dp:1996].

**Summary:** Weak and weak* convergence provide conceptual frameworks for understanding distribution shift, existence of optimal policies, and robustness of function approximation. However, modern deep RL operates in regimes (non-stationary data, nonlinear function approximation, finite-horizon) where classical theory gives only partial coverage. Bridging this gap is an active research area (see [@agarwal:theory_deep_rl:2022] for recent progress).

---

### **V. Summary and Looking Ahead**

**Mathematical Insight:**

Today we introduced two topologies on function spaces:
1. **Strong (norm) topology**: $\|f_n - f\|_p \to 0$ (convergence in $L^p$ norm)
2. **Weak topology**: $\int f_n g \to \int fg$ for all $g \in L^q$ (convergence tested by dual functionals)

Key properties:
- **Strong $\Rightarrow$ weak** ([PROP-3.15]), but not conversely (Example 3.5)
- **Weak limits are unique** ([PROP-3.16])
- **Norm lower semicontinuity** ([PROP-3.17]): $\|f\|_p \leq \liminf \|f_n\|_p$
- **Banach-Alaoglu [THM-3.18]**: Bounded sequences in $(L^p)^*$ have weak* convergent subsequences (compactness)

**Connection to Days 1-2:**
- Day 1: $L^p$ is complete [THM-3.4] (Riesz-Fischer)
- Day 2: $(L^p)^* \cong L^q$ [THM-3.9] (Riesz Representation)
- Day 3: Weak/weak* topologies reveal compactness properties essential for existence theorems

**RL Connection:**

Weak convergence is crucial for:
1. **Infinite-state value iteration**: Weak convergence when strong fails (Example 3.6)
2. **Distribution shift**: State distributions $\rho_{\pi_\theta}$ converge weak* during policy gradient descent
3. **Existence of optimal policies**: Banach-Alaoglu guarantees weak* compactness of policy sets

**Looking Ahead:**

- **Day 4 (Thursday, Extended Proof)**: **Radon-Nikodym theorem**—when does a measure have a density $d\mu/d\nu$? This formalizes importance sampling ratios $\pi/\mu$ used in off-policy RL.

- **Day 5 (Friday, Synthesis)**: Weekly reflection on $L^p$ completeness and duality, coding exercises on weak convergence and importance sampling.

- **Week 4**: Probability spaces and conditional expectation—formalizing MDPs as measure-theoretic objects.

- **Week 14 (Hilbert Spaces)**: Orthogonal projections in $L^2$ and the Projection Theorem, foundation of least-squares TD (Proposition 3.23 fully proved).

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_3_exercises_draft_revised_all]]**

**Anchor Exercise Preview:**
1. **Verify weak but not strong convergence:** Show $f_n(x) = \sqrt{2}\sin(2\pi nx)$ converges weakly to $0$ in $L^2([0,1])$ but $\|f_n\|_2 = 1$ for all $n$. **(20 min)**

2. **Apply Banach-Alaoglu:** Prove that any bounded sequence in $\ell^2$ has a weakly convergent subsequence. **(15 min)**

3. **RL Application (Distribution Shift):** Show that if $\rho_n \overset{*}{\rightharpoonup} \rho$ (weak* convergence of state distributions) and $V_n \to V$ uniformly, then $\mathbb{E}_{\rho_n}[V_n] \to \mathbb{E}_\rho[V]$. **(20 min)**

4. **Continuity of State Distributions:** Show that if $\pi_\theta$ is continuous in $\theta$ (for finite-state MDP), then $\rho_{\pi_\theta_k} \to \rho_{\pi_{\theta^*}}$ (pointwise = weak*) when $\theta_k \to \theta^*$. **(25 min)**

**Total exercise time:** ~90-120 minutes (can extend to Thursday; see Day_3_exercises_draft_revised_all.md for full solutions)

---

**Reflection Questions:**

1. **Why is weak* compactness (Banach-Alaoglu) more powerful than norm compactness in infinite dimensions?**
   *Hint:* In $L^2([0,1])$, the unit ball $\{f : \|f\|_2 \leq 1\}$ is not norm-compact (no convergent subsequence in norm for $\sin(2\pi nx)$), but it is weakly* compact (every bounded sequence has weak* convergent subsequence).

2. **When is weak convergence sufficient in RL, and when do we need strong convergence?**
   *Hint:* Weak convergence of value functions $V_n \rightharpoonup V^*$ suffices for $\mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V^*]$ (objective convergence). But strong convergence $\|V_n - V^*\|_\infty \to 0$ is needed for uniform error bounds across all states.

3. **How does Banach-Alaoglu guarantee existence of optimal policies?**
   *Hint:* The set of policies (viewed as elements of $(C(\mathcal{A}))^*$) is weakly* compact by Banach-Alaoglu. The objective $J(\pi)$ is weak* continuous. Thus $\sup_\pi J(\pi)$ is attained.

---

**Daily Study Note:**

**What I learned today:**
- **Weak convergence** $f_n \rightharpoonup f$ in $L^p$: $\int f_n g \to \int fg$ for all $g \in L^q$ (conjugate)
- **Weak* convergence** $\phi_n \overset{*}{\rightharpoonup} \phi$ in $(L^p)^*$: $\phi_n(f) \to \phi(f)$ for all $f \in L^p$
- **Key properties**: Strong $\Rightarrow$ weak, weak limits unique, norm lower semicontinuity
- **Banach-Alaoglu [THM-3.18]**: Bounded sequences in dual spaces have weak* convergent subsequences (compactness!)
- **RL applications**: Infinite-state value iteration (weak convergence when strong fails), distribution shift (weak* convergence of $\rho_\pi$), existence of optimal policies

**Connection to previous material:**
- Builds on Riesz Representation [THM-3.9] (Day 2): duality $(L^p)^* \cong L^q$ enables explicit characterization of weak convergence
- Uses Riesz-Fischer [THM-3.4] (Day 1): completeness ensures weak limits lie in $L^p$
- Prepares for Radon-Nikodym (Day 4): weak* convergence of measures formalizes distribution shift

**Looking forward:**
- Day 4: Radon-Nikodym theorem—densities $d\mu/d\nu$ for importance sampling
- Day 5: Weekly synthesis, coding exercises on weak convergence and importance sampling
- Week 14: Hilbert spaces, orthogonal projections, Projection Theorem

**RL connections identified:**
- Infinite-state value iteration: weak convergence sufficient for expectation convergence
- Distribution shift: state distributions converge weak* during policy gradient descent
- Existence of optimal policies: Banach-Alaoglu + weak* continuity of $J(\pi)$

**Time spent:** 120-150 minutes (theory core 90-120 min + initial exercises 30 min; remaining exercises on Thursday)

---

**End of Day 3 Theory**

---

## **Appendix 3.A: Full Proof of the Banach-Alaoglu Theorem** {#APP-3.A}

See companion file: **[[Day_3_Appendix_Banach_Alaoglu]]** for the complete, rigorous proof with all details.

The appendix covers:
- Tychonoff's theorem (statement and use)
- Product topology on $\prod_{x \in X} [-\|\phi\|, \|\phi\|]$
- Embedding $B_{X^*} \hookrightarrow$ product space
- Weak* topology = subspace topology of product topology
- Closedness of $B_{X^*}$ in product topology (linearity and boundedness preserved under pointwise limits)
- Conclusion: $B_{X^*}$ is closed subset of compact space, hence compact

**Estimated reading time:** 30-40 minutes (optional, can defer to Week 14 when we study functional analysis in depth)
### Agenda:

##### 📘 Day 3 — Week 3: Weak Convergence, Dual Topologies, and RL Applications of $L^p$ Duality

**Total time: ~120-150 minutes (Wednesday, extended)**
- **Theory core**: 90-120 minutes (Sections I-III)
- **Exercises**: 90-120 minutes (can extend to Thursday; see companion exercise file)
- **Realistic total**: 2.5-3 hours for mastery of weak convergence + Banach-Alaoglu

**Note on pacing**: This is dense foundational material. The Syllabus originally allocated 90 minutes, but weak convergence and Banach-Alaoglu are cornerstone results requiring careful study. We recommend:
- **Wednesday (today)**: Theory core (Sections I-II) + 2-3 exercises (90-120 min total)
- **Thursday morning**: Remaining exercises + extended proof review (60 min)
- **Friday**: Synthesis and numerical experiments

**Syllabus alignment note**: The Syllabus.md Week 3 outline described "continuing $(L^p)^*$ duality" on Day 3. We have reorganized to cover **weak/weak* convergence and Banach-Alaoglu** today, as this is the natural continuation of duality (Day 2 identified dual spaces; Day 3 studies topologies on these spaces). The Radon-Nikodym theorem (originally Day 3-4) moves to Thursday as planned. This reorganization improves mathematical flow: completeness (Day 1) $\to$ duality (Day 2) $\to$ topologies on dual spaces (Day 3) $\to$ densities and measures (Day 4).

---

#### **⏱️ Segment 1 (40 min) — Reading**

**Topic:** _Weak and weak* convergence in dual spaces, deeper RL applications of duality_

- Continue from **Folland §6.3-6.4** [@folland:real_analysis:1999, §6.3-6.4] ($L^p$ duality) or **Brezis Ch 3** [@brezis:functional_analysis:2011, Ch 3] (Weak Convergence)
- Focus on:
    - **Weak convergence** $f_n \rightharpoonup f$ in $L^p$: $\phi(f_n) \to \phi(f)$ for all $\phi \in (L^p)^*$
    - **Weak* convergence** $\phi_n \overset{*}{\rightharpoonup} \phi$ in $(L^p)^*$: $\phi_n(f) \to \phi(f)$ for all $f \in L^p$
    - **Relationship to strong convergence**: Weak convergence ⇐ strong convergence ($\|f_n - f\|_p \to 0$)
    - **Non-equivalence**: Sequences can converge weakly but not strongly
    - **Compactness**: Banach-Alaoglu theorem (weak* compactness of unit ball)
    - **RL significance**: Convergence of value function approximations, policy gradient convergence, distribution shift

---

#### **⏱️ Segment 2 (60-80 min) — Theory and Examples**

**Primary Task:**
1. **Define weak and weak* convergence** formally
2. **Understand key examples**:
   - In $L^2$: $f_n(x) = \sin(nx)$ converges weakly to $0$ but not strongly
   - In $(L^\infty)^*$: Dirac delta sequence converging weak*
3. **Banach-Alaoglu theorem**: Unit ball in $(L^p)^*$ is weak* compact (full proof in Appendix 3.A)
4. **Apply to RL**:
   - Infinite-state value iteration: weak convergence when strong fails
   - Distribution shift: state distributions converging weak* in policy gradients
   - Existence of optimal policies via compactness
   - (LSTD discussion deferred to Friday synthesis)

**Guidance:**
- Weak convergence is **strictly weaker** than norm convergence (hence the name)
- In infinite dimensions, bounded sequences need not have convergent subsequences in norm topology
- But bounded sequences in $(L^p)^*$ **always** have weak* convergent subsequences (Banach-Alaoglu)
- This is crucial for existence proofs in RL (e.g., showing optimal policies exist)

---

## **Chapter 3.3: Weak Convergence and Dual Topologies**

### **Motivation: Multiple Notions of Convergence**

Recall from Week 1 that we studied various modes of convergence for functions:
- **Pointwise convergence**: $f_n(x) \to f(x)$ for each $x$
- **Uniform convergence**: $\sup_x |f_n(x) - f(x)| \to 0$
- **$L^p$ convergence** (norm convergence): $\|f_n - f\|_p \to 0$
- **Almost everywhere convergence**: $f_n(x) \to f(x)$ for $\mu$-almost all $x$

Each mode has different strength and implications. Today we add two more notions, crucial for functional analysis and RL:
- **Weak convergence**: Convergence "tested" by all continuous linear functionals
- **Weak* convergence**: Convergence in the dual space topology

**Why do we need these?** Consider a concrete challenge from reinforcement learning: In policy gradient descent, we optimize $J(\theta) = \mathbb{E}_{\rho_{\pi_\theta}}[V^{\pi_\theta}(s)]$ where both the state distribution $\rho$ and the value function $V$ change at each iteration. When does $J(\theta_k)$ converge? The distributions $\{\rho_{\pi_{\theta_k}}\}$ may not converge in total variation distance (strong convergence of measures), yet $J(\theta_k)$ can still converge if the distributions converge in a weaker sense—**weak* convergence**—which turns out to be sufficient for objective convergence.

More broadly: In infinite-dimensional spaces, norm-bounded sequences need not have norm-convergent subsequences. But Banach-Alaoglu guarantees that bounded sequences in dual spaces always have **weak* convergent subsequences**. This compactness result is essential for existence theorems in optimization and RL.

---

### **I. Weak Convergence in $L^p$**

Yesterday we identified the dual spaces $(L^p)^* \cong L^q$ via the Riesz Representation Theorem [THM-3.9]. Today we study the natural topology on these dual spaces.

**Explicit Definition via Riesz Representation.** {#DEF-3.13-EXPLICIT}

Let $(X, \mathcal{F}, \mu)$ be a measure space and $1 < p < \infty$ with conjugate exponent $q$ (where $1/p + 1/q = 1$). By [THM-3.9], every continuous linear functional $\phi \in (L^p)^*$ has the form $\phi(f) = \int fg \, d\mu$ for unique $g \in L^q$.

A sequence $\{f_n\}$ in $L^p(\mu)$ **converges weakly** to $f \in L^p$ if:
$$
\int f_n g \, d\mu \to \int f g \, d\mu \quad \text{for all } g \in L^q \tag{3.35}
$$

We write $f_n \rightharpoonup f$ (weak limit).

**Abstract Definition (General Dual Spaces).** {#DEF-3.13}

More generally, for any normed vector space $X$ and its dual $X^*$, a sequence $\{x_n\}$ in $X$ **converges weakly** to $x \in X$ if:
$$
\phi(x_n) \to \phi(x) \quad \text{for all } \phi \in X^* \tag{3.36}
$$

This abstract definition applies to all Banach spaces (not just $L^p$), and we will use it in Weeks 13-18 when studying Hilbert spaces and general functional analysis.

**Notation convention (critical for RL sections):** Throughout this chapter:
- $\mu$ denotes an abstract measure on $(X, \mathcal{F})$ (as in Definitions 3.13-3.14)
- $\rho$ denotes a state distribution in an MDP (probability measure on state space $\mathcal{S}$)

This distinction prevents confusion when discussing weak* convergence of state distributions $\rho_{\pi_\theta}$ in RL applications (Section III).

**Remark 3.18 (Relation Between Definitions).** For $1 < p < \infty$, the explicit and abstract definitions coincide: $f_n \rightharpoonup f$ in $L^p$ if and only if $\phi(f_n) \to \phi(f)$ for all $\phi \in (L^p)^*$, since every such $\phi$ corresponds to integration against some $g \in L^q$ by [THM-3.9]. We use the explicit form (3.35) for computations and the abstract form (3.36) for conceptual understanding.

**Example 3.5 (Weak vs. Strong Convergence in $L^2([0,1])$).** Consider $f_n(x) = \sqrt{2}\sin(2\pi nx)$ on $[0,1]$.

*Intuition before computation:* As $n$ increases, $f_n$ oscillates faster and faster. When integrated against a smooth function $g$, the positive and negative oscillations cancel out—the integral $\int f_n g$ vanishes in the limit. This is **weak convergence to zero**. However, the functions themselves don't get smaller in norm ($\|f_n\|_2 = 1$ for all $n$), so there's no strong convergence.

1. **No strong convergence:** First, we verify that $\|f_n\|_2$ does not approach zero.
   $$
   \|f_n\|_2^2 = \int_0^1 |f_n(x)|^2 \, dx = 2 \int_0^1 \sin^2(2\pi nx) \, dx
   $$

   **Substitution:** Let $u = 2\pi nx$, so $du = 2\pi n \, dx$. When $x = 0$, $u = 0$; when $x = 1$, $u = 2\pi n$. Thus:
   $$
   \int_0^1 \sin^2(2\pi nx) \, dx = \frac{1}{2\pi n} \int_0^{2\pi n} \sin^2(u) \, du
   $$

   **Periodicity:** Since $\sin^2(u)$ has period $\pi$, we have $\int_0^{2\pi n} \sin^2(u) \, du = 2n \int_0^\pi \sin^2(u) \, du = 2n \cdot \frac{\pi}{2} = \pi n$ (using the standard integral $\int_0^\pi \sin^2(u) du = \pi/2$).

   Therefore:
   $$
   \int_0^1 \sin^2(2\pi nx) \, dx = \frac{1}{2\pi n} \cdot \pi n = \frac{1}{2}
   $$

   Thus $\|f_n\|_2^2 = 2 \cdot (1/2) = 1$, so $\|f_n\|_2 = 1$ for all $n$. Hence $\|f_n - 0\|_2 = 1 \not\to 0$, so $f_n \not\to 0$ in norm.

2. **Weak convergence to zero:** We will show $\int_0^1 f_n(x) g(x) \, dx \to 0$ for any $g \in L^2([0,1])$.

   This follows from the **Riemann-Lebesgue Lemma**, which we state and prove for self-containment:

**Lemma 3.24 (Riemann-Lebesgue Lemma).** {#LEM-3.24}
For any $g \in L^1([0,1])$:
$$
\lim_{n \to \infty} \int_0^1 g(x) \sin(2\pi nx) \, dx = 0 \tag{3.37}
$$

This classical result from Fourier analysis captures the cancellation of rapid oscillations: as the sine wave oscillates faster, its integral against any $L^1$ function vanishes.

*Proof.* By density of continuous functions in $L^1$ ([@folland:real_analysis:1999, Proposition 2.10]), it suffices to prove for $g \in C([0,1])$.

For $g \in C^1([0,1])$ (continuously differentiable), integrate by parts with $u = g(x)$, $dv = \sin(2\pi nx) dx$:
$$
\int_0^1 g(x) \sin(2\pi nx) \, dx = \left[-\frac{g(x)}{2\pi n}\cos(2\pi nx)\right]_0^1 + \frac{1}{2\pi n}\int_0^1 \cos(2\pi nx) g'(x) \, dx
$$

Since $\cos(2\pi n) = 1$ for all $n$:
$$
= -\frac{g(1) - g(0)}{2\pi n} + O\left(\frac{1}{n}\right) = O\left(\frac{1}{n}\right) \to 0
$$
(the integral term is bounded by $\|g'\|_1/(2\pi n) \to 0$).

For general $g \in C([0,1])$, approximate by $C^1$ functions (or use Weierstrass approximation) and apply a standard $\epsilon/3$ argument. □

**Returning to Example 3.5:** For any $g \in L^2([0,1])$, since $L^2 \subset L^1$ on finite measure spaces (by Hölder's inequality: $\|g\|_1 \leq \|g\|_2 \|1\|_2 = \|g\|_2 \cdot 1$), we have $g \in L^1$. By [LEM-3.24]:
$$
\int_0^1 f_n(x) g(x) \, dx = \sqrt{2} \int_0^1 \sin(2\pi nx) g(x) \, dx \to 0
$$

Thus $\int f_n g \to \int 0 \cdot g = 0$ for all $g \in L^2$, so $f_n \rightharpoonup 0$ weakly in $L^2([0,1])$ by [DEF-3.13-EXPLICIT].

**Conclusion:** $f_n \rightharpoonup 0$ weakly but $f_n \not\to 0$ strongly. Weak convergence is **strictly weaker** than strong.

**Remark 3.19 (Geometric Intuition).** Think of $f_n = \sqrt{2}\sin(2\pi nx)$ as "oscillating faster and faster." While the functions don't converge pointwise (they oscillate between $-\sqrt{2}$ and $\sqrt{2}$), their "average effect" when tested against smooth functions $g$ vanishes—the positive and negative oscillations cancel out when integrated. This is the essence of weak convergence: behavior in expectation against test functions, not pointwise behavior.

**Visualization note:** (Fig 3.1: plots of $\sin(2\pi nx)$ for $n = 1, 5, 10$—see Friday coding session for numerical verification.)

---

#### **A. Basic Properties of Weak Convergence**

**Proposition 3.15 (Strong Implies Weak).** {#PROP-3.15}
If $f_n \to f$ in $L^p$ norm (i.e., $\|f_n - f\|_p \to 0$), then $f_n \rightharpoonup f$ weakly.

*Proof.* For any $\phi \in (L^p)^*$ with $\|\phi\| < \infty$:
$$
|\phi(f_n) - \phi(f)| = |\phi(f_n - f)| \leq \|\phi\| \|f_n - f\|_p \to 0
$$
(by boundedness of $\phi$). Thus $\phi(f_n) \to \phi(f)$ for all $\phi$, so $f_n \rightharpoonup f$. □

**Remark 3.20 (Converse Fails).** The converse is false in infinite dimensions, as shown by Example 3.5. In **finite dimensions**, weak and strong convergence are equivalent (by compactness of closed bounded sets in $\mathbb{R}^n$).

---

**Proposition 3.16 (Weak Limits are Unique).** {#PROP-3.16}
If $f_n \rightharpoonup f$ and $f_n \rightharpoonup g$ weakly in $L^p$, then $f = g$ $\mu$-almost everywhere.

*Proof.* By linearity, $f_n \rightharpoonup f$ and $f_n \rightharpoonup g$ imply $0 = f_n - f_n \rightharpoonup f - g$. Thus $\phi(f - g) = 0$ for all $\phi \in (L^p)^*$.

By Riesz Representation [THM-3.9], taking $\phi(h) = \int h \cdot \text{sgn}(f-g)|f-g|^{p-1} \, d\mu$ (test functional corresponding to $g = \text{sgn}(f-g)|f-g|^{p-1} \in L^q$):
$$
0 = \phi(f - g) = \int |f - g|^p \, d\mu
$$

Since $|f-g|^p \geq 0$ and its integral is zero, $|f-g|^p = 0$ $\mu$-a.e., hence $f = g$ $\mu$-a.e. □

---

**Proposition 3.17 (Norm Lower Semicontinuity).** {#PROP-3.17}
If $f_n \rightharpoonup f$ weakly in $L^p$, then:
$$
\|f\|_p \leq \liminf_{n \to \infty} \|f_n\|_p \tag{3.38}
$$

(The limit function has norm no larger than the $\liminf$ of norms.)

*Proof.* By Riesz Representation [THM-3.9], the norm on $L^p$ is given by:
$$
\|f\|_p = \sup_{\|g\|_q \leq 1} \left|\int fg \, d\mu\right|
$$

There exists $g \in L^q$ with $\|g\|_q = 1$ such that $\|f\|_p = |\int fg \, d\mu|$ (this $g$ "tests" the norm of $f$).

By weak convergence, $\int f_n g \to \int fg$ for all $g \in L^q$. In particular, for the $g$ that achieves $\|f\|_p$:
$$
\|f\|_p = \left|\int fg \, d\mu\right| = \lim_{n \to \infty} \left|\int f_n g \, d\mu\right| \leq \liminf_{n \to \infty} \|f_n\|_p \|g\|_q = \liminf_{n \to \infty} \|f_n\|_p
$$
(using Hölder's inequality [THM-2.4] and $\|g\|_q = 1$). □

**Remark 3.21 (Strict Inequality Possible).** In Example 3.5, $f_n \rightharpoonup 0$ with $\|f_n\|_2 = 1$ and $\|0\|_2 = 0$. Thus $\|0\|_2 = 0 < 1 = \liminf \|f_n\|_2$ (strict inequality). This shows the norm is only **lower semicontinuous** in the weak topology, not continuous.

---

### **II. Weak* Convergence in $(L^p)^*$**

**Definition 3.14 (Weak* Convergence).** {#DEF-3.14}
Let $(X, \mathcal{F}, \mu)$ be a measure space and $1 \leq p < \infty$. A sequence $\{\phi_n\}$ in $(L^p)^*$ **converges weak*** (pronounced "weak-star") to $\phi \in (L^p)^*$ if:
$$
\phi_n(f) \to \phi(f) \quad \text{for all } f \in L^p \tag{3.39}
$$

We write $\phi_n \overset{*}{\rightharpoonup} \phi$ (weak* limit).

**Remark 3.22 (Explicit Form via $L^q$).** By Riesz Representation [THM-3.9], $(L^p)^* \cong L^q$ for $1 < p < \infty$. Thus $\phi_n \leftrightarrow g_n \in L^q$ via $\phi_n(f) = \int fg_n \, d\mu$. Weak* convergence becomes:
$$
g_n \overset{*}{\rightharpoonup} g \quad \Leftrightarrow \quad \int f g_n \, d\mu \to \int f g \, d\mu \quad \text{for all } f \in L^p \tag{3.40}
$$

**Relation to Weak Convergence:** If we view $L^q$ as a normed space in its own right (since $(L^p)^* \cong L^q$), then:
- **Weak convergence in $L^q$**: $\int g_n h \, d\mu \to \int gh \, d\mu$ for all $h \in (L^q)^* \cong L^p$ (by duality $(L^q)^{**} \cong L^p$ for reflexive spaces)
- **Weak* convergence in $(L^p)^* \cong L^q$**: $\int f g_n \, d\mu \to \int fg \, d\mu$ for all $f \in L^p$

For reflexive spaces ($1 < p < \infty$), these coincide: weak and weak* convergence in $L^q$ are the same. But for $L^1$ and $L^\infty$ (non-reflexive), weak* is weaker than weak.

---

#### **A. Banach-Alaoglu Theorem**

We now arrive at the central compactness result. The proof is substantial, so we present a detailed sketch here and defer the complete proof to **Appendix 3.A** (see end of this file).

**Why Compactness Matters in RL:** Recall the motivating question from the introduction: In policy gradient descent, does $J(\theta_k) = \mathbb{E}_{\rho_{\pi_{\theta_k}}}[V^{\pi_{\theta_k}}]$ converge? If the sequence of state distributions $\{\rho_{\pi_{\theta_k}}\}$ is bounded but not norm-convergent, can we still extract a convergent subsequence? More broadly:

- **Policy iteration** generates sequences of value functions $\{V^{\pi_k}\}$ that are bounded ($\|V^{\pi_k}\|_\infty \leq R_{\max}/(1-\gamma)$). Do convergent subsequences exist?
- **Policy optimization** searches over the space of policies. Is this space compact in any sense? If so, does $\sup_\pi J(\pi)$ attain its supremum (i.e., does an optimal policy exist)?
- **Function approximation** uses sequences of approximate value functions $\{V_\theta^{(k)}\}$. Can we extract convergent subsequences even when strong convergence fails?

The answer to all these questions is **yes**, provided we use the weak* topology. This is the power of Banach-Alaoglu:

**Theorem 3.18 (Banach-Alaoglu Theorem).** {#THM-3.18}
Let $X$ be a normed vector space and $X^*$ its dual. The **closed unit ball** in $X^*$:
$$
B_{X^*} := \{\phi \in X^* : \|\phi\| \leq 1\} \tag{3.41}
$$
is **compact** in the **weak* topology**.

More explicitly: Every bounded sequence $\{\phi_n\}$ in $X^*$ (i.e., $\sup_n \|\phi_n\| < \infty$) has a subsequence $\{\phi_{n_k}\}$ that converges weak* to some $\phi \in X^*$.

**Proof sketch.** The proof uses Tychonoff's theorem (product of compact spaces is compact in product topology). The key steps are:

1. **Embedding into a product space:** For each $x \in X$ with $\|x\| \leq 1$, we have $|\phi(x)| \leq \|\phi\| \|x\| \leq \|\phi\|$. Thus $\phi \in B_{X^*}$ (unit ball) satisfies $\phi(x) \in [-1, 1]$ for all $x$ with $\|x\| \leq 1$.

   We can view $B_{X^*}$ as a subset of the product space:
   $$
   \prod_{x \in B_X} [-\|\phi\|, \|\phi\|]
   $$
   where $B_X = \{x \in X : \|x\| \leq 1\}$. Each $\phi$ is a function $B_X \to \mathbb{R}$, so we embed $B_{X^*}$ into the space of all such functions.

2. **Product topology and Tychonoff:** By Tychonoff's theorem, the product $\prod_{x \in B_X} [-C, C]$ is compact in the product topology (pointwise convergence topology) for any $C > 0$. For bounded sequences $\{\phi_n\}$ with $\|\phi_n\| \leq C$, the image lies in this compact product.

3. **Weak* topology = subspace of product topology:** The weak* topology on $X^*$ is precisely the subspace topology induced by the embedding $\phi \mapsto (\phi(x))_{x \in X}$. Weak* convergence $\phi_n \overset{*}{\rightharpoonup} \phi$ means $\phi_n(x) \to \phi(x)$ for all $x \in X$ (pointwise convergence).

4. **Closedness in product topology:** We must verify that $B_{X^*}$ is a closed subset of the product space (to apply Tychonoff). This follows from the linearity and boundedness conditions defining $X^*$: if $\phi_n \overset{*}{\rightharpoonup} \phi$ (pointwise) and $\|\phi_n\| \leq 1$, then $\phi$ is linear and $\|\phi\| \leq 1$.

5. **Conclusion:** $B_{X^*}$ is a closed subset of a compact space, hence compact. Thus every sequence in $B_{X^*}$ has a convergent subsequence in the weak* topology. □

**For a complete, rigorous proof with all details**, see **Appendix 3.A: Full Proof of Banach-Alaoglu Theorem** at the end of this file.

**Remark 3.23 (Contrast with Strong Topology).** In the **norm topology**, the unit ball in $X^*$ is **not compact** unless $X$ is finite-dimensional (Riesz's theorem). For example, in $L^2([0,1])$, the sequence $f_n(x) = \sqrt{2}\sin(2\pi nx)$ satisfies $\|f_n\|_2 = 1$ for all $n$, but has no norm-convergent subsequence (it converges weakly to $0$, but $\|f_n\|_2 = 1 \not\to 0$). This is why weak* compactness is so powerful: it restores compactness in infinite dimensions.

---

**Pause and Reflect:** Why is Banach-Alaoglu's weak* compactness more powerful than norm compactness in infinite dimensions?

*Hint:* In $L^2([0,1])$, the unit ball $\{f : \|f\|_2 \leq 1\}$ is not norm-compact (no convergent subsequence in norm for $\sin(2\pi nx)$). But by Banach-Alaoglu, it **is** weakly* compact: every bounded sequence has a weak* convergent subsequence. This is essential for existence theorems in optimization and RL, where we need to extract convergent subsequences from bounded iterates.

---

**Corollary 3.19 (Weak* Compactness in $(L^p)^*$).** {#COR-3.19}
For $1 \leq p < \infty$ and $(X, \mathcal{F}, \mu)$ $\sigma$-finite, the closed unit ball in $(L^p)^* \cong L^q$ is weak* compact:
$$
\{g \in L^q : \|g\|_q \leq 1\} \quad \text{is weak* compact} \tag{3.42}
$$

**Proof.** Apply Theorem 3.18 with $X = L^p$. □

---

### **III. RL Applications of Weak Convergence**

We now demonstrate how weak and weak* convergence arise naturally in reinforcement learning. We focus on three applications:

**A.** Value iteration in infinite-state MDPs (weak convergence when strong fails)
**B.** Distribution shift in policy gradients (weak* convergence of state distributions)
**C.** Existence of optimal policies (compactness via Banach-Alaoglu)

**Note:** We originally included a fourth application (least-squares TD and weak continuity of projections), but this connection is more subtle than initially presented. The LSTD fixed point $V_\theta^* = \Pi T^\pi V_\theta^*$ depends on contraction properties of $\Pi T^\pi$, not primarily on weak continuity of $\Pi$. We defer this topic to **Friday's synthesis session**, where we can explore it alongside numerical experiments.

---

#### **A. Value Iteration in Infinite-State MDPs**

**Context:** In **finite-state MDPs**, value iteration enjoys **strong (exponential) convergence** by the Banach Fixed-Point Theorem: $\|V^{(k)} - V^*\|_\infty \leq \gamma^k \|V^{(0)} - V^*\|_\infty$ (geometric rate $\gamma$). This is norm convergence, the strongest form.

However, weak convergence becomes relevant in **infinite-state MDPs** where strong convergence may fail but weak convergence (in a weighted $L^2$ space under the stationary distribution) still holds. This is the setting where Banach-Alaoglu provides convergent subsequences.

**Example 3.6 (Infinite-State MDP with Weak but Not Strong Convergence).** {#EX-3.6}

Consider a countable-state MDP with state space $\mathcal{S} = \{1, 2, 3, \ldots\}$ and the following structure:
- **Transition dynamics:** From state $s$, the agent moves to state $s+1$ with probability $1$ (deterministic rightward drift).
- **Reward:** $r(s, a) = 1/s$ (reward decays as $1/s$).
- **Discount:** $\gamma = 0.9$.

The optimal value function is $V^*(s) = \sum_{k=0}^\infty \gamma^k \cdot \frac{1}{s+k}$ (sum of discounted future rewards). This series converges, so $V^* \in \ell^\infty(\mathcal{S})$ (bounded).

Now consider a sequence of "truncated" approximations:
$$
V_n(s) := \begin{cases} V^*(s) & \text{if } s \leq n \\ 0 & \text{if } s > n \end{cases}
$$

**Strong convergence fails:** $\|V_n - V^*\|_\infty = \sup_{s > n} V^*(s) = V^*(n+1) \not\to 0$ (since $V^*(n+1) \sim 1/n \to 0$ only as $n \to \infty$, but the supremum over $s > n$ doesn't vanish).

**Weak convergence holds:** For any probability distribution $\rho$ on $\mathcal{S}$ (e.g., stationary distribution) with $\sum_s \rho(s) = 1$:
$$
\mathbb{E}_\rho[V_n] = \sum_s V_n(s) \rho(s) = \sum_{s \leq n} V^*(s) \rho(s) \to \sum_s V^*(s) \rho(s) = \mathbb{E}_\rho[V^*]
$$
(by dominated convergence, since $|V_n(s)| \leq V^*(s) \leq \|V^*\|_\infty < \infty$ and $\sum_s \rho(s) < \infty$).

This is weak convergence in the sense of functionals: $\phi_\rho(V_n) := \mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V^*]$ for all probability distributions $\rho$. By the identification $\ell^1 \hookrightarrow (\ell^\infty)^*$, this is weak* convergence in $\ell^\infty$.

**RL significance:** In practice, we often only care about $\mathbb{E}_\rho[V(s)]$ for a specific distribution $\rho$ (e.g., initial state distribution). Weak convergence is sufficient for this purpose—we don't need uniform convergence $\|V_n - V^*\|_\infty \to 0$ over all states. This matters for:
- **Approximate policy iteration**: Errors in policy evaluation may prevent strong convergence but allow weak convergence.
- **Function approximation**: Neural network value functions $V_\theta$ may not converge uniformly but can converge in expectation under the data distribution.

For detailed theory of infinite-state MDPs with weak convergence, see [@meyn-tweedie:markov_chains:2009, Chapter 17].

---

#### **B. Distribution Shift in Policy Gradient Methods**

**Context:** In **policy gradient methods** (Week 37), we optimize:
$$
J(\theta) = \mathbb{E}_{\rho_{\pi_\theta}}[V^{\pi_\theta}(s_0)]
$$
where $\rho_{\pi_\theta}$ is the state visitation distribution under policy $\pi_\theta$, and $s_0 \sim \rho_0$ is the initial state.

During gradient descent $\theta_{k+1} = \theta_k + \alpha \nabla J(\theta_k)$, both $\pi_\theta$ and $\rho_{\pi_\theta}$ change at each iteration. The sequence of distributions $\{\rho_{\pi_{\theta_k}}\}$ may not converge in total variation distance (strong convergence of measures), but it often converges **weak*** (convergence of measures in the weak topology).

**Definition 3.15 (Weak* Convergence of Probability Measures).** {#DEF-3.15}
A sequence of probability measures $\{\rho_n\}$ on $(X, \mathcal{F})$ converges **weak*** to $\rho$ if:
$$
\int_X f \, d\rho_n \to \int_X f \, d\rho \quad \text{for all continuous bounded } f: X \to \mathbb{R} \tag{3.43}
$$

**Remark 3.25 (Terminology).** In probability theory, this is called **weak convergence of probability measures** ([@billingsley:convergence:1999]). In functional analysis, it's **weak* convergence** when viewing measures as elements of $(C_b(X))^*$ (dual of continuous bounded functions). The two notions coincide by the Riesz-Markov theorem [@folland:real_analysis:1999, §7.2].

**Proposition 3.21 (Objective Convergence Under Weak* + Uniform).** {#PROP-3.21}
Suppose $\rho_n \overset{*}{\rightharpoonup} \rho$ (weak* convergence of measures) and $V_n \to V$ uniformly (i.e., $\|V_n - V\|_\infty \to 0$). Then:
$$
\mathbb{E}_{\rho_n}[V_n(s)] \to \mathbb{E}_\rho[V(s)] \tag{3.44}
$$

*Proof.* We decompose the error into two terms corresponding to function convergence and measure convergence:

**Term A (function convergence, uniform):**
$$
\left|\mathbb{E}_{\rho_n}[V_n] - \mathbb{E}_{\rho_n}[V]\right| = \left|\int (V_n - V) \, d\rho_n\right| \leq \int |V_n - V| \, d\rho_n \leq \|V_n - V\|_\infty \underbrace{\rho_n(\mathcal{S})}_{=1} \to 0
$$
(by uniform convergence $V_n \to V$ and $\rho_n$ being a probability measure).

**Term B (measure convergence, weak*):**
$$
\left|\mathbb{E}_{\rho_n}[V] - \mathbb{E}_\rho[V]\right| = \left|\int V \, d\rho_n - \int V \, d\rho\right| \to 0
$$
(by weak* convergence $\rho_n \overset{*}{\rightharpoonup} \rho$ and boundedness of $V$, assuming $V$ is continuous or at least $\rho_n$-uniformly integrable).

**Combining:** By triangle inequality:
$$
\left|\mathbb{E}_{\rho_n}[V_n] - \mathbb{E}_\rho[V]\right| \leq \underbrace{\left|\mathbb{E}_{\rho_n}[V_n] - \mathbb{E}_{\rho_n}[V]\right|}_{\text{Term A} \to 0} + \underbrace{\left|\mathbb{E}_{\rho_n}[V] - \mathbb{E}_\rho[V]\right|}_{\text{Term B} \to 0} \to 0
$$

Thus $\mathbb{E}_{\rho_n}[V_n] \to \mathbb{E}_\rho[V]$. □

**Implication for Policy Gradients:** Even if $\rho_{\pi_{\theta_k}}$ doesn't converge in total variation distance (strong), weak* convergence is sufficient to guarantee $J(\theta_k) = \mathbb{E}_{\rho_{\pi_{\theta_k}}}[V^{\pi_{\theta_k}}] \to J(\theta^*)$ (objective convergence), provided $V^{\pi_{\theta_k}} \to V^{\pi_{\theta^*}}$ uniformly.

**Practical Note:** In practice, neural network policies $\pi_\theta$ are continuous in $\theta$, so $\theta_k \to \theta^*$ implies $\rho_{\pi_{\theta_k}} \overset{*}{\rightharpoonup} \rho_{\pi_{\theta^*}}$ (weak* continuity). This underpins convergence guarantees for actor-critic methods. For formal results, see [@sutton-barto:rl_intro:2018, Chapter 13] and [@kakade:natural_pg:2001].

---

**Pause and Reflect:** When is weak convergence sufficient in RL, and when do we need strong convergence?

*Hint:* Weak convergence of value functions $V_n \rightharpoonup V^*$ suffices for $\mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V^*]$ (objective convergence under a specific distribution $\rho$). But strong convergence $\|V_n - V^*\|_\infty \to 0$ is needed for **uniform error bounds** across all states—critical for safety-critical applications where worst-case guarantees matter.

---

#### **C. Existence of Optimal Policies via Banach-Alaoglu**

**Context:** In general MDPs (infinite state spaces, non-tabular), does an optimal policy $\pi^*$ achieving $J(\pi^*) = \sup_\pi J(\pi)$ always exist? Not necessarily—the supremum might not be attained (e.g., supremum over open set in $\mathbb{R}$).

Banach-Alaoglu provides the compactness needed for existence theorems:

**Theorem 3.22 (Existence of Optimal Policies, Compact Formulation).** {#THM-3.22}
Consider an MDP with:
- Compact state space $\mathcal{S}$ (e.g., $\mathcal{S} = [0,1]^d$)
- Compact action space $\mathcal{A}$
- Continuous reward $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$
- Continuous transition kernel $P(\cdot|s,a)$ (in weak topology of measures)

If the set of policies is **weakly* compact** (e.g., all policies $\pi(\cdot|s)$ with $\|\pi(\cdot|s)\|_1 = 1$, viewed as measures), then there exists an optimal policy $\pi^*$ with $J(\pi^*) = \sup_\pi J(\pi)$.

**Proof sketch.** This is an informal sketch; the full proof requires advanced MDP theory (see [@puterman:mdps:2005, Theorem 6.2.10] for weak continuity of the policy evaluation operator and Theorem 6.2.7 for existence).

**Step 1: Policy set is weakly* compact (Banach-Alaoglu).** Policies $\pi(\cdot|s)$ are probability distributions on $\mathcal{A}$, viewed as elements of $(C(\mathcal{A}))^*$ (dual of continuous functions on $\mathcal{A}$). By the Riesz-Markov theorem [@folland:real_analysis:1999, §7.2], this is the space of signed measures on $\mathcal{A}$. The set of probability measures is a subset of the unit ball in $(C(\mathcal{A}))^*$, hence weak* compact by [THM-3.18].

**Step 2: Objective $J(\pi)$ is weak* continuous.** The objective $J(\pi) = \mathbb{E}_{\rho_\pi}[V^\pi(s_0)]$ depends on the value function $V^\pi$, which solves the Bellman equation $V^\pi = T^\pi V^\pi = R^\pi + \gamma P^\pi V^\pi$ (where $T^\pi$ is the policy evaluation operator).

For weak* convergence $\pi_n \overset{*}{\rightharpoonup} \pi$ to imply $J(\pi_n) \to J(\pi)$, we need:
1. $V^{\pi_n} \to V^\pi$ (convergence of value functions)
2. $\rho_{\pi_n} \overset{*}{\rightharpoonup} \rho_\pi$ (convergence of state distributions)

The first follows from continuity of the policy evaluation operator $\pi \mapsto V^\pi$ in the weak* topology. This requires analysis of the Neumann series $V^\pi = \sum_{k=0}^\infty \gamma^k (P^\pi)^k R^\pi$ and showing that $P^{\pi_n} \to P^\pi$ weakly implies $V^{\pi_n} \to V^\pi$ uniformly (see [@puterman:mdps:2005, Theorem 6.2.10] for full proof).

The second (state distribution convergence) follows from weak continuity of the stationary distribution map $\pi \mapsto \rho_\pi$ (see Exercise 3.3.4(c) for finite-state case; continuous-state version requires [@billingsley:convergence:1999, Theorem 6.7]).

Given (1) and (2), [PROP-3.21] implies $J(\pi_n) \to J(\pi)$ (objective continuity).

**Step 3: Maximum is attained.** By weak* compactness (Step 1), any sequence $\{\pi_n\}$ with $J(\pi_n) \to \sup_\pi J(\pi)$ has a weak* convergent subsequence $\pi_{n_k} \overset{*}{\rightharpoonup} \pi^*$. By weak* continuity (Step 2), $J(\pi^*) = \lim J(\pi_{n_k}) = \sup_\pi J(\pi)$.

Thus $\pi^*$ is optimal. □

**Note on rigor:** The above is an **informal sketch**. The full proof requires:
- Precise definition of **weak continuity of transition kernels** (see [@hernandez-lerma-lasserre:mdps:1996, Definition 4.2.1])
- Verification that $\pi \mapsto V^\pi$ is continuous in weak* topology via Neumann series analysis
- Uniform integrability conditions for interchange of limits

For complete details, see [@puterman:mdps:2005, Chapter 6, §6.2-6.3] (Theorem 6.2.10 on weak continuity and Theorem 6.2.7 on existence of optimal policies).

**Remark 3.26 (Contrast with Finite MDPs).** For **finite state/action spaces**, existence of optimal policies is trivial (the set of policies is finite, so the supremum is attained). But for **continuous control** (e.g., robotic tasks with $\mathcal{S} = \mathbb{R}^d$, $\mathcal{A} = \mathbb{R}^m$), compactness arguments via Banach-Alaoglu are essential.

**Modern Deep RL:** Neural network policies $\pi_\theta$ with bounded weights $\|\theta\| \leq R$ form a weakly* compact set (by Banach-Alaoglu, since $\theta$ lies in a bounded subset of a Banach space). This ensures that gradient descent on $J(\theta)$ can converge to a local maximum (though global optimality is not guaranteed due to non-convexity of neural network parameterizations).

---

**Pause and Reflect:** How does Banach-Alaoglu guarantee existence of optimal policies?

*Hint:* The set of policies (viewed as elements of $(C(\mathcal{A}))^*$) is weakly* compact by Banach-Alaoglu. The objective $J(\pi)$ is weak* continuous (under continuity assumptions on $r$ and $P$). By compactness, the continuous function $J$ attains its supremum on the policy set, so an optimal policy $\pi^* \in \arg\max_\pi J(\pi)$ exists.

---

### **IV. Modern Deep RL: Theory-Practice Gaps**

The three RL applications above (infinite-state value iteration, distribution shift, existence of optimal policies) are grounded in weak convergence theory. However, modern deep RL algorithms operate in regimes where classical theory provides only partial guidance. We briefly survey these gaps:

**Policy Gradients (PPO, TRPO):**
- **Theory:** [PROP-3.21] shows that weak* convergence of state distributions $\rho_{\pi_\theta_k} \overset{*}{\rightharpoonup} \rho_{\pi_{\theta^*}}$ + uniform value convergence $V^{\pi_\theta_k} \to V^{\pi_{\theta^*}}$ implies $J(\theta_k) \to J(\theta^*)$.
- **Practice:** PPO [@schulman:ppo:2017] uses clipped surrogate objectives and finite-horizon rollouts. The finite-horizon setting introduces bias (infinite-horizon theory doesn't directly apply). Empirically, PPO converges reliably, but formal guarantees are limited to tabular or linear function approximation [@agarwal:theory_pg:2021].
- **Gap:** No general convergence theory for PPO with neural network function approximation. Weak convergence analysis suggests robustness to distribution shift, but formal proofs remain open.

**Off-Policy Methods (DQN, Experience Replay):**
- **Theory:** Q-learning is inherently **off-policy** (learns $Q^*$ under behavior policy $\mu \neq \pi$). Classical theory [@watkins:qlearning:1992] assumes samples from a fixed distribution.
- **Practice:** Experience replay [@mnih:dqn:2015] samples from a buffer containing transitions from many past policies. This creates a **non-stationary data distribution** $\rho_{\text{replay}}$ (mixture of past policies), violating the fixed-distribution assumption.
- **Why DQN works despite this:**
  - **Contraction:** The Bellman operator $T^* Q = \max_a (r + \gamma P Q)$ is a contraction in $\|\cdot\|_\infty$ (uniform convergence), **independent of the data distribution** (Weeks 16-18).
  - **Exploration:** $\epsilon$-greedy ensures sufficient coverage of state-action space.
  - **Target networks:** Slow-moving target $Q_{\theta^-}$ reduces non-stationarity.
- **Gap:** No formal convergence proof for DQN with neural networks and experience replay. The non-stationarity is a practical necessity (sample efficiency), but breaks classical theory.

**Importance Sampling for Off-Policy RL:**
- **Theory:** Off-policy actor-critic [@degris:off_policy_ac:2012] multiplies gradient by $\pi_\theta(a|s)/\mu(a|s)$ (importance ratio) to correct for distribution mismatch.
- **Practice:** High-variance importance ratios can destabilize learning. Modern methods use:
  - **Retrace** [@munos:retrace:2016]: Multi-step off-policy correction with bounded importance weights
  - **V-trace** [@espeholt:impala:2018]: Clipped importance weights for stability
  - **Reward-weighted regression** [@peters:rwr:2007]: Implicit importance weighting via weighted supervised learning
- **Connection to weak* convergence:** As behavior policy $\mu$ approaches target policy $\pi_\theta$, the importance ratio $\pi_\theta/\mu \to 1$ and variance decreases. This is closely related to weak* convergence $\mu \overset{*}{\rightharpoonup} \pi_\theta$ (when $\mu$ is close to $\pi_\theta$, the distributions are "close" in weak* topology, reducing importance sampling variance).

**Function Approximation and Weak Convergence:**
- **Theory:** [PROP-3.23] (deferred to Friday) shows orthogonal projections $\Pi: L^2 \to \mathcal{V}$ are weakly continuous. This suggests approximate value functions $V_\theta$ can converge weakly even when strong convergence fails.
- **Practice:** Neural networks $V_\theta$ provide **approximate** projections (not exact orthogonal projections). Weak convergence analysis suggests robustness, but formal convergence guarantees remain elusive [@bertsekas-tsitsiklis:neuro-dp:1996].

**Summary:** Weak and weak* convergence provide conceptual frameworks for understanding distribution shift, existence of optimal policies, and robustness of function approximation. However, modern deep RL operates in regimes (non-stationary data, nonlinear function approximation, finite-horizon) where classical theory gives only partial coverage. Bridging this gap is an active research area (see [@agarwal:theory_deep_rl:2022] for recent progress).

---

### **V. Summary and Looking Ahead**

**Mathematical Insight:**

Today we introduced two topologies on function spaces:
1. **Strong (norm) topology**: $\|f_n - f\|_p \to 0$ (convergence in $L^p$ norm)
2. **Weak topology**: $\int f_n g \to \int fg$ for all $g \in L^q$ (convergence tested by dual functionals)

Key properties:
- **Strong $\Rightarrow$ weak** ([PROP-3.15]), but not conversely (Example 3.5)
- **Weak limits are unique** ([PROP-3.16])
- **Norm lower semicontinuity** ([PROP-3.17]): $\|f\|_p \leq \liminf \|f_n\|_p$
- **Banach-Alaoglu [THM-3.18]**: Bounded sequences in $(L^p)^*$ have weak* convergent subsequences (compactness)

**Connection to Days 1-2:**
- Day 1: $L^p$ is complete [THM-3.4] (Riesz-Fischer)
- Day 2: $(L^p)^* \cong L^q$ [THM-3.9] (Riesz Representation)
- Day 3: Weak/weak* topologies reveal compactness properties essential for existence theorems

**RL Connection:**

Weak convergence is crucial for:
1. **Infinite-state value iteration**: Weak convergence when strong fails (Example 3.6)
2. **Distribution shift**: State distributions $\rho_{\pi_\theta}$ converge weak* during policy gradient descent
3. **Existence of optimal policies**: Banach-Alaoglu guarantees weak* compactness of policy sets

**Looking Ahead:**

- **Day 4 (Thursday, Extended Proof)**: **Radon-Nikodym theorem**—when does a measure have a density $d\mu/d\nu$? This formalizes importance sampling ratios $\pi/\mu$ used in off-policy RL.

- **Day 5 (Friday, Synthesis)**: Weekly reflection on $L^p$ completeness and duality, coding exercises on weak convergence and importance sampling.

- **Week 4**: Probability spaces and conditional expectation—formalizing MDPs as measure-theoretic objects.

- **Week 14 (Hilbert Spaces)**: Orthogonal projections in $L^2$ and the Projection Theorem, foundation of least-squares TD (Proposition 3.23 fully proved).

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_3_exercises_draft_revised_all]]**

**Anchor Exercise Preview:**
1. **Verify weak but not strong convergence:** Show $f_n(x) = \sqrt{2}\sin(2\pi nx)$ converges weakly to $0$ in $L^2([0,1])$ but $\|f_n\|_2 = 1$ for all $n$. **(20 min)**

2. **Apply Banach-Alaoglu:** Prove that any bounded sequence in $\ell^2$ has a weakly convergent subsequence. **(15 min)**

3. **RL Application (Distribution Shift):** Show that if $\rho_n \overset{*}{\rightharpoonup} \rho$ (weak* convergence of state distributions) and $V_n \to V$ uniformly, then $\mathbb{E}_{\rho_n}[V_n] \to \mathbb{E}_\rho[V]$. **(20 min)**

4. **Continuity of State Distributions:** Show that if $\pi_\theta$ is continuous in $\theta$ (for finite-state MDP), then $\rho_{\pi_\theta_k} \to \rho_{\pi_{\theta^*}}$ (pointwise = weak*) when $\theta_k \to \theta^*$. **(25 min)**

**Total exercise time:** ~90-120 minutes (can extend to Thursday; see Day_3_exercises_draft_revised_all.md for full solutions)

---

**Reflection Questions:**

1. **Why is weak* compactness (Banach-Alaoglu) more powerful than norm compactness in infinite dimensions?**
   *Hint:* In $L^2([0,1])$, the unit ball $\{f : \|f\|_2 \leq 1\}$ is not norm-compact (no convergent subsequence in norm for $\sin(2\pi nx)$), but it is weakly* compact (every bounded sequence has weak* convergent subsequence).

2. **When is weak convergence sufficient in RL, and when do we need strong convergence?**
   *Hint:* Weak convergence of value functions $V_n \rightharpoonup V^*$ suffices for $\mathbb{E}_\rho[V_n] \to \mathbb{E}_\rho[V^*]$ (objective convergence). But strong convergence $\|V_n - V^*\|_\infty \to 0$ is needed for uniform error bounds across all states.

3. **How does Banach-Alaoglu guarantee existence of optimal policies?**
   *Hint:* The set of policies (viewed as elements of $(C(\mathcal{A}))^*$) is weakly* compact by Banach-Alaoglu. The objective $J(\pi)$ is weak* continuous. Thus $\sup_\pi J(\pi)$ is attained.

---

**Daily Study Note:**

**What I learned today:**
- **Weak convergence** $f_n \rightharpoonup f$ in $L^p$: $\int f_n g \to \int fg$ for all $g \in L^q$ (conjugate)
- **Weak* convergence** $\phi_n \overset{*}{\rightharpoonup} \phi$ in $(L^p)^*$: $\phi_n(f) \to \phi(f)$ for all $f \in L^p$
- **Key properties**: Strong $\Rightarrow$ weak, weak limits unique, norm lower semicontinuity
- **Banach-Alaoglu [THM-3.18]**: Bounded sequences in dual spaces have weak* convergent subsequences (compactness!)
- **RL applications**: Infinite-state value iteration (weak convergence when strong fails), distribution shift (weak* convergence of $\rho_\pi$), existence of optimal policies

**Connection to previous material:**
- Builds on Riesz Representation [THM-3.9] (Day 2): duality $(L^p)^* \cong L^q$ enables explicit characterization of weak convergence
- Uses Riesz-Fischer [THM-3.4] (Day 1): completeness ensures weak limits lie in $L^p$
- Prepares for Radon-Nikodym (Day 4): weak* convergence of measures formalizes distribution shift

**Looking forward:**
- Day 4: Radon-Nikodym theorem—densities $d\mu/d\nu$ for importance sampling
- Day 5: Weekly synthesis, coding exercises on weak convergence and importance sampling
- Week 14: Hilbert spaces, orthogonal projections, Projection Theorem

**RL connections identified:**
- Infinite-state value iteration: weak convergence sufficient for expectation convergence
- Distribution shift: state distributions converge weak* during policy gradient descent
- Existence of optimal policies: Banach-Alaoglu + weak* continuity of $J(\pi)$

**Time spent:** 120-150 minutes (theory core 90-120 min + initial exercises 30 min; remaining exercises on Thursday)

---

**End of Day 3 Theory**

---

## **Appendix 3.A: Full Proof of the Banach-Alaoglu Theorem** {#APP-3.A}

See companion file: **[[Day_3_Appendix_Banach_Alaoglu]]** for the complete, rigorous proof with all details.

The appendix covers:
- Tychonoff's theorem (statement and use)
- Product topology on $\prod_{x \in X} [-\|\phi\|, \|\phi\|]$
- Embedding $B_{X^*} \hookrightarrow$ product space
- Weak* topology = subspace topology of product topology
- Closedness of $B_{X^*}$ in product topology (linearity and boundedness preserved under pointwise limits)
- Conclusion: $B_{X^*}$ is closed subset of compact space, hence compact

**Estimated reading time:** 30-40 minutes (optional, can defer to Week 14 when we study functional analysis in depth)
