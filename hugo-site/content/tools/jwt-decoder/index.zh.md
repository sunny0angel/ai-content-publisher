---
title: "JWT 解码器"
date: 2026-11-17
lastmod: 2026-11-17
description: "在浏览器内解码 JWT 的 header、payload 与签名，无需密钥即可查看 claims 和时间戳。免费本地工具，你的 token 不会离开页面。"
tags: [JWT解码, JWT解析, JSON Web Token, JWT claims, JWT header, token调试]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "jwt-decoder"
---

粘贴 JSON Web Token，即刻解码其 header、payload 与签名，`iat`/`exp` 自动换算为本地时间。token 始终留在浏览器内，不会被发送到任何地方。

<!--more-->

{{< jwt-decoder >}}

## 什么是 JWT

JSON Web Token 由三个以点分隔的 Base64url 编码部分组成：`header.payload.signature`。header 声明签名算法（`alg`），payload 携带 claims（`sub`、`exp`、`iss` 及自定义字段），signature 用于让服务器验证前两部分未被篡改。

**重要**：解码不等于验证。任何人都能解码 JWT——签名只有在用正确密钥校验后才有证明力。本工具有意不做验证，所以不需要密钥，也能完全离线运行。

## 检查要点

- **`alg: "none"`** — 声明无签名的 token，生产环境里是立即亮起的红灯，校验器必须拒绝
- **`exp` 已过期** — 服务器会拒绝过期 token；客户端还留着它，说明刷新流程坏了
- **claims 过多** — token 应携带最少必要信息。每多一个 claim，token 就大一圈，而它每次请求都要发送
- **payload 里的秘密** — 出现 `password` 或 `api_key` claim，说明有人把认证和存储搞混了

## 典型用途

调试 401 死循环：解码 token，检查 `exp` 和 `aud`，确认后端期待的密钥和签发方。与 [Base64 编码器](/zh/tools/base64-encoder/)（JWT 底层就是 Base64url）和 [SHA 哈希生成器](/zh/tools/hash-generator/)（HS256 即 HMAC-SHA-256）天然搭配。
