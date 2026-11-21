---
title: "删除 PDF 页面"
date: 2026-11-20
lastmod: 2026-11-21
description: "删除 PDF 中不需要的页面并下载干净文件——全程在浏览器本地处理，其余页面保持原样。"
tags: [删除PDF页面, PDF去除页面, PDF删页, PDF清理]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-delete-pages"
faq:
  - q: "会修改原文件吗？"
    a: "不会。工具会生成一个去掉所选页面的新文件，原文件保持不变。"
  - q: "加密 PDF 能删除页面吗？"
    a: "需要先在阅读器中解锁并另存为无密码副本。加密状态的文件无法解析。"
  - q: "删除后页码为什么变了？"
    a: "页面被真正移除，页面内容中印的页码会随之前移。若需要稳定编号，删除后用页码工具重新添加。"
related: [pdf-merge, pdf-split, pdf-reorder, pdf-rotate]
---

把空白扫描页、过时条款或误插入的页面从 PDF 中删掉。指定要删除的页，保留其余内容，然后下载清理后的文档。

<!--more-->

{{< pdf-delete-pages >}}

## 工作原理

工具把除指定页以外的所有页面复制进新 PDF，保留页面内容与顺序。不做涂黑，也不重新编码。若想只保留某些页，用 [PDF 拆分](/zh/tools/pdf-split/)做相反操作。

## 使用提示

- 用范围批量删除：2, 4-6 表示删第 2 页和第 4 到 6 页
- 做破坏性编辑前务必保留原文件副本
- 扫描件删页后可用 [PDF 压缩](/zh/tools/pdf-compress/)减小体积
