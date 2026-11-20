---
title: "画像→PDF変換"
date: 2026-11-20
lastmod: 2026-11-20
description: "JPG・PNG画像を1ページ1枚のPDFに変換。自動フィット、無料・ローカル——写真はアップロードされません。"
tags: [画像 PDF 変換, JPG PDF, PNG PDF, 写真 PDF, 画像結合]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "images-to-pdf"
---

スマホ写真、スキャンページ、書き出したスクリーンショットを1つのPDFに——1ページ1画像、中央揃えで歪みなくフィット。

<!--more-->

{{< images-to-pdf >}}

## 仕組み

各画像をフル解像度で埋め込み、選んだページサイズに縦横比を保って縮小します。JPGとPNGに対応し、PNGの透過は保持されます。既存PDFとまとめる場合は[PDF結合](/ja/tools/pdf-merge/)へ。

## 補足

- ページにしたい順番で画像を選択
- A4縦は書類向き、A4横はスライドや横長写真向き
- 20MBのスマホ写真は先に[画像圧縮](/ja/tools/image-compressor/)で
