---
title: "图片取色器"
date: 2026-11-19
lastmod: 2026-11-21
description: "点击图片任意像素复制 HEX 色值，并自动提取主色调。免费本地工具。"
tags: [图片取色, 从图片提取颜色, 调色板提取, hex取色]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-color-picker"
faq:
  - q: "图片会上传吗？"
    a: "不会。图片在本标签页绘制到 canvas，并用 getImageData 在本地读取像素值。"
  - q: "主色是怎么算的？"
    a: "先缩小图片，把像素归入颜色桶，再返回出现最多的 6 种颜色。因此大面积纯色会主导结果。"
  - q: "取色的 HEX 准确吗？"
    a: "取的是光标下那一像素的真实值。预览被缩小时细节不易点准，需要精确取色可先裁剪。"
related: [color-converter, image-cropper, image-compressor, image-to-base64]
---

上传图片，点击任意位置复制该像素的 HEX 色值，并自动提取六大主色调——用于品牌调色板、设计配色和 UI 主题。完全在浏览器内运行。

<!--more-->

{{< image-color-picker >}}

## 工作原理

点击坐标通过 `getImageData` 映射到 canvas 像素；调色板由降采样像素分桶后按频率排序得出。结果可配合[颜色转换器](/zh/tools/color-converter/)在 HEX、RGB、HSL 之间互转。
