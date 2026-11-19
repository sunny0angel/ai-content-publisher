---
title: "图片尺寸调整器"
date: 2026-11-19
lastmod: 2026-11-19
description: "按宽度、高度或百分比调整图片尺寸。文件不出本机的免费本地工具。"
tags: [图片尺寸调整, 改变图片大小, 照片缩放]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-resizer"
---

设置目标宽度、高度或百分比，即刻调整任意图片的尺寸。输出以 PNG 下载；需要控制格式请配合[图片格式转换](/zh/tools/image-converter/)。完全在浏览器内运行。

<!--more-->

{{< image-resizer >}}

## 工作原理

工具把图片按目标尺寸绘制到 canvas。填宽度**或**高度即可等比缩放，也可以填百分比（100 = 不变）。调整尺寸后的质量与体积优化，交给[图片压缩器](/zh/tools/image-compressor/)。
