---
title: "JSON差分チェッカー"
date: 2026-11-20
lastmod: 2026-11-20
description: "2つのJSON文書を比較し、追加・削除・変更されたフィールドをパス付きでハイライト。データがページの外に出ない無料ローカルツール。"
tags: [JSON差分, JSON比較, JSON diff, JSON差異]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "json-diff"
---

2つのJSON文書——デプロイ前後のAPIレスポンス、設定変更、2つの環境——を貼り付けると、追加・削除・変更されたフィールドがフルパス付きで分かります。完全にブラウザ内で動作します。

<!--more-->

{{< json-diff >}}

## 仕組み

両方の文書をパースし、再帰的に走査してオブジェクトをキーごと、配列を要素ごとに比較します。変更値は `パス: 旧 → 新` の遷移で表示され、新規と削除は緑と赤でマークされます。JSONでなくテキスト文書なら[テキスト差分チェッカー](/ja/tools/text-diff/)が適任。比較前に両側の検証を[JSONフォーマッター](/ja/tools/json-formatter/)で。
