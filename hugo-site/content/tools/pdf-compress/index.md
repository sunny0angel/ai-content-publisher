---
title: "Compress PDF in Your Browser"
date: 2026-11-20
lastmod: 2026-11-20
description: "Shrink PDFs by re-rendering pages at 72–150 DPI with adjustable JPEG quality. Local, no upload, no file limits."
tags: [compress PDF, reduce PDF size, PDF compressor, shrink PDF, PDF file size]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-compress"
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
