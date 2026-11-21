---
title: "Case Converter"
date: 2026-11-18
lastmod: 2026-11-21
description: "Convert text between UPPERCASE, lowercase, Title Case, camelCase, snake_case, and kebab-case. Free local tool for naming and formatting."
tags: [case converter, camelCase, snake_case, kebab-case, title case, text case, developer tools]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "case-converter"
faq:
  - q: "Which naming conventions are supported?"
    a: "UPPERCASE, lowercase, Title Case, camelCase, snake_case and kebab-case. Input is split on spaces, underscores and hyphens first."
  - q: "Are acronyms and punctuation preserved?"
    a: "Words are normalized, so an acronym like API becomes api in camelCase and snake_case. In identifier modes, punctuation other than separators is dropped."
  - q: "Is my text uploaded?"
    a: "No. Conversion happens inside this tab and nothing is transmitted."
related: [url-encoder, text-diff, lorem-ipsum-generator, regex-tester]
---

Turn any text into UPPERCASE, lowercase, Title Case, camelCase, snake_case, or kebab-case with one click. Handy for code naming, URL slugs, and API field names. Runs entirely in your browser.

<!--more-->

{{< case-converter >}}

## How it works

The converter splits input on spaces, underscores, and hyphens into words, then re-joins them per convention: `camelCase` lowercases the first word and capitalizes the rest; `snake_case` and `kebab-case` lowercase everything and join with `_` or `-`.

## Naming conventions in practice

| Context | Convention |
|---------|-----------|
| JavaScript/Go variables | camelCase |
| Python variables/files | snake_case |
| CSS classes, URLs | kebab-case |
| API fields | snake_case (REST) or camelCase (GraphQL) |
| Classes | PascalCase (Title Case without spaces) |

When API responses switch conventions on you, converting field names before the [JSON to CSV converter](/tools/json-to-csv/) keeps headers consistent.
