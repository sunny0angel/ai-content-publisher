---
title: "视频提取音频工具"
date: 2026-11-19
lastmod: 2026-11-19
description: "从任意视频文件中提取音轨并下载。文件不出本机的免费本地工具。"
tags: [视频转音频, 提取音频, 视频转mp3, 视频音轨提取]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "video-extract-audio"
---

把视频里的音频抽出来下载。工具随视频播放实时录制音频——不会上传任何内容，输出为 WebM 音频文件。

<!--more-->

{{< video-extract-audio >}}

## 工作原理

视频音频经 Web Audio 图送入 MediaRecorder，边播放边捕获——因此提取耗时与视频等长。之后的播放调节交给[音频变速播放器](/zh/tools/audio-speed/)和[波形可视化器](/zh/tools/audio-waveform/)，凑齐音频工具链。
