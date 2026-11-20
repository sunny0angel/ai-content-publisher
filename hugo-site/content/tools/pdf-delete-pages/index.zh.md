---
title: "删除 PDF 页面"
date: 2026-11-20
lastmod: 2026-11-20
description: "删除 PDF 中不需要的页面并下载干净文件——全程在浏览器本地处理，其余页面保持原样。"
tags: [删除PDF页面, PDF去除页面, PDF删页, PDF清理]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-delete-pages"
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
