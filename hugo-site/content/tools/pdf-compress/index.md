---
title: "Compress PDF in Your Browser"
date: 2026-11-20
lastmod: 2026-11-21
description: "Shrink PDFs by re-rendering pages at 72–150 DPI with adjustable JPEG quality. Local, no upload, no file limits."
tags: [compress PDF, reduce PDF size, PDF compressor, shrink PDF, PDF file size]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-compress"
faq:
  - q: "How much smaller will the file get?"
    a: "It depends on the source. Scanned image-only PDFs often shrink 50–80%; text-only PDFs may barely change because there is little raster data to drop."
  - q: "Why does the text become unselectable?"
    a: "Compression re-renders pages as images at the chosen quality. That is what removes the weight, but it also removes the text layer."
  - q: "Can I keep searchable text and still compress?"
    a: "Not with this tool. For searchable output, use an optimiser that downsamples images without rasterising text, or keep the original alongside the compressed copy."
  - q: "What quality setting should I choose?"
    a: "150 DPI is fine for screen reading, 200–300 DPI for printing. Lower values shrink more but blur small print."
related: [pdf-to-jpg, pdf-resize, pdf-merge, pdf-crop]
---

Reduce a PDF's file size by re-rendering its pages as JPEG images at a resolution and quality you control — then compare the before and after size.

<!--more-->

{{< pdf-compress >}}

## How it works

PDF.js renders each page to a canvas; the JPEG is embedded into a new PDF at the original page dimensions with pdf-lib. This is ideal for scans and image-heavy decks. Because text is rasterized, it stops being selectable or searchable — check the result before replacing the original. For pure vector size reduction, try [N-up](/tools/pdf-n-up/) or remove pages with [delete pages](/tools/pdf-delete-pages/).

## Good to know

- 110 DPI at 65% quality usually cuts scans by 50–80%
- 72 DPI for email previews; 150 DPI when text must stay readable
- If the rebuilt file is larger, the original was already efficiently encoded
