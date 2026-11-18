---
title: "进制转换器（HEX / DEC / BIN / OCT）"
date: 2026-11-18
lastmod: 2026-11-18
description: "在十六进制、十进制、二进制、八进制和 base36 之间转换数字，任意精度。面向开发者的免费本地工具。"
tags: [进制转换, hex转十进制, 二进制转换, 八进制转换, base36, 基数转换, 开发者工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "number-base-converter"
---

在十进制、十六进制、二进制、八进制和 base36 之间转换任意整数——使用 BigInt 精度，64 位及更大的值也不会丢位。完全在浏览器内运行。

<!--more-->

{{< number-base-converter >}}

## 工作原理

工具用 `BigInt` 按所选进制解析输入——与 JavaScript 普通数字不同，BigInt 能精确处理任意大的整数，颜色码、哈希片段和数据库 ID 都能完整往返。四种表示随输入实时更新。

## 你会遇到的场景

- **调试**：十六进制转储、内存地址、位掩码本质上是二进制/十六进制算术
- **颜色**：`#2563eb` 就是一个十六进制数——视觉部分交给[颜色转换器](/zh/tools/color-converter/)
- **哈希**：SHA 摘要是十六进制字符串；片段转十进制便于排序和压缩——用[哈希生成器](/zh/tools/hash-generator/)生成
- **Base36 URL**：短链接服务用 base36 编码 ID——在这里解码
