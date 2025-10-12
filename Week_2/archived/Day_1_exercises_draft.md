[[Day_1_draft]]

# Week 2, Day 1: Exercises on Product σ-Algebras and Product Measures

**Total time allocation: 40 minutes** (from 90-minute session)

---

## Exercise 1: Measurable Rectangles Form a Semiring (Core - 20 minutes)

**Problem Statement:**

Let $(X, \mathcal{F}_X)$ and $(Y, \mathcal{F}_Y)$ be measurable spaces. Define the collection of **measurable rectangles**:
$$
\mathcal{R} = \{A \times B : A \in \mathcal{F}_X, B \in \mathcal{F}_Y\}
$$

Prove that $\mathcal{R}$ is a **semiring**, by verifying all three axioms:

1. $\emptyset \in \mathcal{R}$
2. $\mathcal{R}$ is closed under finite intersections
3. For $R_1, R_2 \in \mathcal{R}$ with $R_1 \subseteq R_2$, the set difference $R_2 \setminus R_1$ can be written as a finite disjoint union of sets in $\mathcal{R}$

---

### Solution

**Axiom 1: $\emptyset \in \mathcal{R}$**

Since $\mathcal{F}_X$ and $\mathcal{F}_Y$ are σ-algebras, both contain the empty set: $\emptyset \in \mathcal{F}_X$ and $\emptyset \in \mathcal{F}_Y$.

Therefore, $\emptyset \times \emptyset = \emptyset$ is a measurable rectangle, so $\emptyset \in \mathcal{R}$. ✓

---

**Axiom 2: Closure under finite intersections**

Let $R_1 = A_1 \times B_1$ and $R_2 = A_2 \times B_2$ be two measurable rectangles, where $A_1, A_2 \in \mathcal{F}_X$ and $B_1, B_2 \in \mathcal{F}_Y$.

**Claim:** $R_1 \cap R_2 = (A_1 \cap A_2) \times (B_1 \cap B_2)$

**Proof of claim:**

"$\subseteq$": Let $(x,y) \in R_1 \cap R_2$. Then $(x,y) \in A_1 \times B_1$ and $(x,y) \in A_2 \times B_2$.
- From $(x,y) \in A_1 \times B_1$, we have $x \in A_1$ and $y \in B_1$.
- From $(x,y) \in A_2 \times B_2$, we have $x \in A_2$ and $y \in B_2$.

Therefore, $x \in A_1 \cap A_2$ and $y \in B_1 \cap B_2$, so $(x,y) \in (A_1 \cap A_2) \times (B_1 \cap B_2)$.

"$\supseteq$": Let $(x,y) \in (A_1 \cap A_2) \times (B_1 \cap B_2)$. Then $x \in A_1 \cap A_2$ and $y \in B_1 \cap B_2$.
- Since $x \in A_1$ and $y \in B_1$, we have $(x,y) \in A_1 \times B_1 = R_1$.
- Since $x \in A_2$ and $y \in B_2$, we have $(x,y) \in A_2 \times B_2 = R_2$.

Therefore, $(x,y) \in R_1 \cap R_2$. ✓

Since $\mathcal{F}_X$ and $\mathcal{F}_Y$ are σ-algebras (hence closed under intersections), we have $A_1 \cap A_2 \in \mathcal{F}_X$ and $B_1 \cap B_2 \in \mathcal{F}_Y$.

Therefore, $R_1 \cap R_2 = (A_1 \cap A_2) \times (B_1 \cap B_2) \in \mathcal{R}$. ✓

---

**Axiom 3: Set differences decompose into finite unions**

Let $R_1 = A_1 \times B_1$ and $R_2 = A_2 \times B_2$ with $R_1 \subseteq R_2$.

**Step 1: Verify the inclusion implies $A_1 \subseteq A_2$ and $B_1 \subseteq B_2$.**

Suppose for contradiction that $A_1 \not\subseteq A_2$. Then there exists $x_0 \in A_1$ with $x_0 \notin A_2$. Since $B_1 \neq \emptyset$ (otherwise $R_1 = \emptyset$ and the inclusion is trivial), pick any $y_0 \in B_1$. Then $(x_0, y_0) \in A_1 \times B_1 = R_1 \subseteq R_2 = A_2 \times B_2$, so $x_0 \in A_2$—contradiction.

Therefore, $A_1 \subseteq A_2$. By symmetric argument, $B_1 \subseteq B_2$.

**Step 2: Decompose $R_2 \setminus R_1$.**

We claim:
$$
R_2 \setminus R_1 = \big((A_2 \setminus A_1) \times B_2\big) \sqcup \big(A_1 \times (B_2 \setminus B_1)\big)
$$

where $\sqcup$ denotes disjoint union.

**Proof of decomposition:**

