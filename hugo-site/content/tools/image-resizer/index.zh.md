---
title: "图片尺寸调整器"
date: 2026-11-19
lastmod: 2026-11-21
description: "按宽度、高度或百分比调整图片尺寸。文件不出本机的免费本地工具。"
tags: [图片尺寸调整, 改变图片大小, 照片缩放]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-resizer"
faq:
  - q: "放大会提升画质吗？"
    a: "不会。放大只是对现有像素插值，无法增加细节，结果通常更糊。"
  - q: "怎么保持宽高比？"
    a: "只填宽度或只填高度，另一维会按比例缩放；也可以直接输入 50 这样的百分比。"
  - q: "输出是什么格式？"
    a: "无损 PNG。需要更小体积时，之后再转成 JPG 或 WebP。"
  - q: "会修改原文件吗？"
    a: "不会。只下载新文件，原文件保持不变。"
related: [image-cropper, image-compressor, image-converter, image-rotator]
---

设置目标宽度、高度或百分比，即刻调整任意图片的尺寸。输出以 PNG 下载；需要控制格式请配合[图片格式转换](/zh/tools/image-converter/)。完全在浏览器内运行。

<!--more-->

{{< image-resizer >}}

## 工作原理

工具把图片按目标尺寸绘制到 canvas。填宽度**或**高度即可等比缩放，也可以填百分比（100 = 不变）。调整尺寸后的质量与体积优化，交给[图片压缩器](/zh/tools/image-compressor/)。
