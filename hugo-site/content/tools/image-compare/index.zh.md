---
title: "图片对比工具（前后对比）"
date: 2026-11-20
lastmod: 2026-11-21
description: "用可拖动的分隔线并排对比两张图片——适合压缩质量检查、修图前后和设计评审。免费本地工具。"
tags: [图片对比, 前后对比, 图片对比滑块, 照片对比]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-compare"
faq:
  - q: "图片会上传吗？"
    a: "不会。两张图都在本地渲染，滑块只改变页面内的裁剪边界。"
  - q: "能量化像素差异吗？"
    a: "不能。它是视觉对比滑块。需要数值比较时，请对比文件大小或使用专用图像差分工具。"
  - q: "两张图尺寸要一致吗？"
    a: "尺寸一致时叠加效果最好。尺寸不同也能显示，但分割线两侧可能对不齐。"
related: [image-compressor, image-filter, image-resizer, image-converter]
---

加载两张图片，拖动分隔线让一张盖住另一张——压缩质量、修图和设计迭代的经典前后对比滑块。文件留在浏览器内。

<!--more-->

{{< image-compare >}}

## 工作原理

两张图片在裁剪的叠加层中渲染，滑杆控制裁剪边界，也可以直接在图片上拖动。配合[图片压缩器](/zh/tools/image-compressor/)检查画质损失，或配合[图片滤镜](/zh/tools/image-filter/)对比编辑前后。
