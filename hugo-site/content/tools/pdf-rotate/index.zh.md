---
title: "PDF 旋转页面"
date: 2026-11-20
lastmod: 2026-11-20
description: "把 PDF 全部页面旋转 90°、180° 或 270° 后下载。免费、本地、不上传。"
tags: [PDF旋转, PDF页面转向, 修正PDF方向, PDF横页]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-rotate"
---

修正横向扫描和倒置导出的文件。把全部页面旋转 90°、180° 或 270°，下载打开方向正确的 PDF。

<!--more-->

{{< pdf-rotate >}}

## 工作原理

旋转写入每页的 rotation 属性，不重新渲染，也不损失画质。多数阅读器和打印机立即生效。只想转某一页？先用 [PDF 拆分](/zh/tools/pdf-split/)拆出来，再用[页面重排](/zh/tools/pdf-reorder/)。

## 使用提示

- 横向扫描存成纵向时，用 90° 或 270°
- 双面扫描上下颠倒用 180°
- 旋转只是元数据——文件体积几乎不变
