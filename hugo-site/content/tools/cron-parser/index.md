---
title: "Cron Expression Parser"
date: 2026-11-18
lastmod: 2026-11-18
description: "Decode cron expressions into plain English and see the next run times. Supports *, */n, ranges, and lists. Free local tool for scheduling and debugging."
tags: [cron parser, cron expression, crontab, cron syntax, schedule parser, cron tester, developer tools]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "cron-parser"
---

Paste a cron expression — `*/15 * * * *` — and see it explained field by field plus the next five run times computed from your local clock. Runs entirely in your browser.

<!--more-->

{{< cron-parser >}}

## How it works

The standard 5-field cron format is `minute hour day-of-month month day-of-week`. The tool parses each field — supporting `*` (every), `*/n` (every n), `a-b` (ranges), and `a,b` (lists) — then walks minute by minute from now until it collects five matching times. The day-of-month/day-of-week pair follows the standard OR rule: a schedule matches when **either** field matches.

## Where you will meet it

- **CI pipelines**: GitHub Actions and GitLab schedules use cron syntax
- **Cloud cron**: Cloudflare Cron Triggers, Vercel Cron — same 5-field format
- **Servers**: crontab entries, systemd timers' ancestors

When a job "didn't run", the bug is almost always the expression, not the scheduler. Paste it here and read the next runs before touching the server. Pair with the [timestamp converter](/tools/timestamp-converter/) to double-check timezones — cron runs in the server's zone, which is rarely yours.
