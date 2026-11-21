---
title: "正则表达式测试器"
date: 2026-11-18
lastmod: 2026-11-21
description: "在浏览器里测试正则表达式：匹配高亮、标志开关（g/i/m/s）、实时匹配数。免费本地工具，你的正则不会离开页面。"
tags: [正则测试器, 正则表达式测试, 正则标志, 正则调试, 开发者工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "regex-tester"
faq:
  - q: "使用哪个正则引擎？"
    a: "通过 new RegExp 使用浏览器原生引擎，与 JavaScript 和 Node.js 相同，结果与代码一致。"
  - q: "可以切换哪些标志？"
    a: "g、i、m、s。未启用 g 时只高亮第一个匹配。"
  - q: "正则或测试文本会上传吗？"
    a: "不会。编译与匹配都在标签页内完成。"
  - q: "为什么这里能匹配，Python 里却失败？"
    a: "不同语言在后向断言、命名分组和 Unicode 类上存在差异。上线前请在目标语言中验证。"
related: [regex-visualizer, text-diff, case-converter, json-formatter]
---

输入正则、粘贴文本，所有匹配即刻高亮——可切换 `g`/`i`/`m`/`s` 标志并实时显示匹配数。运行在浏览器原生正则引擎上，结果与你的 JavaScript 代码完全一致。

<!--more-->

{{< regex-tester >}}

## 工作原理

工具用 `new RegExp(pattern, flags)` 编译你的正则——与 Node.js 和浏览器代码同一个引擎——然后遍历所有匹配并加高亮。正则无效时，会显示精确的错误信息而不是静默失败。

## 值得记住的常用正则

| 目标 | 正则 |
|------|------|
| 邮箱 | `\b[\w.+-]+@[\w-]+\.[\w.]+\b` |
| URL | `https?://[^\s]+` |
| 日期（YYYY-MM-DD） | `\d{4}-\d{2}-\d{2}` |
| 电话（宽松） | `\+?\d[\d -]{7,}\d` |

## 正则的使用场景

- **校验**：表单输入、API 请求体——发送前先验证
- **日志解析**：配合 [时间戳转换器](/zh/tools/timestamp-converter/)提取时间戳和 ID
- **数据清洗**：交给 [JSON 转 CSV](/zh/tools/json-to-csv/) 之前先清理字段

如果工具里的结果和生产环境不一致，常见原因是标志差异（`g` 会改变 `matchAll`/`exec` 行为）或正则方言不同（PCRE vs JavaScript）。本工具按设计使用 JavaScript 方言。
