---
title: "图片旋转与翻转工具"
date: 2026-11-19
lastmod: 2026-11-19
description: "图片左右旋转 90°、水平或垂直翻转并下载。文件不出本机的免费本地工具。"
tags: [图片旋转, 图片翻转, 照片旋转90度, 镜像翻转]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-rotator"
---

修正横着拍的手机照片：左右旋转 90°、水平或垂直翻转、下载。所有操作都在浏览器 canvas 内完成——文件不会离开你的电脑。

<!--more-->

{{< image-rotator >}}

## 工作原理

旋转与翻转是对解码后图片应用 canvas 坐标变换，再编码为 PNG。编辑链的其余部分——裁剪与缩放——用[图片裁剪器](/zh/tools/image-cropper/)和[图片尺寸调整器](/zh/tools/image-resizer/)。
