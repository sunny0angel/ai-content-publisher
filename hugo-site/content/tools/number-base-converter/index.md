---
title: "Number Base Converter (HEX / DEC / BIN / OCT)"
date: 2026-11-18
lastmod: 2026-11-18
description: "Convert numbers between hex, decimal, binary, octal, and base-36 with arbitrary precision. Free local tool for developers."
tags: [number base converter, hex to decimal, binary converter, octal converter, base36, radix converter, developer tools]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "number-base-converter"
---

Convert any integer between decimal, hex, binary, octal, and base-36 — with BigInt precision, so 64-bit values and beyond never lose digits. Runs entirely in your browser.

<!--more-->

{{< number-base-converter >}}

## How it works

The tool parses your input in the selected base using `BigInt` — unlike JavaScript numbers, BigInt handles arbitrarily large integers exactly, so color codes, hash fragments, and database IDs survive the trip. All four representations update as you type.

## Where you will meet it

- **Debugging**: hex dumps, memory addresses, and bitmasks are binary/hex arithmetic in disguise
- **Colors**: `#2563eb` is just a hex number — the [color converter](/tools/color-converter/) handles the visual side
- **Hashes**: SHA digests are hex strings; converting fragments to decimal makes them sortable/compact — generate some with the [hash generator](/tools/hash-generator/)
- **Base36 URLs**: short-link services encode IDs in base36 — decode them here
