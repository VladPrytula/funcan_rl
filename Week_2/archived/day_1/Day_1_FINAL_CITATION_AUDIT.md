# Citation Audit Report

**File:** `Week_2/final/Day_1_FINAL.md`
**Date:** 2025-10-11
**Total informal references found:** 12

---

## Instructions for Author

Review each suggestion below. For each:
1. ✅ If correct: Copy the suggested citation and replace the original text
2. ✏️ If needs adjustment: Modify the suggestion before applying
3. ❌ If incorrect: Skip (no citation needed or wrong source)

After applying citations, run:
- `/validate-citations Week_2/final/Day_1_FINAL.md` to verify all citations exist

---

## Suggested Citations

### Line 12
**Current text:**
> Read from **Folland, "Real Analysis" §2.4-2.5** or equivalent in Durrett Ch. 4.

**Suggested replacement:**
> Read from [@folland:real_analysis:1999, §2.4-2.5] or equivalent in [@durrett:probability:2019, Ch. 4].

**Reasoning:** Reading assignment explicitly referencing two primary textbooks. Both are Tier 1 references in bibliography.

**Bibliography match:**
- `folland:real_analysis:1999` = Folland, Gerald B. "Real Analysis: Modern Techniques and Their Applications" (1999)
- `durrett:probability:2019` = Durrett, Rick "Probability: Theory and Examples" (2019)

**Confidence:** ✅ Very High

---

### Line 166
**Current text:**
> see Folland §1.1, Exercise 10

**Suggested replacement:**
> see [@folland:real_analysis:1999, §1.1, Ex 10]

**Reasoning:** Reference to specific exercise in Folland's Real Analysis text for additional context on σ-algebra construction.

**Bibliography match:**
- `folland:real_analysis:1999` = Folland, Gerald B. "Real Analysis: Modern Techniques and Their Applications" (1999)

**Confidence:** ✅ Very High

---

### Line 258
**Current text:**
> The full verification (Folland §2.4, Proposition 2.27) handles this...

**Suggested replacement:**
> The full verification [@folland:real_analysis:1999, §2.4, Prop 2.27] handles this...

**Reasoning:** Pointing to specific result in Folland that provides complete proof of countable additivity on semirings.

**Bibliography match:**
- `folland:real_analysis:1999` = Folland, Gerald B. "Real Analysis: Modern Techniques and Their Applications" (1999)

**Confidence:** ✅ Very High

---

### Line 264
**Current text:**
> For the complete verification of countable additivity on semirings, see Folland §2.4, Proposition 2.27.

**Suggested replacement:**
> For the complete verification of countable additivity on semirings, see [@folland:real_analysis:1999, §2.4, Prop 2.27].

**Reasoning:** Directing reader to full proof in textbook (duplicate reference from line 258).

**Bibliography match:**
- `folland:real_analysis:1999` = Folland, Gerald B. "Real Analysis: Modern Techniques and Their Applications" (1999)

**Confidence:** ✅ Very High

---

### Line 312
**Current text:**
> We invoke the π-λ theorem (Week 1, Day 1, or Folland §1.5, Theorem 1.14):

**Suggested replacement:**
> We invoke the π-λ theorem (Week 1, Day 1, or [@folland:real_analysis:1999, §1.5, Thm 1.14]):

**Reasoning:** Citing standard theorem, providing both internal reference (Week 1) and external textbook source.

**Bibliography match:**
- `folland:real_analysis:1999` = Folland, Gerald B. "Real Analysis: Modern Techniques and Their Applications" (1999)

**Confidence:** ✅ Very High

---

### Line 340
**Current text:**
> For metric spaces, $\mathcal{B}(X \times Y) = \mathcal{B}(X) \otimes \mathcal{B}(Y)$ (this is a nontrivial result; see Folland §2.5, Theorem 2.29).

