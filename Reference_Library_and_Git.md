# Reference Library and Git Workflow

This document provides the reference library organization and git workflow conventions for the 48-week study plan.

---

## Reference Library

The study plan draws from a carefully curated collection of textbooks and papers, organized into three tiers based on usage frequency.

### Tier 1 (Weekly Use)

These are the primary textbooks that will be referenced most frequently throughout the study plan:

- **Folland** - "Real Analysis: Modern Techniques and Their Applications"
  - Foundation for measure theory and integration (Weeks 1-6, 10-12)
  - Standard reference for Lebesgue theory

- **Brezis** - "Functional Analysis, Sobolev Spaces and PDEs"
  - Core text for functional analysis (Weeks 13-18)
  - Sobolev spaces and PDE connections (Weeks 19-24)
  - Pedagogically excellent, rigorous without obscurity

- **Puterman** - "Markov Decision Processes: Discrete Stochastic Dynamic Programming"
  - Definitive MDP reference (Weeks 25-28)
  - Value iteration, policy iteration, average reward
  - Connects to RL algorithms

- **Lattimore-Szepesvári** - "Bandit Algorithms"
  - Modern, comprehensive bandit theory (Weeks 29-33)
  - Regret bounds, UCB, Thompson Sampling
  - Contextual bandits and connections to RL

### Tier 2 (Regular Reference)

These textbooks will be consulted frequently but not continuously:

- **Durrett** - "Probability: Theory and Examples"
  - Rigorous probability theory
  - Markov chains, martingales, ergodic theory
  - Used throughout Weeks 7-12, referenced later

- **Levin-Peres-Wilmer** - "Markov Chains and Mixing Times"
  - Accessible treatment of Markov chains
  - Mixing times, coupling, MCMC
  - Complements Durrett for Weeks 7-12

- **Borkar** - "Stochastic Approximation: A Dynamical Systems Viewpoint"
  - Essential for SA theory (Weeks 34-39)
  - ODE method, convergence analysis
  - TD learning, Q-learning convergence

- **Bertsekas** - "Reinforcement Learning and Optimal Control"
  - Modern RL perspective
  - Approximate DP, neural network function approximation
  - Connects classical control to deep RL

### Tier 3 (Specialized Topics)

These are advanced references for specific topics:

- **Meyn-Tweedie** - "Markov Chains and Stochastic Stability"
  - Advanced general state space theory
  - Ergodic theory for Markov chains
  - Used for specialized results in Weeks 10-12

- **Yong-Zhou** - "Stochastic Controls: Hamiltonian Systems and HJB Equations"
  - Continuous-time optimal control
  - HJB equations, viscosity solutions
  - Advanced topics in Weeks 19-24, 40-43

- **Bardi-Capuzzo Dolcetta** - "Optimal Control and Viscosity Solutions of Hamilton-Jacobi-Bellman Equations"
  - Rigorous viscosity solution theory
  - PDE approach to control
  - Reference for Weeks 19-24

- **Sutton-Barto** - "Reinforcement Learning: An Introduction"
  - Narrative guide to RL
  - Intuition and motivation
  - Not rigorous, but excellent for conceptual understanding

---

## Citation Key Format

All references in `references.bib` follow the format:

```
author:shortname:year
```

**Examples:**
- `@folland:real_analysis:1999`
- `@brezis:functional_analysis:2011`
- `@puterman:mdp:2014`
- `@lattimore:bandit_algorithms:2020`
- `@borkar:stochastic_approximation:2008`

See **Citation_System_Reference.md** for complete citation and cross-referencing guidelines.

---

## Git Workflow

### Branch Structure

**Current branch:** `main`

The repository uses a simple trunk-based workflow:
- All work is done on `main`
- No feature branches (this is a personal study repository)
- Commits reflect incremental progress

### Commit Philosophy

The repository tracks study progress through clear, descriptive commits. Each commit should reflect a meaningful milestone in the learning journey.

### Recommended Commit Messages

#### Daily Work

```
Week 1 Day 2 draft complete
Week 1 Day 2 revised (math review feedback)
Week 1 Day 2 finalized
Week 1 Day 2 v2 (additional pedagogy revision)
```

