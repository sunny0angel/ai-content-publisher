---
title: "Prompt 对比测试器"
date: 2026-11-19
lastmod: 2026-11-21
description: "把两个提示词并排发到任意 OpenAI 兼容 API，对比输出、token 用量和延迟。key 只留在你的浏览器——本站没有后端。"
tags: [提示词对比, 提示词测试, prompt A/B测试, LLM提示词测试, 提示词工程工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "prompt-compare"
faq:
  - q: "API 密钥保存在哪里？"
    a: "保存在你设备的浏览器 localStorage 中。只会发送到你填写的 API 端点，不会发送到本站。"
  - q: "支持哪些 API？"
    a: "任何兼容 OpenAI 的 /chat/completions 端点，包括 OpenAI、DeepSeek、Groq、Together 和本地服务。"
  - q: "为什么两次运行延迟不同？"
    a: "网络状况和服务商负载会波动。下结论前请多跑几次。"
  - q: "提示词会存到服务器吗？"
    a: "不会。本站没有后端，提示词只存在于页面中，请求直接发往服务商。"
related: [ai-token-cost-calculator, text-similarity, json-formatter, text-diff]
---

写两个提示词，把工具指向任意 OpenAI 兼容 API，并排运行两者——对比输出、token 用量和延迟。请求**从你的浏览器直连你的 API 服务商**；本站没有后端，永远看不到你的 key 和提示词。

<!--more-->

{{< prompt-compare >}}

## 工作原理

工具以标准聊天格式调用 `POST {base}/chat/completions`——适用于 OpenAI、DeepSeek 及大多数自托管和兼容端点。API key 和配置仅为方便存入 `localStorage`；离开共用电脑时请删除。系统提示词由两次运行共享，让对比恰好隔离「改了什么」。

## 该对比什么

- **措辞**：同一条指令换两种说法——哪种输出更听话？
- **格式**：要求 JSON 还是散文——结构能保持吗？
- **模型**：同一提示词换不同 `model`——配合 [Token 费用计算器](/zh/tools/ai-token-cost-calculator/) 还能给两边标价

提示词工程是可测量的。配合 [Markdown 预览器](/zh/tools/markdown-previewer/) 写结构化提示词；测试端点需要 token 时用 [JWT 签发工具](/zh/tools/jwt-signer/)。
