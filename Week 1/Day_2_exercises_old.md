[[Day_2 (old)]]

# The Lebesgue Integral and Monotone Convergence Theorem

This document contains complete proofs and exercises for Day 2 of Week 1, focusing on the construction of the Lebesgue integral and the Monotone Convergence Theorem.

---

## **Core Exercise: Complete Proof of the Monotone Convergence Theorem**

**Theorem (Monotone Convergence Theorem).** Let $(X, \mathcal{F}, \mu)$ be a measure space. Suppose $\{f_n\}_{n=1}^{\infty}$ is a sequence of measurable functions with:
1. $f_n \geq 0$ for all $n$ (non-negativity)
2. $f_1(x) \leq f_2(x) \leq f_3(x) \leq \cdots$ for all $x \in X$ (monotonicity)
3. $f_n(x) \to f(x)$ for all $x \in X$ (pointwise convergence)

Then $f$ is measurable and:
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu
$$

---

### **Proof**

We proceed in four carefully structured steps, each addressing a distinct aspect of the theorem.

---

#### **Step 1: Measurability of the Limit Function**

**Claim:** The pointwise limit $f = \lim_{n \to \infty} f_n$ is a measurable function.

**Proof of Step 1:**

Recall that for any sequence of real numbers, the pointwise limit can be expressed as:
$$
f(x) = \lim_{n \to \infty} f_n(x) = \sup_{n \geq 1} f_n(x)
$$
This equality holds because the sequence $\{f_n(x)\}$ is monotone increasing.

For any $a \in \mathbb{R}$, consider the set:
$$
\{x \in X : f(x) > a\} = \{x \in X : \sup_{n \geq 1} f_n(x) > a\}
$$

An element $x$ belongs to this set if and only if there exists some index $n$ such that $f_n(x) > a$. Therefore:
$$
\{x \in X : f(x) > a\} = \bigcup_{n=1}^{\infty} \{x \in X : f_n(x) > a\}
$$

Since each $f_n$ is measurable, the set $\{x : f_n(x) > a\}$ belongs to $\mathcal{F}$ for every $n$. The union of countably many measurable sets is measurable (by the definition of a $\sigma$-algebra), so:
$$
\{x \in X : f(x) > a\} \in \mathcal{F}
$$

This holds for every $a \in \mathbb{R}$. Since the sets $\{x : f(x) > a\}$ generate the Borel $\sigma$-algebra on the codomain, and since their preimages are all in $\mathcal{F}$, we conclude that $f$ is measurable.

$\blacksquare$ (Step 1)

---

#### **Step 2: The "Easy" Inequality $\liminf \int f_n \leq \int f$**

**Claim:** The sequence of integrals $\{\int f_n \, d\mu\}$ is increasing and bounded above by $\int f \, d\mu$.

**Proof of Step 2:**

By the monotonicity of the functions, we have $f_n \leq f_{n+1}$ for all $n$. The monotonicity property of the integral (which we established for non-negative measurable functions) gives:
$$
\int f_n \, d\mu \leq \int f_{n+1} \, d\mu
$$

Thus, $\{\int f_n \, d\mu\}$ is a monotone increasing sequence of non-negative extended real numbers.

Furthermore, since $f_n \leq f$ for all $n$ (because the sequence is increasing and converges to $f$), we have by monotonicity:
$$
\int f_n \, d\mu \leq \int f \, d\mu
$$
for every $n$.

A monotone increasing sequence that is bounded above has a limit. Therefore:
$$
\lim_{n \to \infty} \int f_n \, d\mu \text{ exists (possibly infinite) and satisfies } \lim_{n \to \infty} \int f_n \, d\mu \leq \int f \, d\mu
$$

$\blacksquare$ (Step 2)

---

#### **Step 3: The "Hard" Inequality $\int f \, d\mu \leq \liminf \int f_n$**

This is the crux of the theorem. We must prove that the integral of the limit is no larger than the limit of the integrals. The strategy is to show this inequality by considering simple functions that approximate $f$ from below.

**Proof of Step 3:**

