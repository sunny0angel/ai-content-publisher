---
title: "Rotate PDF Pages"
date: 2026-11-20
lastmod: 2026-11-21
description: "Rotate every page of a PDF by 90°, 180°, or 270° and download the fixed file. Free, local, no upload."
tags: [rotate PDF, PDF rotation, fix PDF orientation, turn PDF pages]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-rotate"
faq:
  - q: "Does rotating re-encode the page?"
    a: "No. It changes the page rotation flag, so text and images are not recompressed and quality is unchanged."
  - q: "Can I rotate only some pages?"
    a: "Yes. Rotate all pages or enter a range such as 1, 4-6 to fix only the landscape scans."
  - q: "Why does the page still look sideways in another viewer?"
    a: "Some viewers ignore the rotation flag. Re-save the file with this tool and check in a second reader; the stored orientation is corrected."
related: [pdf-reorder, pdf-delete-pages, pdf-n-up, pdf-crop]
---

Fix sideways scans and upside-down exports. Rotate all pages by 90°, 180°, or 270° and download a PDF that opens the right way up.

<!--more-->

{{< pdf-rotate >}}

## How it works

Rotation is written into each page's rotation attribute, so the content is not re-rendered or degraded. Most readers and printers honor it immediately. Need to rotate a single page differently? Use [reorder pages](/tools/pdf-reorder/) after splitting it out with [split PDF](/tools/pdf-split/).

## Good to know

- 90° or 270° is right for landscape scans saved as portrait
- 180° fixes upside-down duplex scans
- Rotation is metadata — the file size stays essentially the same
