---
title: "图片压缩器"
date: 2026-11-19
lastmod: 2026-11-19
description: "在浏览器内压缩 JPG、PNG、WebP——调节质量和最大宽度，直观对比前后大小。照片不出本机的免费本地工具。"
tags: [图片压缩, 压缩图片, 减小图片体积, jpg压缩, png压缩, 图片优化]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-compressor"
---

为网页、邮件或上传限制压缩图片——设置 JPEG 质量和最大宽度，原图与压缩版并排展示，节省的体积一目了然。全部在浏览器本地运行，照片不会被上传到任何地方。

<!--more-->

{{< image-compressor >}}

## 工作原理

工具把图片绘制到 canvas，缩放到你设置的最大宽度，再按所选质量重新编码为 JPEG。显示的输出大小由数据长度计算，因此前后节省比例真实可信。PNG 透明背景在 JPEG 中会丢失——需要无损输出请用[图片格式转换](/zh/tools/image-converter/)。

## 压得更小的技巧

- **质量 70–80** 对照片几乎无损，体积却小得多
- **最大宽度 1200–1600** 覆盖多数网页用途，社交上传无需更大
- **截图**仅在照片类内容时才适合 PNG→JPG；文字为主的截图保持 PNG

其余媒体工具见[媒体工具总览](/zh/blog/media-tools-roundup/)。
