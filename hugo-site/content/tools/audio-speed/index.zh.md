---
title: "音频变速与变调播放器"
date: 2026-11-19
lastmod: 2026-11-19
description: "以 0.5 到 2 倍速播放任意音频，并经 Web Audio 实时调节音调。面向语言学习与复习的免费本地工具。"
tags: [音频变速, 慢速播放, 倍速播放, 语言学习工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "audio-speed"
---

加载任意音频文件，实时把播放速度从 0.5 倍调到 2 倍——语言学习（放慢听清每个词）或快速复习录音都合适。通过 Web Audio API 完全在浏览器内运行。

<!--more-->

{{< audio-speed >}}

## 工作原理

播放速度走媒体元素的 `playbackRate`；音调滑杆走 Web Audio 图。注意浏览器默认会随速度改变音调——音调滑杆让你进一步微调。想「看见」你听到的内容，配合[音频波形可视化](/zh/tools/audio-waveform/)。
