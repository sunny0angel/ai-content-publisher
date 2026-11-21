---
title: "URL 编码与解码器"
date: 2026-11-18
lastmod: 2026-11-21
description: "用百分号编码正确地对 URL 组件进行编码和解码。构建查询串、链接和永不失效的 API URL 的免费本地工具。"
tags: [URL编码, URL解码, 百分号编码, encodeURIComponent, URL转义, 开发者工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "url-encoder"
faq:
  - q: "和哪个 JavaScript 函数一致？"
    a: "与 encodeURIComponent / decodeURIComponent 一致，结果和你代码里查询参数发送的值相同。"
  - q: "为什么空格编码成 %20 而不是 +？"
    a: "%20 是标准百分号编码；+ 属于 application/x-www-form-urlencoded，并非在所有场景等价。"
  - q: "可以编码整个 URL 吗？"
    a: "本工具按组件编码，://?& 也会被转义。只应编码动态值，不要编码完整 URL。"
  - q: "支持日文和 emoji 吗？"
    a: "支持。文本先转 UTF-8 再做百分号编码，多字节字符不会丢失。"
related: [base64-encoder, json-formatter, hash-generator, case-converter]
---

把任意文本转成 URL 安全的百分号编码字符串，并可还原。正确处理 UTF-8，中文、日文和 emoji 都能安全通过查询串。全部在浏览器内运行，不会发送任何内容。

<!--more-->

{{< url-encoder >}}

## 工作原理

URL 只能安全容纳少量字符（字母、数字和 `-._~`）。其他一切——空格、`&`、`?`、`#`、非 ASCII 文本——都必须百分号编码：每个字节变成 `%XX`。本工具使用浏览器的 `encodeURIComponent`/`decodeURIComponent`，与你的 JavaScript 代码一致，结果和你应用实际发送的完全相同。

两个变体的区别很重要：`encodeURIComponent` 转义**一切**（查询值该用它），`encodeURI` 保留 URL 结构字符（完整 URL 该用它）。本工具用组件版——构建查询串的安全选择。

## 你会遇到的场景

- **查询串**：`?q=AI+Forward&lang=ja`——值里未编码的 `&` 或 `=` 会毁掉整个 URL
- **API 调用**：动态值（姓名、地址、自由文本搜索）在拼接前必须编码
- **OAuth 重定向与签名链接**：编码错误会让签名失效

与 [Base64 编码器](/zh/tools/base64-encoder/)（Base64url 是另一种 URL 安全编码）和查询结果为 JSON 时用到的 [JSON 格式化器](/zh/tools/json-formatter/)天然搭配。
