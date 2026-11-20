---
title: "PDF 拆分与提取页面"
date: 2026-11-20
lastmod: 2026-11-20
description: "把 PDF 中指定的页面提取成新文件。支持 1-3, 5, 7-9 这样的范围。不上传、不注册、无页数限制。"
tags: [PDF拆分, PDF提取页面, PDF页面提取, PDF分割]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-split"
---

只把你需要的页面——签字页、附录、某一章——提取成干净的新 PDF。输入 1-3, 5, 7-9 这样的范围，只下载这些页。

<!--more-->

{{< pdf-split >}}

## 工作原理

工具读取总页数，只保留你列出的索引，并按给定顺序复制进新文档。原文件不会被修改。如果要删除页面，请用[删除页面](/zh/tools/pdf-delete-pages/)；要合并文件，请用 [PDF 合并](/zh/tools/pdf-merge/)。

## 使用提示

- 页码从 1 开始，与阅读器显示一致
- 范围可以重复或重排——3, 1, 1 表示第 3 页后接两次第 1 页
- 加密 PDF 需先移除密码再拆分
