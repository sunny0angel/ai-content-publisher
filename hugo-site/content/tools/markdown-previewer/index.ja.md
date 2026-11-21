---
title: "Markdownプレビューアー"
date: 2026-11-19
lastmod: 2026-11-21
description: "ブラウザ内でライブ2ペインのMarkdownプレビュー——見出し、リスト、コードブロック、引用、リンク、画像対応。アップロードなしの無料ローカルツール。"
tags: [Markdownプレビュー, Markdownエディタ, MarkdownからHTML, ライブMarkdown, 開発ツール]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "markdown-previewer"
faq:
  - q: "対応しているMarkdown機能は？"
    a: "見出し、強調、インライン/フェンス付きコード、リンク、画像、リスト、引用です。表、脚注、生HTMLの通過は対象外です。"
  - q: "生のHTMLは描画されますか？"
    a: "いいえ。先にHTMLをエスケープするため、貼り付けたマークアップは無効化され、スクリプトも実行されません。"
  - q: "文書は保存されますか？"
    a: "いいえ。内容はタブ内にのみ存在するため、閉じる前にコピーしてください。"
related: [text-diff, sql-formatter, lorem-ipsum-generator, case-converter]
---

左でMarkdownを書くと、右に描画結果がライブ表示されます——ビルドもサーバーも不要。日常的なサブセットをカバー：見出し、強調、インライン／フェンスコード、リンク、画像、リスト、引用。

<!--more-->

{{< markdown-previewer >}}

## 仕組み

プレビューアーはまず生のHTMLをエスケープし（貼り付けたマークアップが無害のまま）、小さなブロックレベルパーサーを適用します。フェンスコードブロック、見出し、リスト、引用、段落——続いて各ブロック内のインライン整形（コード、太字、斜体、リンク、画像）。これは一般的な90%のための*プレビュー*エンジンであって、完全なCommonMark実装ではありません。テーブル、脚注、HTMLパススルーは意図的に対象外です。

## 手を伸ばす場面

- **READMEやコメントの下書き**をリポジトリへプッシュする前に
- **ドキュメントの文章確認**——サイトのビルドを走らせられないとき
- **MarkdownでLLMプロンプトを書き**、構造が意図どおり読めるか確認——[プロンプト比較テスター](/ja/tools/prompt-compare/)と組み合わせてAIワークフローを完成

同じツールチェーンのJSONとSQLには、[フォーマッター](/ja/tools/json-formatter/)と[SQLフォーマッター](/ja/tools/sql-formatter/)が揃っています。