**Suggested replacement:**
> For metric spaces, $\mathcal{B}(X \times Y) = \mathcal{B}(X) \otimes \mathcal{B}(Y)$ (this is a nontrivial result; see [@folland:real_analysis:1999, §2.5, Thm 2.29]).

**Reasoning:** Important non-obvious result relating Borel σ-algebras on product spaces for metric spaces.

**Bibliography match:**
- `folland:real_analysis:1999` = Folland, Gerald B. "Real Analysis: Modern Techniques and Their Applications" (1999)

**Confidence:** ✅ Very High

---

### Line 420
**Current text:**
> originally introduced by Barto, Sutton, and Anderson (1983)

**Suggested replacement:**
> originally introduced by [@barto:cart_pole:1983]

**Reasoning:** Historical attribution to original CartPole paper. **However**, this citation key does NOT currently exist in `references.bib`.

**Bibliography match:**
- ⚠️ **NOT FOUND in current bibliography** - Must add this entry first!
- **Suggested BibTeX entry:**
```bibtex
@article{barto:cart_pole:1983,
  author  = {Barto, Andrew G. and Sutton, Richard S. and Anderson, Charles W.},
  title   = {Neuronlike adaptive elements that can solve difficult learning control problems},
  journal = {IEEE Transactions on Systems, Man, and Cybernetics},
  year    = {1983},
  volume  = {SMC-13},
  number  = {5},
  pages   = {834--846},
  doi     = {10.1109/TSMC.1983.6313077},
  note    = {Original CartPole problem formulation}
}
```

**Confidence:** ⚠️ High (but need to add to bibliography first)

---

### Line 459
**Current text:**
> **Reference:** Barto, Sutton, and Anderson (1983), "Neuronlike adaptive elements that can solve difficult learning control problems," *IEEE Transactions on Systems, Man, and Cybernetics*.

**Suggested action:**
1. Add the BibTeX entry suggested at Line 420 to `references.bib`
2. Replace this **Reference:** paragraph with inline citation at Line 420
3. Remove this standalone reference paragraph (redundant once proper citation is inline)

**Alternative format (if keeping reference):**
> Barto, Sutton, and Anderson [@barto:cart_pole:1983], "Neuronlike adaptive elements..."

**Reasoning:** Full reference details provided inline, should be moved to bibliography and cited properly at first mention (Line 420).

**Confidence:** ✅ Very High

---

### Line 480
**Current text:**
> In policy gradient methods (Sutton et al., 2000), we compute...

**Suggested replacement:**
> In policy gradient methods [@sutton:policy_gradient:2000], we compute...

**Reasoning:** Reference to Sutton's 2000 NeurIPS paper on policy gradients. **However**, this specific paper is NOT in current bibliography.

**Bibliography match:**
- ⚠️ **NOT FOUND** - Need to add
- **Note:** Current bibliography has `sutton:reinforcement_learning:2018` (textbook), but the 2000 reference is to a specific conference paper
- **Suggested BibTeX entry:**
```bibtex
@inproceedings{sutton:policy_gradient:2000,
  author    = {Sutton, Richard S. and McAllester, David A. and Singh, Satinder P. and Mansour, Yishay},
  title     = {Policy Gradient Methods for Reinforcement Learning with Function Approximation},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2000},
  volume    = {13},
  pages     = {1057--1063},
  note      = {Policy gradient theorem, REINFORCE with baseline}
}
```

**Confidence:** ⚠️ High (but need to add to bibliography first)

---

### Line 502
**Current text:**
> **Reference:** Sutton, McAllester, Singh, and Mansour (2000), "Policy Gradient Methods for Reinforcement Learning with Function Approximation," *NeurIPS*.

**Suggested action:**
1. Add the BibTeX entry suggested at Line 480 to `references.bib`
2. Replace this **Reference:** paragraph with inline citation at Line 480
3. Remove this standalone reference paragraph (redundant once proper citation is inline)

**Reasoning:** Full reference details provided, should be moved to bibliography and cited properly at first mention (Line 480).

