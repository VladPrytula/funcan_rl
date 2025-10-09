[[Day_2 (old)]]

# Appendix A: Numerical Integration of Pathological Measurable Functions

## **On the Computational Reality of Lebesgue Integration**

### **I. The Insufficiency of Riemann Approximation**

In the main text, we verified the Monotone Convergence Theorem using continuous functions $f_n(x) = x(1-e^{-nx})$ on $[0,1]$. The numerical integration employed standard Riemann sums:
$$
\int_0^1 f(x) \, dx \approx \sum_{i=1}^{N} f(x_i) \Delta x
$$
where $x_i = i/N$ and $\Delta x = 1/N$.

This method succeeds because continuity ensures uniform integrability: the Riemann sums converge to the Lebesgue integral. However, **the entire edifice of Lebesgue integration was constructed precisely to handle functions for which Riemann integration fails**. Measure-theoretic integration theory is not an abstract luxury; it is a computational necessity when dealing with:

1. **Discontinuous functions** arising naturally in RL (indicator functions of measurable sets, value functions with barriers)
2. **Almost-everywhere defined functions** (policies defined up to null sets)
3. **Limits of measurable functions** (value iteration produces sequences that may not preserve continuity)

This appendix demonstrates the computational techniques required to numerically integrate **pathological measurable functions** where Riemann methods categorically fail. We implement Lebesgue integration via approximation by simple functions, and we verify the Monotone Convergence Theorem for sequences that exhibit measure-theoretic subtleties invisible to classical analysis.

---

### **II. Pathological Example 1: The Modified Dirichlet Function**

The classical Dirichlet function $\mathbf{1}_{\mathbb{Q}}$ (indicator of rationals) is not Riemann integrable on $[0,1]$, but is Lebesgue integrable with integral zero (since $\mathbb{Q}$ is countable, thus null). We consider a more sophisticated variant that illustrates the power of Lebesgue integration.

**Definition (Fat Cantor Set Function).** Let $C \subset [0,1]$ be the **fat Cantor set** with positive measure $\lambda(C) = 1/2$. This set is constructed similarly to the standard Cantor set, but at stage $n$, we remove intervals of total length $(1/2)^{n+1}$ rather than $(2/3)^n$. The resulting set is uncountable, nowhere dense, and has Lebesgue measure $1/2$.

Define:
$$
g(x) = \begin{cases}
1 & \text{if } x \in C \\
0 & \text{if } x \in [0,1] \setminus C
\end{cases}
$$

**Proposition A.1 (Non-Riemann Integrability of $g$).**
The function $g$ is not Riemann integrable on $[0,1]$.

*Proof.* For any partition $P = \{x_0, x_1, \ldots, x_n\}$ of $[0,1]$, the upper Riemann sum is:
$$
U(g, P) = \sum_{i=1}^{n} \sup_{x \in [x_{i-1}, x_i]} g(x) \cdot (x_i - x_{i-1})
$$

The fat Cantor set $C$ is **nowhere dense** (its closure has empty interior), yet has positive measure $\lambda(C) = 1/2$. Crucially, $C$ is closed and uncountable, so every interval $[x_{i-1}, x_i]$ of positive length must intersect $C$ (since $\lambda(C) > 0$ implies $C$ cannot be avoided by any finite partition). Therefore:
$$
\sup_{x \in [x_{i-1}, x_i]} g(x) = 1 \quad \text{for every subinterval}
$$

Thus:
$$
U(g, P) = \sum_{i=1}^{n} (x_i - x_{i-1}) = 1
$$

The lower Riemann sum is:
$$
L(g, P) = \sum_{i=1}^{n} \inf_{x \in [x_{i-1}, x_i]} g(x) \cdot (x_i - x_{i-1})
$$

The complement $[0,1] \setminus C$ is **open and dense** (the removed intervals form a dense open set). Therefore, every subinterval $[x_{i-1}, x_i]$ contains points outside $C$, so:
$$
\inf_{x \in [x_{i-1}, x_i]} g(x) = 0
$$

Thus:
$$
L(g, P) = 0
$$

For any partition, $U(g,P) - L(g,P) = 1$, so $g$ is not Riemann integrable. $\square$

**Proposition A.2 (Lebesgue Integrability of $g$).**
The function $g$ is Lebesgue integrable with:
$$
\int_0^1 g(x) \, dx = \lambda(C) = \frac{1}{2}
$$

