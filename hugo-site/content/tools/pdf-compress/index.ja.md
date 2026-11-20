---
title: "PDF圧縮（ブラウザ内）"
date: 2026-11-20
lastmod: 2026-11-20
description: "PDFページを72〜150 DPIで再描画し、JPEG画質を調整してファイルを縮小。ローカル、アップロード不要、ファイル制限なし。"
tags: [PDF 圧縮, PDF サイズ 縮小, PDF 軽量化, PDF ファイルサイズ]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-compress"
---

ページを制御可能な解像度と画質のJPEGとして再描画し、PDFのファイルサイズを削減——圧縮前後のサイズを比較できます。

<!--more-->

{{< pdf-compress >}}

## 仕組み

PDF.jsが各ページをcanvasに描画し、そのJPEGをpdf-libで元のページ寸法の新しいPDFに埋め込みます。スキャンや画像中心の資料に最適です。文字はラスタライズされるため選択・検索できなくなります——元ファイルを置き換える前に結果を確認してください。純粋なベクター削減には[N-up](/ja/tools/pdf-n-up/)や[ページ削除](/ja/tools/pdf-delete-pages/)を。

## 補足

- 110 DPI・画質65%でスキャンは通常50〜80%削減
- メール用プレビューは72 DPI、文字の可読性が必要なら150 DPI
- 再構築後の方が大きい場合、元ファイルはすでに効率的に符号化されています
