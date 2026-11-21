---
title: "空白 PDF 生成器"
date: 2026-11-20
lastmod: 2026-11-21
description: "生成 1 到 100 页 A4 或 Letter 空白页——用于分隔页、笔记空间和打印测试。免费本地。"
tags: [空白PDF, 生成空白PDF, 空白页, 分隔页, PDF生成]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-blank-pages"
faq:
  - q: "什么时候需要插入空白页？"
    a: "双面打印分隔章节、留出手写空间、让插入的扫描页与印刷页数对齐，都会用到。"
  - q: "空白页能匹配原文档尺寸吗？"
    a: "可以。空白页沿用相邻页面的尺寸，打印时不会错位。"
  - q: "空白页会计入页码吗？"
    a: "会。它们是真实页面，插入几页，后面的编号就顺延几页。"
related: [pdf-duplicate-pages, pdf-merge, pdf-page-numbers, pdf-n-up]
---

生成只有空白页的干净 PDF——一页到一百页，A4 或 Letter。适合章节分隔、笔记空间和打印机对位测试。

<!--more-->

{{< pdf-blank-pages >}}

## 工作原理

用 pdf-lib 从零构建文档，除基本信息外不含隐藏内容、字体或元数据。要与真实文档合并，用 [PDF 合并](/zh/tools/pdf-merge/)；想减少纸张，用 [N-up](/zh/tools/pdf-n-up/)。

## 使用提示

- 用 100% 比例打印一页，检查打印机边距
- A4 是 595×842 pt；Letter 是 612×792 pt
- 空白页常是扫描副产物——用[删除页面](/zh/tools/pdf-delete-pages/)去掉
