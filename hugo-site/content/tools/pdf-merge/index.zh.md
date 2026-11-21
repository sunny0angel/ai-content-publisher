---
title: "PDF 合并"
date: 2026-11-20
lastmod: 2026-11-21
description: "按你选择的顺序把多个 PDF 合并成一个文件。不上传、不注册、无水印——全部在浏览器内完成。"
tags: [PDF合并, PDF合并工具, 多个PDF合并, PDF拼接]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-merge"
faq:
  - q: "合并 PDF 会上传文件吗？"
    a: "不会。每个文件都在本标签页内由 pdf-lib 打开并合并，不会上传，关闭标签页即丢弃。"
  - q: "可以合并加密 PDF 吗？"
    a: "不能直接合并。请先在阅读器中输入密码并另存为无保护副本，再合并该副本；加密文件无法解析。"
  - q: "合并会降低画质或加水印吗？"
    a: "不会。页面按原样复制，不重新压缩，也不加任何水印。纸张尺寸也不会统一，A4 与 Letter 混排会原样保留。"
  - q: "书签、链接和表单会保留吗？"
    a: "页面内容、图片和文字会保留。文档级书签、部分批注和交互表单可能丢失，发送前请检查结果。"
related: [pdf-split, pdf-delete-pages, pdf-reorder, pdf-compress]
---

把两个以上的 PDF 按你选择的顺序合并成一个文件。合同、扫描件、发票、导出的幻灯片，几秒完成——文件不出浏览器。

<!--more-->

{{< pdf-merge >}}

## 工作原理

每个 PDF 都用 pdf-lib 在本地解析，页面按选择顺序复制进新文档后保存。有密码的 PDF 需先移除密码。要做相反的操作，请用 [PDF 拆分](/zh/tools/pdf-split/)或[删除页面](/zh/tools/pdf-delete-pages/)。

## 使用提示

- 按你希望的合并顺序选择文件
- 结果下载为 merged.pdf，之后自行重命名
- 扫描件体积大时，合并后可用 [PDF 压缩](/zh/tools/pdf-compress/)
