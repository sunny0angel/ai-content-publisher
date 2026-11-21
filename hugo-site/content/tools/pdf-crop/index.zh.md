---
title: "PDF 裁切边距"
date: 2026-11-20
lastmod: 2026-11-21
description: "按百分比裁掉 PDF 页面四周的白边——上、右、下、左分别设置。本地、免费、不上传。"
tags: [PDF裁切, PDF白边, PDF修剪, PDF裁剪工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-crop"
faq:
  - q: "裁剪会删除画面外的内容吗？"
    a: "工具修改的是可见区域（CropBox），裁剪框外的内容被隐藏而非删除，所以文件大小几乎不变。"
  - q: "可以每页裁剪不同区域吗？"
    a: "可以。既能对全部页面套用同一裁剪框，也能在扫描页边距不一致时逐页设置。"
  - q: "为什么裁剪后文件没变小？"
    a: "因为被隐藏的内容仍保存在文件里。要真正减小体积，请用 PDF 压缩工具。"
related: [pdf-resize, pdf-rotate, pdf-n-up, pdf-compress]
---

裁掉 PDF 页面四周多余的空白——为每条边设置百分比，下载更贴合内容的文档。

<!--more-->

{{< pdf-crop >}}

## 工作原理

裁切设置每页的 CropBox：框外内容在阅读器中隐藏、打印时排除，但不会从文件中删除，因此可逆且非破坏性。要改变实际纸张尺寸，请用 [PDF 尺寸调整](/zh/tools/pdf-resize/)。

## 使用提示

- 扫描件边距过大时，每边先试 5%
- 裁切只改可见区域——把数值调回 0% 即可恢复
- 部分打印对话框会忽略 CropBox，先用一页测试
