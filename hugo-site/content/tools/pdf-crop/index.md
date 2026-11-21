---
title: "Crop PDF Margins"
date: 2026-11-20
lastmod: 2026-11-21
description: "Trim white margins from PDF pages by percentage — top, right, bottom, left. Local, free, no upload."
tags: [crop PDF, PDF margins, trim PDF, PDF crop tool, remove white space]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-crop"
faq:
  - q: "Does cropping delete the hidden content?"
    a: "It changes the visible area (CropBox). Content outside the crop is hidden, not deleted, so the file size barely changes."
  - q: "Can I crop each page differently?"
    a: "Yes. Apply one crop box to all pages, or use per-page values when scan margins differ."
  - q: "Why is the file size the same after cropping?"
    a: "Because the hidden content is still stored. To actually shrink the file, run it through the PDF compressor."
related: [pdf-resize, pdf-rotate, pdf-n-up, pdf-compress]
---

Trim wasted white space around PDF pages — set a percentage for each edge and download a document that fits its content better.

<!--more-->

{{< pdf-crop >}}

## How it works

Cropping sets each page's crop box: the content outside the box is hidden by viewers and excluded from printing, but it is not deleted from the file. That keeps the operation reversible and non-destructive. To change the actual paper size, use [resize PDF](/tools/pdf-resize/).

## Good to know

- Start with 5% per side for scans with oversized margins
- Crop only changes the visible area — recover it by setting 0% again
- Some print dialogs ignore crop boxes; test one page first
