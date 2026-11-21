---
title: "URL Encoder & Decoder"
date: 2026-11-18
lastmod: 2026-11-21
description: "Encode and decode URL components with proper percent-encoding. Free local tool for building query strings, links, and API URLs that never break."
tags: [URL encoder, URL decoder, percent encoding, URL encode, encodeURIComponent, URL escape, developer tools]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "url-encoder"
faq:
  - q: "Which JavaScript function does it match?"
    a: "encodeURIComponent and decodeURIComponent, so the output matches what your code sends in query strings."
  - q: "Why is a space encoded as %20 instead of +?"
    a: "%20 is standard percent-encoding. The + form belongs to application/x-www-form-urlencoded and is not interchangeable everywhere."
  - q: "Can I encode a whole URL?"
    a: "This tool encodes components, so ://?& would be escaped as well. Encode only the dynamic values, not the full URL."
  - q: "Does it handle Japanese and emoji?"
    a: "Yes. Text is converted to UTF-8 before percent-encoding, so multi-byte characters survive."
related: [base64-encoder, json-formatter, hash-generator, case-converter]
---

Convert any text to a URL-safe percent-encoded string and back. Handles UTF-8 correctly, so Japanese, Chinese, and emoji survive the trip through query strings. Runs entirely in your browser — nothing is sent anywhere.

<!--more-->

{{< url-encoder >}}

## How it works

URLs can only safely contain a small set of characters (letters, digits, and `-._~`). Everything else — spaces, `&`, `?`, `#`, non-ASCII text — must be percent-encoded: each byte becomes `%XX`. This tool uses the browser's `encodeURIComponent`/`decodeURIComponent`, the same functions your JavaScript code uses, so results match what your app will send.

The two variants matter: `encodeURIComponent` escapes **everything** (correct for query values), while `encodeURI` leaves URL structure characters intact (correct for full URLs). This tool uses the component variant — the safe choice for building query strings.

## Where you will meet it

- **Query strings**: `?q=AI+Forward&lang=ja` — unencoded `&` or `=` inside a value corrupts the URL
- **API calls**: dynamic values (names, addresses, free-text search) must be encoded before interpolation
- **OAuth redirects and signed links**: a mis-encoded URL breaks signatures

Pairs naturally with the [Base64 encoder](/tools/base64-encoder/) (Base64url is the other URL-safe encoding) and the [JSON formatter](/tools/json-formatter/) when query results come back as JSON.
