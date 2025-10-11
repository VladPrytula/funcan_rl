# Citation Guide: References and Cross-References

**Purpose:** Quick reference for maintaining consistent citation and cross-referencing throughout the 48-week study plan.

---

## External Citations (from `references.bib`)

### Basic Citation Syntax

**Books:**
```markdown
See [@folland:real_analysis:1999] for the complete treatment.
The proof follows [@brezis:functional_analysis:2011].
```

**With specific sections:**
```markdown
By the Carathéodory Extension Theorem [@folland:real_analysis:1999, §1.2, Thm 1.14], we have...
For details, see [@puterman:mdp:2014, Chapter 6].
The construction is standard [@durrett:probability:2019, §6.5, pp. 312-315].
```

**Papers:**
```markdown
This approach was pioneered by [@mnih:dqn:2015].
The PPO algorithm [@schulman:ppo:2017] addresses this issue.
Recent work [@silver:alphazero:2018] demonstrates...
```

**Multiple references:**
```markdown
This result appears in several texts [@folland:real_analysis:1999, §2.3; @royden:real_analysis:2010, Thm 4.12; @rudin:real_complex:1987, §3.4].
```

### In Theorem Statements

```markdown
### Theorem 1.3.1 (Monotone Convergence Theorem) {#THM-1.3.1}

**Statement:** [@folland:real_analysis:1999, Thm 2.14] If $(f_n)$ is a sequence of measurable functions with $f_n \uparrow f$ a.e., then
$$\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu.$$

*Proof.* (Following [@brezis:functional_analysis:2011, §2.3])
...
□
```

### In Definitions

```markdown
### Definition 1.2.3 (Measure) {#DEF-1.2.3}

[@folland:real_analysis:1999, §1.2] A **measure** on a measurable space $(X, \mathcal{A})$ is a function $\mu: \mathcal{A} \to [0, \infty]$ satisfying...
```

### Common Section/Theorem Notation

- **Sections**: `§3.2` or `Section 3.2`
- **Theorems**: `Thm 2.14` or `Theorem 2.14`
- **Lemmas**: `Lem 1.5` or `Lemma 1.5`
- **Propositions**: `Prop 4.3` or `Proposition 4.3`
- **Corollaries**: `Cor 2.6` or `Corollary 2.6`
- **Examples**: `Ex 3.7` or `Example 3.7`
- **Exercises**: `Exercise 2.5.3`
- **Pages**: `pp. 45-47` or `p. 123`
- **Chapters**: `Chapter 5` or `Ch. 5`

---

## Internal Cross-References (Master_Index.md)

### ID Format

Use `TYPE-W.D.N` where:
- `TYPE` ∈ {`DEF`, `THM`, `LEM`, `PROP`, `COR`, `EX`}
- `W` = Week number (1-48)
- `D` = Day number (1-5)
- `N` = Sequential number within that day

Examples: `THM-2.3.1`, `DEF-1.4.5`, `LEM-3.2.2`, `PROP-1.1.3`

### Cross-Reference Syntax

**In running text:**
```markdown
Recall from **Definition 1.2.1** [DEF-1.2.1] that a measure is σ-additive.

By **Theorem 1.3.1** [THM-1.3.1] (Monotone Convergence), we have...

Using **Lemma 2.1.3** [LEM-2.1.3] and **Proposition 1.4.2** [PROP-1.4.2], we obtain...
```

**In proofs:**
```markdown
*Proof.*
**Step 1:** By [DEF-1.1.1], $\mathcal{A}$ is a σ-algebra.

**Step 2:** Applying [THM-1.3.1] (MCT), we have $\int f_n \to \int f$.

**Step 3:** The result follows from [LEM-2.1.1] (Fatou).
□
```

**Multiple dependencies:**
```markdown
**Proof sketch:** The result follows immediately from [THM-1.4.2], [LEM-2.1.1], and [PROP-1.2.3]. □
```

### Labeling Your Own Results

**Attach an ID anchor to every formal result:**

