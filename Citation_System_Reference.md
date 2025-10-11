# Citation System Reference

This document provides comprehensive documentation for the citation and indexing system used throughout the 48-week study plan to maintain rigor and traceability.

---

## Overview

To maintain rigor and traceability across 48 weeks of mathematical content, a comprehensive citation and cross-referencing system is in place. This system ensures:

1. **External citations** (books, papers) are tracked in a central bibliography
2. **Internal cross-references** (theorems, lemmas, definitions) are indexed systematically
3. **Validation tools** verify citation/reference integrity automatically

---

## Core Infrastructure Files

### 1. `references.bib` - Master Bibliography

**Purpose:** Central BibTeX database for all external sources (books, papers, articles).

**Citation Key Format:** `author:shortname:year`

**Examples:**
- `@folland:real_analysis:1999` - Folland's "Real Analysis"
- `@brezis:functional_analysis:2011` - Brezis's "Functional Analysis"
- `@mnih:dqn:2015` - DQN Nature paper
- `@puterman:mdp:2014` - Puterman's MDP textbook

**Usage in daily files:**
```markdown
By the Carathéodory Extension Theorem [@folland:real_analysis:1999, §1.2, Thm 1.14], we have...

This approach follows [@brezis:functional_analysis:2011, §3.2; @durrett:probability:2019, Thm 1.6.1].
```

**Maintenance:**
- Add new sources immediately when first cited
- Use consistent key format: `author:shortname:year`
- Include `note` field explaining relevance to study plan
- Organized by tiers (Tier 1: Weekly Use, Tier 2: Regular Reference, Tier 3: Specialized)

### 2. `Master_Index.md` - Formal Results Registry

**Purpose:** Central index tracking every definition, theorem, lemma, proposition, corollary, and example produced during the 48-week plan.

**ID Format:** `TYPE-W.D.N` where:
- `TYPE` ∈ {`DEF`, `THM`, `LEM`, `PROP`, `COR`, `EX`, `POSTPONE`}
- `W` = Week number (1-48)
- `D` = Day number (1-5)
- `N` = Sequential number within that day (1, 2, 3, ...)

**Examples:**
- `THM-2.3.1` = Week 2, Day 3, Theorem 1 (Dominated Convergence Theorem)
- `DEF-1.4.5` = Week 1, Day 4, Definition 5
- `LEM-3.2.2` = Week 3, Day 2, Lemma 2
- `PROP-1.1.3` = Week 1, Day 1, Proposition 3

**Index Structure:**
- **Definitions table**: All formal definitions (standard and original)
- **Theorems table**: Major results with proof status and dependencies
- **Lemmas table**: Technical supporting results
- **Propositions table**: Formalized exercises and intermediate results
- **Corollaries table**: Direct consequences of theorems
- **Examples table**: Canonical examples and counterexamples
- **Postponed Generalizations**: Simplified proofs deferred to later weeks

**Usage in daily files:**
```markdown
### Theorem 2.3.1 (Dominated Convergence) {#THM-2.3.1}

**Statement:** [@folland:real_analysis:1999, Thm 2.24] If $|f_n| \leq g \in L^1$, then...

*Proof.*
By [DEF-1.2.1] (measure definition) and [THM-1.4.2] (Monotone Convergence), we have...
Using [LEM-2.1.1] (Fatou's Lemma), the result follows.
□
```

**Key Features:**
- **Version-aware**: Always references canonical (highest version) files
- **Dependency tracking**: Links results to their prerequisites
- **Usage tracking**: Shows which later results depend on each entry
- **Status tracking**: Proved / Sketch / Stated / Postponed / Exercise
- **Reference linking**: Connects to external citations in `references.bib`

### 3. `Citation_Guide.md` - Quick Reference

**Purpose:** Concise syntax guide for citations and cross-references.

**Key Patterns:**

**External Citations:**
```markdown
[@folland:real_analysis:1999]                    # Basic citation
[@brezis:functional_analysis:2011, §3.2]        # With section
[@mnih:dqn:2015; @schulman:ppo:2017]            # Multiple sources
```

**Internal Cross-References:**
```markdown
[THM-2.3.1]                                      # Reference theorem
[DEF-1.4.2], [LEM-2.1.1], [PROP-3.2.5]          # Multiple references
```

**Result Labels:**
```markdown
### Theorem 2.3.1 (Name) {#THM-2.3.1}            # Add anchor for backlinking
```

---