Let $\varphi$ be an arbitrary non-negative simple function with $0 \leq \varphi \leq f$. By the definition of the integral for non-negative functions as a supremum over simple functions, it suffices to prove:
$$
\int \varphi \, d\mu \leq \lim_{n \to \infty} \int f_n \, d\mu
$$

Once we establish this for all such $\varphi$, taking the supremum over all simple functions $\varphi \leq f$ will give us:
$$
\int f \, d\mu = \sup_{0 \leq \varphi \leq f, \, \varphi \text{ simple}} \int \varphi \, d\mu \leq \lim_{n \to \infty} \int f_n \, d\mu
$$

**The α-Trick:**

Fix a constant $\alpha \in (0, 1)$. For each $n$, define the set:
$$
E_n = \{x \in X : f_n(x) \geq \alpha \varphi(x)\}
$$

**Key observations about $\{E_n\}$:**

1.  **Measurability:** Since $f_n$ and $\varphi$ are both measurable, the set $E_n = \{x : f_n(x) - \alpha\varphi(x) \geq 0\}$ is measurable for each $n$.

2.  **Monotonicity:** If $x \in E_n$, then $f_n(x) \geq \alpha\varphi(x)$. Since $f_{n+1}(x) \geq f_n(x)$, we have $f_{n+1}(x) \geq \alpha\varphi(x)$, so $x \in E_{n+1}$. Thus, $E_1 \subseteq E_2 \subseteq E_3 \subseteq \cdots$.

3.  **Exhaustion:** We claim that $\bigcup_{n=1}^{\infty} E_n = X$.
    
    *Proof:* Take any $x \in X$. We have two cases:
    
    *   If $\varphi(x) = 0$, then $\alpha\varphi(x) = 0$, so $f_n(x) \geq 0 = \alpha\varphi(x)$ for all $n \geq 1$. Thus, $x \in E_1 \subseteq \bigcup E_n$.
    *   If $\varphi(x) > 0$, then since $f_n(x) \to f(x)$ and $f(x) \geq \varphi(x) > \alpha\varphi(x)$ (because $\alpha < 1$), there must exist some index $N$ such that $f_N(x) \geq \alpha\varphi(x)$. Therefore, $x \in E_N \subseteq \bigcup E_n$.
    
    In both cases, $x \in \bigcup E_n$. Hence, $\bigcup_{n=1}^{\infty} E_n = X$.

**Using the sets $E_n$:**

For each $n$, we have the inequality $f_n \geq \alpha\varphi$ on the set $E_n$. Therefore:
$$
\int f_n \, d\mu \geq \int_{E_n} f_n \, d\mu \geq \int_{E_n} \alpha\varphi \, d\mu = \alpha \int_{E_n} \varphi \, d\mu
$$

Taking the limit as $n \to \infty$:
$$
\lim_{n \to \infty} \int f_n \, d\mu \geq \lim_{n \to \infty} \left( \alpha \int_{E_n} \varphi \, d\mu \right) = \alpha \lim_{n \to \infty} \int_{E_n} \varphi \, d\mu
$$

**Applying continuity of measure:**

Since $\{E_n\}$ is an increasing sequence of measurable sets with $\bigcup E_n = X$, and $\varphi$ is a simple function (hence has finite integral on any set of finite measure), we can apply the **continuity of measure from below**. 

For a simple function $\varphi = \sum_{i=1}^{k} a_i \mathbf{1}_{A_i}$ with $a_i \geq 0$:
$$
\int_{E_n} \varphi \, d\mu = \sum_{i=1}^{k} a_i \mu(A_i \cap E_n)
$$

As $n \to \infty$, we have $E_n \uparrow X$, so $A_i \cap E_n \uparrow A_i \cap X = A_i$ for each $i$. By continuity of measure:
$$
\mu(A_i \cap E_n) \to \mu(A_i)
$$

Therefore:
$$
\lim_{n \to \infty} \int_{E_n} \varphi \, d\mu = \sum_{i=1}^{k} a_i \mu(A_i) = \int_X \varphi \, d\mu = \int \varphi \, d\mu
$$

Substituting back:
$$
\lim_{n \to \infty} \int f_n \, d\mu \geq \alpha \int \varphi \, d\mu
$$

