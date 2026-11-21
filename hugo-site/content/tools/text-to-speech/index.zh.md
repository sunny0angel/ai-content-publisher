---
title: "文字转语音（TTS）"
date: 2026-11-19
lastmod: 2026-11-21
description: "用浏览器内置声音朗读任意文本，语速可调。无上传的免费本地工具。"
tags: [文字转语音, TTS, 语音合成, 文本朗读]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "text-to-speech"
faq:
  - q: "有哪些语音可用？"
    a: "浏览器和操作系统已安装的语音。Chrome、Edge、macOS 和 Windows 提供的集合不同，部分平台语音依赖云端。"
  - q: "文本会上传吗？"
    a: "Web Speech API 通常在本地运行，但某些语音使用网络服务。不确定时请不要粘贴机密文本。"
  - q: "可以下载音频吗？"
    a: "不能。该 API 只播放，不提供文件；需要音频文件请用录音工具。"
  - q: "为什么语音列表是空的？"
    a: "语音异步加载。请稍等或刷新；部分浏览器要在首次交互后才会填充列表。"
related: [audio-recorder, audio-speed, audio-waveform, video-extract-audio]
---

粘贴任意文本，用浏览器内置声音朗读——选择声音和语言、调节语速。离线可用、不上传任何内容、无需账号。

<!--more-->

{{< text-to-speech >}}

## 工作原理

工具以你选择的声音和语速驱动浏览器的 SpeechSynthesis API。它是试听工具，不会下载音频文件。反方向——录自己的声音——用[在线录音器](/zh/tools/audio-recorder/)。
