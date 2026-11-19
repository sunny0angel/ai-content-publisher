---
title: "图片取色器"
date: 2026-11-19
lastmod: 2026-11-19
description: "点击图片任意像素复制 HEX 色值，并自动提取主色调。免费本地工具。"
tags: [图片取色, 从图片提取颜色, 调色板提取, hex取色]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-color-picker"
---

上传图片，点击任意位置复制该像素的 HEX 色值，并自动提取六大主色调——用于品牌调色板、设计配色和 UI 主题。完全在浏览器内运行。

<!--more-->

{{< image-color-picker >}}

## 工作原理

点击坐标通过 `getImageData` 映射到 canvas 像素；调色板由降采样像素分桶后按频率排序得出。结果可配合[颜色转换器](/zh/tools/color-converter/)在 HEX、RGB、HSL 之间互转。
