---
title: "Image Cropper"
date: 2026-11-19
lastmod: 2026-11-19
description: "Crop images with aspect-ratio presets (1:1, 4:3, 16:9) and position controls. Free local tool — files never leave your machine."
tags: [image cropper, crop image online, crop photo, aspect ratio crop, square crop]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-cropper"
---

Crop any image with preset aspect ratios — 1:1 for avatars, 4:3 for slides, 16:9 for covers — plus center position and crop-size sliders. The result downloads as PNG. Runs entirely in your browser.

<!--more-->

{{< image-cropper >}}

## How it works

The tool computes a crop window from the ratio, size, and center-position sliders, then copies that region to a new canvas. After cropping, the [image resizer](/tools/image-resizer/) handles exact dimensions and the [image compressor](/tools/image-compressor/) handles file size.
