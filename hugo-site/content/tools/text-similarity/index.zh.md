---
title: "文本相似度检测器"
date: 2026-11-20
lastmod: 2026-11-20
description: "对比两段文本，得到带可视化进度条的相似度百分比。用于查重、去重和 diff 前置判断的免费本地工具。"
tags: [文本相似度, 相似度检测, 查重, 文本对比百分比]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "text-similarity"
---

粘贴两段文本，得到由最长公共子序列算法计算的相似度百分比和可视化进度条。适合检查改写、发现近似重复、在完整 diff 前做筛选。完全在浏览器内运行。

<!--more-->

{{< text-similarity >}}

## 工作原理

相似度 = LCS 长度 ÷ 较长文本长度。它衡量的是*序列重叠*——顺序很重要——因此改写但重排的文本比逐字复制得分低。行级增删由[文本差异对比](/zh/tools/text-diff/)精确展示；本工具先回答「有多少」。
