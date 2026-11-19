---
title: "動画から音声抽出"
date: 2026-11-19
lastmod: 2026-11-19
description: "任意の動画ファイルから音声トラックを抽出してダウンロード。ファイルがマシンの外に出ない無料ローカルツール。"
tags: [動画から音声, 音声抽出, 動画からmp3, 動画音声抽出]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "video-extract-audio"
---

動画ファイルから音声を取り出してダウンロード。動画の再生に合わせてリアルタイムに録音する方式で、アップロードは一切なく、出力はWebM音声ファイルです。

<!--more-->

{{< video-extract-audio >}}

## 仕組み

動画の音声をWeb Audioグラフ経由でMediaRecorderに流し、再生しながらキャプチャします——そのため抽出には動画の長さと同じ時間がかかります。その後の再生調整は[音声変速プレーヤー](/ja/tools/audio-speed/)と[波形ビューアー](/ja/tools/audio-waveform/)がオーディオツールキットを完成させます。
