### Agenda:

##### 📘 Day 1 — Week 2: Product σ-Algebras and Product Measures
**Total time: ~90 minutes**

---

#### **⏱️ Segment 1 (40 min) — Reading**

**Topic:** _Product σ-algebras and the construction of product measures_

- Read from **Folland, "Real Analysis" §2.4-2.5** or equivalent in Durrett Ch. 4.
- Focus on:
    - **Product σ-algebra** $\mathcal{F}_X \otimes \mathcal{F}_Y$ as the smallest σ-algebra making projections measurable
    - **Measurable rectangles** $A \times B$ and why they generate the product σ-algebra
    - **Pre-measure on rectangles**: $\mu_0(A \times B) = \mu(A)\nu(B)$
    - **Extension to product measure** via Carathéodory (existence and uniqueness)
- _Key takeaway:_ Product measures formalize the notion of "joint measurement" in two spaces. When combined with independence assumptions, they model independent observations—essential for defining trajectory spaces in MDPs.

---

#### **⏱️ Segment 2 (40 min) — Proof/Exercise**

**Primary Task:** Prove that the collection of measurable rectangles forms a **semiring** (Definition from Week 1 Day 4), verifying:
1. Closure under finite intersections
2. Set differences decompose into finite unions of rectangles
3. This enables Carathéodory extension to product σ-algebra

**Guidance:**
- Start with $(A_1 \times B_1) \cap (A_2 \times B_2) = (A_1 \cap A_2) \times (B_1 \cap B_2)$
- For differences, use $(A_1 \times B_1) \setminus (A_2 \times B_2)$ and visualize as geometric regions
- Connect to Week 1 Day 4: semirings are the starting point for pre-measures

**Stretch Goal:** Prove uniqueness of product measure when both $\mu$ and $\nu$ are σ-finite.

---

#### **⏱️ Segment 3 (10 min) — Reflection**

**Reflection Questions:**
1. How does the product σ-algebra $\mathcal{F}_{\mathcal{S}} \otimes \mathcal{F}_{\mathcal{A}}$ formalize the state-action space in an MDP?
2. Why is σ-finiteness necessary for uniqueness? What fails without it? (We explore this via counterexample in Week 2, Day 3.)
3. How will product measures enable us to define trajectory distributions $\mathbb{P}(s_0, a_0, s_1, a_1, \ldots)$?

**Preview for Day 2:** Tomorrow we prove **Tonelli's theorem**: for non-negative measurable functions, iterated integrals equal the double integral, justifying computing $\mathbb{E}_{s,a}[\cdots]$ via iterated expectations.

---

#### **💡 Conceptual bridge to RL**

