---
title: "UUIDジェネレーター"
date: 2026-11-17
lastmod: 2026-11-21
description: "RFC 9562準拠のUUID v4を一括生成。小文字・大文字を選択可能。Web Crypto APIによるブラウザ内生成で、サーバー通信なし。無料。"
tags: [UUIDジェネレーター, GUID生成, UUID v4, RFC 9562, ランダムID, UUIDツール]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "uuid-generator"
faq:
  - q: "UUIDは本当にランダムですか？"
    a: "はい。Math.randomではなくcrypto.getRandomValuesから生成するバージョン4 UUIDです。"
  - q: "一度に何個まで生成できますか？"
    a: "1回100個までです。それ以上は繰り返し生成してください。"
  - q: "バージョン7は生成できますか？"
    a: "このツールはv4のみです。時刻順のデータベースキーが必要な場合はv7ライブラリを使ってください。"
  - q: "生成したUUIDが重複することはありますか？"
    a: "実質的にありません。122ビットの乱数では、毎秒数十億個を何年も生成しない限り衝突しません。"
related: [hash-generator, password-generator, base64-encoder, timestamp-converter]
---

UUID v4を最大100個まで一度に生成できます（小文字／大文字選択可）。IDはWeb Crypto API（`crypto.getRandomValues` / `crypto.randomUUID`）でブラウザ内生成されるため、リクエストが外部に送信されることはなく、実用上衝突も起こりません。

<!--more-->

{{< uuid-generator >}}

## UUIDとは

UUID（Universally Unique Identifier）は128ビットの値を36文字で表した識別子です。`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` の形式で、バージョン4は122ビットの乱数から生成されるため、取りうる値は2¹²²通り——毎秒数十億個を生成しても衝突確率は無視できるレベルです。形式は [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562) で標準化されており、2024年の改訂で時刻順序付きのバージョン6・7も追加されました。

## v4とv7、どちらを使うべきか

- **v4（本ツール）**: 完全ランダム。シンプルで均一、ほとんどの用途の安全なデフォルト
- **v7**: 生成時刻で順序付けられるため、PostgreSQLなどで主キーの挿入性能が大幅に向上します（シーケンシャルなキーはインデックスの断片化を防ぐ）。2026年時点で新規テーブルにはv7が推奨されます

UUIDをデータベースの主キーにする場合は、サーバー側でv7を生成することを検討してください。APIトークンやセッションIDなど、生成順序を推測されたくないIDにはv4が適しています——ランダム性が作成順を隠してくれます。

## 実用的な使い方

- **DBキー**: `INSERT INTO users (id, name) VALUES ('<uuid>', 'Ada');`
- **APIの冪等性キー**やリクエスト相関ID
- **アップロードファイル名**（衝突が起きては困る場面）
- **テストデータ**: 一括生成してJSONペイロードに組み込む。[JSONフォーマッター](/ja/tools/json-formatter/)と併用すると便利です

バージョン比較とDB性能への影響を詳しく知りたい方は、[UUIDとは？バージョン・ユースケース・ベストプラクティス](/ja/blog/what-is-a-uuid/)をご覧ください。
