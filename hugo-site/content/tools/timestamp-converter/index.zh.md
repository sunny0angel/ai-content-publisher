---
title: "Unix 时间戳转换器"
date: 2026-11-18
lastmod: 2026-11-21
description: "把 Unix 时间戳（秒或毫秒）即转为本地时间、UTC 和 ISO 8601，或一键获取当前时间戳。免费本地工具。"
tags: [unix时间戳转换, epoch转换, 时间戳转日期, unix时间, epoch时间, 日期转换, 开发者工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "timestamp-converter"
faq:
  - q: "会自动区分秒和毫秒吗？"
    a: "会。10 位按秒处理，13 位按毫秒处理。"
  - q: "会显示哪些时区？"
    a: "本地时间、UTC 和 ISO 8601，便于直接对比服务器日志与本机时间。"
  - q: "会有 2038 年问题吗？"
    a: "JavaScript 日期是 64 位，可处理远超 2038 年的日期；限制只存在于 32 位 time_t 系统。"
related: [cron-parser, date-interval-calculator, uuid-generator, jwt-decoder]
---

粘贴 Unix 时间戳——秒或毫秒均可——即刻看到本地时间、UTC、ISO 8601，以及「2 小时前」这样的相对时间。一键获取当前时间戳。全部在浏览器内运行。

<!--more-->

{{< timestamp-converter >}}

## 工作原理

Unix 时间统计自 1970-01-01 00:00:00 UTC 以来的秒数——这是日志、API 响应、JWT 的 `exp` claim、数据库背后的时钟格式。工具自动识别输入是秒（10 位）还是毫秒（13 位），并用浏览器原生日期处理完成转换。

## 你会遇到的场景

- **日志**：一处是 `2026-11-18T10:32:00Z`，另一处是 `1764733320`
- **JWT claims**：`iat` 和 `exp` 是 Unix 秒——[JWT 解码器](/zh/tools/jwt-decoder/)也帮你转换
- **API 分页**：游标常常是时间戳；本工具告诉你它们的含义
- **任务调度**：cron 和批量任务都用 epoch 时间——配合 [cron 解析器](/zh/tools/cron-parser/)使用

没有上下文的时间戳是模糊的——工具同时显示本地时区和 UTC，让「凌晨 3 点还是下午 3 点」的误会消失。
