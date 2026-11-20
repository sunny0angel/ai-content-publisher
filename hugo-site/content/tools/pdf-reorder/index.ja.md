---
title: "PDFページ並べ替え"
date: 2026-11-20
lastmod: 2026-11-20
description: "PDFのページを任意の順序に並べ替え——新しい順序を入力してダウンロード。ローカル・無料・アップロード不要。"
tags: [PDF ページ並べ替え, PDF 順序変更, PDF ページ整理, PDF 並び替え]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-reorder"
---

本来あるべき順序にページを直します。3, 1, 2, 5, 4 のように新しい順序を入力して、再構築したPDFをダウンロード。

<!--more-->

{{< pdf-reorder >}}

## 仕組み

入力した順序どおりにページを新しい文書へコピーします。記載しないページは削除され、同じ番号を繰り返せば複製されます。全体を逆順にするなら[ページ順反転](/ja/tools/pdf-reverse-pages/)、コピーを増やすなら[ページ複製](/ja/tools/pdf-duplicate-pages/)を。

## 補足

- 残したいページはすべて列挙——漏れたページは削除されます
- 同じ番号を繰り返すとその位置に複製
- 先に[PDF検査](/ja/tools/pdf-info/)でページ数を確認