```markdown
### Definition 2.3.5 (Dominated Convergence) {#DEF-2.3.5}

### Theorem 1.4.2 (Banach Fixed-Point) {#THM-1.4.2}

### Lemma 3.1.1 (Dynkin π-λ) {#LEM-3.1.1}

### Proposition 2.2.4 (Measure Continuity) {#PROP-2.2.4}

### Corollary 1.5.3 (Bounded Convergence) {#COR-1.5.3}

### Example 1.2.1 (Counting Measure) {#EX-1.2.1}
```

The `{#ID}` syntax creates an Obsidian-compatible anchor for future backlinking.

---

## Complete Examples

### Example 1: Theorem with Citations and Cross-References

```markdown
### Theorem 2.4.3 (Fubini-Tonelli) {#THM-2.4.3}

**Statement:** [@folland:real_analysis:1999, Thm 2.37] Let $(X, \mathcal{A}, \mu)$ and $(Y, \mathcal{B}, \nu)$ be σ-finite measure spaces. If $f: X \times Y \to [0, \infty]$ is $\mathcal{A} \otimes \mathcal{B}$-measurable, then
$$\int_X \int_Y f(x, y) \, d\nu(y) \, d\mu(x) = \int_{X \times Y} f \, d(\mu \otimes \nu) = \int_Y \int_X f(x, y) \, d\mu(x) \, d\nu(y).$$

*Proof.* (Adapted from [@folland:real_analysis:1999, §2.4])

**Step 1: Simple functions.**
For $f = \chi_A$ with $A \in \mathcal{A} \otimes \mathcal{B}$, the result follows from [DEF-2.3.1] (product measure) and [PROP-2.3.5] (measurability of sections).

**Step 2: Nonnegative functions.**
For general $f \geq 0$, approximate by simple functions $s_n \uparrow f$ and apply [THM-1.4.2] (Monotone Convergence) three times.

**Step 3: General functions.**
Apply Step 2 to $f^+$ and $f^-$ separately, using [DEF-1.5.2] (integrability).

□

**Remark 2.4.1:** The σ-finiteness hypothesis is essential. For a counterexample, see [@folland:real_analysis:1999, Exercise 2.38] or [EX-2.4.1] below.

**RL Connection:** Fubini's theorem is critical for verifying that the Bellman operator [DEF-25.2.3] preserves measurability in product state-action spaces. We will use this extensively in Week 26 when analyzing policy evaluation for continuous MDPs [@puterman:mdp:2014, §6.3].
```

### Example 2: Definition with Standard/Original Marking

```markdown
### Definition 3.2.7 (Lᵖ Norm) {#DEF-3.2.7}

[@folland:real_analysis:1999, §6.1] For $1 \leq p < \infty$ and measurable $f: X \to \mathbb{R}$, define
$$\|f\|_p := \left( \int_X |f|^p \, d\mu \right)^{1/p}.$$

For $p = \infty$, define
$$\|f\|_\infty := \inf \{ M \geq 0 : \mu(\{|f| > M\}) = 0 \}.$$

**Note:** [Standard] This is the canonical Lᵖ norm. See also [@brezis:functional_analysis:2011, §4.1; @rudin:functional_analysis:1991, §3.3] for alternative treatments.
```

### Example 3: Proposition (Formalized Exercise)

```markdown
### Proposition 1.3.4 (Borel-Cantelli Lemma) {#PROP-1.3.4}

**Statement:** Let $(A_n)$ be a sequence of events in a probability space $(\Omega, \mathcal{F}, \mathbb{P})$.

(i) If $\sum_{n=1}^\infty \mathbb{P}(A_n) < \infty$, then $\mathbb{P}(\limsup_n A_n) = 0$.

(ii) If $(A_n)$ are independent and $\sum_{n=1}^\infty \mathbb{P}(A_n) = \infty$, then $\mathbb{P}(\limsup_n A_n) = 1$.

*Proof.* (Formalized from [@durrett:probability:2019, Exercise 1.3.5])

**(i)** By [DEF-1.1.1] and [PROP-1.2.2] (measure continuity from above),
$$\mathbb{P}(\limsup_n A_n) = \lim_{N \to \infty} \mathbb{P}\left( \bigcup_{n=N}^\infty A_n \right) \leq \lim_{N \to \infty} \sum_{n=N}^\infty \mathbb{P}(A_n) = 0.$$

**(ii)** Use independence to show $\mathbb{P}(\bigcap_{n=N}^\infty A_n^c) = 0$ for all $N$. (Details in `Day_1_exercises_FINAL.md`.)

□

**Note:** [Original] This is a formalized solution to an anchor exercise from Syllabus.md Week 1.

**RL Connection:** Part (i) is used to prove almost-sure convergence of stochastic approximation algorithms (Week 35) when step sizes $\alpha_n$ satisfy $\sum \alpha_n^2 < \infty$ [@borkar:stochastic_approximation:2008, §2.1].
```

