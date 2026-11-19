---
title: "图片滤镜与调节工具"
date: 2026-11-19
lastmod: 2026-11-19
description: "应用灰度、复古、反色、模糊滤镜并调节亮度与对比度。文件不出本机的免费本地工具。"
tags: [图片滤镜, 灰度图片, 复古滤镜, 在线修图, 亮度对比度]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-filter"
---

应用滤镜——灰度、复古、反色、模糊——并用滑杆实时调节亮度和对比度，然后下载。全部通过 canvas 滤镜在浏览器内完成。

<!--more-->

{{< image-filter >}}

## 工作原理

工具把 CSS 风格的 canvas 滤镜（`brightness()`、`contrast()`、`grayscale()` 等）合成进一次渲染，再导出为 JPEG。马赛克等像素级效果交给[图片像素化工具](/zh/tools/image-pixelator/)。