**Letting $\alpha \to 1$:**

The above inequality holds for every $\alpha \in (0,1)$. Taking the limit as $\alpha \to 1^-$:
$$
\lim_{n \to \infty} \int f_n \, d\mu \geq \int \varphi \, d\mu
$$

This holds for every simple function $0 \leq \varphi \leq f$. Taking the supremum over all such $\varphi$:
$$
\lim_{n \to \infty} \int f_n \, d\mu \geq \sup_{0 \leq \varphi \leq f, \, \varphi \text{ simple}} \int \varphi \, d\mu = \int f \, d\mu
$$

$\blacksquare$ (Step 3)

---

#### **Step 4: Conclusion**

From Step 2, we have:
$$
\lim_{n \to \infty} \int f_n \, d\mu \leq \int f \, d\mu
$$

From Step 3, we have:
$$
\lim_{n \to \infty} \int f_n \, d\mu \geq \int f \, d\mu
$$

Combining these two inequalities:
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu
$$

This completes the proof of the Monotone Convergence Theorem.

$\square$

---

## **Reflection on the Proof Technique**

### **Where was monotonicity essential?**

1.  **Step 1 (Measurability):** Monotonicity allowed us to express $f = \sup_n f_n$, which made the measurability argument straightforward via countable unions.

2.  **Step 2 (Easy inequality):** Monotonicity ensured that $\{\int f_n\}$ is an increasing sequence, guaranteeing the existence of its limit.

3.  **Step 3 (Hard inequality – the α-trick):** Monotonicity was crucial in two ways:
    *   It ensured that $E_n \subseteq E_{n+1}$ (monotonicity of the sets).
    *   It guaranteed that $\bigcup E_n = X$ (because $f_n(x) \to f(x) \geq \varphi(x)$ forces eventual membership in $E_n$ when $\varphi(x) > 0$).

Without monotonicity, the sequence of sets $E_n$ would not be increasing, and we could not apply the continuity of measure from below. This is the key reason why MCT requires monotonicity.

### **What happens without monotonicity?**

Consider the sequence on $[0,1]$ with Lebesgue measure:
$$
f_n(x) = \begin{cases}
1 & \text{if } x \in [0, 1/n) \\
0 & \text{if } x \in [1/n, 1]
\end{cases}
$$

We have $f_n(x) \to 0$ for all $x \in (0,1]$, and $f_1(0) = f_2(0) = \cdots = 1 \to 0$ at $x=0$. The limit is $f(x) = 0$ everywhere.

However:
$$
\int f_n \, d\mu = \int_0^{1/n} 1 \, dx = \frac{1}{n} \to 0 = \int f \, d\mu
$$

In this case, the conclusion of MCT holds even without monotonicity! But this is not a counterexample to the necessity of monotonicity; rather, it shows that monotonicity is **sufficient** but not **necessary** for the conclusion.

The real issue arises with oscillating sequences. Consider:
$$
g_n(x) = \mathbf{1}_{[0,1]}(x) \cdot \sin^2(n\pi x) \cdot n
$$

This sequence does not converge for most $x$, but if it did converge to $g(x)$, the integrals would oscillate and not necessarily converge to $\int g$. Monotonicity prevents such pathological behavior.

### **Why is the α-trick necessary?**

The α-trick handles the case where $\varphi(x) = f(x)$ on a set of **infinite measure**. Without the deflation factor $\alpha$, we might have $E_n = \{x : f_n(x) \geq \varphi(x)\}$, and on the complement $E_n^c = \{x : f_n(x) < \varphi(x)\}$, the inequality $f_n \geq \varphi$ would be violated. If $\mu(E_n^c)$ remains bounded away from zero for all $n$, we cannot conclude that $\int f_n \to \int \varphi$.

By using $\alpha < 1$, we ensure that $\varphi(x) > \alpha\varphi(x)$ wherever $\varphi(x) > 0$, giving us a "buffer" that allows $f_n$ to eventually exceed $\alpha\varphi$ without requiring $f_n \geq \varphi$.

---

## **Additional Exercises**