## Validation Tools (Slash Commands)

### `/validate-citations [file-path]`

**Purpose:** Verify that all `[@cite_key]` references exist in `references.bib`.

**What it checks:**
- Extracts all citation patterns: `[@key]`, `[@key, §X.Y]`, `[@key1; @key2]`
- Cross-references against `references.bib` entries
- Identifies missing citations
- Detects syntax errors (missing `@`, incorrect format)
- Reports citation frequency statistics

**Output:** Structured validation report with:
- ✅ Valid citations (with line numbers and frequency)
- ❌ Missing citations (action required)
- ⚠️ Syntax issues (corrections needed)

**When to run:**
- After finalizing each day (`Day_X_FINAL.md`)
- Before weekly validation
- After adding new external references

### `/validate-index [file-path]`

**Purpose:** Verify that all `[TYPE-W.D.N]` cross-references exist in `Master_Index.md`.

**What it checks:**
- Extracts all internal references: `[THM-X.Y.Z]`, `[DEF-X.Y.Z]`, `[LEM-X.Y.Z]`, etc.
- Cross-references against `Master_Index.md` entries
- Identifies undefined references
- Checks that labeled results `{#THM-X.Y.Z}` are indexed
- Validates dependency chains (no circular dependencies)
- Flags forward references to future weeks

**Output:** Structured validation report with:
- ✅ Valid references (with Master_Index.md lookup)
- ❌ Missing references (must be added to index)
- 🏷️ Labels defined but not indexed
- 🔗 Dependency chain validation
- 🔍 Forward reference analysis

**When to run:**
- After finalizing each day (`Day_X_FINAL.md`)
- After adding new formal results
- Before weekly validation
- When cross-referencing earlier weeks

---

## Daily Workflow Integration

### While Writing `Day_X_draft.md` or `Day_X_FINAL.md`:

1. **Cite external sources:**
   ```markdown
   By the Carathéodory Extension Theorem [@folland:real_analysis:1999, Thm 1.14], every premeasure...
   ```

2. **Label your formal results:**
   ```markdown
   ### Definition 2.3.5 (Lᵖ Space) {#DEF-2.3.5}

   ### Theorem 1.4.2 (Monotone Convergence) {#THM-1.4.2}

   ### Lemma 3.1.1 (Dynkin π-λ) {#LEM-3.1.1}
   ```

3. **Cross-reference earlier results:**
   ```markdown
   Recall from [DEF-1.1.1] that $\mathcal{A}$ is a σ-algebra.

   By [THM-1.3.1] (Carathéodory Extension) and [LEM-1.2.1] (Dynkin π-λ), we have...
   ```

### After Finalizing `Day_X_FINAL.md`:

4. **Update `Master_Index.md`:**
   - Add all new formal results (definitions, theorems, lemmas, propositions)
   - Fill in: ID, Name, Location (with version), Status, Dependencies, References
   - Use templates provided in `Master_Index.md` for consistency

5. **Run validation:**
   ```bash
   /validate-citations Week_Y/Day_X_FINAL_vN.md
   /validate-index Week_Y/Day_X_FINAL_vN.md
   ```

6. **Fix any issues:**
   - Add missing citations to `references.bib`
   - Add missing results to `Master_Index.md`
   - Correct typos in citation keys or cross-reference IDs
   - Re-run validation to confirm fixes

7. **Update retroactively:**
   - For earlier results used in today's work, update their "Used In" field in `Master_Index.md`
   - Example: If `Day_3` uses `THM-1.2.1`, add `THM-3.X.Y` to `THM-1.2.1`'s "Used In" column

### At Week's End:

8. **Comprehensive validation:**
   ```bash
   /validate-citations Week_Y/*_FINAL*.md
   /validate-index Week_Y/*_FINAL*.md
   /validate-week Y all
   ```

9. **Update `Master_Index.md` statistics:**
   - Total results by type (DEF, THM, LEM, PROP, COR, EX)
   - Results by status (Proved, Sketch, Postponed)
   - Week-by-week progress tracker

10. **Review postponed generalizations:**
    - Document any proofs simplified for time constraints
    - Specify return week and RL application motivation

---

## Version Management and Citations

**Important:** When creating new versions (`Day_X_FINAL_v2.md`, `Day_X_FINAL_v3.md`):

1. **Update `Master_Index.md` Location fields** to point to the new canonical version:
   ```markdown
   | THM-2.3.1 | Dominated Convergence | ... | Week_2/Day_3_FINAL_v2.md:45 | ... |
   ```

