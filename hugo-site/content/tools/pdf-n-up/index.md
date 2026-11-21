---
title: "PDF N-up: 2 or 4 Pages per Sheet"
date: 2026-11-20
lastmod: 2026-11-21
description: "Print two or four PDF pages on one landscape sheet to save paper. Built locally in your browser — no upload."
tags: [PDF N-up, pages per sheet, PDF 2-up, print multiple pages, save paper]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-n-up"
faq:
  - q: "What does N-up mean?"
    a: "It places 2, 4, 6 or 9 source pages on one sheet. 2-up suits reading spreads, 4-up suits handouts and 9-up suits thumbnail overviews."
  - q: "Will the text still be readable?"
    a: "At 2-up, A4 body text usually stays readable. At 4-up and above, small print becomes hard to read, so check the preview before printing."
  - q: "Does N-up change the original file?"
    a: "No. A new PDF is generated and the source stays untouched."
related: [pdf-resize, pdf-page-numbers, pdf-crop, pdf-compress]
---

Turn a long PDF into half or a quarter of the sheets: two or four pages are placed on each landscape page, in reading order.

<!--more-->

{{< pdf-n-up >}}

## How it works

Each source page is embedded as a vector form on a new A4 landscape sheet, scaled to fit a 2×1 or 2×2 grid. Because pages are embedded rather than rasterized, text stays sharp. The [PDF resizer](/tools/pdf-resize/) handles page dimensions instead.

## Good to know

- 2-up is readable for slides; 4-up suits handouts and cheat sheets
- A4 landscape is 842×595 pt
- Print double-sided and you cut paper use by four