- The product space $\mathcal{S} \times \mathcal{A}$ is where transition kernels $P(s'|s,a)$ are defined
- Product measures formalize "joint measurement" of state and action
- Trajectory spaces $(\mathcal{S} \times \mathcal{A})^\infty$ use infinite products (Week 3 topic)
- Fubini's theorem (Day 2) enables computing $\mathbb{E}_{s \sim \mu}[\mathbb{E}_{a \sim \pi(\cdot|s)}[Q(s,a)]]$ via iterated integrals

---

📅 Tomorrow (Day 2): **Tonelli's theorem** (complete proof) and preparation for Fubini.

---

## **Chapter 2: Product Spaces and Iterated Integration**

### **2.1 Product σ-Algebras: Formalizing Joint Observations**

**Motivation:** In Week 1, we constructed measure theory on a single space $(X, \mathcal{F}, \mu)$—the foundation for defining probabilities, expectations, and integration. But reinforcement learning is fundamentally a theory of **interactions**: an agent observes a state $s \in \mathcal{S}$, chooses an action $a \in \mathcal{A}$, receives a reward $r \in \mathbb{R}$, and transitions to a new state $s' \in \mathcal{S}$. Each of these is an event in a different measurable space.

To reason about such interactions rigorously, we must construct a **product space**—a single measurable space that encodes joint observations from multiple component spaces. The fundamental question is: *Given two measurable spaces $(X, \mathcal{F}_X)$ and $(Y, \mathcal{F}_Y)$, what is the "correct" σ-algebra on the Cartesian product $X \times Y$ that makes coordinate projections measurable?*

The answer, the **product σ-algebra** $\mathcal{F}_X \otimes \mathcal{F}_Y$, is not merely a technical construction—it is the mathematical formalization of **joint measurability**. It is the smallest σ-algebra on $X \times Y$ such that:
- The projection maps $\pi_X: X \times Y \to X$ and $\pi_Y: X \times Y \to Y$ are measurable
- Sets of the form $A \times Y$ and $X \times B$ (where $A \in \mathcal{F}_X$, $B \in \mathcal{F}_Y$) are measurable
- Any "reasonable" subset of $X \times Y$ that can be constructed from measurable sets in the factors is measurable

**Why this matters for RL:** The state-action space $\mathcal{S} \times \mathcal{A}$ is a product space. The transition kernel $P(\cdot | s,a)$ assigns to each pair $(s,a) \in \mathcal{S} \times \mathcal{A}$ a probability measure on $\mathcal{S}$. For this to be well-defined, we need:
1. The state-action space to have a measurable structure (the product σ-algebra)
2. The reward function $R: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ to be measurable with respect to this structure
3. The transition kernel to be jointly measurable in $(s,a)$

Moreover, the infinite trajectory space $(\mathcal{S} \times \mathcal{A} \times \mathcal{S})^\infty$ (encoding infinite-horizon trajectories) is an infinite product space, requiring a careful generalization of the finite product construction we develop today.

**Learning Objectives:**
* Define the product σ-algebra $\mathcal{F}_X \otimes \mathcal{F}_Y$ and prove it is generated by measurable rectangles
* Understand why measurable rectangles form a semiring, enabling Carathéodory extension
* Construct the product measure $\mu \times \nu$ via the extension theorem
* Establish uniqueness of product measures on σ-finite spaces
* Recognize product spaces as the domain for reward functions and transition kernels in RL

---

### **I. Core Theory: The Product σ-Algebra**

#### **A. Motivation: What Should "Measurable" Mean on $X \times Y$?**

Given measurable spaces $(X, \mathcal{F}_X)$ and $(Y, \mathcal{F}_Y)$, consider the Cartesian product $X \times Y = \{(x,y) : x \in X, y \in Y\}$. What subsets of $X \times Y$ should be considered "measurable"?

**Intuition 1: Rectangles.** If $A \in \mathcal{F}_X$ is measurable in $X$ and $B \in \mathcal{F}_Y$ is measurable in $Y$, then the **measurable rectangle** $A \times B = \{(x,y) : x \in A, y \in B\}$ should be measurable in $X \times Y$. This is the natural generalization of rectangles in $\mathbb{R}^2$.

**Intuition 2: Projections.** The coordinate projection maps $\pi_X: X \times Y \to X$ defined by $\pi_X(x,y) = x$ and $\pi_Y: X \times Y \to Y$ defined by $\pi_Y(x,y) = y$ should be measurable. This ensures that "observing the first coordinate" or "observing the second coordinate" are measurable operations.

**Observation:** If $\pi_X$ is measurable, then for any $A \in \mathcal{F}_X$, the set $\pi_X^{-1}(A) = A \times Y$ must be measurable. Similarly, $\pi_Y^{-1}(B) = X \times B$ must be measurable for all $B \in \mathcal{F}_Y$. Thus, requiring measurability of projections **implies** that sets of the form $A \times Y$ and $X \times B$ are measurable.

Furthermore, $(A \times Y) \cap (X \times B) = A \times B$, so all measurable rectangles are measurable. This suggests that the **smallest** σ-algebra making projections measurable is precisely the σ-algebra **generated by measurable rectangles**.

**Definition 2.1 (Product σ-Algebra).** Let $(X, \mathcal{F}_X)$ and $(Y, \mathcal{F}_Y)$ be measurable spaces. The **product σ-algebra**, denoted $\mathcal{F}_X \otimes \mathcal{F}_Y$, is the smallest σ-algebra on $X \times Y$ containing all measurable rectangles:
$$
\mathcal{F}_X \otimes \mathcal{F}_Y = \sigma(\{A \times B : A \in \mathcal{F}_X, B \in \mathcal{F}_Y\})
$$

The triple $(X \times Y, \mathcal{F}_X \otimes \mathcal{F}_Y)$ is called the **product measurable space**.

**Remark 2.1 (Alternative Characterization).** An equivalent definition: $\mathcal{F}_X \otimes \mathcal{F}_Y$ is the smallest σ-algebra on $X \times Y$ such that both projection maps $\pi_X$ and $\pi_Y$ are measurable. This is the categorical definition (product in the category of measurable spaces) and aligns with the intuition that joint measurability means "each component is individually observable."

---

#### **B. Structure of the Product σ-Algebra**

**Proposition 2.1 (Properties of the Product σ-Algebra).**
1. **Rectangles are measurable:** For any $A \in \mathcal{F}_X$ and $B \in \mathcal{F}_Y$, we have $A \times B \in \mathcal{F}_X \otimes \mathcal{F}_Y$.
2. **Projections are measurable:** The maps $\pi_X: (X \times Y, \mathcal{F}_X \otimes \mathcal{F}_Y) \to (X, \mathcal{F}_X)$ and $\pi_Y: (X \times Y, \mathcal{F}_X \otimes \mathcal{F}_Y) \to (Y, \mathcal{F}_Y)$ are measurable.
3. **Universal property:** If $\mathcal{G}$ is any σ-algebra on $X \times Y$ such that $\pi_X$ and $\pi_Y$ are $(\mathcal{G}, \mathcal{F}_X)$ and $(\mathcal{G}, \mathcal{F}_Y)$-measurable respectively, then $\mathcal{F}_X \otimes \mathcal{F}_Y \subseteq \mathcal{G}$.

*Proof.*

**(1):** By definition, $\mathcal{F}_X \otimes \mathcal{F}_Y$ is the σ-algebra generated by the collection of all measurable rectangles, so every such rectangle is measurable.

**(2):** We prove $\pi_X$ is measurable. For any $A \in \mathcal{F}_X$:
$$
\pi_X^{-1}(A) = \{(x,y) \in X \times Y : \pi_X(x,y) = x \in A\} = A \times Y
$$
We must show $A \times Y \in \mathcal{F}_X \otimes \mathcal{F}_Y$. Observe that $A \times Y = A \times Y$ is a measurable rectangle (with $A \in \mathcal{F}_X$ and $Y \in \mathcal{F}_Y$), hence is in $\mathcal{F}_X \otimes \mathcal{F}_Y$ by definition. Thus $\pi_X$ is measurable. The proof for $\pi_Y$ is symmetric.

**(3):** Suppose $\mathcal{G}$ is a σ-algebra on $X \times Y$ such that $\pi_X$ and $\pi_Y$ are measurable with respect to $\mathcal{G}$. Then for any $A \in \mathcal{F}_X$ and $B \in \mathcal{F}_Y$:
$$
A \times B = \pi_X^{-1}(A) \cap \pi_Y^{-1}(B) = (A \times Y) \cap (X \times B) \in \mathcal{G}
$$
since both $\pi_X^{-1}(A)$ and $\pi_Y^{-1}(B)$ are in $\mathcal{G}$ (by measurability of the projections) and $\mathcal{G}$ is closed under intersections. Thus $\mathcal{G}$ contains all measurable rectangles. Since $\mathcal{F}_X \otimes \mathcal{F}_Y$ is the *smallest* σ-algebra containing all measurable rectangles, we have $\mathcal{F}_X \otimes \mathcal{F}_Y \subseteq \mathcal{G}$. □

**Remark 2.2 (What is NOT in the Product σ-Algebra—Generally).** A common misconception is that $\mathcal{F}_X \otimes \mathcal{F}_Y$ consists *only* of countable unions of measurable rectangles. This is false in general. For instance, the diagonal $\Delta = \{(x,x) : x \in X\}$ (when $X = Y$) may be in $\mathcal{F}_X \otimes \mathcal{F}_X$ without being a countable union of rectangles. The product σ-algebra can contain vastly more complicated sets—it is the closure of rectangles under countable unions, intersections, and complements, which can produce intricate structures.

However, there is a partial positive result:

**Proposition 2.2 (Generating the Product σ-Algebra).** The product σ-algebra is generated by the collection of measurable rectangles:
$$
\mathcal{F}_X \otimes \mathcal{F}_Y = \sigma(\{A \times B : A \in \mathcal{F}_X, B \in \mathcal{F}_Y\})
$$
Moreover, every set in $\mathcal{F}_X \otimes \mathcal{F}_Y$ is the limit (in the sense of taking countable unions, intersections, and complements iteratively) of measurable rectangles.

*Proof.* This follows from the definition of $\mathcal{F}_X \otimes \mathcal{F}_Y$ as the smallest σ-algebra containing rectangles. The "limit" statement is a consequence of the transfinite construction of σ-algebras via the Borel hierarchy (see Folland §1.1, Exercise 10), which shows that $\sigma(\mathcal{C})$ for any collection $\mathcal{C}$ is obtained by iterating countable set operations starting from $\mathcal{C}$. □

---

#### **C. Measurable Rectangles Form a Semiring**

To construct a measure on the product space $(X \times Y, \mathcal{F}_X \otimes \mathcal{F}_Y)$, we will apply the **Carathéodory extension theorem** (Week 1, Day 4). Recall that the extension theorem begins with a **pre-measure on an algebra** and extends it to a measure on the generated σ-algebra. A key step is to verify that the starting collection (measurable rectangles) forms a **semiring**, which is a weaker structure than an algebra but sufficient for Carathéodory's construction.

**Definition 2.2 (Semiring - Recall from Week 1 Day 4).** A collection $\mathcal{S} \subseteq 2^{X \times Y}$ is a **semiring** if:
1. $\emptyset \in \mathcal{S}$
2. If $E, F \in \mathcal{S}$, then $E \cap F \in \mathcal{S}$ (closed under finite intersections)
3. If $E, F \in \mathcal{S}$ with $E \subseteq F$, then $F \setminus E$ can be written as a finite disjoint union of sets in $\mathcal{S}$

**Theorem 2.1 (Measurable Rectangles Form a Semiring).** Let $\mathcal{R} = \{A \times B : A \in \mathcal{F}_X, B \in \mathcal{F}_Y\}$ be the collection of measurable rectangles. Then $\mathcal{R}$ is a semiring.

*Proof.* We verify each axiom.

**(1) $\emptyset \in \mathcal{R}$:** We have $\emptyset = \emptyset \times \emptyset$, where $\emptyset \in \mathcal{F}_X$ and $\emptyset \in \mathcal{F}_Y$ (since σ-algebras contain the empty set). Thus $\emptyset \in \mathcal{R}$.

**(2) Closure under intersections:** Let $R_1 = A_1 \times B_1$ and $R_2 = A_2 \times B_2$ be two measurable rectangles. Their intersection is:
$$
R_1 \cap R_2 = (A_1 \times B_1) \cap (A_2 \times B_2) = (A_1 \cap A_2) \times (B_1 \cap B_2)
$$
Since $\mathcal{F}_X$ and $\mathcal{F}_Y$ are σ-algebras, we have $A_1 \cap A_2 \in \mathcal{F}_X$ and $B_1 \cap B_2 \in \mathcal{F}_Y$. Thus $R_1 \cap R_2 \in \mathcal{R}$.

**(3) Differences decompose into finite disjoint unions:** Let $R_1 = A_1 \times B_1$ and $R_2 = A_2 \times B_2$ with $R_1 \subseteq R_2$. This inclusion $R_1 \subseteq R_2$ means that for all $(x,y) \in A_1 \times B_1$, we have $(x,y) \in A_2 \times B_2$, which implies $A_1 \subseteq A_2$ and $B_1 \subseteq B_2$.

We compute the set difference:
$$
R_2 \setminus R_1 = (A_2 \times B_2) \setminus (A_1 \times B_1)
$$

**Geometric decomposition:** Visualize $A_2 \times B_2$ as a rectangle in the plane. The subset $A_1 \times B_1$ carves out a smaller rectangle. The complement $R_2 \setminus R_1$ consists of an "L-shaped" region, which we decompose as follows:

$$
R_2 \setminus R_1 = \big((A_2 \setminus A_1) \times B_2\big) \sqcup \big(A_1 \times (B_2 \setminus B_1)\big)
$$

where $\sqcup$ denotes disjoint union. To verify this is correct:

- **Coverage:** For $(x,y) \in R_2 \setminus R_1$, we have $(x,y) \in A_2 \times B_2$ but $(x,y) \notin A_1 \times B_1$.

  From $(x,y) \in A_2 \times B_2$, we have $x \in A_2$ and $y \in B_2$.

  From $(x,y) \notin A_1 \times B_1$, we have $\neg(x \in A_1 \land y \in B_1)$. By De Morgan's law, this is equivalent to $(x \notin A_1) \lor (y \notin B_1)$. Thus every point falls into at least one case:

  - **Case 1:** $x \notin A_1$ (and $x \in A_2$, so $x \in A_2 \setminus A_1$). Then $(x,y) \in (A_2 \setminus A_1) \times B_2$ (since $x \in A_2 \setminus A_1$ and $y \in B_2$).
  - **Case 2:** $x \in A_1$ and $y \notin B_1$ (and $y \in B_2$, so $y \in B_2 \setminus B_1$). Then $(x,y) \in A_1 \times (B_2 \setminus B_1)$.

  Thus every point in $R_2 \setminus R_1$ is in the union.

- **Disjointness:** A point in $(A_2 \setminus A_1) \times B_2$ has its first coordinate in $A_2 \setminus A_1$, so the first coordinate is not in $A_1$. A point in $A_1 \times (B_2 \setminus B_1)$ has its first coordinate in $A_1$. These are disjoint conditions, so the two sets are disjoint.

Since $\mathcal{F}_X$ and $\mathcal{F}_Y$ are σ-algebras, we have $A_2 \setminus A_1 \in \mathcal{F}_X$ and $B_2 \setminus B_1 \in \mathcal{F}_Y$. Therefore:
- $(A_2 \setminus A_1) \times B_2 \in \mathcal{R}$
- $A_1 \times (B_2 \setminus B_1) \in \mathcal{R}$

Thus $R_2 \setminus R_1$ is a finite (2-element) disjoint union of rectangles in $\mathcal{R}$. □

**Remark 2.3 (Why the Semiring Structure Matters).** The semiring property is precisely what allows us to define a **pre-measure** on rectangles and then extend it via the Carathéodory construction (Week 1, Day 4). The semiring ensures that:
1. We can unambiguously define "volume" $\mu_0(A \times B) = \mu(A) \nu(B)$ on rectangles
2. Set differences (needed for additivity checks) decompose into rectangles
3. The generated algebra consists of finite disjoint unions of rectangles, on which the pre-measure extends naturally

---

### **II. Product Measures: Construction via Carathéodory**

Having established that measurable rectangles form a semiring, we now construct the **product measure** $\mu \times \nu$ on $(X \times Y, \mathcal{F}_X \otimes \mathcal{F}_Y)$ via the Carathéodory extension theorem.

#### **A. Pre-Measure on Rectangles**

**Definition 2.3 (Pre-Measure on Rectangles).** Let $(X, \mathcal{F}_X, \mu)$ and $(Y, \mathcal{F}_Y, \nu)$ be measure spaces. Define $\mu_0: \mathcal{R} \to [0, \infty]$ on the semiring of measurable rectangles by:
$$
\mu_0(A \times B) = \mu(A) \cdot \nu(B)
$$
with the convention $0 \cdot \infty = 0$.

**Remark 2.4 (Why This Formula?).** The formula $\mu_0(A \times B) = \mu(A) \nu(B)$ is the natural generalization of "area = length × width" from elementary geometry. If $A$ has "size" $\mu(A)$ and $B$ has "size" $\nu(B)$, then the rectangle $A \times B$ should have "size" equal to their product.

**Proposition 2.3 (Pre-Measure Property - Proof Sketch).** The function $\mu_0$ is a pre-measure on the semiring $\mathcal{R}$. That is, $\mu_0(\emptyset) = 0$ and $\mu_0$ is countably additive on disjoint rectangles whose union is also a rectangle.

*Proof (Sketch).*
- $\mu_0(\emptyset \times \emptyset) = \mu(\emptyset) \nu(\emptyset) = 0 \cdot 0 = 0$.
- Countable additivity requires careful verification using the semiring property and the additivity of $\mu$ and $\nu$ on their respective spaces. The key step is to show that if $A \times B = \bigsqcup_{n=1}^{\infty} (A_n \times B_n)$ is a disjoint union of rectangles, then:
  $$
  \mu(A) \nu(B) = \sum_{n=1}^{\infty} \mu(A_n) \nu(B_n)
  $$
  This uses the fact that $A = \bigsqcup_{n=1}^{\infty} A_n$ (after accounting for how the $A_n$ tile $A$) and similarly for $B$. The full argument requires handling the case where rectangles may have complex overlaps, which is resolved by considering the algebra generated by the semiring.

For the complete verification of countable additivity on semirings, see Folland §2.4, Proposition 2.27. □

**Remark 2.5 (Extension to the Algebra).** The semiring $\mathcal{R}$ generates an algebra $\mathcal{A}(\mathcal{R})$ consisting of all finite disjoint unions of rectangles. The pre-measure $\mu_0$ extends uniquely to this algebra by additivity:
$$
\mu_0\left(\bigsqcup_{i=1}^{n} (A_i \times B_i)\right) = \sum_{i=1}^{n} \mu(A_i) \nu(B_i)
$$
This extension is well-defined (independent of the representation as a disjoint union) because of the semiring properties. We then apply Carathéodory's theorem to extend from the algebra to the σ-algebra.

---

#### **B. The Product Measure Theorem**

**Theorem 2.2 (Existence and Uniqueness of Product Measure).** Let $(X, \mathcal{F}_X, \mu)$ and $(Y, \mathcal{F}_Y, \nu)$ be measure spaces. Then:

1. **Existence:** There exists a unique measure $\mu \times \nu$ on $(X \times Y, \mathcal{F}_X \otimes \mathcal{F}_Y)$ such that:
   $$
   (\mu \times \nu)(A \times B) = \mu(A) \cdot \nu(B) \quad \text{for all } A \in \mathcal{F}_X, B \in \mathcal{F}_Y
   $$

2. **Uniqueness (σ-Finite Case):** If both $\mu$ and $\nu$ are **σ-finite**, then $\mu \times \nu$ is the unique measure on $\mathcal{F}_X \otimes \mathcal{F}_Y$ satisfying the rectangle formula above.

*Proof.*

**Existence:** Apply the **Carathéodory extension theorem** (Week 1, Day 4, Theorem 1.10):

**Step 0 (Verification of hypotheses):**
- $\mathcal{R}$ is a semiring (Theorem 2.1)
- $\mu_0: \mathcal{R} \to [0,\infty]$ is a pre-measure (Proposition 2.3)
- Therefore, Carathéodory applies.

**Step 1:** Start with the semiring $\mathcal{R}$ of measurable rectangles and the pre-measure $\mu_0(A \times B) = \mu(A)\nu(B)$.

**Step 2:** Extend $\mu_0$ to the algebra $\mathcal{A}(\mathcal{R})$ generated by $\mathcal{R}$ (finite disjoint unions of rectangles).

**Step 3:** Define the outer measure $(\mu \times \nu)^*(E)$ for any $E \subseteq X \times Y$ as:
   $$
   (\mu \times \nu)^*(E) = \inf\left\{\sum_{n=1}^{\infty} \mu(A_n)\nu(B_n) : E \subseteq \bigcup_{n=1}^{\infty} (A_n \times B_n)\right\}
   $$

**Step 4:** Identify the Carathéodory-measurable sets: the collection $\mathcal{M}$ of sets $E$ such that for all test sets $T \subseteq X \times Y$:
   $$
   (\mu \times \nu)^*(T) = (\mu \times \nu)^*(T \cap E) + (\mu \times \nu)^*(T \cap E^c)
   $$

**Step 5:** By Carathéodory's theorem, $\mathcal{M}$ is a σ-algebra containing $\mathcal{A}(\mathcal{R})$, hence containing $\mathcal{F}_X \otimes \mathcal{F}_Y = \sigma(\mathcal{R})$.

**Step 6:** The restriction of $(\mu \times \nu)^*$ to $\mathcal{F}_X \otimes \mathcal{F}_Y$ is the product measure $\mu \times \nu$.

**Uniqueness:** We invoke the π-λ theorem (Week 1, Day 1, or Folland §1.5, Theorem 1.14):

**Step 1:** The collection of measurable rectangles $\{A \times B : A \in \mathcal{F}_X, B \in \mathcal{F}_Y\}$ is a **π-system** (closed under finite intersections). This was verified in Theorem 2.1, Axiom 2.

**Step 2:** If $\mu$ and $\nu$ are σ-finite, then $\mu \times \nu$ is σ-finite (Remark 2.7).

**Step 3:** Two σ-finite measures that agree on a π-system generating a σ-algebra must be equal (π-λ theorem).

Since $\mu \times \nu$ is uniquely determined by its values on rectangles, uniqueness follows. □

**Remark 2.6 (Why σ-Finiteness?).** Without σ-finiteness, uniqueness can fail. The canonical counterexample involves counting measure on an uncountable set (this will be explored in Week 2, Day 3 as part of our study of counterexamples to Fubini). For RL applications, state and action spaces are typically either finite, countable, or Euclidean (with Lebesgue measure), all of which are σ-finite. Thus uniqueness is automatic in practice.

**Remark 2.7 (σ-Finiteness of the Product).** If $\mu$ and $\nu$ are σ-finite, then $\mu \times \nu$ is σ-finite. To see this: if $X = \bigcup_{m=1}^{\infty} X_m$ with $\mu(X_m) < \infty$ and $Y = \bigcup_{n=1}^{\infty} Y_n$ with $\nu(Y_n) < \infty$, then:
$$
X \times Y = \bigcup_{m,n=1}^{\infty} (X_m \times Y_n)
$$
and $(\mu \times \nu)(X_m \times Y_n) = \mu(X_m) \nu(Y_n) < \infty$. Since this is a countable union, $\mu \times \nu$ is σ-finite.

---

### **III. Measurability on Product Spaces**

Having constructed the product σ-algebra and product measure, we now investigate which functions on $X \times Y$ are measurable with respect to $\mathcal{F}_X \otimes \mathcal{F}_Y$.

**Remark 2.8 (Common Misconception).** A tempting conjecture is that measurability of all sections (horizontal and vertical) would suffice for joint measurability. This is **false**, as Exercise 3 (in the companion file) demonstrates. Measurability of sections is necessary but not sufficient.

**Proposition 2.4 (Sufficient Condition for Measurability).** If $f: X \times Y \to \mathbb{R}$ is **continuous** (when $X$ and $Y$ are topological spaces with Borel σ-algebras), then $f$ is $(\mathcal{F}_X \otimes \mathcal{F}_Y, \mathcal{B}(\mathbb{R}))$-measurable.

*Proof.* For any open set $U \subseteq \mathbb{R}$, the preimage $f^{-1}(U)$ is open in $X \times Y$ (by continuity). Open sets in $X \times Y$ are in the Borel σ-algebra $\mathcal{B}(X \times Y)$. For metric spaces, $\mathcal{B}(X \times Y) = \mathcal{B}(X) \otimes \mathcal{B}(Y)$ (this is a nontrivial result; see Folland §2.5, Theorem 2.29). Thus $f^{-1}(U) \in \mathcal{B}(X) \otimes \mathcal{B}(Y)$, so $f$ is measurable. □

**Proposition 2.5 (Composition of Measurable Functions).** If $g: X \to X'$ is $(\mathcal{F}_X, \mathcal{F}_{X'})$-measurable and $h: Y \to Y'$ is $(\mathcal{F}_Y, \mathcal{F}_{Y'})$-measurable, then the product map:
$$
g \times h: X \times Y \to X' \times Y', \quad (g \times h)(x,y) = (g(x), h(y))
$$
is $(\mathcal{F}_X \otimes \mathcal{F}_Y, \mathcal{F}_{X'} \otimes \mathcal{F}_{Y'})$-measurable.

