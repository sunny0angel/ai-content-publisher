---
title: "浏览器内 PDF 压缩"
date: 2026-11-20
lastmod: 2026-11-20
description: "以 72–150 DPI 重新渲染页面并调节 JPEG 质量来缩小 PDF。本地处理、不上传、无文件大小限制。"
tags: [PDF压缩, 减小PDF体积, PDF压缩工具, PDF文件大小]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-compress"
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
