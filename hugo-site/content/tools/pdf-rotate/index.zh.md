---
title: "PDF 旋转页面"
date: 2026-11-20
lastmod: 2026-11-21
description: "把 PDF 全部页面旋转 90°、180° 或 270° 后下载。免费、本地、不上传。"
tags: [PDF旋转, PDF页面转向, 修正PDF方向, PDF横页]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-rotate"
faq:
  - q: "旋转会重新压缩页面吗？"
    a: "不会。工具只修改页面的旋转标记，文字和图片不会重新压缩，画质保持不变。"
  - q: "可以只旋转部分页面吗？"
    a: "可以。选择全部页面，或输入「1, 4-6」这样的范围，只修正横置的扫描页。"
  - q: "为什么在别的阅读器里还是歪的？"
    a: "部分阅读器会忽略旋转标记。用本工具重新保存后，换一个阅读器确认；文件中的方向已经修正。"
related: [pdf-reorder, pdf-delete-pages, pdf-n-up, pdf-crop]
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