*Proof (Sketch).* For any rectangle $A' \times B' \in \mathcal{F}_{X'} \otimes \mathcal{F}_{Y'}$:
$$
(g \times h)^{-1}(A' \times B') = \{(x,y) : g(x) \in A', h(y) \in B'\} = g^{-1}(A') \times h^{-1}(B')
$$
Since $g$ and $h$ are measurable, $g^{-1}(A') \in \mathcal{F}_X$ and $h^{-1}(B') \in \mathcal{F}_Y$, so the preimage is a measurable rectangle. By the definition of the product σ-algebra as generated by rectangles, $g \times h$ is measurable. □

---

### **IV. Application Bridge: Product Spaces in Reinforcement Learning**

**Connection 1: The State-Action Space $\mathcal{S} \times \mathcal{A}$**

In an MDP, the **state-action space** $\mathcal{S} \times \mathcal{A}$ is the natural domain for:
- **Reward functions**: $R: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$
- **Q-functions**: $Q^\pi: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$
- **Transition kernels** (parametrized by state-action pairs): $P(\cdot | s, a)$ is a measure on $\mathcal{S}$ for each $(s,a) \in \mathcal{S} \times \mathcal{A}$

For these objects to be well-defined, we need:
1. A measurable structure on $\mathcal{S} \times \mathcal{A}$: the product σ-algebra $\mathcal{B}(\mathcal{S}) \otimes \mathcal{B}(\mathcal{A})$
2. $R$ and $Q^\pi$ to be measurable with respect to this structure
3. The transition kernel to be jointly measurable: the map $(s,a,A) \mapsto P(A|s,a)$ should be measurable

