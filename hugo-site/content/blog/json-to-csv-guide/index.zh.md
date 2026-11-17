---
title: "JSON 转 CSV 实用指南：正确做法与不该用的场合"
date: 2026-11-17
lastmod: 2026-11-17
description: "把 JSON 数组正确转为 CSV：表头检测、RFC 4180 转义、Excel 的 UTF-8 BOM、嵌套数据扁平化，以及 CSV 选错目标的场景。附免费转换工具。"
tags: [JSON转CSV, JSON CSV转换, JSON转Excel, JSON转表格, CSV导出, UTF-8 BOM Excel, 嵌套JSON扁平化]
categories: ["AI Tools"]
images:
  featured_image: "/images/json-to-csv-guide.jpg"
draft: false
authors: ["AI Forward"]
slug: "json-to-csv-guide"
---

> **题图:** 在桌前对照图表做笔记和计算。摄影：[Jakub Zerdzicki](https://www.pexels.com/photo/making-notes-and-calculations-based-on-charts-20251480/)（Pexels，免费使用）

API 说 JSON。人在表格里看数据。夹在两者之间的是软件世界里最常见的杂活之一：把 JSON 数组转成 CSV 文件——而每个看起来简单的杂活都有锋利的边角。让 Excel 里所有非英文字符乱码的编码、静默塌缩成 `[object Object]` 的嵌套对象、把整列挤到右边去的含逗号值。本指南覆盖正确的转换方式，以及 CSV 从一开始就选错目的地的场景。

实际转换交给本站免费的 [JSON 转 CSV 转换器](/zh/tools/json-to-csv/)——表头检测、转义、Excel 友好的 UTF-8 输出，全在浏览器内完成。

## CSV 到底是什么

CSV（comma-separated values）是由 [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180) 标准化的文本表格格式：行用换行分隔、字段用逗号分隔，对含特殊字符的值有三条规则：

1. 含逗号、引号或换行的值要**用双引号包裹**
2. 被包裹值内部的引号要**加倍**：`"` 变 `""`
3. 表头行可选但属惯例

这个格式在实际中的规格缺失程度惊人：有的工具用分号（Excel 欧洲区域默认）、有的用制表符、有的给所有值加引号。RFC 4180 版本是通用语——按它输出，所有表格工具都能解析。

## 关键转换规则

把对象数组 JSON 转成 CSV 是三步活，每步都有陷阱：

**1. 检测表头。** 表头行是所有对象键的并集。陷阱：形状不一致的对象。`{"name":"A"}` 和 `{"name":"B","age":30}` 在同一个数组里，表头就是 `name,age`，第一行的 `age` 单元格为空。这本身没问题——但一个只出现在 10,000 个对象中*最后一个*里的键，会被只采样首行的转换器漏掉，导致列消失或顺序错乱。正确的转换器取全部键的并集。

**2. 转义值。** 数字和布尔值以文本形式通过。含逗号、引号或换行的字符串按 RFC 4180 加引号。陷阱：`null` 和 `undefined`。惯例是渲染为空单元格，但有些转换器会输出字面量 `"null"`——一个静默存活的脏数据 bug。

**3. 处理编码。** 痛点的本体。Excel 需要文件开头的 **UTF-8 BOM**（`\uFEFF`）才能识别 UTF-8；没有 BOM，Excel 会用系统代码页打开非 ASCII 文本，中文、日文和重音字符全部乱码。解法是机械的——前置 BOM——但只有知道要做的人才会做。本站[转换器](/zh/tools/json-to-csv/)自动加。

## 嵌套数据：先扁平化

CSV 是二维格式；JSON 是树。当对象值本身是对象或数组时，必须扁平化或字符串化：

```
{"user": "ada", "address": {"city": "Tokyo", "zip": "100-0001"}}
```

按优先级三个选项：

1. **点号扁平化** — `address.city`、`address.zip` 各自成列。嵌套形状一致时最佳
2. **字符串化进一个单元格** — `{"city":"Tokyo",...}` 作为字面 JSON 文本。嵌套部分在表格里几乎不被查询时
3. **丢弃** — 嵌套部分与分析无关时

用朴素的 `String(value)` 字符串化嵌套对象会得到 `[object Object]`——忘了这一步的转换器的签名。在 CSV 里看到 `[object Object]`，说明 JSON 从未被正确处理。

## CSV 选错目标的场合

CSV 的简单性是优点，直到数据超出它的承载。以下场景换别的：

- **深层或不规则嵌套。** 三层嵌套拍平成 40 列点号表头，比原始 JSON 还糟。用文档存储或 Parquet
- **数百万行。** 表格软件远不到百万行就卡死；CSV 没有 schema、没有类型、没有压缩。规模的归宿是 Parquet 或数据库
- **精度重要时。** 数字以文本形式在 CSV 里往返，被打开它的工具重新解析——64 位整数 ID 会在 Excel 里静默丢精度（与 [JSON 指南](/zh/blog/json-formatter-guide/)里的 2⁵³ 问题相同）
- **流式或增量更新。** CSV 是整文件格式；安全追加行需要重写逻辑，而这在数据库里免费

## 受益最大的工作流

**API 导出。** 每个 REST API 都返回 JSON 数组，每个业务用户都想要表格。一个小小的转换步骤，替代掉一堆「请给我做导出功能」的需求票。

**LLM 批量输出。** 结构化输出和批量任务的响应以 JSON 数组到达。转成 CSV 放进可审阅的表格——而这份输出的 token 成本可以用 [Token 费用计算器](/zh/tools/ai-token-cost-calculator/)测量。

**日志分析。** JSON Lines 日志每行一个 JSON 对象——离数组只有一步之遥。解析、转换、在表格里透视，小数据量下是条正当的快速分析路径。

## 完整流水线

1. 用 [JSON 格式化器](/zh/tools/json-formatter/)**校验**——因输入非法而失败的转换工具，会以令人困惑的方式浪费你的时间
2. 用 [JSON 转 CSV](/zh/tools/json-to-csv/)**转换**——键并集、转义、UTF-8 BOM 齐备
3. 在 Excel/Sheets 里**打开**，确认非 ASCII 文本存活——BOM 检查就是整场编码战斗
4. **归档** CSV 或继续传递；数据需要装进别的请求体时，[Base64 编码器](/zh/tools/base64-encoder/)负责打包

## 嵌套 JSON 转 CSV：完整实例

真实的 API 响应很少是扁平的。以 users 端点为例：

```json
[
  {"id": 1, "name": "Ada", "profile": {"city": "Tokyo", "plan": "pro"},
   "roles": ["admin", "editor"]},
  {"id": 2, "name": "Alan", "profile": {"city": "London", "plan": "basic"},
   "roles": ["viewer"]}
]
```

应用扁平化规则后得到：

| id | name | profile.city | profile.plan | roles |
|----|------|--------------|--------------|-------|
| 1 | Ada | Tokyo | pro | `["admin","editor"]` |
| 2 | Alan | London | basic | `["viewer"]` |

这里展示的决策：

- **`profile`** 用点号扁平化——它是形状一致的对象，`profile.city` 和 `profile.plan` 值得各自成列
- **`roles`** 字符串化——长度变化的数组没有稳定的列形状，于是以 JSON 字符串进一个单元格，需要的人仍可解析
- **`id`** 以文本通过——如果这些 ID 是超过 2⁵³ 的 64 位整数，这里正是精度陷阱咬人的地方；安全做法是让 ID 端到端保持字符串

一个会帮你扁平化的转换器需要明确两个决策：**嵌套策略**（点号 vs 字符串化 vs 丢弃）和**编码**（BOM 与否）。本站的 [JSON 转 CSV 转换器](/zh/tools/json-to-csv/)对嵌套值选择字符串化、BOM 始终开启——对大多数 API 导出都成立的务实默认。

## CSV 与 AI：批量输出、日志和 LLM 数据流水线

JSON→CSV 转换在 AI 相关工作中异常常见，集中在三个位置：

**结构化输出审阅。** 当 LLM 通过结构化输出模式返回 JSON 数组——比如 500 个抽取出的实体——最快的人工审阅循环是：用 [JSON 格式化器](/zh/tools/json-formatter/)校验 → 转 CSV → 打开表格 → 抽查行。表格审阅能抓住模式错误（某行缺字段、某个分类标签拼错），而盯 JSON 原文永远发现不了。

**批量任务检查。** OpenAI 风格的批量任务返回 `.jsonl` 文件——每行一个 JSON 对象。逐行解析后转换，整个任务就变成可审计的表格。每行的 token 用量就在请求体里；[Token 费用计算器](/zh/tools/ai-token-cost-calculator/)把这些数字变成钱。

**数据集准备。** 反向同样重要：表格训练数据常从电子表格开始，成为 CSV，再被解析成 JSON 进入微调或 RAG 流水线。掌握两个方向的转义规则，就能防止经典的「第 14,207 行有个未转义引号，整个导入错位」事故。

共同点：CSV 是审阅格式，JSON 是传输格式，可靠的转换器让两者之间的往返变得无聊——而无聊正是数据流水线环节能拥有的最好属性。

## 常见问题

{{< faq-schema >}}
[
  {"q": "如何把 JSON 数组转成 CSV？", "a": "把所有对象的键取并集作为表头行，按 RFC 4180 转义含逗号、引号或换行的值，每个对象写一行。AI Forward 的转换器完成这三步，并自动添加 Excel 友好的 UTF-8 BOM。"},
  {"q": "为什么中文或日文在 Excel 里变成乱码？", "a": "Excel 需要文件开头的 UTF-8 BOM 才能识别 UTF-8。没有它，Excel 按系统代码页解码字节，非 ASCII 文本就乱码。对策是在生成 CSV 时前置 BOM。"},
  {"q": "CSV 单元格里的 [object Object] 是什么意思？", "a": "嵌套 JSON 对象或数组被 JavaScript 默认的 String() 字符串化了，而不是 JSON.stringify 或扁平化。应把嵌套键拍平成点号列，或作为字面 JSON 字符串化。"},
  {"q": "值里的逗号在 CSV 里如何处理？", "a": "按 RFC 4180，含逗号、双引号或换行的值用双引号包裹，值内的引号加倍（\" 变 \"\"）。正确的转换器会自动处理。"},
  {"q": "CSV 能处理嵌套 JSON 吗？", "a": "原生不能。CSV 是二维的。嵌套对象要么用点号扁平化成独立列，要么作为 JSON 文本字符串化进单格，无关的话就丢弃。"},
  {"q": "什么时候不该用 CSV？", "a": "深层嵌套数据、数百万行、数值精度重要（64 位 ID）、数据流式增量更新时。这些场景用文档存储或 Parquet。"},
  {"q": "CSV 一定是逗号分隔吗？", "a": "实践中不一定。部分区域默认分号，部分工具用制表符，但 RFC 4180 的逗号分隔 CSV 是通用交换格式，所有表格工具都能解析。"}
]
{{< /faq-schema >}}

---

*CSV 规则依据 RFC 4180。Excel 的 UTF-8 BOM 行为依据 Microsoft Excel 文档化的文件格式行为。JSON 字符串化与精度行为依据 ECMAScript 规范。*
