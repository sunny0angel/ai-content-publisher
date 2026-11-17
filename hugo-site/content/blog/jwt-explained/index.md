---
title: "JWT Explained: A Practical Guide to JSON Web Tokens"
date: 2026-11-17
lastmod: 2026-11-17
description: "How JSON Web Tokens work: structure, signing and verification, HS256 vs RS256, security pitfalls, and when opaque session tokens are better. Includes a free JWT decoder."
tags: [JWT explained, JSON Web Token, JWT security, HS256 vs RS256, JWT best practices, access token, refresh token, JWT decoder]
categories: ["AI Tools"]
images:
  featured_image: "/images/jwt-explained.jpg"
draft: false
authors: ["AI Forward"]
slug: "jwt-explained"
---

> **Featured image:** A laptop displaying a security lock icon. Photo by [Dan Nelson](https://www.pexels.com/photo/a-laptop-over-a-round-table-4973899/) on Pexels (Free to use).

The JSON Web Token is the closest thing the web has to a standard ID card: a self-contained, signed document that says who you are and what you are allowed to do, passed between browser and server on every request. It powers the login flows of a large fraction of modern APIs and mobile apps — and it is also the source of a reliably repeating set of security incidents, because a JWT is easy to *use* and subtle to use *correctly*.

This guide explains what a JWT is, how signing and verification actually work, where the traps are, and when you should prefer plain old opaque session tokens instead. To inspect any token's header, payload, and claims in your browser, use the free [JWT Decoder](/tools/jwt-decoder/).

## The Anatomy of a JWT

A JWT is three Base64url-encoded parts joined by dots:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9  ← header
.eyJzdWIiOiIxMjM0NTY3ODkwIn0            ← payload
.s5T_6eJ7xQ8...                          ← signature
```

- **Header** — metadata: the signing algorithm (`alg`) and token type (`typ`). Typical content: `{"alg":"HS256","typ":"JWT"}`.
- **Payload** — the claims: identity (`sub`), expiry (`exp`), issuer (`iss`), audience (`aud`), plus whatever custom fields the application adds.
- **Signature** — computed over the first two parts with the algorithm and a key. This is what prevents tampering.

Note what decoding does and does not do. Anyone can Base64url-decode the header and payload — the [JWT decoder](/tools/jwt-decoder/) does exactly that, no key required. Decoding reveals claims; only **signature verification against the correct key** proves the claims are authentic. The two are frequently confused, and most "JWT security" incidents come from systems that decode and never verify.

## How Signing and Verification Work

**HS256** (HMAC-SHA256) uses a single symmetric secret:

```
signature = HMAC-SHA256(secret, base64url(header) + "." + base64url(payload))
```

The server signs with the secret and verifies by recomputing. One secret, one shared by everyone who needs to verify — if it leaks, anyone can forge tokens.

**RS256** (RSA with SHA-256) uses a private/public key pair: the authorization server signs with the private key, and any resource server verifies with the public key. Nothing sensitive needs to be distributed to verifiers, which is why RS256 is the standard for multi-service and multi-tenant systems, and the required choice for OpenID Connect providers.

The verification checklist a server must run on every request: parse, verify the signature, check `exp` (not expired), check `iss`/`aud` (intended issuer/audience), and only then trust the claims.

## Claims: What Goes In, What Stays Out

Standard claims worth knowing:

| Claim | Meaning |
|-------|---------|
| `sub` | Subject — the user/entity ID |
| `iss` | Issuer — who signed it |
| `aud` | Audience — who it is for |
| `exp` | Expiration (Unix seconds) |
| `iat` / `nbf` | Issued-at / not-valid-before |

The design rule for custom claims: **minimum viable information.** The token is sent on every request; every extra claim inflates it, and every claim in the token is readable by the client (remember: decoding is free). Secrets — API keys, password hashes, credit-card fragments — must never appear in a JWT payload. A token carrying `"api_key": "..."` is not a bug waiting to happen; it is the bug.

## The Security Pitfalls, Ranked

**1. Accepting `alg: "none"`.** A token that declares no algorithm must be rejected unconditionally. Historically, some libraries allowed it — the "alg none attack" — letting attackers strip the signature entirely. Verify the algorithm field is the one you expect, not just the one the token claims.

**2. Weak or leaked HS256 secrets.** "secret", "changeme", and hardcoded demo keys are forgeable in seconds. Secrets should be at least 32 random bytes, stored in environment variables, and rotated.

**3. Storing tokens in localStorage.** localStorage is readable by any script on the origin — meaning any XSS vulnerability immediately escalates to token theft. HttpOnly cookies are the safer transport; if you must use a header, keep expiry short.

**4. Long-lived tokens.** A token with a one-year `exp` is a stolen credential that works for a year. Short-lived access tokens (minutes) paired with a refresh-token rotation scheme shrink the blast radius to minutes.

**5. Not checking `aud` and `iss`.** A token validly signed for a different service, if accepted by yours, is a cross-service forgery. Check both fields.

## Access Tokens vs Refresh Tokens

The modern pattern splits the credential in two:

- **Access token** — short-lived (5–60 minutes), sent with every request, grants the actual API access.
- **Refresh token** — long-lived, kept server-side or in a hardened cookie, used only to mint new access tokens, and invalidated on every use (rotation).

The split is what makes short expiry practical: users do not re-login every five minutes, and a stolen access token expires before an attacker can do much with it. JWTs are well-suited to the access-token role; refresh tokens are usually opaque values stored server-side.

## When NOT to Use a JWT

JWTs are not a universal upgrade. Opaque session tokens — a random ID stored server-side — beat JWTs in three situations: when you need instant **revocation** (a JWT is valid until `exp`, period, unless you add infrastructure), when the token carries **large claims** (a 5 KB JWT on every request is pure overhead), and when **auditing and control** matter more than statelessness (server-side sessions can be killed centrally). The honest rule: if your system is a single service with a database, opaque sessions are simpler and safer; JWTs earn their complexity when you have many services or multiple trust domains.

## Debugging with the JWT Decoder

The fastest path through a 401 mystery: paste the token into the [JWT decoder](/tools/jwt-decoder/), check `exp` against the current time, confirm `aud`/`iss` match your service, and verify the `alg` is what your backend expects. The decoder converts `iat`/`exp` to local time automatically and runs entirely in the browser — the token never leaves the page. It pairs with the [Base64 tool](/tools/base64-encoder/) (JWTs are Base64url underneath) and the [SHA hash generator](/tools/hash-generator/) (HS256 is HMAC-SHA-256).

## Implementing Verification: A Checklist That Works in Every Language

Whatever the stack, the verification sequence is the same — and the order matters. A common vulnerability is checking `exp` but not the signature (or vice versa):

```
1. Split the token on "." and require exactly three parts.
2. Reject alg values you did not configure — accept only an allowlist
   (e.g., {"RS256"} or {"HS256"}), never the token's own claim.
3. Verify the signature over the first two parts with the correct key.
4. Decode the payload and validate exp: reject if now >= exp (with
   a small clock-skew tolerance, e.g., 30 seconds).
5. Validate nbf and iat sanity if present.
6. Validate iss and aud against your expected values.
7. Only now read claims and authorize.
```

Library notes per ecosystem:

- **Node.js**: `jsonwebtoken` is the common choice — pass `{ algorithms: ['RS256'] }` explicitly, never the default.
- **Python**: `PyJWT`; use `jwt.decode(token, key, algorithms=["RS256"], audience=..., issuer=...)`.
- **Go**: `golang-jwt/jwt`; register only the methods you use via `jwt.WithValidMethods`.
- **Java**: `jjwt` (io.jsonwebtoken); require a specific algorithm with `Jwts.parser().verifyWith(key)`.

The recurring mistake in every one of these ecosystems is the same: a permissive configuration that accepts whatever `alg` the token declares. Allowlist your algorithms; everything else follows from that one decision.

**Key management.** HS256 secrets live in environment variables or a secret manager, are at least 32 random bytes, and rotate on a schedule — with an overlap window so old tokens still verify during rotation. RS256 keys live in an identity provider or JWKS endpoint; resource servers fetch the public key (or the JWKS document) and cache it with a short TTL. Never embed either key type in application code or front-end bundles.

## Reading a Token by Hand: What the Decoder Shows

Take this minimal token:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJBZGEiLCJleHAiOjE3OTg3NTg0MDB9.sig
```

Pasting it into the [JWT decoder](/tools/jwt-decoder/) yields:

- **Header**: `{"alg":"HS256","typ":"JWT"}` — HMAC-signed, symmetric secret.
- **Payload**: `sub: 42`, `name: "Ada"`, `exp: 1798758400` — decoded and, with the tool, converted to local time.
- **Signature**: truncated for display — the tool deliberately does not verify, because no key was supplied.

That display is the whole of what decoding can tell you: structure and claims. Whether the token is *valid* is a question only the server with the key can answer — a fact worth repeating to anyone who thinks pasting a token into a debugger "hacks" anything.

## Frequently Asked Questions

{{< faq-schema >}}
[
  {"q": "What is a JWT?", "a": "A JSON Web Token is a signed, Base64url-encoded document in three parts — header, payload, signature — standardized in RFC 7519. It carries claims about identity and authorization and is verified with a key rather than a server-side lookup."},
  {"q": "Can anyone decode a JWT?", "a": "Yes. The header and payload are only Base64url-encoded, not encrypted — anyone can read them. Decoding reveals claims; only signature verification against the correct key proves they are authentic."},
  {"q": "What is the difference between HS256 and RS256?", "a": "HS256 uses one shared symmetric secret for signing and verifying; RS256 uses a private key to sign and a public key to verify. RS256 is standard for multi-service systems because verifiers need no secret."},
  {"q": "What is the alg:none attack?", "a": "A token claiming alg: none asks the verifier to skip signature checking entirely. Correct implementations reject it unconditionally and only accept the specific algorithms they were configured for."},
  {"q": "Should I store JWTs in localStorage?", "a": "No. Any script running on your origin can read localStorage, so an XSS bug immediately escalates to token theft. Prefer HttpOnly cookies, and if a header-based token is unavoidable, keep its lifetime short."},
  {"q": "Why use refresh tokens?", "a": "They let access tokens stay short-lived: the access token expires in minutes, and a separate, rotated refresh token mints replacements. A stolen access token is then only useful for minutes."},
  {"q": "When are opaque session tokens better than JWTs?", "a": "When you need instant revocation, when claims are large, or when central control and auditing matter. A single service with a database is usually better off with opaque server-side sessions."}
]
{{< /faq-schema >}}

---

*JWT structure and claims per RFC 7519. HMAC/RSA algorithm names per RFC 7518. OpenID Connect signing requirements per the OpenID Connect Core specification.*
