---
title: "PDFページ削除"
date: 2026-11-20
lastmod: 2026-11-20
description: "PDFから不要なページを削除して保存。残りのページはそのまま——すべてブラウザ内で処理。"
tags: [PDF ページ削除, PDF ページ取り除き, PDF 不要ページ, PDF編集]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-delete-pages"
---

空白のスキャン、古い条項、誤って挿入されたページをPDFから取り除きます。削除するページを指定し、それ以外はそのままにして保存します。

<!--more-->

{{< pdf-delete-pages >}}

## 仕組み

指定したページ以外をすべて新しいPDFへコピーし、内容と順序を保ちます。墨消しや再エンコードは行いません。逆に特定ページだけ残したい場合は[PDF分割](/ja/tools/pdf-split/)を使います。

## 補足

- 範囲指定でまとめて削除: 2, 4-6 は2ページ目と4〜6ページ目
- 破壊的編集の前に必ず元ファイルを保存
- スキャンPDFなら削除後に[PDF圧縮](/ja/tools/pdf-compress/)を
