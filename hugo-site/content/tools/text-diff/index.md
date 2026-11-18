---
title: "Text Diff Checker"
date: 2026-11-18
lastmod: 2026-11-18
description: "Compare two texts line by line and see additions, deletions, and unchanged lines color-coded. Free local diff tool for configs, logs, and API responses."
tags: [text diff, diff checker, compare text, file diff, line diff, diff tool, developer tools]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "text-diff"
---

Paste two versions of any text — configs, logs, API responses, code — and see exactly what changed: green for added lines, red for removed lines. Computed entirely in your browser with a line-level diff; nothing is uploaded.

<!--more-->

{{< text-diff >}}

## How it works

The tool splits both inputs into lines and runs a longest-common-subsequence (LCS) diff — the same algorithm family behind `git diff`. Every line is classified as added, removed, or unchanged, then rendered with colors.

## Where it saves you

- **Config debugging**: compare the working config against the broken one
- **API responses**: diff two responses to spot what a new version changed — pair with the [JSON formatter](/tools/json-formatter/) to normalize whitespace first
- **Logs**: compare two runs of the same job to find the new error

For best results, keep inputs under a few hundred lines — the LCS algorithm is quadratic, and very large inputs will slow down.
