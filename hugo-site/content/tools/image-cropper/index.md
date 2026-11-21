---
title: "Image Cropper"
date: 2026-11-19
lastmod: 2026-11-21
description: "Crop images with aspect-ratio presets (1:1, 4:3, 16:9) and position controls. Free local tool — files never leave your machine."
tags: [image cropper, crop image online, crop photo, aspect ratio crop, square crop]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-cropper"
faq:
  - q: "Does cropping reduce image quality?"
    a: "Cropping itself is lossless: the selected region is copied to a canvas and exported as PNG. Only later JPEG compression would lose quality."
  - q: "Can I crop to exact pixel dimensions?"
    a: "The tool uses aspect presets and a relative size slider. Crop first, then use the image resizer for exact width and height."
  - q: "Is the original file changed?"
    a: "No. You download a new PNG and the file on disk stays untouched."
related: [image-resizer, image-rotator, image-compressor, image-color-picker]
---

Crop any image with preset aspect ratios — 1:1 for avatars, 4:3 for slides, 16:9 for covers — plus center position and crop-size sliders. The result downloads as PNG. Runs entirely in your browser.

<!--more-->

{{< image-cropper >}}

## How it works

The tool computes a crop window from the ratio, size, and center-position sliders, then copies that region to a new canvas. After cropping, the [image resizer](/tools/image-resizer/) handles exact dimensions and the [image compressor](/tools/image-compressor/) handles file size.