2. **Do NOT renumber IDs** - `THM-2.3.1` remains `THM-2.3.1` across all versions

3. **Add version notes** in content files:
   ```markdown
   ### Theorem 2.3.1 (Dominated Convergence) {#THM-2.3.1}

   **Version note:** Proof expanded in v2 based on reviewer feedback (clarified measurability in Step 2).
   ```

4. **Validation commands auto-detect** the highest version number

---

## Best Practices

### Citation Discipline

- ✅ **Do:** Cite original sources for all theorems, even if "standard"
- ✅ **Do:** Include section/theorem numbers: `[@folland:real_analysis:1999, §2.3, Thm 2.14]`
- ✅ **Do:** Add new sources to `references.bib` immediately when first cited
- ❌ **Don't:** Use inconsistent citation keys (stick to `author:shortname:year`)
- ❌ **Don't:** Cite sources not in `references.bib` (fails validation)

### Cross-Reference Discipline

- ✅ **Do:** Label every formal result with `{#TYPE-W.D.N}`
- ✅ **Do:** Use full result names on first mention: `[THM-1.3.1] (Monotone Convergence)`
- ✅ **Do:** Check dependencies before referencing (earlier weeks only, unless marked)
- ❌ **Don't:** Skip labeling theorems/lemmas (breaks cross-referencing)
- ❌ **Don't:** Forward-reference without explicit note ("We will prove this in Week X")

### Index Maintenance

- ✅ **Do:** Update `Master_Index.md` same day as finalizing content
- ✅ **Do:** Run `/validate-index` before committing
- ✅ **Do:** Update "Used In" fields retroactively when using earlier results
- ❌ **Don't:** Let index drift out of sync (causes validation failures)
- ❌ **Don't:** Renumber IDs when creating new versions (breaks references)

---

## Weekly Checklist

```
□ All days have results indexed in Master_Index.md
□ All external citations validated (/validate-citations)
□ All internal references validated (/validate-index)
□ Postponed generalizations documented
□ Statistics in Master_Index.md updated
□ references.bib contains all cited sources
```

---

## Future Splitting Strategy

When `Master_Index.md` grows large (estimated Week 12-15), consider topic-based splitting:
- `Master_Index_Measure_Theory.md` (Weeks 1-6, 10-12)
- `Master_Index_Functional_Analysis.md` (Weeks 13-18)
- `Master_Index_Sobolev_PDEs.md` (Weeks 19-24)
- `Master_Index_MDPs.md` (Weeks 25-28)
- `Master_Index_Bandits.md` (Weeks 29-33)
- `Master_Index_SA_RL.md` (Weeks 34-39)
- `Master_Index_Advanced.md` (Weeks 40-48)

Keep unified `Master_Index.md` as aggregator with links to topic-specific indices.

---

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `/validate-citations` reports missing `@key` | Citation not in `references.bib` | Add BibTeX entry to `references.bib` with correct key format |
| `/validate-index` reports undefined `[THM-X.Y.Z]` | Result not indexed | Add entry to appropriate table in `Master_Index.md` |
| Validation finds syntax error `[folland:1999]` | Missing `@` symbol | Correct to `[@folland:real_analysis:1999]` |
| Result labeled `{#THM-X.Y.Z}` but not indexed | Forgot to update index | Add full entry to `Master_Index.md` Theorems table |
| Circular dependency detected | Result A depends on B, B depends on A | Restructure proof or merge into single result |
| Forward reference to Week 10 in Week 2 | Referencing future material | Mark explicitly: "We will prove this in [THM-10.3.1] (Week 10)" |

---

# Citation Metadata Validation

## Overview

Beyond verifying that citations exist in `references.bib`, the system can validate the **metadata accuracy** of bibliographic entries by checking ISBNs, DOIs, arXiv IDs, URLs, and search engine findability.

**Purpose:** Ensure all cited sources:
- Actually exist (DOIs resolve, arXiv IDs are valid)
- Are findable by others (search engine verification)
- Have correct metadata (no typos in ISBNs, years, etc.)
- Don't have broken URLs (link rot detection)

---

## Core Tool: `/validate-citations-metadata`

**Script:** `scripts/validate_citations_metadata.py`
**Config:** `scripts/citation_validation_config.json`
**Reports:** `scripts/citation_validation_report.json` and `.md`

---

## Validation Levels

### Fast Level (Offline, ~5 seconds)

