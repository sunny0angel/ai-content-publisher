---
title: "音声波形ビジュアライザー"
date: 2026-11-19
lastmod: 2026-11-19
description: "任意の音声ファイルの再生に合わせてライブの周波数バーを表示。Web Audio API製の無料ローカルツール。"
tags: [音声ビジュアライザー, 波形表示, オーディオスペクトラム, 音楽ビジュアライザー]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "audio-waveform"
---

音声ファイルを読み込むと、再生に合わせてライブの周波数バーが踊ります——Web AudioのAnalyserNodeで作られたカラフルなスペクトラムです。完全にブラウザ内で動作します。

<!--more-->

{{< audio-waveform >}}

## 仕組み

AnalyserNodeがリアルタイムの周波数データを提供し、ツールがそれをキャンバスにスペクトラム全体で色を変えながらバーとして描画します。これはビジュアライザーであってエディターではありません——速度とピッチの制御は[音声変速プレーヤー](/ja/tools/audio-speed/)、自分の入力を録るなら[録音ツール](/ja/tools/audio-recorder/)を。