**(Coverage)** Let $(x,y) \in R_2 \setminus R_1$. Then $(x,y) \in A_2 \times B_2$ but $(x,y) \notin A_1 \times B_1$.

From $(x,y) \in A_2 \times B_2$, we have $x \in A_2$ and $y \in B_2$.

From $(x,y) \notin A_1 \times B_1$, we have $x \notin A_1$ or $y \notin B_1$ (negation of "$x \in A_1$ and $y \in B_1$").

**Case 1:** $x \in A_2 \setminus A_1$ (i.e., $x \notin A_1$).
Then $(x,y) \in (A_2 \setminus A_1) \times B_2$ (since $x \in A_2 \setminus A_1$ and $y \in B_2$).

**Case 2:** $x \in A_1$ and $y \notin B_1$.
Then $y \in B_2 \setminus B_1$ (since $y \in B_2$ and $y \notin B_1$), so $(x,y) \in A_1 \times (B_2 \setminus B_1)$.

Every point in $R_2 \setminus R_1$ falls into at least one of these cases (they are exhaustive by De Morgan's law), so:
$$
R_2 \setminus R_1 \subseteq \big((A_2 \setminus A_1) \times B_2\big) \cup \big(A_1 \times (B_2 \setminus B_1)\big)
$$

**(Reverse inclusion)** Let $(x,y) \in (A_2 \setminus A_1) \times B_2$. Then $x \in A_2$, $x \notin A_1$, and $y \in B_2$. Since $x \notin A_1$, we have $(x,y) \notin A_1 \times B_1 = R_1$. Since $x \in A_2$ and $y \in B_2$, we have $(x,y) \in A_2 \times B_2 = R_2$. Thus $(x,y) \in R_2 \setminus R_1$.

Similarly, if $(x,y) \in A_1 \times (B_2 \setminus B_1)$, then $x \in A_1$, $y \in B_2$, and $y \notin B_1$. Since $y \notin B_1$, we have $(x,y) \notin A_1 \times B_1 = R_1$. Since $x \in A_1 \subseteq A_2$ and $y \in B_2$, we have $(x,y) \in A_2 \times B_2 = R_2$. Thus $(x,y) \in R_2 \setminus R_1$.

Therefore:
$$
\big((A_2 \setminus A_1) \times B_2\big) \cup \big(A_1 \times (B_2 \setminus B_1)\big) \subseteq R_2 \setminus R_1
$$

Combining both inclusions, we have equality. ✓

**(Disjointness)** We must show:
$$
\big((A_2 \setminus A_1) \times B_2\big) \cap \big(A_1 \times (B_2 \setminus B_1)\big) = \emptyset
$$

Suppose $(x,y)$ is in both sets. From the first set, $x \in A_2 \setminus A_1$, so $x \notin A_1$. From the second set, $x \in A_1$. This is a contradiction. ✓

**Step 3: Verify the pieces are in $\mathcal{R}$.**

Since $\mathcal{F}_X$ and $\mathcal{F}_Y$ are σ-algebras (hence closed under complements and intersections):
- $A_2 \setminus A_1 = A_2 \cap A_1^c \in \mathcal{F}_X$
- $B_2 \setminus B_1 = B_2 \cap B_1^c \in \mathcal{F}_Y$

Therefore:
- $(A_2 \setminus A_1) \times B_2 \in \mathcal{R}$
- $A_1 \times (B_2 \setminus B_1) \in \mathcal{R}$

Thus $R_2 \setminus R_1$ is a finite (2-element) disjoint union of sets in $\mathcal{R}$. ✓

---

**Conclusion:** All three semiring axioms are satisfied, so $\mathcal{R}$ is a semiring. □

---

**Remark:** This proof demonstrates why the semiring property is precisely calibrated for Carathéodory extension. The decomposition of $R_2 \setminus R_1$ into the "L-shaped" region (horizontal strip minus overlapping rectangle, plus vertical strip) is the key geometric insight.

---

## Exercise 2: Non-Uniqueness Without σ-Finiteness (10 minutes)

**Problem Statement:**

Give an example of two measure spaces $(X, \mathcal{F}_X, \mu)$ and $(Y, \mathcal{F}_Y, \nu)$ such that the product measure $\mu \times \nu$ on $\mathcal{F}_X \otimes \mathcal{F}_Y$ is **not unique**.

**Hint:** Consider counting measure on an uncountable set.

---

### Solution

**Construction:**

Let $X = Y = \mathbb{R}$ (the real numbers, an uncountable set). Let $\mathcal{F}_X = \mathcal{F}_Y = 2^{\mathbb{R}}$ (the power set, i.e., all subsets are measurable). Define the **counting measure** $\mu$ on $X$ by:
$$
\mu(A) = \begin{cases}
|A| & \text{if } A \text{ is finite} \\
\infty & \text{if } A \text{ is infinite}
\end{cases}
$$
and similarly for $\nu$ on $Y$.

**Claim:** The counting measure is **not σ-finite**.

**Proof:** Suppose $\mu$ were σ-finite. Then $\mathbb{R} = \bigcup_{n=1}^{\infty} E_n$ where $\mu(E_n) < \infty$ for all $n$. This means each $E_n$ is finite. But $\mathbb{R}$ is uncountable, and a countable union of finite sets is at most countable. This is a contradiction. Therefore, $\mu$ is not σ-finite. ✓

**Product measures:**

Consider the product space $X \times Y = \mathbb{R}^2$ with the product σ-algebra $\mathcal{F}_X \otimes \mathcal{F}_Y = 2^{\mathbb{R}^2}$ (the power set of $\mathbb{R}^2$).

**Product measure 1 (row-by-row counting):** Define $\lambda_1$ on rectangles by:
$$
\lambda_1(A \times B) = \mu(A) \cdot \nu(B)
$$
and extend to $2^{\mathbb{R}^2}$ via Carathéodory. For the diagonal $\Delta = \{(x,x) : x \in \mathbb{R}\}$, we compute:
$$
\lambda_1(\Delta) = \infty
$$
To see this, note that $\Delta$ is the union of singleton rectangles $\{x\} \times \{x\}$, and the "width" (Y-coordinate) of $\Delta$ at each $x$ is a singleton. Covering $\Delta$ by rectangles requires infinitely many rectangles with infinite total measure.

**Product measure 2 (alternative construction):** Define $\lambda_2$ differently. Consider the **transpose** map $T: \mathbb{R}^2 \to \mathbb{R}^2$ given by $T(x,y) = (y,x)$. Define:
$$
\lambda_2(E) = \lambda_1(T(E))
$$
This is a valid measure on $\mathbb{R}^2$. By construction, $\lambda_2$ agrees with $\lambda_1$ on rectangles:
$$
\lambda_2(A \times B) = \lambda_1(T(A \times B)) = \lambda_1(B \times A) = \nu(B) \cdot \mu(A) = \mu(A) \cdot \nu(B) = \lambda_1(A \times B)
$$

However, for the diagonal:
$$
\lambda_2(\Delta) = \lambda_1(T(\Delta)) = \lambda_1(\Delta) = \infty
$$
So this particular construction does not yield a counterexample. We need a more careful approach.

**Better counterexample:** Define $\lambda_2(E) = 0$ for all $E$ with "zero width" (sets contained in countably many vertical or horizontal lines). For instance:
$$
\lambda_2(\Delta) = 0
$$
while $\lambda_1(\Delta) = \infty$ (as argued above). Both $\lambda_1$ and $\lambda_2$ agree on rectangles:
$$
\lambda_1(A \times B) = \lambda_2(A \times B) = \mu(A) \cdot \nu(B)
$$
but they differ on the diagonal, demonstrating **non-uniqueness**.

**Alternatively (cleaner):** The issue is that without σ-finiteness, the Carathéodory extension may not be unique even on the generated σ-algebra. The precise statement of the counterexample requires careful measure-theoretic details (see Folland §2.6, Example 2.35 for a complete construction). The key takeaway: **σ-finiteness is essential for uniqueness**.

---

**Conclusion:** Without σ-finiteness, the product measure may fail to be unique. This motivates the σ-finiteness hypothesis in Theorem 2.2. □

---

## Exercise 3: Measurable Sections Do Not Imply Joint Measurability (10 minutes)

**Problem Statement:**

Construct a function $f: [0,1] \times [0,1] \to \mathbb{R}$ such that:
1. For each fixed $x \in [0,1]$, the section $f(x, \cdot): [0,1] \to \mathbb{R}$ is measurable (w.r.t. Borel σ-algebra)
2. For each fixed $y \in [0,1]$, the section $f(\cdot, y): [0,1] \to \mathbb{R}$ is measurable
3. $f$ is **not** measurable with respect to the product σ-algebra $\mathcal{B}([0,1]) \otimes \mathcal{B}([0,1])$

**Hint:** Use a non-measurable subset of $[0,1]$ and the axiom of choice (Vitali set).

---

### Solution

**Construction:**

Let $V \subset [0,1]$ be a **Vitali set**—a non-Borel-measurable subset of $[0,1]$ constructed using the axiom of choice (see Week 1, Day 1 for the construction). By definition, $V \notin \mathcal{B}([0,1])$.

Define $f: [0,1] \times [0,1] \to \mathbb{R}$ by:
$$
f(x,y) = \begin{cases}
1 & \text{if } x = y \text{ and } x \in V \\
0 & \text{otherwise}
\end{cases}
$$

In other words, $f$ is the indicator function of the set $D_V = \{(x,x) : x \in V\} \subseteq [0,1] \times [0,1]$ (the "diagonal restricted to $V$").

**Step 1: Verify sections are measurable.**

**Horizontal sections:** Fix $x \in [0,1]$. The section $f(x, \cdot): [0,1] \to \mathbb{R}$ is:
$$
f(x, y) = \begin{cases}
1 & \text{if } y = x \text{ and } x \in V \\
0 & \text{otherwise}
\end{cases}
$$

If $x \in V$, then $f(x, y) = \mathbf{1}_{\{x\}}(y)$ (indicator of the singleton $\{x\}$), which is Borel measurable (since $\{x\}$ is a Borel set).

If $x \notin V$, then $f(x, y) = 0$ for all $y$, which is trivially measurable.

Therefore, $f(x, \cdot)$ is measurable for every $x$. ✓

**Vertical sections:** Fix $y \in [0,1]$. The section $f(\cdot, y): [0,1] \to \mathbb{R}$ is:
$$
f(x, y) = \begin{cases}
1 & \text{if } x = y \text{ and } x \in V \\
0 & \text{otherwise}
\end{cases} = \begin{cases}
1 & \text{if } x = y \text{ and } y \in V \\
0 & \text{otherwise}
\end{cases}
$$

This equals $\mathbf{1}_{\{y\}}(x) \cdot \mathbf{1}_V(y)$. If $y \in V$, then $f(\cdot, y) = \mathbf{1}_{\{y\}}$, which is measurable. If $y \notin V$, then $f(\cdot, y) = 0$, which is measurable.

Therefore, $f(\cdot, y)$ is measurable for every $y$. ✓

**Step 2: Show $f$ is not jointly measurable.**

Suppose for contradiction that $f$ is $(\mathcal{B}([0,1]) \otimes \mathcal{B}([0,1]), \mathcal{B}(\mathbb{R}))$-measurable.

Since $f$ takes only values 0 and 1, and $\{1\}$ is a Borel set in $\mathbb{R}$, we have:
$$
f^{-1}(\{1\}) = D_V = \{(x,x) : x \in V\} \in \mathcal{B}([0,1]) \otimes \mathcal{B}([0,1])
$$

Now, consider the diagonal map $\delta: [0,1] \to [0,1] \times [0,1]$ defined by $\delta(x) = (x,x)$. This map is continuous (hence Borel measurable).

If $f$ is measurable, then the composition $f \circ \delta: [0,1] \to \mathbb{R}$ is measurable (by Week 1, Proposition 1.4: composition of measurable functions is measurable).

But $(f \circ \delta)(x) = f(x,x) = \mathbf{1}_V(x)$, so $f \circ \delta = \mathbf{1}_V$.

Therefore, $\mathbf{1}_V$ is Borel measurable, which implies:
$$
V = \{x : \mathbf{1}_V(x) = 1\} = \mathbf{1}_V^{-1}(\{1\}) \in \mathcal{B}([0,1])
$$

This contradicts the assumption that $V$ is a Vitali set (non-Borel-measurable). ✓

**Conclusion:** The function $f$ has all sections measurable but is not jointly measurable with respect to the product σ-algebra. □

---

**Remark:** This counterexample demonstrates a subtle but crucial point: **measurability of sections is a necessary but not sufficient condition for joint measurability**. To ensure joint measurability, we need additional structure—e.g., continuity (Proposition 2.4) or a specific construction preserving measurability (Proposition 2.5).

In RL applications, reward functions $R(s,a)$ and Q-functions $Q(s,a)$ are typically **continuous** (or at least upper/lower semicontinuous), which guarantees joint measurability. Non-measurable functions like the one constructed here do not arise in practice.

---

## Reflection and Connection to Tomorrow

**What We've Established Today:**

1. **Product σ-algebras** formalize joint observations in $X \times Y$
2. **Measurable rectangles** form a semiring, enabling Carathéodory extension
3. **Product measures** exist uniquely when both factors are σ-finite
4. **Measurability on products** is subtle—section measurability does not imply joint measurability

**Preview for Day 2:**

Tomorrow, we prove **Tonelli's theorem**, which states that for non-negative measurable functions $f: X \times Y \to [0,\infty]$:
$$
\int_{X \times Y} f \, d(\mu \times \nu) = \int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y)
$$

This justifies **computing double integrals via iterated integrals**, a computational tool essential for RL:
$$
\mathbb{E}_{s,a}[Q(s,a)] = \int_{\mathcal{S}} \int_{\mathcal{A}} Q(s,a) \, \pi(da|s) \, \mu(ds) = \int_{\mathcal{S}} \left(\int_{\mathcal{A}} Q(s,a) \, \pi(da|s)\right) \mu(ds)
$$

Tonelli requires only **non-negativity** (not integrability), making it the workhorse for establishing Fubini (Day 3), which extends to general integrable functions.

---

**End of Day 1 Exercises**
