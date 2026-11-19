---
title: "Date Interval Calculator (with Working Days)"
date: 2026-11-19
lastmod: 2026-11-19
description: "Calculate days, working days, and weeks between two dates. Free local tool for leave, contracts, invoices, and project planning."
tags: [date calculator, days between dates, working days calculator, date difference, business days calculator, day counter]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "date-interval-calculator"
---

Pick two dates and get the total days, working days (Mon–Fri), and weeks between them — the arithmetic behind leave requests, contract terms, invoice due dates, and project timelines. Runs entirely in your browser.

<!--more-->

{{< date-interval-calculator >}}

## How it works

The tool computes the difference in milliseconds and converts to days, then counts working days by walking each day and excluding Saturday and Sunday. Public holidays are country-specific and are **not** included — add them manually when precision matters (e.g., statutory leave).

## Typical uses

- **Leave**: "10 working days from Monday" — when do I return?
- **Contracts and invoices**: net-30 payment terms from the issue date
- **Projects**: how many working days until the deadline?

For timestamps rather than calendar dates, the [Unix timestamp converter](/tools/timestamp-converter/) covers the machine-readable side.