**Example 2.1 (Reward Function Measurability).** Suppose $\mathcal{S} = [0,1]$ (continuous state) and $\mathcal{A} = \{0,1\}$ (binary action). Define:
$$
R(s,a) = \begin{cases} s^2 & \text{if } a = 0 \\ 1-s & \text{if } a = 1 \end{cases}
$$
Is $R$ measurable with respect to $\mathcal{B}([0,1]) \otimes \mathcal{B}(\{0,1\})$?

**Analysis:** For each action $a$, the section $R(\cdot, a)$ is a continuous function of $s$, hence Borel measurable. By Proposition 2.5, we can verify measurability by checking preimages of Borel sets. For instance:
$$
R^{-1}([0, 1/4]) = \{(s,0) : s^2 \in [0, 1/4]\} \cup \{(s,1) : 1-s \in [0, 1/4]\} = ([0, 1/2] \times \{0\}) \cup ([3/4, 1] \times \{1\})
$$
This is a union of two measurable rectangles, hence in $\mathcal{B}([0,1]) \otimes \mathcal{B}(\{0,1\})$. A similar analysis for arbitrary Borel sets confirms $R$ is measurable.

**Connection 2: Trajectory Spaces as Infinite Products**

An infinite-horizon trajectory in an MDP is a sequence:
$$
\tau = (s_0, a_0, r_0, s_1, a_1, r_1, \ldots) \in (\mathcal{S} \times \mathcal{A} \times \mathbb{R})^\infty
$$

