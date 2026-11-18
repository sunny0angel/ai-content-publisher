---
title: "Cron 表达式解析器"
date: 2026-11-18
lastmod: 2026-11-18
description: "把 cron 表达式翻译成通俗解释并显示接下来几次执行时间。支持 *、*/n、范围和列表。用于排程与调试的免费本地工具。"
tags: [cron解析, cron表达式, crontab, cron语法, 排程解析, cron测试, 开发者工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "cron-parser"
---

粘贴 cron 表达式——`*/15 * * * *`——即可看到逐字段解释，以及从本地时钟算出的接下来五次执行时间。完全在浏览器内运行。

<!--more-->

{{< cron-parser >}}

## 工作原理

标准 5 字段 cron 格式是 `分 时 日 月 星期`。工具解析每个字段——支持 `*`（每）、`*/n`（每隔 n）、`a-b`（范围）和 `a,b`（列表）——然后从当前时间逐分钟推进，收集五个匹配时刻。日与星期的组合遵循标准 OR 规则：**任一**字段匹配即触发。

## 你会遇到的场景

- **CI 流水线**：GitHub Actions 和 GitLab 的定时任务用 cron 语法
- **云 cron**：Cloudflare Cron Triggers、Vercel Cron——同一个 5 字段格式
- **服务器**：crontab 条目、systemd 定时器的前身

任务「没跑」时，bug 几乎总在表达式里而不是调度器上。动服务器之前先粘到这里看看接下来的执行时间。配合 [时间戳转换器](/zh/tools/timestamp-converter/)确认时区——cron 按服务器时区运行，那通常不是你的时区。
