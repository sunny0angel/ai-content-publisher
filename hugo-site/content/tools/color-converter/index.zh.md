---
title: "颜色转换器（HEX / RGB / HSL）"
date: 2026-11-18
lastmod: 2026-11-18
description: "在 HEX、RGB、HSL 之间转换颜色，带实时预览色块。面向设计与前端工作的免费本地工具。"
tags: [颜色转换, hex转rgb, rgb转hsl, 颜色选择, hex颜色, hsl转换, 设计工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "color-converter"
---

输入任意格式的颜色——HEX（`#2563eb`）、RGB（`rgb(37,99,235)`）或 HSL（`hsl(221,83%,53%)`）——即可看到三种格式和实时预览色块。完全在浏览器内运行。

<!--more-->

{{< color-converter >}}

## 工作原理

工具解析你输入的格式，经由内部 RGB 表示转换，再渲染全部三种格式。转换遵循标准 CSS Color Module 公式——与浏览器在样式表里求值 `hsl()` 时用的是同一套。

## 你会遇到的场景

- **主题设计**：设计系统用一种格式存储，工具要求另一种——Tailwind 就同时说 HEX 和 RGB
- **设计交接**：Figma 导出 HEX，有些图表库要 HSL
- **深色模式微调**：只调 HSL 的亮度可以保持色相——提交数值前先看清楚

与 [密码生成器](/zh/tools/password-generator/) 凑成前端工具包；把颜色当原始十六进制数看待时，[进制转换器](/zh/tools/number-base-converter/) 也能帮上忙。
