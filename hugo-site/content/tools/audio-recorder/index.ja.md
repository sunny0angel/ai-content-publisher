---
title: "オンライン録音ツール"
date: 2026-11-19
lastmod: 2026-11-19
description: "ブラウザ内でマイクから録音し、ダウンロード。録音がマシンの外に出ない無料ローカルツール。"
tags: [録音, 音声録音, ボイスレコーダー, マイク録音]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "audio-recorder"
---

ワンクリックでマイクから録音し、再生してダウンロード。音声は完全にブラウザ内でキャプチャ・保存され、どこにもアップロードされません。

<!--more-->

{{< audio-recorder >}}

## 仕組み

MediaRecorder APIでマイクのストリームをWebM blobにキャプチャします。出力形式はWebM（ブラウザ依存）。MP3が必要なら別途変換を。再生速度の調整は[音声変速プレーヤー](/ja/tools/audio-speed/)が担当します。
