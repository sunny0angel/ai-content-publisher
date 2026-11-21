---
title: "浏览器内 PDF 压缩"
date: 2026-11-20
lastmod: 2026-11-21
description: "以 72–150 DPI 重新渲染页面并调节 JPEG 质量来缩小 PDF。本地处理、不上传、无文件大小限制。"
tags: [PDF压缩, 减小PDF体积, PDF压缩工具, PDF文件大小]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-compress"
faq:
  - q: "能压到多小？"
    a: "取决于原文件。纯扫描图片型 PDF 常能缩小 50–80%；纯文字 PDF 可压缩的位图很少，体积几乎不变。"
  - q: "为什么文字变得无法选中？"
    a: "压缩会把页面按指定质量重新渲染为图片，这正是减重的原因，同时也去掉了文字层。"
  - q: "能保留可搜索文字再压缩吗？"
    a: "本工具做不到。要保留文字层，请使用只降采样图片、不栅格化文字的优化工具，或同时保留原文件。"
  - q: "质量该选多少？"
    a: "屏幕阅读 150 DPI 足够，打印建议 200–300 DPI。数值越低体积越小，但小字会发虚。"
related: [pdf-to-jpg, pdf-resize, pdf-merge, pdf-crop]
---

按你可控的分辨率和质量把页面重新渲染为 JPEG，从而减小 PDF 体积——并对比压缩前后的大小。

<!--more-->

{{< pdf-compress >}}

## 工作原理

PDF.js 把每页渲染到 canvas，JPEG 再由 pdf-lib 按原页面尺寸嵌入新 PDF。非常适合扫描件和图片型文档。由于文字被栅格化，将无法选中或搜索——替换原文件前请先检查结果。纯矢量减体积可试 [N-up](/zh/tools/pdf-n-up/)或用[删除页面](/zh/tools/pdf-delete-pages/)。

## 使用提示

- 110 DPI + 65% 质量通常能让扫描件缩小 50–80%
- 邮件预览用 72 DPI；文字必须清晰时用 150 DPI
- 如果重建后更大，说明原文件本身编码已经很高效
