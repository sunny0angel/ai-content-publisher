---
title: "PDF Metadata Editor"
date: 2026-11-20
lastmod: 2026-11-21
description: "View and edit PDF title, author, subject, keywords, and creator — then download. Local, free, no upload."
tags: [PDF metadata editor, edit PDF properties, PDF author, PDF title, remove PDF metadata]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-metadata"
faq:
  - q: "Can I remove author and software information?"
    a: "Yes. Clear a field to remove it, which strips names, office suite versions and creation tools that often leak more than intended."
  - q: "Does editing metadata change the content?"
    a: "No. Only document properties are rewritten; pages, images and text are untouched."
  - q: "Why does some metadata come back after saving?"
    a: "Some producers rewrite their own fields on export. Save with this tool last, or re-check the file before publishing."
related: [pdf-info, pdf-flatten, pdf-compress, pdf-sign]
---

See what a PDF says about itself — title, author, subject, keywords, creator — and rewrite those fields before you share it.

<!--more-->

{{< pdf-metadata >}}

## How it works

pdf-lib reads the document info dictionary on load and writes your edits on save. Metadata is not encrypted and travels with the file, so it is worth checking before publishing: an internal project name or a personal author field is easy to leak. The [PDF inspector](/tools/pdf-info/) shows everything at once.

## Good to know

- Replace a personal author name with a team or brand name
- Keywords help some document managers; they are not SEO tags
- Editing metadata does not remove hidden content or annotations
