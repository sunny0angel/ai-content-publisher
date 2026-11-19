---
title: "在线录音器"
date: 2026-11-19
lastmod: 2026-11-19
description: "在浏览器内从麦克风录音并下载。录音不出本机的免费本地工具。"
tags: [在线录音, 录音器, 语音录制, 麦克风录音]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "audio-recorder"
---

一键从麦克风录音、回放并下载。音频完全在浏览器内捕获和保存——不会上传到任何地方。

<!--more-->

{{< audio-recorder >}}

## 工作原理

工具用 MediaRecorder API 把麦克风流捕获为 WebM blob。输出格式为 WebM（依浏览器而定）；需要 MP3 请另行转码。播放速度调整交给[音频变速播放器](/zh/tools/audio-speed/)。
