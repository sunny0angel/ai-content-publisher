---
title: "PDF Inspector: Pages, Size, Metadata"
date: 2026-11-20
lastmod: 2026-11-20
description: "Inspect any PDF locally — page count, page dimensions, file size, and metadata. No upload, works offline."
tags: [PDF inspector, PDF page count, PDF information, PDF size checker, PDF metadata viewer]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-info"
---

Check what is inside a PDF before you send, print, or archive it: page count, page dimensions, file size, and metadata, all read locally.

<!--more-->

{{< pdf-info >}}

## How it works

The file is parsed in the tab with pdf-lib; only the structure is read, never the rendered content. Common page sizes (595×842 for A4, 612×792 for Letter) are shown in points. Encrypted PDFs are reported clearly instead of failing silently. Related: [metadata editor](/tools/pdf-metadata/) and [compressor](/tools/pdf-compress/).

## Good to know

- A4 = 595×842 pt, Letter = 612×792 pt, A3 = 842×1191 pt
- Mixed page sizes usually mean a merged document
- If the file is encrypted, remove the password in your reader first
