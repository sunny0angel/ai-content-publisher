---
title: "UUID Generator"
date: 2026-11-17
lastmod: 2026-11-17
description: "Generate RFC 9562 version 4 UUIDs in bulk, in lowercase or uppercase. Free browser tool using crypto.getRandomValues — no server round-trip, no tracking."
tags: [UUID generator, GUID generator, UUID v4, RFC 9562, random ID, UUID online tool, UUID uppercase]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "uuid-generator"
---

Generate up to 100 version 4 UUIDs at once, in lowercase or uppercase. IDs are created locally with the Web Crypto API (`crypto.getRandomValues` / `crypto.randomUUID`), so no request ever leaves your browser and no two runs can collide in practice.

{{< uuid-generator >}}

## What is a UUID?

A Universally Unique Identifier is a 128-bit value rendered as 36 characters: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`. Version 4 UUIDs are generated from 122 random bits, giving 2¹²² possible values — the collision probability is negligible even at billions of IDs per second. The format is standardized in [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562), which in 2024 also added the time-ordered versions 6 and 7.

## v4 vs v7: which should you use?

- **v4 (this tool)**: fully random. Simple, uniform, and the safe default for most applications.
- **v7**: time-ordered by construction, so primary-key insert performance in databases like PostgreSQL improves dramatically — sequential keys mean less index fragmentation. Preferred for new database tables in 2026.

If your UUIDs end up as database primary keys, consider generating v7 server-side instead. For API tokens, session IDs, and identifiers that should not leak ordering information, v4 remains the better choice — randomness hides creation order.

## Practical usage

- **Database keys**: `INSERT INTO users (id, name) VALUES ('<uuid>', 'Ada');`
- **API idempotency keys** and request correlation IDs
- **Filenames** for uploaded assets that must never collide
- **Test data**: generate a batch, then feed it into a JSON payload — pair this tool with the [JSON formatter](/tools/json-formatter/).

For the deeper version comparison and database performance implications, see [What Is a UUID? Versions, Use Cases, and Best Practices](/blog/what-is-a-uuid/).
