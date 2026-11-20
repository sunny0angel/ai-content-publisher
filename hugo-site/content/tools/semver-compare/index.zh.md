---
title: "语义化版本对比与排序"
date: 2026-11-20
lastmod: 2026-11-20
description: "对比两个语义化版本（1.2.3 vs 1.2.4-rc.1）并升序排列版本列表。面向依赖管理的免费本地工具。"
tags: [semver对比, 版本对比, 语义化版本, 版本排序]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "semver-compare"
---

对比两个语义化版本——包括 `-rc.1` 这类预发布标签——并把整个版本列表升序排列。规则遵循 [SemVer 2.0.0 规范](https://semver.org/)。完全在浏览器内运行。

<!--more-->

{{< semver-compare >}}

## 工作原理

版本逐字段比较（主版本、次版本、修订号），再按规范的「数字先于字母」规则比较预发布标识。与你的包管理器同款逻辑——解析器行为诡异时，把依赖版本贴进来。lockfile 对比用 [JSON 差异对比](/zh/tools/json-diff/)。
