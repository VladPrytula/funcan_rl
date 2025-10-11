# File Management Guide

This document provides comprehensive guidelines for file naming, versioning, and workflow management throughout the 48-week study plan.

---

## File Naming Conventions (Underscore Standard)

**All filenames use underscores `_` instead of spaces:**

### Standard File Types

- `Day_X.md` - Polished theory notes (production-ready)
- `Day_X_exercises.md` - Exercise solutions
- `Day_X_draft.md` - Work-in-progress (may be incomplete)
- `Day_X_FINAL.md` - Final version after complete review/revision cycle
- `Day_X_FINAL_v2.md`, `Day_X_FINAL_v3.md`, etc. - Subsequent final versions after additional review cycles
- `Day_X_REVISED.md` - Revised version incorporating specific feedback
- `Day_X_exercises_FINAL.md` - Finalized exercise solutions
- `Day_X_exercises_FINAL_v2.md`, etc. - Subsequent versions of finalized exercises
- `Day_X_Appendix_[Topic].md` - Supplementary material for Day X

### Version Numbering Philosophy

- Use `_FINAL` for the first complete, validated version
- Use `_FINAL_v2`, `_FINAL_v3`, etc. for subsequent iterations when:
  - Additional reviewer feedback requires substantial revision
  - New cross-week connections are added after later material
  - Syllabus validation reveals missing proof targets
  - Pedagogical improvements are made after student testing
- Keep the highest version number as the canonical version
- Previous versions can be kept for reference or deleted once superseded

### Examples

```
Day_1_FINAL.md
Day_1_exercises_FINAL.md
Day_2_FINAL_v2.md          # Second complete revision cycle
Day_2_exercises_FINAL_v2.md
Day_3_draft.md
Day_3_REVISED.md
Day_5_FINAL.md
Day_5_Appendix_Numerical_Lebesgue.md
```

---

## File Evolution Workflow

### Typical Daily Content Lifecycle

1. **Draft Creation** → `Day_X_draft.md` (lowercase)
   - Initial notes, proofs, exercises
   - May contain incomplete reasoning or rough sketches
   - Keep in root `Week_X/` directory during work

2. **Comprehensive Review** → Run `/review-all Day_X_draft.md`
   - Mathematical review: theorem statements, proof completeness, rigor
   - Pedagogical review: flow, motivation, accessibility
   - RL bridge review: connections to RL/control theory

3. **First Revision** → Create `Day_X_REVISED.md` (UPPERCASE)
   - Incorporate all feedback from reviews
   - Polish proofs and definitions
   - Keep in root `Week_X/` directory during revision work

4. **Final Polish** (optional) → Run `/edit-polish Day_X_REVISED.md`
   - Grammar, LaTeX formatting, citations
   - Final consistency checks

5. **Finalization** → Rename to `Day_X_FINAL.md` and move to `Week_X/final/`
   - Production-ready textbook quality
   - All reviews passed, validated against Syllabus.md

6. **Exercise Formalization** → Create `Day_X_exercises_FINAL.md` in `final/`
   - Formalize exercises as Propositions/Lemmas
   - Complete proofs with pedagogical annotations

7. **Weekly Validation** → Run `/validate-week [week-number] all`
   - Verify alignment with Syllabus.md goals
   - Check proof targets and anchor exercises

8. **Cleanup** → Delete `Day_X_draft.md` and `Day_X_REVISED.md` from root

9. **Subsequent Revisions** (if needed) → Create `Day_X_FINAL_v2.md`, `Day_X_FINAL_v3.md`, etc.
   - Additional review cycles based on new feedback
   - Cross-week integration improvements
   - Keep or delete previous versions based on utility
   - Always work from the highest version number

### Quick Workflow (Alternative)

```bash
/review-all Day_X_draft.md           # Get comprehensive feedback
# → Edit to create Day_X_REVISED.md
/edit-polish Day_X_REVISED.md        # Final polish
# → Rename to Day_X_FINAL.md
```

---

## Directory Organization Rules

