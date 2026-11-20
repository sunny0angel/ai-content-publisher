---
title: "PDF 检查：页数、尺寸、元数据"
date: 2026-11-20
lastmod: 2026-11-20
description: "在本地检查 PDF——页数、页面尺寸、文件大小和元数据。不上传，离线也能用。"
tags: [PDF信息, PDF页数, PDF尺寸查看, PDF元数据查看, PDF检查]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-info"
---

在发送、打印或归档前先看清 PDF 里有什么：页数、页面尺寸、文件大小和元数据，全部本地读取。

<!--more-->

{{< pdf-info >}}

## 工作原理

文件在标签页内由 pdf-lib 解析，只读结构，不读取渲染内容。常见尺寸（A4 为 595×842，Letter 为 612×792）以 pt 显示。加密 PDF 会明确提示，而不是静默失败。相关：[元数据编辑](/zh/tools/pdf-metadata/)和[压缩](/zh/tools/pdf-compress/)。

## 使用提示

- A4=595×842 pt、Letter=612×792 pt、A3=842×1191 pt
- 页面尺寸混杂通常说明是合并过的文档
- 若已加密，请先在阅读器中移除密码
