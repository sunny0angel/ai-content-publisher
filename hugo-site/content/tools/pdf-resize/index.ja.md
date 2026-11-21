---
title: "PDFページサイズ変更（A4・Letter・A3）"
date: 2026-11-20
lastmod: 2026-11-21
description: "PDFの全ページをA4・Letter・A3・Legalに変更。再描画なし。ローカル・無料・アップロード不要。"
tags: [PDF サイズ変更, PDF A4, PDF ページサイズ, PDF 印刷設定]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-resize"
faq:
  - q: "リサイズとN-upの違いは何ですか？"
    a: "リサイズは各ページの用紙サイズを変更します（A4からLetterなど）。N-upは複数ページを1枚に配置します。"
  - q: "内容が歪みませんか？"
    a: "縦横比を保って拡大・縮小するため、引き伸ばしにはなりません。比率が違う場合は余白ができます。"
  - q: "拡大すると画質は落ちますか？"
    a: "ベクター文字は鮮明なままです。画像は情報が増えないため、低解像度スキャンをA3に拡大するとぼやけることがあります。"
related: [pdf-crop, pdf-n-up, pdf-compress, images-to-pdf]
---

サイズが混在したPDFをA4・Letter・A3・Legalに統一して、印刷やファイリングをきれいに。ページのキャンバスが変わり、内容はベクターのままです。

<!--more-->

{{< pdf-resize >}}

## 仕組み

pdf-libで各ページのメディアボックスを目標サイズに設定します。内容の拡大縮小や再エンコードは行わないためぼやけませんが、異なる縦横比向けの内容は中央からずれる場合があります。余白を切りたい場合は[PDFトリム](/ja/tools/pdf-crop/)を。

## 補足

- A4は595×842pt、Letterは612×792pt
- 印刷前に結果を確認——内容は自動拡大されません
- 混在サイズは[PDF検査](/ja/tools/pdf-info/)で確認できます
