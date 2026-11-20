---
title: "PDF結合"
date: 2026-11-20
lastmod: 2026-11-20
description: "複数のPDFを選んだ順番のまま1つのファイルに結合。アップロード不要、登録不要、透かしなし——すべてブラウザ内で完結。"
tags: [PDF結合, PDF まとめる, 複数PDF 結合, PDFマージ]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-merge"
---

2つ以上のPDFを、選んだ順番のまま1つの文書に結合します。契約書、スキャン、請求書、書き出したスライドも数秒で結合——ファイルはブラウザの外に出ません。

<!--more-->

{{< pdf-merge >}}

## 仕組み

各PDFはpdf-libでローカルに解析され、ページが選択順に新しい文書へコピーされて保存されます。パスワード保護されたPDFは先にパスワードを解除してください。逆の操作は[PDF分割](/ja/tools/pdf-split/)や[ページ削除](/ja/tools/pdf-delete-pages/)で。

## 補足

- 結合したい順番どおりにファイルを選択
- 出力は merged.pdf としてダウンロード——後で名前を変更してください
- 大きなスキャンPDFは結合後に[PDF圧縮](/ja/tools/pdf-compress/)へ
