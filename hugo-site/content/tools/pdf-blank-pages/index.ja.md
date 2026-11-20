---
title: "空白PDF生成"
date: 2026-11-20
lastmod: 2026-11-20
description: "A4またはLetterの空白ページを1〜100枚生成——区切り紙、メモ欄、印刷テストに。無料・ローカル。"
tags: [空白PDF, 白紙PDF 作成, 空PDF, 区切りページ, PDF生成]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-blank-pages"
---

空白ページだけのきれいなPDFを生成——1枚から100枚まで、A4またはLetter。章の区切り、メモ欄、プリンタの位置合わせに便利です。

<!--more-->

{{< pdf-blank-pages >}}

## 仕組み

pdf-libでゼロから文書を構築し、基本的な情報以外に隠れた内容・フォント・メタデータは含みません。実際の文書とまとめるには[PDF結合](/ja/tools/pdf-merge/)、枚数を減らしたいときは[N-up](/ja/tools/pdf-n-up/)を。

## 補足

- 1ページを100%で印刷してプリンタの余白を確認
- A4は595×842pt、Letterは612×792pt
- 空白ページはスキャンの副産物になりがち——[ページ削除](/ja/tools/pdf-delete-pages/)で除去
