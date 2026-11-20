---
title: "JSON 差异对比工具"
date: 2026-11-20
lastmod: 2026-11-20
description: "对比两个 JSON 文档，按路径高亮新增、删除和变更字段。数据不出页面的免费本地工具。"
tags: [JSON对比, JSON diff, JSON差异, JSON比较工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "json-diff"
---

粘贴两个 JSON 文档——部署前后的 API 响应、配置变更、两个环境——即可看到哪些字段被新增、删除或修改，并带完整路径。完全在浏览器内运行。

<!--more-->

{{< json-diff >}}

## 工作原理

工具解析两个文档并递归遍历，逐键比较对象、逐元素比较数组。变更值显示 `路径: 旧 → 新` 的完整变化，新增与删除分别标绿和标红。对比文本而非 JSON 用[文本差异对比](/zh/tools/text-diff/)；对比前先用 [JSON 格式化器](/zh/tools/json-formatter/)校验两侧。
