---
title: "Image Filter & Adjuster"
date: 2026-11-19
lastmod: 2026-11-21
description: "Apply grayscale, sepia, invert, and blur filters plus brightness and contrast adjustments. Free local tool — files never leave your machine."
tags: [image filter, grayscale image, sepia filter, photo editor online, brightness contrast]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-filter"
faq:
  - q: "Which filters are available?"
    a: "Grayscale, sepia, invert and blur, plus brightness and contrast sliders. They combine in a single render pass."
  - q: "Is the export lossless?"
    a: "No. The result is saved as JPEG at quality 0.9. Re-editing an exported file compounds compression, so keep the original."
  - q: "Can I filter only part of the image?"
    a: "No, filters apply to the whole image. Crop the region first if you need a local edit."
  - q: "Is the image uploaded?"
    a: "No. Canvas filters run in the tab."
related: [image-compare, image-pixelator, image-compressor, image-converter]
---

Apply filters — grayscale, sepia, invert, blur — and adjust brightness and contrast with live sliders, then download the result. Everything runs in your browser via canvas filters.

<!--more-->

{{< image-filter >}}

## How it works

The tool composes CSS-style canvas filters (`brightness()`, `contrast()`, `grayscale()`, etc.) into a single rendering pass, then exports as JPEG. For pixel-level effects like mosaic privacy blurs, the [image pixelator](/tools/image-pixelator/) does the heavy lifting.
