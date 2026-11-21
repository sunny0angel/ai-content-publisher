---
title: "JSON Diff Checker"
date: 2026-11-20
lastmod: 2026-11-21
description: "Compare two JSON documents and see added, removed, and changed fields highlighted path by path. Free local tool — your data never leaves the page."
tags: [JSON diff, compare JSON, JSON compare tool, JSON difference, json diff checker, developer tools]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "json-diff"
faq:
  - q: "Are both JSON documents uploaded?"
    a: "No. Both are parsed and compared inside this tab; neither document is transmitted."
  - q: "Does key order matter?"
    a: "No. Objects are compared by key, so reordering keys alone produces no differences. Array order does matter."
  - q: "Can it compare two versions of an API response?"
    a: "Yes, that is the main use case. Paste the old response on one side and the new one on the other to see added, removed and changed paths."
related: [json-formatter, text-diff, comparison-table-generator, json-to-csv]
---

Paste two JSON documents — an API response before and after a deploy, a config change, two environments — and see exactly which fields were added, removed, or changed, with full paths. Runs entirely in your browser.

<!--more-->

{{< json-diff >}}

## How it works

The tool parses both documents and walks them recursively, comparing objects key by key and arrays element by element. Changed values show the full `path: old → new` transition; new and removed fields are marked green and red. For text documents instead of JSON, the [text diff checker](/tools/text-diff/) is the right tool; for schema-level comparison, validate both sides with the [JSON formatter](/tools/json-formatter/) first.
