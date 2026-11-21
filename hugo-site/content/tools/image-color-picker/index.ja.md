---
title: "画像カラーピッカー"
date: 2026-11-19
lastmod: 2026-11-21
description: "画像の任意のピクセルをクリックしてHEX色をコピーし、メインカラーを自動抽出。無料ローカルツール。"
tags: [画像カラーピッカー, 画像から色抽出, カラーパレット抽出, hexカラー]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-color-picker"
faq:
  - q: "画像はアップロードされますか？"
    a: "いいえ。このタブ内でcanvasに描画し、getImageDataでピクセル値をローカルに読み取ります。"
  - q: "主要色はどう計算されますか？"
    a: "画像を縮小し、ピクセルを色のバケットにまとめて上位6色を返します。面積の大きい平坦な領域が結果を支配します。"
  - q: "HEX値の精度は？"
    a: "カーソル下のピクセルそのものです。プレビューが縮小表示される場合、細部はクリックしにくいため、必要なら事前にトリミングしてください。"
related: [color-converter, image-cropper, image-compressor, image-to-base64]
---

画像をアップロードし、任意の場所をクリックしてピクセルのHEX色をコピー、さらに6つのメインカラーを自動抽出——ブランドパレット、デザイン合わせ、UIテーマに。完全にブラウザ内で動作します。

<!--more-->

{{< image-color-picker >}}

## 仕組み

クリック座標を `getImageData` でキャンバスのピクセルに対応付けます。パレットはダウンサンプリングしたピクセルをバケット化し、頻度上位の色を抽出します。結果は[カラーコンバーター](/ja/tools/color-converter/)でHEX・RGB・HSL間を変換できます。
