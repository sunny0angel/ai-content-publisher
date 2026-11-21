---
title: "PDF 页面重排"
date: 2026-11-20
lastmod: 2026-11-21
description: "把 PDF 页面按任意顺序重排——输入新顺序即可下载。本地、免费、不上传。"
tags: [PDF页面重排, PDF顺序调整, PDF页面整理, PDF排序]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-reorder"
faq:
  - q: "调整顺序会降低画质吗？"
    a: "不会。页面只是被移动，不会重新渲染或压缩。"
  - q: "可以把最后一页移到最前面吗？"
    a: "可以。拖到第一位，或使用移动按钮，保存前可在预览中确认。"
  - q: "页面上印的页码会自动更新吗？"
    a: "不会。印在页面里的数字属于内容。顺序变化较大时，请用页码工具重新编号。"
related: [pdf-split, pdf-delete-pages, pdf-rotate, pdf-duplicate-pages]
---

把页面排回本该有的顺序。输入新序列——3, 1, 2, 5, 4——下载重建后的 PDF。

<!--more-->

{{< pdf-reorder >}}

## 工作原理

页面按你输入的序列复制进新文档；未列出的页面会被丢弃，重复编号则会复制该页。想整体反转用[页面倒序](/zh/tools/pdf-reverse-pages/)；想增加副本用[页面复制](/zh/tools/pdf-duplicate-pages/)。

## 使用提示

- 要保留的页面必须全部列出——漏写等于删除
- 重复写同一编号可在该位置复制该页
- 先用 [PDF 检查](/zh/tools/pdf-info/)确认总页数
