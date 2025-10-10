[[Day_1_FINAL]]

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

From $(x,y) \notin A_1 \times B_1$, we have $\neg(x \in A_1 \land y \in B_1)$. By De Morgan's law, this is equivalent to $(x \notin A_1) \lor (y \notin B_1)$. Thus every point falls into at least one case:

**Case 1:** $x \notin A_1$ (and $x \in A_2$, so $x \in A_2 \setminus A_1$).
Then $(x,y) \in (A_2 \setminus A_1) \times B_2$ (since $x \in A_2 \setminus A_1$ and $y \in B_2$).

**Case 2:** $x \in A_1$ and $y \notin B_1$ (and $y \in B_2$, so $y \in B_2 \setminus B_1$).
Then $(x,y) \in A_1 \times (B_2 \setminus B_1)$.

Every point in $R_2 \setminus R_1$ falls into at least one of these cases, so:
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

## Exercise 2: Product σ-Algebra on Discrete Spaces (10 minutes)

**Problem Statement:**

Let $X = \{1, 2\}$ and $Y = \{a, b, c\}$ with $\mathcal{F}_X = 2^X$ (power set) and $\mathcal{F}_Y = 2^Y$.

(a) How many elements are in $\mathcal{F}_X \otimes \mathcal{F}_Y$?

(b) Show that the set $D = \{(1,a), (2,b)\}$ is in $\mathcal{F}_X \otimes \mathcal{F}_Y$ by expressing it as a finite union of measurable rectangles.

(c) Is every subset of $X \times Y$ in $\mathcal{F}_X \otimes \mathcal{F}_Y$? Justify.

---

### Solution

**(a) Number of elements in $\mathcal{F}_X \otimes \mathcal{F}_Y$:**

Since $\mathcal{F}_X = 2^X$ and $\mathcal{F}_Y = 2^Y$ are both power sets (all subsets are measurable), the product σ-algebra $\mathcal{F}_X \otimes \mathcal{F}_Y$ is the σ-algebra generated by all measurable rectangles.

**Claim:** $\mathcal{F}_X \otimes \mathcal{F}_Y = 2^{X \times Y}$ (the power set of $X \times Y$).

**Proof:** We must show $\mathcal{F}_X \otimes \mathcal{F}_Y \supseteq 2^{X \times Y}$ (since the reverse inclusion is automatic).

For any subset $E \subseteq X \times Y$, we can write:
$$
E = \bigcup_{(x,y) \in E} \{(x,y)\}
$$

Each singleton $\{(x,y)\}$ is a measurable rectangle: $\{(x,y)\} = \{x\} \times \{y\}$, where $\{x\} \in 2^X = \mathcal{F}_X$ and $\{y\} \in 2^Y = \mathcal{F}_Y$.

Since $\mathcal{F}_X \otimes \mathcal{F}_Y$ is a σ-algebra containing all measurable rectangles, it contains all singletons, hence all their countable unions. Thus $E \in \mathcal{F}_X \otimes \mathcal{F}_Y$ for every $E \subseteq X \times Y$. ✓

**Answer:** $X \times Y$ has $|X| \times |Y| = 2 \times 3 = 6$ elements. Therefore, $\mathcal{F}_X \otimes \mathcal{F}_Y = 2^{X \times Y}$ has $2^6 = 64$ elements.

---

**(b) Express $D = \{(1,a), (2,b)\}$ as a union of rectangles:**

We can write:
$$
D = \{(1,a), (2,b)\} = (\{1\} \times \{a\}) \cup (\{2\} \times \{b\})
$$

Both $\{1\} \times \{a\}$ and $\{2\} \times \{b\}$ are measurable rectangles (since $\{1\}, \{2\} \in \mathcal{F}_X$ and $\{a\}, \{b\} \in \mathcal{F}_Y$).

Since $\mathcal{F}_X \otimes \mathcal{F}_Y$ is a σ-algebra (hence closed under finite unions), we have:
$$
D = (\{1\} \times \{a\}) \cup (\{2\} \times \{b\}) \in \mathcal{F}_X \otimes \mathcal{F}_Y
$$

✓

---

**(c) Is every subset of $X \times Y$ measurable?**

**Answer:** Yes. As shown in part (a), when both $\mathcal{F}_X$ and $\mathcal{F}_Y$ are power sets, the product σ-algebra $\mathcal{F}_X \otimes \mathcal{F}_Y$ equals the power set of $X \times Y$. Therefore, every subset of $X \times Y$ is measurable. ✓

**Remark:** This is a special property of discrete spaces with the discrete σ-algebra (power set). For general σ-algebras (e.g., Borel σ-algebras on $\mathbb{R}$), the product σ-algebra is strictly smaller than the power set of the product space.

---

## Exercise 3: Measurable Sections Do Not Imply Joint Measurability (Advanced - Optional)

**Problem Statement:**

Construct a function $f: [0,1] \times [0,1] \to \mathbb{R}$ such that:
1. For each fixed $x \in [0,1]$, the section $f(x, \cdot): [0,1] \to \mathbb{R}$ is measurable (w.r.t. Borel σ-algebra)
2. For each fixed $y \in [0,1]$, the section $f(\cdot, y): [0,1] \to \mathbb{R}$ is measurable
3. $f$ is **not** measurable with respect to the product σ-algebra $\mathcal{B}([0,1]) \otimes \mathcal{B}([0,1])$

**Hint:** Use a non-measurable subset of $[0,1]$ and the axiom of choice (Vitali set).

---

### Solution

**Construction:**

Let $V \subset [0,1]$ be a **Vitali set**—a non-Borel-measurable subset of $[0,1]$ constructed using the axiom of choice. **Recall from Week 1, Day 4**: A Vitali set is constructed by choosing one representative from each equivalence class of $[0,1]$ under the relation $x \sim y \iff x - y \in \mathbb{Q}$. This requires the axiom of choice and produces a non-Lebesgue-measurable (hence non-Borel-measurable) set. By definition, $V \notin \mathcal{B}([0,1])$.

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

If $f$ is measurable, then the composition $f \circ \delta: [0,1] \to \mathbb{R}$ is measurable. This follows from the general principle (Week 1, Day 1): if $g: X \to Y$ is $(\mathcal{F}_X, \mathcal{F}_Y)$-measurable and $h: Y \to Z$ is $(\mathcal{F}_Y, \mathcal{F}_Z)$-measurable, then $h \circ g$ is $(\mathcal{F}_X, \mathcal{F}_Z)$-measurable.

But $(f \circ \delta)(x) = f(x,x) = \mathbf{1}_V(x)$, so $f \circ \delta = \mathbf{1}_V$.

Therefore, $\mathbf{1}_V$ is Borel measurable, which implies:
$$
V = \{x : \mathbf{1}_V(x) = 1\} = \mathbf{1}_V^{-1}(\{1\}) \in \mathcal{B}([0,1])
$$

This contradicts the assumption that $V$ is a Vitali set (non-Borel-measurable). ✓

**Conclusion:** The function $f$ has all sections measurable but is not jointly measurable with respect to the product σ-algebra. □

---

**Remark:** This counterexample demonstrates a subtle but crucial point: **measurability of sections is a necessary but not sufficient condition for joint measurability**. To ensure joint measurability, we need additional structure—e.g., continuity (Proposition 2.4 in the main text) or a specific construction preserving measurability (Proposition 2.5).

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
