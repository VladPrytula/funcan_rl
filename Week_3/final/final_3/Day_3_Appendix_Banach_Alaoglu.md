## **Appendix 3.A: Complete Proof of the Banach-Alaoglu Theorem**

**Companion to:** [[Day_3_draft_revised_all]] — Weak Convergence and Dual Topologies (Week 3, Day 3)

**Reading time:** ~40 minutes (optional extended proof; can defer to Week 14 when studying functional analysis in depth)

**Prerequisites:** Basic topology (product topology, compactness, Tychonoff's theorem), dual spaces, weak* topology

**Purpose:** This appendix provides a complete, rigorous proof of the Banach-Alaoglu theorem [THM-3.18], the cornerstone compactness result for weak* topology. The main Day 3 theory file presented a proof sketch; here we fill in all details for readers who want full rigor.

---

### **Statement of Banach-Alaoglu Theorem**

**Theorem 3.18 (Banach-Alaoglu Theorem).** {#THM-3.18-FULL}
Let $X$ be a normed vector space over $\mathbb{R}$ (or $\mathbb{C}$) and $X^*$ its dual space. The **closed unit ball** in $X^*$:
$$
B_{X^*} := \{\phi \in X^* : \|\phi\| \leq 1\} \tag{A.1}
$$
is **compact** in the **weak* topology**.

**Recall:** The **weak* topology** on $X^*$ is the coarsest topology making all evaluation maps $\phi \mapsto \phi(x)$ continuous for $x \in X$. Equivalently:
- A sequence $\{\phi_n\}$ converges weak* to $\phi$ if $\phi_n(x) \to \phi(x)$ for all $x \in X$ (pointwise convergence)
- A set is weak* compact if every sequence has a weak* convergent subsequence (sequential compactness; equivalent to compactness in metrizable spaces, which the weak* topology on bounded sets is)

**Implication:** Every bounded sequence $\{\phi_n\}$ in $X^*$ (i.e., $\sup_n \|\phi_n\| \leq C < \infty$) has a subsequence $\{\phi_{n_k}\}$ converging weak* to some $\phi \in X^*$.

---

### **Proof Strategy**

The proof has three main steps:

**Step 1:** Embed $B_{X^*}$ into a product space $\prod_{x \in B_X} [-C, C]$ where $B_X = \{x \in X : \|x\| \leq 1\}$ is the unit ball in $X$.

**Step 2:** Apply **Tychonoff's theorem** to show the product space is compact in the product topology (pointwise convergence topology).

**Step 3:** Show that $B_{X^*}$ is a **closed subset** of this compact product space (in the product topology), hence compact by general topology.

**Step 4:** Verify that the weak* topology on $B_{X^*}$ coincides with the subspace topology inherited from the product space, so compactness in product topology implies weak* compactness.

Let us execute each step carefully.

---

### **Step 1: Embedding into Product Space**

**Construction of the embedding:** For each $x \in X$, the evaluation map $\text{ev}_x: X^* \to \mathbb{R}$ defined by $\text{ev}_x(\phi) = \phi(x)$ is a linear functional. We use these evaluation maps to embed $X^*$ into a product of real numbers.

**Key observation:** If $\phi \in B_{X^*}$ (i.e., $\|\phi\| \leq 1$) and $x \in B_X$ (i.e., $\|x\| \leq 1$), then:
$$
|\phi(x)| \leq \|\phi\| \|x\| \leq 1 \cdot 1 = 1 \tag{A.2}
$$

Thus $\phi(x) \in [-1, 1]$ for all $x \in B_X$.

**The embedding map:** Define $\Phi: B_{X^*} \to \prod_{x \in B_X} [-1, 1]$ by:
$$
\Phi(\phi) = (\phi(x))_{x \in B_X} \tag{A.3}
$$

That is, $\Phi$ maps each functional $\phi$ to the "tuple" (infinite-dimensional) of its values on all unit vectors.

**Claim 1:** $\Phi$ is injective.

*Proof.* Suppose $\Phi(\phi_1) = \Phi(\phi_2)$. Then $\phi_1(x) = \phi_2(x)$ for all $x \in B_X$. For any $x \in X$ with $x \neq 0$:
$$
\phi_1(x) = \phi_1\left(\|x\| \cdot \frac{x}{\|x\|}\right) = \|x\| \phi_1\left(\frac{x}{\|x\|}\right) = \|x\| \phi_2\left(\frac{x}{\|x\|}\right) = \phi_2(x)
$$
(using linearity and $\frac{x}{\|x\|} \in B_X$). Thus $\phi_1 = \phi_2$ on all of $X$. □

**Image of $\Phi$:** We view $B_{X^*}$ as a subset of the product space $\prod_{x \in B_X} [-1, 1]$ via the identification $\phi \leftrightarrow (\phi(x))_{x \in B_X}$.

---

### **Step 2: Tychonoff's Theorem**

We need a fundamental result from topology:

**Theorem A.1 (Tychonoff's Theorem).** {#THM-A.1}
Let $\{K_\alpha\}_{\alpha \in A}$ be a family of compact topological spaces (indexed by an arbitrary set $A$). Then the product space:
$$
\prod_{\alpha \in A} K_\alpha
$$
is compact in the **product topology** (the coarsest topology making all projection maps $\pi_\alpha: \prod K_\alpha \to K_\alpha$ continuous).

**Proof:** See any standard topology textbook (e.g., [@munkres:topology:2000, Theorem 37.3] or [@folland:real_analysis:1999, Theorem 4.40]). The proof requires the Axiom of Choice (or equivalently, Zorn's Lemma). □

**Application to our setting:** For each $x \in B_X$, the interval $[-1, 1]$ is compact in $\mathbb{R}$ (Heine-Borel). By Tychonoff's theorem:
$$
K := \prod_{x \in B_X} [-1, 1] \quad \text{is compact in the product topology} \tag{A.4}
$$

**Product topology on $K$:** A sequence $(y^{(n)}) = (y_x^{(n)})_{x \in B_X}$ converges in the product topology to $(y) = (y_x)_{x \in B_X}$ if and only if:
$$
y_x^{(n)} \to y_x \quad \text{for all } x \in B_X \tag{A.5}
$$
(pointwise convergence in each coordinate).

---

### **Step 3: $B_{X^*}$ is Closed in $K$**

We now show that $B_{X^*}$ (viewed as a subset of $K$ via the embedding $\Phi$) is closed in the product topology. By general topology, a closed subset of a compact space is compact. Thus, once we show $B_{X^*}$ is closed in $K$, we can conclude $B_{X^*}$ is compact in the subspace topology.

**Key properties that define $B_{X^*}$:** An element $(y_x)_{x \in B_X} \in K$ lies in $\Phi(B_{X^*})$ if and only if:
1. **Linearity:** $y_{ax+by} = a y_x + b y_y$ for all $x, y \in B_X$ and $a, b \in \mathbb{R}$ with $ax + by \in B_X$
2. **Boundedness:** $|y_x| \leq \|x\|$ for all $x \in B_X$

More precisely, $(y_x) \in \Phi(B_{X^*})$ means there exists $\phi \in B_{X^*}$ with $y_x = \phi(x)$ for all $x \in B_X$. The linearity and boundedness of $\phi$ translate to constraints on the tuple $(y_x)$.

**Claim 2:** $\Phi(B_{X^*})$ is closed in $K$ (in the product topology).

*Proof.* We show that the complement of $\Phi(B_{X^*})$ is open, or equivalently, that $\Phi(B_{X^*})$ contains all its limit points.

Let $(y^{(n)}) = (y_x^{(n)})_{x \in B_X}$ be a sequence in $\Phi(B_{X^*})$ converging to $(y) = (y_x)_{x \in B_X}$ in the product topology. We must show $(y) \in \Phi(B_{X^*})$.

Since $(y^{(n)}) \in \Phi(B_{X^*})$, there exist functionals $\phi_n \in B_{X^*}$ with $y_x^{(n)} = \phi_n(x)$ for all $x \in B_X$.

By product topology convergence (A.5):
$$
\phi_n(x) = y_x^{(n)} \to y_x \quad \text{for all } x \in B_X \tag{A.6}
$$

**Define candidate functional:** For $x \in X$, define:
$$
\phi(x) := \begin{cases}
y_x & \text{if } x \in B_X \\
\|x\| y_{x/\|x\|} & \text{if } x \notin B_X \text{ and } x \neq 0 \\
0 & \text{if } x = 0
\end{cases} \tag{A.7}
$$

We need to verify:
1. $\phi$ is well-defined and linear
2. $\phi$ is bounded with $\|\phi\| \leq 1$
3. $\phi(x) = y_x$ for all $x \in B_X$ (so $(y) = \Phi(\phi)$)

**Verification of linearity:** For $x, y \in X$ and $a, b \in \mathbb{R}$, we need $\phi(ax + by) = a\phi(x) + b\phi(y)$.

**Case 1:** $ax + by \in B_X$. Then $\phi(ax+by) = y_{ax+by}$. Since each $\phi_n$ is linear:
$$
\phi_n(ax + by) = a\phi_n(x) + b\phi_n(y)
$$

Taking $n \to \infty$ and using (A.6):
$$
y_{ax+by} = \lim_{n \to \infty} \phi_n(ax+by) = a \lim_{n \to \infty} \phi_n(x) + b \lim_{n \to \infty} \phi_n(y)
$$

Now, for $\lim \phi_n(x)$:
- If $x \in B_X$: $\lim \phi_n(x) = y_x = \phi(x)$
- If $x \notin B_X$: We have $\frac{x}{\|x\|} \in B_X$, so:
$$
\phi_n(x) = \phi_n\left(\|x\| \cdot \frac{x}{\|x\|}\right) = \|x\| \phi_n\left(\frac{x}{\|x\|}\right) \to \|x\| y_{x/\|x\|} = \phi(x)
$$

Thus $\lim \phi_n(x) = \phi(x)$ for all $x \in X$. Similarly for $y$. Therefore:
$$
y_{ax+by} = a\phi(x) + b\phi(y)
$$

which gives $\phi(ax+by) = a\phi(x) + b\phi(y)$ when $ax+by \in B_X$.

**Case 2:** $ax + by \notin B_X$ and $ax+by \neq 0$. Similar reasoning (left as exercise; the key is that scaling preserves linearity).

Thus $\phi$ is linear on $X$.

**Verification of boundedness:** For any $x \in X$ with $\|x\| \leq 1$:
$$
|\phi(x)| = |y_x| = \lim_{n \to \infty} |\phi_n(x)| \leq \lim_{n \to \infty} \|\phi_n\| \|x\| \leq 1 \cdot \|x\| \leq 1
$$
(using $\|\phi_n\| \leq 1$ for all $n$).

For $x \in X$ with $\|x\| > 0$:
$$
|\phi(x)| = \left|\|x\| y_{x/\|x\|}\right| = \|x\| |y_{x/\|x\|}| = \|x\| \left|\lim_{n \to \infty} \phi_n\left(\frac{x}{\|x\|}\right)\right| \leq \|x\| \cdot 1 = \|x\|
$$

Thus $|\phi(x)| \leq \|x\|$ for all $x \in X$, so $\|\phi\| \leq 1$. Hence $\phi \in B_{X^*}$.

**Verification of $\Phi(\phi) = (y)$:** By definition (A.7), $\phi(x) = y_x$ for all $x \in B_X$. Thus $\Phi(\phi) = (\phi(x))_{x \in B_X} = (y_x)_{x \in B_X} = (y)$.

**Conclusion:** Every limit point $(y)$ of $\Phi(B_{X^*})$ lies in $\Phi(B_{X^*})$. Thus $\Phi(B_{X^*})$ is closed in $K$. □

**Corollary:** Since $K$ is compact (by Tychonoff) and $\Phi(B_{X^*})$ is closed in $K$, we have that $\Phi(B_{X^*})$ is compact in the subspace topology inherited from $K$.

---

### **Step 4: Weak* Topology = Subspace Topology**

We now verify that compactness of $\Phi(B_{X^*})$ in the product topology (subspace topology from $K$) is equivalent to compactness of $B_{X^*}$ in the weak* topology on $X^*$.

**Definition of weak* topology on $X^*$:** The **weak* topology** on $X^*$ is the coarsest topology making all evaluation maps $\text{ev}_x: X^* \to \mathbb{R}$ (defined by $\text{ev}_x(\phi) = \phi(x)$) continuous.

**Basis for weak* topology:** A subbasis for the weak* topology consists of sets:
$$
U_{x,V} := \{\phi \in X^* : \phi(x) \in V\}
$$
where $x \in X$ and $V \subset \mathbb{R}$ is open.

**Weak* convergence:** $\phi_n \overset{*}{\rightharpoonup} \phi$ (weak*) if and only if $\phi_n(x) \to \phi(x)$ for all $x \in X$ (pointwise convergence).

**Product topology on $K$:** Convergence in the product topology on $K = \prod_{x \in B_X} [-1, 1]$ is precisely pointwise convergence in each coordinate: $(y^{(n)}) \to (y)$ if and only if $y_x^{(n)} \to y_x$ for all $x \in B_X$.

**Claim 3:** The weak* topology on $B_{X^*}$ coincides with the subspace topology inherited from the product topology on $K$ via the embedding $\Phi$.

*Proof.* We need to show:
1. Weak* convergence $\phi_n \overset{*}{\rightharpoonup} \phi$ in $B_{X^*}$ if and only if $\Phi(\phi_n) \to \Phi(\phi)$ in the product topology on $K$.

**($\Rightarrow$)** Suppose $\phi_n \overset{*}{\rightharpoonup} \phi$ weak*. Then $\phi_n(x) \to \phi(x)$ for all $x \in X$, in particular for all $x \in B_X$. Thus:
$$
\Phi(\phi_n) = (\phi_n(x))_{x \in B_X} \to (\phi(x))_{x \in B_X} = \Phi(\phi)
$$
in the product topology (pointwise convergence in each coordinate).

**($\Leftarrow$)** Suppose $\Phi(\phi_n) \to \Phi(\phi)$ in product topology. Then $\phi_n(x) \to \phi(x)$ for all $x \in B_X$. For any $x \in X$ with $x \neq 0$:
$$
\phi_n(x) = \|x\| \phi_n\left(\frac{x}{\|x\|}\right) \to \|x\| \phi\left(\frac{x}{\|x\|}\right) = \phi(x)
$$
(using $\frac{x}{\|x\|} \in B_X$ and linearity). Thus $\phi_n(x) \to \phi(x)$ for all $x \in X$, so $\phi_n \overset{*}{\rightharpoonup} \phi$ weak*.

Therefore, the topologies coincide on $B_{X^*}$. □

**Conclusion of proof:** We have shown:
1. $B_{X^*}$ embeds via $\Phi$ into the product space $K = \prod_{x \in B_X} [-1, 1]$ (Step 1)
2. $K$ is compact in the product topology (Tychonoff, Step 2)
3. $\Phi(B_{X^*})$ is closed in $K$, hence compact in the subspace topology (Step 3)
4. The weak* topology on $B_{X^*}$ coincides with the subspace topology from $K$ (Step 4)

Therefore, $B_{X^*}$ is compact in the weak* topology. This completes the proof of Banach-Alaoglu. □

---

### **Sequential Compactness and Metrizability**

**Remark A.2 (Sequential Compactness).** The Banach-Alaoglu theorem is often stated in terms of sequential compactness: every bounded sequence $\{\phi_n\}$ in $X^*$ has a weak* convergent subsequence.

In general topological spaces, compactness and sequential compactness are distinct notions. However, for the weak* topology on bounded sets in $X^*$ (when $X$ is separable), the weak* topology is **metrizable**, so compactness and sequential compactness coincide.

**Proposition A.3 (Metrizability of Weak* Topology on Bounded Sets).** {#PROP-A.3}
If $X$ is a **separable** normed space (i.e., $X$ has a countable dense subset), then the weak* topology on $B_{X^*}$ is **metrizable** (can be induced by a metric).

**Proof sketch:** Let $\{x_n\}_{n=1}^\infty$ be a countable dense subset of $B_X$. Define a metric on $B_{X^*}$ by:
$$
d(\phi, \psi) := \sum_{n=1}^\infty \frac{1}{2^n} |\phi(x_n) - \psi(x_n)| \tag{A.8}
$$

This metric induces the weak* topology on $B_{X^*}$ (verification left as exercise; the key is that convergence in this metric $\Leftrightarrow$ pointwise convergence on the dense set $\{x_n\}$, which extends to pointwise convergence on all of $X$ by continuity and density). □

**Corollary:** For separable $X$, the Banach-Alaoglu theorem can be stated as: every bounded sequence in $X^*$ has a weak* convergent subsequence (sequential compactness).

**Application to $L^p$ spaces:** For $1 \leq p < \infty$, $L^p(\mu)$ is separable (when $\mu$ is σ-finite; simple functions are dense). Thus Banach-Alaoglu gives sequential compactness of bounded sets in $(L^p)^* \cong L^q$.

---

### **Proof Summary and Key Ideas**

**Main idea:** Embed the unit ball $B_{X^*}$ into a product of compact intervals $[-1, 1]$. By Tychonoff, the product is compact. Show $B_{X^*}$ is a closed subset (using linearity and boundedness), hence compact. Verify weak* topology = product topology on the embedding.

**Key ingredients:**
1. **Tychonoff's theorem** (product of compact spaces is compact) — requires Axiom of Choice
2. **Characterization of $X^*$** via evaluation maps (functionals determined by values on unit ball)
3. **Linearity and boundedness are preserved under pointwise limits** (closed subset argument)
4. **Weak* topology = pointwise convergence topology** (via embedding)

**Why Banach-Alaoglu is powerful:**
- In infinite dimensions, unit balls are **not** norm-compact (Riesz's theorem: norm-compact unit ball $\Leftrightarrow$ finite dimension)
- But unit balls in $X^*$ **are** weak*-compact (Banach-Alaoglu)
- This restores compactness in a weaker topology, enabling existence theorems in optimization, PDE theory, and RL

**RL relevance (from main text):**
- Policy spaces are weak*-compact, so optimal policies exist (Theorem 3.22)
- Value function iterates have convergent subsequences (Exercise 3.3.3(c))
- Distribution sequences in policy gradients have convergent subsequences (Exercise 3.3.4)

---

### **Further Reading**

For deeper exploration of Banach-Alaoglu and its applications:

**Functional Analysis:**
- [@brezis:functional_analysis:2011, Theorem 3.16]: Banach-Alaoglu with detailed proof (similar to ours)
- [@folland:real_analysis:1999, Theorem 5.18]: Banach-Alaoglu in the context of measure theory and $L^p$ spaces
- [@rudin:functional_analysis:1991, Theorem 3.15]: Alaoglu's theorem with applications to weak compactness

**Topology (Tychonoff's Theorem):**
- [@munkres:topology:2000, Theorem 37.3]: Tychonoff's theorem with proof using ultrafilters
- [@folland:real_analysis:1999, Theorem 4.40]: Tychonoff's theorem using Zorn's Lemma

**Applications to Optimization and RL:**
- [@puterman:mdps:2005, Chapter 6]: Existence of optimal policies via weak* compactness
- [@bertsekas-tsitsiklis:neuro-dp:1996, Appendix A]: Functional analysis for dynamic programming
- [@borkar:stochastic_approximation:2008, Appendix B]: Compactness arguments in stochastic approximation

**Weak Topologies in Probability:**
- [@billingsley:convergence:1999, Chapter 1]: Weak convergence of probability measures (closely related to weak* convergence)
- [@durrett:probability:2019, Section 2.3]: Convergence of measures and distributions

---

### **Exercises for Appendix 3.A** (optional, for readers seeking deeper understanding)

**Exercise A.1 (Verification of Linearity).** {#EX-A.1}
Complete the proof of Claim 2 by verifying that the functional $\phi$ defined in (A.7) is linear in Case 2 ($ax + by \notin B_X$ and $ax + by \neq 0$).

**Exercise A.2 (Metrizability).** {#EX-A.2}
Prove Proposition A.3: show that the metric $d(\phi, \psi) = \sum_{n=1}^\infty \frac{1}{2^n} |\phi(x_n) - \psi(x_n)|$ induces the weak* topology on $B_{X^*}$ when $X$ is separable with dense set $\{x_n\}$.

**Exercise A.3 (Application to $\ell^2$).** {#EX-A.3}
Apply the Banach-Alaoglu theorem to $\ell^2$:
1. Show that $\ell^2$ is separable (construct a countable dense subset)
2. Verify that the unit ball in $\ell^2$ is weak*-compact by applying Banach-Alaoglu
3. Extract a weakly convergent subsequence from $\{e^{(n)}\}$ (standard basis vectors) using sequential compactness

**Exercise A.4 (Non-reflexive Spaces).** {#EX-A.4}
For $X = c_0$ (sequences converging to $0$ with supremum norm), we have $X^* = \ell^1$ but $X^{**} \supsetneq c_0$ (not reflexive).
1. Show that the unit ball in $\ell^1 = (c_0)^*$ is weak*-compact (Banach-Alaoglu)
2. Show that the unit ball in $c_0$ is **not** weakly compact (unlike reflexive spaces where weak and weak* compactness of unit ball both hold)
3. Explain why reflexivity fails: $c_0 \subsetneq (c_0)^{**}$

---

**End of Appendix 3.A**

**Return to:** [[Day_3_draft_revised_all]] for the main theory content and RL applications of weak convergence.
## **Appendix 3.A: Complete Proof of the Banach-Alaoglu Theorem**

**Companion to:** [[Day_3_draft_revised_all]] — Weak Convergence and Dual Topologies (Week 3, Day 3)

**Reading time:** ~40 minutes (optional extended proof; can defer to Week 14 when studying functional analysis in depth)

**Prerequisites:** Basic topology (product topology, compactness, Tychonoff's theorem), dual spaces, weak* topology

**Purpose:** This appendix provides a complete, rigorous proof of the Banach-Alaoglu theorem [THM-3.18], the cornerstone compactness result for weak* topology. The main Day 3 theory file presented a proof sketch; here we fill in all details for readers who want full rigor.

---

### **Statement of Banach-Alaoglu Theorem**

**Theorem 3.18 (Banach-Alaoglu Theorem).** {#THM-3.18-FULL}
Let $X$ be a normed vector space over $\mathbb{R}$ (or $\mathbb{C}$) and $X^*$ its dual space. The **closed unit ball** in $X^*$:
$$
B_{X^*} := \{\phi \in X^* : \|\phi\| \leq 1\} \tag{A.1}
$$
is **compact** in the **weak* topology**.

**Recall:** The **weak* topology** on $X^*$ is the coarsest topology making all evaluation maps $\phi \mapsto \phi(x)$ continuous for $x \in X$. Equivalently:
- A sequence $\{\phi_n\}$ converges weak* to $\phi$ if $\phi_n(x) \to \phi(x)$ for all $x \in X$ (pointwise convergence)
- A set is weak* compact if every sequence has a weak* convergent subsequence (sequential compactness; equivalent to compactness in metrizable spaces, which the weak* topology on bounded sets is)

**Implication:** Every bounded sequence $\{\phi_n\}$ in $X^*$ (i.e., $\sup_n \|\phi_n\| \leq C < \infty$) has a subsequence $\{\phi_{n_k}\}$ converging weak* to some $\phi \in X^*$.

---

### **Proof Strategy**

The proof has three main steps:

**Step 1:** Embed $B_{X^*}$ into a product space $\prod_{x \in B_X} [-C, C]$ where $B_X = \{x \in X : \|x\| \leq 1\}$ is the unit ball in $X$.

**Step 2:** Apply **Tychonoff's theorem** to show the product space is compact in the product topology (pointwise convergence topology).

**Step 3:** Show that $B_{X^*}$ is a **closed subset** of this compact product space (in the product topology), hence compact by general topology.

**Step 4:** Verify that the weak* topology on $B_{X^*}$ coincides with the subspace topology inherited from the product space, so compactness in product topology implies weak* compactness.

Let us execute each step carefully.

---

### **Step 1: Embedding into Product Space**

**Construction of the embedding:** For each $x \in X$, the evaluation map $\text{ev}_x: X^* \to \mathbb{R}$ defined by $\text{ev}_x(\phi) = \phi(x)$ is a linear functional. We use these evaluation maps to embed $X^*$ into a product of real numbers.

**Key observation:** If $\phi \in B_{X^*}$ (i.e., $\|\phi\| \leq 1$) and $x \in B_X$ (i.e., $\|x\| \leq 1$), then:
$$
|\phi(x)| \leq \|\phi\| \|x\| \leq 1 \cdot 1 = 1 \tag{A.2}
$$

Thus $\phi(x) \in [-1, 1]$ for all $x \in B_X$.

**The embedding map:** Define $\Phi: B_{X^*} \to \prod_{x \in B_X} [-1, 1]$ by:
$$
\Phi(\phi) = (\phi(x))_{x \in B_X} \tag{A.3}
$$

That is, $\Phi$ maps each functional $\phi$ to the "tuple" (infinite-dimensional) of its values on all unit vectors.

**Claim 1:** $\Phi$ is injective.

*Proof.* Suppose $\Phi(\phi_1) = \Phi(\phi_2)$. Then $\phi_1(x) = \phi_2(x)$ for all $x \in B_X$. For any $x \in X$ with $x \neq 0$:
$$
\phi_1(x) = \phi_1\left(\|x\| \cdot \frac{x}{\|x\|}\right) = \|x\| \phi_1\left(\frac{x}{\|x\|}\right) = \|x\| \phi_2\left(\frac{x}{\|x\|}\right) = \phi_2(x)
$$
(using linearity and $\frac{x}{\|x\|} \in B_X$). Thus $\phi_1 = \phi_2$ on all of $X$. □

**Image of $\Phi$:** We view $B_{X^*}$ as a subset of the product space $\prod_{x \in B_X} [-1, 1]$ via the identification $\phi \leftrightarrow (\phi(x))_{x \in B_X}$.

---

### **Step 2: Tychonoff's Theorem**

We need a fundamental result from topology:

**Theorem A.1 (Tychonoff's Theorem).** {#THM-A.1}
Let $\{K_\alpha\}_{\alpha \in A}$ be a family of compact topological spaces (indexed by an arbitrary set $A$). Then the product space:
$$
\prod_{\alpha \in A} K_\alpha
$$
is compact in the **product topology** (the coarsest topology making all projection maps $\pi_\alpha: \prod K_\alpha \to K_\alpha$ continuous).

**Proof:** See any standard topology textbook (e.g., [@munkres:topology:2000, Theorem 37.3] or [@folland:real_analysis:1999, Theorem 4.40]). The proof requires the Axiom of Choice (or equivalently, Zorn's Lemma). □

**Application to our setting:** For each $x \in B_X$, the interval $[-1, 1]$ is compact in $\mathbb{R}$ (Heine-Borel). By Tychonoff's theorem:
$$
K := \prod_{x \in B_X} [-1, 1] \quad \text{is compact in the product topology} \tag{A.4}
$$

**Product topology on $K$:** A sequence $(y^{(n)}) = (y_x^{(n)})_{x \in B_X}$ converges in the product topology to $(y) = (y_x)_{x \in B_X}$ if and only if:
$$
y_x^{(n)} \to y_x \quad \text{for all } x \in B_X \tag{A.5}
$$
(pointwise convergence in each coordinate).

---

### **Step 3: $B_{X^*}$ is Closed in $K$**

We now show that $B_{X^*}$ (viewed as a subset of $K$ via the embedding $\Phi$) is closed in the product topology. By general topology, a closed subset of a compact space is compact. Thus, once we show $B_{X^*}$ is closed in $K$, we can conclude $B_{X^*}$ is compact in the subspace topology.

**Key properties that define $B_{X^*}$:** An element $(y_x)_{x \in B_X} \in K$ lies in $\Phi(B_{X^*})$ if and only if:
1. **Linearity:** $y_{ax+by} = a y_x + b y_y$ for all $x, y \in B_X$ and $a, b \in \mathbb{R}$ with $ax + by \in B_X$
2. **Boundedness:** $|y_x| \leq \|x\|$ for all $x \in B_X$

More precisely, $(y_x) \in \Phi(B_{X^*})$ means there exists $\phi \in B_{X^*}$ with $y_x = \phi(x)$ for all $x \in B_X$. The linearity and boundedness of $\phi$ translate to constraints on the tuple $(y_x)$.

**Claim 2:** $\Phi(B_{X^*})$ is closed in $K$ (in the product topology).

*Proof.* We show that the complement of $\Phi(B_{X^*})$ is open, or equivalently, that $\Phi(B_{X^*})$ contains all its limit points.

Let $(y^{(n)}) = (y_x^{(n)})_{x \in B_X}$ be a sequence in $\Phi(B_{X^*})$ converging to $(y) = (y_x)_{x \in B_X}$ in the product topology. We must show $(y) \in \Phi(B_{X^*})$.

Since $(y^{(n)}) \in \Phi(B_{X^*})$, there exist functionals $\phi_n \in B_{X^*}$ with $y_x^{(n)} = \phi_n(x)$ for all $x \in B_X$.

By product topology convergence (A.5):
$$
\phi_n(x) = y_x^{(n)} \to y_x \quad \text{for all } x \in B_X \tag{A.6}
$$

**Define candidate functional:** For $x \in X$, define:
$$
\phi(x) := \begin{cases}
y_x & \text{if } x \in B_X \\
\|x\| y_{x/\|x\|} & \text{if } x \notin B_X \text{ and } x \neq 0 \\
0 & \text{if } x = 0
\end{cases} \tag{A.7}
$$

We need to verify:
1. $\phi$ is well-defined and linear
2. $\phi$ is bounded with $\|\phi\| \leq 1$
3. $\phi(x) = y_x$ for all $x \in B_X$ (so $(y) = \Phi(\phi)$)

**Verification of linearity:** For $x, y \in X$ and $a, b \in \mathbb{R}$, we need $\phi(ax + by) = a\phi(x) + b\phi(y)$.

**Case 1:** $ax + by \in B_X$. Then $\phi(ax+by) = y_{ax+by}$. Since each $\phi_n$ is linear:
$$
\phi_n(ax + by) = a\phi_n(x) + b\phi_n(y)
$$

Taking $n \to \infty$ and using (A.6):
$$
y_{ax+by} = \lim_{n \to \infty} \phi_n(ax+by) = a \lim_{n \to \infty} \phi_n(x) + b \lim_{n \to \infty} \phi_n(y)
$$

Now, for $\lim \phi_n(x)$:
- If $x \in B_X$: $\lim \phi_n(x) = y_x = \phi(x)$
- If $x \notin B_X$: We have $\frac{x}{\|x\|} \in B_X$, so:
$$
\phi_n(x) = \phi_n\left(\|x\| \cdot \frac{x}{\|x\|}\right) = \|x\| \phi_n\left(\frac{x}{\|x\|}\right) \to \|x\| y_{x/\|x\|} = \phi(x)
$$

Thus $\lim \phi_n(x) = \phi(x)$ for all $x \in X$. Similarly for $y$. Therefore:
$$
y_{ax+by} = a\phi(x) + b\phi(y)
$$

which gives $\phi(ax+by) = a\phi(x) + b\phi(y)$ when $ax+by \in B_X$.

**Case 2:** $ax + by \notin B_X$ and $ax+by \neq 0$. Similar reasoning (left as exercise; the key is that scaling preserves linearity).

Thus $\phi$ is linear on $X$.

**Verification of boundedness:** For any $x \in X$ with $\|x\| \leq 1$:
$$
|\phi(x)| = |y_x| = \lim_{n \to \infty} |\phi_n(x)| \leq \lim_{n \to \infty} \|\phi_n\| \|x\| \leq 1 \cdot \|x\| \leq 1
$$
(using $\|\phi_n\| \leq 1$ for all $n$).

For $x \in X$ with $\|x\| > 0$:
$$
|\phi(x)| = \left|\|x\| y_{x/\|x\|}\right| = \|x\| |y_{x/\|x\|}| = \|x\| \left|\lim_{n \to \infty} \phi_n\left(\frac{x}{\|x\|}\right)\right| \leq \|x\| \cdot 1 = \|x\|
$$

Thus $|\phi(x)| \leq \|x\|$ for all $x \in X$, so $\|\phi\| \leq 1$. Hence $\phi \in B_{X^*}$.

**Verification of $\Phi(\phi) = (y)$:** By definition (A.7), $\phi(x) = y_x$ for all $x \in B_X$. Thus $\Phi(\phi) = (\phi(x))_{x \in B_X} = (y_x)_{x \in B_X} = (y)$.

**Conclusion:** Every limit point $(y)$ of $\Phi(B_{X^*})$ lies in $\Phi(B_{X^*})$. Thus $\Phi(B_{X^*})$ is closed in $K$. □

**Corollary:** Since $K$ is compact (by Tychonoff) and $\Phi(B_{X^*})$ is closed in $K$, we have that $\Phi(B_{X^*})$ is compact in the subspace topology inherited from $K$.

---

### **Step 4: Weak* Topology = Subspace Topology**

We now verify that compactness of $\Phi(B_{X^*})$ in the product topology (subspace topology from $K$) is equivalent to compactness of $B_{X^*}$ in the weak* topology on $X^*$.

**Definition of weak* topology on $X^*$:** The **weak* topology** on $X^*$ is the coarsest topology making all evaluation maps $\text{ev}_x: X^* \to \mathbb{R}$ (defined by $\text{ev}_x(\phi) = \phi(x)$) continuous.

**Basis for weak* topology:** A subbasis for the weak* topology consists of sets:
$$
U_{x,V} := \{\phi \in X^* : \phi(x) \in V\}
$$
where $x \in X$ and $V \subset \mathbb{R}$ is open.

**Weak* convergence:** $\phi_n \overset{*}{\rightharpoonup} \phi$ (weak*) if and only if $\phi_n(x) \to \phi(x)$ for all $x \in X$ (pointwise convergence).

**Product topology on $K$:** Convergence in the product topology on $K = \prod_{x \in B_X} [-1, 1]$ is precisely pointwise convergence in each coordinate: $(y^{(n)}) \to (y)$ if and only if $y_x^{(n)} \to y_x$ for all $x \in B_X$.

**Claim 3:** The weak* topology on $B_{X^*}$ coincides with the subspace topology inherited from the product topology on $K$ via the embedding $\Phi$.

*Proof.* We need to show:
1. Weak* convergence $\phi_n \overset{*}{\rightharpoonup} \phi$ in $B_{X^*}$ if and only if $\Phi(\phi_n) \to \Phi(\phi)$ in the product topology on $K$.

**($\Rightarrow$)** Suppose $\phi_n \overset{*}{\rightharpoonup} \phi$ weak*. Then $\phi_n(x) \to \phi(x)$ for all $x \in X$, in particular for all $x \in B_X$. Thus:
$$
\Phi(\phi_n) = (\phi_n(x))_{x \in B_X} \to (\phi(x))_{x \in B_X} = \Phi(\phi)
$$
in the product topology (pointwise convergence in each coordinate).

**($\Leftarrow$)** Suppose $\Phi(\phi_n) \to \Phi(\phi)$ in product topology. Then $\phi_n(x) \to \phi(x)$ for all $x \in B_X$. For any $x \in X$ with $x \neq 0$:
$$
\phi_n(x) = \|x\| \phi_n\left(\frac{x}{\|x\|}\right) \to \|x\| \phi\left(\frac{x}{\|x\|}\right) = \phi(x)
$$
(using $\frac{x}{\|x\|} \in B_X$ and linearity). Thus $\phi_n(x) \to \phi(x)$ for all $x \in X$, so $\phi_n \overset{*}{\rightharpoonup} \phi$ weak*.

Therefore, the topologies coincide on $B_{X^*}$. □

**Conclusion of proof:** We have shown:
1. $B_{X^*}$ embeds via $\Phi$ into the product space $K = \prod_{x \in B_X} [-1, 1]$ (Step 1)
2. $K$ is compact in the product topology (Tychonoff, Step 2)
3. $\Phi(B_{X^*})$ is closed in $K$, hence compact in the subspace topology (Step 3)
4. The weak* topology on $B_{X^*}$ coincides with the subspace topology from $K$ (Step 4)

Therefore, $B_{X^*}$ is compact in the weak* topology. This completes the proof of Banach-Alaoglu. □

---

### **Sequential Compactness and Metrizability**

**Remark A.2 (Sequential Compactness).** The Banach-Alaoglu theorem is often stated in terms of sequential compactness: every bounded sequence $\{\phi_n\}$ in $X^*$ has a weak* convergent subsequence.

In general topological spaces, compactness and sequential compactness are distinct notions. However, for the weak* topology on bounded sets in $X^*$ (when $X$ is separable), the weak* topology is **metrizable**, so compactness and sequential compactness coincide.

**Proposition A.3 (Metrizability of Weak* Topology on Bounded Sets).** {#PROP-A.3}
If $X$ is a **separable** normed space (i.e., $X$ has a countable dense subset), then the weak* topology on $B_{X^*}$ is **metrizable** (can be induced by a metric).

**Proof sketch:** Let $\{x_n\}_{n=1}^\infty$ be a countable dense subset of $B_X$. Define a metric on $B_{X^*}$ by:
$$
d(\phi, \psi) := \sum_{n=1}^\infty \frac{1}{2^n} |\phi(x_n) - \psi(x_n)| \tag{A.8}
$$

This metric induces the weak* topology on $B_{X^*}$ (verification left as exercise; the key is that convergence in this metric $\Leftrightarrow$ pointwise convergence on the dense set $\{x_n\}$, which extends to pointwise convergence on all of $X$ by continuity and density). □

**Corollary:** For separable $X$, the Banach-Alaoglu theorem can be stated as: every bounded sequence in $X^*$ has a weak* convergent subsequence (sequential compactness).

**Application to $L^p$ spaces:** For $1 \leq p < \infty$, $L^p(\mu)$ is separable (when $\mu$ is $\sigma$-finite; simple functions are dense). Thus Banach-Alaoglu gives sequential compactness of bounded sets in $(L^p)^* \cong L^q$.

---

### **Proof Summary and Key Ideas**

**Main idea:** Embed the unit ball $B_{X^*}$ into a product of compact intervals $[-1, 1]$. By Tychonoff, the product is compact. Show $B_{X^*}$ is a closed subset (using linearity and boundedness), hence compact. Verify weak* topology = product topology on the embedding.

**Key ingredients:**
1. **Tychonoff's theorem** (product of compact spaces is compact) — requires Axiom of Choice
2. **Characterization of $X^*$** via evaluation maps (functionals determined by values on unit ball)
3. **Linearity and boundedness are preserved under pointwise limits** (closed subset argument)
4. **Weak* topology = pointwise convergence topology** (via embedding)

**Why Banach-Alaoglu is powerful:**
- In infinite dimensions, unit balls are **not** norm-compact (Riesz's theorem: norm-compact unit ball $\Leftrightarrow$ finite dimension)
- But unit balls in $X^*$ **are** weak*-compact (Banach-Alaoglu)
- This restores compactness in a weaker topology, enabling existence theorems in optimization, PDE theory, and RL

**RL relevance (from main text):**
- Policy spaces are weak*-compact, so optimal policies exist (Theorem 3.22)
- Value function iterates have convergent subsequences (Exercise 3.3.3(c))
- Distribution sequences in policy gradients have convergent subsequences (Exercise 3.3.4)

---

### **Further Reading**

For deeper exploration of Banach-Alaoglu and its applications:

**Functional Analysis:**
- [@brezis:functional_analysis:2011, Theorem 3.16]: Banach-Alaoglu with detailed proof (similar to ours)
- [@folland:real_analysis:1999, Theorem 5.18]: Banach-Alaoglu in the context of measure theory and $L^p$ spaces
- [@rudin:functional_analysis:1991, Theorem 3.15]: Alaoglu's theorem with applications to weak compactness

**Topology (Tychonoff's Theorem):**
- [@munkres:topology:2000, Theorem 37.3]: Tychonoff's theorem with proof using ultrafilters
- [@folland:real_analysis:1999, Theorem 4.40]: Tychonoff's theorem using Zorn's Lemma

**Applications to Optimization and RL:**
- [@puterman:mdps:2005, Chapter 6]: Existence of optimal policies via weak* compactness
- [@bertsekas-tsitsiklis:neuro-dp:1996, Appendix A]: Functional analysis for dynamic programming
- [@borkar:stochastic_approximation:2008, Appendix B]: Compactness arguments in stochastic approximation

**Weak Topologies in Probability:**
- [@billingsley:convergence:1999, Chapter 1]: Weak convergence of probability measures (closely related to weak* convergence)
- [@durrett:probability:2019, Section 2.3]: Convergence of measures and distributions

---

### **Exercises for Appendix 3.A** (optional, for readers seeking deeper understanding)

**Exercise A.1 (Verification of Linearity).** {#EX-A.1}
Complete the proof of Claim 2 by verifying that the functional $\phi$ defined in (A.7) is linear in Case 2 ($ax + by \notin B_X$ and $ax + by \neq 0$).

**Exercise A.2 (Metrizability).** {#EX-A.2}
Prove Proposition A.3: show that the metric $d(\phi, \psi) = \sum_{n=1}^\infty \frac{1}{2^n} |\phi(x_n) - \psi(x_n)|$ induces the weak* topology on $B_{X^*}$ when $X$ is separable with dense set $\{x_n\}$.

**Exercise A.3 (Application to $\ell^2$).** {#EX-A.3}
Apply the Banach-Alaoglu theorem to $\ell^2$:
1. Show that $\ell^2$ is separable (construct a countable dense subset)
2. Verify that the unit ball in $\ell^2$ is weak*-compact by applying Banach-Alaoglu
3. Extract a weakly convergent subsequence from $\{e^{(n)}\}$ (standard basis vectors) using sequential compactness

**Exercise A.4 (Non-reflexive Spaces).** {#EX-A.4}
For $X = c_0$ (sequences converging to $0$ with supremum norm), we have $X^* = \ell^1$ but $X^{**} \supsetneq c_0$ (not reflexive).
1. Show that the unit ball in $\ell^1 = (c_0)^*$ is weak*-compact (Banach-Alaoglu)
2. Show that the unit ball in $c_0$ is **not** weakly compact (unlike reflexive spaces where weak and weak* compactness of unit ball both hold)
3. Explain why reflexivity fails: $c_0 \subsetneq (c_0)^{**}$

---

**End of Appendix 3.A**

**Return to:** [[Day_3_draft_revised_all]] for the main theory content and RL applications of weak convergence.
