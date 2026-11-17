---
title: "How to Convert JSON to CSV: A Practical Guide (and When Not To)"
date: 2026-11-17
lastmod: 2026-11-17
description: "Convert JSON arrays to CSV correctly: header detection, RFC 4180 escaping, UTF-8 BOM for Excel, flattening nested data, and the cases where CSV is the wrong tool."
tags: [JSON to CSV, JSON to CSV converter, convert JSON to Excel, JSON to spreadsheet, CSV export, UTF-8 BOM Excel, nested JSON flatten]
categories: ["AI Tools"]
images:
  featured_image: "/images/json-to-csv-guide.jpg"
draft: false
authors: ["AI Forward"]
slug: "json-to-csv-guide"
---

> **Featured image:** Making notes and calculations based on charts at a desk. Photo by [Jakub Zerdzicki](https://www.pexels.com/photo/making-notes-and-calculations-based-on-charts-20251480/) on Pexels (Free to use).

APIs speak JSON. Humans review data in spreadsheets. Between the two sits one of the most common data chores in software: converting a JSON array into a CSV file — and like every chore that looks trivial, it has sharp edges. The encoding that mangles every non-English character in Excel, the nested object that silently collapses into `[object Object]`, the value with a comma in it that shifts every column to the right. This guide covers the conversion done correctly, and the cases where CSV was the wrong destination in the first place.

For the actual conversion, the free [JSON to CSV Converter](/tools/json-to-csv/) on this site handles header detection, escaping, and Excel-friendly UTF-8 output entirely in your browser.

## What CSV Actually Is

CSV (comma-separated values) is a text table format standardized in [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180): rows separated by line breaks, fields separated by commas, and three rules for values that contain special characters:

1. Values containing a comma, quote, or line break are **wrapped in double quotes**.
2. Quotes inside a quoted value are **doubled**: `"` becomes `""`.
3. A header row is optional but conventional.

The format is deceptively underspecified in the wild: some tools use semicolons (European locale default in Excel), some use tabs, some quote everything. The RFC-4180 version is the lingua franca — produce it, and every spreadsheet tool will parse it.

## The Conversion Rules That Matter

Converting a JSON array of objects to CSV is a three-step job, and each step has a trap:

**1. Detect headers.** The header row is the union of keys across all objects. The trap: objects with inconsistent shapes. `{"name":"A"}` and `{"name":"B","age":30}` in the same array means the header is `name,age` and the first row has an empty `age` cell. Fine — but a key that appears only in the *last* of 10,000 objects will reorder or surprise you if your converter only samples the first row. A correct converter unions all keys.

**2. Escape values.** Numbers and booleans pass through as text. Strings containing commas, quotes, or newlines get quoted per RFC 4180. The trap: `null` and `undefined`. The convention is to render them as empty cells, but some converters print the literal string `"null"` — a data-corruption bug that survives silently.

**3. Handle encoding.** This is where the pain lives. Excel expects a **UTF-8 BOM** (`\uFEFF` at the start of the file) to recognize UTF-8; without it, Excel opens non-ASCII text as the system codepage and Japanese, Chinese, or accented characters become mojibake. The fix is mechanical — prepend the BOM — but only if you know to do it. Our [converter](/tools/json-to-csv/) adds it automatically.

## Nested Data: Flatten First

CSV is a two-dimensional format; JSON is a tree. When an object value is itself an object or array, it must be flattened or stringified:

```
{"user": "ada", "address": {"city": "Tokyo", "zip": "100-0001"}}
```

Options, in order of preference:

1. **Flatten with dot notation** — `address.city`, `address.zip` become their own columns. Best when the nesting shape is consistent.
2. **Stringify into one cell** — `{"city":"Tokyo",...}` as literal JSON text. Best when the nested data is rarely queried in the spreadsheet.
3. **Drop it** — when the nested part is irrelevant to the analysis.

Stringifying a nested object with a naive `String(value)` produces `[object Object]` — the signature of a converter that forgot this step. If you see `[object Object]` in your CSV, the JSON was never properly handled.

## When CSV Is the Wrong Destination

CSV's simplicity is a feature until the data outgrows it. Choose something else when:

- **Deep or irregular nesting.** Three levels of nesting flattened into 40 columns of dot-notation headers is worse than the JSON it came from. Use a document store or Parquet.
- **Millions of rows.** Spreadsheets choke well below a million rows; CSV files have no schema, no types, and no compression. Parquet or a database is the destination for scale.
- **Precision matters.** Numbers round-trip through CSV as text and get re-parsed by whatever opens them — a 64-bit integer ID can silently lose precision in Excel (the same 2⁵³ problem described in our [JSON guide](/blog/json-formatter-guide/)).
- **Streaming or incremental updates.** CSV is a whole-file format; appending rows safely requires rewriting logic that a database gives you for free.

## The Workflows That Benefit Most

**API exports.** Every REST API returns JSON arrays; every business user wants a spreadsheet. A small conversion step replaces "please build me an export feature" tickets.

**LLM batch output.** Structured-output and batch-job responses arrive as JSON arrays. Converting to CSV puts them in a reviewable table — and the token cost of that output is measurable with the [token cost calculator](/tools/ai-token-cost-calculator/).

**Log analysis.** JSON Lines logs are one JSON object per line — a format one small step from an array. Parsing, converting, and pivoting in a spreadsheet is a legitimate quick analysis path for small volumes.

## The Full Pipeline

1. **Validate** the JSON with the [JSON formatter](/tools/json-formatter/) — a conversion tool that chokes on invalid input wastes your time in a confusing way.
2. **Convert** with the [JSON to CSV converter](/tools/json-to-csv/) — headers unioned, values escaped, UTF-8 BOM added.
3. **Open in Excel/Sheets** and confirm the non-ASCII text survived — the BOM check is the whole encoding battle.
4. **Archive the CSV** or push it onward; if the data needs to travel inside another payload, the [Base64 encoder](/tools/base64-encoder/) handles the wrapping.

## Nested JSON to CSV: A Worked Example

Real API responses are rarely flat. Take a users endpoint:

```json
[
  {"id": 1, "name": "Ada", "profile": {"city": "Tokyo", "plan": "pro"},
   "roles": ["admin", "editor"]},
  {"id": 2, "name": "Alan", "profile": {"city": "London", "plan": "basic"},
   "roles": ["viewer"]}
]
```

Applying the flattening rules produces:

| id | name | profile.city | profile.plan | roles |
|----|------|--------------|--------------|-------|
| 1 | Ada | Tokyo | pro | `["admin","editor"]` |
| 2 | Alan | London | basic | `["viewer"]` |

The decisions illustrated:

- **`profile`** is flattened with dot notation — it is an object with a consistent shape, so `profile.city` and `profile.plan` earn their own columns.
- **`roles`** is stringified — an array with varying length has no stable column shape, so it becomes a JSON string in one cell, still parseable by anyone who needs it.
- **`id`** passes through as text — and if those IDs were 64-bit integers beyond 2⁵³, this is exactly where the precision trap would bite; the safe move is to keep IDs as strings end-to-end.

A converter that does the flattening for you needs two decisions spelled out: the **nesting strategy** (dot-notation vs stringify vs drop) and the **encoding** (BOM or not). The [JSON to CSV converter](/tools/json-to-csv/) on this site chooses stringify for nested values and BOM always on — pragmatic defaults that work for the majority of API exports.

## CSV and AI: Batch Outputs, Logs, and LLM Data Pipelines

The JSON→CSV conversion is unusually common in AI-adjacent work, in three specific places:

**Structured output review.** When an LLM returns a JSON array via structured-output mode — say, 500 extracted entities — the fastest human-review loop is: validate with the [JSON formatter](/tools/json-formatter/), convert to CSV, open in a spreadsheet, spot-check rows. A spreadsheet review catches pattern errors (one row missing a field, one category label misspelled) that eyeballing JSON never would.

**Batch job inspection.** OpenAI-style batch jobs return `.jsonl` files — one JSON object per line. Strip to an array or parse line by line, convert, and the whole job becomes auditable as a table. Token usage per row is right there in the payload; the [token cost calculator](/tools/ai-token-cost-calculator/) turns those counts into money.

**Dataset preparation.** The reverse direction matters too: tabular training data often starts life in spreadsheets, becomes CSV, and is parsed into JSON for fine-tuning or RAG pipelines. Knowing the escaping rules in both directions prevents the classic "row 14,207 has an unescaped quote and the whole import shifted" incident.

The common thread: CSV is the review format, JSON is the transport format, and a reliable converter is what makes moving between them boring — which is the best possible property a data pipeline step can have.

## Frequently Asked Questions

{{< faq-schema >}}
[
  {"q": "How do I convert a JSON array to CSV?", "a": "Union the keys of all objects into a header row, escape values containing commas, quotes, or newlines per RFC 4180, and write one row per object. Browser tools such as the AI Forward converter do all three, plus add a UTF-8 BOM for Excel."},
  {"q": "Why do Japanese or Chinese characters turn into garbage in Excel?", "a": "Excel needs a UTF-8 BOM at the start of the file to detect UTF-8. Without it, it decodes bytes with the system codepage and non-ASCII text becomes mojibake. The fix is to prepend the BOM when generating the CSV."},
  {"q": "What does [object Object] in a CSV cell mean?", "a": "A nested JSON object or array was stringified with JavaScript's default String() instead of JSON.stringify or flattening. Flatten nested keys into dot-notation columns, or stringify them as literal JSON before writing."},
  {"q": "How are commas inside values handled in CSV?", "a": "Per RFC 4180, values containing commas, double quotes, or line breaks are wrapped in double quotes, and any quote inside the value is doubled (\" becomes \"\"). Correct converters do this automatically."},
  {"q": "Can CSV handle nested JSON?", "a": "Not natively. CSV is two-dimensional. Flatten nested objects into separate columns with dot notation, stringify them into a single cell as JSON text, or drop them when irrelevant."},
  {"q": "When should I not use CSV?", "a": "For deeply nested data, for millions of rows, when numeric precision matters (64-bit IDs), or when data streams incrementally. Use a document store or Parquet for those cases."},
  {"q": "Is CSV always comma-separated?", "a": "Not in practice. Some locales default to semicolons and some tools use tabs, but RFC 4180 comma-separated CSV is the common interchange format every spreadsheet tool parses."}
]
{{< /faq-schema >}}

---

*CSV rules per RFC 4180. Excel UTF-8 BOM behavior reflects documented Microsoft Excel file-format behavior. JSON stringify/precision behavior per the ECMAScript specification.*
