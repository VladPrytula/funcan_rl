# Complete Workflow Manual

**Quick reference for daily content creation, review, revision, and validation**

---

## Daily Content Creation Workflow

### Step 1: Create Draft
```bash
# Create new draft file
Week_X/Day_Y_draft.md
```

**Content structure (90-120 min target):**
- Read assigned material from Syllabus.md
- Write theory notes with definitions, theorems, proofs
- Solve anchor exercises
- Add RL connection section
- Include code examples (Fridays)

**Citation as you write:**
- External sources: `[@folland:real_analysis:1999, §2.3]`
- Internal references: `[THM-1.3.1]`, `[DEF-2.2.1]`
- Label your results: `### Theorem 2.3.1 (Name) {#THM-2.3.1}`

---

### Step 2: Transform to Textbook Quality (Professor Dubois)

Ask Claude Code with context from `agent.md`:

```
Using the Professor Dubois persona from agent.md, transform Week_X/Day_Y_draft.md
into textbook-quality exposition following the four-part structure:
I. Motivation, II. Core Theory, III. Proofs, IV. Computational Illustration
```

**What Dubois adds:**
- Sophisticated motivation connecting to RL
- Bourbaki-precise definitions with examples
- Brezis-style pedagogical proofs (step-by-step)
- Contemporary RL references (DeepMind, FAIR papers)
- Forward/backward connections to other weeks

**Output:** Create `Week_X/Day_Y.md` with polished content

---

### Step 3: Run Comprehensive Reviews

**Option A: All at once (recommended)**
```bash
/review-all Week_X/Day_Y.md
```

**Option B: Sequential reviews**
```bash
/review-math Week_X/Day_Y.md           # Mathematical rigor (Springer GTM standards)
/review-pedagogy Week_X/Day_Y.md       # Pedagogical flow and accessibility
/review-rl-bridge Week_X/Day_Y.md      # RL/control theory connections
```

**What reviewers check:**
- **Math**: Theorem completeness, proof rigor, hypothesis verification
- **Pedagogy**: Motivation clarity, example quality, flow and pacing
- **RL Bridge**: Concrete connections, algorithmic relevance, forward applicability

**Output:** Detailed feedback in three categories

---

### Step 4: Revise Based on Feedback

```bash
# Create revised version incorporating all feedback
Week_X/Day_Y_REVISED.md
```

**Revision checklist:**
- [ ] Address mathematical issues (proof gaps, missing hypotheses)
- [ ] Improve pedagogical flow (add examples, clarify motivation)
- [ ] Strengthen RL connections (concrete algorithms, forward references)
- [ ] Check time target (90-120 min acceptable, >150 min = split content)
- [ ] Document any simplifications in Postponed Generalizations Log

**If substantial changes made:** Re-run targeted review
```bash
/review-math Week_X/Day_Y_REVISED.md    # If math was revised
```

---

### Step 5: Validate Citations and Cross-References

**Check citation syntax** (do all [@keys] exist in references.bib?)
```bash
/validate-citations Week_X/Day_Y_REVISED.md
```

**Check internal cross-references** (do all [TYPE-W.D.N] exist in Master_Index.md?)
```bash
/validate-index Week_X/Day_Y_REVISED.md
```

**Fix any issues:**
- Missing citations → Add to `references.bib`
- Missing internal refs → Add to `Master_Index.md`
- Syntax errors → Correct in content file

**Re-run validation until clean** ✅

---

### Step 6: Final Polish

```bash
/edit-polish Week_X/Day_Y_REVISED.md
```

**What polish does:**
- Grammar and style cleanup
- LaTeX formatting consistency
- Reference formatting (§X.Y, Thm X.Y)
- Equation numbering verification
- Proof completion markers (□)

**Output:** Content ready for finalization

---

### Step 7: Finalize and Index

**Rename to final version:**
```bash
Week_X/Day_Y_REVISED.md → Week_X/Day_Y_FINAL.md
```

**Add all results to Master_Index.md:**

For each labeled result in the file (e.g., `{#THM-2.3.1}`), add to appropriate table:

```markdown
| THM-2.3.1 | Dominated Convergence | If |fₙ| ≤ g ∈ L¹, then lim ∫fₙ = ∫lim fₙ | Week_2/Day_3_FINAL.md:45 | Proved | THM-1.4.2, LEM-2.1.1 | @folland:real_analysis:1999, Thm 2.24 | Standard result, used in Week 5, 8, 12 |
```

