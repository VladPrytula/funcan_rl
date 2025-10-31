[[Day_4#]]

# Carathéodory Extension Theorem: Exercises and Detailed Proofs

This document formalizes the construction steps for Lebesgue measure, providing technical details that support the main exposition in Day 4. These exercises verify the foundational properties of semirings, algebras, and pre-measures that underpin the Carathéodory extension.

---

## **Core Exercise: Verification of Semiring and Algebra Properties**

Before we can apply the Carathéodory extension theorem, we must verify that the elementary geometric objects (rectangles) form a semiring and that their finite unions form an algebra.

---

### **Exercise 1: Rectangles in $\mathbb{R}^n$ Form a Semiring**

**Statement:** Let $\mathcal{R}_n$ be the collection of all half-open rectangles in $\mathbb{R}^n$:
$$
\mathcal{R}_n = \left\{ \prod_{i=1}^{n} (a_i, b_i] \;\Big|\; a_i, b_i \in \mathbb{R}, \, a_i < b_i \right\} \cup \{\emptyset\}
$$
Prove that $\mathcal{R}_n$ is a semiring.

**Proof:**

We must verify the three defining properties of a semiring:

**Property 1: $\emptyset \in \mathcal{R}_n$**

By definition, we have included $\emptyset$ in $\mathcal{R}_n$. ✓

**Property 2: Closure under finite intersections**

Let $R_1 = \prod_{i=1}^{n} (a_i, b_i]$ and $R_2 = \prod_{i=1}^{n} (c_i, d_i]$ be two rectangles in $\mathcal{R}_n$.

The intersection is:
$$
R_1 \cap R_2 = \prod_{i=1}^{n} ((a_i, b_i] \cap (c_i, d_i])
$$

For each coordinate $i$, the intersection of intervals is:
$$
(a_i, b_i] \cap (c_i, d_i] = (\max\{a_i, c_i\}, \min\{b_i, d_i\}]
$$

This is a half-open interval if $\max\{a_i, c_i\} < \min\{b_i, d_i\}$, and is $\emptyset$ otherwise.

Thus $R_1 \cap R_2$ is either a rectangle in $\mathcal{R}_n$ or is $\emptyset \in \mathcal{R}_n$. ✓

**Property 3: Set differences are finite disjoint unions of rectangles**

Let $R_1 \subseteq R_2$ where $R_1 = \prod_{i=1}^{n} (a_i, b_i]$ and $R_2 = \prod_{i=1}^{n} (c_i, d_i]$.

The condition $R_1 \subseteq R_2$ implies $c_i \leq a_i < b_i \leq d_i$ for all $i \in \{1, \ldots, n\}$.

We must show that $R_2 \setminus R_1$ can be expressed as a finite disjoint union of rectangles.

**Strategy:** Use the principle of inclusion-exclusion in reverse. For dimension $n=1$, the difference of intervals is straightforward. For $n > 1$, we "slice" the difference along each coordinate.

**Case $n=1$:**
$$
R_2 \setminus R_1 = (c, d] \setminus (a, b] = (c, a] \cup (b, d]
$$
where we use the convention that $(x, y] = \emptyset$ if $x \geq y$.

Thus:
- If $c < a$, we include $(c, a]$
- If $b < d$, we include $(b, d]$

These are at most two disjoint intervals (rectangles in $\mathcal{R}_1$). ✓

**Case $n \geq 2$:**

We decompose $R_2 \setminus R_1$ by considering the "slabs" that extend beyond $R_1$ in each coordinate direction. The strategy is to peel off layers coordinate by coordinate.

**Explicit construction for $n = 2$:**

Let $R_1 = (a_1, b_1] \times (a_2, b_2]$ and $R_2 = (c_1, d_1] \times (c_2, d_2]$ with $c_i \leq a_i < b_i \leq d_i$ for $i = 1,2$.

Visualize $R_2$ as a large rectangle containing the smaller rectangle $R_1$. The difference $R_2 \setminus R_1$ consists of four "slabs":

1. **Bottom slab:** $(c_1, d_1] \times (c_2, a_2]$ (extends below $R_1$ in the second coordinate)
2. **Top slab:** $(c_1, d_1] \times (b_2, d_2]$ (extends above $R_1$ in the second coordinate)
3. **Left slab:** $(c_1, a_1] \times (a_2, b_2]$ (extends left of $R_1$ in the first coordinate)
4. **Right slab:** $(b_1, d_1] \times (a_2, b_2]$ (extends right of $R_1$ in the first coordinate)

These four rectangles are pairwise disjoint and their union is $R_2 \setminus R_1$. Each uses the convention that $(x, y] = \emptyset$ if $x \geq y$.

**General case $n \geq 2$:**

For arbitrary dimension $n$, we use the following **slab decomposition formula**.

For each $i \in \{1, \ldots, n\}$, define the **$i$-th left slab**:
$$
S_i^{-} = \left(\prod_{j < i} (a_j, b_j]\right) \times (c_i, a_i] \times \left(\prod_{j > i} (c_j, d_j]\right)
$$

and the **$i$-th right slab**:
$$
S_i^{+} = \left(\prod_{j < i} (a_j, b_j]\right) \times (b_i, d_i] \times \left(\prod_{j > i} (c_j, d_j]\right)
$$

Then:
$$
R_2 \setminus R_1 = \bigcup_{i=1}^{n} (S_i^{-} \cup S_i^{+})
$$

This gives at most $2n$ disjoint rectangles (using the convention that empty intervals contribute $\emptyset$).

**Verification of disjointness:** For $i \neq j$, the slabs $S_i^{-}$, $S_i^{+}$, $S_j^{-}$, $S_j^{+}$ differ in the coordinates where they extend beyond $R_1$, ensuring disjointness.

The key point: each slab is a product of intervals, hence a rectangle in $\mathcal{R}_n$, and they are pairwise disjoint. ✓

**Note (alternative semiring definition).** Some texts define a semiring by requiring that for all $A,B\in\mathcal{R}_n$ there exist finitely many disjoint $C_i\in\mathcal{R}_n$ with $A\setminus B=\bigsqcup_i C_i$. This reduces to the nested case above by writing $A\setminus B = A\setminus(A\cap B)$, with $A\cap B\in\mathcal{R}_n$ by closure under intersection.

**Conclusion:** $\mathcal{R}_n$ satisfies all three properties of a semiring. $\square$

---

### **Exercise 2: The Algebra Generated by $\mathcal{R}_n$**

**Statement:** Let $\mathcal{A}(\mathcal{R}_n)$ denote the Boolean algebra generated by the semiring $\mathcal{R}_n$ of rectangles in $\mathbb{R}^n$. Verify that this algebra exists and contains all finite disjoint unions of rectangles.

**Solution:**

The construction of $\mathcal{A}(\mathcal{R}_n)$ proceeds in stages:

**Stage 1: Semiring $\mathcal{R}_n$**

Start with the semiring of half-open rectangles, which is closed under finite intersections and has the property that set differences decompose into finite disjoint unions of rectangles (Exercise 1).

**Stage 2: Finite Unions**

Form the collection $\mathcal{F}$ of all finite disjoint unions of rectangles:
$$
\mathcal{F} = \left\{ \bigcup_{k=1}^{m} R_k \;\Big|\; m \in \mathbb{N}, \, R_k \in \mathcal{R}_n, \, R_i \cap R_j = \emptyset \text{ for } i \neq j \right\}
$$

This collection contains all "elementary sets" but is not yet an algebra (it lacks closure under complementation).

**Stage 3: Boolean Closure**

Define $\mathcal{A}(\mathcal{R}_n)$ as the smallest collection containing $\mathcal{R}_n$ that is closed under:
- Finite unions: $A, B \in \mathcal{A} \Rightarrow A \cup B \in \mathcal{A}$
- Finite intersections: $A, B \in \mathcal{A} \Rightarrow A \cap B \in \mathcal{A}$
- Set differences: $A, B \in \mathcal{A} \Rightarrow A \setminus B \in \mathcal{A}$

**Lemma 2.1 (Folland §1.3, Theorem 1.6).** Let $\mathcal{S}$ be a semiring on $X$. Then the collection of all finite Boolean combinations (formed by finite applications of $\cup, \cap, \setminus$) of sets in $\mathcal{S}$ forms an algebra, denoted $\mathcal{A}(\mathcal{S})$.

*Proof sketch:* The verification that Boolean combinations form an algebra requires showing:
1. $X \in \mathcal{A}(\mathcal{S})$: This follows by expressing $X$ as a limit of increasing finite unions of rectangles (e.g., $X = \bigcup_{N=1}^{\infty} \prod_{i=1}^{n} (-N, N]$), but for the algebra we need only finite approximations or we take $X$ as a primitive element.

   **Corrected approach:** For $\mathbb{R}^n$, the whole space is *not* a finite union of rectangles. However, we can define the algebra differently: $\mathcal{A}(\mathcal{R}_n)$ consists of all sets that can be expressed as finite unions of differences of rectangles. With this characterization, bounded sets are easily represented, and unbounded sets require more care.

   For Carathéodory's application, what matters is:
   - $\mathcal{R}_n \subseteq \mathcal{A}(\mathcal{R}_n)$ (the algebra contains all rectangles)
   - $\mathcal{A}(\mathcal{R}_n)$ is closed under finite unions, finite intersections, and complements
   - Every set in $\mathcal{A}(\mathcal{R}_n)$ can be expressed using finite Boolean operations on rectangles

2. Closure under complement: For $A \in \mathcal{A}$, the complement $A^c$ can be expressed using De Morgan's laws applied to the Boolean representation of $A$.

3. Closure under finite unions: This holds by the definition of Boolean combinations.

The detailed verification is technical and not immediately illuminating for the Carathéodory construction. We refer to Folland §1.3 for the complete proof. □

**For our purposes:** We take as given that the algebra $\mathcal{A}(\mathcal{R}_n)$ exists with the following properties:
- It contains all finite disjoint unions of rectangles: $\mathcal{F} \subseteq \mathcal{A}(\mathcal{R}_n)$
- It is closed under finite Boolean operations
- It generates the Borel $\sigma$-algebra: $\sigma(\mathcal{A}(\mathcal{R}_n)) = \mathcal{B}(\mathbb{R}^n)$

**Remark:** The precise characterization of $\mathcal{A}(\mathcal{R}_n)$ involves sets that are finite unions of "generalized rectangles" (differences of rectangles). For Carathéodory's theorem, the existence of such an algebra containing the semiring is what matters, not its exact form.

---

## **Exercise 3: Pre-Measure of Volume is Well-Defined**

**Statement:** On the semiring $\mathcal{R}_n$, define:
$$
\mu_0\left(\prod_{i=1}^{n} (a_i, b_i]\right) = \prod_{i=1}^{n} (b_i - a_i)
$$
Extend this to the algebra $\mathcal{A}(\mathcal{R}_n)$ by defining, for a finite disjoint union $A = \bigcup_{k=1}^{m} R_k$ with $R_k \in \mathcal{R}_n$:
$$
\mu_0(A) = \sum_{k=1}^{m} \mu_0(R_k)
$$
Prove that $\mu_0$ is well-defined on the algebra (i.e., if a set has two different representations as finite disjoint unions of rectangles, the two values of $\mu_0$ agree).

**Proof:**

**Preliminary observation:** Before showing well-definedness, we must verify that finite additivity on the semiring $\mathcal{R}_n$ holds. That is, if $R = \bigsqcup_{k=1}^{m} R_k$ is a disjoint union of rectangles $R, R_1, \ldots, R_m \in \mathcal{R}_n$, then:
$$
\mu_0(R) = \sum_{k=1}^{m} \mu_0(R_k)
$$

This is a geometric fact about volumes in $\mathbb{R}^n$. For $n=1$, it is immediate from the additivity of length. For $n > 1$, it follows by induction on dimension (using Fubini-type arguments for finite sums, which are elementary).

**Main proof of well-definedness:**

Suppose $A$ has two representations:
$$
A = \bigcup_{k=1}^{m} R_k = \bigcup_{j=1}^{\ell} S_j
$$
where both unions are disjoint and $R_k, S_j \in \mathcal{R}_n$.

We must show:
$$
\sum_{k=1}^{m} \mu_0(R_k) = \sum_{j=1}^{\ell} \mu_0(S_j)
$$

**Step 1: Refine to a common partition.**

For each $k, j$, the set $R_k \cap S_j$ is either a rectangle (by closure of $\mathcal{R}_n$ under intersections, Exercise 1) or empty.

Define:
$$
T_{k,j} = R_k \cap S_j
$$

Then $\{T_{k,j}\}_{k,j}$ forms a partition of $A$ into disjoint rectangles (or empty sets).

**Step 2: Express each $R_k$ as a union of $T_{k,j}$.**

For each $k$:
$$
R_k = R_k \cap A = R_k \cap \left(\bigcup_{j=1}^{\ell} S_j\right) = \bigcup_{j=1}^{\ell} (R_k \cap S_j) = \bigcup_{j=1}^{\ell} T_{k,j}
$$

This union is disjoint. Since each $T_{k,j} \in \mathcal{R}_n$ (or is empty), and we have established finite additivity on $\mathcal{R}_n$ above:
$$
\mu_0(R_k) = \sum_{j=1}^{\ell} \mu_0(T_{k,j})
$$

**Step 3: Sum over all $k$.**

$$
\sum_{k=1}^{m} \mu_0(R_k) = \sum_{k=1}^{m} \sum_{j=1}^{\ell} \mu_0(T_{k,j}) = \sum_{k,j} \mu_0(T_{k,j})
$$

**Step 4: By symmetry, express each $S_j$ similarly.**

$$
S_j = \bigcup_{k=1}^{m} T_{k,j}
$$
$$
\mu_0(S_j) = \sum_{k=1}^{m} \mu_0(T_{k,j})
$$
$$
\sum_{j=1}^{\ell} \mu_0(S_j) = \sum_{j=1}^{\ell} \sum_{k=1}^{m} \mu_0(T_{k,j}) = \sum_{k,j} \mu_0(T_{k,j})
$$

**Step 5: Conclusion.**

Both sums equal $\sum_{k,j} \mu_0(T_{k,j})$, so:
$$
\sum_{k=1}^{m} \mu_0(R_k) = \sum_{j=1}^{\ell} \mu_0(S_j)
$$

Thus $\mu_0$ is well-defined on finite disjoint unions. $\square$

**Remark:** The extension from $\mathcal{R}_n$ to $\mathcal{A}(\mathcal{R}_n)$ uses finite additivity on the semiring as a prerequisite. This circularity is resolved by first establishing finite additivity as a geometric property of Euclidean volume, then using well-definedness to extend the function to the algebra.

---

## **Exercise 4: Outer Measure is Subadditive (Detailed Verification)**

**Statement:** Let $\mu^*$ be the outer measure constructed from a pre-measure $\mu_0$ on an algebra $\mathcal{A}$. Prove that for any countable collection $\{E_n\}_{n=1}^{\infty}$ of subsets of $X$:
$$
\mu^*\left(\bigcup_{n=1}^{\infty} E_n\right) \leq \sum_{n=1}^{\infty} \mu^*(E_n)
$$

**Proof:** (This proof was sketched in Day 4 main content; we provide full details here.)

**Case 1:** If $\sum_{n=1}^{\infty} \mu^*(E_n) = \infty$, the inequality is trivially true.

**Case 2:** Assume $\sum_{n=1}^{\infty} \mu^*(E_n) < \infty$.

Fix $\varepsilon > 0$. For each $n \in \mathbb{N}$, by the definition of infimum in the outer measure:
$$
\mu^*(E_n) = \inf \left\{ \sum_{k=1}^{\infty} \mu_0(A_{n,k}) \;\Big|\; A_{n,k} \in \mathcal{A}, \, E_n \subseteq \bigcup_{k=1}^{\infty} A_{n,k} \right\}
$$

there exists a cover $\{A_{n,k}\}_{k=1}^{\infty} \subseteq \mathcal{A}$ with $E_n \subseteq \bigcup_{k=1}^{\infty} A_{n,k}$ such that:
$$
\sum_{k=1}^{\infty} \mu_0(A_{n,k}) \leq \mu^*(E_n) + \frac{\varepsilon}{2^n}
$$

**Step 1: Construct a countable cover of $\bigcup_{n=1}^{\infty} E_n$.**

Define:
$$
E = \bigcup_{n=1}^{\infty} E_n
$$

For each $n$, we have $E_n \subseteq \bigcup_{k=1}^{\infty} A_{n,k}$. Therefore:
$$
E = \bigcup_{n=1}^{\infty} E_n \subseteq \bigcup_{n=1}^{\infty} \bigcup_{k=1}^{\infty} A_{n,k}
$$

The collection $\{A_{n,k}\}_{n,k=1}^{\infty}$ is a countable cover of $E$ (it is a double sequence indexed by $(n,k) \in \mathbb{N} \times \mathbb{N}$, which is countable).

**Step 2: Compute the total measure of the cover.**

$$
\sum_{n=1}^{\infty} \sum_{k=1}^{\infty} \mu_0(A_{n,k}) \leq \sum_{n=1}^{\infty} \left(\mu^*(E_n) + \frac{\varepsilon}{2^n}\right) = \sum_{n=1}^{\infty} \mu^*(E_n) + \varepsilon \sum_{n=1}^{\infty} \frac{1}{2^n} = \sum_{n=1}^{\infty} \mu^*(E_n) + \varepsilon
$$

**Step 3: Apply the definition of outer measure.**

Since $\{A_{n,k}\}$ is a cover of $E$, by the definition of $\mu^*(E)$ as an infimum over all covers:
$$
\mu^*(E) \leq \sum_{n=1}^{\infty} \sum_{k=1}^{\infty} \mu_0(A_{n,k}) \leq \sum_{n=1}^{\infty} \mu^*(E_n) + \varepsilon
$$

**Step 4: Let $\varepsilon \to 0$.**

Since the inequality holds for all $\varepsilon > 0$:
$$
\mu^*(E) \leq \sum_{n=1}^{\infty} \mu^*(E_n)
$$

This completes the proof. $\square$

---

## **Exercise 5: Verification of Carathéodory's Criterion for Elementary Sets**

**Statement:** Let $\mu^*$ be the outer measure constructed from a pre-measure $\mu_0$ on an algebra $\mathcal{A}$. Prove that every set $A \in \mathcal{A}$ is $\mu^*$-measurable.

**Proof:** (This is Theorem 1.10(1) from Day 4; we provide a detailed, step-by-step verification here.)

Let $A \in \mathcal{A}$. We must show that for any test set $T \subseteq X$:
$$
\mu^*(T) = \mu^*(T \cap A) + \mu^*(T \cap A^c) \tag{*}
$$

**Direction 1: "$\leq$" by subadditivity.**

By countable subadditivity of $\mu^*$:
$$
\mu^*(T) = \mu^*(T \cap A \cup T \cap A^c) \leq \mu^*(T \cap A) + \mu^*(T \cap A^c)
$$

This holds for any outer measure, without any assumptions on $A$.

**Direction 2: "$\geq$" is the hard part.**

We must show:
$$
\mu^*(T) \geq \mu^*(T \cap A) + \mu^*(T \cap A^c)
$$

Fix $\varepsilon > 0$. By the definition of outer measure, there exists a cover $\{A_n\}_{n=1}^{\infty} \subseteq \mathcal{A}$ with $T \subseteq \bigcup_{n=1}^{\infty} A_n$ such that:
$$
\sum_{n=1}^{\infty} \mu_0(A_n) \leq \mu^*(T) + \varepsilon
$$

**Key observation:** Since $A \in \mathcal{A}$ and $\mathcal{A}$ is an algebra, for each $n$ we have:
- $A_n \cap A \in \mathcal{A}$
- $A_n \cap A^c \in \mathcal{A}$

These two sets are disjoint and their union is $A_n$. By additivity of $\mu_0$ on disjoint sets in $\mathcal{A}$ (which follows from the definition of pre-measure):
$$
\mu_0(A_n) = \mu_0(A_n \cap A) + \mu_0(A_n \cap A^c) \tag{**}
$$

**Step 1: Construct covers for $T \cap A$ and $T \cap A^c$.**

We have:
$$
T \cap A \subseteq \left(\bigcup_{n=1}^{\infty} A_n\right) \cap A = \bigcup_{n=1}^{\infty} (A_n \cap A)
$$

Thus $\{A_n \cap A\}_{n=1}^{\infty}$ is a cover of $T \cap A$ by sets in $\mathcal{A}$.

Similarly, $\{A_n \cap A^c\}_{n=1}^{\infty}$ is a cover of $T \cap A^c$.

**Step 2: Apply definition of outer measure.**

By the definition of $\mu^*$ as an infimum over covers:
$$
\mu^*(T \cap A) \leq \sum_{n=1}^{\infty} \mu_0(A_n \cap A)
$$
$$
\mu^*(T \cap A^c) \leq \sum_{n=1}^{\infty} \mu_0(A_n \cap A^c)
$$

**Step 3: Add the inequalities.**

$$
\mu^*(T \cap A) + \mu^*(T \cap A^c) \leq \sum_{n=1}^{\infty} \mu_0(A_n \cap A) + \sum_{n=1}^{\infty} \mu_0(A_n \cap A^c)
$$

Using (**):
$$
= \sum_{n=1}^{\infty} (\mu_0(A_n \cap A) + \mu_0(A_n \cap A^c)) = \sum_{n=1}^{\infty} \mu_0(A_n) \leq \mu^*(T) + \varepsilon
$$

**Step 4: Let $\varepsilon \to 0$.**

Since the inequality holds for all $\varepsilon > 0$:
$$
\mu^*(T \cap A) + \mu^*(T \cap A^c) \leq \mu^*(T)
$$

**Conclusion:**

Combining both directions:
$$
\mu^*(T) = \mu^*(T \cap A) + \mu^*(T \cap A^c)
$$

Thus $A \in \mathcal{M}$, the $\sigma$-algebra of $\mu^*$-measurable sets. $\square$

---

## **Exercise 6: Uniqueness of Lebesgue Measure on $\mathcal{B}(\mathbb{R})$**

**Statement:** Let $\mu$ and $\nu$ be two measures on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ such that:
1. $\mu((a, b]) = \nu((a, b]) = b - a$ for all $a < b$
2. Both $\mu$ and $\nu$ are $\sigma$-finite

Prove that $\mu = \nu$ on $\mathcal{B}(\mathbb{R})$.

**Proof:** (This uses the Uniqueness of Extension Theorem, stated without proof in Day 4.)

**Step 1: Identify the algebra.**

Let $\mathcal{A}$ be the algebra of finite disjoint unions of half-open intervals $(a, b]$. Both $\mu$ and $\nu$ agree on this algebra by hypothesis.

**Step 2: $\sigma$-algebra generation.**

The Borel $\sigma$-algebra $\mathcal{B}(\mathbb{R})$ is generated by open intervals $(a, b)$. Since:
$$
(a, b) = \bigcup_{n=1}^{\infty} (a, b - 1/n]
$$
and each $(a, b - 1/n]$ is in the algebra (or can be approximated by sets in the algebra), we have:
$$
\mathcal{B}(\mathbb{R}) = \sigma(\mathcal{A})
$$

**Step 3: Apply Uniqueness Theorem.**

**Theorem (Uniqueness of Extension, Folland 1.14):** Let $\mathcal{A}$ be an algebra on $X$ generating the $\sigma$-algebra $\mathcal{F} = \sigma(\mathcal{A})$. Let $\mu, \nu$ be two measures on $(X, \mathcal{F})$ such that:
1. $\mu(A) = \nu(A)$ for all $A \in \mathcal{A}$
2. There exist sets $E_n \in \mathcal{A}$ with $X = \bigcup_{n=1}^{\infty} E_n$ and $\mu(E_n) = \nu(E_n) < \infty$ ($\sigma$-finiteness)

Then $\mu = \nu$ on $\mathcal{F}$.

**Application to our problem:**

- $X = \mathbb{R}$, $\mathcal{F} = \mathcal{B}(\mathbb{R})$
- $\mu$ and $\nu$ agree on $\mathcal{A}$ (by hypothesis)
- $\sigma$-finiteness: $\mathbb{R} = \bigcup_{n=1}^{\infty} (-n, n]$, and $\mu((-n, n]) = \nu((-n, n]) = 2n < \infty$

By the uniqueness theorem, $\mu = \nu$ on $\mathcal{B}(\mathbb{R})$. $\square$

**Remark:** This proves that Lebesgue measure is *uniquely* determined by the requirement that intervals have measure equal to their length. No other measure on $\mathcal{B}(\mathbb{R})$ satisfies this property (along with $\sigma$-finiteness).

---

## **Exercise 7: Non-Measurable Sets (Preview of Vitali Set)**

**Statement:** Using the axiom of choice, construct a subset $V \subseteq [0,1]$ that is not Lebesgue measurable.

**Proof:** (This is the famous **Vitali set**, constructed in 1905.)

**Step 1: Define an equivalence relation on $[0,1]$.**

For $x, y \in [0,1]$, define:
$$
x \sim y \quad \text{if and only if} \quad x - y \in \mathbb{Q}
$$

This is an equivalence relation:
- Reflexive: $x - x = 0 \in \mathbb{Q}$
- Symmetric: If $x - y \in \mathbb{Q}$, then $y - x = -(x-y) \in \mathbb{Q}$
- Transitive: If $x - y \in \mathbb{Q}$ and $y - z \in \mathbb{Q}$, then $x - z = (x-y) + (y-z) \in \mathbb{Q}$

**Step 2: Partition $[0,1]$ into equivalence classes.**

Each equivalence class is a set of the form:
$$
[x] = \{y \in [0,1] : y - x \in \mathbb{Q}\}
$$

The equivalence classes partition $[0,1]$. Note that each class is countable (since $\mathbb{Q}$ is countable), but there are uncountably many classes (since $[0,1]$ is uncountable).

**Step 3: Use the axiom of choice to select a representative from each class.**

By the **axiom of choice**, there exists a set $V \subseteq [0,1]$ such that $V$ contains exactly one element from each equivalence class.

This set $V$ is called a **Vitali set**.

**Step 4: Prove that $V$ is not Lebesgue measurable.**

Enumerate the rationals in $(-1, 1)$ as $\{q_n\}_{n=1}^{\infty}$. For each $n$, define:
$$
V_n = V + q_n = \{v + q_n : v \in V\}
$$
where addition is taken modulo arithmetic if necessary to stay in $[0,1]$ (or we can work in $\mathbb{R}/\mathbb{Z}$, the circle). We shall work on $\mathbb{R}/\mathbb{Z}$ to avoid endpoint ambiguities; equivalently, restrict to $[0,1)$ with addition modulo $1$ and rationals in $(-1,1)$.

**Key observations:**

1. **Disjoint translates:** If $n \neq m$, then $V_n \cap V_m = \emptyset$.

   *Proof:* Suppose $v_1 + q_n = v_2 + q_m$ for some $v_1, v_2 \in V$. Then $v_1 - v_2 = q_m - q_n \in \mathbb{Q}$, so $v_1 \sim v_2$. But $V$ contains at most one element from each equivalence class, so $v_1 = v_2$, which implies $q_n = q_m$, contradicting $n \neq m$.

2. **Cover:** Every element of $[0,1]$ belongs to some $V_n$.

   *Proof:* For any $x \in [0,1]$, there exists $v \in V$ such that $x \sim v$, i.e., $x - v = q$ for some $q \in \mathbb{Q}$. If $q \in (-1, 1)$, then $q = q_n$ for some $n$, so $x = v + q_n \in V_n$.

**Step 5: Derive a contradiction.**

Assume $V$ is Lebesgue measurable. Then each $V_n$ is also measurable (Lebesgue measure is translation-invariant), and $\lambda(V_n) = \lambda(V)$ for all $n$.

By countable additivity:
$$
\lambda\left(\bigcup_{n=1}^{\infty} V_n\right) = \sum_{n=1}^{\infty} \lambda(V_n) = \sum_{n=1}^{\infty} \lambda(V)
$$

But:
- If $\lambda(V) = 0$, then $\lambda(\bigcup V_n) = 0$. However, $\bigcup V_n \supseteq [0,1]$ (by observation 2), so $\lambda(\bigcup V_n) \geq 1$. Contradiction.
- If $\lambda(V) > 0$, then $\sum_{n=1}^{\infty} \lambda(V) = \infty$. However, $\bigcup V_n \subseteq [-1, 2]$ (by construction of the translates), so $\lambda(\bigcup V_n) \leq 3 < \infty$. Contradiction.

Therefore, $V$ cannot be Lebesgue measurable. $\square$

**Remark:** The Vitali set is not Borel-measurable either. However, it *is* Carathéodory-measurable with respect to some outer measures (e.g., the counting measure). The key point: Lebesgue measure cannot be extended to a translation-invariant measure on *all* subsets of $\mathbb{R}$—some sets must remain non-measurable.

---

## **Exercise 8: Connecting Carathéodory to RL: Transition Kernels**

**Statement:** In a continuous-state MDP, suppose the dynamics are given by:
$$
S_{t+1} = f(S_t, a_t) + \varepsilon_t, \quad \varepsilon_t \sim \mathcal{N}(0, \sigma^2 I_n)
$$
where $f: \mathbb{R}^n \times \mathcal{A} \to \mathbb{R}^n$ is a measurable function and $\mathcal{N}(0, \sigma^2 I_n)$ is the Gaussian distribution on $\mathbb{R}^n$.

Explain how the transition kernel $P(\cdot | s,a): \mathcal{B}(\mathbb{R}^n) \to [0,1]$ is constructed using the Carathéodory extension.

**Solution:**

**Step 1: Define the kernel on rectangles.**

For a rectangle $R = \prod_{i=1}^{n} (a_i, b_i] \in \mathcal{R}_n$, define:
$$
P(R | s, a) = \mathbb{P}(f(s,a) + \varepsilon \in R)
$$
where $\varepsilon \sim \mathcal{N}(0, \sigma^2 I_n)$.

**Notation clarification:** For a set $R \subseteq \mathbb{R}^n$ and a point $x \in \mathbb{R}^n$, we define the **translated set**:
$$
R - x := \{z \in \mathbb{R}^n : z = y - x \text{ for some } y \in R\}
$$

Equivalently:
$$
R - x = \{z \in \mathbb{R}^n : z + x \in R\}
$$

Thus:
$$
P(R | s, a) = \mathbb{P}(\varepsilon \in R - f(s,a))
$$

This is computed via the Gaussian density:
$$
P(R | s, a) = \int_{R - f(s,a)} \frac{1}{(2\pi\sigma^2)^{n/2}} \exp\left(-\frac{\|\varepsilon\|^2}{2\sigma^2}\right) d\varepsilon
$$

Equivalently, by change of variables $y = f(s,a) + \varepsilon$ (so $\varepsilon = y - f(s,a)$):
$$
P(R | s, a) = \int_{R} \frac{1}{(2\pi\sigma^2)^{n/2}} \exp\left(-\frac{\|y - f(s,a)\|^2}{2\sigma^2}\right) dy
$$

**Step 2: Extend to the algebra.**

For $A \in \mathcal{A}(\mathcal{R}_n)$ (a finite disjoint union of rectangles), extend by additivity:
$$
P(A | s, a) = \sum_{k} P(R_k | s, a)
$$
where $A = \bigcup_k R_k$ is the disjoint union.

**Verification of pre-measure:** We must check countable additivity on $\mathcal{A}$. For disjoint $\{A_n\} \subseteq \mathcal{A}$ with $\bigcup A_n \in \mathcal{A}$:
$$
P\left(\bigcup_{n=1}^{\infty} A_n \;\Big|\; s, a\right) = \sum_{n=1}^{\infty} P(A_n | s, a)
$$

This follows from the fact that the Gaussian measure on $\mathbb{R}^n$ is a probability measure, hence countably additive.

**Step 3: Apply Carathéodory extension.**

Define the outer measure:
$$
P^*(E | s, a) = \inf \left\{ \sum_{k=1}^{\infty} P(A_k | s, a) \;\Big|\; A_k \in \mathcal{A}, \, E \subseteq \bigcup_{k=1}^{\infty} A_k \right\}
$$

By Carathéodory's theorem, the collection of $P^*(\cdot | s,a)$-measurable sets is a $\sigma$-algebra containing $\mathcal{A}$. Since $\mathcal{B}(\mathbb{R}^n) = \sigma(\mathcal{A})$, we have $\mathcal{B}(\mathbb{R}^n) \subseteq \mathcal{M}$.

**Step 4: Restrict to Borel sets.**

Define $P(\cdot | s, a) = P^*(\cdot | s, a)|_{\mathcal{B}(\mathbb{R}^n)}$.

This is a probability measure on $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$, which is the transition kernel for the MDP.

**Key insight:** The Carathéodory construction ensures that:
1. The kernel is well-defined on all Borel sets (not just rectangles)
2. It satisfies countable additivity (essential for Bellman equation)
3. It is uniquely determined by the dynamics $f$ and noise distribution $\mathcal{N}(0, \sigma^2 I_n)$

Without Carathéodory, we would have no rigorous way to extend the kernel from elementary sets to the full Borel $\sigma$-algebra.

---

**Numerical Example: Linear Dynamics in One Dimension**

Consider a one-dimensional continuous-state MDP with dynamics:
$$
S_{t+1} = 0.8 S_t + a_t + \varepsilon_t, \quad \varepsilon_t \sim \mathcal{N}(0, 1)
$$

**Part (a): Computing the kernel for an interval**

Fix $s = 0$ and $a = 0$. Then $f(s,a) = 0.8 \cdot 0 + 0 = 0$, so $S_{t+1} \sim \mathcal{N}(0, 1)$.

For the rectangle $R = (-1, 1]$, we compute:
$$
P((-1, 1] | 0, 0) = \int_{-1}^{1} \frac{1}{\sqrt{2\pi}} e^{-y^2/2} dy = \Phi(1) - \Phi(-1) \approx 0.6826
$$

where $\Phi$ is the standard normal CDF.

**Part (b): Extension to non-elementary Borel sets**

To illustrate the power of Carathéodory's extension to exotic Borel sets, consider the Cantor set $C \subset [0,1]$ (a Borel set that is not an interval). We cannot compute $P(C | 0, 0)$ directly from the definition on rectangles. However, by Carathéodory's theorem:

1. Approximate $C$ from outside by covering with intervals: $C \subseteq \bigcup_{k=1}^{\infty} I_k$ where $I_k$ are intervals
2. Compute $P^*(C | 0, 0) = \inf \{\sum_k P(I_k | 0, 0)\}$
3. Since $C$ is Borel-measurable, $P^*(C | 0, 0) = P(C | 0, 0)$

In this case, $C$ has Lebesgue measure zero, so $P(C | 0, 0) = 0$ (since the Gaussian measure is absolutely continuous with respect to Lebesgue measure).

This example illustrates how Carathéodory extends the transition kernel from simple rectangles to all Borel sets, including exotic constructions like the Cantor set. $\square$

---

## **Reflection: What We Have Achieved**

### **Mathematical Insight**

The Carathéodory extension theorem is a triumph of mathematical engineering. It provides a **canonical procedure** for constructing measures:
1. Start with a simple, intuitive notion (length, area, volume on elementary sets)
2. Extend to an outer measure via an infimum construction
3. Characterize measurable sets via an additivity criterion
4. Restrict to obtain a true measure

This pattern recurs throughout mathematics: in probability (constructing distributions from CDFs), in functional analysis (extending linear functionals), and in differential geometry (constructing volume forms).

### **RL Connection**

The Carathéodory construction is not abstract formalism—it is the **rigorous foundation** ensuring that:
- Transition kernels $P(\cdot | s,a)$ are well-defined probability measures on continuous state spaces
- Value functions $V: \mathcal{S} \to \mathbb{R}$ are measurable, making expectations $\mathbb{E}_{s' \sim P(\cdot|s,a)}[V(s')]$ computable
- The Bellman operator $TV = R + \gamma P V$ is a well-defined mapping on function spaces

Without this foundation, the entire theory of continuous-state MDPs would be built on sand.

### **Open Questions for Further Investigation**

1. **Necessity of Axiom of Choice:** The Vitali set construction uses the axiom of choice. Is there a model of set theory (ZF without choice) in which all subsets of $\mathbb{R}$ are Lebesgue measurable? (Answer: Yes, in Solovay's model. But then other desirable properties fail.)

2. **Carathéodory for Infinite-Dimensional Spaces:** Can we construct Lebesgue-type measures on infinite-dimensional spaces (e.g., Banach spaces, path spaces)? This leads to Gaussian measures on Hilbert spaces and Wiener measure—essential for stochastic control (Week 40).

3. **Non-Borel Policies:** If a policy $\pi: \mathcal{S} \to \mathcal{A}$ is not Borel-measurable, can we still define $V^\pi$? In general, no—expectations may not exist. This shows that measurability is not a technicality but a **physical constraint** on realizable policies.

---

**End of Day 4 Exercises**

Tomorrow (Day 5), we synthesize the week's material with coding implementations and reflect on the connection between $\sigma$-algebras and observability in RL.
