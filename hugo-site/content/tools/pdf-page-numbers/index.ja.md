---
title: "PDFにページ番号を追加"
date: 2026-11-20
lastmod: 2026-11-20
description: "PDFの全ページにページ番号を押印——位置、開始番号、文字サイズ、「X / Y」形式に対応。無料・ローカル・アップロード不要。"
tags: [PDF ページ番号, ページ番号 追加, PDF ノンブル, PDF ページ付け]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-page-numbers"
---

ページ番号のないPDFに番号を追加——下または上、左・中央・右、任意で「X / Y」の総ページ数付き。再描画なし、アップロードなし。

<!--more-->

{{< pdf-page-numbers >}}

## 仕組み

標準Helveticaフォントのベクター文字として、各ページ端から余白を取って描画するため、どのサイズでも鮮明に印刷されます。既存内容は再エンコードされません。透かしも必要な場合は[透かし追加](/ja/tools/pdf-watermark/)と併用を。

## 補足

- 表紙を数えたくない場合は0から開始
- 表紙を除いて番号を振るなら、先に[ページ削除](/ja/tools/pdf-delete-pages/)で外し、後で結合し直す
- 総ページ数はこのファイル内のページ数のみ
