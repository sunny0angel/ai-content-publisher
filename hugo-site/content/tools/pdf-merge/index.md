---
title: "Merge PDF Files"
date: 2026-11-20
lastmod: 2026-11-21
description: "Combine multiple PDFs into one file in the order you choose — entirely in your browser. No uploads, no signup, no watermarks."
tags: [PDF merge, merge PDF, combine PDF, join PDF files, PDF merger]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-merge"
faq:
  - q: "Does merging PDFs upload my files to a server?"
    a: "No. Each file is opened and combined in this tab with pdf-lib, which runs inside your browser. Nothing is uploaded, and closing the tab discards the files."
  - q: "Can I merge a password-protected PDF?"
    a: "Not directly. Unlock the file in your PDF reader first (enter the password and save a copy without protection), then merge that copy. Encrypted files cannot be parsed."
  - q: "Will merging reduce quality or add a watermark?"
    a: "No. Pages are copied as-is without recompression and nothing is stamped on the output. Page sizes are not normalized either, so a mix of A4 and Letter pages keeps its original dimensions."
  - q: "Are bookmarks, links and form fields preserved?"
    a: "Page content, images and text are preserved. Document-level bookmarks, some annotations and interactive form fields may not carry over, so check the result before sending it out."
related: [pdf-split, pdf-delete-pages, pdf-reorder, pdf-compress]
---

Combine two or more PDFs into a single document, in exactly the order you select. Contracts, scans, invoices, and exported slides merge in seconds — and the files never leave your browser.

<!--more-->

{{< pdf-merge >}}

## When to use it

- **Contracts and appendices.** Merge a signed agreement with its statement of work, price list and annexes into one file that is easy to archive or send.
- **Monthly paperwork.** Combine bank statements, invoices or receipts into a single PDF per month instead of mailing a folder of loose files.
- **Multi-part scans.** A physical document scanned in several passes (front and back, or page by page from a phone) becomes one continuous file.
- **Slide handouts.** Join exported decks, or put a cover page in front of an existing report.

## How it works

Each PDF is parsed locally with pdf-lib, its pages copied into a new document in selection order, then saved as a fresh file. There is no server in the middle, so even confidential documents stay on your machine.

Two practical limits are worth knowing. Password-protected files must be unlocked in your reader before they can be parsed. And because pages are copied rather than re-rendered, mixed page sizes, orientation and quality are preserved exactly — the merged file will simply contain both A4 and Letter pages if that is what you gave it.

Need the opposite operation? Use the [PDF splitter](/tools/pdf-split/) to cut a file into parts, or the [page deleter](/tools/pdf-delete-pages/) to remove pages you do not need. If the result is too heavy to email, run it through the [PDF compressor](/tools/pdf-compress/).

## Good to know

- Select files in the exact order you want them merged
- The result downloads as merged.pdf — rename it afterward
- For large scanned files, run the result through the [PDF compressor](/tools/pdf-compress/)
- If a file fails, it is usually encrypted or corrupted; try opening it in a reader first
