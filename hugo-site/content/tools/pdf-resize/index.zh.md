---
title: "PDF 页面尺寸调整（A4 / Letter / A3）"
date: 2026-11-20
lastmod: 2026-11-20
description: "把 PDF 全部页面改成 A4、Letter、A3 或 Legal，不重新渲染。本地免费，不上传。"
tags: [PDF尺寸调整, PDF A4, PDF页面大小, PDF打印尺寸]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-resize"
---

把尺寸混杂的 PDF 统一成 A4、Letter、A3 或 Legal，打印和归档都更规整。页面画布改变，内容仍是矢量。

<!--more-->

{{< pdf-resize >}}

## 工作原理

用 pdf-lib 把每页的 MediaBox 设为目标尺寸。内容不缩放、不重新编码，因此不会模糊——但为其他长宽比排版的内容可能偏离中心。想裁掉边距请用 [PDF 裁切](/zh/tools/pdf-crop/)。

## 使用提示

- A4 是 595×842 pt；Letter 是 612×792 pt
- 打印前先检查——内容不会自动缩放
- 混合尺寸可用 [PDF 检查](/zh/tools/pdf-info/)查看
