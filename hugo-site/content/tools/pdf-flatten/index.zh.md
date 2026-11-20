---
title: "扁平化 PDF 表单"
date: 2026-11-20
lastmod: 2026-11-20
description: "把可填写的 PDF 表单字段固化为固定内容，数值不再被修改。免费本地，不上传。"
tags: [PDF表单扁平化, 固定PDF表单, 锁定PDF表单, 可填写PDF]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-flatten"
---

把可填写的 PDF 变成固定文档：表单数值烘焙进页面，无法再编辑、切换字段或被其他阅读器重置。

<!--more-->

{{< pdf-flatten >}}

## 工作原理

pdf-lib 枚举 AcroForm 字段后扁平化为页面内容。若 PDF 没有表单字段，工具会明确提示，而不是输出一个一模一样的文件。这不是加密——页面内容仍可用 PDF 编辑器修改，但表单结构已消失。

## 使用提示

- 填写或签署完成的表单，归档前先扁平化
- 扁平化后的数值在各阅读器中显示和打印一致
- 如果以后还要改数值，保留一份未扁平化的副本
