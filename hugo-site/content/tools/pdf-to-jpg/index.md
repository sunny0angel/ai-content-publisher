---
title: "PDF to JPG Converter"
date: 2026-11-20
lastmod: 2026-11-21
description: "Render PDF pages as JPG images at 96, 150, or 300 DPI — preview and download each page. Free, local, no upload."
tags: [PDF to JPG, PDF to image, convert PDF to JPEG, PDF page image, PDF to PNG]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-to-jpg"
faq:
  - q: "What resolution are the exported images?"
    a: "You choose the scale from 1x to 4x. 2x is usually enough for screen use; 3x or 4x is better for printing or OCR."
  - q: "Why is text sometimes missing in Japanese or Chinese PDFs?"
    a: "CJK fonts need embedded data or CMap mapping. This tool loads the standard CMap files locally; a subset font without a mapping can render as blank characters."
  - q: "Can I convert only one page?"
    a: "Yes. Enter a single page or a range instead of exporting the whole document."
  - q: "Are my files uploaded for rendering?"
    a: "No. PDF.js renders each page on a canvas in this tab; images are created locally and downloaded as a ZIP."
related: [pdf-compress, images-to-pdf, pdf-crop, pdf-info]
---

Turn PDF pages into JPG images at 96, 150, or 300 DPI — preview every page and download individually or all at once. Rendering happens in your browser.

<!--more-->

{{< pdf-to-jpg >}}

## How it works

PDF.js draws each page to a canvas, which is encoded as JPEG at your chosen quality. Text becomes pixels, so this is for previews, slide decks, and scanned documents — not for editing. If the PDF is mostly text, keep it as a PDF and compress it with the [PDF compressor](/tools/pdf-compress/) instead.

## Good to know

- 150 DPI is the sweet spot for screen sharing and documents
- 300 DPI for print, but expect large files and slower rendering
- Password-protected PDFs must be unlocked first
