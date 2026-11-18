---
title: "カラーコンバーター（HEX / RGB / HSL）"
date: 2026-11-18
lastmod: 2026-11-18
description: "HEX・RGB・HSLを相互変換し、プレビュー色見本をライブ表示。デザインとフロントエンド作業のための無料ローカルツール。"
tags: [カラー変換, hexからrgb, rgbからhsl, カラーピッカー, hexカラー, hsl変換, デザインツール]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "color-converter"
---

HEX（`#2563eb`）、RGB（`rgb(37,99,235)`）、HSL（`hsl(221,83%,53%)`）のいずれかを入力すると、3形式すべてとライブのプレビュー色見本を表示します。完全にブラウザ内で動作します。

<!--more-->

{{< color-converter >}}

## 仕組み

このツールは入力された形式をパースし、内部のRGB表現を経由して3形式すべてを再描画します。変換は標準のCSS Color Moduleの式——ブラウザがスタイルシートの `hsl()` を評価するのと同じもの——に従います。

## 出会う場面

- **テーマ設計**: デザインシステムはある形式で保存し、ツールは別の形式を要求——TailwindはHEXとRGBの両方を話します
- **デザイン受け渡し**: FigmaはHEXを出力し、一部のチャートライブラリはHSLを要求
- **ダークモード調整**: HSLの明度だけを動かすと色相が保たれます——値を確定する前に確認しましょう

[パスワードジェネレーター](/ja/tools/password-generator/)と合わせてフロントエンドのユーティリティセットに。色を生の16進数として見るなら[進数変換](/ja/tools/number-base-converter/)もどうぞ。
