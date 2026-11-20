---
title: "比較表ジェネレーター"
date: 2026-11-20
lastmod: 2026-11-20
description: "項目と特徴のリストを整形された比較表に変換——ライブ描画とMarkdownコピー対応。レビュー、ドキュメント、ブログのための無料ローカルツール。"
tags: [比較表, 比較表生成, Markdown表生成, 製品比較, テーブル作成]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "comparison-table-generator"
---

項目と特徴を入力すると整形された比較表が得られます——確認用にライブ描画され、ドキュメント・README・ブログ用にMarkdownとしてコピーできます。完全にブラウザ内で動作します。

<!--more-->

{{< comparison-table-generator >}}

## 仕組み

項目は `名前: 値1, 値2, …` と書き、特徴がヘッダー列を定義。値は位置で特徴と対応し、空セルは `–` を使います。出力はライブ表と生Markdownの両方——[Markdownプレビューアー](/ja/tools/markdown-previewer/)で再描画できるのと同じ形式です。
