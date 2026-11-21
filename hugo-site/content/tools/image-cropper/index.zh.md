---
title: "图片裁剪器"
date: 2026-11-19
lastmod: 2026-11-21
description: "用预设宽高比（1:1、4:3、16:9）和位置控制裁剪图片。文件不出本机的免费本地工具。"
tags: [图片裁剪, 照片裁剪, 宽高比裁剪, 方形裁剪]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-cropper"
faq:
  - q: "裁剪会降低画质吗？"
    a: "裁剪本身无损：所选区域复制到 canvas 后以 PNG 导出，这一步不会劣化。"
  - q: "能按精确像素裁剪吗？"
    a: "工具使用比例预设和相对大小滑块。需要精确宽高时，先裁剪再用图片缩放工具。"
  - q: "会修改原文件吗？"
    a: "不会。只下载新的 PNG，磁盘上的原文件保持不变。"
related: [image-resizer, image-rotator, image-compressor, image-color-picker]
---

用预设宽高比裁剪任意图片——头像用 1:1、幻灯片用 4:3、封面用 16:9——并带中心位置和裁剪大小滑杆。结果以 PNG 下载。完全在浏览器内运行。

<!--more-->

{{< image-cropper >}}

## 工作原理

工具根据比例、大小和中心位置滑杆计算裁剪窗口，再把该区域复制到新 canvas。裁剪后的精确尺寸用[图片尺寸调整器](/zh/tools/image-resizer/)，文件体积用[图片压缩器](/zh/tools/image-compressor/)。
