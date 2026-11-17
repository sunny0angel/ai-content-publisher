---
title: "How to Calculate AI API Costs in 2026: A Practical Guide for Developers"
date: 2026-11-17
lastmod: 2026-11-17
description: "Learn how to calculate AI API costs the right way: token counting, input vs output pricing, caching, and batch discounts. Worked examples for GPT-5.6 and DeepSeek V4 with a free cost calculator."
tags: [AI API cost, token cost calculator, LLM pricing, GPT-5.6 pricing, DeepSeek V4 pricing, API cost optimization, token counting, AI cost estimate]
categories: ["AI Tools"]
images:
  featured_image: "/images/how-to-calculate-ai-api-costs.jpg"
draft: false
authors: ["AI Forward"]
slug: "how-to-calculate-ai-api-costs"
---

> **Featured image:** A person calculating at a desk with a laptop, calculator, and notebook. Photo by [Mikhail Nilov](https://www.pexels.com/photo/person-using-a-calculator-and-a-laptop-8296991/) on Pexels (Free to use).

Every AI application that survives contact with production eventually confronts the same spreadsheet: how much does an API call actually cost? The question sounds simple, but most teams get the answer wrong — not because the arithmetic is hard, but because the pricing model has enough moving parts that intuition fails. A team that budgets $500 per month for inference and lands at $4,300 usually made one of three mistakes: they counted tokens wrong, they ignored the input/output price split, or they assumed the list price is what they would pay.

This guide walks through the exact calculation, with worked examples using the official list prices of OpenAI's GPT-5.6 family and DeepSeek's V4 family as of August 2026, and shows how to turn the math into a budgeting discipline. If you want to skip the theory and just run the numbers, our free [AI Token & API Cost Calculator](/tools/ai-token-cost-calculator/) does the whole calculation in your browser.

## Why API Cost Estimates Are Usually Wrong

Before the formula, the diagnosis. Three failure modes explain most cost overruns in AI applications:

**1. Token counts are estimated from the wrong base.** People budget with "average request size" numbers they invented during prototyping, then ship a prompt that is five times longer — system instructions, tool schemas, retrieval context, conversation history. Every additional token in the input is billed on every request, forever.

**2. Input and output are priced completely differently.** On GPT-5.6 Sol, output tokens cost six times more than input tokens ($30 vs $5 per million). An application that generates long outputs — reports, code, translations — is dominated by output pricing, while a RAG application that stuffs documents into the context is dominated by input pricing. Applying one blended number to both is how estimates drift 3–5x.

**3. Caching, batching, and tiers are ignored.** OpenAI offers automatic prompt caching discounts for repeated prefixes, and DeepSeek offers discounted pricing for cache hits. Both providers reward batch processing. List prices are a starting point, not your invoice.

## The Core Formula

The cost of one API call is:

```
cost = (input_tokens ÷ 1,000,000 × input_price)
     + (output_tokens ÷ 1,000,000 × output_price)
```

Prices are quoted per million tokens. The formula looks trivial; the difficulty is feeding it accurate numbers. Let's go through each term.

### Step 1: Count the tokens correctly

You cannot divide character count by four and call it done — that heuristic is within ±10–30% for English prose, but Japanese, Chinese, and code can differ by far more. Tokenization splits text into subword units, so one CJK character is often one token while one English word is often 1.3–1.5 tokens.

Three ways to get exact numbers:

- **OpenAI**: the `tiktoken` Python library with the correct encoding for your model (`o200k_base` for GPT-5.6-class models).
- **Anthropic**: the `claude-tokenizer` package or the API's `count_tokens` endpoint.
- **DeepSeek**: the tokenizer endpoint in the API docs, or OpenAI-compatible `tokenizer` responses.

A practical rule of thumb that holds across providers: budget your input at **characters ÷ 3.5** for mixed English text and **characters ÷ 2.5** for code-heavy payloads. Then re-measure with the real tokenizer before signing any infrastructure commitment.

### Step 2: Use the actual price table

List prices as of August 2026, per one million tokens:

| Model | Input ($/1M) | Output ($/1M) | Output/Input ratio |
|-------|-------------|---------------|--------------------|
| GPT-5.6 Sol | $5.00 | $30.00 | 6.0x |
| GPT-5.6 Terra | $2.00 | $12.00 | 6.0x |
| GPT-5.6 Luna | $0.20 | $1.20 | 6.0x |
| DeepSeek V4 Pro | $0.435 | $0.87 | 2.0x |
| DeepSeek V4 Flash | $0.14 | $0.28 | 2.0x |

Source: [OpenAI platform pricing](https://platform.openai.com/docs/pricing) and [DeepSeek API docs](https://api-docs.deepseek.com/quick_start/pricing), retrieved August 2026. The US-China gap is structural — our full [GPT-5.6 vs DeepSeek-V4 pricing analysis](/blog/gpt-5.6-vs-deepseek-v4-pricing-2026/) shows the same $100 budget buys 107x more output tokens on DeepSeek V4 Flash than on GPT-5.6 Sol.

### Step 3: Work an example

Suppose you ship a support chatbot: 2,000-token system prompt, 1,500 tokens of retrieved context, 300 tokens of user message, and a 400-token average response. On GPT-5.6 Luna (the budget tier):

```
input  = 2,000 + 1,500 + 300 = 3,800 tokens
output = 400 tokens
cost   = (3,800 ÷ 1M × $0.20) + (400 ÷ 1M × $1.20)
       = $0.00076 + $0.00048
       = $0.00124 per request
```

At 10,000 conversations per day, that is $12.40 per day, or **about $372 per month** on Luna. The same workload on Sol costs $4,650 per month — a 12.5x difference from a pricing-tier choice alone, before any prompt optimization. This is why model selection is the highest-leverage cost decision you will make.

## The Four Levers That Actually Move Costs

Cost control is not about shaving tokens one by one; it is about structural choices. In order of impact:

**1. Model tier selection (10–100x).** The difference between Sol and Luna, or between Sol and DeepSeek V4 Flash, dwarfs every other lever. Route simple tasks to cheap models and reserve frontier models for tasks that genuinely need them. Multi-model routing is now standard practice among teams running AI at scale, as documented in our [open source vs proprietary AI analysis](/blog/open-source-vs-proprietary-ai-market-shift-2026/).

**2. Prompt caching (up to 50–90% off repeated prefixes, depending on provider).** OpenAI and DeepSeek automatically cache input prefixes that repeat across requests and bill cache hits at a discount versus full input pricing. Anthropic bills cache reads at roughly 10% of the standard input price. Structure your prompts so the system message and retrieved context sit at the beginning, unchanged.

**3. Batch processing (25–50% off).** OpenAI's Batch API and DeepSeek's batch pricing apply discounts to workloads that can wait up to 24 hours. Classification runs, backfills, and evaluation jobs rarely need real-time responses.

**4. Output length control (2–10x).** Enforce `max_tokens` limits, use structured output modes, and instruct concise answers. Output is the most expensive token on OpenAI models, so trimming output pays twice: fewer tokens billed, and shorter latency.

## Building the Budget Model

A budget that survives production needs three numbers per feature: request volume, token profile (input/output split), and model tier. Track them in a table:

| Feature | Requests/day | Input tokens | Output tokens | Model | Monthly cost |
|---------|-------------|--------------|---------------|-------|--------------|
| Support bot | 10,000 | 3,800 | 400 | Luna | ~$372 |
| Doc summarizer | 500 | 12,000 | 1,500 | Terra | ~$240 |
| Code review | 2,000 | 8,000 | 2,000 | Sol | ~$3,720 |

The uncomfortable row is usually the last one. When a single feature dominates the budget, that is where routing to a cheaper tier or an open-weight model produces the largest return.

Use the [token cost calculator](/tools/ai-token-cost-calculator/) to experiment with these numbers directly — paste a real payload, switch models, and watch the monthly projection move. Then multiply by 1.3: every team underestimates volume in the first quarter.

## Estimating Token Counts for Your Specific Workload

Every workload has a characteristic token profile. Knowing yours is the difference between an estimate and a guess. Typical profiles, measured on real applications:

| Workload | Typical input | Typical output | Dominant side |
|----------|--------------|----------------|---------------|
| Chat support (RAG) | 3,000–6,000 | 200–600 | Input |
| Document Q&A (large corpus) | 8,000–30,000 | 300–800 | Input |
| Summarization | 8,000–30,000 | 500–1,500 | Output |
| Code generation | 2,000–10,000 | 800–3,000 | Output |
| Translation | 2,000–15,000 | ≈ input size | Balanced |
| Agent loops (function calling) | 3,000–8,000 per step | 200–800 per step | Input, multiplied by steps |

Three disciplines turn these profiles into a working budget:

1. **Measure before you estimate.** Run your real prompts through the official tokenizer once, and record the numbers in the same table you use for pricing. The act of measuring changes every assumption.
2. **Log tokens in production.** Every request should record `prompt_tokens` and `completion_tokens` from the API response. Providers return them on every call — logging them is free, and it converts guesswork into a time series.
3. **Set alerts on drift.** When a prompt edit adds 2,000 tokens, nobody notices in the diff. A weekly chart of average tokens per request catches it in seconds. The same alert works for output length: a model that starts answering in bullet-point novels doubles your bill before anyone reads the logs.

## The Discount Layer: Caching, Batching, and Tiers

List prices are the ceiling, not the bill. Three mechanisms discount them, and the math is worth running once:

**Prompt caching.** Providers cache the prefix of your input that repeats across requests. When the prefix is identical, the cache hits: OpenAI bills cached input tokens at a discount (historically 50% for eligible long prompts), Anthropic bills cache reads at roughly 10% of the standard input price, and DeepSeek prices cache hits far below its already-low input rate. A 4,000-token system-and-context prefix that repeats across 10,000 requests per day is 40 million input tokens per day at full price. A 50–90% discount on that prefix is often the single largest line-item saving available, and it requires zero prompt engineering beyond keeping the prefix byte-identical.

**Batch APIs.** OpenAI's Batch API and DeepSeek's batch pricing cut list prices by roughly half for workloads that can wait up to 24 hours. Classification backfills, nightly embeddings, evaluation suites, and report generation are the classic candidates.

**Throughput tiers and commitments.** Both providers offer committed-use and provisioned-throughput pricing for sustained workloads. These require contractual commitment and make sense only after you have three months of real usage data — signing early locks in the wrong number.

The practical order: fix the prompt structure first (caching is free), move eligible jobs to batch (one API change), and only then negotiate tiers (a contract).

## From Prototype to 1 Million Requests: A Budget Walkthrough

Take a product that starts at 10,000 requests per day with a 4,000-token input and 500-token output on GPT-5.6 Luna:

```
cost per request = (4,000 ÷ 1M × $0.20) + (500 ÷ 1M × $1.20)
                 = $0.0008 + $0.0006 = $0.0014
monthly cost     = $0.0014 × 10,000 × 30 ≈ $420
```

Six months later, traffic has grown 5x to 50,000 requests per day. The honest projection is **$2,100 per month** — the cost grows linearly, which is the uncomfortable property of metered inference. Now apply the levers in order:

1. **Route 60% of traffic** (simple Q&A) to DeepSeek V4 Flash at $0.14/$0.28: that slice drops from ~$1,260 to ~$105.
2. **Cache the shared prefix**: the 40% still on Luna gets a 50% discount on its 4,000-token prefix, saving roughly $250 more.
3. **Batch the nightly report job**: another $60 saved.

The same product at the same traffic goes from $2,100 to about $700 — a 3x reduction, achieved with zero prompt changes and one routing decision. That is the entire discipline in one example: **price per token is a supplier fact; cost per request is an engineering choice.**

## Operationalizing the Budget: Dashboards, Alerts, and the Price War

A cost model is worthless if nobody looks at it. The systems that keep AI bills under control share four habits:

**Per-feature usage tags.** OpenAI lets you attach metadata to API requests; Langfuse and Helicone (both open source) do the same across providers. Tag every request with the feature that initiated it, and your cost dashboard stops being one number and becomes a ranked list of cost centers. Most teams discover that two features out of twenty drive 80% of the bill — a fact that only becomes visible with tagging.

**Budget alerts at 50 / 80 / 100%.** Every provider console supports usage alerts, and the open-source trackers add anomaly detection on top. Set the first alert low enough that you can still act. The standard failure story is not "we never checked" — it is "we checked after the invoice."

**A cost-per-unit metric, not a monthly total.** Cost per conversation, per document processed, per thousand tokens of user-facing value: some unit that scales with business success rather than hiding it. A monthly total that grows because your product is growing is good news; the same total growing while usage is flat is a bug in your prompt. The unit metric distinguishes the two in one glance.

**Quarterly re-forecasting, because prices only fall.** This is the structural fact of the 2026 market: the [US-China price gap](/blog/gpt-5.6-vs-deepseek-v4-pricing-2026/) is wide enough — 107x at the extremes — that list prices are falling every quarter as Chinese open-weight models force the whole market down. A budget built on today's prices is an overestimate in six months. The implication runs both ways: do not sign long-term commitments at today's rates, and re-run your model-selection decision every quarter. The cheapest correct model this quarter may not be the frontier model you defaulted to last quarter.

One more habit that pays for itself: keep a plain-text file of every prompt change with a note of its token impact. Cost regressions, like performance regressions, are almost always introduced by a well-intentioned edit. The file turns "why did the bill jump" from an investigation into a lookup.

## A Glossary of Pricing Terms That Appear on Your Invoice

Provider invoices use a vocabulary worth learning once, because each term hides a cost decision:

- **Token** — the billing unit. A subword fragment; ~4 characters of English text.
- **Input / output tokens** — tokens you send versus tokens the model generates. Outputs are priced higher on every major provider because generation is sequential.
- **Context window** — the maximum input a model accepts in one call. Larger windows enable longer documents but bill the full input every call — a 128K context stuffed with 100K tokens costs 25x a 4K context on the same task.
- **Cached tokens** — input prefix tokens the provider stores and re-bills at a discount when they repeat across requests. Keep stable prefixes at the front of the prompt.
- **Batch pricing** — discounted rates for jobs that can wait (up to 24 hours on OpenAI). The trade is latency for a roughly 50% price cut.
- **TPM / RPM** — tokens per minute / requests per minute rate limits. They are not costs, but they set the ceiling on how fast you can spend, and higher tiers carry different prices.
- **Committed use / provisioned throughput** — contractual capacity at a discounted rate. Only worth it with months of stable usage data.
- **Fine-tuning cost** — training tokens billed separately from inference, plus storage for the resulting model. Small fine-tunes are cheap; the recurring cost people forget is inference on a fine-tuned model at a premium per-token rate.

Reading your first invoice line-by-line against this glossary is the fastest way to find the number that does not belong — every team that does this finds one.

## Frequently Asked Questions

{{< faq-schema >}}
[
  {"q": "How do I calculate the cost of one AI API call?", "a": "Multiply input tokens by the input price per million tokens, multiply output tokens by the output price per million, and add the two: cost = (input_tokens / 1,000,000 × input_price) + (output_tokens / 1,000,000 × output_price). Example: 3,800 input tokens and 400 output tokens on GPT-5.6 Luna ($0.20/$1.20 per million) costs about $0.00124."},
  {"q": "Why are output tokens more expensive than input tokens?", "a": "Generating tokens requires the model to run sequentially, one token at a time, which uses more compute per token than processing input in parallel. On OpenAI's GPT-5.6 models the output price is 6x the input price; on DeepSeek V4 it is 2x. Applications with long outputs are therefore dominated by output cost."},
  {"q": "How many tokens is 1,000 words?", "a": "For English prose, 1,000 words is roughly 1,300–1,500 tokens using modern subword tokenizers. For Japanese or Chinese text, count characters more than words — one CJK character is often one token, so 1,000 Chinese characters is roughly 800–1,000 tokens."},
  {"q": "Does prompt caching really reduce AI API costs?", "a": "Yes. OpenAI and DeepSeek automatically cache input prefixes that repeat across requests and bill cache hits at a large discount versus full input pricing. Keeping the system prompt and retrieved context at the start of every request, unchanged, maximizes the cache hit rate."},
  {"q": "How much does DeepSeek V4 cost compared to GPT-5.6?", "a": "DeepSeek V4 Flash costs $0.14 per million input tokens and $0.28 per million output tokens. GPT-5.6 Sol costs $5.00 and $30.00. The same $100 budget buys roughly 357 million output tokens on V4 Flash versus 3.3 million on Sol — a 107x difference."},
  {"q": "What is the cheapest way to run an AI application?", "a": "Route simple tasks to a budget tier such as GPT-5.6 Luna or DeepSeek V4 Flash, cache repeated input prefixes, batch non-urgent workloads, and cap output lengths. Tier selection alone typically changes cost by 10–100x, far more than any token-by-token optimization."},
  {"q": "How accurate is the 4-characters-per-token estimate?", "a": "For English prose it is within roughly ±10–30%. For CJK text and code-heavy payloads the error can be larger because subword tokenizers compress repeated patterns. Use the official tokenizer libraries (tiktoken for OpenAI) for exact counts before committing to a budget."}
]
{{< /faq-schema >}}

---

*Prices are official list prices from [OpenAI platform pricing](https://platform.openai.com/docs/pricing) and [DeepSeek API docs](https://api-docs.deepseek.com/quick_start/pricing), retrieved August 2026. Actual invoices vary with caching, batch discounts, and throughput tiers. All dollar figures in USD.*
