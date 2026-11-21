---
title: "在线录音器"
date: 2026-11-19
lastmod: 2026-11-21
description: "在浏览器内从麦克风录音并下载。录音不出本机的免费本地工具。"
tags: [在线录音, 录音器, 语音录制, 麦克风录音]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "audio-recorder"
faq:
  - q: "录音保存在哪里？"
    a: "在你下载之前只存在于本标签页内存中。不会上传，未保存就关闭页面会丢失。"
  - q: "下载是什么格式？"
    a: "Opus 编码的 WebM 音频，浏览器和多数编辑软件都支持。平台要求时可转成 MP3。"
  - q: "为什么麦克风被阻止？"
    a: "浏览器要求 HTTPS 和明确授权。在地址栏允许麦克风；此前拒绝过的话，请重置站点权限。"
  - q: "能录制系统声音吗？"
    a: "只能录麦克风。录制标签页或系统声音需要屏幕录制工具。"
related: [audio-speed, audio-waveform, text-to-speech, video-extract-audio]
---

一键从麦克风录音、回放并下载。音频完全在浏览器内捕获和保存——不会上传到任何地方。

<!--more-->

{{< audio-recorder >}}

## 工作原理

工具用 MediaRecorder API 把麦克风流捕获为 WebM blob。输出格式为 WebM（依浏览器而定）；需要 MP3 请另行转码。播放速度调整交给[音频变速播放器](/zh/tools/audio-speed/)。