The space of all trajectories is an **infinite product space**. To define probabilities over trajectories (induced by a policy $\pi$ and transition kernel $P$), we need:
1. The product σ-algebra on $(\mathcal{S} \times \mathcal{A})^\infty$ (the cylinder σ-algebra)
2. A product measure induced by $\pi$ and $P$ (the trajectory distribution)

The construction of infinite product measures requires additional care beyond the finite case we develop today (Kolmogorov extension theorem, Week 3). However, the finite product measure is the foundational building block.

**Connection 3: Fubini's Theorem and Policy Evaluation**

The expected return under a policy $\pi$ involves a **double expectation**:
$$
J(\pi) = \mathbb{E}_{s_0 \sim \mu_0}\left[\mathbb{E}_{a_0 \sim \pi(\cdot|s_0), s_1 \sim P(\cdot|s_0,a_0), \ldots}\left[\sum_{t=0}^{\infty} \gamma^t R(s_t, a_t)\right]\right]
$$

To compute this, we often interchange the order of expectations—taking the expectation over states first, then actions, or vice versa. This interchange is justified by **Fubini's theorem** (Day 2), which requires:
1. A well-defined product measure on the joint space
2. The integrand (cumulative reward) to be integrable

Today's product measure construction ensures (1) holds. Tomorrow, Fubini will justify the interchange.

