---
title: "图片转 Base64 工具"
date: 2026-11-19
lastmod: 2026-11-19
description: "把图片转成可直接嵌入 HTML 或 CSS 的 Base64 Data URL。无上传的免费本地工具。"
tags: [图片转base64, data url生成, base64图片, HTML图片嵌入]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-to-base64"
---

把图片转成 `data:image/...;base64,...` URL，可直接粘进 HTML 的 `src` 属性或 CSS 的 `background-image`——无需单独文件、无需服务器请求。完全在浏览器内运行。

<!--more-->

{{< image-to-base64 >}}

## 工作原理

浏览器读取文件并把字节编码为 Base64（与 [Base64 编码器](/zh/tools/base64-encoder/)背后同一种编码）。注意：内嵌比原文件大约 33%，所以 Data URL 适合图标和预览缩略图等小资源，不适合照片。
