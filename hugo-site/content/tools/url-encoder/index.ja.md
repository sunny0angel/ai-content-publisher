---
title: "URLエンコーダー／デコーダー"
date: 2026-11-18
lastmod: 2026-11-21
description: "パーセントエンコーディングでURLコンポーネントを正しくエンコード／デコード。クエリ文字列やリンク構築のための無料ローカルツール。"
tags: [URLエンコード, URLデコード, パーセントエンコーディング, encodeURIComponent, URLエスケープ, 開発ツール]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "url-encoder"
faq:
  - q: "どのJavaScript関数と同じ結果ですか？"
    a: "encodeURIComponentとdecodeURIComponentです。クエリ文字列として送信する値と一致します。"
  - q: "スペースが+ではなく%20になるのはなぜですか？"
    a: "%20が標準のパーセントエンコードです。+はapplication/x-www-form-urlencodedの形式で、どこでも同じ意味ではありません。"
  - q: "URL全体をエンコードできますか？"
    a: "このツールはコンポーネント用のため、://?&もエスケープされます。動的な値だけをエンコードしてください。"
  - q: "日本語や絵文字も扱えますか？"
    a: "はい。UTF-8に変換してからパーセントエンコードするため、マルチバイト文字も保持されます。"
related: [base64-encoder, json-formatter, hash-generator, case-converter]
---

任意のテキストをURLセーフなパーセントエンコード文字列に変換し、戻せます。UTF-8を正しく扱うため、日本語・中国語・絵文字もクエリ文字列を無事に通過します。すべてブラウザ内で処理され、外部送信はありません。

<!--more-->

{{< url-encoder >}}

## 仕組み

URLが安全に含められる文字はごく一部（英数字と `-._~`）だけです。それ以外——スペース、`&`、`?`、`#`、非ASCII文字——はパーセントエンコーディングで各バイトを `%XX` に変換する必要があります。このツールはブラウザの `encodeURIComponent`／`decodeURIComponent` を使用するため、あなたのアプリが送る値と結果が一致します。

2つの変種の違いは重要です。`encodeURIComponent` は**すべて**をエスケープし（クエリ値に正しい）、`encodeURI` はURL構造文字を残します（完全なURLに正しい）。このツールはコンポーネント版——クエリ文字列構築の安全な選択です。

## 出会う場面

- **クエリ文字列**: `?q=AI+Forward&lang=ja` ——値の中の未エンコードの `&` や `=` はURLを壊します
- **API呼び出し**: 動的な値（名前、住所、フリーテキスト検索）は埋め込み前にエンコード必須
- **OAuthリダイレクトと署名付きリンク**: エンコードを誤ると署名が壊れます

[Base64エンコーダー](/ja/tools/base64-encoder/)（Base64urlもURLセーフな別方式）や、クエリ結果がJSONで返るときの[JSONフォーマッター](/ja/tools/json-formatter/)と自然に組み合わせられます。
