---
title: "密码生成器"
date: 2026-11-18
lastmod: 2026-11-18
description: "用密码学安全随机源生成强密码，可调长度与字符集，带强度估算。免费本地工具。"
tags: [密码生成, 强密码, 随机密码, 安全密码, 密码强度, 安全工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "password-generator"
---

用 `crypto.getRandomValues`——浏览器 TLS 使用的同一密码学安全随机源——在本地生成强密码。可选长度（8–64）和字符集，附带基于熵的强度估算。不会传输任何内容，密码只存在于你的标签页里。

<!--more-->

{{< password-generator >}}

## 工作原理

生成器通过 Web Crypto API 取字符，保证每个选中的字符集至少出现一个字符，然后洗牌。强度估算按 `长度 × log2(字符集大小)` 计算熵——约 80 位以上被认为能抵御离线攻击。字符集刻意剔除了易混字符（`0/O`、`1/l/I`），方便输入和阅读。

## 比密码本身更重要的规则

- **每站唯一**：复用是强密码死掉的头号原因——配合密码管理器使用
- **长度胜过复杂度**：20 位随机小写字母（约 94 位熵）胜过 10 位混合大小写（约 59 位）
- **不是 SHA-256 的场合**：密码在服务端用 Argon2/bcrypt 哈希存储——原因见 [SHA-256 详解](/zh/blog/sha-256-explained/)

API 密钥和 token 可配合 [UUID 生成器](/zh/tools/uuid-generator/)——v4 UUID 是「绝不能碰撞」的标识符标准。
