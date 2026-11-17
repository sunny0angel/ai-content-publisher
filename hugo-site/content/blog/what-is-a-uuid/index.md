---
title: "What Is a UUID? Versions, Use Cases, and Best Practices"
date: 2026-11-17
lastmod: 2026-11-17
description: "A practical explainer of UUIDs: how version 4, 7, and others differ, when to use each, and why v7 is winning for database primary keys. Includes a free UUID generator."
tags: [UUID, UUID v4, UUID v7, GUID, RFC 9562, database primary key, unique identifier, UUID generator]
categories: ["AI Tools"]
images:
  featured_image: "/images/what-is-a-uuid.jpg"
draft: false
authors: ["AI Forward"]
slug: "what-is-a-uuid"
---

> **Featured image:** Data center server racks with active equipment. Photo by [Cookiecutter](https://www.pexels.com/@cookiecutter/) on Pexels (Free to use).

Every record in every system needs a name that never collides, never needs a central registry, and never reveals more than it should. The UUID is that name — a 128-bit identifier that any machine can mint independently, at any time, without asking anyone. It is the default primary key of modern distributed systems, and it is the format underneath the IDs you see in databases, logs, API responses, and mobile push notifications.

This guide explains what a UUID actually is, how the versions differ, and the practical rules for choosing between them. To generate UUIDs right now, use the free [UUID Generator](/tools/uuid-generator/) — it runs entirely in your browser.

## What a UUID Is, Structurally

A UUID is 128 bits, conventionally written as 36 characters in five groups: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`. The version is encoded in the 13th hexadecimal digit of the third group — `...-4xxx-...` means version 4, `...-7xxx-...` means version 7. The format was defined in [RFC 4122](https://www.rfc-editor.org/rfc/rfc4122) (2005) and replaced by [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562) (2024), which added versions 6, 7, and 8.

The versions in active use:

| Version | Generation | Sorting | Typical use |
|---------|-----------|---------|-------------|
| 1 | Timestamp + MAC address | Time-ordered | Legacy systems |
| 4 | 122 random bits | Random | Default choice for most apps |
| 7 | Unix timestamp (ms) + randomness | Time-ordered | Database primary keys |

Versions 3 and 5 (name-based, MD5/SHA-1) serve a different purpose: they derive a *deterministic* UUID from a name, so the same input always yields the same ID. Useful for content addressing, but rarely for records that need uniqueness per entity.

## v4: The Random Default

Version 4 sets 122 of its 128 bits randomly. That yields 2¹²² possible values — roughly 5.3 × 10³⁶. The collision math is worth internalizing because it kills a persistent worry: at one billion UUIDs generated per second, you would need about 85 million years to have a 50% chance of one collision. Random UUIDs do not collide in practice; they fail only if the underlying random generator is weak, which is why the [UUID generator tool](/tools/uuid-generator/) uses the Web Crypto API (`crypto.randomUUID` / `crypto.getRandomValues`) rather than `Math.random()`.

v4 is the correct default for:

- **API tokens and session IDs** — randomness hides creation order, so IDs leak no information about when an account or session was created.
- **Client-generated IDs** — mobile apps and browsers that create records offline need IDs that require no server round-trip.
- **Anything public-facing** — a sequential ID in a URL reveals your volume; a v4 UUID reveals nothing.

## v7: The Database-Friendly Upgrade

The weakness of v4 appears inside databases. A random ID becomes a primary key that inserts rows at random positions in the index. For PostgreSQL and InnoDB (MySQL), whose primary-key indexes are B-trees, random insert order fragments the index, increases write amplification, and slows inserts measurably at scale. UUIDv7 fixes this by putting a millisecond Unix timestamp in the high-order bits: IDs generated close in time sort close together, so inserts land at the end of the index — nearly sequential write performance with all the uniqueness properties of a UUID.

The practical guidance in 2026: **for new database primary keys, use v7 on the server**. PostgreSQL generates them natively with `gen_random_uuid()` (which now returns v7 by default on recent versions) or `uuidv7()` from the `uuid-ossp` extension. If your framework does not support v7 yet, use v4 — the performance gap matters at millions of rows, not thousands, and schema correctness is worth more than premature optimization.

## When NOT to Use a UUID

UUIDs are not free. The costs are real, and there are three situations where another identifier wins:

1. **Huge tables under heavy sequential scan.** A UUID is 16 bytes; a `bigint` is 8. On a multi-terabyte table, the index size difference matters for memory and IO.
2. **Identifiers humans must type or say.** Nobody reads a UUID over the phone. Booking codes, order numbers, and error codes should be short and unambiguous.
3. **Sorting by creation time in the application layer.** If your queries depend on ID order rather than a timestamp column, prefer v7 over v4 — or just add a `created_at` column and stop deriving order from IDs.

## UUIDs in the AI/LLM Stack

UUIDs show up everywhere in modern AI infrastructure, in three specific patterns worth knowing:

**Idempotency keys.** Stripe-style APIs accept a client-generated UUID per request so a retried call does not double-charge. LLM platforms use the same pattern: generate a UUID per request, and network retries become safe.

**Run and trace IDs.** Every LangChain/OpenTelemetry-style trace, every agent run, and every batch job gets a UUID. Distributed tracing stitches logs together purely by matching these IDs across services.

**Batch file keys.** OpenAI-compatible batch jobs reference their files and jobs by platform-generated IDs; if you build your own pipeline, mint v4 UUIDs for job IDs so concurrent workers cannot collide.

For all of the above, our [UUID Generator](/tools/uuid-generator/) produces RFC 9562 v4 IDs in bulk — useful when you are seeding test data, writing fixtures, or building a payload that needs a batch of IDs at once. Pair it with the [JSON formatter](/tools/json-formatter/) to assemble those IDs into a well-formed request body.

## The Full Version Family: 1, 3, 5, 6, 8 — and Why Most Are Ignored

Eight versions exist in the spec; four matter in practice. The others are worth knowing so you can recognize them in the wild:

- **v1 (time + MAC)**: the original, generated from a timestamp and the machine's MAC address. Time-ordered, but it leaked the generating machine's network identity — a privacy flaw that motivated later versions. Still visible in old Java and SQL Server systems (`newsequentialid()` is a v1 variant).
- **v3 / v5 (name-based)**: deterministic UUIDs derived from a name within a namespace (DNS, URL, OID, X.500). Same input, same output, forever. Prefer v5 (SHA-1) over v3 (MD5) for any new use. The killer application: content addressing and deduplication, where you *want* identical inputs to map to identical IDs.
- **v6 (reordered v1)**: keeps v1's timestamp semantics but orders the bits for better sortability. Rarely used — v7 supersedes it for all practical purposes.
- **v7 (timestamp + randomness)**: the modern workhorse, covered above. Millisecond precision means IDs sort in creation order, which databases love.
- **v8 (vendor-specific)**: reserved for custom formats, with only the version nibble fixed. Use it when you need to embed your own semantics — shard IDs, region codes — inside a standards-compliant shell.
- **v2 (DCE Security)**: historical, includes local domain and UID; effectively obsolete.

The decision tree collapses to two branches in practice: **v4 for client-side and security-sensitive identifiers, v7 for server-side database keys.** Everything else is a niche.

## UUID Performance: Myths and Measurements

Two claims circulate about UUIDs, one true and one exaggerated:

**The true one: random primary keys fragment indexes.** B-tree indexes keep pages sorted; inserting a random key lands in a random page, splitting pages and growing the index unevenly. The effect is measurable at scale — published benchmarks show UUIDv4 insert throughput degrading well below sequential keys at tens of millions of rows, while UUIDv7 stays within a few percent of `bigserial`. The mechanism is uncontroversial; only the magnitude varies by workload.

**The exaggerated one: UUIDs make queries dramatically slower.** For point lookups by primary key, the difference between a 16-byte UUID and an 8-byte bigint is small. The real costs are in three places: index size (twice the bytes), join performance on very wide tables, and insert throughput under write-heavy load. If your table has a million rows and moderate traffic, v4 is completely fine — correctness and portability matter more than the last few percent of insert speed.

| Key type | Size | Insert performance | Exposes info | Typical use |
|----------|------|--------------------|--------------|-------------|
| bigserial | 8 B | Best | Creation order, volume | Internal tables, small apps |
| UUID v4 | 16 B | Good (fragments at scale) | Nothing | Public IDs, tokens, client-generated |
| UUID v7 | 16 B | Near-sequential | Creation time only | Database primary keys |

## Migrating to UUIDs: A Practical Sequence

If you are designing a new table, the answer is one line: `id uuid primary key default gen_random_uuid()`. If you are migrating an existing `bigserial` table, the answer is usually: **do not migrate it**. Sequential-integer tables that work keep working; the migration risk concentrates in foreign keys and application code that assumes integers. The pragmatic middle path — used by most systems that expose UUIDs in public APIs while keeping integers internally — is an additive migration:

1. **Add a UUID column** (`uuid` type, nullable, no default yet) alongside the existing ID.
2. **Backfill** with `UPDATE ... SET uuid = gen_random_uuid() WHERE uuid IS NULL`, batched to avoid long locks.
3. **Add a unique index** and set the column `NOT NULL`, then a server-side default for new rows.
4. **Expose the UUID in the API** while foreign keys internally keep pointing at the integer ID. External systems see stable, opaque identifiers; internal joins stay fast.
5. **Only if required**, swap foreign keys to the UUID in a later, separately tested migration.

This pattern — integer internally, UUID externally — is the standard answer for systems that grew before the API was designed. It gets the security properties of v4 without the index cost of converting the schema.

## UUIDs in the Wild: URLs, Logs, and Every Language

**URLs.** UUIDs are URL-safe by design — hexadecimal plus hyphens, with no characters that need percent-encoding. They appear in REST paths (`/users/019b2f1a-...`), query parameters, and signed links. The one habit to adopt: use the canonical lowercase form everywhere. Mixed-case UUIDs are technically equal but break naive equality checks and cache keys.

**Logs and tracing.** In distributed systems the UUID's second life is as a *correlation ID*: the same ID is generated at the edge of a request and passed through every service, so a single grep across a dozen log streams reassembles one user's journey. OpenTelemetry formalizes this as the trace ID — 128 bits, the same size as a UUID, and (in the W3C Trace Context standard) a format closely related to v4. If your system has no tracing yet, generating a v4 UUID per request and logging it in every service is 80% of the value at 5% of the cost.

**Every language ships a generator.** None of this requires a library in 2026:

| Language | One-liner |
|----------|-----------|
| JavaScript (browser/Node 20+) | `crypto.randomUUID()` |
| Python | `uuid.uuid4()` / `uuid.uuid7()` (3.14+) |
| Go | `github.com/google/uuid` — `uuid.New()` |
| Java | `java.util.UUID.randomUUID()` |
| SQL (PostgreSQL) | `gen_random_uuid()` |

For v7 specifically: Python 3.14 added `uuid.uuid7()`; recent PostgreSQL returns v7 from `gen_random_uuid()`; Go and Java need the standard third-party libraries. Our [UUID Generator](/tools/uuid-generator/) produces v4 in bulk — the version to reach for when you need identifiers that reveal nothing, fast.

**Deterministic IDs with v5.** One pattern worth stealing from content-addressed systems: instead of storing a random ID for every document, compute `uuid5(NAMESPACE_URL, canonical_url)` — the same URL always yields the same ID, forever, across machines. Deduplication then falls out for free: "have I seen this document" becomes "does this ID exist." Use it for content fingerprints, cache keys, and idempotent imports — anywhere you *want* identical inputs to produce identical IDs.

## UUID Security Considerations

UUIDs are not a security mechanism, but choosing them well is part of one:

**Never derive security from unguessability alone.** A v4 UUID is unguessable in practice — but it is an identifier, not a secret. An API that treats "the client knows the UUID" as authorization is vulnerable to enumeration and leakage through logs, referrer headers, and browser history. Pair opaque IDs with real authorization checks; the UUID only prevents guessing, and guessing is the weakest attack.

**Avoid exposing sequential or derivable IDs publicly.** The classic vulnerability class here is IDOR (Insecure Direct Object Reference): `/invoices/1042` invites incrementing the number. `/invoices/<v4-uuid>` makes enumeration infeasible. This is the strongest practical argument for UUIDs in public APIs, and it is also why v1's MAC-address leak mattered enough to motivate later versions.

**Use cryptographically secure generators.** `Math.random()` is not good enough for identifiers — its output is predictable in practice under some browser implementations. `crypto.randomUUID()` and `crypto.getRandomValues()` are. The same rule applies server-side: use the platform's CSPRNG, never a general-purpose random function.

**Do not sign or encode secrets into UUIDs.** UUIDs have a fixed 122 random bits in v4; packing extra meaning into them (user IDs, timestamps in v4) reduces the randomness that makes them safe. If you need to embed semantics, use v7 (timestamp) or v8 (vendor-defined) deliberately — or keep a separate field.

**When UUIDs must not appear at all**: in places where an ID is itself the proof of possession — password-reset tokens, one-time download links, and API secrets should use larger random values (256-bit tokens) that are not formatted like record identifiers. A UUID tells the world "I am an ID"; a reset token should not.

## UUID vs ULID vs NanoID vs ObjectId

UUID is not the only game in town. Four alternatives appear constantly, and the differences are small enough that choosing wrong is easy:

| Format | Size / alphabet | Sortable? | Collision model | Best for |
|--------|----------------|-----------|-----------------|----------|
| UUID v4 | 128-bit, hex | No | Random | Public IDs, tokens |
| UUID v7 | 128-bit, hex | Yes (ms) | Random + timestamp | DB primary keys |
| ULID | 128-bit, Crockford base32 | Yes (ms) | Random + timestamp | Logs, short sortable IDs |
| NanoID | 126-bit, URL alphabet | No | Random | Short opaque IDs |
| ObjectId | 96-bit, hex | Yes (sec) | Timestamp + counter + random | MongoDB default |

The practical decision rules:

- **ULID** is essentially UUID v7 in a denser, prettier casing (26 characters, case-insensitive, sortable as text). Choose ULID when humans will read IDs in logs or tickets and you want time-order without a separate column.
- **NanoID** wins on compactness and URL-friendliness — its alphabet omits look-alike characters (`0/O/1/l/I`). Choose it for short codes, share links, and anything user-facing where a 36-character UUID feels heavy.
- **ObjectId** is MongoDB's 12-byte format: 4-byte timestamp, 5-byte random, 3-byte counter. If you live in MongoDB, use it and forget the rest of this article; if you are designing for portability across databases, prefer v7.
- **UUID v7** remains the best default for relational databases: standards-track, widely supported in 2026, and interoperable with the ecosystem of UUID tooling.

The honest summary: v4 for opacity, v7 for database keys, ULID for readable logs, NanoID for short links. Four formats, four jobs, and a [generator](/tools/uuid-generator/) for the one you will reach for most often.

## Frequently Asked Questions

{{< faq-schema >}}
[
  {"q": "What is a UUID?", "a": "A Universally Unique Identifier is a 128-bit value written as 36 characters in five groups, standardized in RFC 9562. Version 4 uses 122 random bits; version 7 embeds a millisecond timestamp so IDs sort in creation order."},
  {"q": "Can two UUIDs ever be the same?", "a": "In practice, no. Version 4 has 2¹²² possible values; at one billion IDs per second you would need about 85 million years for a 50% collision probability. Weak random generators are the only realistic failure mode, which is why generators should use cryptographically secure randomness."},
  {"q": "Should I use UUID v4 or v7 for database primary keys?", "a": "Use v7 for new tables in 2026 if your database supports it: timestamp-ordered IDs keep B-tree primary-key indexes from fragmenting, improving insert performance. Use v4 if your framework or database version does not support v7 — the difference matters at millions of rows."},
  {"q": "Does PostgreSQL support UUID v7?", "a": "Yes. Recent PostgreSQL versions' gen_random_uuid() returns v7 by default, and the uuid-ossp extension provides uuidv7(). Older versions can generate v7 in application code or via SQL expressions."},
  {"q": "When should I not use a UUID?", "a": "When identifiers must be short and human-typable (booking codes, order numbers), when a table is so large that the 16-byte key versus an 8-byte bigint matters for index size, or when application logic sorts by ID instead of using a timestamp column."},
  {"q": "How does a UUID generator avoid collisions without a server?", "a": "It uses cryptographically secure randomness from the Web Crypto API. With 122 random bits, the probability of two independently generated v4 UUIDs colliding is negligible — no coordination or central registry is needed."},
  {"q": "Why do LLM APIs ask for idempotency keys?", "a": "So retries are safe: the client sends a UUID with each request, and the server deduplicates by it. If the response is lost and the client retries with the same UUID, the operation executes once instead of twice."}
]
{{< /faq-schema >}}

---

*Version details per RFC 9562 (2024). PostgreSQL gen_random_uuid() behavior reflects current upstream documentation as of November 2026.*