**Confidence:** ✅ Very High

---

### Line 658
**Current text:**
> The answer is subtle and involves measurable cardinals (see Folland §2.6, advanced topic).

**Suggested replacement:**
> The answer is subtle and involves measurable cardinals (see [@folland:real_analysis:1999, §2.6], advanced topic).

**Reasoning:** Pointing to advanced material in Folland for readers interested in non-σ-finite product measures.

**Bibliography match:**
- `folland:real_analysis:1999` = Folland, Gerald B. "Real Analysis: Modern Techniques and Their Applications" (1999)

**Confidence:** ✅ Very High

---

### Additional Context References (Optional - Not Urgent)

#### Lines 392-393
**Current text:**
> - **Model-based RL**: PETS (Chua et al., NeurIPS 2018) and MBPO (Janner et al., NeurIPS 2019) learn Gaussian dynamics models via neural networks

**Suggested enhancement:**
Consider adding citations for PETS and MBPO papers if they become more prominent in later weeks. For now, these are contextual mentions (not claims requiring citation).

**Action:** ⏸️ Optional (add if papers are discussed in detail later)

---

## Summary

**By confidence level:**
- ✅ **Very High Confidence (9 suggestions):**
  All Folland references have clear matches in bibliography

- ⚠️ **High Confidence - Missing from Bibliography (2 items):**
  1. `barto:cart_pole:1983` - Lines 420, 459
  2. `sutton:policy_gradient:2000` - Lines 480, 502

**Missing bibliography entries to add:**

### 1. Barto, Sutton, Anderson (1983) - CartPole Paper
```bibtex
@article{barto:cart_pole:1983,
  author  = {Barto, Andrew G. and Sutton, Richard S. and Anderson, Charles W.},
  title   = {Neuronlike adaptive elements that can solve difficult learning control problems},
  journal = {IEEE Transactions on Systems, Man, and Cybernetics},
  year    = {1983},
  volume  = {SMC-13},
  number  = {5},
  pages   = {834--846},
  doi     = {10.1109/TSMC.1983.6313077},
  note    = {Original CartPole problem formulation}
}
```

### 2. Sutton et al. (2000) - Policy Gradient NeurIPS Paper
```bibtex
@inproceedings{sutton:policy_gradient:2000,
  author    = {Sutton, Richard S. and McAllester, David A. and Singh, Satinder P. and Mansour, Yishay},
  title     = {Policy Gradient Methods for Reinforcement Learning with Function Approximation},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2000},
  volume    = {13},
  pages     = {1057--1063},
  note      = {Policy gradient theorem, REINFORCE with baseline}
}
```

---

## Recommended Workflow

### Step 1: Add Missing Entries to references.bib
Copy the two BibTeX entries above and add them to `references.bib` in the appropriate section (probably "REINFORCEMENT LEARNING PAPERS" or "POLICY GRADIENT METHODS").

### Step 2: Apply Citations Manually
Go through each suggestion above and replace the informal citations with proper `[@cite_key]` format. You have full control - review each one before applying.

### Step 3: Remove Redundant Reference Paragraphs
Delete the standalone **Reference:** paragraphs at lines 459 and 502 (now redundant with inline citations).

### Step 4: Validate
Run `/validate-citations Week_2/final/Day_1_FINAL.md` to verify all citations exist in bibliography.

### Step 5: Clean Up
Delete this audit file once you're satisfied with the changes.

---

##Note on Style

**Current style (informal):**
> see Folland §2.4, Theorem 3.5

**Proper citation style:**
> see [@folland:real_analysis:1999, §2.4, Thm 3.5]

**Benefits of proper citations:**
1. Machine-readable (validators can check them)
2. Consistent format across all files
3. Easy to generate bibliography later
4. Clear separation between internal refs `[THM-1.3.1]` and external citations `[@key]`

---

**Questions or concerns?** The audit is advisory only - you control every change!
