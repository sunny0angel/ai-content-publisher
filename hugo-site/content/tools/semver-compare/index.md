---
title: "Semver Compare & Sort"
date: 2026-11-20
lastmod: 2026-11-21
description: "Compare two semantic versions (1.2.3 vs 1.2.4-rc.1) and sort a list of versions in order. Free local tool for dependency management."
tags: [semver compare, version compare, semantic versioning, semver sort, version checker, developer tools]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "semver-compare"
faq:
  - q: "Does it follow SemVer 2.0.0?"
    a: "Yes, including prerelease precedence: 1.0.0-alpha < 1.0.0-beta < 1.0.0."
  - q: "How is build metadata handled?"
    a: "Metadata after the plus sign is ignored for precedence, as the specification requires."
  - q: "Can I sort a long list?"
    a: "Paste one version per line and sort ascending; invalid lines are reported instead of being silently skipped."
related: [text-diff, json-diff, regex-tester, comparison-table-generator]
---

Compare two semantic versions — including prerelease tags like `-rc.1` — and sort a whole list of versions in ascending order. The rules follow the [SemVer 2.0.0 specification](https://semver.org/). Runs entirely in your browser.

<!--more-->

{{< semver-compare >}}

## How it works

Versions are compared field by field (major, minor, patch), then by prerelease identifiers with the spec's numeric-before-alphanumeric rule. It is the same logic your package manager uses — paste dependency versions here when a resolver surprises you. For dependency JSON, the [JSON diff checker](/tools/json-diff/) compares lockfiles.
