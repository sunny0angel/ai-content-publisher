---
title: "テキスト読み上げ（TTS）"
date: 2026-11-19
lastmod: 2026-11-19
description: "ブラウザ内蔵の音声でテキストを読み上げ、速度も調整。アップロードなしの無料ローカルツール。"
tags: [テキスト読み上げ, TTS, 音声合成, テキストリーダー]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "text-to-speech"
---

任意のテキストを貼り付けて、ブラウザ内蔵の音声で読み上げます——声と言語を選び、速度を調整。オフラインで動作し、アップロードなし、アカウント不要です。

<!--more-->

{{< text-to-speech >}}

## 仕組み

選択した声と速度でブラウザのSpeechSynthesis APIを駆動します。これは聴くためのツールで、音声ファイルはダウンロードされません。逆方向——自分の声を録る——は[録音ツール](/ja/tools/audio-recorder/)が担当します。
