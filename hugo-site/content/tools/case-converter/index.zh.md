---
title: "大小写转换器"
date: 2026-11-18
lastmod: 2026-11-21
description: "一键在 UPPERCASE、lowercase、Title Case、camelCase、snake_case、kebab-case 之间转换文本。用于命名与格式化的免费本地工具。"
tags: [大小写转换, camelCase, snake_case, kebab-case, 标题大小写, 文本大小写, 开发者工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "case-converter"
faq:
  - q: "支持哪些命名格式？"
    a: "大写、小写、标题格式、camelCase、snake_case 和 kebab-case。转换前会按空格、下划线、连字符拆词。"
  - q: "会保留缩写和标点吗？"
    a: "会按单词归一化，API 等缩写会变成 api；标识符模式下除分隔符外的标点不会保留。"
  - q: "文本会上传吗？"
    a: "不会，转换在标签页内完成。"
related: [url-encoder, text-diff, lorem-ipsum-generator, regex-tester]
---

一键把任意文本转成 UPPERCASE、lowercase、Title Case、camelCase、snake_case 或 kebab-case。代码命名、URL 别名、API 字段名都用得上。完全在浏览器内运行。

<!--more-->

{{< case-converter >}}

## 工作原理

转换器按空格、下划线和连字符把输入切成单词，再按惯例重组：`camelCase` 首词小写、其余首字母大写；`snake_case` 和 `kebab-case` 全部小写，分别用 `_` 和 `-` 连接。

## 命名规范实战

| 场景 | 规范 |
|------|------|
| JavaScript/Go 变量 | camelCase |
| Python 变量/文件 | snake_case |
| CSS 类、URL | kebab-case |
| API 字段 | snake_case（REST）或 camelCase（GraphQL） |
| 类名 | PascalCase（无空格的 Title Case） |

API 响应的字段规范不一致时，先统一再交给 [JSON 转 CSV](/zh/tools/json-to-csv/)，表头就整齐了。
