---
title: "Add Page Numbers to PDF"
date: 2026-11-20
lastmod: 2026-11-21
description: "Stamp page numbers on every PDF page — position, start number, font size, and “X / Y” format. Free, local, no upload."
tags: [add page numbers to PDF, PDF page numbering, number PDF pages, PDF pagination]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-page-numbers"
faq:
  - q: "Can I start numbering from a page other than 1?"
    a: "Yes. Set the starting number and the first page to stamp, so a cover page stays unnumbered."
  - q: "Where are the numbers placed?"
    a: "Choose a position such as bottom center, bottom right or top right, plus font size and margin. The same style is applied to every selected page."
  - q: "Are the numbers searchable text?"
    a: "Yes. They are written as real text on top of the page, so they can be selected and searched, unlike a scanned stamp."
related: [pdf-watermark, pdf-n-up, pdf-blank-pages, pdf-merge]
---

Add page numbers to a PDF that has none — bottom or top, left, center, or right, with an optional “X / Y” total. No re-rendering, no upload.

<!--more-->

{{< pdf-page-numbers >}}

## How it works

Numbers are drawn as vector text with the standard Helvetica font, offset from each page edge, so they print crisply at any size. Existing content is not re-encoded. Pair it with [watermarking](/tools/pdf-watermark/) when a document needs both.

## Good to know

- Start at 0 if the cover page should not count
- If numbering must skip the cover, delete it first with [delete pages](/tools/pdf-delete-pages/) and merge it back after
- The total count reflects the pages in this file only
