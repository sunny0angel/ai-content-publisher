---
title: "视频信息查看器"
date: 2026-11-19
lastmod: 2026-11-21
description: "在浏览器本地读取视频的分辨率、时长和文件大小。无上传的免费工具。"
tags: [视频信息, 视频元数据, 视频分辨率查询, 视频时长]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "video-info"
faq:
  - q: "会读取哪些信息？"
    a: "浏览器报告的分辨率、时长、文件大小和文件类型。"
  - q: "视频会上传吗？"
    a: "不会。元数据在标签页内从本地文件读取。"
  - q: "为什么时长显示 0 或 Infinity？"
    a: "部分 WebM 和 MKV 没有时长头。转成 MP4 可获得可靠元数据。"
  - q: "能显示编码或码率吗？"
    a: "不能。浏览器只暴露基础信息；编码、码率和帧率请用 ffprobe。"
related: [video-thumbnail, video-extract-audio, audio-waveform, image-resizer]
---

选择视频，即刻看到分辨率、时长和文件大小——上传或转码前需要的元信息。在浏览器本地读取，文件不会被上传。

<!--more-->

{{< video-info >}}

## 工作原理

视频加载时浏览器直接读取容器元数据。视频「传不上去」时，原因通常是大小或时长——试之前在这里就能看到。配合[视频抽帧工具](/zh/tools/video-thumbnail/)还能顺便预览内容。
