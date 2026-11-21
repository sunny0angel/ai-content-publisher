---
title: "图片滤镜与调节工具"
date: 2026-11-19
lastmod: 2026-11-21
description: "应用灰度、复古、反色、模糊滤镜并调节亮度与对比度。文件不出本机的免费本地工具。"
tags: [图片滤镜, 灰度图片, 复古滤镜, 在线修图, 亮度对比度]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-filter"
faq:
  - q: "有哪些滤镜？"
    a: "灰度、棕褐色、反色、模糊，以及亮度和对比度滑块，可一次渲染叠加应用。"
  - q: "导出是无损的吗？"
    a: "不是。结果以质量 0.9 的 JPEG 保存。对导出文件再次编辑会叠加压缩损失，请保留原图。"
  - q: "可以只处理局部吗？"
    a: "不能，滤镜作用于整张图。需要局部处理时请先裁剪出该区域。"
  - q: "图片会上传吗？"
    a: "不会。canvas 滤镜在本标签页内运行。"
related: [image-compare, image-pixelator, image-compressor, image-converter]
---

应用滤镜——灰度、复古、反色、模糊——并用滑杆实时调节亮度和对比度，然后下载。全部通过 canvas 滤镜在浏览器内完成。

<!--more-->

{{< image-filter >}}

## 工作原理

工具把 CSS 风格的 canvas 滤镜（`brightness()`、`contrast()`、`grayscale()` 等）合成进一次渲染，再导出为 JPEG。马赛克等像素级效果交给[图片像素化工具](/zh/tools/image-pixelator/)。
