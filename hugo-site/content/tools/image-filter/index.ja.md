---
title: "画像フィルター・調整ツール"
date: 2026-11-19
lastmod: 2026-11-19
description: "グレースケール、セピア、反転、ぼかしフィルターと明るさ・コントラスト調整。ファイルがマシンの外に出ない無料ローカルツール。"
tags: [画像フィルター, グレースケール, セピア, 写真編集, 明るさコントラスト]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-filter"
---

グレースケール、セピア、反転、ぼかしのフィルターを適用し、明るさとコントラストをスライダーで調整してダウンロード。すべてブラウザ内のキャンバスフィルターで動作します。

<!--more-->

{{< image-filter >}}

## 仕組み

CSSスタイルのキャンバスフィルター（`brightness()`、`contrast()`、`grayscale()` など）を1回の描画に合成し、JPEGとして書き出します。モザイクなどピクセル単位の効果は[画像ピクセル化](/ja/tools/image-pixelator/)が担当します。
