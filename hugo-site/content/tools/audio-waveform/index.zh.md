---
title: "音频波形可视化器"
date: 2026-11-19
lastmod: 2026-11-19
description: "任意音频文件播放时显示实时频率柱状图。基于 Web Audio API 的免费本地工具。"
tags: [音频可视化, 波形可视化, 音频频谱, 音乐可视化]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "audio-waveform"
---

加载音频文件，看着实时频率柱随播放舞动——基于 Web Audio AnalyserNode 的彩色频谱。完全在浏览器内运行。

<!--more-->

{{< audio-waveform >}}

## 工作原理

AnalyserNode 提供实时频率数据，工具将其按频谱变色绘制成 canvas 柱状图。它是可视化器而非编辑器——速度与音调控制用[音频变速播放器](/zh/tools/audio-speed/)，录制自己的声音用[在线录音器](/zh/tools/audio-recorder/)。
