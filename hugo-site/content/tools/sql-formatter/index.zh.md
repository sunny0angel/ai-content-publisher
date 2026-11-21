---
title: "SQL 格式化器"
date: 2026-11-19
lastmod: 2026-11-21
description: "把杂乱的 SQL 整理成清晰可读的查询——关键字大写、子句换行、缩进分层。无服务器、无上传的免费本地格式化器。"
tags: [SQL格式化, SQL美化, SQL查询格式化, 开发者工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "sql-formatter"
faq:
  - q: "会校验 SQL 吗？"
    a: "不会。只做格式化，不检查方言或语义，无效 SQL 也会原样排版。"
  - q: "会保留方言特性吗？"
    a: "会。Postgres 类型转换、MySQL 反引号和引号字符串都原样保留。"
  - q: "查询会上传吗？"
    a: "不会。分词和格式化都在标签页内完成，生产查询不离开本机。"
related: [json-formatter, case-converter, markdown-previewer, json-to-csv]
---

粘贴一行 SQL 查询，得到规范格式的版本：关键字大写、每个子句独立成行、子查询缩进。完全在浏览器内运行——生产查询不会离开你的机器。

<!--more-->

{{< sql-formatter >}}

## 工作原理

格式化器对 SQL 做词法分析——把字符串、带引号的标识符、注释和数字与代码分离——再按结构规则重写：主要子句（`SELECT`、`FROM`、`WHERE`、`GROUP BY`、`ORDER BY`、JOIN、`UNION`）另起一行，`AND`/`OR` 单独成行，括号增加缩进层级。字符串和注释原样通过。

## 最实用的场景

- **调试**：ORM 日志里 400 字符的单行查询变成真正可读的结构
- **代码审查**：规范化的排版让 diff 显示真正的改动，而不是空白噪音
- **文档与工单**：贴进工单的可读 SQL，比一大坨文本得到答案快得多

它刻意只是*格式化器*而非校验器——方言特有语法（Postgres 的 `::` 转换、MySQL 反引号）原样保留。查询*产出*的数据，下一步交给 [JSON 转 CSV](/zh/tools/json-to-csv/)。
