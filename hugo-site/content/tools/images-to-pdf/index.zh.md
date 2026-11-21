---
title: "图片转 PDF"
date: 2026-11-20
lastmod: 2026-11-21
description: "把 JPG、PNG 图片转成每页一张的 PDF，自动等比适配。免费本地——照片不会被上传。"
tags: [图片转PDF, JPG转PDF, PNG转PDF, 照片转PDF, 图片合成PDF]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "images-to-pdf"
faq:
  - q: "支持哪些图片格式？"
    a: "支持 JPG、PNG、WebP 和 GIF（首帧）。每张图片生成一页，按你排列的顺序输出。"
  - q: "可以设置纸张大小和方向吗？"
    a: "可以。选择 A4、Letter 或适应图片，设置横竖与页边距；适应图片会保持原始比例。"
  - q: "照片会被重新压缩吗？"
    a: "在格式允许时按原样嵌入。大图较多时 PDF 会很重，需要邮件发送的话请先缩小或压缩图片。"
  - q: "会保留 EXIF 位置信息吗？"
    a: "部分格式会保留元数据。如果照片含不想公开的位置信息，请先用图片工具清除元数据。"
related: [pdf-to-jpg, pdf-compress, pdf-merge, image-compressor]
---

把手机照片、扫描页或导出的截图合成一份 PDF——每页一张图，居中适配且不变形。

<!--more-->

{{< images-to-pdf >}}

## 工作原理

每张图片按原分辨率嵌入，按所选页面尺寸等比缩放。支持 JPG 和 PNG，PNG 透明通道保留。要与现有 PDF 合并，请用 [PDF 合并](/zh/tools/pdf-merge/)。

## 使用提示

- 按你希望的页面顺序选择图片
- A4 纵向适合文档，A4 横向适合幻灯片和宽图
- 20 MB 的手机照片先用[图片压缩](/zh/tools/image-compressor/)处理
