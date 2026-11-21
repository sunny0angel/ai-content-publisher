---
title: "Resize PDF Pages (A4, Letter, A3)"
date: 2026-11-20
lastmod: 2026-11-21
description: "Change every PDF page to A4, Letter, A3, or Legal without re-rendering. Local and free — no upload."
tags: [resize PDF, PDF page size, PDF A4, PDF Letter, change PDF size]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-resize"
faq:
  - q: "What is the difference between resize and N-up?"
    a: "Resize changes the paper size of each page, for example A4 to Letter. N-up puts several pages on a single sheet."
  - q: "Will resizing distort the content?"
    a: "The tool scales proportionally and keeps the aspect ratio, so pages are not stretched. Expect white margins when the ratios differ."
  - q: "Does scaling up reduce quality?"
    a: "Vector text stays sharp. Raster images cannot gain detail, so a low-resolution scan enlarged to A3 may look soft."
related: [pdf-crop, pdf-n-up, pdf-compress, images-to-pdf]
---

Standardize a mixed-size PDF on A4, Letter, A3, or Legal so it prints and files cleanly. The page canvas changes; the content stays vector.

<!--more-->

{{< pdf-resize >}}

## How it works

Each page's media box is set to the target dimensions with pdf-lib. Content is not scaled or re-encoded, so nothing blurs — but content positioned for a different aspect ratio may sit off-center. To trim margins instead, use [crop PDF](/tools/pdf-crop/).

## Good to know

- A4 is 595×842 pt; Letter is 612×792 pt
- Check the result before printing — content is not auto-scaled
- Mixed page sizes are detected by the [PDF inspector](/tools/pdf-info/)
