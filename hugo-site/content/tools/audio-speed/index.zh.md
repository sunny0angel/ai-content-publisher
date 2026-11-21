---
title: "音频变速与变调播放器"
date: 2026-11-19
lastmod: 2026-11-21
description: "以 0.5 到 2 倍速播放任意音频，并经 Web Audio 实时调节音调。面向语言学习与复习的免费本地工具。"
tags: [音频变速, 慢速播放, 倍速播放, 语言学习工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "audio-speed"
faq:
  - q: "改变速度会变调吗？"
    a: "现代浏览器在改变播放速率时默认保持音调，因此 0.7 倍或 1.5 倍时语音仍然清晰。"
  - q: "支持哪些格式？"
    a: "MP3、WAV、M4A/AAC、OGG，通常还有 WebM——只要是浏览器能解码的格式。不支持的编码会加载失败，请先转换。"
  - q: "可以导出变速后的音频吗？"
    a: "不能。这是播放器，不是导出工具。确认效果后请用音频软件处理。"
  - q: "文件会上传吗？"
    a: "不会。播放完全在标签页内进行。"
related: [audio-waveform, audio-recorder, text-to-speech, video-extract-audio]
---

加载任意音频文件，实时把播放速度从 0.5 倍调到 2 倍——语言学习（放慢听清每个词）或快速复习录音都合适。通过 Web Audio API 完全在浏览器内运行。

<!--more-->

{{< audio-speed >}}

## 工作原理

播放速度走媒体元素的 `playbackRate`；音调滑杆走 Web Audio 图。注意浏览器默认会随速度改变音调——音调滑杆让你进一步微调。想「看见」你听到的内容，配合[音频波形可视化](/zh/tools/audio-waveform/)。
