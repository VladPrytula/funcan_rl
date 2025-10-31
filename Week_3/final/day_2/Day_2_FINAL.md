### Agenda:

##### 📘 Day 2 — Week 3: Duality of $L^p$ Spaces—The Riesz Representation Theorem

**Total time: ~90 minutes (Tuesday)**
**Actual time estimate: 90-120 minutes for rigorous duality theory**

---

#### **⏱️ Segment 1 (40 min) — Reading**

**Topic:** _Duality of $L^p$ spaces: $(L^p)^* \cong L^q$ for conjugate exponents_

- Read from **Folland §6.3-6.4** [@folland:real_analysis:1999, §6.3-6.4] ($L^p$ duality) or **Brezis Ch 4** [@brezis:functional_analysis:2011, Ch 4] (Functional Analysis)
- Focus on:
    - **Dual space $(L^p)^*$**: continuous linear functionals $\phi: L^p \to \mathbb{R}$ with $|\phi(f)| \leq C\|f\|_p$
    - **Conjugate exponents**: $1/p + 1/q = 1$ (e.g., $(p=2, q=2)$, $(p=1, q=\infty)$, $(p=4, q=4/3)$)
    - **Riesz Representation Theorem**: Every $\phi \in (L^p)^*$ has the form $\phi(f) = \int fg \, d\mu$ for some unique $g \in L^q$
    - **Isometric isomorphism**: $(L^p)^* \cong L^q$ with $\|\phi\| = \|g\|_q$
    - **RL significance**: Linear value function approximation lives in $(L^2)^*$; state distributions are dual to value functions

---

#### **⏱️ Segment 2 (40 min) — Proof and Exercises**

**Primary Task:**
1. **State the Riesz Representation Theorem** for $(L^p)^*$ when $1 < p < \infty$
2. **Understand the proof strategy**:
   - Step 1: Define candidate $g \in L^q$ from $\phi$ (construction on simple functions, extend by density)
   - Step 2: Prove $g \in L^q$ with $\|g\|_q = \|\phi\|$
   - Step 3: Show $\phi(f) = \int fg \, d\mu$ for all $f \in L^p$
   - Step 4: Prove uniqueness of $g$ (if $\phi(f) = \int fg_1 = \int fg_2$ for all $f$, then $g_1 = g_2$ a.e.)
3. **Special cases**:
   - $(L^2)^* \cong L^2$ (self-dual)
   - $(L^1)^* \cong L^\infty$ on σ-finite spaces
   - $(L^\infty)^* \supsetneq L^1$ in general (duality fails for $L^\infty$)

**Guidance:**
- The proof uses **Hölder's inequality** [THM-2.4] crucially: $\int |fg| \leq \|f\|_p \|g\|_q$
- For $1 < p < \infty$, the proof constructs $g$ by defining $\phi$ on characteristic functions and extending by linearity
- The $p = 1$ case requires σ-finiteness; without it, $(L^1)^*$ can be strictly larger than $L^\infty$

---

#### **💡 Conceptual Bridge to RL**

**Why duality matters in RL:** In MDPs, the **state visitation distribution** $\mu_\pi$ under policy $\pi$ and the **value function** $V^\pi: \mathcal{S} \to \mathbb{R}$ are related via the performance objective:
$$
J(\pi) = \mathbb{E}_{\mu_\pi}[V^\pi(s)] = \int_\mathcal{S} V^\pi(s) \, \mu_\pi(ds)
$$
This is **precisely the duality pairing** $\langle V^\pi, \mu_\pi \rangle$ between:
- $V^\pi \in L^2(\mathcal{S}, \nu)$ (value function; lives in function space)
- $\mu_\pi$ (state visitation distribution; induces a functional $\phi_\mu(V) = \mathbb{E}_\mu[V(s)]$ in $(L^2)^*$)

By Riesz representation [THM-3.9], if $\mu_\pi \ll \nu$ (absolute continuity with respect to reference measure $\nu$), then $\phi_{\mu_\pi}$ corresponds to the density $d\mu_\pi/d\nu \in L^2(\nu)$ via:
$$
\mathbb{E}_{\mu_\pi}[V(s)] = \int_\mathcal{S} V(s) \frac{d\mu_\pi}{d\nu}(s) \, d\nu(s)
$$
This formalizes the state-value duality used in policy gradient derivations (Week 37).

**Connection to Day 1:** Yesterday we proved $L^p$ is complete (Riesz-Fischer [THM-3.4]). Today we study its **dual space**—the continuous linear functionals. The combination "complete + duality" makes $L^p$ a **reflexive Banach space** for $1 < p < \infty$ (i.e., $(L^p)^{**} \cong L^p$).

**Preview for Day 3:** Tomorrow we continue duality for special cases ($L^1$ and $L^\infty$) and discuss counterexamples where duality fails. Thursday we move to **Radon-Nikodym theorem** (densities $d\mu/d\nu$), the foundation of importance sampling.

---

## **Chapter 3.2: Duality of $L^p$ Spaces**

### **Motivation: What is the Dual Space?**

Recall from Day 1 that $L^p(\mu)$ is a **Banach space** (complete normed vector space) for $1 \leq p \leq \infty$ by Riesz-Fischer [THM-3.4]. Today we study the **dual space** $(L^p)^*$, which consists of all **continuous linear functionals** on $L^p$.

