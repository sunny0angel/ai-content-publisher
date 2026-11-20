---
title: "Split PDF & Extract Pages"
date: 2026-11-20
lastmod: 2026-11-20
description: "Extract selected pages from a PDF into a new file. Type ranges like 1-3, 5, 7-9 — no upload, no account, no page limit."
tags: [split PDF, extract PDF pages, PDF page extractor, PDF splitter]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-split"
---

Pull out exactly the pages you need — a signature page, an appendix, one chapter — into a clean new PDF. Type a range such as 1-3, 5, 7-9 and download only those pages.

<!--more-->

{{< pdf-split >}}

## How it works

The tool reads the page count, keeps only the indices you list, and copies them into a new document in the order given. The original file is never modified. To remove pages instead, use [delete pages](/tools/pdf-delete-pages/); to combine files, use [merge PDF](/tools/pdf-merge/).

## Good to know

- Page numbers are 1-based, matching what your reader shows
- Ranges can repeat or reorder pages — 3, 1, 1 gives you page 3 then page 1 twice
- Encrypted PDFs need their password removed before splitting
