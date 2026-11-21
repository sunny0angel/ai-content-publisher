---
title: "進数変換（HEX / DEC / BIN / OCT）"
date: 2026-11-18
lastmod: 2026-11-21
description: "16進数・10進数・2進数・8進数・base36を任意精度で相互変換。開発者向けの無料ローカルツール。"
tags: [進数変換, hexから10進数, 2進数変換, 8進数変換, base36, 基数変換, 開発ツール]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "number-base-converter"
faq:
  - q: "大きな数値で精度は落ちますか？"
    a: "いいえ。BigIntを使うため、64ビットのIDやそれ以上の整数もJavaScriptのNumberのように丸められず正確に変換されます。"
  - q: "対応している基数は？"
    a: "10進、16進、2進、8進、36進で、相互にリアルタイム変換します。"
  - q: "負の数も変換できますか？"
    a: "符号は扱えますが、固定幅整数の2の補数変換は行いません。"
related: [hash-generator, color-converter, base64-encoder, timestamp-converter]
---

任意の整数を10進数・16進数・2進数・8進数・base36の間で変換します。BigInt精度のため、64ビット以上の値でも桁落ちしません。完全にブラウザ内で動作します。

<!--more-->

{{< number-base-converter >}}

## 仕組み

このツールは選択された基数で入力を `BigInt` でパースします——JavaScriptの数値と違い、BigIntは任意に大きな整数を正確に扱うため、カラーコード、ハッシュ断片、DBのIDが無傷で通過します。4つの表現が入力に合わせて更新されます。

## 出会う場面

- **デバッグ**: 16進ダンプ、メモリアドレス、ビットマスクは、実は2進・16進の算術
- **色**: `#2563eb` はただの16進数——視覚面は[カラーコンバーター](/ja/tools/color-converter/)が担当
- **ハッシュ**: SHAダイジェストは16進文字列。断片を10進数にするとソート・圧縮に便利——[ハッシュジェネレーター](/ja/tools/hash-generator/)で生成を
- **base36 URL**: 短縮リンクサービスはIDをbase36でエンコード——ここでデコードできます
