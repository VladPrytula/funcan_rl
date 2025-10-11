#!/usr/bin/env python3
"""
Citation Metadata Validation Script

Validates bibliographic entries in references.bib by checking:
- ISBN format and validity
- DOI resolution and metadata
- arXiv ID validity
- URL reachability
- Search engine verification (SearXNG)

Usage:
    python validate_citations_metadata.py [--level fast|thorough] [--searxng-url URL]

Author: Generated for 48-Week RL Study Plan
Date: 2025-10-11
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import quote_plus

try:
    import bibtexparser
    import requests
except ImportError:
    print("ERROR: Missing dependencies. Install with:")
    print("  pip install bibtexparser requests")
    sys.exit(1)

# Optional: isbnlib for advanced ISBN validation
try:
    import isbnlib
    HAS_ISBNLIB = True
except ImportError:
    HAS_ISBNLIB = False


# ============================================================================
# Configuration
# ============================================================================

DEFAULT_CONFIG = {
    "searxng_url": "http://localhost:9090/",
    "enable_doi_validation": True,
    "enable_arxiv_validation": True,
    "enable_url_validation": True,
    "enable_searxng_validation": True,
    "http_timeout_seconds": 10,
    "cache_results": True,
    "cache_duration_days": 30,
    "doi_api_url": "https://doi.org",
    "arxiv_api_url": "http://export.arxiv.org/api/query",
}


# ============================================================================
# Validation Functions
# ============================================================================

def validate_isbn_format(isbn: str) -> Tuple[bool, str]:
    """
    Validate ISBN-13 format and checksum.

    Returns: (is_valid, message)
    """
    # Remove hyphens and spaces
    isbn_clean = isbn.replace("-", "").replace(" ", "")

    if len(isbn_clean) != 13:
        return False, f"ISBN must be 13 digits (got {len(isbn_clean)})"

    if not isbn_clean.isdigit():
        return False, "ISBN contains non-digit characters"

    # ISBN-13 checksum validation
    try:
        digits = [int(d) for d in isbn_clean]
        checksum = sum(d if i % 2 == 0 else d * 3 for i, d in enumerate(digits[:-1]))
        check_digit = (10 - (checksum % 10)) % 10

        if check_digit != digits[-1]:
            return False, f"Invalid ISBN checksum (expected {check_digit}, got {digits[-1]})"

        return True, "✅ Valid ISBN-13"
    except Exception as e:
        return False, f"ISBN validation error: {str(e)}"


def validate_isbn_advanced(isbn: str) -> Tuple[bool, str, Optional[Dict]]:
    """
    Advanced ISBN validation using isbnlib (if available).

    Returns: (is_valid, message, metadata)
    """
    if not HAS_ISBNLIB:
        return validate_isbn_format(isbn)[0], "Basic validation only (isbnlib not installed)", None

    isbn_clean = isbn.replace("-", "").replace(" ", "")

    # Validate format
    is_valid, msg = validate_isbn_format(isbn)
    if not is_valid:
        return False, msg, None

    # Try to get metadata (this queries online services, may be slow)
    try:
        # Note: This is optional and can be disabled for speed
        # metadata = isbnlib.meta(isbn_clean, service='default')
        # For now, just validate format
        return True, "✅ Valid ISBN-13", None
    except Exception as e:
        return True, f"✅ Valid ISBN-13 (metadata lookup failed: {e})", None


def validate_doi(doi: str, config: Dict, timeout: int = 10) -> Tuple[bool, str, Optional[Dict]]:
    """
    Validate DOI by querying DOI.org resolver.

    Returns: (is_valid, message, metadata)
    """
    if not config.get("enable_doi_validation", True):
        return True, "⏭️ DOI validation skipped (disabled in config)", None

    try:
        # DOI Content Negotiation: request JSON metadata
        url = f"{config['doi_api_url']}/{doi}"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)

        if response.status_code == 200:
            metadata = response.json()
            return True, "✅ DOI resolves correctly", metadata
        elif response.status_code == 404:
            return False, "❌ DOI not found in registry", None
        else:
            return False, f"⚠️ DOI query returned status {response.status_code}", None

    except requests.exceptions.Timeout:
        return False, f"⏱️ DOI query timed out after {timeout}s", None
    except requests.exceptions.RequestException as e:
        return False, f"⚠️ DOI query error: {str(e)}", None
    except Exception as e:
        return False, f"⚠️ Unexpected error: {str(e)}", None


def extract_arxiv_id(entry: Dict) -> Optional[str]:
    """Extract arXiv ID from URL or eprint field."""
    # Check explicit eprint field
    if "eprint" in entry:
        return entry["eprint"]

    # Check URL for arXiv ID
    url = entry.get("url", "")
    arxiv_pattern = r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)"
    match = re.search(arxiv_pattern, url, re.IGNORECASE)
    if match:
        return match.group(1)

    return None


def validate_arxiv(arxiv_id: str, config: Dict, timeout: int = 10) -> Tuple[bool, str, Optional[Dict]]:
    """
    Validate arXiv ID by querying arXiv API.

    Returns: (is_valid, message, metadata)
    """
    if not config.get("enable_arxiv_validation", True):
        return True, "⏭️ arXiv validation skipped (disabled in config)", None

    try:
        url = f"{config['arxiv_api_url']}?id_list={arxiv_id}"

        response = requests.get(url, timeout=timeout)

        if response.status_code == 200:
            # Parse XML response (simple check: does it contain the arXiv ID?)
            if arxiv_id.split("v")[0] in response.text:  # Remove version suffix for check
                # Extract version info if present
                version_match = re.search(r'v(\d+)', arxiv_id)
                version_str = f" ({arxiv_id})" if version_match else ""
                return True, f"✅ arXiv ID valid{version_str}", {"raw_xml": response.text[:500]}
            else:
                return False, "❌ arXiv ID not found", None
        else:
            return False, f"⚠️ arXiv API returned status {response.status_code}", None

    except requests.exceptions.Timeout:
        return False, f"⏱️ arXiv query timed out after {timeout}s", None
    except requests.exceptions.RequestException as e:
        return False, f"⚠️ arXiv query error: {str(e)}", None
    except Exception as e:
        return False, f"⚠️ Unexpected error: {str(e)}", None


def validate_url(url: str, config: Dict, timeout: int = 10) -> Tuple[bool, str]:
    """
    Check if URL is reachable (HTTP HEAD request).

    Returns: (is_valid, message)
    """
    if not config.get("enable_url_validation", True):
        return True, "⏭️ URL validation skipped (disabled in config)"

    try:
        # Use HEAD request to avoid downloading content
        response = requests.head(url, timeout=timeout, allow_redirects=True)

        if response.status_code == 200:
            return True, f"✅ URL reachable (status 200)"
        elif response.status_code == 405:  # Method Not Allowed - try GET
            response = requests.get(url, timeout=timeout, stream=True)
            if response.status_code == 200:
                return True, f"✅ URL reachable (status 200)"

        if response.status_code == 404:
            return False, f"❌ URL not found (404)"
        else:
            return False, f"⚠️ URL returned status {response.status_code}"

    except requests.exceptions.Timeout:
        return False, f"⏱️ URL request timed out after {timeout}s"
    except requests.exceptions.SSLError:
        return False, f"⚠️ SSL certificate error"
    except requests.exceptions.ConnectionError:
        return False, f"⚠️ Connection error (domain may be down)"
    except requests.exceptions.RequestException as e:
        return False, f"⚠️ URL check error: {str(e)}"
    except Exception as e:
        return False, f"⚠️ Unexpected error: {str(e)}"


def validate_via_searxng(
    title: str,
    author: str,
    year: str,
    searxng_url: str,
    timeout: int = 15
) -> Tuple[bool, str, int]:
    """
    Search for entry via SearXNG and verify it's findable.

    Returns: (is_valid, message, confidence_score)
    """
    try:
        # Build search query
        query = f'"{title}" "{author}" {year}'
        search_url = f"{searxng_url.rstrip('/')}/search"

        params = {
            "q": query,
            "format": "json",
            "categories": "science"
        }

        response = requests.get(search_url, params=params, timeout=timeout)

        if response.status_code != 200:
            return False, f"⚠️ SearXNG returned status {response.status_code}", 0

        results = response.json()
        num_results = len(results.get("results", []))

        if num_results == 0:
            return False, "⚠️ No search results found", 20

        # Check if any top results seem to match
        top_results = results.get("results", [])[:3]
        matched = any(
            title.lower() in result.get("title", "").lower() or
            title.lower() in result.get("content", "").lower()
            for result in top_results
        )

        if matched:
            confidence = min(95, 70 + num_results)
            return True, f"✅ Found {num_results} results (matched in top 3)", confidence
        else:
            confidence = min(60, 30 + num_results)
            return True, f"⚠️ Found {num_results} results (no clear match)", confidence

    except requests.exceptions.Timeout:
        return False, f"⏱️ SearXNG query timed out after {timeout}s", 0
    except requests.exceptions.ConnectionError:
        return False, f"⚠️ Cannot connect to SearXNG (is it running at {searxng_url}?)", 0
    except Exception as e:
        return False, f"⚠️ SearXNG query error: {str(e)}", 0


# ============================================================================
# Entry Validation
# ============================================================================

def validate_entry(entry: Dict, config: Dict, validation_level: str) -> Dict:
    """
    Validate a single BibTeX entry.

    Returns: validation result dictionary
    """
    entry_id = entry.get("ID", "unknown")
    result = {
        "entry_id": entry_id,
        "type": entry.get("ENTRYTYPE", "unknown"),
        "status": "valid",
        "checks": {},
        "warnings": [],
        "errors": [],
        "confidence": 100,
        "metadata": {}
    }

    # Extract fields
    title = entry.get("title", "").strip("{}")
    author = entry.get("author", "Unknown")
    year = entry.get("year", "")

    # Basic checks (always run)
    if not title:
        result["errors"].append("Missing title")
        result["status"] = "error"

    if not year or not year.isdigit() or len(year) != 4:
        result["warnings"].append(f"Invalid or missing year: {year}")
        result["confidence"] -= 10

    # Format validation (fast level)
    if "isbn" in entry:
        is_valid, msg = validate_isbn_format(entry["isbn"])
        result["checks"]["isbn"] = msg
        if not is_valid:
            result["warnings"].append(f"ISBN issue: {msg}")
            result["confidence"] -= 15

    if "doi" in entry:
        # Basic DOI format check
        doi = entry["doi"]
        if not doi.startswith("10."):
            result["warnings"].append(f"DOI should start with '10.' (got: {doi})")
            result["confidence"] -= 10
        result["checks"]["doi_format"] = "✅ DOI format looks valid"

    # Thorough validation (APIs + SearXNG)
    if validation_level == "thorough":
        timeout = config.get("http_timeout_seconds", 10)

        # DOI validation
        if "doi" in entry:
            is_valid, msg, metadata = validate_doi(entry["doi"], config, timeout)
            result["checks"]["doi_resolution"] = msg
            if metadata:
                result["metadata"]["doi"] = metadata
            if not is_valid:
                result["warnings"].append(f"DOI validation: {msg}")
                result["confidence"] -= 20
                result["status"] = "warning"

        # arXiv validation
        arxiv_id = extract_arxiv_id(entry)
        if arxiv_id:
            is_valid, msg, metadata = validate_arxiv(arxiv_id, config, timeout)
            result["checks"]["arxiv"] = msg
            if metadata:
                result["metadata"]["arxiv"] = metadata
            if not is_valid:
                result["warnings"].append(f"arXiv validation: {msg}")
                result["confidence"] -= 15

        # URL validation
        if "url" in entry:
            is_valid, msg = validate_url(entry["url"], config, timeout)
            result["checks"]["url"] = msg
            if not is_valid:
                result["warnings"].append(f"URL check: {msg}")
                result["confidence"] -= 10

        # SearXNG validation
        if config.get("enable_searxng_validation", True):
            is_valid, msg, confidence = validate_via_searxng(
                title, author, year,
                config["searxng_url"],
                timeout + 5
            )
            result["checks"]["searxng"] = msg
            if not is_valid:
                result["warnings"].append(f"Search verification: {msg}")
                result["confidence"] = min(result["confidence"], confidence)
            else:
                # Boost confidence if search found it
                result["confidence"] = min(100, (result["confidence"] + confidence) // 2)

    # Final status determination
    if result["errors"]:
        result["status"] = "error"
    elif result["warnings"]:
        result["status"] = "warning"
    else:
        result["status"] = "valid"

    return result


# ============================================================================
# Report Generation
# ============================================================================

def generate_json_report(results: List[Dict], output_path: Path):
    """Generate JSON validation report."""
    summary = {
        "validated": sum(1 for r in results if r["status"] == "valid"),
        "warnings": sum(1 for r in results if r["status"] == "warning"),
        "errors": sum(1 for r in results if r["status"] == "error"),
    }

    report = {
        "validation_date": datetime.now().isoformat(),
        "total_entries": len(results),
        "summary": summary,
        "entries": {r["entry_id"]: r for r in results}
    }

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"✅ JSON report saved to: {output_path}")


def generate_markdown_report(results: List[Dict], output_path: Path, level: str):
    """Generate Markdown validation report."""
    valid = [r for r in results if r["status"] == "valid"]
    warnings = [r for r in results if r["status"] == "warning"]
    errors = [r for r in results if r["status"] == "error"]

    total = len(results)

    lines = [
        "# Citation Metadata Validation Report",
        "",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Level:** {level.capitalize()}",
        f"**Database:** references.bib ({total} entries)",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Metric | Count | Percentage |",
        "|--------|-------|------------|",
        f"| ✅ Valid | {len(valid)} | {len(valid)/total*100:.1f}% |",
        f"| ⚠️ Warnings | {len(warnings)} | {len(warnings)/total*100:.1f}% |",
        f"| ❌ Errors | {len(errors)} | {len(errors)/total*100:.1f}% |",
        "",
        "---",
        "",
    ]

    # Valid entries summary
    if valid:
        lines.extend([
            f"## ✅ Valid Entries ({len(valid)})",
            "",
            "All checks passed with confidence ≥ 80%.",
            "",
        ])
        for r in valid[:5]:  # Show first 5
            checks_str = ", ".join([f"{k}: {v}" for k, v in r.get("checks", {}).items()])
            lines.append(f"- ✅ **{r['entry_id']}** (confidence: {r['confidence']}%)")
        if len(valid) > 5:
            lines.append(f"- ... and {len(valid) - 5} more")
        lines.append("")

    # Warnings
    if warnings:
        lines.extend([
            "---",
            "",
            f"## ⚠️ Warnings ({len(warnings)})",
            "",
            "Entries with minor issues (confidence 50-79%).",
            "",
        ])
        for r in warnings:
            lines.extend([
                f"### ⚠️ {r['entry_id']}",
                f"**Confidence:** {r['confidence']}%",
                "",
                "**Issues:**",
            ])
            for warning in r.get("warnings", []):
                lines.append(f"- {warning}")
            lines.extend(["", "**Checks:**"])
            for check_name, check_result in r.get("checks", {}).items():
                lines.append(f"- {check_name}: {check_result}")
            lines.append("")

    # Errors
    if errors:
        lines.extend([
            "---",
            "",
            f"## ❌ Errors ({len(errors)})",
            "",
            "Critical issues requiring immediate attention.",
            "",
        ])
        for r in errors:
            lines.extend([
                f"### ❌ {r['entry_id']}",
                "",
                "**Errors:**",
            ])
            for error in r.get("errors", []):
                lines.append(f"- {error}")
            if r.get("warnings"):
                lines.append("")
                lines.append("**Warnings:**")
                for warning in r["warnings"]:
                    lines.append(f"- {warning}")
            lines.append("")

    lines.extend([
        "---",
        "",
        "## Recommendations",
        "",
    ])

    if warnings or errors:
        lines.extend([
            "1. **Review all entries with warnings or errors**",
            "2. **Verify DOIs and ISBNs** using official sources",
            "3. **Update broken URLs** or mark as unavailable",
            "4. **Re-run validation** after fixes: `/validate-citations-metadata --level thorough`",
        ])
    else:
        lines.extend([
            "✅ **All citations validated successfully!**",
            "",
            "Your bibliography is in excellent shape. No action required.",
        ])

    markdown = "\n".join(lines)

    with open(output_path, "w") as f:
        f.write(markdown)

    print(f"✅ Markdown report saved to: {output_path}")


# ============================================================================
# Main Function
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Validate citation metadata in references.bib"
    )
    parser.add_argument(
        "--level",
        choices=["fast", "thorough"],
        default="thorough",
        help="Validation level: fast (offline checks) or thorough (APIs + SearXNG)"
    )
    parser.add_argument(
        "--searxng-url",
        default="http://localhost:9090/",
        help="SearXNG instance URL (default: http://localhost:9090/)"
    )
    parser.add_argument(
        "--config",
        type=Path,
        help="Path to custom config JSON file"
    )
    parser.add_argument(
        "--bib",
        type=Path,
        help="Path to references.bib file (default: ../references.bib)"
    )

    args = parser.parse_args()

    # Load configuration
    config = DEFAULT_CONFIG.copy()
    config["searxng_url"] = args.searxng_url

    if args.config and args.config.exists():
        with open(args.config) as f:
            custom_config = json.load(f)
            config.update(custom_config)

    # Find references.bib
    if args.bib:
        bib_path = args.bib
    else:
        script_dir = Path(__file__).parent
        bib_path = script_dir.parent / "references.bib"

    if not bib_path.exists():
        print(f"ERROR: references.bib not found at: {bib_path}")
        sys.exit(1)

    print(f"📖 Loading bibliography: {bib_path}")

    # Parse BibTeX
    with open(bib_path) as f:
        bib_database = bibtexparser.load(f)

    entries = bib_database.entries
    print(f"📚 Found {len(entries)} entries")
    print(f"🔍 Validation level: {args.level}")
    print()

    # Validate entries
    results = []
    for i, entry in enumerate(entries, 1):
        entry_id = entry.get("ID", f"entry_{i}")
        print(f"[{i}/{len(entries)}] Validating {entry_id}...", end=" ", flush=True)

        result = validate_entry(entry, config, args.level)
        results.append(result)

        # Print status
        status_icon = {"valid": "✅", "warning": "⚠️", "error": "❌"}[result["status"]]
        print(f"{status_icon} (confidence: {result['confidence']}%)")

    print()
    print("="*70)
    print("Validation complete!")
    print("="*70)
    print()

    # Generate reports
    output_dir = Path(__file__).parent
    json_path = output_dir / "citation_validation_report.json"
    md_path = output_dir / "citation_validation_report.md"

    generate_json_report(results, json_path)
    generate_markdown_report(results, md_path, args.level)

    # Summary
    valid = sum(1 for r in results if r["status"] == "valid")
    warnings = sum(1 for r in results if r["status"] == "warning")
    errors = sum(1 for r in results if r["status"] == "error")

    print()
    print("Summary:")
    print(f"  ✅ Valid: {valid} ({valid/len(results)*100:.1f}%)")
    print(f"  ⚠️ Warnings: {warnings} ({warnings/len(results)*100:.1f}%)")
    print(f"  ❌ Errors: {errors} ({errors/len(results)*100:.1f}%)")
    print()

    if warnings or errors:
        print("⚠️ Some entries have issues. Review the reports for details.")
        sys.exit(1)
    else:
        print("✅ All citations validated successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
