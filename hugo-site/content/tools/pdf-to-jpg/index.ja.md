---
title: "PDF→JPG変換"
date: 2026-11-20
lastmod: 2026-11-20
description: "PDFページを96・150・300 DPIのJPG画像に変換——プレビューと個別ダウンロード。無料・ローカル・アップロード不要。"
tags: [PDF JPG 変換, PDF 画像化, PDF JPEG, PDF ページ 画像]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-to-jpg"
---

PDFページを96・150・300 DPIのJPG画像に——全ページをプレビューし、個別または一括でダウンロード。描画はブラウザ内で行われます。

<!--more-->

{{< pdf-to-jpg >}}

## 仕組み

PDF.jsが各ページをcanvasに描画し、選んだ画質でJPEGにエンコードします。文字はピクセルになるため、プレビュー、スライド、スキャン文書向けで、編集には向きません。文字中心のPDFはPDFのまま[PDF圧縮](/ja/tools/pdf-compress/)を使うのが適切です。

## 補足

- 画面共有や書類には150 DPIが最適
- 印刷用は300 DPI、ただし大きいファイルと遅い描画に注意
- パスワード保護PDFは先に解除してください