### **Exercise 1: Approximation of Measurable Functions by Simple Functions**

**Statement:** Let $(X, \mathcal{F}, \mu)$ be a measure space and $f: X \to [0, \infty]$ a measurable function. Prove that there exists an increasing sequence of simple functions $\{\varphi_n\}$ such that:
1. $0 \leq \varphi_1 \leq \varphi_2 \leq \cdots \leq f$
2. $\varphi_n(x) \to f(x)$ for all $x \in X$

**Proof:**

For each $n \in \mathbb{N}$, partition the range $[0, \infty]$ as follows:
- Divide $[0, n]$ into $n \cdot 2^n$ intervals: $[k/2^n, (k+1)/2^n)$ for $k = 0, 1, \ldots, n \cdot 2^n - 1$
- The single interval $[n, \infty]$

Define:
$$
\varphi_n(x) = \begin{cases}
\frac{k}{2^n} & \text{if } f(x) \in [k/2^n, (k+1)/2^n) \text{ for some } k < n \cdot 2^n \\
n & \text{if } f(x) \geq n
\end{cases}
$$

Equivalently:
$$
\varphi_n(x) = \sum_{k=0}^{n \cdot 2^n - 1} \frac{k}{2^n} \mathbf{1}_{A_{n,k}}(x) + n \cdot \mathbf{1}_{B_n}(x)
$$
where:
$$
A_{n,k} = \{x : k/2^n \leq f(x) < (k+1)/2^n\}, \qquad B_n = \{x : f(x) \geq n\}
$$

**Properties:**

1. **Simple functions:** Each $\varphi_n$ is a simple function (takes finitely many values).

2. **Measurability of the sets:** Since $f$ is measurable, $A_{n,k} = f^{-1}([k/2^n, (k+1)/2^n))$ and $B_n = f^{-1}([n, \infty])$ are measurable.

3. **Monotonicity:** If $f(x) < n$, then $\varphi_n(x) = \lfloor 2^n f(x) \rfloor / 2^n$ and $\varphi_{n+1}(x) = \lfloor 2^{n+1} f(x) \rfloor / 2^{n+1}$. Since the partition for $n+1$ is finer, $\varphi_{n+1}(x) \geq \varphi_n(x)$.
   If $f(x) \geq n$, then $\varphi_n(x) = n \leq n+1 \leq \varphi_{n+1}(x)$.

4. **Convergence:** For $x$ with $f(x) < \infty$, choose $N$ such that $f(x) < N$. For $n \geq N$, we have $\varphi_n(x) = \lfloor 2^n f(x) \rfloor / 2^n$, which satisfies:
   $$
   f(x) - \frac{1}{2^n} < \varphi_n(x) \leq f(x)
   $$
   As $n \to \infty$, $1/2^n \to 0$, so $\varphi_n(x) \to f(x)$.
   
   If $f(x) = \infty$, then $\varphi_n(x) = n \to \infty = f(x)$.

Thus, $\{\varphi_n\}$ satisfies all required properties. $\square$

---

### **Exercise 2: Fatou's Lemma from MCT (Preview)**

**Statement:** Use the Monotone Convergence Theorem to prove the following weaker result:

Let $\{f_n\}$ be a sequence of non-negative measurable functions. Define $g_n(x) = \inf_{k \geq n} f_k(x)$. Then:
$$
\int \left(\liminf_{n \to \infty} f_n\right) d\mu = \int \left(\lim_{n \to \infty} g_n\right) d\mu \leq \liminf_{n \to \infty} \int f_n \, d\mu
$$

**Proof:**

**Step 1:** Define $g_n(x) = \inf_{k \geq n} f_k(x)$. Each $g_n$ is measurable (as infimum of measurable functions), and $g_n \geq 0$ (since each $f_k \geq 0$).

**Step 2:** The sequence $\{g_n\}$ is increasing:
$$
g_1(x) = \inf_{k \geq 1} f_k(x) \leq \inf_{k \geq 2} f_k(x) = g_2(x) \leq \cdots
$$
This is because taking the infimum over a smaller set yields a larger value.