### Example 4: Lemma with Multiple References

```markdown
### Lemma 3.4.2 (Approximation by Simple Functions) {#LEM-3.4.2}

**Statement:** [@folland:real_analysis:1999, Prop 2.10; @durrett:probability:2019, Lem 1.6.1] If $f: X \to [0, \infty]$ is measurable, there exists a sequence $(s_n)$ of simple functions with $0 \leq s_1 \leq s_2 \leq \cdots \uparrow f$ pointwise.

*Proof.*
Define
$$s_n(x) := \begin{cases}
\frac{k}{2^n} & \text{if } \frac{k}{2^n} \leq f(x) < \frac{k+1}{2^n}, \; k = 0, 1, \ldots, n \cdot 2^n - 1, \\
n & \text{if } f(x) \geq n.
\end{cases}$$

By [DEF-1.3.1], each $s_n$ is measurable and simple. Monotonicity and pointwise convergence follow by construction.

□
```

---

## RL Connection Sections

**Always include explicit RL connections** using this format:

```markdown
**RL Connection:** [Explain how this mathematical tool applies to RL/control]

- **Immediate application:** What RL concept does this directly support?
- **Future use:** Which week/topic will deploy this result?
- **Intuition:** Bridge abstract math to concrete algorithms

**Example:**
- *Banach Fixed-Point Theorem* → Value iteration convergence (Week 26)
- *Dominated Convergence* → Policy evaluation with function approximation (Week 36)
- *Sobolev Embedding* → Neural network approximation theory (Week 42)

**Citation pattern:**
Cite both mathematical source AND RL application:
[@brezis:functional_analysis:2011, Thm 2.1] underpins the convergence proof in [@bertsekas:rl_optimal_control:2019, §4.2].
```

---

## Remarks and Conceptual Notes

```markdown
**Remark W.D.N:** Use numbered remarks for:
- Historical context: "This result is due to Lebesgue (1904)..."
- Hypothesis necessity: "The σ-finiteness condition cannot be dropped; see [EX-2.4.1]."
- Forward connections: "We will generalize this to Banach spaces in [THM-14.3.2] (Week 14)."
- Proof technique insights: "The key mechanism here is dominated convergence [THM-2.2.1], a pattern recurring throughout measure-theoretic probability."

**Example:**

**Remark 2.3.4:** The Radon-Nikodym theorem [@folland:real_analysis:1999, Thm 3.2] requires $\nu \ll \mu$ (absolute continuity). When this fails, we must work with signed measures (Week 5) or resort to Hahn decomposition. This subtlety will matter for off-policy RL (Week 38) where behavior and target policies differ [@sutton:reinforcement_learning:2018, §5.5].
```

---

## Counterexamples

```markdown
### Example W.D.N (Counterexample: [Description]) {#EX-W.D.N}

**Purpose:** Show necessity of [specific condition in theorem]

**Construction:**
[Explicit construction with details]

**Why it fails:**
[Explain which hypothesis is violated and what breaks]

**Reference:** [@source, Exercise X.Y] or [Original]

**Example:**

### Example 2.2.5 (Counterexample: DCT without domination) {#EX-2.2.5}

**Purpose:** Show that [THM-2.2.1] (Dominated Convergence) requires integrable domination.

**Construction:** On $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ (Lebesgue measure), define
$$f_n(x) := \frac{1}{n} \chi_{[0, n]}(x).$$

Then $f_n \to 0$ pointwise, but $\int f_n = 1$ for all $n$, so $\int f_n \not\to \int 0$.

**Why it fails:** No integrable $g$ satisfies $|f_n| \leq g$ for all $n$ (the constant function $g = 1/n$ doesn't work uniformly).

**Reference:** [Original] Adapted from [@folland:real_analysis:1999, Exercise 2.25].
```