**Tables in Master_Index.md:**
- Definitions (DEF-W.D.N)
- Theorems (THM-W.D.N)
- Lemmas (LEM-W.D.N)
- Propositions (PROP-W.D.N)
- Corollaries (COR-W.D.N)
- Examples (EX-W.D.N)
- Postponed Generalizations (POSTPONE-W.D.N)

---

### Step 8: Formalize Exercises

**Create exercise file:**
```bash
Week_X/Day_Y_exercises_FINAL.md
```

**Convert informal exercises to formal results:**
```markdown
### Proposition 2.3.5 (Exercise 2.3.4) {#PROP-2.3.5}

**Statement:** [Formal proposition statement]

**Proof:**
*Step 1:* [Clear reasoning]
*Step 2:* [Build on Step 1]
*Step 3:* Conclude. □

**Pedagogical Note:** This result demonstrates [technique/concept].
```

**Add to Master_Index.md** (same as Step 7)

---

## Weekly Completion Workflow

### Step 9: Validate Week Against Syllabus

```bash
/validate-week X all     # Validate all days in Week X
```

**What it checks:**
- [ ] All proof targets from Syllabus.md addressed
- [ ] Anchor exercises (≥2 per week) completed
- [ ] Weekly learning goals met
- [ ] Postponed generalizations documented (if any)
- [ ] Time targets reasonable (90-150 min per day)

**Output:** `Week_X/syllabus_validation_report.md`

**Address any gaps** before moving to next week

---

### Step 10: Validate Bibliography Metadata (Weekly)

```bash
/validate-citations-metadata --level thorough
```