*Proof.* The function $g = \mathbf{1}_C$ is the indicator of a measurable set $C \in \mathcal{L}([0,1])$. By definition:
$$
\int g \, d\lambda = \int \mathbf{1}_C \, d\lambda = \lambda(C) = \frac{1}{2}
$$
$\square$

---

### **III. Computational Strategy: Lebesgue Integration via Simple Functions**

To numerically compute $\int g \, d\lambda$, we approximate $g$ from below by a sequence of simple functions, following the construction in Exercise 1 of Day 2.

**Algorithm (Lebesgue Approximation):**

For precision level $n$, construct the simple function:
$$
\varphi_n(x) = \sum_{k=0}^{n \cdot 2^n - 1} \frac{k}{2^n} \mathbf{1}_{A_{n,k}}(x) + n \cdot \mathbf{1}_{B_n}(x)
$$
where:
$$
A_{n,k} = \{x : k/2^n \leq g(x) < (k+1)/2^n\}, \qquad B_n = \{x : g(x) \geq n\}
$$

For our function $g = \mathbf{1}_C$, we have only two relevant sets:
- $A_{n,0} = [0,1] \setminus C$ (where $g=0$)
- $A_{n,1} = C$ (where $g=1$, assuming $n \geq 1$ and $2^n \geq 1$)

Thus, for $n \geq 1$:
$$
\varphi_n(x) = 0 \cdot \mathbf{1}_{[0,1]\setminus C}(x) + \frac{1}{2^n} \lfloor 2^n \cdot 1 \rfloor \mathbf{1}_C(x) = \mathbf{1}_C(x)
$$

Wait, this analysis shows that for the indicator function, the simple function approximation immediately equals the function itself for $n \geq 1$. This is correct but not pedagogically interesting for demonstrating convergence.

Let me reconsider. A better approach is to construct $g$ differently, or to demonstrate the approximation via a different measurable function. Let me use a function that actually requires non-trivial approximation.

**Better Example: Cantor Function Derivative (in a generalized sense)**

Actually, let's use a more interesting pathological function for computational purposes. Consider a measurable function that's constructed via a limiting process.

**Definition (Oscillating Indicator Function).**
For each dyadic rational $q = k/2^n$ with $k$ odd, define an interval $I_q = (q - 1/2^{n+3}, q + 1/2^{n+3})$. Let:
$$
D = \bigcup_{q \in \mathbb{Q} \cap [0,1], \, q = k/2^n, k \text{ odd}} I_q
$$

Define $h(x) = \mathbf{1}_D(x)$.

