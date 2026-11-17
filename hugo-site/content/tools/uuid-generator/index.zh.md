---
title: "UUID 生成器"
date: 2026-11-17
lastmod: 2026-11-17
description: "批量生成 RFC 9562 第 4 版 UUID，支持大小写。基于 Web Crypto API 的浏览器本地生成，无服务器交互、无追踪，完全免费。"
tags: [UUID生成器, GUID生成, UUID v4, RFC 9562, 随机ID, UUID在线工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "uuid-generator"
---

一次最多生成 100 个 v4 UUID，可选择小写或大写。ID 通过 Web Crypto API（`crypto.getRandomValues` / `crypto.randomUUID`）在浏览器本地生成，不会向外部发送任何请求，实际应用中也不会发生碰撞。

{{< uuid-generator >}}

## 什么是 UUID

UUID（通用唯一标识符）是以 36 个字符表示的 128 位值，形如 `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`。第 4 版 UUID 由 122 位随机数生成，共 2¹²² 种可能取值——即使每秒生成数十亿个，碰撞概率也可以忽略。格式由 [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562) 标准化，2024 年的修订还新增了按时间排序的第 6、7 版。

## v4 还是 v7？

- **v4（本工具）**：完全随机。简单、分布均匀，是大多数场景的稳妥默认值
- **v7**：构造上按时间排序，能大幅提升 PostgreSQL 等数据库的主键插入性能——顺序键可以减少索引碎片。2026 年新建数据表时优先考虑 v7

如果 UUID 要作为数据库主键，建议在服务端生成 v7。API token、会话 ID 等不希望暴露创建顺序的标识符，v4 是更好的选择——随机性会隐藏生成顺序。

## 实用场景

- **数据库主键**：`INSERT INTO users (id, name) VALUES ('<uuid>', 'Ada');`
- **API 幂等键**与请求关联 ID
- **上传文件名**：绝不允许冲突的场景
- **测试数据**：批量生成后组装进 JSON 请求体，可与 [JSON 格式化器](/zh/tools/json-formatter/)配合使用

想深入了解各版本的差异与数据库性能影响，见 [UUID 是什么？版本、使用场景与最佳实践](/zh/blog/what-is-a-uuid/)。
