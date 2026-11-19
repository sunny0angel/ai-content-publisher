---
title: "画像回転・反転ツール"
date: 2026-11-19
lastmod: 2026-11-19
description: "画像を左右90°回転、水平・垂直反転してダウンロード。ファイルがマシンの外に出ない無料ローカルツール。"
tags: [画像回転, 画像反転, 写真回転, ミラー反転]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-rotator"
---

横向きに撮れた写真を修正——左右90°回転、水平・垂直反転してダウンロード。すべての操作はブラウザ内のキャンバスで行われ、ファイルがマシンの外に出ることはありません。

<!--more-->

{{< image-rotator >}}

## 仕組み

回転と反転は、デコード済み画像にキャンバスの座標変換を適用してPNGに再エンコードします。編集チェーンの残り——切り取りとリサイズ——は[画像切り取り](/ja/tools/image-cropper/)と[画像リサイズ](/ja/tools/image-resizer/)を。
