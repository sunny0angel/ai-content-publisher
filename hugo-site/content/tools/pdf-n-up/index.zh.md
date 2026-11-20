---
title: "PDF N-up：每张 2 页或 4 页"
date: 2026-11-20
lastmod: 2026-11-20
description: "把 PDF 的 2 页或 4 页排到一张横向纸上，节省纸张。浏览器本地完成，不上传。"
tags: [PDF N-up, 每张多页, PDF 2合1, 省纸打印, 拼版打印]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-n-up"
---

把长 PDF 变成一半或四分之一的张数：每张横向页面放 2 页或 4 页，按阅读顺序排列。

<!--more-->

{{< pdf-n-up >}}

## 工作原理

每个源页面以矢量形式嵌入新的 A4 横向纸张，缩放到 2×1 或 2×2 网格。因为不是栅格化，文字依旧清晰。只想改页面尺寸请用 [PDF 尺寸调整](/zh/tools/pdf-resize/)。

## 使用提示

- 2-up 适合幻灯片，4-up 适合讲义和速查表
- A4 横向是 842×595 pt
- 配合双面打印，纸张用量可降到四分之一
