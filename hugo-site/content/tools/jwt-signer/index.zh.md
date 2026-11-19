---
title: "JWT 签发工具（HS256）"
date: 2026-11-19
lastmod: 2026-11-19
description: "用 Web Crypto 在浏览器内完成 HS256（HMAC-SHA256）JWT 签发。密钥绝不离开页面。与 JWT 解码器配套的免费本地工具。"
tags: [JWT签发, JWT生成, HS256, HMAC-SHA256, JWT token生成, JSON Web Token签名]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "jwt-signer"
---

用你自己的 header、payload 和密钥生成签名 JWT——HS256 签名由浏览器 Web Crypto API 计算，密钥不会离开你的标签页。它是 [JWT 解码器](/zh/tools/jwt-decoder/)的天然搭档：解码为了理解，签发为了构建。

<!--more-->

{{< jwt-signer >}}

## 工作原理

工具先对 header 和 payload 做 Base64url 编码，再通过 `crypto.subtle.sign` 计算 `HMAC-SHA256(密钥, header.payload)`——与生产 JWT 库用于 HS256 的原语相同。结果是标准 [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519) 格式的完整 `header.payload.signature` token。

## 值得一读的安全说明

- **密钥就是全部安全。** 任何持有密钥的人都能为你的系统伪造 token。请使用至少 32 个随机字节——[密码生成器](/zh/tools/password-generator/)可以产出，但专用密钥管理器更合适
- **HS256 是对称的。** 所有验证 token 的服务都需要同一把密钥。多服务架构下 RS256（非对称）是更好的设计——本工具覆盖 HS256 场景，适合单服务应用和快速测试
- **不要把密钥发给客户端。** 本工具仅为测试便利将其留在本地；生产签名应放在服务端

JWT 的结构、验证清单和常见攻击全貌，见 [JWT 详解](/zh/blog/jwt-explained/)。
