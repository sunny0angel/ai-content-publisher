---
title: "Base64 编码与解码器"
date: 2026-11-17
lastmod: 2026-11-21
description: "完整支持 UTF-8 的 Base64 编码与解码。面向处理 API、JWT 和文本内嵌二进制数据的开发者的免费本地工具。"
tags: [Base64编码, Base64解码, Base64转换, URL安全Base64, 开发者工具]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "base64-encoder"
faq:
  - q: "支持日文、中文和 emoji 吗？"
    a: "支持。文本先转为 UTF-8 字节再编码，多字节字符可正确往返，这一点与 btoa() 不同。"
  - q: "Base64 是加密吗？"
    a: "不是。它是可逆的传输编码，任何人都能解码。保密需要 TLS 和真正的加密。"
  - q: "可以编码文件或图片吗？"
    a: "本工具只处理文本。图片请用「图片转 Base64」工具，它在本地读取文件并生成 data URL。"
related: [image-to-base64, url-encoder, hash-generator, jwt-decoder]
---

在纯文本与 Base64 之间互相转换，并正确处理 UTF-8——不同于 `btoa()`，本工具不会在中文、日文或 emoji 上出错。全部在浏览器本地运行，不会上传任何内容。

<!--more-->

{{< base64-encoder >}}

## 工作原理

Base64 用 64 个可打印 ASCII 字符（`A–Z`、`a–z`、`0–9`、`+`、`/`）加 `=` 填充来表达二进制数据。每 3 个输入字节变成 4 个输出字符——体积增加 33%，换来的是能安全通过纯文本通道传输：JSON 字符串、XML、邮件（MIME）、URL 参数。

本工具先把文本编码为 UTF-8 字节，再套用 Base64——这正是只会处理 Latin-1 的原生 `btoa()` 做不到的正确行为。解码过程相反。

## 你会遇到它的场景

- **JWT**：每个 JSON Web Token 的 header 和 payload 都是 Base64url 编码的 JSON，用 [JWT 解码器](/zh/tools/jwt-decoder/)可以解码
- **Data URL**：`data:image/png;base64,...` 把图片直接嵌进 HTML 和 CSS
- **API 请求体**：二进制数据（图片、证书、protobuf）在 JSON 里以 Base64 字符串传输
- **Basic 认证**：`Authorization: Basic base64(user:pass)`——这里的编码只是传输手段，不是安全措施，任何人都能解码

数据工作流的另一半——结构化记录转表格——见 [JSON 转 CSV](/zh/tools/json-to-csv/)。


想深入了解编码本身，请阅读 [Base64 编码详解](/zh/blog/base64-encoding-explained/)。
