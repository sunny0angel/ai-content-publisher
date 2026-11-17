---
title: "JWT 详解：JSON Web Token 实用指南"
date: 2026-11-17
lastmod: 2026-11-17
description: "JSON Web Token 的工作原理：结构、签名与验证、HS256 与 RS256、安全陷阱，以及不透明会话 token 更合适的场景。附免费 JWT 解码器。"
tags: [JWT详解, JSON Web Token, JWT安全, HS256 RS256, JWT最佳实践, 访问令牌, 刷新令牌, JWT解码器]
categories: ["AI Tools"]
images:
  featured_image: "/images/jwt-explained.jpg"
draft: false
authors: ["AI Forward"]
slug: "jwt-explained"
---

> **题图:** 一台显示安全锁图标的笔记本电脑。摄影：[Dan Nelson](https://www.pexels.com/photo/a-laptop-over-a-round-table-4973899/)（Pexels，免费使用）

JSON Web Token 是 Web 世界里最接近标准证件的东西：一份自包含、经过签名的文档，写着你是谁、你被允许做什么，在每个请求里往返于浏览器和服务器之间。它支撑着现代 API 和移动应用的大部分登录流程——同时，它也是一连串反复出现的真实安全事故的来源，因为 JWT *用起来*容易，*用对*却微妙。

本指南讲解 JWT 是什么、签名与验证如何真正运作、陷阱在哪里，以及什么时候该回头用朴素的不透明会话 token。要在浏览器里查看任何 token 的 header、payload 和 claims，用免费的 [JWT 解码器](/zh/tools/jwt-decoder/)。

## JWT 的解剖

JWT 是三个以点连接的 Base64url 编码部分：

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9  ← header
.eyJzdWIiOiIxMjM0NTY3ODkwIn0            ← payload
.s5T_6eJ7xQ8...                          ← signature
```

- **Header** — 元数据：签名算法（`alg`）和 token 类型（`typ`）。典型内容：`{"alg":"HS256","typ":"JWT"}`
- **Payload** — claims：身份（`sub`）、过期时间（`exp`）、签发方（`iss`）、受众（`aud`），加上应用自定义字段
- **Signature** — 用算法和密钥对前两部分计算得出。防篡改靠的就是它

注意解码做什么、不做什么。任何人都能对 header 和 payload 做 Base64url 解码——[JWT 解码器](/zh/tools/jwt-decoder/)干的正是这个，无需密钥。解码只能揭示 claims；**只有用正确密钥做签名验证**才能证明 claims 真实。两者被频繁混淆，而大多数「JWT 安全」事故来自只解码、不验证的系统。

## 签名与验证如何运作

**HS256**（HMAC-SHA256）使用单一对称密钥：

```
signature = HMAC-SHA256(secret, base64url(header) + "." + base64url(payload))
```

服务器用密钥签名，验证时重新计算。一个密钥，所有需要验证的各方共享——一旦泄露，任何人都能伪造 token。

**RS256**（带 SHA-256 的 RSA）使用私钥/公钥对：授权服务器用私钥签名，任何资源服务器用公钥验证。验证方无需分发任何敏感信息，因此 RS256 是多服务、多租户系统的标准，也是 OpenID Connect 提供方的必选。

服务器在每次请求上必须执行的验证清单：解析 → 验签 → 检查 `exp`（未过期）→ 检查 `iss`/`aud`（预期的签发方与受众）→ 然后才信任 claims。

## Claims：什么该放、什么不该放

值得了解的标准 claims：

| Claim | 含义 |
|-------|------|
| `sub` | 主体——用户/实体 ID |
| `iss` | 签发方——谁签的名 |
| `aud` | 受众——发给谁的 |
| `exp` | 过期时间（Unix 秒） |
| `iat` / `nbf` | 签发时间 / 生效时间 |

自定义 claims 的设计规则：**最小可用信息。** token 每次请求都要发送，每多一个 claim 就膨胀一圈；而且 token 里的 claim 客户端都能读到（记住：解码免费）。秘密——API key、密码哈希、卡号片段——绝不能出现在 JWT payload 里。一个带着 `"api_key": "..."` 的 token 不是「等待发生的 bug」，它就是 bug 本身。

## 安全陷阱排行榜

**1. 接受 `alg: "none"`。** 声明无算法的 token 必须无条件拒绝。历史上部分库曾放行——「alg none 攻击」——让攻击者彻底剥掉签名。要验证的是你期望的算法，而不是 token 声称的算法。

**2. 弱或泄露的 HS256 密钥。** 「secret」「changeme」和硬编码的演示密钥秒级可伪造。密钥至少 32 个随机字节，存环境变量，定期轮换。

**3. 把 token 存进 localStorage。** localStorage 可被同源任何脚本读取——意味着一个 XSS 漏洞立刻升级为 token 窃取。HttpOnly cookie 是更安全的传输方式；非用 header 不可，就把有效期设短。

**4. 长寿 token。** `exp` 为一年的 token，是失窃后能用一年的凭据。短命访问令牌（分钟级）加刷新令牌轮换，把爆炸半径缩到分钟。

**5. 不检查 `aud` 和 `iss`。** 为别的服务合法签发的 token 若被你的服务接受，就是跨服务伪造。两个字段都要查。

## 访问令牌 vs 刷新令牌

现代模式把凭据一分为二：

- **访问令牌** — 短命（5–60 分钟），随每个请求发送，授予实际 API 访问权
- **刷新令牌** — 长寿，保存在服务端或加固 cookie 中，只用于签发新的访问令牌，每次使用即失效（轮换）

这个拆分让短有效期变得实用：用户不必每五分钟重新登录，而失窃的访问令牌在攻击者动手前就已过期。JWT 很适合访问令牌这个角色；刷新令牌通常是存服务端的不透明值。

## 什么时候不该用 JWT

JWT 不是无条件的升级。不透明会话 token——服务端保存的随机 ID——在三种情况下胜过 JWT：需要即时**吊销**时（JWT 到 `exp` 前一直有效，除非加额外基础设施）、token 携带**大体积 claims** 时（每个请求带 5 KB 的 JWT 是纯开销）、**审计与控制**比无状态更重要时（服务端会话可集中一键吊销）。诚实的规则：单服务 + 数据库，不透明会话更简单更安全；JWT 的复杂度只在你有众多服务或多个信任域时才划算。

## 用 JWT 解码器调试

解开 401 之谜的最快路径：把 token 粘进 [JWT 解码器](/zh/tools/jwt-decoder/)，拿 `exp` 对比当前时间，确认 `aud`/`iss` 与你的服务匹配，核实 `alg` 是后端期望的那个。解码器自动把 `iat`/`exp` 转为当地时间，并完全在浏览器内运行——token 不会离开页面。它与 [Base64 工具](/zh/tools/base64-encoder/)（JWT 底层是 Base64url）和 [SHA 哈希生成器](/zh/tools/hash-generator/)（HS256 即 HMAC-SHA-256）是天然搭配。

## 实现验证：在每个语言里都成立的清单

无论什么技术栈，验证顺序相同——而且顺序很重要。常见的漏洞是只查 `exp` 不验签（或反过来）：

```
1. 按「.」切分 token，要求恰好三部分。
2. 拒绝你未配置的 alg——只接受允许列表
   （如 {"RS256"} 或 {"HS256"}），绝不接受 token 自己的声明。
3. 用正确的密钥对前两部分验证签名。
4. 解码 payload 并校验 exp：now >= exp 即拒绝
   （留小的时钟偏移容忍，例如 30 秒）。
5. 若存在 nbf 和 iat，校验其合理性。
6. 校验 iss 和 aud 与预期值一致。
7. 此时才读取 claims 并授权。
```

各生态库提示：

- **Node.js**：`jsonwebtoken` 是常见选择——显式传 `{ algorithms: ['RS256'] }`，不要用默认值
- **Python**：`PyJWT`；用 `jwt.decode(token, key, algorithms=["RS256"], audience=..., issuer=...)`
- **Go**：`golang-jwt/jwt`；用 `jwt.WithValidMethods` 只注册你使用的方法
- **Java**：`jjwt`（io.jsonwebtoken）；用 `Jwts.parser().verifyWith(key)` 要求特定算法

每个生态里反复出现的错误都一样：一个宽松配置，接受 token 声明的任何 `alg`。给算法做白名单，其余一切都会随这一个决定归位。

**密钥管理。** HS256 密钥存环境变量或密钥管理器，至少 32 随机字节，按计划轮换——留出重叠窗口让旧 token 在轮换期间仍可验证。RS256 密钥存在身份提供方或 JWKS 端点；资源服务器拉取公钥（或 JWKS 文档）并以短 TTL 缓存。两类密钥都不要嵌进应用代码或前端打包产物。

## 手读 token：解码器展示的东西

以这个最小 token 为例：

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJBZGEiLCJleHAiOjE3OTg3NTg0MDB9.sig
```

粘贴进 [JWT 解码器](/zh/tools/jwt-decoder/)会得到：

- **Header**：`{"alg":"HS256","typ":"JWT"}` — HMAC 签名、对称密钥
- **Payload**：`sub: 42`、`name: "Ada"`、`exp: 1798758400` — 解码后由工具转为当地时间
- **Signature**：为展示而截断——工具刻意不做验证，因为没有提供密钥

这个展示就是解码能给你的全部：结构和 claims。token 是否*有效*，只有持有密钥的服务器能回答——这个事实值得反复告诉那些以为把 token 粘进调试器就是「黑掉」什么的人。

## 常见问题

{{< faq-schema >}}
[
  {"q": "什么是 JWT？", "a": "JSON Web Token 是由 header、payload、signature 三部分组成的签名 Base64url 编码文档，由 RFC 7519 标准化。它携带身份与授权 claims，用密钥验证而非服务端查询。"},
  {"q": "任何人都能解码 JWT 吗？", "a": "能。header 和 payload 只是 Base64url 编码而非加密——任何人都能读。解码揭示 claims；只有用正确密钥做签名验证才能证明其真实。"},
  {"q": "HS256 和 RS256 有什么区别？", "a": "HS256 用同一个共享对称密钥签名和验证；RS256 用私钥签名、公钥验证。验证方无需持有秘密，因此多服务系统以 RS256 为标准。"},
  {"q": "什么是 alg:none 攻击？", "a": "声称 alg: none 的 token 要求验证方完全跳过签名检查。正确实现会无条件拒绝，只接受自己配置过的算法。"},
  {"q": "JWT 应该存 localStorage 吗？", "a": "不应该。同源任何脚本都能读 localStorage，XSS 漏洞会立即升级为 token 窃取。优先 HttpOnly cookie；必须用 header 的话，把寿命设短。"},
  {"q": "为什么要用刷新令牌？", "a": "让访问令牌保持短命：访问令牌几分钟过期，由另一个轮换的刷新令牌签发替代品。失窃的访问令牌因此只有几分钟价值。"},
  {"q": "什么时候不透明会话 token 比 JWT 好？", "a": "需要即时吊销、claims 体积大、或中央控制与审计更重要时。单服务 + 数据库通常更适合服务端不透明会话。"}
]
{{< /faq-schema >}}

---

*JWT 结构与 claims 依据 RFC 7519。HMAC/RSA 算法名依据 RFC 7518。OpenID Connect 签名要求依据 OpenID Connect Core 规范。*
