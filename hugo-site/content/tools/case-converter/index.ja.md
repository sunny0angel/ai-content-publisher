---
title: "大文字小文字変換（ケースコンバーター）"
date: 2026-11-18
lastmod: 2026-11-21
description: "UPPERCASE、lowercase、Title Case、camelCase、snake_case、kebab-caseをワンクリックで相互変換。命名と整形のための無料ローカルツール。"
tags: [ケース変換, camelCase, snake_case, kebab-case, タイトルケース, テキストケース, 開発ツール]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "case-converter"
faq:
  - q: "対応している変換は？"
    a: "大文字、小文字、タイトルケース、camelCase、snake_case、kebab-caseです。まず空白・アンダースコア・ハイフンで単語に分割します。"
  - q: "略語や句読点は保持されますか？"
    a: "単語単位に正規化するため、APIなどの略語はcamelCaseやsnake_caseではapiになります。識別子モードでは区切り以外の句読点は保持されません。"
  - q: "テキストは送信されますか？"
    a: "いいえ。変換はタブ内で完結します。"
related: [url-encoder, text-diff, lorem-ipsum-generator, regex-tester]
---

任意のテキストをUPPERCASE、lowercase、Title Case、camelCase、snake_case、kebab-caseにワンクリック変換。コードの命名、URLスラッグ、APIフィールド名に便利です。完全にブラウザ内で動作します。

<!--more-->

{{< case-converter >}}

## 仕組み

変換器は入力をスペース・アンダースコア・ハイフンで単語に分割し、規約に従って再結合します。`camelCase` は最初の単語を小文字にし残りを大文字始まりに、`snake_case` と `kebab-case` はすべて小文字にして `_` か `-` で結合します。

## 命名規約の実践

| 文脈 | 規約 |
|------|------|
| JavaScript/Goの変数 | camelCase |
| Pythonの変数/ファイル | snake_case |
| CSSクラス、URL | kebab-case |
| APIフィールド | snake_case（REST）またはcamelCase（GraphQL） |
| クラス | PascalCase（スペースなしのTitle Case） |

APIレスポンスの規約が混在するときは、[JSON to CSV変換](/ja/tools/json-to-csv/)の前にフィールド名を揃えるとヘッダーが一貫します。
