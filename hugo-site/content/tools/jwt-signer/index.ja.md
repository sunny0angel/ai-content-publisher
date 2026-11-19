---
title: "JWT署名ツール（HS256）"
date: 2026-11-19
lastmod: 2026-11-19
description: "Web CryptoでHS256（HMAC-SHA256）のJWTをブラウザ内で署名。秘密鍵はページの外に出ません。[JWTデコーダー]と対になる無料ローカルツール。"
tags: [JWT署名, JWT生成, HS256, HMAC-SHA256, JWTトークン生成, JSON Web Token署名]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "jwt-signer"
---

自分のヘッダー・ペイロード・秘密鍵から署名済みJWTを生成します——HS256署名はブラウザのWeb Crypto APIで計算されるため、秘密鍵がタブの外に出ることはありません。[JWTデコーダー](/ja/tools/jwt-decoder/)の自然な相棒です。理解するためにデコードし、構築するために署名する。

<!--more-->

{{< jwt-signer >}}

## 仕組み

このツールはヘッダーとペイロードをBase64urlエンコードし、`crypto.subtle.sign` で `HMAC-SHA256(秘密鍵, header.payload)` を計算します——本番のJWTライブラリがHS256に使うのと同じプリミティブです。結果は標準の [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519) 形式の完全な `header.payload.signature` トークンです。

## 読む価値のあるセキュリティメモ

- **秘密鍵がセキュリティのすべて。** 鍵を持つ者は誰でもあなたのシステムのトークンを偽造できます。最低32ランダムバイトを使いましょう——[パスワードジェネレーター](/ja/tools/password-generator/)でも生成できますが、専用のシークレットマネージャーの方が適切です
- **HS256は対称。** トークンを検証する全サービスが同じ秘密鍵を必要とします。マルチサービス構成ではRS256（非対称）がより良い設計——このツールは単一サービスアプリと迅速なテストに適したHS256を扱います
- **秘密鍵をクライアントに配らない。** このツールはテストの利便性のためローカルに保持しますが、本番の署名はサーバー側で行うべきです

JWTの構造・検証チェックリスト・代表的な攻撃の全体像は[JWT徹底解説](/ja/blog/jwt-explained/)をご覧ください。