**Format:** `Week X Day Y [status] [(reason)]`

**Status options:**
- `draft complete` - Initial notes finished
- `revised` - Incorporating feedback
- `finalized` - First FINAL version ready
- `v2`, `v3`, etc. - Additional revision cycles

**Reason (optional):** Brief explanation for revisions
- `(math review feedback)`
- `(additional pedagogy revision)`
- `(cross-week integration improvements)`
- `(syllabus validation fixes)`

#### Weekly Milestones

```
Week 1 complete: σ-algebras and measures
Week 1 validation passed
```

**Format:** `Week X complete: [topic summary]`

Use this after:
- All 5 days finalized and moved to `final/`
- `/validate-week X all` passes
- Weekly reflection written

#### Phase Completions

```
Phase I complete: Measure-theoretic foundations (Weeks 1-6)
```

**Format:** `Phase X complete: [phase name] (Weeks Y-Z)`

Use this after:
- All weeks in phase validated
- Phase summary document created
- Postponed generalizations reviewed

### Commit Best Practices

#### Do's

- ✅ **Commit after each meaningful milestone**: Don't batch multiple days
- ✅ **Write clear, descriptive messages**: Future you will thank present you
- ✅ **Commit validation passes**: "Week 2 validation passed" is a milestone
- ✅ **Document version increments**: Explain why `_FINAL_v2` was created
- ✅ **Commit after updating documentation**: `Master_Index.md`, `references.bib` updates

#### Don'ts

- ❌ **Don't commit broken work**: Run validation before committing
- ❌ **Don't use vague messages**: "updates" or "changes" are not helpful
- ❌ **Don't batch unrelated changes**: Separate citation updates from content revisions
- ❌ **Don't commit without testing**: Ensure LaTeX renders, code runs

### Special Commit Types

#### Adding Citations

```
Add missing citations for Week 2 Day 3
Update references.bib with Borkar SA text
```

#### Updating Index

```
Update Master_Index.md with Week 2 Day 3 results
Fix cross-reference IDs in Master_Index.md
```

#### Fixing Validation Issues

```
Fix citation syntax in Week 1 Day 2
Resolve circular dependency in Week 2 theorems
```

#### Documentation Updates

```
Update Syllabus.md with revised Week 3 proof targets
Document postponed generalizations for Weeks 1-2
```

---

## Git Hygiene Checklist

Before committing, verify:

```
□ All validation tools pass
  □ /validate-citations Week_Y/*_FINAL*.md
  □ /validate-index Week_Y/*_FINAL*.md
  □ /validate-week Y all (if end of week)
□ LaTeX renders correctly in Obsidian
□ Code examples run without errors (if applicable)
□ File naming follows underscore convention
□ Version numbers are correct and justified
□ Master_Index.md updated with new results
□ references.bib contains all cited sources
□ Commit message is clear and descriptive
```

---

## Long-Term Repository Maintenance

### Weekly Tasks

- Commit after each day finalized
- Commit after weekly validation passes
- Update `Master_Index.md` statistics
- Review and commit postponed generalizations log

### Phase Completion Tasks

- Comprehensive validation across entire phase
- Create phase summary document
- Review all postponed generalizations
- Commit with clear "Phase X complete" message
- Tag the commit (optional): `git tag phase-1-complete`

### Semester Milestones

- Validate entire codebase (all completed weeks)
- Review commit history for patterns
- Consider squashing old WIP commits (optional)
- Update documentation based on lessons learned

---

## Repository Statistics

As of Week 2:
- Total commits: ~15-20 (estimate)
- Weeks completed: 2
- Phase progress: Phase I (Weeks 1-6) - 33% complete
- Results indexed: Check `Master_Index.md` statistics section

---

## Related Documentation

- **CLAUDE.md**: Main instructions for Claude Code
- **File_Management_Guide.md**: File naming, versioning, and workflow
- **Citation_System_Reference.md**: Citation and indexing system details
- **Best_Practices_and_Pitfalls.md**: Common mistakes and how to avoid them
- **references.bib**: Master BibTeX bibliography