---

### **V. Computational Illustration: Visualizing Product Measures**

To build intuition for product measures, we implement a simple example: constructing the product measure of two discrete probability measures and visualizing the resulting joint distribution.

**Example 2.2 (Discrete Product Measure).** Let $X = \{1, 2, 3\}$ with measure $\mu$ given by $\mu(\{1\}) = 1/2$, $\mu(\{2\}) = 1/3$, $\mu(\{3\}) = 1/6$. Let $Y = \{a, b\}$ with measure $\nu$ given by $\nu(\{a\}) = 2/3$, $\nu(\{b\}) = 1/3$. Compute the product measure $\mu \times \nu$ on $X \times Y$.

**Solution:** The product space has 6 elements: $X \times Y = \{(1,a), (1,b), (2,a), (2,b), (3,a), (3,b)\}$. For each singleton:
$$
\begin{align}
(\mu \times \nu)(\{(1,a)\}) &= \mu(\{1\}) \cdot \nu(\{a\}) = \frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3} \\
(\mu \times \nu)(\{(1,b)\}) &= \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6} \\
(\mu \times \nu)(\{(2,a)\}) &= \frac{1}{3} \cdot \frac{2}{3} = \frac{2}{9} \\
(\mu \times \nu)(\{(2,b)\}) &= \frac{1}{3} \cdot \frac{1}{3} = \frac{1}{9} \\
(\mu \times \nu)(\{(3,a)\}) &= \frac{1}{6} \cdot \frac{2}{3} = \frac{1}{9} \\
(\mu \times \nu)(\{(3,b)\}) &= \frac{1}{6} \cdot \frac{1}{3} = \frac{1}{18}
\end{align}
$$

