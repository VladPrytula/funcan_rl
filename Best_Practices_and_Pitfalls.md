# Best Practices and Common Pitfalls

This document provides guidance on common mistakes to avoid and best practices to follow throughout the 48-week study plan.

---

## Common Pitfalls to Avoid

### Mathematical Content

- **Don't skip hypothesis checks**: Always verify all conditions before applying theorems
- **Counterexamples matter**: When a condition is necessary, construct the counterexample showing why
- **Cross-references**: When citing earlier results, use format "Recall from Day X that..." or "By Theorem Y.Z"
- **Proof completeness**: Mark incomplete proofs explicitly as "Sketch:" or "Outline:" – never leave ambiguous
- **Notation consistency**: Maintain consistent notation within a week (e.g., don't switch between $\mu$ and $m$ for same measure)

### Review Process

**Note:** Starting Week 2, review outputs are automatically written to `Week_X/reviews/` subdirectory.

- **Don't review drafts in isolation**: Provide context from previous days when reviewing Day 3+ content
- **Sequential reviews work best**: Run `/review-math` before `/review-pedagogy` (fix logic before flow)
- **Use batch operations**: `/review-all` gives comprehensive feedback in one pass and writes to `reviews/[file]_review_all.md`
- **Review file organization**: All review outputs automatically saved to `reviews/` subdirectory
- **Context matters**: When agent requests context, provide file paths or paste relevant sections

### Time Management

- **90-minute target is sacred**: If content exceeds 2.5 hours, split immediately—don't defer
- **Document simplifications immediately**: Add to Postponed Generalizations Log right away, not at week's end
- **Friday code scope**: Limit to 30-40 minutes total; resist implementation rabbit holes
- **Don't batch revisions**: Address feedback same day or next day—fresh context is crucial

### File Management

**Note:** This applies to **Week 2 onwards** (structured subdirectories). Week 1 uses legacy structure.

- **Use day subdirectories**: Organize workflow stages by day (drafts/day_X/, reviews/day_X/, revisions/day_X/, final/day_X/)
- **Automated outputs go to revisions/**: `/revise` and `/edit-polish` commands write to `revisions/day_X/` with descriptive names
  - `Day_X_revised_math.md`, `Day_X_revised_all.md`, `Day_X_polished.md`
- **User controls final/**: Manually move files from `revisions/` to `final/` when satisfied, adding `_FINAL` postfix
- **Delete obsolete files**: Once finalized, remove drafts and intermediate revisions
- **Version hierarchy**: When `final/day_X/Day_X_FINAL_v2.md` exists, it supersedes `Day_X_FINAL.md`
  - Always work from the highest version number
  - Delete previous versions once superseded to reduce clutter
  - Document reason for version increment in commit message
- **Consistent naming**: Always use underscores `_`, never spaces in filenames
- **Clean root directory**: No work-in-progress files in `Week_X/` root (only TODOs.md and validation reports)
- **Automatic reviews**: Review commands write output to `reviews/day_X/` subdirectory automatically
- **Version control**: Commit after each major stage (draft → revision → polish → final → v2 → v3, etc.)

---

## Best Practices

### Mathematical Rigor

- ✅ **Do:** State all hypotheses explicitly in theorem statements
- ✅ **Do:** Construct counterexamples for "necessity" results
- ✅ **Do:** Mark proof status clearly (Complete / Sketch / Outline / Postponed)
- ✅ **Do:** Verify all conditions before applying theorems
- ✅ **Do:** Maintain consistent notation throughout each week

### Pedagogical Clarity

- ✅ **Do:** Include explicit "RL Connection" sections
- ✅ **Do:** Recall earlier results with clear references
- ✅ **Do:** Preview future applications ("We will use this in Week X...")
- ✅ **Do:** Provide motivation before introducing abstractions
- ✅ **Do:** Follow the four-part structure (Motivation → Theory → Proofs → Application)

### Time Management

- ✅ **Do:** Aim for 90 minutes per session (Mon-Fri)
- ✅ **Do:** Accept up to 2.5 hours for dense material
- ✅ **Do:** Split content immediately if exceeding 2.5 hours
- ✅ **Do:** Document simplifications in Postponed Generalizations Log
- ✅ **Do:** Take weekends completely off

### Review Workflow

- ✅ **Do:** Run `/review-math` first to fix logical issues (output written to `reviews/day_X/` subdirectory)
- ✅ **Do:** Follow with `/review-pedagogy` for flow/clarity
- ✅ **Do:** Use `/review-rl-bridge` to verify connections
- ✅ **Do:** Or use `/review-all` for comprehensive feedback in one pass
- ✅ **Do:** Check `Week_X/reviews/day_X/` subdirectory for all review outputs
- ✅ **Do:** Use `/revise` to incorporate feedback → outputs to `revisions/day_X/` with descriptive postfix
- ✅ **Do:** Use `/edit-polish` for final polish → outputs to `revisions/day_X/Day_X_polished.md`
- ✅ **Do:** Manually finalize to `final/day_X/Day_X_FINAL.md` when satisfied
- ✅ **Do:** Provide context from earlier days when reviewing Day 3+ content

### File Management

**Note:** Week 2+ uses structured subdirectories organized by day (drafts/day_X/, reviews/day_X/, revisions/day_X/, final/day_X/).

- ✅ **Do:** Always work from the highest version number
- ✅ **Do:** Use underscores consistently in filenames
- ✅ **Do:** Organize work by day subdirectory (drafts/day_X/ → revisions/day_X/ → final/day_X/)
- ✅ **Do:** Let review commands automatically write to `reviews/day_X/` subdirectory
- ✅ **Do:** Let `/revise` and `/edit-polish` automatically write to `revisions/day_X/` with descriptive names
- ✅ **Do:** Manually move from `revisions/` to `final/` when satisfied (user-controlled)
- ✅ **Do:** Delete intermediate drafts and revisions after finalization
- ✅ **Do:** Keep root `Week_X/` directory clean (only TODOs.md and validation reports)
- ✅ **Do:** Document version increment reasons in commit messages

### Citation and Indexing

- ✅ **Do:** Cite original sources for all theorems (even "standard" ones)
- ✅ **Do:** Include section/theorem numbers in citations
- ✅ **Do:** Label all formal results with `{#TYPE-W.D.N}` anchors
- ✅ **Do:** Update `Master_Index.md` same day as finalizing content
- ✅ **Do:** Run validation tools before committing
- ✅ **Do:** Update "Used In" fields retroactively

---

## Review Agent Context Awareness

When using review agents (review-math, review-pedagogy, review-rl-bridge), they will automatically check:

### Within-Day Coherence

- Internal logical flow
- Definition → Theorem → Proof structure
- Examples and counterexamples

### Cross-Day Continuity

- Backward references (correctly citing previous results)
- Forward references (fulfilling earlier promises)
- Weekly narrative arc (building appropriately)

### Syllabus Alignment

- Proof targets met or justified
- Weekly goals addressed
- Postponed generalizations documented

### Providing Context to Agents

**Important:** If an agent needs context from previous days or Syllabus.md to assess continuity, it will **explicitly request** that content. When this happens:

```bash
# Agent says: "I need to see Day 1-3 to verify this reference"
# You provide context:

# Week 1 (legacy structure)
/review-pedagogy Week_1/final/Day_4_FINAL.md

# Week 2+ (structured subdirectories)
/review-pedagogy Week_2/final/Day_4_FINAL.md

# In the same conversation, paste content from earlier days
# Or provide file paths: "Also review Week_2/final/Day_1_FINAL.md, Day_2_FINAL.md, Day_3_FINAL.md"
```

The agents are **context-aware by design**, but rely on you to provide cross-references when needed.

---

## Mistake Recovery Strategies

### When You Realize a Proof is Incomplete

1. **Mark it explicitly**: Change heading to "Sketch:" or "Outline:"
2. **Document in Postponed Generalizations Log**: Specify what's missing and when to return
3. **Provide RL motivation**: Explain why the full proof matters for later applications
4. **Don't pretend it's complete**: Readers will notice, and it undermines trust

### When Time Constraints are Exceeded

1. **Don't push through**: Fatigue leads to errors and undermines learning
2. **Split the content**: Move material to next day or create appendix
3. **Simplify the proof**: Prove special case, note general case for later
4. **Document the decision**: Add to Postponed Generalizations Log with justification

### When Notation Becomes Inconsistent

1. **Fix it immediately**: Don't let inconsistency propagate to later days
2. **Update earlier references**: Ensure cross-references use new notation
3. **Add a Remark**: "We adopt the convention that... for the remainder of this week"
4. **Check Master_Index.md**: Update any affected result descriptions

### When Citations are Missing

1. **Run `/validate-citations`**: Identify all missing references
2. **Add to `references.bib`**: Use correct key format `author:shortname:year`
3. **Re-run validation**: Confirm all issues resolved
4. **Commit with clear message**: "Add missing citations for Week X Day Y"

### When Cross-References Break

1. **Run `/validate-index`**: Identify undefined references
2. **Add missing results to `Master_Index.md`**: Use correct `TYPE-W.D.N` format
3. **Check for typos**: `[THM-1.2.1]` vs `[THM-1.2.2]`
4. **Update "Used In" fields**: Maintain bidirectional links
5. **Re-run validation**: Confirm all references resolve

---

## Weekly Review Checklist

Use this checklist at the end of each week to ensure quality:

```
□ All theorems have explicit hypotheses
□ All proofs are complete or marked as sketches
□ Counterexamples provided for necessity results
□ RL connections explicit in every section
□ Cross-references to earlier results correct
□ Forward references to later weeks documented
□ All formal results labeled with {#TYPE-W.D.N}
□ Master_Index.md updated with all new results
□ All citations exist in references.bib
□ /validate-citations passes for all days
□ /validate-index passes for all days
□ /validate-week passes for the week
□ Postponed generalizations documented
□ Time targets respected (90 min ± extensions justified)
□ Finalized content moved to Week_X/final/
□ Obsolete drafts deleted
□ Git commits reflect progress clearly
```

---

## Long-Term Maintenance

### Monthly Tasks

- Review Postponed Generalizations Log
- Check if deferred proofs can now be completed
- Verify cross-week dependencies remain valid
- Run `/validate-citations-metadata --level thorough`
- Update `Master_Index.md` statistics

### Phase Completion Tasks

- Comprehensive validation across all weeks in phase
- Review all postponed generalizations for the phase
- Ensure phase goals from Syllabus.md are met
- Create phase summary document
- Commit with "Phase X complete" message

### Semester Milestones

- Validate entire codebase (all weeks completed so far)
- Review and update reference library tiers
- Check for notation drift across phases
- Verify all RL connections remain current with frontier research
- Consider splitting `Master_Index.md` if it's grown large

---

## Related Documentation

- **CLAUDE.md**: Main instructions for Claude Code
- **File_Management_Guide.md**: File naming, versioning, and workflow
- **Citation_System_Reference.md**: Citation and indexing system details
- **Reference_Library_and_Git.md**: Bibliography and version control
- **Syllabus.md**: Canonical 48-week study plan with weekly goals
