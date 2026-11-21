---
title: "图片转 Base64 工具"
date: 2026-11-19
lastmod: 2026-11-21
description: "把图片转成可直接嵌入 HTML 或 CSS 的 Base64 Data URL。无上传的免费本地工具。"
tags: [图片转base64, data url生成, base64图片, HTML图片嵌入]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-to-base64"
faq:
  - q: "内嵌图片多大合适？"
    a: "Base64 会让体积增加约 33%，因此适合图标和小缩略图，大约 100 KB 以下。"
  - q: "支持哪些格式？"
    a: "浏览器能读取的图片都支持。Data URL 使用文件的 MIME 类型，例如 image/png。"
  - q: "能把 Data URL 还原成文件吗？"
    a: "本工具只编码。还原请用能把载荷写成二进制文件的解码工具。"
  - q: "图片会上传吗？"
    a: "不会。读取文件与 Base64 编码都在标签页内完成。"
related: [base64-encoder, image-converter, image-compressor, image-color-picker]
---

把图片转成 `data:image/...;base64,...` URL，可直接粘进 HTML 的 `src` 属性或 CSS 的 `background-image`——无需单独文件、无需服务器请求。完全在浏览器内运行。

<!--more-->

{{< image-to-base64 >}}

## 工作原理

浏览器读取文件并把字节编码为 Base64（与 [Base64 编码器](/zh/tools/base64-encoder/)背后同一种编码）。注意：内嵌比原文件大约 33%，所以 Data URL 适合图标和预览缩略图等小资源，不适合照片。
