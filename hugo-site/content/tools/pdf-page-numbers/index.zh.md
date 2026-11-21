---
title: "给 PDF 添加页码"
date: 2026-11-20
lastmod: 2026-11-21
description: "为 PDF 每页盖页码——可选位置、起始编号、字号和「X / Y」格式。免费、本地、不上传。"
tags: [PDF添加页码, PDF页码, PDF编页, PDF页脚]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-page-numbers"
faq:
  - q: "可以从 1 以外的数字开始吗？"
    a: "可以。设置起始编号和首个盖章页，封面就能保持无页码。"
  - q: "页码位置可以选吗？"
    a: "可以。支持底部居中、右下、右上等位置，并可设置字号与边距，所选页面统一应用。"
  - q: "页码是可搜索的文字吗？"
    a: "是。页码以真实文字写入页面，可选中、可搜索，不同于图片印章。"
related: [pdf-watermark, pdf-n-up, pdf-blank-pages, pdf-merge]
---

给没有页码的 PDF 加上页码——页脚或页眉，左中右可选，还能显示「X / Y」总页数。不重新渲染，不上传。

<!--more-->

{{< pdf-page-numbers >}}

## 工作原理

用标准 Helvetica 字体以矢量文字绘制，并与页面边缘留出间距，任何尺寸打印都清晰。原有内容不重新编码。若还需要水印，可配合[添加水印](/zh/tools/pdf-watermark/)。

## 使用提示

- 封面不想计数时，起始编号设为 0
- 若编号要跳过封面，先用[删除页面](/zh/tools/pdf-delete-pages/)去掉，之后再合并回来
- 总页数只统计本文件内的页面
