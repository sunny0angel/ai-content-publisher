---
title: "Password Generator"
date: 2026-11-18
lastmod: 2026-11-21
description: "Generate strong random passwords with selectable length and character sets, using cryptographically secure randomness. Free local tool with strength estimate."
tags: [password generator, strong password, random password, secure password, password strength, security tools]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "password-generator"
faq:
  - q: "Is the generated password transmitted?"
    a: "No. Randomness comes from crypto.getRandomValues and the password exists only in this tab until you copy it."
  - q: "How is the strength estimate calculated?"
    a: "It uses entropy: length times log2 of the alphabet size. Around 80 bits resists offline guessing; 100+ bits is better for long-lived secrets."
  - q: "Are ambiguous characters excluded?"
    a: "Yes. Look-alike characters such as 0/O and 1/l/I are left out so the password is easier to read and type."
  - q: "Can I use it for API keys?"
    a: "Yes, but store the result in a secret manager rather than a document. For user passwords, pair it with a password manager."
related: [uuid-generator, hash-generator, base64-encoder, jwt-signer]
---

Generate strong passwords locally with `crypto.getRandomValues` — the same cryptographically secure source browsers use for TLS — with selectable length (8–64) and character sets, plus an entropy-based strength estimate. Nothing is transmitted; the password exists only in your tab.

<!--more-->

{{< password-generator >}}

## How it works

The generator picks characters via the Web Crypto API and guarantees at least one character from each selected set, then shuffles. The strength estimate computes entropy as `length × log2(alphabet size)` — above ~80 bits is considered strong against offline attacks. Note the alphabet deliberately excludes look-alike characters (`0/O`, `1/l/I`) to make typing and reading easier.

## Rules that matter more than the password

- **Unique per site**: reuse is the #1 way strong passwords die — pair with a password manager
- **Length beats complexity**: 20 random lowercase characters (~94 bits) beat 10 mixed-case ones (~59 bits)
- **Not SHA-256 territory**: passwords are stored hashed with Argon2/bcrypt server-side — see the [SHA-256 guide](/blog/sha-256-explained/) for why

For API keys and tokens, pair this with the [UUID generator](/tools/uuid-generator/) — v4 UUIDs are the standard for identifiers that must never collide.
