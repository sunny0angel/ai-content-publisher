---
title: "PDF 转 JPG"
date: 2026-11-20
lastmod: 2026-11-20
description: "把 PDF 页面渲染成 96、150 或 300 DPI 的 JPG——逐页预览并下载。免费本地，不上传。"
tags: [PDF转JPG, PDF转图片, PDF转JPEG, PDF页面图片]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-to-jpg"
---

把 PDF 页面变成 96、150 或 300 DPI 的 JPG——逐页预览，可单张或全部下载。渲染在浏览器内完成。

<!--more-->

{{< pdf-to-jpg >}}

## 工作原理

PDF.js 把每页绘制到 canvas，再按所选质量编码为 JPEG。文字会变成像素，因此适合预览、幻灯片和扫描件，不适合编辑。以文字为主的 PDF 应保持 PDF，并用 [PDF 压缩](/zh/tools/pdf-compress/)处理。

## 使用提示

- 150 DPI 是屏幕分享和文档的平衡点
- 打印用 300 DPI，但文件更大、渲染更慢
- 有密码的 PDF 需先解锁
