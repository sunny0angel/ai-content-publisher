---
title: "JSON 转 CSV 转换器"
date: 2026-11-17
lastmod: 2026-11-21
description: "在浏览器内把对象数组 JSON 转为 CSV，自动识别表头，附带 Excel 友好的 UTF-8 BOM。免费本地工具，无需上传。"
tags: [JSON转CSV, JSON CSV转换, JSON转Excel, JSON数组转CSV, CSV导出, 数据转换工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "json-to-csv"
faq:
  - q: "支持什么输入格式？"
    a: "对象数组。每个对象一行，所有键的并集作为表头。单个对象或数组的数组不支持。"
  - q: "嵌套对象怎么处理？"
    a: "会被序列化成单个单元格。需要独立列时，请先展平数据。"
  - q: "Excel 打开中文会乱码吗？"
    a: "输出带 UTF-8 BOM，Excel 可正常识别。若旧软件仍乱码，请按 UTF-8 导入。"
related: [json-formatter, json-diff, base64-encoder, comparison-table-generator]
---

把对象数组 JSON 转成 CSV 表格——表头按对象键自动识别，值正确转义，并附 UTF-8 BOM，让 Excel 能正确打开中文和日文内容。全部在浏览器内完成，不会上传任何数据。

<!--more-->

{{< json-to-csv >}}

## 工作原理

工具接收扁平对象数组，输出一行表头 + 每个对象一行的 CSV。表头取所有对象键的并集（缺失的键为空单元格），含逗号、引号或换行的值按 RFC 4180 加引号转义。

## 省时间的场景

- **API 导出**：多数 API 返回 JSON 数组，而表格软件要 CSV。本工具就是那座桥
- **LLM 输出**：批量任务和结构化输出的响应常以 JSON 数组形式返回——转成 CSV 放进 Excel 或 Sheets 里审阅
- **临时分析**：把 JSON 日志倒进表格，再用任意表格工具做透视

## 输入规则

- 顶层必须是对象的 JSON **数组**（不是数组的数组，也不是裸对象）
- 嵌套对象和数组会被字符串化进单个单元格——需要分列请先自行扁平化
- 每个不同键对应一列，顺序按首次出现

先用 [JSON 格式化器](/zh/tools/json-formatter/)校验输入，CSV 需要塞进其他请求体时配合 [Base64 编码器](/zh/tools/base64-encoder/)。


想了解完整的转换指南，请阅读 [JSON 转 CSV 实用指南](/zh/blog/json-to-csv-guide/)。
