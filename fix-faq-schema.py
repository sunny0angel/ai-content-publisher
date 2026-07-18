#!/usr/bin/env python3
"""Fix {{< faq-schema >}} shortcodes by replacing them with proper JSON content."""

import re
import json
import os

BASE = "/Users/yudi/ai-content-publisher/hugo-site/content/blog"

ARTICLES = [
    "ai-adoption-report-2026",
    "ai-bubble-economic-crisis-2026",
    "do-you-still-need-experts-in-ai-era",
    "future-global-hr-ai",
    "getting-started-with-ai-automation",
    "how-ai-transforms-small-business-operations-2026",
    "japan-ai-economy-yen-global-capital-2026",
    "open-source-vs-proprietary-ai-market-shift-2026",
    "state-of-ai-2026-stanford-index",
    "tech-ai-hegemony-and-decentralization",
    "us-china-ai-race-2026",
    "us-government-vs-anthropic-ai-control-2026",
]

# FAQ section heading patterns by language
FAQ_HEADING_EN = "## Frequently Asked Questions"
FAQ_HEADING_JA = "## よくある質問"
FAQ_HEADING_ZH = "## 常见问题"

LANGS = {
    "index.md": FAQ_HEADING_EN,
    "index.ja.md": FAQ_HEADING_JA,
    "index.zh.md": FAQ_HEADING_ZH,
}

# Some files have alternative FAQ headings
ALT_FAQ = {
    "do-you-still-need-experts-in-ai-era": {
        "index.md": "## FAQ",
    }
}

def extract_qa_pairs(lines, faq_start_idx):
    """Extract Q&A pairs from H3 headings and their answer text."""
    qa_pairs = []
    i = faq_start_idx
    while i < len(lines):
        line = lines[i]
        if line.startswith("### "):
            question = line[4:].strip()
            answer_lines = []
            i += 1
            # Collect answer text (paragraphs after the H3 until next H3 or end)
            while i < len(lines):
                next_line = lines[i]
                if next_line.startswith("### ") or (next_line.startswith("## ") and not next_line.startswith("### ")):
                    break
                stripped = next_line.strip()
                if stripped:
                    answer_lines.append(stripped)
                elif answer_lines and stripped == "":
                    answer_lines.append("")
                i += 1
            # Clean up answer text
            answer = " ".join([p for p in answer_lines if p]).strip()
            # Remove trailing empty lines
            if answer:
                qa_pairs.append({"q": question, "a": answer})
        else:
            i += 1
    return qa_pairs


def process_file(filepath, faq_heading):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.split("\n")

    # Find the FAQ section
    faq_idx = None
    for i, line in enumerate(lines):
        if line.strip() == faq_heading:
            faq_idx = i
            break

    if faq_idx is None:
        print(f"  WARNING: FAQ heading not found in {filepath}")
        return False

    # Find the bare {{< faq-schema >}} line
    schema_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "{{< faq-schema >}}":
            schema_idx = i
            break

    if schema_idx is None:
        print(f"  WARNING: {{< faq-schema >}} not found in {filepath}")
        return False

    # Extract Q&A pairs
    qa_pairs = extract_qa_pairs(lines, faq_idx + 1)

    if not qa_pairs:
        print(f"  WARNING: No Q&A pairs found in {filepath}")
        return False

    # Build the replacement JSON
    json_str = json.dumps(qa_pairs, ensure_ascii=False, indent=2)

    replacement = "{{< faq-schema >}}\n" + json_str + "\n{{< /faq-schema >}}"

    # Replace the bare shortcode
    lines[schema_idx] = replacement

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"  DONE: Replaced {len(qa_pairs)} Q&A pairs")
    return True


def main():
    for article in ARTICLES:
        article_dir = os.path.join(BASE, article)
        for filename, faq_heading in LANGS.items():
            filepath = os.path.join(article_dir, filename)
            if not os.path.exists(filepath):
                print(f"  SKIP: {filepath} does not exist")
                continue
            print(f"Processing: {article}/{filename}")
            process_file(filepath, faq_heading)

if __name__ == "__main__":
    main()