**Step 3:** The pointwise limit of $g_n$ is:
$$
\lim_{n \to \infty} g_n(x) = \lim_{n \to \infty} \left(\inf_{k \geq n} f_k(x)\right) = \liminf_{n \to \infty} f_n(x)
$$
This is the definition of $\liminf$.

**Step 4:** Apply MCT to the sequence $\{g_n\}$:
$$
\int \left(\liminf_{n \to \infty} f_n\right) d\mu = \int \left(\lim_{n \to \infty} g_n\right) d\mu = \lim_{n \to \infty} \int g_n \, d\mu
$$

**Step 5:** For each $n$, we have $g_n(x) = \inf_{k \geq n} f_k(x) \leq f_k(x)$ for all $k \geq n$. In particular, $g_n \leq f_n$. By monotonicity of the integral:
$$
\int g_n \, d\mu \leq \int f_n \, d\mu
$$

**Step 6:** Since $\{\int g_n\}$ is an increasing sequence (by MCT applied to $g_n$), we have:
$$
\lim_{n \to \infty} \int g_n \, d\mu = \liminf_{n \to \infty} \int g_n \, d\mu \leq \liminf_{n \to \infty} \int f_n \, d\mu
$$

**Conclusion:** Combining the steps:
$$
\int \left(\liminf_{n \to \infty} f_n\right) d\mu = \lim_{n \to \infty} \int g_n \, d\mu \leq \liminf_{n \to \infty} \int f_n \, d\mu
$$

This is **Fatou's Lemma**, which we will study in detail on Day 3. $\square$

---

### **Exercise 3: Necessity of Non-Negativity**

**Statement:** Construct an example showing that MCT fails without the non-negativity assumption.

**Solution:**

Consider the sequence on $[0,1]$ with Lebesgue measure:
$$
f_n(x) = -\frac{1}{n}
$$

This sequence is:
- Monotone increasing: $f_1(x) = -1 \leq f_2(x) = -1/2 \leq \cdots$
- Convergent: $f_n(x) \to 0$ for all $x \in [0,1]$

However:
$$
\int_0^1 f_n(x) \, dx = -\frac{1}{n} \to 0
$$
and
$$
\int_0^1 \lim_{n \to \infty} f_n(x) \, dx = \int_0^1 0 \, dx = 0
$$

In this case, MCT's conclusion holds: $\lim \int f_n = \int f$. But this is a "degenerate" case.

**A more pathological example:**

Consider:
$$
h_n(x) = -n \mathbf{1}_{[0, 1/n]}(x)
$$

We have:
- $h_n(x) \to 0$ for all $x \in (0,1]$
- $h_1(0) = -1, h_2(0) = -2, \ldots \to -\infty$

For $x > 0$, eventually $x \notin [0, 1/n]$, so $h_n(x) = 0$ for large $n$. Thus $h_n(x) \to 0$ except at $x = 0$, where it diverges to $-\infty$.

But this sequence is not monotone. To get a true counterexample, we need non-negativity violated with monotonicity preserved.

**Correct counterexample:**

Actually, for **monotone sequences**, even if $f_n < 0$, the MCT conclusion can still hold (as in the $f_n = -1/n$ example). The real issue is when we have $\int f_n = -\infty$ for all $n$ and the limit also has $\int f = -\infty$. The equation "$-\infty = -\infty$" is not meaningful in extended real arithmetic.

The crucial point is that MCT is stated for **non-negative** functions to avoid issues with $\infty - \infty$ in the integral definition. For functions that can be negative, we need the **Dominated Convergence Theorem** (Day 3), which requires a dominating integrable function.

---

### **Exercise 4: Application to Series**

**Statement:** Use MCT to prove that for non-negative measurable functions $\{g_n\}$:
$$
\int \left(\sum_{n=1}^{\infty} g_n\right) d\mu = \sum_{n=1}^{\infty} \int g_n \, d\mu
$$

**Proof:**

Define the partial sums:
$$
f_N(x) = \sum_{n=1}^{N} g_n(x)
$$

