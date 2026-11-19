---
title: "画像カラーピッカー"
date: 2026-11-19
lastmod: 2026-11-19
description: "画像の任意のピクセルをクリックしてHEX色をコピーし、メインカラーを自動抽出。無料ローカルツール。"
tags: [画像カラーピッカー, 画像から色抽出, カラーパレット抽出, hexカラー]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-color-picker"
---

画像をアップロードし、任意の場所をクリックしてピクセルのHEX色をコピー、さらに6つのメインカラーを自動抽出——ブランドパレット、デザイン合わせ、UIテーマに。完全にブラウザ内で動作します。

<!--more-->

{{< image-color-picker >}}

## 仕組み

クリック座標を `getImageData` でキャンバスのピクセルに対応付けます。パレットはダウンサンプリングしたピクセルをバケット化し、頻度上位の色を抽出します。結果は[カラーコンバーター](/ja/tools/color-converter/)でHEX・RGB・HSL間を変換できます。
