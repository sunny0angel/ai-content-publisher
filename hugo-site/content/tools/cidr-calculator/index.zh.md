---
title: "CIDR 子网计算器"
date: 2026-11-19
lastmod: 2026-11-21
description: "计算任意 IPv4 CIDR 的网络、广播、主机范围、子网掩码、通配符和子网拆分。面向网络工程师与开发者的免费本地工具。"
tags: [CIDR计算, 子网计算, 子网掩码计算, IPv4子网, IP范围计算, 网络工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "cidr-calculator"
faq:
  - q: "支持 IPv6 吗？"
    a: "不支持，仅 IPv4。覆盖 /0 到 /32 的所有前缀，包括 /31 和 /32 边界情况。"
  - q: "拆分表显示什么？"
    a: "把地址块分成 8 个更小的子网（前缀 +3），便于快速规划分配。"
  - q: "结果是精确的吗？"
    a: "是。位运算使用 BigInt，不存在浮点舍入。"
related: [number-base-converter, hash-generator, url-encoder, password-generator]
---

输入 `192.168.1.0/24` 这样的 IPv4 CIDR，即可获得全部信息：网络与广播地址、首末主机、可用数量、子网与通配符掩码、类别，以及现成的更小子网拆分表。全部用 BigInt 精确位运算在本地完成。

<!--more-->

{{< cidr-calculator >}}

## 工作原理

工具把 IP 转成 32 位整数，由前缀长度导出掩码，用 `BigInt` 位运算计算网络/广播/主机范围——从 /0 到 /32 全精确，包括边界情况（/31 点对点链路、/32 单主机）。子网拆分表把地址块分成 8 个更小的子网（前缀 +3），一眼规划分配。

## 帮你省时间的场景

- **网络规划**：把办公网段按部门拆分子网
- **云与 VPC 设计**：创建网段之前，先验证范围装得下实际需要的主机数
- **排障**：判断两个地址是否同属一个子网——「连不上对面那台机器」的经典问题

同一套基础设施排障流程里，[时间戳转换器](/zh/tools/timestamp-converter/)和 [Cron 解析器](/zh/tools/cron-parser/)就在旁边。
