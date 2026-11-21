---
title: "PDF 转 JPG"
date: 2026-11-20
lastmod: 2026-11-21
description: "把 PDF 页面渲染成 96、150 或 300 DPI 的 JPG——逐页预览并下载。免费本地，不上传。"
tags: [PDF转JPG, PDF转图片, PDF转JPEG, PDF页面图片]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-to-jpg"
faq:
  - q: "导出的图片分辨率是多少？"
    a: "可自选倍率（1x–4x）。屏幕使用 2x 通常足够，打印或 OCR 建议 3x–4x。"
  - q: "为什么日文/中文 PDF 有时缺字？"
    a: "CJK 字体需要内嵌或通过 CMap 建立映射。本工具从本地加载标准 CMap；若字体是缺少映射的子集，字符可能显示为空白。"
  - q: "可以只转换一页吗？"
    a: "可以。输入单页或范围，不必导出整个文档。"
  - q: "渲染需要上传文件吗？"
    a: "不需要。PDF.js 在本标签页的 canvas 上渲染，图片在本地生成并打包为 ZIP 下载。"
related: [pdf-compress, images-to-pdf, pdf-crop, pdf-info]
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
