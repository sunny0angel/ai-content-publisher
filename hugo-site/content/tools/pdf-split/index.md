---
title: "Split PDF & Extract Pages"
date: 2026-11-20
lastmod: 2026-11-21
description: "Extract selected pages from a PDF into a new file. Type ranges like 1-3, 5, 7-9 — no upload, no account, no page limit."
tags: [split PDF, extract PDF pages, PDF page extractor, PDF splitter]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-split"
faq:
  - q: "Does splitting a PDF upload it anywhere?"
    a: "No. The file is opened and rewritten in this tab. Nothing is sent to a server, and the split files exist only in your downloads folder."
  - q: "Can I extract just one page or a range?"
    a: "Yes. Use the range mode and enter pages such as 3, 7-9 or 12-. Each range becomes its own PDF, so one run can produce several files."
  - q: "Are links and bookmarks kept in the split files?"
    a: "Page content is kept. Links that point to pages now in another file, and document-level bookmarks, may stop working. Check the output if the PDF is heavily cross-referenced."
  - q: "Does it work on scanned PDFs?"
    a: "Yes. Splitting works at the page level and does not need selectable text. It cannot run OCR, so scanned pages stay images."
related: [pdf-merge, pdf-delete-pages, pdf-reorder, pdf-compress]
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
