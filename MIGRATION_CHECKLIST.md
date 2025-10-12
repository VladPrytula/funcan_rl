# Directory Structure Migration Checklist

## ⚠️ NOTE: This Document is a Historical Record

This file documents the **initial migration to day subdirectories** (2025-10-11).

**A subsequent workflow update** (same day) changed how `/revise` and `/edit-polish` commands work:
- They now output to `revisions/day_X/` with descriptive naming (`_revised_math`, `_revised_all`, `_polished`)
- User manually promotes to `final/day_X/` (no automated writes to `final/`)

**For the current complete workflow, see:**
- `WORKFLOW_MANUAL.md` - Quick daily checklist
- `CLAUDE.md` - Comprehensive documentation
- `File_Management_Guide.md` - Detailed file conventions

---

## Overview

This checklist documents the migration from flat subdirectories to day-organized subdirectories for Week 2 onwards.

**Migration Date:** 2025-10-11
**Scope:** Week 2+ (Week 1 retains legacy structure)

---

## What Changed

### Old Structure (Week 2+, pre-migration):
```
Week_X/
├── drafts/
│   ├── Day_1_draft.md
│   ├── Day_2_draft.md
│   └── Day_3_draft.md
├── reviews/
│   ├── Day_1_draft_review_all.md
│   ├── Day_1_draft_math_review.md
│   └── Day_2_draft_pedagogy_review.md
├── revisions/
│   ├── Day_1_REVISED.md
│   └── Day_2_REVISED.md
└── final/
    ├── Day_1_FINAL.md
    └── Day_2_FINAL.md
```

### New Structure (Week 2+, post-migration):
```
Week_X/
├── drafts/
│   ├── day_1/
│   │   └── Day_1_draft.md
│   ├── day_2/
│   │   └── Day_2_draft.md
│   └── day_3/
│       └── Day_3_draft.md
├── reviews/
│   ├── day_1/
│   │   ├── Day_1_draft_review_all.md
│   │   ├── Day_1_draft_math_review.md
│   │   └── Day_1_REVISION_LOG.md
│   ├── day_2/
│   └── day_3/
├── revisions/
│   ├── day_1/
│   │   └── Day_1_REVISED.md
│   ├── day_2/
│   └── day_3/
└── final/
    ├── day_1/
    │   └── Day_1_FINAL.md
    ├── day_2/
    └── day_3/
```

---

## Files Updated

### ✅ Completed
- [x] `CLAUDE.md` - Repository structure, directory rules, daily workflow
- [x] `File_Management_Guide.md` - All workflows, examples, best practices
- [x] `.claude/commands/review-math.md` - Output path instructions
- [x] `.claude/commands/review-pedagogy.md` - Output path instructions
- [x] `.claude/commands/review-rl-bridge.md` - Output path instructions
- [x] `.claude/commands/review-all.md` - Output path instructions

### ⏳ Remaining
- [ ] `agent.md` - Update any file path references in Professor Dubois persona
- [ ] `Best_Practices_and_Pitfalls.md` - Update path examples
- [ ] `.claude/commands/revise.md` - Update to look for reviews in reviews/day_X/
- [ ] `.claude/commands/validate-week.md` - Update to search day_X/ subdirectories
- [ ] `.claude/commands/validate-citations.md` - Verify handles subdirectories
- [ ] `.claude/commands/validate-index.md` - Verify handles subdirectories

---

## Week 2 File Migration Plan

### Current Week 2 State (Pre-Migration)
```
Week_2/
├── drafts/
│   ├── (files if any)
├── reviews/
│   ├── Day_3_REVISION_LOG.md
│   ├── Day_3_draft_math_review.md
│   └── Day_3_REVISED_math_review.md
├── revisions/
│   ├── Day_3_REVISED.md
│   └── Day_3_exercises_REVISED.md
├── final/
│   ├── Day_1_FINAL.md
│   ├── Day_1_exercises_FINAL.md
│   ├── Day_1_FINAL.md.bak
│   ├── Day_1_FINAL_CITATION_APPLIED.md
│   ├── Day_1_FINAL_CITATION_AUDIT.md
│   ├── Day_2_FINAL.md
│   ├── Day_2_exercises_FINAL.md
│   └── (possibly Day_3 files)
└── archived/
    └── (various old files)
```

### Migration Steps

**For Day 1:**
1. Create `Week_2/final/day_1/`
2. Move:
   - `final/Day_1_FINAL.md` → `final/day_1/Day_1_FINAL.md`
   - `final/Day_1_exercises_FINAL.md` → `final/day_1/Day_1_exercises_FINAL.md`
3. Handle variants:
   - `final/Day_1_FINAL.md.bak` → `archived/day_1/Day_1_FINAL.md.bak`
   - `final/Day_1_FINAL_CITATION_APPLIED.md` → `archived/day_1/` (or delete)
   - `final/Day_1_FINAL_CITATION_AUDIT.md` → `archived/day_1/` (or delete)

**For Day 2:**
1. Create `Week_2/final/day_2/`
2. Move:
   - `final/Day_2_FINAL.md` → `final/day_2/Day_2_FINAL.md`
   - `final/Day_2_exercises_FINAL.md` → `final/day_2/Day_2_exercises_FINAL.md`

**For Day 3:**
1. Create subdirectories:
   ```bash
   mkdir -p Week_2/reviews/day_3
   mkdir -p Week_2/revisions/day_3
   mkdir -p Week_2/final/day_3
   ```
2. Move review files:
   - `reviews/Day_3_REVISION_LOG.md` → `reviews/day_3/Day_3_REVISION_LOG.md`
   - `reviews/Day_3_draft_math_review.md` → `reviews/day_3/Day_3_draft_math_review.md`
   - `reviews/Day_3_REVISED_math_review.md` → `reviews/day_3/Day_3_REVISED_math_review.md`
3. Move revision files:
   - `revisions/Day_3_REVISED.md` → `revisions/day_3/Day_3_REVISED.md`
   - `revisions/Day_3_exercises_REVISED.md` → `revisions/day_3/Day_3_exercises_REVISED.md`
4. If Day_3_FINAL exists, move to `final/day_3/`

---

## Testing Plan

After migration:

1. **Verify file paths:**
   ```bash
   ls -R Week_2/final/day_1/
   ls -R Week_2/final/day_2/
   ls -R Week_2/reviews/day_3/
   ls -R Week_2/revisions/day_3/
   ```

2. **Test review commands:**
   ```bash
   /review-math Week_2/revisions/day_3/Day_3_REVISED.md
   # Should write to: Week_2/reviews/day_3/Day_3_REVISED_math_review.md
   ```

3. **Test validation:**
   ```bash
   /validate-citations Week_2/final/day_1/Day_1_FINAL.md
   /validate-index Week_2/final/day_1/Day_1_FINAL.md
   ```

4. **Verify Obsidian links:** Check that internal links still work after migration

---

## Rollback Plan

If issues arise:

1. Keep this migration checklist
2. Original file paths documented above
3. Can reverse with:
   ```bash
   mv Week_2/final/day_1/* Week_2/final/
   mv Week_2/final/day_2/* Week_2/final/
   mv Week_2/reviews/day_3/* Week_2/reviews/
   mv Week_2/revisions/day_3/* Week_2/revisions/
   rmdir Week_2/final/day_* Week_2/reviews/day_* Week_2/revisions/day_*
   ```

---

## Post-Migration Cleanup

After verifying new structure works:

- Delete empty old directories
- Update any TODO.md references to use new paths
- Commit with clear message documenting migration

---

**Status:** In Progress
**Next Action:** Execute Week 2 file migration