We verify that the product measure sums to 1:
$$
\begin{align}
\sum_{x,y} (\mu \times \nu)(\{(x,y)\}) &= \frac{1}{3} + \frac{1}{6} + \frac{2}{9} + \frac{1}{9} + \frac{1}{9} + \frac{1}{18} \\
&= \frac{6}{18} + \frac{3}{18} + \frac{4}{18} + \frac{2}{18} + \frac{2}{18} + \frac{1}{18} \\
&= \frac{18}{18} = 1 \quad \checkmark
\end{align}
$$

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define measures
X = np.array([1, 2, 3])
Y = np.array(['a', 'b'])
mu = np.array([1/2, 1/3, 1/6])  # measure on X
nu = np.array([2/3, 1/3])        # measure on Y

# Compute product measure
product_measure = np.outer(mu, nu)  # (mu x nu)(i,j) = mu(i) * nu(j)

print("Product Measure (μ × ν):")
print(f"{'X \\ Y':<8}", end="")
for y_val in Y:
    print(f"{y_val:<12}", end="")
print(f"{'μ(X)':<12}")

for i, x_val in enumerate(X):
    print(f"{x_val:<8}", end="")
    for j, y_val in enumerate(Y):
        print(f"{product_measure[i,j]:<12.4f}", end="")
    print(f"{mu[i]:<12.4f}")

print(f"{'ν(Y)':<8}", end="")
for j in range(len(Y)):
    print(f"{nu[j]:<12.4f}", end="")
total = np.sum(product_measure)
print(f"Total: {total:.4f}")

# Visualization: Heatmap of product measure
fig, ax = plt.subplots(figsize=(8, 6))

# Draw rectangles with sizes proportional to measure
for i, x_val in enumerate(X):
    for j, y_val in enumerate(Y):
        rect = Rectangle((j, i), 1, 1, linewidth=2, edgecolor='black',
                        facecolor=plt.cm.Blues(product_measure[i,j] * 2))
        ax.add_patch(rect)
        ax.text(j + 0.5, i + 0.5, f'{product_measure[i,j]:.3f}',
               ha='center', va='center', fontsize=14, fontweight='bold')