**What it checks:**
- DOIs resolve correctly
- arXiv IDs are valid
- URLs are reachable (not 404)
- ISBNs have correct format
- Sources findable via SearXNG (http://localhost:9090/)

**When to run:**
- After adding new sources to `references.bib`
- Weekly maintenance (check for link rot)
- Before major milestones (phase completions)

**Output:** `scripts/citation_validation_report.md`

---

### Step 11: Organize Files

**Move finalized content:**
```bash
Week_X/
├── Day_1_FINAL.md                    → Move to Week_X/final/
├── Day_1_exercises_FINAL.md          → Move to Week_X/final/
├── Day_2_FINAL.md                    → Move to Week_X/final/
...
├── Day_1_draft.md                    → DELETE (no longer needed)
├── Day_2_REVISED.md                  → DELETE (superseded by FINAL)
└── final/                            ← All polished content here
    ├── Day_1_FINAL.md
    ├── Day_1_exercises_FINAL.md
    ...
```

**Commit to git:**
```bash
git add Week_X/final/
git commit -m "Week X complete: [Topic Name]"
```

---

## File Naming Conventions

### Core Files
- `Day_X_draft.md` - Initial work-in-progress
- `Day_X.md` - After Dubois transformation
- `Day_X_REVISED.md` - After incorporating review feedback
- `Day_X_FINAL.md` - Production-ready (validated)
- `Day_X_FINAL_v2.md` - Second revision cycle
- `Day_X_FINAL_v3.md` - Third revision cycle (etc.)
- `Day_X_exercises_FINAL.md` - Formalized exercise solutions
- `Day_X_Appendix_[Topic].md` - Supplementary material

### Supporting Files
- `TODOs.md` - Week-specific task tracking
- `syllabus_validation_report.md` - Output from `/validate-week`
- `README.md` or `Week_X_Summary.md` - Weekly reflection

**Rule:** Always use underscores `_`, never spaces in filenames

---

## Citation System Quick Reference

### External Citations (references.bib)

**Basic citation:**
```markdown
[@folland:real_analysis:1999]
```

**With section/theorem:**
```markdown
[@folland:real_analysis:1999, §2.3, Thm 2.14]
[@brezis:functional_analysis:2011, Proposition 3.5, pp. 120-125]
```

**Multiple citations:**
```markdown
[@folland:real_analysis:1999; @durrett:probability:2019]
```

**In sentences:**
```markdown
Folland [@folland:real_analysis:1999, §2.3] proves that...
```

### Internal Cross-References (Master_Index.md)

**Reference existing result:**
```markdown
By [THM-1.3.1] (Monotone Convergence), we have...
Recall from [DEF-2.2.1] that a measure is...
Using [LEM-2.1.1] and [PROP-1.4.2], we obtain...
```

**Label your own result:**
```markdown
### Theorem 2.3.1 (Dominated Convergence Theorem) {#THM-2.3.1}
```

**ID Format:** `TYPE-W.D.N`
- `TYPE` ∈ {DEF, THM, LEM, PROP, COR, EX, POSTPONE}
- `W` = Week number (1-48)
- `D` = Day number (1-5)
- `N` = Sequential number within day (1, 2, 3, ...)

---

## Validation Tools Summary

| Command | What It Checks | When to Use |
|---------|---------------|-------------|
| `/validate-citations [file]` | All `[@cite_key]` exist in references.bib | After drafting, before finalization |
| `/validate-index [file]` | All `[TYPE-W.D.N]` exist in Master_Index.md | After drafting, before finalization |
| `/validate-citations-metadata` | DOIs, ISBNs, URLs, search findability | Weekly, after adding new sources |
| `/validate-week X all` | Syllabus alignment, proof targets | End of each week |

---

## Quick Troubleshooting

### "Missing citation [@key]"
→ Add entry to `references.bib` using this template:
```bibtex
@book{author:shortname:year,
  author    = {Last, First},
  title     = {Full Title},
  year      = {YYYY},
  publisher = {Publisher},
  isbn      = {978-XXXXXXXXXX},
  note      = {Brief description}
}
```

### "Missing reference [THM-X.Y.Z]"
→ Add entry to appropriate table in `Master_Index.md`

### "DOI does not resolve"
→ Verify at https://doi.org/[doi], update references.bib if incorrect

### "arXiv ID not found"
→ Verify at https://arxiv.org/abs/[id], check for version (v1, v2)

### "URL returns 404"
→ Search for paper, update URL, or mark: `note = {URL no longer accessible}`

### "Content exceeds 150 minutes"
→ Split into two days or simplify proofs (document in Postponed Generalizations Log)

---

## One-Command Workflows

### Complete Day Pipeline
```bash
# After creating Day_X.md with Dubois transformation:
/review-all Week_X/Day_X.md
# → Revise to create Day_X_REVISED.md
/validate-citations Week_X/Day_X_REVISED.md
/validate-index Week_X/Day_X_REVISED.md
/edit-polish Week_X/Day_X_REVISED.md
# → Rename to Day_X_FINAL.md
# → Add results to Master_Index.md
```

### Alternative: Review-Revise-Polish in One Go
```bash
/review-and-revise Week_X/Day_X_draft.md
# Automatically runs all reviews, creates revised version, and polishes
```

### Week Completion
```bash
/validate-week X all
/validate-citations-metadata --level thorough
# → Organize files into Week_X/final/
# → Commit to git
```

---

## Key Reminders

✅ **Always cite as you write** (easier than retrofitting)
✅ **Label every formal result** with `{#TYPE-W.D.N}`
✅ **Add to Master_Index.md immediately** after labeling
✅ **Run validations before finalizing** (not after)
✅ **Document simplifications** in Postponed Generalizations Log
✅ **Target 90-120 min per day** (150 min absolute max)
✅ **Weekends off** (no study, no guilt)
✅ **Version awareness**: Highest version (v2, v3) is canonical

---

## File Locations Reference

```
Study/
├── WORKFLOW_MANUAL.md              ← This file
├── Syllabus.md                     ← Canonical 48-week plan
├── agent.md                        ← Professor Dubois persona
├── CLAUDE.md                       ← Complete system documentation
├── references.bib                  ← Master bibliography
├── Master_Index.md                 ← Result registry
├── Citation_Guide.md               ← Citation syntax examples
├── .claude/commands/               ← Slash command definitions
│   ├── review-math.md
│   ├── review-pedagogy.md
│   ├── review-rl-bridge.md
│   ├── review-all.md
│   ├── revise.md
│   ├── edit-polish.md
│   ├── review-and-revise.md
│   ├── validate-week.md
│   ├── validate-citations.md
│   ├── validate-index.md
│   └── validate-citations-metadata.md
├── scripts/
│   ├── validate_citations_metadata.py
│   ├── citation_validation_config.json
│   ├── citation_validation_report.md
│   └── citation_validation_report.json
└── Week_X/
    ├── Day_Y_draft.md              ← Work in progress
    ├── Day_Y_REVISED.md            ← After reviews
    ├── TODOs.md
    ├── syllabus_validation_report.md
    └── final/                      ← Polished content
        ├── Day_1_FINAL.md
        ├── Day_1_exercises_FINAL.md
        └── ...
```

---

**For detailed documentation, see CLAUDE.md**
**For citation syntax examples, see Citation_Guide.md**
**For persona details, see agent.md**
**For weekly goals, see Syllabus.md**