1. **Work in Progress**: Keep drafts in root `Week_X/` directory during active work
2. **Finalized Content**: Move to `Week_X/final/` subdirectory after validation
3. **Cleanup**: Delete intermediate drafts once final version is validated
4. **Naming**: Use underscores `_` consistently in all filenames
5. **Version Management**:
   - The highest version number (e.g., `_FINAL_v3`) is the canonical version
   - Previous versions (`_FINAL.md`, `_FINAL_v2.md`) can be kept for reference or deleted
   - When reviewing/editing, always work from the latest version
   - Use `/validate-week` to identify which version should be considered authoritative

### Weekly Directory Structure

Each week follows this pattern:

```
Week_X/
├── Day_3_draft.md          # Initial work (delete after finalization)
├── Day_4_REVISED.md        # After review feedback (delete after finalization)
├── TODOs.md                # Week-specific task tracking
├── syllabus_validation_report.md  # Output from /validate-week
└── final/                  # Polished, validated content only
    ├── Day_1_FINAL.md
    ├── Day_1_exercises_FINAL.md
    ├── Day_2_FINAL_v2.md      # Version 2 after additional review
    ├── Day_2_exercises_FINAL_v2.md
    ├── Day_5_FINAL.md
    ├── Day_5_exercises_FINAL.md
    └── Day_5_Appendix_Numerical_Lebesgue.md
```

---

## Common Tasks

### Adding a New Week's Content

1. Create `Week_X/` directory
2. Follow the weekly template from Syllabus.md (Week X section)
3. Include:
   - Daily theory notes (`Day_Y_draft.md` → `Day_Y_FINAL.md`)
   - Exercise solutions (`Day_Y_exercises_FINAL.md`)
   - Friday code synthesis (embedded in `Day_5_FINAL.md` or separate file)
   - Reflection note (3 questions: Mathematical Insight, RL Connection, Open Questions)
4. Run `/validate-week X all` at week's end

### Reviewing/Editing Existing Content

- **Always work from the highest version**: If `Day_2_FINAL_v2.md` exists, review that, not `Day_2_FINAL.md`
- Check against Syllabus.md for adherence to weekly goals
- Verify anchor exercises are solved
- Ensure RL connections are explicit
- Confirm code runs (if provided)
- Use review commands: `/review-all [file]` for comprehensive check

### Revising Based on Feedback

1. Read reviewer feedback carefully (mathematical vs pedagogical vs RL bridge)
2. **First revision**: Create `Day_X_REVISED.md` (don't overwrite draft)
3. **Additional revisions**: Create `Day_X_FINAL_v2.md` (if `Day_X_FINAL.md` already exists)
4. Address each point systematically
5. Run targeted review: `/review-math` if math issues, `/review-pedagogy` if flow issues
6. When satisfied:
   - **First finalization**: Rename to `Day_X_FINAL.md` and move to `final/` subdirectory
   - **Subsequent revisions**: Keep version number (e.g., `Day_X_FINAL_v2.md`), move to `final/`
7. Optional: Delete superseded versions to reduce clutter

### Version Increment Triggers

Create a new version (`_FINAL_v2`, `_FINAL_v3`, etc.) when:
- Additional reviewer feedback requires substantial revision after initial finalization
- Cross-week integration improvements are discovered during later material
- Syllabus validation reveals missing elements
- Pedagogical improvements from reflection or testing

---

## File Management Best Practices

### Do's

- ✅ Use underscores consistently in all filenames
- ✅ Always work from the highest version number
- ✅ Move finalized content to `final/` subdirectory
- ✅ Delete intermediate drafts after finalization
- ✅ Document reason for version increment in commit message
- ✅ Use `/validate-week` to identify authoritative versions

### Don'ts

- ❌ Never use spaces in filenames
- ❌ Don't leave polished content in root `Week_X/` directory
- ❌ Don't work from outdated versions (e.g., `Day_2_FINAL.md` when `Day_2_FINAL_v2.md` exists)
- ❌ Don't create new versions without substantial reason
- ❌ Don't keep obsolete drafts after validation passes

---

## Related Documentation

- **CLAUDE.md**: Main instructions for Claude Code
- **Citation_System_Reference.md**: Citation and indexing system details
- **Best_Practices_and_Pitfalls.md**: Common mistakes and how to avoid them
- **Syllabus.md**: Canonical 48-week study plan with weekly goals
