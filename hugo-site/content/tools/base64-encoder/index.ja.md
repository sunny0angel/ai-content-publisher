---
title: "Base64エンコーダー／デコーダー"
date: 2026-11-17
lastmod: 2026-11-17
description: "UTF-8完全対応のBase64エンコード／デコード。API、JWT、テキストに埋め込まれたバイナリデータを扱う開発者向けの無料ローカルツール。"
tags: [Base64エンコード, Base64デコード, Base64変換, URLセーフBase64, 開発ツール]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "base64-encoder"
---

テキストとBase64を相互変換できます。UTF-8に完全対応しており、`btoa()` と違い日本語・中国語・絵文字でも壊れません。すべてブラウザ内で処理され、アップロードは一切ありません。

<!--more-->

{{< base64-encoder >}}

## 仕組み

Base64はバイナリデータを64種類の表示可能なASCII文字（`A–Z`、`a–z`、`0–9`、`+`、`/`）と `=` パディングで表現します。3バイトの入力が4文字の出力になり、サイズは33%増えます。その代償に、JSON文字列、XML、メール（MIME）、URLパラメータなど、テキストしか通らない経路で安全に運べるようになります。

このツールはまずテキストをUTF-8バイト列にエンコードしてからBase64を適用します——Latin-1しか扱えない素の `btoa()` が失敗する場面でも正しく動きます。デコードはその逆です。

## 出会う場面

- **JWT**: すべてのJSON Web TokenのヘッダーとペイロードはBase64urlエンコードされたJSONです。[JWTデコーダー](/ja/tools/jwt-decoder/)でデコードできます
- **データURL**: `data:image/png;base64,...` はHTMLやCSSに画像を直接埋め込みます
- **APIペイロード**: バイナリブロブ（画像、証明書、protobuf）はJSON内でBase64文字列として運ばれます
- **Basic認証**: `Authorization: Basic base64(user:pass)` ——ここでのエンコードは輸送手段であってセキュリティではありません。誰でもデコードできます

データワークフローの残り半分——構造化レコードのテーブル変換——は[JSON to CSV変換](/ja/tools/json-to-csv/)をご覧ください。
