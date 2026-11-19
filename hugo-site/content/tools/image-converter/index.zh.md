---
title: "图片格式转换器（JPG / PNG / WebP）"
date: 2026-11-19
lastmod: 2026-11-19
description: "在浏览器内把图片转换为 JPG、PNG 或 WebP。文件在本机处理、绝不上传的免费本地工具。"
tags: [图片转换, png转jpg, jpg转png, webp转换, 图片格式转换]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-converter"
---

把任意图片转成 JPG、PNG 或 WebP——选好目标格式即可下载。转换完全通过 canvas 在浏览器内完成，文件不会离开你的电脑。

<!--more-->

{{< image-converter >}}

## 工作原理

工具解码图片、绘制到 canvas、再以 92% 质量重新编码为目标格式。格式要点：**PNG** 无损（截图和需要透明的图片首选）、**JPG** 对照片体积最小、**WebP** 压缩率与质量比最佳——现代环境通用。

## 各格式的适用场景

| 格式 | 最适合 |
|------|--------|
| PNG | 截图、logo、透明背景 |
| JPG | 照片、大图 |
| WebP | 网页传输、最小体积 |

转换前需要调整尺寸用[图片尺寸调整器](/zh/tools/image-resizer/)，调节质量与体积用[图片压缩器](/zh/tools/image-compressor/)。
