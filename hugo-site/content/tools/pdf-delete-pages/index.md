---
title: "Delete Pages from PDF"
date: 2026-11-20
lastmod: 2026-11-21
description: "Remove unwanted pages from a PDF and download the cleaned file — locally in your browser. Keep the rest of the document intact."
tags: [delete PDF pages, remove pages from PDF, PDF page remover, clean PDF]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-delete-pages"
faq:
  - q: "Is my original PDF modified?"
    a: "No. A new file is written without the selected pages; the original stays untouched on your disk."
  - q: "Can I delete pages from a protected PDF?"
    a: "Only after unlocking it in a reader and saving a copy without the password. Encrypted files cannot be parsed."
  - q: "Why did the remaining page numbers change?"
    a: "Pages are physically removed, so numbers printed into the page content move up. Add fresh numbering with the page number tool if you need stable references."
related: [pdf-merge, pdf-split, pdf-reorder, pdf-rotate]
---

Cut blank scans, outdated clauses, or accidentally inserted pages out of a PDF. Specify what to remove, keep everything else, and download the cleaned document.

<!--more-->

{{< pdf-delete-pages >}}

## How it works

The tool copies every page except the ones you list into a new PDF, preserving page content and order. Nothing is redacted or re-encoded. To keep only certain pages instead, the [PDF splitter](/tools/pdf-split/) does the inverse.

## Good to know

- Use ranges for blocks: 2, 4-6 removes page 2 and pages 4 through 6
- Always keep a copy of the original before destructive edits
- If the file is a scan, compress it afterward with the [PDF compressor](/tools/pdf-compress/)
