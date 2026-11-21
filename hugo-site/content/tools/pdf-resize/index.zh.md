---
title: "PDF 页面尺寸调整（A4 / Letter / A3）"
date: 2026-11-20
lastmod: 2026-11-21
description: "把 PDF 全部页面改成 A4、Letter、A3 或 Legal，不重新渲染。本地免费，不上传。"
tags: [PDF尺寸调整, PDF A4, PDF页面大小, PDF打印尺寸]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-resize"
faq:
  - q: "调整尺寸和 N-up 有什么区别？"
    a: "调整尺寸改变每页的纸张大小（如 A4 转 Letter）；N-up 是把多页排到一张纸上。"
  - q: "会把内容拉变形吗？"
    a: "工具按比例缩放并保持宽高比，不会拉伸。比例不同时会留白边。"
  - q: "放大后画质会下降吗？"
    a: "矢量文字仍然清晰；位图无法凭空增加细节，低分辨率扫描件放大到 A3 可能发虚。"
related: [pdf-crop, pdf-n-up, pdf-compress, images-to-pdf]
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
