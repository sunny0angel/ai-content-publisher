---
title: "Resize PDF Pages (A4, Letter, A3)"
date: 2026-11-20
lastmod: 2026-11-20
description: "Change every PDF page to A4, Letter, A3, or Legal without re-rendering. Local and free — no upload."
tags: [resize PDF, PDF page size, PDF A4, PDF Letter, change PDF size]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-resize"
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
