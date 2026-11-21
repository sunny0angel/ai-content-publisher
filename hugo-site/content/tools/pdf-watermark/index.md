---
title: "Add Watermark to PDF"
date: 2026-11-20
lastmod: 2026-11-21
description: "Stamp a diagonal text watermark on every PDF page — custom text, size, opacity, and angle. Runs locally, nothing uploads."
tags: [PDF watermark, add watermark to PDF, confidential stamp, PDF draft watermark]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-watermark"
faq:
  - q: "Is the watermark added to the original file?"
    a: "No. A new PDF is written and the source stays unchanged."
  - q: "Can I use a logo instead of text?"
    a: "Yes. Upload a PNG or JPG and set opacity, scale and rotation. Transparent PNG logos work best."
  - q: "Can I watermark only some pages?"
    a: "Yes. Choose all pages or a range, which is useful for stamping DRAFT on the first page only."
  - q: "Does the watermark survive editing?"
    a: "It is drawn into the page content, so casual editing will not remove it. It is a visible mark, not DRM."
related: [pdf-page-numbers, pdf-sign, pdf-flatten, pdf-compress]
---

Mark drafts, confidential documents, and internal copies with a diagonal text watermark — custom wording, size, opacity, and angle, applied to every page.

<!--more-->

{{< pdf-watermark >}}

## How it works

The watermark is drawn as vector text over each page with adjustable opacity, so the underlying content stays selectable. It is a visual mark, not encryption: anyone can remove it with a PDF editor. For access control, use your PDF tool's password protection instead.

## Good to know

- “CONFIDENTIAL” at 15–20% opacity is readable without hiding content
- Rotate 45° for the classic diagonal look, or 0° for a footer-like band
- Watermark before sharing, not after — recipients can strip it
