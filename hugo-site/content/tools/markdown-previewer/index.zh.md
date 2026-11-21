---
title: "Markdown 预览器"
date: 2026-11-19
lastmod: 2026-11-21
description: "浏览器内实时双栏 Markdown 预览——标题、列表、代码块、引用、链接、图片。无上传的免费本地工具。"
tags: [Markdown预览, Markdown编辑器, Markdown转HTML, 实时Markdown, 开发者工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "markdown-previewer"
faq:
  - q: "支持哪些 Markdown 功能？"
    a: "标题、强调、行内与围栏代码、链接、图片、列表和引用。表格、脚注和原始 HTML 直通不在支持范围。"
  - q: "原始 HTML 会被渲染吗？"
    a: "不会。先转义 HTML，粘贴的标记保持惰性，无法注入脚本。"
  - q: "文档会自动保存吗？"
    a: "不会。内容只存在于标签页，关闭前请复制出去。"
related: [text-diff, sql-formatter, lorem-ipsum-generator, case-converter]
---

左边写 Markdown，右边实时看到渲染结果——无需构建、无需服务器。覆盖日常子集：标题、强调、行内与围栏代码、链接、图片、列表、引用。

<!--more-->

{{< markdown-previewer >}}

## 工作原理

预览器先把原始 HTML 转义（粘贴进来的标记保持惰性），再套用一个小型块级解析器：围栏代码块、标题、列表、引用、段落——随后是每个块内的行内格式化（代码、粗体、斜体、链接、图片）。它是面向常用 90% 的*预览*引擎，不是完整的 CommonMark 实现：表格、脚注和 HTML 直通刻意不在范围内。

## 什么时候用得上

- **草拟 README 和注释**，推送仓库之前先看效果
- **检查文档文字**，跑不了站点构建的时候
- **用 Markdown 写 LLM 提示词**，确认结构读起来符合预期——配合 [Prompt 对比测试器](/zh/tools/prompt-compare/) 完成整套 AI 工作流

同一工具链里的 JSON 和 SQL 有 [格式化器](/zh/tools/json-formatter/) 和 [SQL 格式化器](/zh/tools/sql-formatter/) 兜底。
