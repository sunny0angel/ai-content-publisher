---
title: "画像をBase64に変換"
date: 2026-11-19
lastmod: 2026-11-19
description: "画像をHTML/CSSに直接埋め込めるBase64 Data URLへ変換。アップロードなしの無料ローカルツール。"
tags: [画像からBase64, Data URL生成, base64画像, HTML画像埋め込み]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "image-to-base64"
---

画像を `data:image/...;base64,...` URLに変換し、HTMLの `src` 属性やCSSの `background-image` にそのまま貼り付けられます——別ファイルもサーバーリクエストも不要。完全にブラウザ内で動作します。

<!--more-->

{{< image-to-base64 >}}

## 仕組み

ブラウザがファイルを読み取り、バイト列をBase64でエンコードします（[Base64エンコーダー](/ja/tools/base64-encoder/)の背後と同じエンコード）。埋め込みは生ファイルより約33%大きくなるため、Data URLは写真ではなくアイコンやプレビューサムネイルなど小さなアセットに向いています。
