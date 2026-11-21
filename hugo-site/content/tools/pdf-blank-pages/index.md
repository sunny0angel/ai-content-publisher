---
title: "Blank PDF Generator"
date: 2026-11-20
lastmod: 2026-11-21
description: "Create a PDF with 1 to 100 blank A4 or Letter pages — for separators, note space, and print tests. Free and local."
tags: [blank PDF, create empty PDF, blank pages PDF, PDF generator, separator pages]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-blank-pages"
faq:
  - q: "Why insert blank pages?"
    a: "Separate chapters for double-sided printing, leave room for notes, or align a scanned insert with a printed page count."
  - q: "Can I match the page size of the document?"
    a: "Yes. Blank pages inherit the size of the surrounding pages so printouts stay aligned."
  - q: "Do blank pages count in the page numbering?"
    a: "Yes. They are real pages, so later numbering shifts by the number inserted."
related: [pdf-duplicate-pages, pdf-merge, pdf-page-numbers, pdf-n-up]
---

Generate a clean PDF of blank pages — one page or a hundred — in A4 or Letter. Useful as section separators, note space, and printer alignment tests.

<!--more-->

{{< pdf-blank-pages >}}

## How it works

The document is built from scratch with pdf-lib, with no hidden content, fonts, or metadata beyond the basics. Combine it with your real document using [merge PDF](/tools/pdf-merge/), or use [N-up](/tools/pdf-n-up/) when you need fewer sheets.

## Good to know

- Check printer margins by printing one page at 100% scale
- A4 is 595×842 pt; Letter is 612×792 pt
- Blank pages are a common scan artifact — remove them with [delete pages](/tools/pdf-delete-pages/)