**Definition 3.8 (Dual Space).** {#DEF-3.8}
Let $X$ be a normed vector space. The **dual space** $X^*$ is the set of all **bounded linear functionals** $\phi: X \to \mathbb{R}$ (or $\mathbb{C}$ for complex spaces), i.e., linear maps satisfying:
$$
\exists C \geq 0 : |\phi(f)| \leq C\|f\| \quad \text{for all } f \in X \tag{3.14}
$$

Equipped with the **operator norm**:
$$
\|\phi\| = \sup_{\|f\| \leq 1} |\phi(f)| = \sup_{f \neq 0} \frac{|\phi(f)|}{\|f\|} \tag{3.15}
$$
$X^*$ is itself a Banach space (even if $X$ is not complete, $X^*$ always is; see [@brezis:functional_analysis:2011, Theorem 1.10]).

**Remark 3.8 (Continuity vs. Boundedness).** For **linear** functionals, **continuity** and **boundedness** are equivalent (see [@folland:real_analysis:1999, Proposition 5.3]). Thus "$\phi \in X^*$" means "$\phi$ is a continuous linear functional." For nonlinear maps, boundedness does not imply continuity, so the distinction matters. Throughout this chapter, "functional" always means "linear functional."

---

#### **A. Examples of Dual Spaces**

**Example 3.1 (Finite Dimensions).** For $X = \mathbb{R}^n$ with any norm, the dual space $X^*$ is isomorphic to $\mathbb{R}^n$ itself. Every linear functional $\phi: \mathbb{R}^n \to \mathbb{R}$ has the form $\phi(x) = a^\top x$ for some $a \in \mathbb{R}^n$. Thus $(\mathbb{R}^n)^* \cong \mathbb{R}^n$ (canonical isomorphism).

**Example 3.2 ($\ell^p$ Spaces).** For the sequence space $\ell^p = \{(x_n) : \sum |x_n|^p < \infty\}$ with $1 \leq p < \infty$, the dual is:
$$
(\ell^p)^* \cong \ell^q \quad \text{where } 1/p + 1/q = 1
$$

Every $\phi \in (\ell^p)^*$ has the form $\phi(x) = \sum_{n=1}^\infty a_n x_n$ for some $a = (a_n) \in \ell^q$, with $\|\phi\| = \|a\|_q$ (by Hölder's inequality).

**Example 3.3 ($C([0,1])$ with sup norm).** The dual of $(C([0,1]), \|\cdot\|_\infty)$ is the space of **signed Radon measures** on $[0,1]$:
$$
(C([0,1]))^* \cong \mathcal{M}([0,1]) \quad \text{(Riesz-Markov representation theorem)}
$$

Every $\phi \in (C([0,1]))^*$ has the form $\phi(f) = \int_{[0,1]} f \, d\mu$ for some signed Borel measure $\mu$.

**Example 3.4 ($L^p$ Spaces—Today's Goal).** For $1 \leq p < \infty$ and σ-finite $(X, \mathcal{F}, \mu)$:
$$
(L^p(\mu))^* \cong L^q(\mu) \quad \text{where } 1/p + 1/q = 1
$$

This is the **Riesz Representation Theorem** for $L^p$ spaces (Theorem 3.9 below).

---

#### **B. Conjugate Exponents**

**Definition 3.9 (Conjugate Exponents).** {#DEF-3.9}
Two numbers $1 \leq p, q \leq \infty$ are **conjugate** (or **dual**, or **Hölder conjugate**) if:
$$
\frac{1}{p} + \frac{1}{q} = 1 \tag{3.16}
$$

**Conventions:**
- If $p = 1$, then $q = \infty$ (since $1/1 + 1/\infty = 1 + 0 = 1$)
- If $p = \infty$, then $q = 1$
- If $p = 2$, then $q = 2$ (self-conjugate)

**Notation:** We often write $q = p'$ or $q = p/(p-1)$ for the conjugate of $p$.

**Remark 3.9 (Equivalent Form).** Equation (3.16) is equivalent to:
$$
q = \frac{p}{p-1} \quad \text{for } 1 < p < \infty \tag{3.17}
$$

**Proof:** From $1/p + 1/q = 1$, solve for $q$:
$$
\frac{1}{q} = 1 - \frac{1}{p} = \frac{p-1}{p} \Rightarrow q = \frac{p}{p-1} \quad \square
$$

**Common Conjugate Pairs:**
- $p = 1 \leftrightarrow q = \infty$
- $p = 2 \leftrightarrow q = 2$ (self-dual)
- $p = 4 \leftrightarrow q = 4/3$
- $p = 3/2 \leftrightarrow q = 3$
- $p = 6 \leftrightarrow q = 6/5$

**Symmetry:** The conjugate relation is symmetric: if $q$ is conjugate to $p$, then $p$ is conjugate to $q$ (since $1/p + 1/q = 1/q + 1/p$).

---

### **II. The Riesz Representation Theorem for $(L^p)^*$**

**Theorem 3.9 (Riesz Representation for $(L^p)^*$, $1 < p < \infty$).** {#THM-3.9}
Let $(X, \mathcal{F}, \mu)$ be a σ-finite measure space and $1 < p < \infty$. Let $q$ be the conjugate exponent ($1/p + 1/q = 1$). Then:

**(Existence and Uniqueness):** For every continuous linear functional $\phi \in (L^p(\mu))^*$, there exists a **unique** $g \in L^q(\mu)$ (up to sets of measure zero) such that:
$$
\phi(f) = \int_X f g \, d\mu \quad \text{for all } f \in L^p(\mu) \tag{3.18}
$$

**(Isometry):** The operator norm of $\phi$ equals the $L^q$ norm of $g$:
$$
\|\phi\| = \|g\|_q \tag{3.19}
$$

**(Isomorphism):** The map $T: L^q(\mu) \to (L^p(\mu))^*$ defined by $T(g) = \phi_g$ (where $\phi_g(f) = \int fg \, d\mu$) is an **isometric isomorphism**. Thus:
$$
(L^p)^* \cong L^q \quad \text{(isometrically)} \tag{3.20}
$$

**Remark 3.10 (Bilinear Pairing).** The integral $\langle f, g \rangle := \int fg \, d\mu$ defines a **bilinear pairing** between $L^p$ and $L^q$. The theorem states that every continuous linear functional on $L^p$ arises from such a pairing with some $g \in L^q$.

**Remark 3.11 (Historical Context).** This theorem is another result due to **Frigyes Riesz** (1909), who proved it as part of his development of functional analysis on $L^p$ spaces. It generalizes the Riesz-Fischer theorem [THM-3.4] (completeness) by characterizing the **dual space** structure. The proof we present follows [@folland:real_analysis:1999, Theorem 6.14] and [@brezis:functional_analysis:2011, Theorem 4.10], using a constructive approach via simple functions.

---

**Proof (Case $1 < p < \infty$).**

The proof proceeds in four steps:
1. **Construction of $g$:** Define $g$ on simple functions, extend by density
2. **Prove $g \in L^q$:** Show $\|g\|_q = \|\phi\|$ using clever test functions
3. **Show $\phi(f) = \int fg$:** Verify the representation formula
4. **Uniqueness:** Prove $g$ is unique up to null sets

**Step 1: Construction of $g$ on simple functions.**

**Setup:** Let $\phi \in (L^p)^*$ be a continuous linear functional with $\|\phi\| < \infty$ (guaranteed by definition of dual space). We assume $\mu$ is σ-finite, so there exist sets $E_n \in \mathcal{F}$ with $\mu(E_n) < \infty$ and $E_n \nearrow X$.

**Key observation:** For measurable sets $E$ with $\mu(E) < \infty$, the characteristic function $\mathbf{1}_E \in L^p(\mu)$ (since $\|\mathbf{1}_E\|_p = \mu(E)^{1/p} < \infty$). Thus $\phi(\mathbf{1}_E)$ is well-defined.

**Substep 1a: Define $g$ on measurable sets.**

Define a **signed measure** $\nu$ on $(X, \mathcal{F})$ by:
$$
\nu(E) := \phi(\mathbf{1}_E) \quad \text{for all } E \in \mathcal{F} \text{ with } \mu(E) < \infty \tag{3.21}
$$

**Claim:** $\nu$ extends to a signed measure on $\mathcal{F}$ (not just finite measure sets).

**Proof of claim:** By σ-finiteness, write $X = \bigcup_{n=1}^\infty E_n$ with $E_n \nearrow X$ and $\mu(E_n) < \infty$. For any $E \in \mathcal{F}$, define:
$$
\nu(E) := \lim_{n \to \infty} \nu(E \cap E_n) = \lim_{n \to \infty} \phi(\mathbf{1}_{E \cap E_n})
$$

This limit exists because $\mathbf{1}_{E \cap E_n} \to \mathbf{1}_E$ in $L^p$ norm (by Dominated Convergence: $|\mathbf{1}_{E \cap E_n}| \leq \mathbf{1}_{E}$, and if $E$ has infinite measure, we restrict to $E \cap E_n$ first). By continuity of $\phi$:
$$
\nu(E) = \lim_{n \to \infty} \phi(\mathbf{1}_{E \cap E_n}) = \phi\left(\lim_{n \to \infty} \mathbf{1}_{E \cap E_n}\right) = \phi(\mathbf{1}_E)
$$
(using that $\mathbf{1}_{E \cap E_n} \to \mathbf{1}_E$ in $L^p$). □

**Substep 1b: $\nu$ is absolutely continuous with respect to $\mu$.**

**Claim:** If $\mu(E) = 0$, then $\nu(E) = 0$ (i.e., $\nu \ll \mu$, absolute continuity).

**Proof of claim:** If $\mu(E) = 0$, then $\mathbf{1}_E = 0$ in $L^p$ (since functions differing on null sets are equivalent). Thus:
$$
\nu(E) = \phi(\mathbf{1}_E) = \phi(0) = 0 \quad \text{(by linearity of $\phi$)} \quad \square
$$

**Substep 1c: Apply Radon-Nikodym theorem (to be proven Day 4).**

We invoke the **Radon-Nikodym theorem** (which we will establish rigorously on Day 4; see Syllabus Week 3, Thursday). Since $\nu \ll \mu$ and both are σ-finite, there exists a unique $g \in L^1(\mu)$ such that:
$$
\nu(E) = \int_E g \, d\mu \quad \text{for all } E \in \mathcal{F} \tag{3.22}
$$

**Pedagogical note:** The proof of Radon-Nikodym uses Hilbert space projection methods that we develop in Week 14 (Hilbert Spaces) and Week 4, Day 4. For today's purposes, we accept this result and complete the proof of Riesz representation. The reader seeking complete logical independence should read Day 4 first, then return to this proof.

**Historical note:** Riesz (1909) proved this theorem before Radon-Nikodym was formalized (1930). The original proof used a direct construction for $L^p$ spaces without invoking general measure-theoretic machinery. See [@folland:real_analysis:1999, §6.3] for the historical development.

This $g$ is called the **Radon-Nikodym derivative** $d\nu/d\mu$.

**Key insight:** For simple functions $f = \sum_{i=1}^n a_i \mathbf{1}_{E_i}$ with disjoint $E_i$:
$$
\phi(f) = \sum_{i=1}^n a_i \phi(\mathbf{1}_{E_i}) = \sum_{i=1}^n a_i \nu(E_i) = \sum_{i=1}^n a_i \int_{E_i} g \, d\mu = \int_X f g \, d\mu \tag{3.23}
$$

Thus $\phi(f) = \int fg \, d\mu$ holds for all **simple functions** $f$.

---

**Step 2: Prove $g \in L^q$ with $\|g\|_q = \|\phi\|$.**

We have $g \in L^1$ from Radon-Nikodym, but we need $g \in L^q$. We will construct a specific test function in $L^p$ and use the definition of $\|\phi\|$.

**Substep 2a: Define test function on finite-measure sets.**

We will prove $g \in L^q$ by showing $\int_A |g|^q < \infty$ for all $A \in \mathcal{F}$ with $\mu(A) < \infty$, then taking $A \nearrow X$ (using σ-finiteness).

**Key idea:** We **assume** $\int_A |g|^q < \infty$ **for the sake of constructing the test function** $f_A$, then **derive** a bound $\int_A |g|^q \leq \|\phi\|^q$ that holds **independently of our assumption**. This bound then implies $\int_A |g|^q < \infty$ is actually true (not just assumed), completing the bootstrap argument.

**Technical justification:** Since $g \in L^1$ (from Radon-Nikodym), the set $\{A : \int_A |g|^q < \infty\}$ is nonempty (contains all null sets and singletons if $\mu$ is discrete). We show this collection is actually **all** finite-measure sets by deriving a uniform bound.

For any measurable set $A$ with $\mu(A) < \infty$, define:
$$
f_A = \text{sgn}(g) \cdot |g|^{q-1} \cdot \mathbf{1}_A \tag{3.24}
$$

where $\text{sgn}(g) = g/|g|$ if $g \neq 0$, and $\text{sgn}(g) = 0$ if $g = 0$.

**Claim:** If $\int_A |g|^q < \infty$, then $f_A \in L^p(\mu)$.

**Proof of claim:** We have $|f_A| = |g|^{q-1} \mathbf{1}_A$, so:
$$
\int_X |f_A|^p \, d\mu = \int_A |g|^{p(q-1)} \, d\mu
$$

Using the conjugate relation $1/p + 1/q = 1$, we get:
$$
p(q-1) = p \left(\frac{p}{p-1} - 1\right) = p \left(\frac{p - (p-1)}{p-1}\right) = p \cdot \frac{1}{p-1} = \frac{p}{p-1} = q
$$

(using $q = p/(p-1)$ from (3.17)). Thus:
$$
\int_X |f_A|^p \, d\mu = \int_A |g|^q \, d\mu < \infty \quad \text{(by assumption)}
$$

Therefore $f_A \in L^p$ with:
$$
\|f_A\|_p^p = \int_A |g|^q \, d\mu \tag{3.25}
$$
□

**Substep 2b: Compute $\phi(f_A)$ using representation.**

By (3.23) (representation on simple functions), extended by density to all $L^p$:
$$
\phi(f_A) = \int_X f_A g \, d\mu = \int_A \text{sgn}(g) |g|^{q-1} \cdot g \, d\mu = \int_A |g|^q \, d\mu \tag{3.26}
$$

(since $\text{sgn}(g) \cdot g = |g|$).

**Substep 2c: Use $\|\phi\|$ to bound $\int |g|^q$.**

**Case 1:** $\int_A |g|^q = 0$. Then $g = 0$ $\mu$-almost everywhere on $A$, so the bound (3.27) below holds trivially ($0 \leq \|\phi\|$).

**Case 2:** $\int_A |g|^q > 0$. Then $f_A \in L^p$ with $\|f_A\|_p = \left(\int_A |g|^q\right)^{1/p} > 0$.

By definition of operator norm (3.15):
$$
|\phi(f_A)| \leq \|\phi\| \cdot \|f_A\|_p
$$

Substituting (3.26) and (3.25):
$$
\int_A |g|^q \, d\mu = |\phi(f_A)| \leq \|\phi\| \cdot \left(\int_A |g|^q \, d\mu\right)^{1/p}
$$

Dividing both sides by $\left(\int_A |g|^q\right)^{1/p}$ (which is nonzero):
$$
\left(\int_A |g|^q \, d\mu\right)^{1 - 1/p} \leq \|\phi\|
$$

Since $1 - 1/p = (p-1)/p = 1/q$ (by conjugate relation $1/p + 1/q = 1$):
$$
\left(\int_A |g|^q \, d\mu\right)^{1/q} \leq \|\phi\| \tag{3.27}
$$

Thus (3.27) holds in both cases. ✓

**Substep 2d: Take supremum over $A$.**

Since (3.27) holds for all $A \in \mathcal{F}$ with $\mu(A) < \infty$, by σ-finiteness we can take $A = E_n \nearrow X$:
$$
\|g\|_q = \left(\int_X |g|^q \, d\mu\right)^{1/q} = \sup_n \left(\int_{E_n} |g|^q \, d\mu\right)^{1/q} \leq \|\phi\| < \infty
$$

Thus $g \in L^q(\mu)$ with $\|g\|_q \leq \|\phi\|$. ✓

**Substep 2e: Prove reverse inequality $\|\phi\| \leq \|g\|_q$.**

For any $f \in L^p$ with $\|f\|_p \leq 1$, by Hölder's inequality [THM-2.4]:
$$
|\phi(f)| = \left|\int f g \, d\mu\right| \leq \int |f| |g| \, d\mu \leq \|f\|_p \|g\|_q \leq \|g\|_q \tag{3.28}
$$

Taking supremum over all $f$ with $\|f\|_p \leq 1$:
$$
\|\phi\| = \sup_{\|f\|_p \leq 1} |\phi(f)| \leq \|g\|_q
$$

Combined with Substep 2d:
$$
\|\phi\| = \|g\|_q \tag{3.29}
$$

This is the **isometry** property. ✓

---

**Step 3: Show $\phi(f) = \int fg \, d\mu$ for all $f \in L^p$.**

We established (3.23) for simple functions. By density of simple functions in $L^p$ (standard fact; see [@folland:real_analysis:1999, Proposition 2.10]), for any $f \in L^p$ there exists a sequence of simple functions $f_n \to f$ in $L^p$ norm.

By continuity of $\phi$:
$$
\phi(f) = \phi\left(\lim_{n \to \infty} f_n\right) = \lim_{n \to \infty} \phi(f_n) = \lim_{n \to \infty} \int f_n g \, d\mu
$$

By Hölder's inequality, $\int |f_n - f| |g| \leq \|f_n - f\|_p \|g\|_q \to 0$, so:
$$
\lim_{n \to \infty} \int f_n g \, d\mu = \int f g \, d\mu
$$

(using Dominated Convergence or direct $\epsilon$-$\delta$ argument). Thus:
$$
\phi(f) = \int f g \, d\mu \quad \text{for all } f \in L^p \tag{3.30}
$$

✓

---

**Step 4: Uniqueness of $g$.**

Suppose $g_1, g_2 \in L^q$ both represent $\phi$, i.e., $\phi(f) = \int fg_1 = \int fg_2$ for all $f \in L^p$. Then:
$$
\int f(g_1 - g_2) \, d\mu = 0 \quad \text{for all } f \in L^p
$$

**Key test function:** Take $f = \text{sgn}(g_1 - g_2) |g_1 - g_2|^{q-1}$ (same construction as in Step 2). This $f \in L^p$ (by conjugate relation), and:
$$
\int f(g_1 - g_2) \, d\mu = \int |g_1 - g_2|^q \, d\mu = 0
$$

Since $|g_1 - g_2|^q \geq 0$ and its integral is zero, we have $|g_1 - g_2|^q = 0$ $\mu$-a.e., hence $g_1 = g_2$ $\mu$-a.e. □

This completes the proof of Theorem 3.9. □

---

**Remark 3.12 (Why $1 < p < \infty$ is Required).** The proof crucially uses that the test function $f_A = \text{sgn}(g) |g|^{q-1} \mathbf{1}_A$ lies in $L^p$, which requires $p(q-1) = q < \infty$ (i.e., $q$ is finite). This holds when $1 < p < \infty$, but:
- For $p = 1$ (so $q = \infty$), the test function $f_A = |g|^{\infty - 1}$ is not well-defined
- For $p = \infty$ (so $q = 1$), the test function would be $f_A = |g|^0 = 1$, which doesn't capture all of $L^\infty$

The cases $p = 1$ and $p = \infty$ require separate treatment (next section).

---

### **III. Special Cases and Counterexamples**

#### **A. Case $p = 2$: Self-Duality of $L^2$**

**Corollary 3.10 ($L^2$ is Self-Dual).** {#COR-3.10}
For any σ-finite measure space $(X, \mathcal{F}, \mu)$:
$$
(L^2(\mu))^* \cong L^2(\mu) \quad \text{(isometrically)} \tag{3.31}
$$

**Proof.** Apply Theorem 3.9 with $p = q = 2$ (since $1/2 + 1/2 = 1$). □

**Remark 3.13 (Inner Product Structure).** The pairing $\langle f, g \rangle = \int fg \, d\mu$ is actually an **inner product** on $L^2$ (symmetric, positive definite, bilinear). This makes $L^2$ a **Hilbert space** (complete inner product space; Week 14). The Riesz representation for $L^2$ is a special case of the **Riesz representation theorem for Hilbert spaces** [@brezis:functional_analysis:2011, Theorem 5.5], which states:

*Every continuous linear functional $\phi$ on a Hilbert space $H$ has the form $\phi(x) = \langle x, y \rangle$ for some unique $y \in H$ with $\|\phi\| = \|y\|$.*

This is more general than our result (applies to any Hilbert space, not just $L^2$), but the proof is essentially the same.

**RL Connection (Least-Squares TD):** LSTD [@bradtke:lstd:1996] solves the projected Bellman equation $V_\theta = \Pi T^\pi V_\theta$ by projecting the Bellman operator $T^\pi$ onto a linear subspace $\text{span}(\phi) \subset L^2(\mu)$, where $\mu$ is the state distribution under policy $\pi$.

The projection $\Pi: L^2(\mu) \to \text{span}(\phi)$ is defined via:
$$
\Pi V = \arg\min_{V_\theta \in \text{span}(\phi)} \|V - V_\theta\|_{L^2(\mu)}^2 = \arg\min \mathbb{E}_\mu[(V(s) - V_\theta(s))^2]
$$

By the **Projection Theorem** (Week 14), $\Pi$ exists, is unique, and satisfies $\langle V - \Pi V, V_\theta \rangle_\mu = 0$ for all $V_\theta \in \text{span}(\phi)$ (orthogonality).

**Key theoretical guarantee:** If the projected Bellman operator $\Pi T^\pi: \text{span}(\phi) \to \text{span}(\phi)$ is a $\gamma$-contraction (holds when features are well-conditioned), then LSTD converges to the unique fixed point $V_\theta^* = \Pi T^\pi V_\theta^*$ [@tsitsiklis:analysis_td:1997].

**Practical limitations:**
1. **Approximation error:** $\|V^\pi - V_\theta^*\|_\mu \geq \|V^\pi - \Pi V^\pi\|_\mu$ (bounded below by representational capacity of features)
2. **Computational cost:** $O(d^3)$ matrix inversion (intractable for $d > 10^4$); practitioners use **incremental TD($\lambda$)** instead ($O(d)$ per sample)
3. **Chattering:** If $\Pi T^\pi$ is not a contraction, LSTD may not converge (see [@baird:residual_algorithms:1995] for counterexamples with linear function approximation)

**Modern deep RL:** Neural network function approximators break the $L^2$ projection framework (features $\phi_\theta$ are learned, not fixed). Convergence guarantees do not apply; empirical success relies on clever exploration, large replay buffers, and target networks [@mnih:dqn:2015].

---

#### **B. Case $p = 1$: $(L^1)^* \cong L^\infty$**

**Theorem 3.11 (Duality of $L^1$ and $L^\infty$).** {#THM-3.11}
Let $(X, \mathcal{F}, \mu)$ be a **σ-finite** measure space. Then:
$$
(L^1(\mu))^* \cong L^\infty(\mu) \quad \text{(isometrically)} \tag{3.32}
$$

More precisely, every $\phi \in (L^1)^*$ has the form:
$$
\phi(f) = \int_X f g \, d\mu \quad \text{for all } f \in L^1
$$
for some unique $g \in L^\infty$ with $\|\phi\| = \|g\|_\infty$.

**Proof sketch:** The proof is similar to Theorem 3.9 but requires σ-finiteness more crucially (without it, the dual of $L^1$ can be strictly larger than $L^\infty$; see Remark 3.14 below). The construction uses Radon-Nikodym to define $g$, then shows $g$ is essentially bounded by using test functions of the form $f = \mathbf{1}_A$ for sets $A$ with $\mu(A) < \infty$. See [@folland:real_analysis:1999, Theorem 6.15] or [@brezis:functional_analysis:2011, Theorem 4.11] for details. □

**Remark 3.14 (σ-Finiteness is Crucial).** Without σ-finiteness, $(L^1)^* \supsetneq L^\infty$ (strict containment).

**Counterexample:** Let $X = \mathbb{R}$ with **counting measure** $\mu(E) = |E|$ (cardinality). Then:
- $L^1(\mu) = \ell^1 = \{(x_n) : \sum |x_n| < \infty\}$ (absolutely summable sequences)
- $L^\infty(\mu) = \ell^\infty = \{(x_n) : \sup_n |x_n| < \infty\}$ (bounded sequences)

The dual $(\ell^1)^* \cong \ell^\infty$ **only on countable spaces**. On uncountable $X$ with counting measure, $(L^1)^*$ includes "finitely additive measures" that are not σ-additive, which lie outside $L^\infty$ (see [@folland:real_analysis:1999, Example 6.16] for details).

**RL Implication:** In RL, state spaces are typically **finite** (discrete MDPs) or have **probability measures** (continuous MDPs with $\mu(\mathcal{S}) = 1 < \infty$), both of which are σ-finite. Thus $(L^1)^* \cong L^\infty$ holds in all practical RL settings.

---

#### **C. Case $p = \infty$: Duality Fails for $L^\infty$**

**Theorem 3.12 ($(L^\infty)^*$ is Larger than $L^1$).** {#THM-3.12}
For any non-atomic measure space (e.g., Lebesgue measure on $\mathbb{R}$):
$$
(L^\infty(\mu))^* \supsetneq L^1(\mu) \quad \text{(strict containment)} \tag{3.33}
$$

**Proof sketch:**

**(Step 1: Embedding $L^1 \to (L^\infty)^*$):** Every $g \in L^1$ defines a functional $\phi_g(f) = \int fg \, d\mu$ on $L^\infty$. This map $g \mapsto \phi_g$ is an **isometric embedding** $L^1 \hookrightarrow (L^\infty)^*$ (injective, norm-preserving), since:
$$
|\phi_g(f)| = \left|\int fg \, d\mu\right| \leq \int |f| |g| \, d\mu \leq \|f\|_\infty \|g\|_1
$$
with equality achieved by $f = \text{sgn}(g)$. Thus $\|\phi_g\| = \|g\|_1$.

**(Step 2: $(L^\infty)^*$ is strictly larger):** For **non-atomic** measure spaces (e.g., Lebesgue measure on $[0,1]$), $(L^\infty)^*$ contains functionals **not** of the form $\phi_g$ for any $g \in L^1$.

**Explicit example (Banach limit):** On $\ell^\infty(\mathbb{N})$ (bounded sequences), the **Banach limit** $\text{LIM}$ is a functional satisfying:
1. $\text{LIM}(x) \geq 0$ if $x_n \geq 0$ for all $n$
2. $\text{LIM}(x_1, x_2, x_3, \ldots) = \text{LIM}(x_2, x_3, x_4, \ldots)$ (shift-invariance)
3. $\text{LIM}$ extends the ordinary limit (if $\lim_{n \to \infty} x_n$ exists, then $\text{LIM}(x) = \lim x_n$)

Such a functional exists by Hahn-Banach (Week 12) but is **not** given by any $g \in \ell^1$. Indeed, if $\text{LIM}(x) = \sum_{n=1}^\infty g_n x_n$ for some $g \in \ell^1$, then property (2) would imply $g_1 = g_2 = g_3 = \cdots$ (constant), but then $\sum g_n = \infty$ (contradicting $g \in \ell^1$).

**General case:** For $L^\infty(\mu)$ with non-atomic $\mu$, analogous "purely finitely additive" functionals exist (see [@folland:real_analysis:1999, §6.4] or [@yosida:functional_analysis:1980, Chapter IV.5]). These are sometimes called "singular functionals" (orthogonal to $L^1$ in a weak sense).

**Conclusion:** $(L^\infty)^* \supsetneq L^1$ strictly. □

**Remark 3.15 (Why This Matters for RL).** In RL, we primarily work with:
- **$L^\infty$ as domain for value functions** (bounded rewards, bounded values)
- **$L^1$ or probability measures as domains for state distributions**

The fact that $(L^\infty)^* \supsetneq L^1$ means that **not all linear functionals on value functions correspond to state distributions**. This is actually not a problem—the functionals arising in RL (e.g., $V \mapsto \mathbb{E}_\mu[V(s)]$) **do** correspond to measures, which are a subset of $(L^\infty)^*$.

**Practical note:** For **finite state spaces**, $L^\infty(\mathcal{S}) = \mathbb{R}^{|\mathcal{S}|}$ (all functions are bounded), and $(L^\infty)^* = L^1 = \mathbb{R}^{|\mathcal{S}|}$ (canonical duality). The failure of duality only matters for **infinite-dimensional** $L^\infty$ spaces.

---

### **IV. Corollaries and Applications**

**Corollary 3.13 (Hölder's Inequality is Sharp).** {#COR-3.13}
For $1 \leq p \leq \infty$ and conjugate $q$, Hölder's inequality [THM-2.4] states:
$$
\left|\int fg \, d\mu\right| \leq \|f\|_p \|g\|_q
$$

The constant $1$ is **sharp** (best possible): for any $f \in L^p$ with $f \neq 0$, there exists $g \in L^q$ with $\|g\|_q = 1$ such that $\int fg = \|f\|_p$.

**Proof.** Take $g = \text{sgn}(f) |f|^{p-1} / \|f\|_p^{p-1}$ (normalized version of the test function from Theorem 3.9 proof). Then $\|g\|_q = 1$ (by conjugate relation) and:
$$
\int fg \, d\mu = \frac{1}{\|f\|_p^{p-1}} \int |f|^p \, d\mu = \frac{\|f\|_p^p}{\|f\|_p^{p-1}} = \|f\|_p \quad \square
$$

---

**Corollary 3.14 (Reflexivity of $L^p$ for $1 < p < \infty$).** {#COR-3.14}
For $1 < p < \infty$ and σ-finite $\mu$, the space $L^p(\mu)$ is **reflexive**, meaning:
$$
(L^p)^{**} \cong L^p \quad \text{(canonically)} \tag{3.34}
$$

where $(L^p)^{**} := ((L^p)^*)^*$ is the **double dual** (dual of the dual).

**Proof.** By Theorem 3.9, $(L^p)^* \cong L^q$ where $1/p + 1/q = 1$. Applying Theorem 3.9 again to $L^q$:
$$
(L^q)^* \cong L^p \quad \text{(since $1/q + 1/p = 1$)}
$$

Thus:
$$
(L^p)^{**} = ((L^p)^*)^* \cong (L^q)^* \cong L^p \quad \square
$$

**Remark 3.16 (Non-Reflexivity of $L^1$ and $L^\infty$).** The spaces $L^1$ and $L^\infty$ are **not reflexive**:
- $(L^1)^{**} \cong (L^\infty)^* \supsetneq L^1$ (strictly larger)
- $(L^\infty)^{**} \supsetneq (L^\infty)^*$ (even larger)

Reflexivity fails at the "endpoints" $p = 1, \infty$. This is why $L^2$ (the "middle" case) is particularly nice—it's reflexive, self-dual, and has an inner product structure.

---

### **V. Mathematical Insight and RL Connections**

**Mathematical Insight:**

The Riesz representation theorem reveals a **profound duality** between $L^p$ and $L^q$:

1. **Geometric interpretation:** Every continuous linear functional on $L^p$ is given by "integration against an $L^q$ function." This is analogous to the finite-dimensional fact that every linear functional on $\mathbb{R}^n$ is "dot product with a vector."

2. **Completeness + Duality = Reflexivity:** For $1 < p < \infty$, combining Riesz-Fischer [THM-3.4] (completeness) with Riesz Representation [THM-3.9] (duality) yields reflexivity: $(L^p)^{**} \cong L^p$. This means $L^p$ "sees itself" when looking at its double dual—there's no "loss of information" in taking duals.

3. **$L^2$ is special:** It's the unique $L^p$ space that is:
   - Complete (Banach)
   - Self-dual ($(L^2)^* \cong L^2$)
   - Has inner product structure (Hilbert space)

   This trio of properties makes $L^2$ the natural home for **least-squares methods** in RL.

**Proof Strategy Recap:**

1. Use Radon-Nikodym to construct $g$ from $\phi$ (via signed measure $\nu(E) = \phi(\mathbf{1}_E)$)
2. Show $g \in L^q$ by testing against $f = \text{sgn}(g) |g|^{q-1}$ (clever use of conjugate exponents)
3. Verify $\|\phi\| = \|g\|_q$ (isometry) via Hölder
4. Uniqueness follows from test function argument

**Key tools:** Hölder's inequality [THM-2.4], Radon-Nikodym (Day 4 preview), density of simple functions in $L^p$

**RL Connection:**

**1. Value Functions and State Distributions are Dual**

In an MDP $(\mathcal{S}, \mathcal{A}, P, r, \gamma)$, the **value function** $V^\pi: \mathcal{S} \to \mathbb{R}$ and the **state visitation distribution** $\mu_\pi$ under policy $\pi$ are related by:
$$
J(\pi) = \mathbb{E}_{\mu_\pi}[V^\pi(s)] = \int_\mathcal{S} V^\pi(s) \, \mu_\pi(ds)
$$

This is **precisely the duality pairing** $\langle V^\pi, \mu_\pi \rangle$ between:
- $V^\pi \in L^2(\mathcal{S}, \nu)$ (value function; lives in function space)
- $\mu_\pi$ (state distribution; lives in dual space of measures)

**Why $L^2$ specifically?** Because:
- $L^2$ has an **inner product** $\langle V, W \rangle_\nu = \mathbb{E}_\nu[V(s)W(s)]$ (weighted by reference measure $\nu$)
- State distributions $\mu_\pi$ are **probability measures**, which induce functionals $\phi_\mu(V) = \mathbb{E}_\mu[V(s)]$
- By Riesz representation, every such functional corresponds to a unique "density" $d\mu_\pi/d\nu \in L^2(\nu)$ (if $\mu_\pi \ll \nu$; see Radon-Nikodym on Day 4)

**Application to Policy Gradients (Week 37):** The **policy gradient theorem** [@sutton:policy_gradient:2000] states that for a parameterized policy $\pi_\theta$ in an MDP with discount factor $\gamma \in [0,1)$, the gradient of the **expected discounted return** $J(\theta) = \mathbb{E}_{\pi_\theta}[\sum_{t=0}^\infty \gamma^t r_t]$ is:
$$
\nabla_\theta J(\theta) = \mathbb{E}_{d_\pi}\left[\mathbb{E}_{a \sim \pi_\theta(\cdot|s)}[\nabla_\theta \log \pi_\theta(a|s) Q^\pi(s,a)]\right]
$$
where $d_\pi(s)$ is the **discounted state occupancy measure**:
$$
d_\pi(s) = (1 - \gamma) \sum_{t=0}^\infty \gamma^t P(s_t = s | s_0 \sim \rho_0, \pi_\theta)
$$
and $Q^\pi(s,a) = \mathbb{E}_\pi[\sum_{t=0}^\infty \gamma^t r_t | s_0 = s, a_0 = a]$ is the action-value function.

**Key assumptions:**
- **On-policy sampling:** The gradient formula assumes samples $(s,a)$ are drawn from $d_\pi$ (the distribution induced by $\pi_\theta$)
- **Differentiable policy:** $\pi_\theta(a|s)$ is differentiable in $\theta$ for all $(s,a)$
- **Finite expected return:** $\mathbb{E}[\sum \gamma^t r_t] < \infty$ (holds if rewards are bounded and $\gamma < 1$)

**Practical implementation:** Actor-critic methods [@konda:actor_critic:2000] approximate $Q^\pi$ with a learned critic $Q_w(s,a)$, yielding the **stochastic policy gradient**:
$$
\nabla_\theta J(\theta) \approx \frac{1}{N} \sum_{i=1}^N \nabla_\theta \log \pi_\theta(a_i|s_i) Q_w(s_i, a_i)
$$
where $(s_i, a_i) \sim d_\pi$ (on-policy samples). For off-policy data, importance sampling corrections are required (Week 36-37).

**2. Linear Function Approximation as Dual Space**

In **linear value function approximation**, we parameterize:
$$
V_\theta(s) = \theta^\top \phi(s) = \sum_{i=1}^d \theta_i \phi_i(s)
$$

where $\phi: \mathcal{S} \to \mathbb{R}^d$ are feature maps. The value function space is:
$$
\mathcal{V} = \{\theta^\top \phi : \theta \in \mathbb{R}^d\} = \text{span}(\phi_1, \ldots, \phi_d) \subseteq L^2(\mathcal{S}, \mu)
$$

**Duality perspective:** Every $V_\theta \in \mathcal{V}$ defines a **linear functional** on the dual space:
$$
\psi_\theta: g \mapsto \mathbb{E}_\mu[V_\theta(s) g(s)] = \int \theta^\top \phi(s) \cdot g(s) \, \mu(ds)
$$

By Riesz representation, this functional **is** the element $V_\theta \in L^2$.

**Least-Squares TD (LSTD):** Given samples $(s_i, r_i, s_i')$ from policy $\pi$, **LSTD (Least-Squares Temporal Difference)** [@bradtke:lstd:1996] solves the **projected Bellman equation**:
$$
V_\theta = \Pi T^\pi V_\theta
$$
where $\Pi: L^2(\mu) \to \text{span}(\phi_1, \ldots, \phi_d)$ is the **orthogonal projection** onto the linear subspace, and $T^\pi$ is the Bellman operator:
$$
(T^\pi V)(s) = r(s) + \gamma \mathbb{E}_{s' \sim P(\cdot|s, \pi(s))}[V(s')]
$$
In matrix form, the fixed-point equation becomes:
$$
\mathbb{E}_\mu[\phi(s)(\phi(s) - \gamma\phi(s'))^\top]\theta = \mathbb{E}_\mu[\phi(s)r(s)]
$$
LSTD solves this via sample averages (requires $O(d^3)$ matrix inversion, where $d$ is feature dimension).

**Key limitation:** The solution $V_\theta$ is the **best linear approximation** to $V^\pi$ in the $L^2(\mu)$ norm, **not** the true value function $V^\pi$ (unless $V^\pi \in \text{span}(\phi)$). The approximation error $\|V^\pi - V_\theta\|_\mu$ depends on the **expressiveness of features** $\phi$ (see [@tsitsiklis:analysis_td:1997] for error bounds).

**3. Importance Sampling and Radon-Nikodym Derivatives**

In **off-policy RL**, we collect data under **behavior policy** $\mu$ but want to evaluate **target policy** $\pi$. The correction is:
$$
\mathbb{E}_\pi[V(s)] = \mathbb{E}_\mu\left[\frac{d\pi}{d\mu}(s) V(s)\right]
$$

where $d\pi/d\mu$ is the **Radon-Nikodym derivative** (density of $\pi$ with respect to $\mu$). This is **precisely** a change-of-measure formula using duality:
- $\mu$ and $\pi$ are measures on $\mathcal{S}$
- $V \in L^2(\mathcal{S}, \mu)$ is the value function
- The ratio $d\pi/d\mu$ converts between the two measures

**Per-decision importance sampling ratio:**
$$
\rho_t = \frac{\pi(a_t|s_t)}{\mu(a_t|s_t)} = \frac{d\pi(a|s)}{d\mu(a|s)}
$$

This is a Radon-Nikodym derivative **on the action space** $\mathcal{A}$ (conditional on state $s$). For trajectories $(s_0, a_0, \ldots, s_T, a_T)$, the cumulative importance weight is:
$$
\rho_{0:T-1} = \prod_{t=0}^{T-1} \frac{\pi(a_t|s_t)}{\mu(a_t|s_t)}
$$

**High-variance problem:** For trajectories of length $T$, the cumulative importance weight is:
$$
\rho_{0:T-1} = \prod_{t=0}^{T-1} \frac{\pi(a_t|s_t)}{\mu(a_t|s_t)}
$$
If each $\rho_t$ has variance $\sigma^2$ (independent), the product has variance:
$$
\text{Var}[\rho_{0:T-1}] \approx (\sigma^2 + 1)^T - 1 \quad \text{(exponential in $T$)}
$$
(assuming $\mathbb{E}[\rho_t] = 1$ and independence). For $T = 100$ and $\sigma = 2$, this yields $\text{Var} \approx 5^{100} \approx 10^{70}$ (astronomical!).

**Variance reduction techniques:**

1. **Per-decision importance sampling** [@precup:per_decision_is:2000]: Use $\rho_t$ only for step $t$, not cumulative product:
   $$
   \mathbb{E}_\pi[r_t] \approx \frac{1}{N} \sum_{i=1}^N \rho_t^{(i)} r_t^{(i)} \quad \text{(variance } O(T\sigma^2) \text{ instead of } O(\sigma^{2T}) \text{)}
   $$

2. **Weighted importance sampling** [@precup:eligibility_traces:2000]: Normalize by sum of weights:
   $$
   \hat{\mathbb{E}}_\pi[r] = \frac{\sum_i \rho_i r_i}{\sum_i \rho_i} \quad \text{(biased but lower variance)}
   $$

3. **Clipping (PPO-style)** [@schulman:ppo:2017]: Clip importance weights to $[1-\epsilon, 1+\epsilon]$:
   $$
   L^{\text{CLIP}}(\theta) = \mathbb{E}_{\mu}\left[\min(\rho_t A_t, \text{clip}(\rho_t, 1-\epsilon, 1+\epsilon) A_t)\right]
   $$
   (ensures $\rho_t \approx 1$, reducing variance; $\epsilon \approx 0.2$ in practice)

4. **V-trace (IMPALA)** [@espeholt:impala:2018]: Truncated importance weights with fixed thresholds:
   $$
   \bar{\rho}_t = \min(\rho_t, \bar{c}), \quad \bar{\rho}_t = \min(\rho_t, \bar{\rho}) \quad (\bar{c} = 1, \bar{\rho} = 1 \text{ typical})
   $$
   (off-policy actor-critic with bounded importance weights; convergent under mild assumptions)

**Note on TRPO:** TRPO [@schulman:trpo:2015] is **on-policy** (uses natural policy gradient, not importance sampling). The KL constraint $D_{\text{KL}}(\pi_{\theta'} \| \pi_\theta) \leq \delta$ ensures $\rho(s,a) = \pi_{\theta'}(a|s)/\pi_\theta(a|s) \approx 1$ (small policy updates), indirectly controlling importance weight variance.

**Connection to Radon-Nikodym (Day 4):** On Thursday, we prove the Radon-Nikodym theorem, which characterizes when $d\mu/d\nu$ exists (when $\mu \ll \nu$, absolute continuity). This formalizes the existence of importance sampling ratios in RL.

---

**Contrast with Non-Dual Spaces:**

Spaces that **don't** have nice duality include:
- **$L^p$ for $p \notin [1, \infty]$:** Quasi-norms (triangle inequality fails), no duality theory
- **$C([0,1])$ with $L^1$ norm:** Incomplete, $(C([0,1]))^* \supsetneq L^\infty([0,1])$ (extra functionals from Hahn-Banach)
- **$L^\infty$ in general:** $(L^\infty)^* \supsetneq L^1$ (purely finitely additive functionals)

The $L^p$ spaces for $1 < p < \infty$ are the "sweet spot"—complete, reflexive, nice duality.

---

**Looking Ahead:**

- **Day 3 (Wednesday):** We continue duality discussion, focusing on special cases and counterexamples. We'll also introduce the concept of **weak convergence** in dual spaces.

- **Day 4 (Thursday, Extended Proof Session):** **Radon-Nikodym theorem**—when does a measure have a **density** with respect to another? (i.e., when does $d\mu/d\nu$ exist?). This is the foundation of importance sampling in RL. We will see that LSTD in detail requires understanding this material (Week 35 provides full implementation details).

- **Day 5 (Friday, Synthesis):** Weekly reflection on $L^p$ completeness and duality, coding exercises on importance sampling and least-squares projection.

- **Week 14 (Hilbert Spaces):** We'll see that $L^2$ is not just a Banach space but a **Hilbert space** (complete inner product space). The **projection theorem** (existence of orthogonal projections onto closed subspaces) is the foundation of least-squares TD.

Today's theorem—Riesz Representation for $(L^p)^*$—establishes the **dual space structure** that underlies all linear methods in RL. Combined with Day 1's completeness (Riesz-Fischer), we now have a complete picture of $L^p$ as a Banach space with explicit dual.

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_2_exercises_revised_math+rl]]**

**Anchor Exercise Preview:**
1. **Verify $(L^2)^* \cong L^2$:** Show that the Riesz representation for $p = 2$ yields the inner product pairing $\phi(f) = \langle f, g \rangle = \int fg \, d\mu$.

2. **Compute conjugate exponents:** For each $p \in \{1, 4/3, 3/2, 2, 3, 4, 6, \infty\}$, find the conjugate $q$ satisfying $1/p + 1/q = 1$. Verify that $q = p/(p-1)$ for $1 < p < \infty$.

3. **RL Application (Bellman Operator as Functional):** Let $\mathcal{S}$ be a finite state space with $|\mathcal{S}| = n$. For a given policy $\pi$, define the **reward functional** $\phi_r: \mathbb{R}^n \to \mathbb{R}$ by $\phi_r(V) = \sum_{s \in \mathcal{S}} r_s V_s$ where $r_s$ is the reward at state $s$. Show:
   - $\phi_r \in (\ell^\infty)^*$ (dual of $L^\infty$)
   - $\phi_r$ is represented by integration against $r \in \ell^1$: $\phi_r(V) = \sum_s r_s V_s$
   - If $\|r\|_1 = 1$, then $\|\phi_r\| = 1$ (operator norm)

4. **Reflexivity of $L^p$:** Prove that $L^p$ is reflexive for $1 < p < \infty$ by showing $(L^p)^{**} \cong L^p$ using Theorem 3.9 twice.

---

**Reflection Questions:**

1. **Why does the proof require $1 < p < \infty$? What goes wrong for $p = 1$ or $p = \infty$?**
   *Hint:* The test function $f = \text{sgn}(g) |g|^{q-1}$ requires $q < \infty$ (so $p > 1$). For $p = 1$ ($q = \infty$), this function is not well-defined. For $p = \infty$ ($q = 1$), the construction doesn't capture all of $(L^\infty)^*$.

2. **What is the relationship between Hölder's inequality [THM-2.4] and Riesz representation [THM-3.9]?**
   *Hint:* Hölder provides the "easy" inequality $\|\phi\| \leq \|g\|_q$ (equation 3.28). The "hard" direction $\|g\|_q \leq \|\phi\|$ uses the test function construction in Step 2, which "saturates" Hölder's inequality (achieves equality).

3. **How does duality explain the "state-value duality" in RL?**
   *Hint:* Value functions $V \in L^2(\mathcal{S})$ and state distributions $\mu$ (measures on $\mathcal{S}$) are dual via the pairing $\langle V, \mu \rangle = \mathbb{E}_\mu[V(s)]$. By Riesz representation, every measure defines a functional on $L^2$, and vice versa (if $\mu \ll \nu$, the reference measure).

---

**Daily Study Note:**

**What I learned today:**
- **Dual space $(L^p)^*$**: continuous linear functionals $\phi: L^p \to \mathbb{R}$ with $|\phi(f)| \leq \|\phi\| \|f\|_p$
- **Riesz Representation [THM-3.9]**: $(L^p)^* \cong L^q$ for conjugate exponents $1/p + 1/q = 1$ (when $1 < p < \infty$)
- **Isometric isomorphism**: $\|\phi\| = \|g\|_q$ where $\phi(f) = \int fg \, d\mu$
- **Proof strategy**: Radon-Nikodym to construct $g$ → test against $f = \text{sgn}(g) |g|^{q-1}$ to show $g \in L^q$ → density argument for representation
- **Special cases**: $(L^2)^* \cong L^2$ (self-dual), $(L^1)^* \cong L^\infty$ (on σ-finite spaces), $(L^\infty)^* \supsetneq L^1$ (duality fails)

**Connection to previous material:**
- Builds on Riesz-Fischer [THM-3.4] (completeness) from Day 1
- Uses Hölder's inequality [THM-2.4] from Week 2, Day 4 crucially
- Previews Radon-Nikodym theorem (Day 4) for constructing $g$ from $\phi$

**Looking forward:**
- Day 3: Weak convergence, dual space topology
- Day 4: Radon-Nikodym theorem—densities $d\mu/d\nu$ for importance sampling
- Week 14: Hilbert spaces—$L^2$ inner product, projection theorem for LSTD

**RL connections identified:**
- Value functions and state distributions are dual (pairing $\langle V, \mu \rangle = \mathbb{E}_\mu[V]$)
- Linear function approximation lives in $L^2$, dual space is also $L^2$ (self-duality)
- Importance sampling ratios $\pi/\mu$ are Radon-Nikodym derivatives (Day 4 preview)
- Least-squares TD uses $L^2$ projection, which requires Hilbert space structure (Week 14)
- Policy gradients integrate against state distributions (duality pairing with value functions)
- Natural policy gradients use Fisher metric (L^2 inner product on score functions)

**Time spent:** 90-120 minutes (within acceptable range for rigorous duality theory on Tuesday)

---

**End of Day 2**
### Agenda:

##### 📘 Day 2 — Week 3: Duality of $L^p$ Spaces—The Riesz Representation Theorem

**Total time: ~90 minutes (Tuesday)**
**Actual time estimate: 90-120 minutes for rigorous duality theory**

---

#### **⏱️ Segment 1 (40 min) — Reading**

**Topic:** _Duality of $L^p$ spaces: $(L^p)^* \cong L^q$ for conjugate exponents_

- Read from **Folland §6.3-6.4** [@folland:real_analysis:1999, §6.3-6.4] ($L^p$ duality) or **Brezis Ch 4** [@brezis:functional_analysis:2011, Ch 4] (Functional Analysis)
- Focus on:
    - **Dual space $(L^p)^*$**: continuous linear functionals $\phi: L^p \to \mathbb{R}$ with $|\phi(f)| \leq C\|f\|_p$
    - **Conjugate exponents**: $1/p + 1/q = 1$ (e.g., $(p=2, q=2)$, $(p=1, q=\infty)$, $(p=4, q=4/3)$)
    - **Riesz Representation Theorem**: Every $\phi \in (L^p)^*$ has the form $\phi(f) = \int fg \, d\mu$ for some unique $g \in L^q$
    - **Isometric isomorphism**: $(L^p)^* \cong L^q$ with $\|\phi\| = \|g\|_q$
    - **RL significance**: Linear value function approximation lives in $(L^2)^*$; state distributions are dual to value functions

---

#### **⏱️ Segment 2 (40 min) — Proof and Exercises**

**Primary Task:**
1. **State the Riesz Representation Theorem** for $(L^p)^*$ when $1 < p < \infty$
2. **Understand the proof strategy**:
   - Step 1: Define candidate $g \in L^q$ from $\phi$ (construction on simple functions, extend by density)
   - Step 2: Prove $g \in L^q$ with $\|g\|_q = \|\phi\|$
   - Step 3: Show $\phi(f) = \int fg \, d\mu$ for all $f \in L^p$
   - Step 4: Prove uniqueness of $g$ (if $\phi(f) = \int fg_1 = \int fg_2$ for all $f$, then $g_1 = g_2$ a.e.)
3. **Special cases**:
   - $(L^2)^* \cong L^2$ (self-dual)
   - $(L^1)^* \cong L^\infty$ on $\sigma$-finite spaces
   - $(L^\infty)^* \supsetneq L^1$ in general (duality fails for $L^\infty$)

**Guidance:**
- The proof uses **Hölder's inequality** [THM-2.4] crucially: $\int |fg| \leq \|f\|_p \|g\|_q$
- For $1 < p < \infty$, the proof constructs $g$ by defining $\phi$ on characteristic functions and extending by linearity
- The $p = 1$ case requires $\sigma$-finiteness; without it, $(L^1)^*$ can be strictly larger than $L^\infty$

---

#### **💡 Conceptual Bridge to RL**

**Why duality matters in RL:** In MDPs, the **state visitation distribution** $\mu_\pi$ under policy $\pi$ and the **value function** $V^\pi: \mathcal{S} \to \mathbb{R}$ are related via the performance objective:
$$
J(\pi) = \mathbb{E}_{\mu_\pi}[V^\pi(s)] = \int_\mathcal{S} V^\pi(s) \, \mu_\pi(ds)
$$
This is **precisely the duality pairing** $\langle V^\pi, \mu_\pi \rangle$ between:
- $V^\pi \in L^2(\mathcal{S}, \nu)$ (value function; lives in function space)
- $\mu_\pi$ (state visitation distribution; induces a functional $\phi_\mu(V) = \mathbb{E}_\mu[V(s)]$ in $(L^2)^*$)

By Riesz representation [THM-3.9], if $\mu_\pi \ll \nu$ (absolute continuity with respect to reference measure $\nu$), then $\phi_{\mu_\pi}$ corresponds to the density $d\mu_\pi/d\nu \in L^2(\nu)$ via:
$$
\mathbb{E}_{\mu_\pi}[V(s)] = \int_\mathcal{S} V(s) \frac{d\mu_\pi}{d\nu}(s) \, d\nu(s)
$$
This formalizes the state-value duality used in policy gradient derivations (Week 37).

**Connection to Day 1:** Yesterday we proved $L^p$ is complete (Riesz-Fischer [THM-3.4]). Today we study its **dual space**—the continuous linear functionals. The combination "complete + duality" makes $L^p$ a **reflexive Banach space** for $1 < p < \infty$ (i.e., $(L^p)^{**} \cong L^p$).

**Preview for Day 3:** Tomorrow we continue duality for special cases ($L^1$ and $L^\infty$) and discuss counterexamples where duality fails. Thursday we move to **Radon-Nikodym theorem** (densities $d\mu/d\nu$), the foundation of importance sampling.

---

## **Chapter 3.2: Duality of $L^p$ Spaces**

### **Motivation: What is the Dual Space?**

Recall from Day 1 that $L^p(\mu)$ is a **Banach space** (complete normed vector space) for $1 \leq p \leq \infty$ by Riesz-Fischer [THM-3.4]. Today we study the **dual space** $(L^p)^*$, which consists of all **continuous linear functionals** on $L^p$.

**Definition 3.8 (Dual Space).** {#DEF-3.8}
Let $X$ be a normed vector space. The **dual space** $X^*$ is the set of all **bounded linear functionals** $\phi: X \to \mathbb{R}$ (or $\mathbb{C}$ for complex spaces), i.e., linear maps satisfying:
$$
\exists C \geq 0 : |\phi(f)| \leq C\|f\| \quad \text{for all } f \in X \tag{3.14}
$$

Equipped with the **operator norm**:
$$
\|\phi\| = \sup_{\|f\| \leq 1} |\phi(f)| = \sup_{f \neq 0} \frac{|\phi(f)|}{\|f\|} \tag{3.15}
$$
$X^*$ is itself a Banach space (even if $X$ is not complete, $X^*$ always is; see [@brezis:functional_analysis:2011, Theorem 1.10]).

**Remark 3.8 (Continuity vs. Boundedness).** For **linear** functionals, **continuity** and **boundedness** are equivalent (see [@folland:real_analysis:1999, Proposition 5.3]). Thus "$\phi \in X^*$" means "$\phi$ is a continuous linear functional." For nonlinear maps, boundedness does not imply continuity, so the distinction matters. Throughout this chapter, "functional" always means "linear functional."

---

#### **A. Examples of Dual Spaces**

**Example 3.1 (Finite Dimensions).** For $X = \mathbb{R}^n$ with any norm, the dual space $X^*$ is isomorphic to $\mathbb{R}^n$ itself. Every linear functional $\phi: \mathbb{R}^n \to \mathbb{R}$ has the form $\phi(x) = a^\top x$ for some $a \in \mathbb{R}^n$. Thus $(\mathbb{R}^n)^* \cong \mathbb{R}^n$ (canonical isomorphism).

**Example 3.2 ($\ell^p$ Spaces).** For the sequence space $\ell^p = \{(x_n) : \sum |x_n|^p < \infty\}$ with $1 \leq p < \infty$, the dual is:
$$
(\ell^p)^* \cong \ell^q \quad \text{where } 1/p + 1/q = 1
$$

Every $\phi \in (\ell^p)^*$ has the form $\phi(x) = \sum_{n=1}^\infty a_n x_n$ for some $a = (a_n) \in \ell^q$, with $\|\phi\| = \|a\|_q$ (by Hölder's inequality).

**Example 3.3 ($C([0,1])$ with sup norm).** The dual of $(C([0,1]), \|\cdot\|_\infty)$ is the space of **signed Radon measures** on $[0,1]$:
$$
(C([0,1]))^* \cong \mathcal{M}([0,1]) \quad \text{(Riesz-Markov representation theorem)}
$$

Every $\phi \in (C([0,1]))^*$ has the form $\phi(f) = \int_{[0,1]} f \, d\mu$ for some signed Borel measure $\mu$.

**Example 3.4 ($L^p$ Spaces—Today's Goal).** For $1 \leq p < \infty$ and $\sigma$-finite $(X, \mathcal{F}, \mu)$:
$$
(L^p(\mu))^* \cong L^q(\mu) \quad \text{where } 1/p + 1/q = 1
$$

This is the **Riesz Representation Theorem** for $L^p$ spaces (Theorem 3.9 below).

---

#### **B. Conjugate Exponents**

**Definition 3.9 (Conjugate Exponents).** {#DEF-3.9}
Two numbers $1 \leq p, q \leq \infty$ are **conjugate** (or **dual**, or **Hölder conjugate**) if:
$$
\frac{1}{p} + \frac{1}{q} = 1 \tag{3.16}
$$

**Conventions:**
- If $p = 1$, then $q = \infty$ (since $1/1 + 1/\infty = 1 + 0 = 1$)
- If $p = \infty$, then $q = 1$
- If $p = 2$, then $q = 2$ (self-conjugate)

**Notation:** We often write $q = p'$ or $q = p/(p-1)$ for the conjugate of $p$.

**Remark 3.9 (Equivalent Form).** Equation (3.16) is equivalent to:
$$
q = \frac{p}{p-1} \quad \text{for } 1 < p < \infty \tag{3.17}
$$

**Proof:** From $1/p + 1/q = 1$, solve for $q$:
$$
\frac{1}{q} = 1 - \frac{1}{p} = \frac{p-1}{p} \Rightarrow q = \frac{p}{p-1} \quad \square
$$

**Common Conjugate Pairs:**
- $p = 1 \leftrightarrow q = \infty$
- $p = 2 \leftrightarrow q = 2$ (self-dual)
- $p = 4 \leftrightarrow q = 4/3$
- $p = 3/2 \leftrightarrow q = 3$
- $p = 6 \leftrightarrow q = 6/5$

**Symmetry:** The conjugate relation is symmetric: if $q$ is conjugate to $p$, then $p$ is conjugate to $q$ (since $1/p + 1/q = 1/q + 1/p$).

---

### **II. The Riesz Representation Theorem for $(L^p)^*$**

**Theorem 3.9 (Riesz Representation for $(L^p)^*$, $1 < p < \infty$).** {#THM-3.9}
Let $(X, \mathcal{F}, \mu)$ be a $\sigma$-finite measure space and $1 < p < \infty$. Let $q$ be the conjugate exponent ($1/p + 1/q = 1$). Then:

**(Existence and Uniqueness):** For every continuous linear functional $\phi \in (L^p(\mu))^*$, there exists a **unique** $g \in L^q(\mu)$ (up to sets of measure zero) such that:
$$
\phi(f) = \int_X f g \, d\mu \quad \text{for all } f \in L^p(\mu) \tag{3.18}
$$

**(Isometry):** The operator norm of $\phi$ equals the $L^q$ norm of $g$:
$$
\|\phi\| = \|g\|_q \tag{3.19}
$$

**(Isomorphism):** The map $T: L^q(\mu) \to (L^p(\mu))^*$ defined by $T(g) = \phi_g$ (where $\phi_g(f) = \int fg \, d\mu$) is an **isometric isomorphism**. Thus:
$$
(L^p)^* \cong L^q \quad \text{(isometrically)} \tag{3.20}
$$

**Remark 3.10 (Bilinear Pairing).** The integral $\langle f, g \rangle := \int fg \, d\mu$ defines a **bilinear pairing** between $L^p$ and $L^q$. The theorem states that every continuous linear functional on $L^p$ arises from such a pairing with some $g \in L^q$.

**Remark 3.11 (Historical Context).** This theorem is another result due to **Frigyes Riesz** (1909), who proved it as part of his development of functional analysis on $L^p$ spaces. It generalizes the Riesz-Fischer theorem [THM-3.4] (completeness) by characterizing the **dual space** structure. The proof we present follows [@folland:real_analysis:1999, Theorem 6.14] and [@brezis:functional_analysis:2011, Theorem 4.10], using a constructive approach via simple functions.

---

**Proof (Case $1 < p < \infty$).**

The proof proceeds in four steps:
1. **Construction of $g$:** Define $g$ on simple functions, extend by density
2. **Prove $g \in L^q$:** Show $\|g\|_q = \|\phi\|$ using clever test functions
3. **Show $\phi(f) = \int fg$:** Verify the representation formula
4. **Uniqueness:** Prove $g$ is unique up to null sets

**Step 1: Construction of $g$ on simple functions.**

**Setup:** Let $\phi \in (L^p)^*$ be a continuous linear functional with $\|\phi\| < \infty$ (guaranteed by definition of dual space). We assume $\mu$ is $\sigma$-finite, so there exist sets $E_n \in \mathcal{F}$ with $\mu(E_n) < \infty$ and $E_n \nearrow X$.

**Key observation:** For measurable sets $E$ with $\mu(E) < \infty$, the characteristic function $\mathbf{1}_E \in L^p(\mu)$ (since $\|\mathbf{1}_E\|_p = \mu(E)^{1/p} < \infty$). Thus $\phi(\mathbf{1}_E)$ is well-defined.

**Substep 1a: Define $g$ on measurable sets.**

Define a **signed measure** $\nu$ on $(X, \mathcal{F})$ by:
$$
\nu(E) := \phi(\mathbf{1}_E) \quad \text{for all } E \in \mathcal{F} \text{ with } \mu(E) < \infty \tag{3.21}
$$

**Claim:** $\nu$ extends to a signed measure on $\mathcal{F}$ (not just finite measure sets).

**Proof of claim:** By $\sigma$-finiteness, write $X = \bigcup_{n=1}^\infty E_n$ with $E_n \nearrow X$ and $\mu(E_n) < \infty$. For any $E \in \mathcal{F}$, define:
$$
\nu(E) := \lim_{n \to \infty} \nu(E \cap E_n) = \lim_{n \to \infty} \phi(\mathbf{1}_{E \cap E_n})
$$

This limit exists because $\mathbf{1}_{E \cap E_n} \to \mathbf{1}_E$ in $L^p$ norm (by Dominated Convergence: $|\mathbf{1}_{E \cap E_n}| \leq \mathbf{1}_{E}$, and if $E$ has infinite measure, we restrict to $E \cap E_n$ first). By continuity of $\phi$:
$$
\nu(E) = \lim_{n \to \infty} \phi(\mathbf{1}_{E \cap E_n}) = \phi\left(\lim_{n \to \infty} \mathbf{1}_{E \cap E_n}\right) = \phi(\mathbf{1}_E)
$$
(using that $\mathbf{1}_{E \cap E_n} \to \mathbf{1}_E$ in $L^p$). □

**Substep 1b: $\nu$ is absolutely continuous with respect to $\mu$.**

**Claim:** If $\mu(E) = 0$, then $\nu(E) = 0$ (i.e., $\nu \ll \mu$, absolute continuity).

**Proof of claim:** If $\mu(E) = 0$, then $\mathbf{1}_E = 0$ in $L^p$ (since functions differing on null sets are equivalent). Thus:
$$
\nu(E) = \phi(\mathbf{1}_E) = \phi(0) = 0 \quad \text{(by linearity of $\phi$)} \quad \square
$$

**Substep 1c: Apply Radon-Nikodym theorem (to be proven Day 4).**

We invoke the **Radon-Nikodym theorem** (which we will establish rigorously on Day 4; see Syllabus Week 3, Thursday). Since $\nu \ll \mu$ and both are $\sigma$-finite, there exists a unique $g \in L^1(\mu)$ such that:
$$
\nu(E) = \int_E g \, d\mu \quad \text{for all } E \in \mathcal{F} \tag{3.22}
$$

**Pedagogical note:** The proof of Radon-Nikodym uses Hilbert space projection methods that we develop in Week 14 (Hilbert Spaces) and Week 4, Day 4. For today's purposes, we accept this result and complete the proof of Riesz representation. The reader seeking complete logical independence should read Day 4 first, then return to this proof.

**Historical note:** Riesz (1909) proved this theorem before Radon-Nikodym was formalized (1930). The original proof used a direct construction for $L^p$ spaces without invoking general measure-theoretic machinery. See [@folland:real_analysis:1999, §6.3] for the historical development.

This $g$ is called the **Radon-Nikodym derivative** $d\nu/d\mu$.

**Key insight:** For simple functions $f = \sum_{i=1}^n a_i \mathbf{1}_{E_i}$ with disjoint $E_i$:
$$
\phi(f) = \sum_{i=1}^n a_i \phi(\mathbf{1}_{E_i}) = \sum_{i=1}^n a_i \nu(E_i) = \sum_{i=1}^n a_i \int_{E_i} g \, d\mu = \int_X f g \, d\mu \tag{3.23}
$$

Thus $\phi(f) = \int fg \, d\mu$ holds for all **simple functions** $f$.

---

**Step 2: Prove $g \in L^q$ with $\|g\|_q = \|\phi\|$.**

We have $g \in L^1$ from Radon-Nikodym, but we need $g \in L^q$. We will construct a specific test function in $L^p$ and use the definition of $\|\phi\|$.

**Substep 2a: Define test function on finite-measure sets.**

We will prove $g \in L^q$ by showing $\int_A |g|^q < \infty$ for all $A \in \mathcal{F}$ with $\mu(A) < \infty$, then taking $A \nearrow X$ (using $\sigma$-finiteness).

**Key idea:** We **assume** $\int_A |g|^q < \infty$ **for the sake of constructing the test function** $f_A$, then **derive** a bound $\int_A |g|^q \leq \|\phi\|^q$ that holds **independently of our assumption**. This bound then implies $\int_A |g|^q < \infty$ is actually true (not just assumed), completing the bootstrap argument.

**Technical justification:** Since $g \in L^1$ (from Radon-Nikodym), the set $\{A : \int_A |g|^q < \infty\}$ is nonempty (contains all null sets and singletons if $\mu$ is discrete). We show this collection is actually **all** finite-measure sets by deriving a uniform bound.

For any measurable set $A$ with $\mu(A) < \infty$, define:
$$
f_A = \text{sgn}(g) \cdot |g|^{q-1} \cdot \mathbf{1}_A \tag{3.24}
$$

where $\text{sgn}(g) = g/|g|$ if $g \neq 0$, and $\text{sgn}(g) = 0$ if $g = 0$.

**Claim:** If $\int_A |g|^q < \infty$, then $f_A \in L^p(\mu)$.

**Proof of claim:** We have $|f_A| = |g|^{q-1} \mathbf{1}_A$, so:
$$
\int_X |f_A|^p \, d\mu = \int_A |g|^{p(q-1)} \, d\mu
$$

Using the conjugate relation $1/p + 1/q = 1$, we get:
$$
p(q-1) = p \left(\frac{p}{p-1} - 1\right) = p \left(\frac{p - (p-1)}{p-1}\right) = p \cdot \frac{1}{p-1} = \frac{p}{p-1} = q
$$

(using $q = p/(p-1)$ from (3.17)). Thus:
$$
\int_X |f_A|^p \, d\mu = \int_A |g|^q \, d\mu < \infty \quad \text{(by assumption)}
$$

Therefore $f_A \in L^p$ with:
$$
\|f_A\|_p^p = \int_A |g|^q \, d\mu \tag{3.25}
$$
□

**Substep 2b: Compute $\phi(f_A)$ using representation.**

By (3.23) (representation on simple functions), extended by density to all $L^p$:
$$
\phi(f_A) = \int_X f_A g \, d\mu = \int_A \text{sgn}(g) |g|^{q-1} \cdot g \, d\mu = \int_A |g|^q \, d\mu \tag{3.26}
$$

(since $\text{sgn}(g) \cdot g = |g|$).

**Substep 2c: Use $\|\phi\|$ to bound $\int |g|^q$.**

**Case 1:** $\int_A |g|^q = 0$. Then $g = 0$ $\mu$-almost everywhere on $A$, so the bound (3.27) below holds trivially ($0 \leq \|\phi\|$).

**Case 2:** $\int_A |g|^q > 0$. Then $f_A \in L^p$ with $\|f_A\|_p = \left(\int_A |g|^q\right)^{1/p} > 0$.

By definition of operator norm (3.15):
$$
|\phi(f_A)| \leq \|\phi\| \cdot \|f_A\|_p
$$

Substituting (3.26) and (3.25):
$$
\int_A |g|^q \, d\mu = |\phi(f_A)| \leq \|\phi\| \cdot \left(\int_A |g|^q \, d\mu\right)^{1/p}
$$

Dividing both sides by $\left(\int_A |g|^q\right)^{1/p}$ (which is nonzero):
$$
\left(\int_A |g|^q \, d\mu\right)^{1 - 1/p} \leq \|\phi\|
$$

Since $1 - 1/p = (p-1)/p = 1/q$ (by conjugate relation $1/p + 1/q = 1$):
$$
\left(\int_A |g|^q \, d\mu\right)^{1/q} \leq \|\phi\| \tag{3.27}
$$

Thus (3.27) holds in both cases. ✓

**Substep 2d: Take supremum over $A$.**

Since (3.27) holds for all $A \in \mathcal{F}$ with $\mu(A) < \infty$, by $\sigma$-finiteness we can take $A = E_n \nearrow X$:
$$
\|g\|_q = \left(\int_X |g|^q \, d\mu\right)^{1/q} = \sup_n \left(\int_{E_n} |g|^q \, d\mu\right)^{1/q} \leq \|\phi\| < \infty
$$

Thus $g \in L^q(\mu)$ with $\|g\|_q \leq \|\phi\|$. ✓

**Substep 2e: Prove reverse inequality $\|\phi\| \leq \|g\|_q$.**

For any $f \in L^p$ with $\|f\|_p \leq 1$, by Hölder's inequality [THM-2.4]:
$$
|\phi(f)| = \left|\int f g \, d\mu\right| \leq \int |f| |g| \, d\mu \leq \|f\|_p \|g\|_q \leq \|g\|_q \tag{3.28}
$$

Taking supremum over all $f$ with $\|f\|_p \leq 1$:
$$
\|\phi\| = \sup_{\|f\|_p \leq 1} |\phi(f)| \leq \|g\|_q
$$

Combined with Substep 2d:
$$
\|\phi\| = \|g\|_q \tag{3.29}
$$

This is the **isometry** property. ✓

---

**Step 3: Show $\phi(f) = \int fg \, d\mu$ for all $f \in L^p$.**

We established (3.23) for simple functions. By density of simple functions in $L^p$ (standard fact; see [@folland:real_analysis:1999, Proposition 2.10]), for any $f \in L^p$ there exists a sequence of simple functions $f_n \to f$ in $L^p$ norm.

By continuity of $\phi$:
$$
\phi(f) = \phi\left(\lim_{n \to \infty} f_n\right) = \lim_{n \to \infty} \phi(f_n) = \lim_{n \to \infty} \int f_n g \, d\mu
$$

By Hölder's inequality, $\int |f_n - f| |g| \leq \|f_n - f\|_p \|g\|_q \to 0$, so:
$$
\lim_{n \to \infty} \int f_n g \, d\mu = \int f g \, d\mu
$$

(using Dominated Convergence or direct $\epsilon$-$\delta$ argument). Thus:
$$
\phi(f) = \int f g \, d\mu \quad \text{for all } f \in L^p \tag{3.30}
$$

✓

---

**Step 4: Uniqueness of $g$.**

Suppose $g_1, g_2 \in L^q$ both represent $\phi$, i.e., $\phi(f) = \int fg_1 = \int fg_2$ for all $f \in L^p$. Then:
$$
\int f(g_1 - g_2) \, d\mu = 0 \quad \text{for all } f \in L^p
$$

**Key test function:** Take $f = \text{sgn}(g_1 - g_2) |g_1 - g_2|^{q-1}$ (same construction as in Step 2). This $f \in L^p$ (by conjugate relation), and:
$$
\int f(g_1 - g_2) \, d\mu = \int |g_1 - g_2|^q \, d\mu = 0
$$

Since $|g_1 - g_2|^q \geq 0$ and its integral is zero, we have $|g_1 - g_2|^q = 0$ $\mu$-a.e., hence $g_1 = g_2$ $\mu$-a.e. □

This completes the proof of Theorem 3.9. □

---

**Remark 3.12 (Why $1 < p < \infty$ is Required).** The proof crucially uses that the test function $f_A = \text{sgn}(g) |g|^{q-1} \mathbf{1}_A$ lies in $L^p$, which requires $p(q-1) = q < \infty$ (i.e., $q$ is finite). This holds when $1 < p < \infty$, but:
- For $p = 1$ (so $q = \infty$), the test function $f_A = |g|^{\infty - 1}$ is not well-defined
- For $p = \infty$ (so $q = 1$), the test function would be $f_A = |g|^0 = 1$, which doesn't capture all of $L^\infty$

The cases $p = 1$ and $p = \infty$ require separate treatment (next section).

---

### **III. Special Cases and Counterexamples**

#### **A. Case $p = 2$: Self-Duality of $L^2$**

**Corollary 3.10 ($L^2$ is Self-Dual).** {#COR-3.10}
For any $\sigma$-finite measure space $(X, \mathcal{F}, \mu)$:
$$
(L^2(\mu))^* \cong L^2(\mu) \quad \text{(isometrically)} \tag{3.31}
$$

**Proof.** Apply Theorem 3.9 with $p = q = 2$ (since $1/2 + 1/2 = 1$). □

**Remark 3.13 (Inner Product Structure).** The pairing $\langle f, g \rangle = \int fg \, d\mu$ is actually an **inner product** on $L^2$ (symmetric, positive definite, bilinear). This makes $L^2$ a **Hilbert space** (complete inner product space; Week 14). The Riesz representation for $L^2$ is a special case of the **Riesz representation theorem for Hilbert spaces** [@brezis:functional_analysis:2011, Theorem 5.5], which states:

*Every continuous linear functional $\phi$ on a Hilbert space $H$ has the form $\phi(x) = \langle x, y \rangle$ for some unique $y \in H$ with $\|\phi\| = \|y\|$.*

This is more general than our result (applies to any Hilbert space, not just $L^2$), but the proof is essentially the same.

**RL Connection (Least-Squares TD):** LSTD [@bradtke:lstd:1996] solves the projected Bellman equation $V_\theta = \Pi T^\pi V_\theta$ by projecting the Bellman operator $T^\pi$ onto a linear subspace $\text{span}(\phi) \subset L^2(\mu)$, where $\mu$ is the state distribution under policy $\pi$.

The projection $\Pi: L^2(\mu) \to \text{span}(\phi)$ is defined via:
$$
\Pi V = \arg\min_{V_\theta \in \text{span}(\phi)} \|V - V_\theta\|_{L^2(\mu)}^2 = \arg\min \mathbb{E}_\mu[(V(s) - V_\theta(s))^2]
$$

By the **Projection Theorem** (Week 14), $\Pi$ exists, is unique, and satisfies $\langle V - \Pi V, V_\theta \rangle_\mu = 0$ for all $V_\theta \in \text{span}(\phi)$ (orthogonality).

**Key theoretical guarantee:** If the projected Bellman operator $\Pi T^\pi: \text{span}(\phi) \to \text{span}(\phi)$ is a $\gamma$-contraction (holds when features are well-conditioned), then LSTD converges to the unique fixed point $V_\theta^* = \Pi T^\pi V_\theta^*$ [@tsitsiklis:analysis_td:1997].

**Practical limitations:**
1. **Approximation error:** $\|V^\pi - V_\theta^*\|_\mu \geq \|V^\pi - \Pi V^\pi\|_\mu$ (bounded below by representational capacity of features)
2. **Computational cost:** $O(d^3)$ matrix inversion (intractable for $d > 10^4$); practitioners use **incremental TD($\lambda$)** instead ($O(d)$ per sample)
3. **Chattering:** If $\Pi T^\pi$ is not a contraction, LSTD may not converge (see [@baird:residual_algorithms:1995] for counterexamples with linear function approximation)

**Modern deep RL:** Neural network function approximators break the $L^2$ projection framework (features $\phi_\theta$ are learned, not fixed). Convergence guarantees do not apply; empirical success relies on clever exploration, large replay buffers, and target networks [@mnih:dqn:2015].

---

#### **B. Case $p = 1$: $(L^1)^* \cong L^\infty$**

**Theorem 3.11 (Duality of $L^1$ and $L^\infty$).** {#THM-3.11}
Let $(X, \mathcal{F}, \mu)$ be a **$\sigma$-finite** measure space. Then:
$$
(L^1(\mu))^* \cong L^\infty(\mu) \quad \text{(isometrically)} \tag{3.32}
$$

More precisely, every $\phi \in (L^1)^*$ has the form:
$$
\phi(f) = \int_X f g \, d\mu \quad \text{for all } f \in L^1
$$
for some unique $g \in L^\infty$ with $\|\phi\| = \|g\|_\infty$.

**Proof sketch:** The proof is similar to Theorem 3.9 but requires $\sigma$-finiteness more crucially (without it, the dual of $L^1$ can be strictly larger than $L^\infty$; see Remark 3.14 below). The construction uses Radon-Nikodym to define $g$, then shows $g$ is essentially bounded by using test functions of the form $f = \mathbf{1}_A$ for sets $A$ with $\mu(A) < \infty$. See [@folland:real_analysis:1999, Theorem 6.15] or [@brezis:functional_analysis:2011, Theorem 4.11] for details. □

**Remark 3.14 (σ-Finiteness is Crucial).** Without $\sigma$-finiteness, $(L^1)^* \supsetneq L^\infty$ (strict containment).

**Counterexample:** Let $X = \mathbb{R}$ with **counting measure** $\mu(E) = |E|$ (cardinality). Then:
- $L^1(\mu) = \ell^1 = \{(x_n) : \sum |x_n| < \infty\}$ (absolutely summable sequences)
- $L^\infty(\mu) = \ell^\infty = \{(x_n) : \sup_n |x_n| < \infty\}$ (bounded sequences)

The dual $(\ell^1)^* \cong \ell^\infty$ **only on countable spaces**. On uncountable $X$ with counting measure, $(L^1)^*$ includes "finitely additive measures" that are not $\sigma$-additive, which lie outside $L^\infty$ (see [@folland:real_analysis:1999, Example 6.16] for details).

**RL Implication:** In RL, state spaces are typically **finite** (discrete MDPs) or have **probability measures** (continuous MDPs with $\mu(\mathcal{S}) = 1 < \infty$), both of which are $\sigma$-finite. Thus $(L^1)^* \cong L^\infty$ holds in all practical RL settings.

---

#### **C. Case $p = \infty$: Duality Fails for $L^\infty$**

**Theorem 3.12 ($(L^\infty)^*$ is Larger than $L^1$).** {#THM-3.12}
For any non-atomic measure space (e.g., Lebesgue measure on $\mathbb{R}$):
$$
(L^\infty(\mu))^* \supsetneq L^1(\mu) \quad \text{(strict containment)} \tag{3.33}
$$

**Proof sketch:**

**(Step 1: Embedding $L^1 \to (L^\infty)^*$):** Every $g \in L^1$ defines a functional $\phi_g(f) = \int fg \, d\mu$ on $L^\infty$. This map $g \mapsto \phi_g$ is an **isometric embedding** $L^1 \hookrightarrow (L^\infty)^*$ (injective, norm-preserving), since:
$$
|\phi_g(f)| = \left|\int fg \, d\mu\right| \leq \int |f| |g| \, d\mu \leq \|f\|_\infty \|g\|_1
$$
with equality achieved by $f = \text{sgn}(g)$. Thus $\|\phi_g\| = \|g\|_1$.

**(Step 2: $(L^\infty)^*$ is strictly larger):** For **non-atomic** measure spaces (e.g., Lebesgue measure on $[0,1]$), $(L^\infty)^*$ contains functionals **not** of the form $\phi_g$ for any $g \in L^1$.

**Explicit example (Banach limit):** On $\ell^\infty(\mathbb{N})$ (bounded sequences), the **Banach limit** $\text{LIM}$ is a functional satisfying:
1. $\text{LIM}(x) \geq 0$ if $x_n \geq 0$ for all $n$
2. $\text{LIM}(x_1, x_2, x_3, \ldots) = \text{LIM}(x_2, x_3, x_4, \ldots)$ (shift-invariance)
3. $\text{LIM}$ extends the ordinary limit (if $\lim_{n \to \infty} x_n$ exists, then $\text{LIM}(x) = \lim x_n$)

Such a functional exists by Hahn-Banach (Week 12) but is **not** given by any $g \in \ell^1$. Indeed, if $\text{LIM}(x) = \sum_{n=1}^\infty g_n x_n$ for some $g \in \ell^1$, then property (2) would imply $g_1 = g_2 = g_3 = \cdots$ (constant), but then $\sum g_n = \infty$ (contradicting $g \in \ell^1$).

**General case:** For $L^\infty(\mu)$ with non-atomic $\mu$, analogous "purely finitely additive" functionals exist (see [@folland:real_analysis:1999, §6.4] or [@yosida:functional_analysis:1980, Chapter IV.5]). These are sometimes called "singular functionals" (orthogonal to $L^1$ in a weak sense).

**Conclusion:** $(L^\infty)^* \supsetneq L^1$ strictly. □

**Remark 3.15 (Why This Matters for RL).** In RL, we primarily work with:
- **$L^\infty$ as domain for value functions** (bounded rewards, bounded values)
- **$L^1$ or probability measures as domains for state distributions**

The fact that $(L^\infty)^* \supsetneq L^1$ means that **not all linear functionals on value functions correspond to state distributions**. This is actually not a problem—the functionals arising in RL (e.g., $V \mapsto \mathbb{E}_\mu[V(s)]$) **do** correspond to measures, which are a subset of $(L^\infty)^*$.

**Practical note:** For **finite state spaces**, $L^\infty(\mathcal{S}) = \mathbb{R}^{|\mathcal{S}|}$ (all functions are bounded), and $(L^\infty)^* = L^1 = \mathbb{R}^{|\mathcal{S}|}$ (canonical duality). The failure of duality only matters for **infinite-dimensional** $L^\infty$ spaces.

---

### **IV. Corollaries and Applications**

**Corollary 3.13 (Hölder's Inequality is Sharp).** {#COR-3.13}
For $1 \leq p \leq \infty$ and conjugate $q$, Hölder's inequality [THM-2.4] states:
$$
\left|\int fg \, d\mu\right| \leq \|f\|_p \|g\|_q
$$

The constant $1$ is **sharp** (best possible): for any $f \in L^p$ with $f \neq 0$, there exists $g \in L^q$ with $\|g\|_q = 1$ such that $\int fg = \|f\|_p$.

**Proof.** Take $g = \text{sgn}(f) |f|^{p-1} / \|f\|_p^{p-1}$ (normalized version of the test function from Theorem 3.9 proof). Then $\|g\|_q = 1$ (by conjugate relation) and:
$$
\int fg \, d\mu = \frac{1}{\|f\|_p^{p-1}} \int |f|^p \, d\mu = \frac{\|f\|_p^p}{\|f\|_p^{p-1}} = \|f\|_p \quad \square
$$

---

**Corollary 3.14 (Reflexivity of $L^p$ for $1 < p < \infty$).** {#COR-3.14}
For $1 < p < \infty$ and $\sigma$-finite $\mu$, the space $L^p(\mu)$ is **reflexive**, meaning:
$$
(L^p)^{**} \cong L^p \quad \text{(canonically)} \tag{3.34}
$$

where $(L^p)^{**} := ((L^p)^*)^*$ is the **double dual** (dual of the dual).

**Proof.** By Theorem 3.9, $(L^p)^* \cong L^q$ where $1/p + 1/q = 1$. Applying Theorem 3.9 again to $L^q$:
$$
(L^q)^* \cong L^p \quad \text{(since $1/q + 1/p = 1$)}
$$

Thus:
$$
(L^p)^{**} = ((L^p)^*)^* \cong (L^q)^* \cong L^p \quad \square
$$

**Remark 3.16 (Non-Reflexivity of $L^1$ and $L^\infty$).** The spaces $L^1$ and $L^\infty$ are **not reflexive**:
- $(L^1)^{**} \cong (L^\infty)^* \supsetneq L^1$ (strictly larger)
- $(L^\infty)^{**} \supsetneq (L^\infty)^*$ (even larger)

Reflexivity fails at the "endpoints" $p = 1, \infty$. This is why $L^2$ (the "middle" case) is particularly nice—it's reflexive, self-dual, and has an inner product structure.

---

### **V. Mathematical Insight and RL Connections**

**Mathematical Insight:**

The Riesz representation theorem reveals a **profound duality** between $L^p$ and $L^q$:

1. **Geometric interpretation:** Every continuous linear functional on $L^p$ is given by "integration against an $L^q$ function." This is analogous to the finite-dimensional fact that every linear functional on $\mathbb{R}^n$ is "dot product with a vector."

2. **Completeness + Duality = Reflexivity:** For $1 < p < \infty$, combining Riesz-Fischer [THM-3.4] (completeness) with Riesz Representation [THM-3.9] (duality) yields reflexivity: $(L^p)^{**} \cong L^p$. This means $L^p$ "sees itself" when looking at its double dual—there's no "loss of information" in taking duals.

3. **$L^2$ is special:** It's the unique $L^p$ space that is:
   - Complete (Banach)
   - Self-dual ($(L^2)^* \cong L^2$)
   - Has inner product structure (Hilbert space)

   This trio of properties makes $L^2$ the natural home for **least-squares methods** in RL.

**Proof Strategy Recap:**

1. Use Radon-Nikodym to construct $g$ from $\phi$ (via signed measure $\nu(E) = \phi(\mathbf{1}_E)$)
2. Show $g \in L^q$ by testing against $f = \text{sgn}(g) |g|^{q-1}$ (clever use of conjugate exponents)
3. Verify $\|\phi\| = \|g\|_q$ (isometry) via Hölder
4. Uniqueness follows from test function argument

**Key tools:** Hölder's inequality [THM-2.4], Radon-Nikodym (Day 4 preview), density of simple functions in $L^p$

**RL Connection:**

**1. Value Functions and State Distributions are Dual**

In an MDP $(\mathcal{S}, \mathcal{A}, P, r, \gamma)$, the **value function** $V^\pi: \mathcal{S} \to \mathbb{R}$ and the **state visitation distribution** $\mu_\pi$ under policy $\pi$ are related by:
$$
J(\pi) = \mathbb{E}_{\mu_\pi}[V^\pi(s)] = \int_\mathcal{S} V^\pi(s) \, \mu_\pi(ds)
$$

This is **precisely the duality pairing** $\langle V^\pi, \mu_\pi \rangle$ between:
- $V^\pi \in L^2(\mathcal{S}, \nu)$ (value function; lives in function space)
- $\mu_\pi$ (state distribution; lives in dual space of measures)

**Why $L^2$ specifically?** Because:
- $L^2$ has an **inner product** $\langle V, W \rangle_\nu = \mathbb{E}_\nu[V(s)W(s)]$ (weighted by reference measure $\nu$)
- State distributions $\mu_\pi$ are **probability measures**, which induce functionals $\phi_\mu(V) = \mathbb{E}_\mu[V(s)]$
- By Riesz representation, every such functional corresponds to a unique "density" $d\mu_\pi/d\nu \in L^2(\nu)$ (if $\mu_\pi \ll \nu$; see Radon-Nikodym on Day 4)

**Application to Policy Gradients (Week 37):** The **policy gradient theorem** [@sutton:policy_gradient:2000] states that for a parameterized policy $\pi_\theta$ in an MDP with discount factor $\gamma \in [0,1)$, the gradient of the **expected discounted return** $J(\theta) = \mathbb{E}_{\pi_\theta}[\sum_{t=0}^\infty \gamma^t r_t]$ is:
$$
\nabla_\theta J(\theta) = \mathbb{E}_{d_\pi}\left[\mathbb{E}_{a \sim \pi_\theta(\cdot|s)}[\nabla_\theta \log \pi_\theta(a|s) Q^\pi(s,a)]\right]
$$
where $d_\pi(s)$ is the **discounted state occupancy measure**:
$$
d_\pi(s) = (1 - \gamma) \sum_{t=0}^\infty \gamma^t P(s_t = s | s_0 \sim \rho_0, \pi_\theta)
$$
and $Q^\pi(s,a) = \mathbb{E}_\pi[\sum_{t=0}^\infty \gamma^t r_t | s_0 = s, a_0 = a]$ is the action-value function.

**Key assumptions:**
- **On-policy sampling:** The gradient formula assumes samples $(s,a)$ are drawn from $d_\pi$ (the distribution induced by $\pi_\theta$)
- **Differentiable policy:** $\pi_\theta(a|s)$ is differentiable in $\theta$ for all $(s,a)$
- **Finite expected return:** $\mathbb{E}[\sum \gamma^t r_t] < \infty$ (holds if rewards are bounded and $\gamma < 1$)

**Practical implementation:** Actor-critic methods [@konda:actor_critic:2000] approximate $Q^\pi$ with a learned critic $Q_w(s,a)$, yielding the **stochastic policy gradient**:
$$
\nabla_\theta J(\theta) \approx \frac{1}{N} \sum_{i=1}^N \nabla_\theta \log \pi_\theta(a_i|s_i) Q_w(s_i, a_i)
$$
where $(s_i, a_i) \sim d_\pi$ (on-policy samples). For off-policy data, importance sampling corrections are required (Week 36-37).

**2. Linear Function Approximation as Dual Space**

In **linear value function approximation**, we parameterize:
$$
V_\theta(s) = \theta^\top \phi(s) = \sum_{i=1}^d \theta_i \phi_i(s)
$$

where $\phi: \mathcal{S} \to \mathbb{R}^d$ are feature maps. The value function space is:
$$
\mathcal{V} = \{\theta^\top \phi : \theta \in \mathbb{R}^d\} = \text{span}(\phi_1, \ldots, \phi_d) \subseteq L^2(\mathcal{S}, \mu)
$$

**Duality perspective:** Every $V_\theta \in \mathcal{V}$ defines a **linear functional** on the dual space:
$$
\psi_\theta: g \mapsto \mathbb{E}_\mu[V_\theta(s) g(s)] = \int \theta^\top \phi(s) \cdot g(s) \, \mu(ds)
$$

By Riesz representation, this functional **is** the element $V_\theta \in L^2$.

**Least-Squares TD (LSTD):** Given samples $(s_i, r_i, s_i')$ from policy $\pi$, **LSTD (Least-Squares Temporal Difference)** [@bradtke:lstd:1996] solves the **projected Bellman equation**:
$$
V_\theta = \Pi T^\pi V_\theta
$$
where $\Pi: L^2(\mu) \to \text{span}(\phi_1, \ldots, \phi_d)$ is the **orthogonal projection** onto the linear subspace, and $T^\pi$ is the Bellman operator:
$$
(T^\pi V)(s) = r(s) + \gamma \mathbb{E}_{s' \sim P(\cdot|s, \pi(s))}[V(s')]
$$
In matrix form, the fixed-point equation becomes:
$$
\mathbb{E}_\mu[\phi(s)(\phi(s) - \gamma\phi(s'))^\top]\theta = \mathbb{E}_\mu[\phi(s)r(s)]
$$
LSTD solves this via sample averages (requires $O(d^3)$ matrix inversion, where $d$ is feature dimension).

**Key limitation:** The solution $V_\theta$ is the **best linear approximation** to $V^\pi$ in the $L^2(\mu)$ norm, **not** the true value function $V^\pi$ (unless $V^\pi \in \text{span}(\phi)$). The approximation error $\|V^\pi - V_\theta\|_\mu$ depends on the **expressiveness of features** $\phi$ (see [@tsitsiklis:analysis_td:1997] for error bounds).

**3. Importance Sampling and Radon-Nikodym Derivatives**

In **off-policy RL**, we collect data under **behavior policy** $\mu$ but want to evaluate **target policy** $\pi$. The correction is:
$$
\mathbb{E}_\pi[V(s)] = \mathbb{E}_\mu\left[\frac{d\pi}{d\mu}(s) V(s)\right]
$$

where $d\pi/d\mu$ is the **Radon-Nikodym derivative** (density of $\pi$ with respect to $\mu$). This is **precisely** a change-of-measure formula using duality:
- $\mu$ and $\pi$ are measures on $\mathcal{S}$
- $V \in L^2(\mathcal{S}, \mu)$ is the value function
- The ratio $d\pi/d\mu$ converts between the two measures

**Per-decision importance sampling ratio:**
$$
\rho_t = \frac{\pi(a_t|s_t)}{\mu(a_t|s_t)} = \frac{d\pi(a|s)}{d\mu(a|s)}
$$

This is a Radon-Nikodym derivative **on the action space** $\mathcal{A}$ (conditional on state $s$). For trajectories $(s_0, a_0, \ldots, s_T, a_T)$, the cumulative importance weight is:
$$
\rho_{0:T-1} = \prod_{t=0}^{T-1} \frac{\pi(a_t|s_t)}{\mu(a_t|s_t)}
$$

**High-variance problem:** For trajectories of length $T$, the cumulative importance weight is:
$$
\rho_{0:T-1} = \prod_{t=0}^{T-1} \frac{\pi(a_t|s_t)}{\mu(a_t|s_t)}
$$
If each $\rho_t$ has variance $\sigma^2$ (independent), the product has variance:
$$
\text{Var}[\rho_{0:T-1}] \approx (\sigma^2 + 1)^T - 1 \quad \text{(exponential in $T$)}
$$
(assuming $\mathbb{E}[\rho_t] = 1$ and independence). For $T = 100$ and $\sigma = 2$, this yields $\text{Var} \approx 5^{100} \approx 10^{70}$ (astronomical!).

**Variance reduction techniques:**

1. **Per-decision importance sampling** [@precup:per_decision_is:2000]: Use $\rho_t$ only for step $t$, not cumulative product:
   $$
   \mathbb{E}_\pi[r_t] \approx \frac{1}{N} \sum_{i=1}^N \rho_t^{(i)} r_t^{(i)} \quad \text{(variance } O(T\sigma^2) \text{ instead of } O(\sigma^{2T}) \text{)}
   $$

2. **Weighted importance sampling** [@precup:eligibility_traces:2000]: Normalize by sum of weights:
   $$
   \hat{\mathbb{E}}_\pi[r] = \frac{\sum_i \rho_i r_i}{\sum_i \rho_i} \quad \text{(biased but lower variance)}
   $$

3. **Clipping (PPO-style)** [@schulman:ppo:2017]: Clip importance weights to $[1-\epsilon, 1+\epsilon]$:
   $$
   L^{\text{CLIP}}(\theta) = \mathbb{E}_{\mu}\left[\min(\rho_t A_t, \text{clip}(\rho_t, 1-\epsilon, 1+\epsilon) A_t)\right]
   $$
   (ensures $\rho_t \approx 1$, reducing variance; $\epsilon \approx 0.2$ in practice)

4. **V-trace (IMPALA)** [@espeholt:impala:2018]: Truncated importance weights with fixed thresholds:
   $$
   \bar{\rho}_t = \min(\rho_t, \bar{c}), \quad \bar{\rho}_t = \min(\rho_t, \bar{\rho}) \quad (\bar{c} = 1, \bar{\rho} = 1 \text{ typical})
   $$
   (off-policy actor-critic with bounded importance weights; convergent under mild assumptions)

**Note on TRPO:** TRPO [@schulman:trpo:2015] is **on-policy** (uses natural policy gradient, not importance sampling). The KL constraint $D_{\text{KL}}(\pi_{\theta'} \| \pi_\theta) \leq \delta$ ensures $\rho(s,a) = \pi_{\theta'}(a|s)/\pi_\theta(a|s) \approx 1$ (small policy updates), indirectly controlling importance weight variance.

**Connection to Radon-Nikodym (Day 4):** On Thursday, we prove the Radon-Nikodym theorem, which characterizes when $d\mu/d\nu$ exists (when $\mu \ll \nu$, absolute continuity). This formalizes the existence of importance sampling ratios in RL.

---

**Contrast with Non-Dual Spaces:**

Spaces that **don't** have nice duality include:
- **$L^p$ for $p \notin [1, \infty]$:** Quasi-norms (triangle inequality fails), no duality theory
- **$C([0,1])$ with $L^1$ norm:** Incomplete, $(C([0,1]))^* \supsetneq L^\infty([0,1])$ (extra functionals from Hahn-Banach)
- **$L^\infty$ in general:** $(L^\infty)^* \supsetneq L^1$ (purely finitely additive functionals)

The $L^p$ spaces for $1 < p < \infty$ are the "sweet spot"—complete, reflexive, nice duality.

---

**Looking Ahead:**

- **Day 3 (Wednesday):** We continue duality discussion, focusing on special cases and counterexamples. We'll also introduce the concept of **weak convergence** in dual spaces.

- **Day 4 (Thursday, Extended Proof Session):** **Radon-Nikodym theorem**—when does a measure have a **density** with respect to another? (i.e., when does $d\mu/d\nu$ exist?). This is the foundation of importance sampling in RL. We will see that LSTD in detail requires understanding this material (Week 35 provides full implementation details).

- **Day 5 (Friday, Synthesis):** Weekly reflection on $L^p$ completeness and duality, coding exercises on importance sampling and least-squares projection.

- **Week 14 (Hilbert Spaces):** We'll see that $L^2$ is not just a Banach space but a **Hilbert space** (complete inner product space). The **projection theorem** (existence of orthogonal projections onto closed subspaces) is the foundation of least-squares TD.

Today's theorem—Riesz Representation for $(L^p)^*$—establishes the **dual space structure** that underlies all linear methods in RL. Combined with Day 1's completeness (Riesz-Fischer), we now have a complete picture of $L^p$ as a Banach space with explicit dual.

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_2_exercises_revised_math+rl]]**

**Anchor Exercise Preview:**
1. **Verify $(L^2)^* \cong L^2$:** Show that the Riesz representation for $p = 2$ yields the inner product pairing $\phi(f) = \langle f, g \rangle = \int fg \, d\mu$.

2. **Compute conjugate exponents:** For each $p \in \{1, 4/3, 3/2, 2, 3, 4, 6, \infty\}$, find the conjugate $q$ satisfying $1/p + 1/q = 1$. Verify that $q = p/(p-1)$ for $1 < p < \infty$.

3. **RL Application (Bellman Operator as Functional):** Let $\mathcal{S}$ be a finite state space with $|\mathcal{S}| = n$. For a given policy $\pi$, define the **reward functional** $\phi_r: \mathbb{R}^n \to \mathbb{R}$ by $\phi_r(V) = \sum_{s \in \mathcal{S}} r_s V_s$ where $r_s$ is the reward at state $s$. Show:
   - $\phi_r \in (\ell^\infty)^*$ (dual of $L^\infty$)
   - $\phi_r$ is represented by integration against $r \in \ell^1$: $\phi_r(V) = \sum_s r_s V_s$
   - If $\|r\|_1 = 1$, then $\|\phi_r\| = 1$ (operator norm)

4. **Reflexivity of $L^p$:** Prove that $L^p$ is reflexive for $1 < p < \infty$ by showing $(L^p)^{**} \cong L^p$ using Theorem 3.9 twice.

---

**Reflection Questions:**

1. **Why does the proof require $1 < p < \infty$? What goes wrong for $p = 1$ or $p = \infty$?**
   *Hint:* The test function $f = \text{sgn}(g) |g|^{q-1}$ requires $q < \infty$ (so $p > 1$). For $p = 1$ ($q = \infty$), this function is not well-defined. For $p = \infty$ ($q = 1$), the construction doesn't capture all of $(L^\infty)^*$.

2. **What is the relationship between Hölder's inequality [THM-2.4] and Riesz representation [THM-3.9]?**
   *Hint:* Hölder provides the "easy" inequality $\|\phi\| \leq \|g\|_q$ (equation 3.28). The "hard" direction $\|g\|_q \leq \|\phi\|$ uses the test function construction in Step 2, which "saturates" Hölder's inequality (achieves equality).

3. **How does duality explain the "state-value duality" in RL?**
   *Hint:* Value functions $V \in L^2(\mathcal{S})$ and state distributions $\mu$ (measures on $\mathcal{S}$) are dual via the pairing $\langle V, \mu \rangle = \mathbb{E}_\mu[V(s)]$. By Riesz representation, every measure defines a functional on $L^2$, and vice versa (if $\mu \ll \nu$, the reference measure).

---

**Daily Study Note:**

**What I learned today:**
- **Dual space $(L^p)^*$**: continuous linear functionals $\phi: L^p \to \mathbb{R}$ with $|\phi(f)| \leq \|\phi\| \|f\|_p$
- **Riesz Representation [THM-3.9]**: $(L^p)^* \cong L^q$ for conjugate exponents $1/p + 1/q = 1$ (when $1 < p < \infty$)
- **Isometric isomorphism**: $\|\phi\| = \|g\|_q$ where $\phi(f) = \int fg \, d\mu$
- **Proof strategy**: Radon-Nikodym to construct $g$ $\to$ test against $f = \text{sgn}(g) |g|^{q-1}$ to show $g \in L^q$ $\to$ density argument for representation
- **Special cases**: $(L^2)^* \cong L^2$ (self-dual), $(L^1)^* \cong L^\infty$ (on $\sigma$-finite spaces), $(L^\infty)^* \supsetneq L^1$ (duality fails)

**Connection to previous material:**
- Builds on Riesz-Fischer [THM-3.4] (completeness) from Day 1
- Uses Hölder's inequality [THM-2.4] from Week 2, Day 4 crucially
- Previews Radon-Nikodym theorem (Day 4) for constructing $g$ from $\phi$

**Looking forward:**
- Day 3: Weak convergence, dual space topology
- Day 4: Radon-Nikodym theorem—densities $d\mu/d\nu$ for importance sampling
- Week 14: Hilbert spaces—$L^2$ inner product, projection theorem for LSTD

**RL connections identified:**
- Value functions and state distributions are dual (pairing $\langle V, \mu \rangle = \mathbb{E}_\mu[V]$)
- Linear function approximation lives in $L^2$, dual space is also $L^2$ (self-duality)
- Importance sampling ratios $\pi/\mu$ are Radon-Nikodym derivatives (Day 4 preview)
- Least-squares TD uses $L^2$ projection, which requires Hilbert space structure (Week 14)
- Policy gradients integrate against state distributions (duality pairing with value functions)
- Natural policy gradients use Fisher metric (L^2 inner product on score functions)

**Time spent:** 90-120 minutes (within acceptable range for rigorous duality theory on Tuesday)

---

**End of Day 2**
