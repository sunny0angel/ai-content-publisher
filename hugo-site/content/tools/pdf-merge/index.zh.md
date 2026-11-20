---
title: "PDF 合并"
date: 2026-11-20
lastmod: 2026-11-20
description: "按你选择的顺序把多个 PDF 合并成一个文件。不上传、不注册、无水印——全部在浏览器内完成。"
tags: [PDF合并, PDF合并工具, 多个PDF合并, PDF拼接]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-merge"
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