Then:
1. Each $f_N$ is measurable (finite sum of measurable functions)
2. Each $f_N \geq 0$ (sum of non-negative functions)
3. $f_N$ is increasing: $f_1 \leq f_2 \leq f_3 \leq \cdots$
4. $f_N(x) \to \sum_{n=1}^{\infty} g_n(x)$ as $N \to \infty$

By MCT:
$$
\int \left(\lim_{N \to \infty} f_N\right) d\mu = \lim_{N \to \infty} \int f_N \, d\mu
$$

The left-hand side is:
$$
\int \left(\sum_{n=1}^{\infty} g_n\right) d\mu
$$

The right-hand side is:
$$
\lim_{N \to \infty} \int \left(\sum_{n=1}^{N} g_n\right) d\mu = \lim_{N \to \infty} \sum_{n=1}^{N} \int g_n \, d\mu = \sum_{n=1}^{\infty} \int g_n \, d\mu
$$
where we used linearity of the integral for finite sums. $\square$

**Corollary (Tonelli for Counting Measure):** This result is the discrete version of Tonelli's theorem, which we will study in Week 3.

---

## **Conceptual Reflection: MCT and Reinforcement Learning**

### **Mathematical Insight**

The proof of MCT demonstrates a profound interplay between:
1. **Topology** (convergence of functions)
2. **Measure theory** (continuity of measure on increasing sets)
3. **Order structure** (monotonicity enabling control of approximations)

The α-trick is a technical device that appears throughout analysis whenever we need to handle functions that may take infinite values on sets of infinite measure. It is related to the concept of "essential supremum" and will reappear in the study of $L^{\infty}$ spaces.

### **RL Connection: Value Iteration Convergence**

In a finite-state MDP with non-negative rewards, the value iteration sequence:
$$
V_{n+1}(s) = \max_a \left\{ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V_n(s') \right\}
$$
starting from $V_0 = 0$ produces a monotonically increasing sequence $V_0 \leq V_1 \leq V_2 \leq \cdots$ converging to $V^*$.

For any initial state distribution $\mu$ on $\mathcal{S}$, MCT guarantees:
$$
\mathbb{E}_{\mu}[V^*] = \mathbb{E}_{\mu}[\lim_{n \to \infty} V_n] = \lim_{n \to \infty} \mathbb{E}_{\mu}[V_n]
$$

This justifies approximating the optimal expected return $\mathbb{E}_{\mu}[V^*]$ by running value iteration for finitely many steps and computing $\mathbb{E}_{\mu}[V_N]$.

**Critical caveat:** MCT requires **non-negativity**. For MDPs with negative rewards, value iteration still converges (by the contraction mapping theorem), but MCT does not directly apply. We must instead use the fact that the Bellman operator is a contraction in the supremum norm, which gives convergence without appealing to MCT. However, for **policy evaluation** with TD learning, where we have stochastic noise, we will need the **Dominated Convergence Theorem** (Day 3) to justify interchanging limits and expectations.

### **Open Question for Further Investigation**

**Question:** In the proof of MCT, we required $f_n$ to be monotone increasing. Can this be relaxed to "eventually monotone" (i.e., $f_n \leq f_{n+1}$ for all $n \geq N$ for some $N$)?

**Answer:** Yes. If $f_n$ is eventually monotone, we can apply MCT to the tail sequence $\{f_n\}_{n \geq N}$, which gives:
$$
\lim_{n \to \infty} \int f_n \, d\mu = \int \left(\lim_{n \to \infty} f_n\right) d\mu
$$

The first $N-1$ terms $\int f_1, \ldots, \int f_{N-1}$ do not affect the limit.

**Deeper question:** What if $f_n$ is "almost monotone" in the sense that $\{x : f_n(x) > f_{n+1}(x)\}$ has measure zero for each $n$? This holds, because we can modify each $f_n$ on a null set without changing its integral, reducing to the standard MCT case. This observation is crucial in stochastic approximation, where iterates are only defined almost surely (i.e., outside of negligible exceptional sets).

---

**End of Day 2 Exercises**

Tomorrow (Day 3), we will prove **Fatou's Lemma** (which we previewed in Exercise 2) and the **Dominated Convergence Theorem**, completing the triumvirate of fundamental convergence results in integration theory.