---

## Version Tracking in Citations

When updating a file to `_FINAL_v2.md`, `_FINAL_v3.md`, etc.:

1. **Update Master_Index.md** `Location` field to point to new version
2. **In the new version**, add a note about what changed:

```markdown
### Theorem 2.3.1 (Dominated Convergence Theorem) {#THM-2.3.1}

**Statement:** [@folland:real_analysis:1999, Thm 2.24] [Same statement as before]

*Proof.* [Updated proof with more detailed steps]

**Version note:** Proof expanded in v2 based on reviewer feedback (clarified measurability argument in Step 2).

**RL Connection:** [Updated in v2] This theorem underpins...
```

3. **Do NOT renumber IDs** when creating new versions—keep THM-2.3.1 as THM-2.3.1 across all versions

---

## Common Patterns

### Pattern 1: Theorem → Proof → Remark → RL Connection

```markdown
### Theorem W.D.N (Name) {#THM-W.D.N}
**Statement:** [@cite] [formal statement]

*Proof.* [proof body] □

**Remark W.D.N:** [conceptual insight]

**RL Connection:** [application to RL/control]
```

### Pattern 2: Definition → Example → Counterexample

```markdown
### Definition W.D.N (Name) {#DEF-W.D.N}
[@cite] [formal definition]

### Example W.D.N (Canonical Example) {#EX-W.D.N}
[Standard example illustrating definition]

### Example W.D.(N+1) (Counterexample/Pathological Case) {#EX-W.D.(N+1)}
[Shows boundary behavior or necessity of conditions]
```

### Pattern 3: Lemma → Proposition → Theorem (Building Blocks)

```markdown
### Lemma W.D.N (Technical Result) {#LEM-W.D.N}
[Key technical ingredient]

### Proposition W.D.(N+1) (Intermediate Step) {#PROP-W.D.(N+1)}
[Uses LEM-W.D.N]

### Theorem W.D.(N+2) (Main Result) {#THM-W.D.(N+2)}
[Uses PROP-W.D.(N+1) and LEM-W.D.N]
```

---

## Validation Checklist

Before finalizing `Day_X_FINAL.md` (or `_FINAL_vN.md`):

- [ ] All external citations use `[@cite_key]` format
- [ ] All citations exist in `references.bib`
- [ ] All internal cross-references use `[TYPE-W.D.N]` format
- [ ] All formal results have ID anchors `{#TYPE-W.D.N}`
- [ ] All results are added to `Master_Index.md`
- [ ] RL connections are explicit and cite both math and RL sources
- [ ] Remarks are numbered and serve a clear purpose
- [ ] Counterexamples are labeled as `{#EX-W.D.N}` with purpose stated

---

## Quick Reference Card

| Context | Syntax | Example |
|---------|--------|---------|
| External book | `[@key]` | `[@folland:real_analysis:1999]` |
| External book + section | `[@key, §X.Y]` | `[@brezis:functional_analysis:2011, §3.2]` |
| External paper | `[@key]` | `[@mnih:dqn:2015]` |
| Multiple references | `[@key1; @key2]` | `[@folland:real_analysis:1999, Thm 2.14; @durrett:probability:2019, Thm 1.6.1]` |
| Internal cross-ref | `[TYPE-W.D.N]` | `[THM-2.3.1]`, `[LEM-1.4.5]` |
| Result label | `{#TYPE-W.D.N}` | `{#DEF-3.2.7}` |
| Remark | `**Remark W.D.N:**` | `**Remark 2.3.4:**` |
| RL Connection | `**RL Connection:**` | (Always at end of result) |

---

**End of Citation Guide**