```bash
/validate-citations-metadata --level fast
```

**Checks:**
- ✅ ISBN format (13-digit + checksum validation)
- ✅ DOI format (starts with `10.`, structural checks)
- ✅ Year sanity (4 digits, reasonable range)
- ✅ Basic field presence (title, author)

**Use when:** Quick checks before committing, no internet needed

### Thorough Level (Online, ~2-3 minutes for 79 entries)

```bash
/validate-citations-metadata --level thorough
```

**Checks (all fast checks plus):**
- ✅ DOI resolution via DOI.org API (verify paper exists, cross-check metadata)
- ✅ arXiv validation via arXiv API (verify paper exists, check version)
- ✅ URL reachability (HTTP HEAD, detect 404s and timeouts)
- ✅ SearXNG search verification (query local instance, verify findability)
- ✅ Metadata consistency (cross-check data across sources)

**Use when:** Weekly maintenance, before major milestones, after bulk imports

---

## SearXNG Integration

**Your Local Instance:** `http://localhost:9090/`

The validation system queries your SearXNG instance to verify that citations are findable via search engines. This simulates what a reader would experience when trying to locate a source.

**What it does:**
1. Searches for: `"title" "author" year`
2. Checks if entry appears in top results
3. Assigns confidence score (0-100%) based on match quality

**Custom URL:**
```bash
/validate-citations-metadata --searxng-url http://192.168.1.100:8080/
```

---

## Output Reports

### JSON Report (`scripts/citation_validation_report.json`)

Machine-readable, contains:
- Full validation results for all entries
- Confidence scores
- Detailed check results
- Metadata from APIs (DOI, arXiv)

### Markdown Report (`scripts/citation_validation_report.md`)

Human-readable, contains:
- Summary statistics (✅ valid, ⚠️ warnings, ❌ errors)
- Detailed issues with actionable recommendations
- Confidence scores for each entry

---

## When to Run

**Recommended frequency:**
1. **Weekly**: After adding new sources to `references.bib`
2. **Before major milestones**: Phase completions, thesis defense
3. **After bulk imports**: When adding many sources at once
4. **Bi-monthly**: General maintenance to catch link rot

**Integration with existing workflow:**
```bash
# After adding new citations to daily file
/validate-citations Week_X/Day_Y_FINAL.md         # Check syntax
# After updating references.bib
/validate-citations-metadata --level thorough      # Check metadata
```

---

## Common Issues and Fixes

| Issue | Cause | Solution |
|-------|-------|----------|
| DOI does not resolve | Incorrect DOI or paper not yet indexed | Verify at https://doi.org/[doi], search on Google Scholar |
| URL returns 404 | Link rot, page moved | Update URL or mark as unavailable |
| arXiv ID not found | Typo or paper withdrawn | Verify at https://arxiv.org/abs/[id] |
| SearXNG no results | Title typo, very recent paper | Check spelling, wait and re-validate |
| ISBN invalid | Typo or incorrect ISBN | Verify on publisher website |

---

## Configuration

Edit `scripts/citation_validation_config.json` to customize behavior:

```json
{
  "searxng_url": "http://localhost:9090/",
  "enable_doi_validation": true,
  "enable_arxiv_validation": true,
  "enable_url_validation": true,
  "enable_searxng_validation": true,
  "http_timeout_seconds": 10
}
```

**Disable specific checks:** Set `enable_*` to `false`
**Adjust timeouts:** Increase `http_timeout_seconds` if requests time out

---

## Dependencies

**Required Python packages:**
```bash
pip install bibtexparser requests isbnlib
```

Or via `requirements.txt`:
```
bibtexparser>=1.4.0
requests>=2.31.0
isbnlib>=3.10.0
```

---

## Enhanced Weekly Checklist

```
□ All days have results indexed in Master_Index.md
□ All external citations validated (/validate-citations)
□ All internal references validated (/validate-index)
□ Citation metadata validated (/validate-citations-metadata)
□ Postponed generalizations documented
□ Statistics in Master_Index.md updated
□ references.bib contains all cited sources with accurate metadata
```

---

## Related Documentation

- **CLAUDE.md**: Main instructions for Claude Code
- **File_Management_Guide.md**: File naming, versioning, and workflow
- **Best_Practices_and_Pitfalls.md**: Common mistakes and how to avoid them
- **Citation_Guide.md**: Quick syntax reference for citations
- **Master_Index.md**: Central registry of all formal results