ax.set_xlim(0, len(Y))
ax.set_ylim(0, len(X))
ax.set_xticks(np.arange(len(Y)) + 0.5)
ax.set_yticks(np.arange(len(X)) + 0.5)
ax.set_xticklabels(Y, fontsize=12)
ax.set_yticklabels(X, fontsize=12)
ax.set_xlabel('Y (Action Space)', fontsize=13)
ax.set_ylabel('X (State Space)', fontsize=13)
ax.set_title('Product Measure μ × ν on X × Y\n(Rectangle area ~ probability)', fontsize=14)
ax.invert_yaxis()  # Match matrix indexing
plt.tight_layout()
plt.show()

print(f"\nVerification: ∑(μ × ν) = {np.sum(product_measure):.6f} (should be 1.0)")
```

**Output:**
```
Product Measure (μ × ν):
X \ Y   a           b           μ(X)
1       0.3333      0.1667      0.5000
2       0.2222      0.1111      0.3333
3       0.1111      0.0556      0.1667
ν(Y)    0.6667      0.3333      Total: 1.0000

Verification: ∑(μ × ν) = 1.000000 (should be 1.0)
```

**RL Interpretation:** This discrete product measure represents a joint distribution over state-action pairs. If $X$ is a finite state space and $Y$ is a finite action space, $\mu$ could be the state occupancy distribution under a policy, and $\nu$ could be the action selection distribution. The product measure $\mu \times \nu$ gives the probability of observing state-action pair $(x,y)$ under the joint distribution.

The heatmap shows that state 1 with action $a$ has the highest probability (1/3), consistent with state 1 having the highest marginal probability (1/2) and action $a$ having the highest conditional probability (2/3).

---

### **VI. Mathematical Insight and Forward Connections**

**Mathematical Insight:**

The product σ-algebra construction reveals a fundamental principle: **joint measurability is not the same as marginal measurability**. Measurable rectangles $A \times B$ are the building blocks, but the product σ-algebra contains vastly more sets—obtained by taking countable unions, intersections, and complements iteratively. This mirrors the structure of information: knowing each component individually (marginal information) is weaker than knowing the joint configuration.

The semiring-to-σ-algebra extension via Carathéodory is the second time we've seen this pattern (first: Week 1 Day 4 for Lebesgue measure). This is not a coincidence—it is the **canonical method** for constructing measures in modern analysis. The blueprint: start with a simple structure (rectangles), verify it forms a semiring or algebra, define a pre-measure, apply Carathéodory.

**RL Connection:**

Product measures formalize **joint distributions** over state-action pairs, essential for:
1. **Reward functions**: $\mathbb{E}_{(s,a) \sim \mu \times \pi}[R(s,a)]$ requires a product measure on $\mathcal{S} \times \mathcal{A}$
2. **Transition kernels**: $P(\cdot | s,a)$ is parametrized by $(s,a) \in \mathcal{S} \times \mathcal{A}$, requiring joint measurability
3. **Trajectory distributions**: Infinite products $(\mathcal{S} \times \mathcal{A})^\infty$ (developed in Week 3)
4. **Fubini's theorem** (Day 2): Justifies computing $\mathbb{E}_{s,a}[Q(s,a)]$ via iterated expectations

Without product measures, we cannot rigorously define what it means to "observe a state and action simultaneously" or "compute expectations over joint spaces."

**Open Questions:**

1. **Non-σ-Finite Spaces:** What happens if $\mu$ or $\nu$ is not σ-finite? Can we still construct a product measure? Uniqueness certainly fails (we explore this in Week 2, Day 3), but does existence hold? The answer is subtle and involves measurable cardinals (see Folland §2.6, advanced topic).

2. **Infinite Products:** How do we extend to countably infinite products $\prod_{n=1}^{\infty} (X_n, \mathcal{F}_n, \mu_n)$? The Kolmogorov extension theorem (Week 3) provides the answer, but it requires additional hypotheses (consistency conditions on finite-dimensional marginals).

3. **Continuous-Time Extensions:** In continuous-time RL (Week 38), trajectories are paths $[0,T] \to \mathcal{S}$. What is the "product measure" on function spaces? This leads to Wiener measure and stochastic processes—an infinite-dimensional generalization of today's construction.

---

**Looking Ahead:**

- **Day 2 (Tomorrow)**: **Tonelli's theorem** proves that for non-negative measurable functions $f: X \times Y \to [0,\infty]$, the iterated integrals equal the double integral:
  $$
  \int_X \left(\int_Y f(x,y) \, d\nu(y)\right) d\mu(x) = \int_{X \times Y} f \, d(\mu \times \nu) = \int_Y \left(\int_X f(x,y) \, d\mu(x)\right) d\nu(y)
  $$
  This justifies computing expectations via iterated integrals.

- **Day 3**: **Fubini's theorem** extends Tonelli to integrable functions (not just non-negative), enabling interchange of integrals for general $L^1$ functions. We also study counterexamples: failure without σ-finiteness and failure without integrability.

- **Week 3**: Infinite product spaces and the Kolmogorov extension theorem construct probability measures on trajectory spaces $(\mathcal{S} \times \mathcal{A})^\infty$.

The product measure constructed today is the cornerstone. Tomorrow, we make it computational via Fubini-Tonelli.

---

### Exercises

Detailed exercises with guided proofs are provided in the companion file:
**[[Day_1_exercises_REVISED]]**
