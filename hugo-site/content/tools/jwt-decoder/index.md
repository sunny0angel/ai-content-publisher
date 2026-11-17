---
title: "JWT Decoder"
date: 2026-11-17
lastmod: 2026-11-17
description: "Decode JWT header, payload, and signature in your browser. Inspect claims and timestamps without a key. Free local tool — your token never leaves the page."
tags: [JWT decoder, JWT parser, decode JWT, JSON web token, JWT header payload, JWT claims, token debugger]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "jwt-decoder"
---

Paste a JSON Web Token and see its header, payload, and signature decoded instantly — including `iat`/`exp` converted to local time. The token stays in your browser; it is never sent anywhere.

<!--more-->

{{< jwt-decoder >}}

## What a JWT is

A JSON Web Token is three Base64url-encoded parts joined by dots: `header.payload.signature`. The header declares the signing algorithm (`alg`), the payload carries claims (`sub`, `exp`, `iss`, custom fields), and the signature lets the server verify the first two parts were not tampered with.

**Important**: decoding is not verification. Anyone can decode a JWT — the signature only proves authenticity when checked against the correct key. This tool deliberately does not verify, which is why it needs no key and can run entirely offline.

## What to look for

- **`alg: "none"`** — a token claiming no signature. In production this is an immediate red flag: validators must reject it.
- **`exp` in the past** — an expired token. Servers reject these; if your client keeps one, the refresh flow is broken.
- **Excessive claims** — tokens should carry the minimum needed. Every claim enlarges the token, and every token is sent on every request.
- **Secrets in the payload** — a token with `password` or `api_key` claims means someone confused authentication with storage.

## Typical use

Debugging a 401 loop: decode the token, check `exp` and `aud`, and confirm which key/issuer your backend expects. Pairs naturally with the [Base64 encoder](/tools/base64-encoder/) (JWTs are Base64url under the hood) and the [SHA hash generator](/tools/hash-generator/) (HS256 = HMAC-SHA-256).
