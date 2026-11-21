---
title: "视频抽帧工具（缩略图）"
date: 2026-11-19
lastmod: 2026-11-21
description: "把视频任意一帧截取为 PNG——用于缩略图、封面和预览。文件不出本机的免费本地工具。"
tags: [视频缩略图, 视频抽帧, 视频截图, 视频转图片]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "video-thumbnail"
faq:
  - q: "截取的画面是什么格式？"
    a: "视频原始分辨率的 PNG。"
  - q: "为什么截出来是黑屏？"
    a: "可能跳转尚未完成，或解码器还没绘制该帧。在目标时间点暂停后再截取。"
  - q: "可以截多张吗？"
    a: "可以。拖动到其他时间再次截取，每次都会下载一个 PNG。"
  - q: "视频会上传吗？"
    a: "不会。解码与 canvas 截取都在标签页内完成。"
related: [video-info, video-extract-audio, image-cropper, image-compressor]
---

加载视频、拖到精确时刻、把那一帧截成 PNG——用于 YouTube 缩略图、视频封面和预览。完全在浏览器内运行。

<!--more-->

{{< video-thumbnail >}}

## 工作原理

工具把当前视频帧绘制到 canvas 并导出。技巧：部分浏览器播放中截取比暂停状态更可靠。截取后用[图片裁剪器](/zh/tools/image-cropper/)和[图片尺寸调整器](/zh/tools/image-resizer/)做裁剪缩放。
