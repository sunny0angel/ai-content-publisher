---
title: "JWT Signer (HS256)"
date: 2026-11-19
lastmod: 2026-11-19
description: "Sign JSON Web Tokens with HS256 (HMAC-SHA256) entirely in your browser via Web Crypto. Free local tool — your secret never leaves the page. Pairs with the JWT decoder."
tags: [JWT signer, JWT generator, sign JWT, HS256, HMAC-SHA256, JWT token generator, JSON web token signer]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "jwt-signer"
---

Generate a signed JWT from your own header, payload, and secret — the HS256 signature is computed with the browser's Web Crypto API, so the secret never leaves your tab. The natural companion to the [JWT decoder](/tools/jwt-decoder/): decode to understand, sign to build.

<!--more-->

{{< jwt-signer >}}

## How it works

The tool Base64url-encodes your header and payload, then computes `HMAC-SHA256(secret, header.payload)` via `crypto.subtle.sign` — the same primitive production JWT libraries use for HS256. The result is a complete `header.payload.signature` token in the standard [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519) format.

## Security notes worth reading

- **The secret is the entire security.** Anyone holding it can forge tokens for your system. Use at least 32 random bytes — the [password generator](/tools/password-generator/) can produce a suitable value, though a dedicated secret manager is better.
- **HS256 is symmetric.** Every service that verifies your tokens needs the same secret. For multi-service setups, RS256 (asymmetric) is the better architecture — this tool covers the HS256 case, which is the right choice for single-service apps and quick testing.
- **Never ship the secret to a client.** This tool keeps it local for testing convenience; production signing belongs server-side.

For the full picture of JWT structure, verification checklists, and common attacks, read [JWT Explained](/blog/jwt-explained/).
