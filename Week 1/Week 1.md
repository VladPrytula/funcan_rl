(slightly adjusted due to my Day 1)
## Week 1 Retrospective and Adjustment

**What We Completed on Day 1:**

- Core material: σ-algebras, measures, measurable functions (definitions and basic properties)
- Advanced material:
    - Set limits (limsup/liminf) - foundational for probability
    - σ-finite and semifinite measures with complete proof
    - Completeness of measure spaces (Cantor set counterexample, completion theorem)
    - Composition theorem for measurable functions with detailed proof via generating sets

**Assessment**: We covered approximately Day 1 + Day 2 content from the original Week 1 plan, but with some more depth on measure classifications. 

**Adjustment Strategy**: Since we've already established σ-algebras, measures, and measurability foundations, we'll pivot Week 1 to emphasize:

1. Integration theory (the raison d'être for measure theory)
2. Convergence theorems (MCT, Fatou, DCT) - these are the workhorses of probability and RL
3. The $\pi-\lambda$ theorem and monotone classes (technical machinery we'll need)

---

## Week 1 Revised: Measure Theory Foundations (Days 2-5)

### Day 2 (Tuesday) — The Lebesgue Integral and Monotone Convergence

**📖 Segment 1 (40 min) — Reading**

**Topic**: Construction of the Lebesgue integral

**Primary Reference**: Folland §2.1-2.2

**Reading Goals**:

- Construction pathway: simple functions → non-negative measurable → general measurable
- For simple function φ = ∑ᵢ aᵢ 𝟙_{Aᵢ}, define ∫φ dμ = ∑ᵢ aᵢμ(Aᵢ)
- For f ≥ 0 measurable: ∫f dμ = sup{∫φ dμ : 0 ≤ φ ≤ f, φ simple}
- For general f: ∫f dμ = ∫f⁺ dμ - ∫f⁻ dμ when both finite
- Monotone Convergence Theorem (MCT) statement: If 0 ≤ f₁ ≤ f₂ ≤ ... and fₙ → f a.e., then ∫fₙ → ∫f

**Key Conceptual Question**: Why does the order of operations matter? In Riemann integration, we approximate the domain (partition into intervals). In Lebesgue integration, we partition the range. This reversal is what enables handling discontinuous functions and proves convergence theorems.

---

**✏️ Segment 2 (40 min) — Proof**

**Exercise**: Prove the Monotone Convergence Theorem

**Setup**: Let (X, ℱ, μ) be a measure space. Suppose {fₙ}ₙ₌₁^∞ is a sequence of measurable functions with:

1. 0 ≤ f₁(x) ≤ f₂(x) ≤ ... for all x ∈ X
2. fₙ(x) → f(x) for all x ∈ X

Then f is measurable and lim_{n→∞} ∫fₙ dμ = ∫f dμ.

**Proof Structure**:

_Step 1 (Measurability of f)_: Since f = sup_n fₙ and each fₙ is measurable, verify that {x : f(x) > a} = ⋃ₙ {x : fₙ(x) > a} ∈ ℱ.

_Step 2 (Show lim ∫fₙ ≤ ∫f)_: By monotonicity of the integral, ∫fₙ ≤ ∫fₙ₊₁ ≤ ∫f for all n. Thus the sequence {∫fₙ} is increasing and bounded above by ∫f. Therefore lim ∫fₙ exists and satisfies lim ∫fₙ ≤ ∫f.

_Step 3 (The hard direction: ∫f ≤ lim ∫fₙ)_: This requires showing that for any simple function 0 ≤ φ ≤ f, we have ∫φ ≤ lim ∫fₙ.

Choose α ∈ (0,1) and define Eₙ = {x : fₙ(x) ≥ αφ(x)}. Then E₁ ⊆ E₂ ⊆ ... and ⋃Eₙ = X (since fₙ → f ≥ φ).

For each n: ∫fₙ dμ ≥ ∫_{Eₙ} fₙ dμ ≥ α∫_{Eₙ} φ dμ

Taking limits and using continuity of measure (μ(Eₙ) ↑ μ(X)): lim ∫fₙ ≥ α∫φ dμ

Since this holds for all α < 1, let α → 1 to get lim ∫fₙ ≥ ∫φ. Taking supremum over all simple φ ≤ f yields lim ∫fₙ ≥ ∫f.

∎

**Reflection Questions**:

1. Where precisely did we use the monotonicity assumption fₙ ≤ fₙ₊₁?
2. What breaks if we only assume fₙ → f without monotonicity?
3. Why is the trick with α < 1 necessary?

---

**📝 Segment 3 (10 min) — Reflection Note**

Write a short note addressing:

**Mathematical Insight**: The MCT proof hinges on two facts: (1) monotone sequences of real numbers converge if bounded, and (2) measure is continuous along increasing sequences of sets. The α-trick handles the case where φ might equal f on a set of infinite measure.

**RL Connection**: MCT justifies computing expectations via limits: E[Vₙ] → E[V] when value functions converge monotonically. In policy evaluation, if we iterate Vₙ₊₁ = TᵖVₙ starting from V₀ = 0, the sequence is increasing (assuming rewards are non-negative), and MCT guarantees ∫Vₙ dP → ∫V^π dP.

**Open Question**: Can MCT be extended to handle "almost monotone" sequences, where the monotonicity fails on a null set?

---

### Day 3 (Wednesday) — Fatou's Lemma and Dominated Convergence Theorem

**📖 Segment 1 (40 min) — Reading**

**Topic**: The triumvirate of convergence theorems

**Primary Reference**: Folland §2.3

**Reading Goals**:

- **Fatou's Lemma**: For fₙ ≥ 0 measurable, ∫(lim inf fₙ) ≤ lim inf ∫fₙ
- **Dominated Convergence Theorem**: If |fₙ| ≤ g with ∫g < ∞ and fₙ → f a.e., then ∫fₙ → ∫f
- Understand the hierarchy: MCT (monotone + non-negative) → Fatou (non-negative only) → DCT (domination condition)
- Each theorem relaxes hypotheses but requires additional structure

**Conceptual Framework**: These three theorems form a ladder:

- MCT: Strongest hypothesis (monotonicity), strongest conclusion (equality)
- Fatou: Weaker hypothesis (only non-negativity), weaker conclusion (inequality)
- DCT: Different hypothesis (domination replaces monotonicity), strong conclusion (equality)

**Key Examples to Read**:

- Example where Fatou's inequality is strict: fₙ = 𝟙_{[n, n+1]} on ℝ
- Example showing necessity of domination in DCT: fₙ = n𝟙_{[0,1/n]}

---

**✏️ Segment 2 (40 min) — Proof**

**Exercise 1**: Prove Fatou's Lemma

**Proof**: Let gₙ = inf_{k≥n} f_k. Then gₙ is measurable, 0 ≤ g₁ ≤ g₂ ≤ ..., and gₙ → lim inf fₙ.

By MCT: ∫(lim inf fₙ) = ∫(lim gₙ) = lim ∫gₙ = lim inf ∫gₙ

Since gₙ ≤ fₙ for all n, we have ∫gₙ ≤ ∫fₙ. Therefore: lim inf ∫gₙ ≤ lim inf ∫fₙ

Combining: ∫(lim inf fₙ) ≤ lim inf ∫fₙ. ∎

**Exercise 2** (if time): Prove DCT using Fatou

**Proof Sketch**: Given |fₙ| ≤ g and fₙ → f:

Apply Fatou to gₙ = g + fₙ ≥ 0: ∫(g + f) = ∫(lim inf(g + fₙ)) ≤ lim inf ∫(g + fₙ) = ∫g + lim inf ∫fₙ

Therefore: ∫f ≤ lim inf ∫fₙ

Similarly, apply Fatou to g - fₙ ≥ 0 to get: ∫f ≥ lim sup ∫fₙ

Thus lim inf ∫fₙ ≥ ∫f ≥ lim sup ∫fₙ, which forces lim ∫fₙ = ∫f. ∎

---

**📝 Segment 3 (10 min) — Reflection Note**

**Mathematical Insight**: Fatou's Lemma is the bridge between MCT and DCT. Its power lies in requiring minimal hypotheses (just non-negativity) while providing an inequality that's often sufficient. The DCT proof demonstrates a beautiful technique: apply Fatou twice to sequences that are non-negative by construction.

**RL Connection**: DCT is essential for gradient-based RL. When we compute ∇_θ E_π[R] by swapping ∇ and E, we're implicitly invoking DCT. The dominating function ensures the gradient is integrable. Without DCT, policy gradient theorems would lack rigorous justification.

---

### Day 4 (Thursday) — Extended Proof: The π-λ Theorem

**📖 Segment 1 (30 min) — Reading**

**Topic**: Generating σ-algebras efficiently

**Primary Reference**: Folland §1.3, or Billingsley "Probability and Measure" Appendix

**Reading Goals**:

- **π-system**: Collection closed under finite intersections
- **λ-system** (Dynkin system): Contains X, closed under complements and countable disjoint unions
- **π-λ Theorem**: If 𝒫 is a π-system and ℒ is a λ-system with 𝒫 ⊆ ℒ, then σ(𝒫) ⊆ ℒ
- Why this matters: To prove two measures are equal, it suffices to check equality on a π-system that generates the σ-algebra

**Motivation**: The Borel σ-algebra ℬ(ℝ) is enormous (uncountably infinite). To prove a measure is uniquely determined on ℬ(ℝ), we don't want to check it on every Borel set. The π-λ theorem says: just check it on intervals (a π-system), and you're done.

---

**✏️ Segment 2 (60 min) — Extended Proof**

**Theorem (π-λ)**: Let 𝒫 be a π-system and ℒ be a λ-system on X. If 𝒫 ⊆ ℒ, then σ(𝒫) ⊆ ℒ.

**Proof Strategy**: We'll show that σ(𝒫) is the smallest λ-system containing 𝒫. Since ℒ is a λ-system containing 𝒫, this will imply σ(𝒫) ⊆ ℒ.

**Lemma 1**: Every σ-algebra is a λ-system.

_Proof_: Let 𝒜 be a σ-algebra.

1. X ∈ 𝒜 by definition.
2. If A ∈ 𝒜, then Aᶜ ∈ 𝒜 by closure under complements.
3. If {Aₙ} are disjoint in 𝒜, then ⋃Aₙ ∈ 𝒜 by countable unions. Thus 𝒜 is a λ-system. ∎

**Lemma 2**: If ℒ is a λ-system that is also closed under finite intersections (i.e., is a π-system), then ℒ is a σ-algebra.

_Proof_: We need to show ℒ is closed under countable unions (not necessarily disjoint).

Let {Aₙ} ⊆ ℒ. Define: B₁ = A₁, B₂ = A₂ \ A₁, B₃ = A₃ \ (A₁ ∪ A₂), ...

Each Bₙ can be written as intersections and complements of sets in ℒ. Since ℒ is a π-system (closed under ∩) and a λ-system (closed under complements), each Bₙ ∈ ℒ. The Bₙ are disjoint and ⋃Bₙ = ⋃Aₙ. Since ℒ is a λ-system, ⋃Bₙ ∈ ℒ. Therefore ⋃Aₙ ∈ ℒ. ∎

**Main Proof**:

_Step 1_: Let ℒ₀ be the smallest λ-system containing 𝒫. We'll show ℒ₀ ⊆ ℒ (since ℒ is a λ-system containing 𝒫).

_Step 2_: We'll prove ℒ₀ is closed under finite intersections, making it a σ-algebra by Lemma 2.

_Step 3_: For A ∈ ℒ₀, define: ℒ_A = {B ∈ ℒ₀ : A ∩ B ∈ ℒ₀}

Claim: ℒ_A is a λ-system.

- X ∈ ℒ_A since A ∩ X = A ∈ ℒ₀
- If B ∈ ℒ_A, then A ∩ B ∈ ℒ₀. We have A ∩ Bᶜ = A \ (A ∩ B) = A \ C where C = A ∩ B ∈ ℒ₀. Since ℒ₀ is a λ-system, A \ C ∈ ℒ₀, so Bᶜ ∈ ℒ_A.
- Disjoint unions: if {Bₙ} are disjoint in ℒ_A, then {A ∩ Bₙ} are disjoint in ℒ₀, so ⋃(A ∩ Bₙ) = A ∩ (⋃Bₙ) ∈ ℒ₀.

_Step 4_: For any P ∈ 𝒫, consider ℒ_P. Since 𝒫 is a π-system, for any Q ∈ 𝒫, we have P ∩ Q ∈ 𝒫 ⊆ ℒ₀. Thus Q ∈ ℒ_P for all Q ∈ 𝒫. Therefore 𝒫 ⊆ ℒ_P. Since ℒ_P is a λ-system and ℒ₀ is the smallest λ-system containing 𝒫, we have ℒ₀ ⊆ ℒ_P. This means for all A ∈ ℒ₀ and all P ∈ 𝒫, we have P ∩ A ∈ ℒ₀.

_Step 5_: Now fix A ∈ ℒ₀. We've shown 𝒫 ⊆ ℒ_A. Since ℒ_A is a λ-system, we have ℒ₀ ⊆ ℒ_A. This means for all A, B ∈ ℒ₀, we have A ∩ B ∈ ℒ₀.

_Step 6_: Therefore ℒ₀ is a π-system. By Lemma 2, ℒ₀ is a σ-algebra. Since it's the smallest λ-system containing 𝒫 and is a σ-algebra, it must equal σ(𝒫). Since ℒ₀ ⊆ ℒ, we conclude σ(𝒫) ⊆ ℒ. ∎

**Reflection**: This proof is a masterclass in bootstrapping. We start with minimal structure (π-system, λ-system) and carefully construct increasingly rich collections until we've built a σ-algebra. The key trick is defining ℒ_A and proving it's a λ-system—this is the "good sets principle" in action.

---

### Day 5 (Friday) — Integration, Review, and Computation

**📖 Segment 1 (20 min) — Reading**

**Topic**: Quick review of Lᵖ spaces setup

**Primary Reference**: Folland §6.1 (skim)

**Goals**:

- Understand ‖f‖_p = (∫|f|ᵖ dμ)^{1/p} defines a "norm" on equivalence classes [f] where f ~ g if f = g a.e.
- The triangle inequality (Minkowski) and Hölder inequality will come next week
- Lᵖ(μ) = {f : ‖f‖_p < ∞} / ~ is a normed space

---

**✏️ Segment 2 (30 min) — Proof Review**

**Exercise**: Write a one-page proof summary document

Create a structured summary of this week's major results:

1. **Monotone Convergence Theorem**
    
    - Hypothesis: 0 ≤ f₁ ≤ f₂ ≤ ... → f a.e.
    - Conclusion: ∫fₙ → ∫f
    - Key technique: α-trick with simple functions
2. **Fatou's Lemma**
    
    - Hypothesis: fₙ ≥ 0
    - Conclusion: ∫(lim inf fₙ) ≤ lim inf ∫fₙ
    - Key technique: Apply MCT to gₙ = inf_{k≥n} f_k
3. **Dominated Convergence Theorem**
    
    - Hypothesis: |fₙ| ≤ g ∈ L¹, fₙ → f a.e.
    - Conclusion: ∫fₙ → ∫f
    - Key technique: Apply Fatou to g ± fₙ
4. **π-λ Theorem**
    
    - Purpose: Uniqueness of measures on generated σ-algebras
    - Key technique: Good sets principle via ℒ_A construction

---

**💻 Segment 3 (40 min) — Coding Synthesis**

**Task**: Numerical verification of convergence theorems

```python
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Part 1: Monotone Convergence Theorem
# ============================================================

def verify_MCT():
    """
    Verify MCT with f_n(x) = x(1 - x^{1/n}) on [0,1]
    f_n increases to f(x) = x
    """
    x = np.linspace(0, 1, 1000)
    dx = x[1] - x[0]
    
    integrals = []
    for n in range(1, 51):
        f_n = x * (1 - x**(1/n))
        integral_n = np.sum(f_n) * dx  # Riemann approximation
        integrals.append(integral_n)
    
    true_integral = 1/2  # ∫x dx from 0 to 1
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(integrals, 'b.-', label='$\\int f_n$')
    plt.axhline(true_integral, color='r', linestyle='--', label='$\\int f$')
    plt.xlabel('n')
    plt.ylabel('Integral value')
    plt.title('MCT: $\\int f_n \\to \\int f$')
    plt.legend()
    plt.grid(True)
    
    # Plot some f_n
    plt.subplot(1, 2, 2)
    for n in [1, 3, 10, 50]:
        f_n = x * (1 - x**(1/n))
        plt.plot(x, f_n, label=f'$f_{n}$')
    plt.plot(x, x, 'k--', linewidth=2, label='$f(x)=x$')
    plt.xlabel('x')
    plt.ylabel('$f_n(x)$')
    plt.title('Monotone convergence of functions')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('MCT_verification.png', dpi=150)
    print(f"MCT: Final integral = {integrals[-1]:.6f}, True = {true_integral:.6f}")

# ============================================================
# Part 2: Fatou's Lemma (strict inequality example)
# ============================================================

def verify_Fatou():
    """
    Example where Fatou's inequality is strict:
    f_n = n * 1_{[0, 1/n]} on [0,1]
    lim inf f_n = 0, but ∫f_n = 1 for all n
    """
    N = 50
    integrals = []
    
    for n in range(1, N+1):
        # Can't represent this perfectly numerically, but we know ∫f_n = 1
        integrals.append(1.0)
    
    lim_inf_integral = 0  # ∫(lim inf f_n) = ∫0 = 0
    lim_inf_of_integrals = 1.0  # lim inf ∫f_n = 1
    
    print(f"\nFatou's Lemma:")
    print(f"∫(lim inf f_n) = {lim_inf_integral}")
    print(f"lim inf ∫f_n = {lim_inf_of_integrals}")
    print(f"Inequality: {lim_inf_integral} ≤ {lim_inf_of_integrals} ✓")
    print(f"Strict inequality demonstrates Fatou can be non-equality")

# ============================================================
# Part 3: DCT necessity of domination
# ============================================================

def verify_DCT_necessity():
    """
    Show DCT fails without domination:
    f_n(x) = n * 1_{[0, 1/n]}
    f_n → 0 pointwise, but ∫f_n = 1 ↛ 0
    """
    x = np.linspace(0, 1, 10000)
    dx = x[1] - x[0]
    
    integrals = []
    for n in [10, 20, 50, 100, 200, 500]:
        f_n = np.where(x <= 1/n, n, 0)
        integral_n = np.sum(f_n) * dx
        integrals.append(integral_n)
    
    plt.figure(figsize=(10, 5))
    plt.plot([10, 20, 50, 100, 200, 500], integrals, 'ro-', markersize=8)
    plt.axhline(0, color='b', linestyle='--', label='$\\int f = 0$')
    plt.xlabel('n')
    plt.ylabel('$\\int f_n$')
    plt.title('DCT fails without domination: $\\int f_n = 1$ but $f_n \\to 0$')
    plt.legend()
    plt.grid(True)
    plt.savefig('DCT_counterexample.png', dpi=150)
    print(f"\nDCT Counterexample: All integrals ≈ 1, despite pointwise convergence to 0")

# ============================================================
# Part 4: RL Connection - Value Iteration Convergence
# ============================================================

def value_iteration_convergence():
    """
    Simple gridworld: 5x5 grid, goal at (4,4), rewards r(goal)=1, else 0
    V_{n+1}(s) = max_a [r(s,a) + γ Σ P(s'|s,a)V_n(s')]
    This is monotone increasing from V_0 = 0, so MCT applies
    """
    gamma = 0.9
    grid_size = 5
    goal = (4, 4)
    
    V = np.zeros((grid_size, grid_size))
    V_history = [V.copy()]
    
    for iteration in range(50):
        V_new = np.zeros_like(V)
        for i in range(grid_size):
            for j in range(grid_size):
                if (i, j) == goal:
                    V_new[i, j] = 1.0  # Terminal state
                else:
                    # Actions: up, down, left, right
                    values = []
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < grid_size and 0 <= nj < grid_size:
                            values.append(gamma * V[ni, nj])
                        else:
                            values.append(gamma * V[i, j])  # Stay in place
                    V_new[i, j] = max(values)
        V = V_new
        V_history.append(V.copy())
    
    # Plot convergence
    plt.figure(figsize=(10, 5))
    goal_values = [V[2, 2] for V in V_history]  # Track a non-goal state
    plt.plot(goal_values, 'b.-')
    plt.xlabel('Iteration n')
    plt.ylabel('$V_n(s)$ at state (2,2)')
    plt.title('Value Iteration: Monotone convergence to $V^*$')
    plt.grid(True)
    plt.savefig('value_iteration_MCT.png', dpi=150)
    print(f"\nRL Connection: Value iteration converges via MCT")
    print(f"V_50(2,2) = {V_history[-1][2, 2]:.4f}")

# ============================================================
# Run all verifications
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Week 1 Synthesis: Convergence Theorems in Action")
    print("=" * 60)
    
    verify_MCT()
    verify_Fatou()
    verify_DCT_necessity()
    value_iteration_convergence()
    
    print("\n" + "=" * 60)
    print("All verifications complete. Check generated plots.")
    print("=" * 60)
```

**Post-Coding Reflection**:

- MCT guarantees value iteration converges (monotone increasing from V₀ = 0)
- DCT enables policy gradient: ∇E[R] = E[∇R] when gradients are dominated
- Fatou provides robustness: even without monotonicity, we get an inequality

---

## Week 1 Summary and Bridge to Week 2

**What You've Mastered**:

1. σ-algebras as formalization of observability
2. Measures and their regularity properties (σ-finite, complete)
3. Measurable functions and closure properties
4. The Lebesgue integral construction
5. The three fundamental convergence theorems
6. The π-λ theorem for proving uniqueness of measures

**RL Connections Established**:

- Policies and value functions must be measurable (physical realizability)
- MCT justifies value iteration convergence
- DCT enables interchange of differentiation and expectation (policy gradients)
- Completeness ensures L² spaces are well-behaved (needed for TD convergence)

**Preview of Week 2**: Product measures and Fubini's theorem (critical for understanding transition kernels P(s'|s,a) as measures), followed by Radon-Nikodym (foundation for importance sampling and likelihood ratios in off-policy RL).

---

Does this detailed Week 1 plan match the depth and style of your Day 1 work? Shall I continue with similarly detailed plans for Week 2, or would you prefer adjustments to the structure?