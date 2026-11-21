---
title: "動画から音声抽出"
date: 2026-11-19
lastmod: 2026-11-21
description: "任意の動画ファイルから音声トラックを抽出してダウンロード。ファイルがマシンの外に出ない無料ローカルツール。"
tags: [動画から音声, 音声抽出, 動画からmp3, 動画音声抽出]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "video-extract-audio"
faq:
  - q: "抽出の仕組みは？"
    a: "動画を実時間で再生し、MediaRecorderで音声を録音します。10分の動画なら約10分かかります。"
  - q: "音声の形式は？"
    a: "OpusのWebM音声です。必要に応じてMP3やM4Aに変換してください。"
  - q: "最後まで再生せずに抽出できますか？"
    a: "できません。実時間キャプチャには再生が必要で、サーバー側のdemuxerは使いません。"
  - q: "動画はアップロードされますか？"
    a: "いいえ。再生と録音はこのタブ内で行われます。"
related: [video-info, video-thumbnail, audio-recorder, audio-speed]
---

動画ファイルから音声を取り出してダウンロード。動画の再生に合わせてリアルタイムに録音する方式で、アップロードは一切なく、出力はWebM音声ファイルです。

<!--more-->

{{< video-extract-audio >}}

## 仕組み

動画の音声をWeb Audioグラフ経由でMediaRecorderに流し、再生しながらキャプチャします——そのため抽出には動画の長さと同じ時間がかかります。その後の再生調整は[音声変速プレーヤー](/ja/tools/audio-speed/)と[波形ビューアー](/ja/tools/audio-waveform/)がオーディオツールキットを完成させます。
