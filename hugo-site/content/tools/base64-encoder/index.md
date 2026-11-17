---
title: "Base64 Encoder & Decoder"
date: 2026-11-17
lastmod: 2026-11-17
description: "Encode and decode Base64 in your browser with full UTF-8 support. Free local tool for developers working with APIs, JWTs, and binary data embedded in text."
tags: [Base64 encoder, Base64 decoder, Base64 converter, base64 encode, base64 decode, URL safe base64, developer tools]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "base64-encoder"
---

Convert plain text to Base64 and back, with correct UTF-8 handling — unlike `btoa()`, this tool does not break on Japanese, Chinese, or emoji. Everything runs locally in your browser; nothing is uploaded.

<!--more-->

{{< base64-encoder >}}

## How it works

Base64 encodes binary data as 64 printable ASCII characters (`A–Z`, `a–z`, `0–9`, `+`, `/`), with `=` padding. Every 3 input bytes become 4 output characters — a 33% size increase, paid in exchange for safe transport through text-only channels: JSON strings, XML, email (MIME), and URL parameters.

This tool encodes text to UTF-8 bytes first, then applies Base64 — the correct behavior that plain `btoa()` (which only handles Latin-1) fails at. Decoding reverses the process.

## Where you will meet it

- **JWT**: the header and payload of every JSON Web Token are Base64url-encoded JSON. Decode them with our [JWT decoder](/tools/jwt-decoder/).
- **Data URLs**: `data:image/png;base64,...` embeds images directly in HTML and CSS.
- **API payloads**: binary blobs (images, certificates, protobuf) travel as Base64 strings inside JSON.
- **Basic auth**: `Authorization: Basic base64(user:pass)` — encoding here is transport, not security; anyone can decode it.

For the other half of the data workflow — converting structured records into tables — see the [JSON to CSV converter](/tools/json-to-csv/).
