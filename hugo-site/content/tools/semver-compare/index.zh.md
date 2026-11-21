---
title: "语义化版本对比与排序"
date: 2026-11-20
lastmod: 2026-11-21
description: "对比两个语义化版本（1.2.3 vs 1.2.4-rc.1）并升序排列版本列表。面向依赖管理的免费本地工具。"
tags: [semver对比, 版本对比, 语义化版本, 版本排序]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "semver-compare"
faq:
  - q: "遵循 SemVer 2.0.0 吗？"
    a: "是，包括预发布优先级：1.0.0-alpha < 1.0.0-beta < 1.0.0。"
  - q: "构建元数据怎么处理？"
    a: "按规范，加号后的元数据不参与优先级比较。"
  - q: "可以排序长列表吗？"
    a: "每行一个版本，按升序排列；无效行会被报告，而不是静默跳过。"
related: [text-diff, json-diff, regex-tester, comparison-table-generator]
---

对比两个语义化版本——包括 `-rc.1` 这类预发布标签——并把整个版本列表升序排列。规则遵循 [SemVer 2.0.0 规范](https://semver.org/)。完全在浏览器内运行。

<!--more-->

{{< semver-compare >}}

## 工作原理

版本逐字段比较（主版本、次版本、修订号），再按规范的「数字先于字母」规则比较预发布标识。与你的包管理器同款逻辑——解析器行为诡异时，把依赖版本贴进来。lockfile 对比用 [JSON 差异对比](/zh/tools/json-diff/)。