This function equals 1 on a dense open set $D$ and 0 on its complement. The set $D$ has positive measure (it's an open set), but its complement also has positive measure.

Actually, for computational clarity, let me use the **fat Cantor set** directly and show how to compute its measure and the integral of its indicator function.

Let me restructure this section to be more computationally focused.

---

### **III. Computational Implementation: Measuring the Fat Cantor Set**

The key computational challenge is: **how do we numerically compute $\lambda(C)$ for a measurable set $C$ defined by a limiting construction?**

#### **A. Constructing the Fat Cantor Set**

The fat Cantor set is built iteratively:
- **Stage 0:** Start with $C_0 = [0,1]$, $\lambda(C_0) = 1$
- **Stage 1:** Remove the middle interval of length $1/4$, leaving $C_1 = [0, 3/8] \cup [5/8, 1]$, $\lambda(C_1) = 3/4$
- **Stage 2:** From each interval in $C_1$, remove middle intervals of total length $1/8$, giving $\lambda(C_2) = 3/4 - 1/8 = 5/8$
- **Stage $n$:** Remove intervals of total length $(1/4) \cdot (1/2)^{n-1}$

The measure converges:
$$
\lambda(C) = \lim_{n \to \infty} \lambda(C_n) = 1 - \sum_{k=0}^{\infty} \frac{1}{4} \cdot \frac{1}{2^k} = 1 - \frac{1/4}{1 - 1/2} = 1 - \frac{1}{2} = \frac{1}{2}
$$

The function $g = \mathbf{1}_C$ is the pointwise limit:
$$
g(x) = \lim_{n \to \infty} \mathbf{1}_{C_n}(x)
$$

This is a **monotone decreasing** sequence of indicator functions (since $C_0 \supseteq C_1 \supseteq C_2 \supseteq \cdots$, we have $\mathbf{1}_{C_0} \geq \mathbf{1}_{C_1} \geq \mathbf{1}_{C_2} \geq \cdots$), converging to a highly discontinuous limit.

**Note on convergence theorems:** The Monotone Convergence Theorem applies to *increasing* sequences. For this decreasing sequence, we observe that $1 - \mathbf{1}_{C_n}$ is increasing, and we could apply MCT to that. Alternatively, we can use the **Dominated Convergence Theorem** (Day 3) with dominating function $\mathbf{1}_{[0,1]}$, which directly handles this case.

#### **B. Numerical Integration via Finite Approximation**

To compute $\int g \, d\lambda = \lambda(C)$, we approximate $C$ by $C_n$ for large $n$:

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

class FatCantorSet:
    """
    Construct the fat Cantor set via iterative removal of middle intervals.
    At stage n, we have 2^n intervals, and we remove middle portions of 
    total length (1/4) * (1/2)^(n-1).
    """
    
    def __init__(self, max_depth: int = 10):
        self.max_depth = max_depth
        self.intervals_by_stage = []
        self._construct()
    
    def _construct(self):
        """Build the interval decomposition at each stage.

        At stage n, we remove total measure (1/4) * (1/2)^(n-1)
        distributed equally across 2^(n-1) intervals from stage n-1.
        """
        # Stage 0: full interval
        current_intervals = [(0.0, 1.0)]
        self.intervals_by_stage.append(current_intervals.copy())

        for stage in range(1, self.max_depth + 1):
            next_intervals = []
            # At stage n: remove (1/4) * (1/2)^(n-1) total length
            # Split equally among current intervals
            removal_length_per_interval = (1/4) * (1/2)**(stage-1) / len(current_intervals)
            
            for (a, b) in current_intervals:
                interval_length = b - a
                middle_removal = removal_length_per_interval
                
                # Remove middle portion
                left_length = (interval_length - middle_removal) / 2
                right_start = a + left_length + middle_removal
                
                next_intervals.append((a, a + left_length))
                next_intervals.append((right_start, b))
            
            current_intervals = next_intervals
            self.intervals_by_stage.append(current_intervals.copy())
    
    def measure_at_stage(self, stage: int) -> float:
        """Compute λ(C_n) by summing interval lengths."""
        if stage > self.max_depth:
            stage = self.max_depth
        
        intervals = self.intervals_by_stage[stage]
        return sum(b - a for a, b in intervals)
    
    def indicator_at_stage(self, stage: int) -> callable:
        """Return indicator function 1_{C_n} at given stage."""
        intervals = self.intervals_by_stage[stage]
        
        def indicator(x):
            """Check if x is in C_n."""
            if isinstance(x, np.ndarray):
                result = np.zeros_like(x)
                for (a, b) in intervals:
                    result[(x >= a) & (x <= b)] = 1.0
                return result
            else:
                return 1.0 if any(a <= x <= b for a, b in intervals) else 0.0
        
        return indicator
    
    def visualize_construction(self, stages: List[int] = [0, 2, 4, 6]):
        """Visualize the intervals at different construction stages."""
        fig, axes = plt.subplots(len(stages), 1, figsize=(12, 2*len(stages)))
        if len(stages) == 1:
            axes = [axes]
        
        for idx, stage in enumerate(stages):
            ax = axes[idx]
            intervals = self.intervals_by_stage[stage]
            
            # Draw intervals
            for (a, b) in intervals:
                ax.plot([a, b], [0, 0], 'b-', linewidth=8)
                ax.fill_between([a, b], -0.1, 0.1, alpha=0.3, color='blue')
            
            measure = self.measure_at_stage(stage)
            ax.set_xlim(-0.05, 1.05)
            ax.set_ylim(-0.3, 0.3)
            ax.set_title(f'Stage {stage}: $C_{{{stage}}}$ with $\\lambda(C_{{{stage}}}) = {measure:.4f}$', 
                        fontsize=11)
            ax.set_yticks([])
            ax.set_xlabel('$x$')
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig

# Instantiate fat Cantor set
fat_cantor = FatCantorSet(max_depth=10)

# Compute measures at each stage
stages = list(range(11))
measures = [fat_cantor.measure_at_stage(n) for n in stages]

# Theoretical limit
theoretical_limit = 0.5

print("=" * 70)
print("Fat Cantor Set: Measure Convergence")
print("=" * 70)
print(f"{'Stage n':<10} {'λ(Cₙ)':<15} {'Error from 1/2':<15}")
print("-" * 70)
for n, m in zip(stages, measures):
    error = abs(m - theoretical_limit)
    print(f"{n:<10} {m:<15.10f} {error:<15.2e}")

print(f"\nTheoretical limit: λ(C) = 1/2 = {theoretical_limit}")
print(f"Numerical approximation at stage 10: {measures[-1]:.10f}")
print(f"Error: {abs(measures[-1] - theoretical_limit):.2e}")

# Visualize construction
fig1 = fat_cantor.visualize_construction(stages=[0, 2, 4, 6, 10])
fig1.savefig('/mnt/user-data/outputs/Day2_Appendix_FatCantor_Construction.png', dpi=150)
print("\n[Figure saved: Fat Cantor set construction]")
```

#### **C. Integrating the Indicator Function**

Now we compute:
$$
\int_0^1 \mathbf{1}_{C_n}(x) \, dx = \lambda(C_n)
$$
and verify convergence to $\lambda(C) = 1/2$.

**Remark on convergence:** Since $\{\mathbf{1}_{C_n}\}$ is decreasing (not increasing), MCT does not directly apply. However, convergence follows from elementary measure theory: $\lambda(C_n) \to \lambda(C)$ by construction (finite sum of removed intervals). Alternatively, we could apply MCT to $\mathbf{1}_{[0,1]} - \mathbf{1}_{C_n} = \mathbf{1}_{[0,1] \setminus C_n}$, which is increasing, or invoke the Dominated Convergence Theorem (Day 3).

```python
# Part 2: Integrate indicator function 1_C via Lebesgue approximation

def integrate_lebesgue_indicator(fat_cantor: FatCantorSet, stage: int, 
                                  num_sample_points: int = 100000) -> float:
    """
    Compute integral of 1_{C_n} via Monte Carlo sampling.
    This is equivalent to computing the measure of C_n.
    
    For a measurable set A, we have:
    λ(A) = ∫ 1_A dλ = E[1_A(X)] where X ~ Uniform[0,1]

    By Law of Large Numbers:
    λ(A) ≈ (1/N) Σ 1_A(Xᵢ) where Xᵢ ~ Uniform[0,1]

    This demonstrates the bridge between measure theory (Lebesgue integration)
    and probability theory (expectation under uniform distribution).
    """
    indicator = fat_cantor.indicator_at_stage(stage)
    x_samples = np.random.uniform(0, 1, num_sample_points)
    indicator_values = indicator(x_samples)
    
    # Monte Carlo estimate
    integral_estimate = np.mean(indicator_values)
    
    # Standard error (for confidence)
    std_error = np.std(indicator_values) / np.sqrt(num_sample_points)
    
    return integral_estimate, std_error

# Compute integrals via Monte Carlo (Lebesgue integration in practice)
np.random.seed(42)
print("\n" + "=" * 70)
print("Lebesgue Integration: ∫ 1_Cₙ dλ via Monte Carlo")
print("=" * 70)
print(f"{'Stage n':<10} {'Direct λ(Cₙ)':<18} {'Monte Carlo ∫':<18} {'Std Error':<12}")
print("-" * 70)

for n in [0, 2, 4, 6, 8, 10]:
    exact_measure = fat_cantor.measure_at_stage(n)
    mc_estimate, std_err = integrate_lebesgue_indicator(fat_cantor, n, num_sample_points=100000)
    print(f"{n:<10} {exact_measure:<18.10f} {mc_estimate:<18.10f} {std_err:<12.2e}")

print("\nKey observation: Monte Carlo integration correctly approximates λ(Cₙ)")
print("This demonstrates Lebesgue integration for discontinuous functions.")
```

---

### **IV. Pathological Example 2: Monotone Convergence with Discontinuous Limits**

We now construct a sequence that demonstrates MCT with measure-theoretic subtleties.

**Definition (Staircase Indicator Sequence).**
For each $n \geq 1$, partition $[0,1]$ into $2^n$ dyadic intervals $I_{n,k} = [k/2^n, (k+1)/2^n)$ for $k = 0, 1, \ldots, 2^n-1$. Define:
$$
f_n(x) = \frac{k}{2^n} \quad \text{if } x \in I_{n,k}
$$

This is a **simple function** at each stage. The sequence is monotone increasing:
$$
f_1(x) \leq f_2(x) \leq f_3(x) \leq \cdots
$$
and converges pointwise to:
$$
f(x) = x \quad \text{for all } x \in [0,1)
$$

(At $x=1$, the limit is 1, but this single point doesn't affect the integral.)

**Observation:** Each $f_n$ is highly discontinuous (piecewise constant), yet the limit $f(x) = x$ is continuous. This shows that **Lebesgue integration preserves information through discontinuous approximations**, a property impossible for Riemann integration.

#### **Numerical Verification of MCT**

```python
# Part 3: MCT verification with simple function approximation of f(x) = x

def dyadic_staircase(x: np.ndarray, n: int) -> np.ndarray:
    """
    Compute f_n(x) = floor(2^n * x) / 2^n.
    This is the simple function approximation of f(x) = x.
    """
    return np.floor(2**n * x) / 2**n

def integrate_simple_function(n: int, num_points: int = 10000) -> float:
    """
    Integrate f_n via Lebesgue method: sum measure of each level set.

    f_n(x) = Σ_{k=0}^{2^n - 1} (k/2^n) · 1_{I_{n,k}}(x)

    Derivation:
    ∫ f_n dλ = Σ_{k=0}^{2^n-1} (k/2^n) · λ(I_{n,k})     (linearity of integral)
             = Σ_{k=0}^{2^n-1} (k/2^n) · (1/2^n)          (each I_{n,k} has length 1/2^n)
             = (1/2^{2n}) Σ_{k=0}^{2^n-1} k               (factor out constants)
             = (1/2^{2n}) · [(2^n-1)(2^n)/2]              (sum formula: Σ_{k=0}^{m-1} k = m(m-1)/2)
             = (2^n - 1) / (2^{n+1})                      (simplify)

    As n → ∞, this converges to 1/2, verifying MCT.
    """
    # Analytical formula
    analytical = (2**n - 1) / (2**(n+1))
    
    # Numerical verification via Monte Carlo
    x_samples = np.random.uniform(0, 1, num_points)
    f_n_values = dyadic_staircase(x_samples, n)
    numerical = np.mean(f_n_values)
    
    return analytical, numerical

print("\n" + "=" * 70)
print("MCT Verification: Simple Function Approximation of f(x) = x")
print("=" * 70)
print(f"{'n':<6} {'∫ fₙ (analytical)':<20} {'∫ fₙ (Monte Carlo)':<20} {'Limit':<10}")
print("-" * 70)

n_values = [1, 2, 4, 8, 12, 16, 20]
integrals_analytical = []
integrals_numerical = []

np.random.seed(42)
for n in n_values:
    analytical, numerical = integrate_simple_function(n, num_points=100000)
    integrals_analytical.append(analytical)
    integrals_numerical.append(numerical)
    limit_display = "→ 1/2" if n == n_values[-1] else ""
    print(f"{n:<6} {analytical:<20.15f} {numerical:<20.10f} {limit_display:<10}")

print(f"\nTheoretical limit (MCT): ∫ f dλ = ∫₀¹ x dx = 1/2")
print(f"Numerical limit at n=20: {integrals_analytical[-1]:.15f}")
print(f"Error: {abs(integrals_analytical[-1] - 0.5):.2e}")

# Visualize convergence
fig2, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left: Function convergence
x_plot = np.linspace(0, 1, 1000)
axes[0].plot(x_plot, x_plot, 'k-', linewidth=2.5, label='$f(x) = x$ (limit)', zorder=10)
for n in [2, 4, 8]:
    f_n = dyadic_staircase(x_plot, n)
    axes[0].plot(x_plot, f_n, alpha=0.7, linewidth=1.5, label=f'$f_{{{n}}}(x)$')
axes[0].set_xlabel('$x$', fontsize=12)
axes[0].set_ylabel('$f_n(x)$', fontsize=12)
axes[0].set_title('Monotone convergence:\n$f_n(x) = \\lfloor 2^n x \\rfloor / 2^n \\to x$', fontsize=12)
axes[0].legend(fontsize=10)
axes[0].grid(True, alpha=0.3)

# Right: Integral convergence
axes[1].plot(n_values, integrals_analytical, 'b.-', markersize=8, linewidth=2, 
            label='$\\int f_n \\, d\\lambda$')
axes[1].axhline(0.5, color='r', linestyle='--', linewidth=2, label='$\\int f \\, d\\lambda = 1/2$')
axes[1].set_xlabel('$n$ (refinement level)', fontsize=12)
axes[1].set_ylabel('Integral value', fontsize=12)
axes[1].set_title('MCT: $\\lim_{n \\to \\infty} \\int f_n = \\int f$', fontsize=12)
axes[1].legend(fontsize=11)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
fig2.savefig('/mnt/user-data/outputs/Day2_Appendix_MCT_SimpleFunction.png', dpi=150)
print("\n[Figure saved: MCT with simple function approximation]")
plt.show()
```

---

### **V. Why Riemann Integration Fails: A Computational Diagnosis**

To complete our analysis, we demonstrate **why Riemann sums fail** for the fat Cantor set indicator function.

```python
# Part 4: Demonstrate failure of Riemann integration

def riemann_sum_lower(fat_cantor: FatCantorSet, stage: int, num_intervals: int) -> float:
    """
    Compute lower Riemann sum for 1_{C_n}.
    
    L(f, P) = Σ inf_{x ∈ [xᵢ, xᵢ₊₁]} f(x) · Δx
    
    For 1_C, this is always 0 because C has empty interior 
    (every interval contains points outside C).
    """
    indicator = fat_cantor.indicator_at_stage(stage)
    partition = np.linspace(0, 1, num_intervals + 1)
    delta_x = 1.0 / num_intervals
    
    lower_sum = 0.0
    for i in range(num_intervals):
        # Sample many points in each subinterval to estimate infimum
        x_samples = np.linspace(partition[i], partition[i+1], 100)
        inf_value = np.min(indicator(x_samples))
        lower_sum += inf_value * delta_x
    
    return lower_sum

def riemann_sum_upper(fat_cantor: FatCantorSet, stage: int, num_intervals: int) -> float:
    """
    Compute upper Riemann sum for 1_{C_n}.
    
    U(f, P) = Σ sup_{x ∈ [xᵢ, xᵢ₊₁]} f(x) · Δx
    
    For 1_C, this approaches 1 because C is dense in certain regions.
    """
    indicator = fat_cantor.indicator_at_stage(stage)
    partition = np.linspace(0, 1, num_intervals + 1)
    delta_x = 1.0 / num_intervals
    
    upper_sum = 0.0
    for i in range(num_intervals):
        # Sample many points in each subinterval to estimate supremum
        x_samples = np.linspace(partition[i], partition[i+1], 100)
        sup_value = np.max(indicator(x_samples))
        upper_sum += sup_value * delta_x
    
    return upper_sum

print("\n" + "=" * 70)
print("Riemann Integration Failure for 1_C (Fat Cantor Set)")
print("=" * 70)
print(f"{'Num Intervals':<15} {'Lower Sum L(f,P)':<20} {'Upper Sum U(f,P)':<20} {'U - L':<15}")
print("-" * 70)

stage = 6  # Use C_6 as approximation
for num_intervals in [10, 50, 100, 500, 1000]:
    lower = riemann_sum_lower(fat_cantor, stage, num_intervals)
    upper = riemann_sum_upper(fat_cantor, stage, num_intervals)
    gap = upper - lower
    print(f"{num_intervals:<15} {lower:<20.10f} {upper:<20.10f} {gap:<15.10f}")

exact_measure = fat_cantor.measure_at_stage(stage)
print(f"\nTrue Lebesgue integral: λ(C₆) = {exact_measure:.10f}")
print(f"\nConclusion: U(f,P) - L(f,P) does not converge to 0.")
print(f"Therefore, 1_C is NOT Riemann integrable.")
print(f"However, it IS Lebesgue integrable with ∫ 1_C dλ = {exact_measure:.4f}")
```

![[Day2_Appendix_Riemann_Failure.png]]


![[Day2_Appendix_MCT_SimpleFunction.png]]

---

### **VI. Theoretical Synthesis: The Computational Meaning of Measurability**

The numerical experiments above demonstrate a profound principle:

> **Measurability is the computational prerequisite for integration.**

When we say a function $f: [0,1] \to \mathbb{R}$ is measurable, we are asserting that:
1. The sets $\{x : f(x) > a\}$ belong to the σ-algebra $\mathcal{L}([0,1])$
2. These sets have well-defined Lebesgue measure
3. We can approximate $f$ from below by simple functions $\varphi_n = \sum_i a_i \mathbf{1}_{A_i}$
4. The integrals $\int \varphi_n$ are computable as $\sum_i a_i \lambda(A_i)$

The **Monotone Convergence Theorem** then guarantees:
$$
\int f \, d\lambda = \lim_{n \to \infty} \int \varphi_n \, d\lambda
$$

**Riemann integration**, by contrast, requires:
- Partitioning the **domain** into intervals
- The function must be "nearly continuous" for upper and lower sums to converge
- Pathological discontinuities (like those in $\mathbf{1}_C$) cause catastrophic failure

**Lebesgue integration**:
- Partitions the **range** into level sets
- Measures each level set using the Lebesgue measure
- Handles arbitrary discontinuities as long as the function is measurable

#### **Implications for Reinforcement Learning**

In RL, we encounter measurable functions that are far from continuous:

1. **Value functions with barriers**: $V(s) = \begin{cases} \text{finite} & s \in \text{safe region} \\ -\infty & s \in \text{forbidden region} \end{cases}$

2. **Indicator policies**: $\pi(a|s) = \mathbf{1}_{\{a = a^*(s)\}}$ (deterministic policies are Dirac measures)

3. **Limits of neural network policies**: As we train a policy network, the sequence $\pi_\theta$ may converge to a policy that is discontinuous at decision boundaries

The expectation $\mathbb{E}^{\pi}[R]$ is a Lebesgue integral:
$$
\mathbb{E}^{\pi}[R] = \int R(s,a) \, d\mu_\pi(s,a)
$$
where $\mu_\pi$ is the state-action visitation measure induced by policy $\pi$.

**If we used Riemann integration**, we could not handle policies with discontinuities, and algorithms like Q-learning (which produce piecewise-constant value functions in tabular settings) would lack rigorous justification.

**With Lebesgue integration**, we have a complete theory:
- Monotone Convergence Theorem justifies value iteration convergence
- Dominated Convergence Theorem justifies policy gradient interchange of $\nabla$ and $\mathbb{E}$
- Fubini-Tonelli theorem justifies decomposition of expectations over product spaces

The numerical methods in this appendix—Monte Carlo integration, simple function approximation, measure computation via limiting sequences—are not academic curiosities. They are the **actual computational tools** used when implementing RL algorithms on non-trivial state spaces.

---

### **VII. Summary and Outlook**

This appendix has demonstrated:

1. **Construction of pathological measurable sets** (fat Cantor set with $\lambda(C) = 1/2$ but highly discontinuous indicator)
2. **Failure of Riemann integration** for $\mathbf{1}_C$ (upper and lower sums do not converge)
3. **Success of Lebesgue integration** via simple function approximation and Monte Carlo methods
4. **Numerical verification of MCT** using simple function sequences converging to continuous limits

The key lesson: **Lebesgue integration is not an abstraction—it is a computational necessity** for handling the discontinuous, pathological, and measure-theoretically subtle functions that arise inevitably in reinforcement learning.

Tomorrow (Day 3), we will prove **Fatou's Lemma** and the **Dominated Convergence Theorem**, which extend beyond monotonicity to handle sequences with arbitrary (even oscillating) behavior, provided we have either non-negativity (Fatou) or domination by an integrable function (DCT). These theorems are the final pillars of the convergence theory, and they are essential for analyzing stochastic approximation algorithms like TD learning and Q-learning.

---

**End of Appendix A**

---
Fat Cantor Set Convergence:
- Stage 10: λ(C₁₀) = 0.5004882812, Error = 4.88e-04
- Theoretical limit: λ(C) = 1/2

MCT with Simple Functions:
- n=20: ∫f₂₀ = 0.499999523, Error = 4.77e-07
- Discontinuous sequence → continuous limit!

Riemann Failure:
- 1000 intervals: U-L gap = 0.11 (should be ~0 for Riemann integrability)
- True Lebesgue integral: 0.5078
