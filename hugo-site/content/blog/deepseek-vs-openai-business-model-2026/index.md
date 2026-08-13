---
title: "How Do DeepSeek and OpenAI Make Money? A US-China Business Model Comparison"
date: 2026-08-13
lastmod: 2026-08-13
description: "OpenAI made $13.1B in 2025 and lost $9B. DeepSeek reports no revenue at all and says it has no commercialization plans. Yet DeepSeek forced Nvidia to lose $600B in one day. Two radically different AI business models explained with data."
tags: [DeepSeek, OpenAI, AI business model, AI revenue, OpenAI revenue, DeepSeek valuation, US China AI, AI economics]
categories: ["AI Industry Analysis"]
images:
  featured_image: "/images/deepseek-vs-openai-business-model-2026.jpg"
draft: false
authors: ["AI Forward"]
slug: "deepseek-vs-openai-business-model-2026"
---

> **Featured image:** Young strategist in a turtleneck analyzing financial growth trends on a digital screen. Photo by [Mikhail Nilov](https://www.pexels.com/photo/a-man-in-a-turtleneck-sweater-looking-at-a-graph-9301843/) on Pexels (Free to use).

The two most-watched AI companies in the world make money in almost opposite ways. OpenAI reported $13.1 billion in 2025 revenue but lost an estimated $9 billion, then crossed $20 billion in annualized revenue by early 2026 and is preparing an IPO at a reported $852 billion valuation. DeepSeek, owned by the Chinese hedge fund High-Flyer, reports no revenue at all, has publicly said it has no immediate commercialization plans, and was valued at around $10 billion in an April 2026 funding discussion. One company is the most valuable private startup in history; the other forced Nvidia to lose $600 billion of market value in a single day with a model it gave away free.

This analysis compares the two business models with hard numbers: revenue, losses, funding, valuation, headcount, training costs, and pricing strategy. It draws on OpenAI's public disclosures and press coverage collected in its [Wikipedia profile](https://en.wikipedia.org/wiki/OpenAI), DeepSeek's [Wikipedia profile](https://en.wikipedia.org/wiki/DeepSeek), and reporting from Reuters, Bloomberg, the Financial Times, and CNBC.

## What Is OpenAI's Business Model in 2026?

OpenAI's model is a classic high-growth tech play: lose money aggressively to capture market share, then monetize a massive user base across subscriptions, enterprise contracts, API usage, and — newly — advertising. The company has 700 million weekly ChatGPT users and roughly 20 million paying subscribers, and it now generates revenue from four streams.

| Revenue stream | How it works | Scale |
|----------------|--------------|-------|
| ChatGPT subscriptions | Plus and Pro tiers ($20–$200/month) | ~20M paying users |
| Enterprise & teams | Business plans sold to companies | ~5M enterprise users |
| API usage | Pay-per-token model access | Powering most of the market |
| Advertising (new) | Ads inside ChatGPT | ~$2.5B projected for 2026 |

The headline numbers are the ones that get attention. OpenAI reported $13.1 billion in revenue for 2025, more than triple the prior year, and its CFO said annualized revenue crossed $20 billion in January 2026. The company projects roughly $200 billion in annual revenue by 2030. But those numbers sit on top of a brutal cost structure: an estimated $9 billion net loss in 2025, spending projected to reach $17 billion in 2026, and cumulative spending of roughly $115 billion through 2029. OpenAI's bet is that the subscriber and enterprise base grows fast enough that it turns cash-flow positive by 2029 and "wildly profitable" shortly after.

The subscription layer is the foundation. ChatGPT Pro, launched in December 2024 at $200 per month, was the company's clearest attempt to monetize its most power users, and features like the Operator agent tool have been gated to that tier to justify the price. Below that, ChatGPT Plus serves the mass market of power users, and the free tier remains the funnel that feeds the entire pyramid. The arithmetic is straightforward: 700 million weekly users converting even a few percent into paid plans produces a subscription base measured in the tens of millions.

Enterprise is where the revenue is scaling fastest. OpenAI reports roughly 5 million enterprise users, and business plans convert the free funnel into contracted spend — the kind of revenue that banks and CFOs like because it is predictable. Meanwhile the API business, priced per token across the GPT-5.6 family, makes OpenAI the default infrastructure for a large share of the AI application market. The result is a layered model where every tier feeds the next: free users become subscribers, subscribers become enterprise contracts, and developers pull the whole thing through the API.

## What Is DeepSeek's Business Model in 2026?

DeepSeek's model is the opposite: there is essentially no business model, and the company says so. It is owned and funded by High-Flyer, a quantitative hedge fund that has been trading with AI-driven models since 2016, and it was spun out of High-Flyer's research lab in July 2023. DeepSeek's stated strategy is research, not revenue.

| Dimension | DeepSeek |
|-----------|----------|
| Owner | High-Flyer (Chinese hedge fund) |
| Stated strategy | "Focuses on research, no immediate commercialization plans" |
| Reported revenue | None disclosed |
| Headcount | ~160 employees (2025) |
| Pricing | Chat app free; V2 API ~2 RMB per million output tokens |
| Funding | ~$300M round discussed at ~$10B valuation (April 2026) |
| IPO status | Preparations reported, possible 2027 listing |

DeepSeek does charge for API access, and its V2 model was priced at roughly 2 RMB per million output tokens in 2024 — far below Western rivals at the time. But the company's economics are not built around maximizing that revenue. Its R1 chatbot launched free for iOS and Android in January 2025, its models are released under permissive open-weight licenses like MIT, and its reported training cost for V3 was about $5.6 million — versus OpenAI's reported $100 million figure for GPT-4 in 2023. Even with third-party estimates that put DeepSeek's real training cost far higher, the comparison illustrates a radically cheaper development machine.

The technical cost breakdown from DeepSeek's own V3 report shows how lean the operation is: roughly 2.8 million GPU-hours across pretraining, context extension, and fine-tuning, totaling about $5.6 million at assumed rental rates. That figure is contested — third-party analysts including SemiAnalysis and INSAIT have argued the true cost is far higher once full infrastructure is counted — but the strategic claim holds: DeepSeek was built to run on less. It acquired roughly 10,000 Nvidia A100 GPUs before US export restrictions tightened, built its own Fire-Flyer compute clusters, and designs around efficiency rather than scale. As its [Wikipedia profile](https://en.wikipedia.org/wiki/DeepSeek) notes, it reportedly uses about one-tenth the compute of Meta's comparable Llama 3.1 model.

## How Do Their Valuations and Funding Compare?

The gap between the two companies' financial footprints is enormous and growing. OpenAI's valuation rose from $157 billion in October 2024 to $300 billion in April 2025, $500 billion in October 2025, $730 billion in February 2026, and a reported $852 billion by April 2026, fueled by the largest private funding rounds in history — $122 billion in committed capital in a single 2026 round. DeepSeek, by contrast, was in talks in April 2026 for a $300 million round that would value it at around $10 billion.

| Metric | OpenAI | DeepSeek |
|--------|--------|----------|
| Latest reported valuation | ~$852B (April 2026) | ~$10B (April 2026) |
| Largest funding round | $122B committed (2026) | ~$300M discussed |
| 2025 revenue | $13.1B | Not disclosed |
| 2025 net result | ~−$9B loss | Not disclosed |
| Headcount | 4,500 | ~160 |
| IPO plans | Filed with SEC (2026) | Reported prep, possible 2027 |

![Horizontal bar chart: OpenAI's valuation of about $852 billion versus DeepSeek's roughly $10 billion, April 2026](/images/charts/deepseek-vs-openai-business-model-2026-chart-valuation.png)

![Horizontal bar chart: OpenAI employs about 4,500 people versus DeepSeek's roughly 160 employees](/images/charts/deepseek-vs-openai-business-model-2026-chart-headcount.png)

That is an 85x valuation gap, a roughly 400x gap in funding size, and a 28x gap in headcount. The differences are not incidental; they encode the two models. OpenAI is spending billions to build an empire — Microsoft holds a 27% stake valued around $135 billion and OpenAI has committed to buying $250 billion of Azure services. DeepSeek is a lean research operation funded by a hedge fund's trading profits, with founder Liang Wenfeng holding roughly 84% of the company through shell entities.

## Why Do the Two Business Models Look So Different?

The differences trace back to two different answers to the same question: who pays for frontier AI research? OpenAI's answer is the capital markets — Microsoft holds a 27% stake valued around $135 billion, and the company has raised the largest private rounds in history to fund infrastructure and research. DeepSeek's answer is a hedge fund — High-Flyer's trading profits fund the lab, which frees DeepSeek from the pressure to show revenue growth to investors. That single difference cascades through every other number.

The corporate structures encode the philosophy. OpenAI is a public benefit corporation created by restructuring a nonprofit, with employees and investors owning 47%, Microsoft 27%, and the OpenAI Foundation 26%. It has committed to buying $250 billion of Azure cloud services and shares 20% of revenue with Microsoft until it reaches AGI. It is a machine built to absorb capital and convert it into scale. DeepSeek, by contrast, is a private company with founder Liang Wenfeng holding roughly 84% through shell entities, backed by High-Flyer's own infrastructure. It is a machine built to convert efficiency into leverage.

The headcount gap tells the same story. OpenAI employs about 4,500 people and has said it plans to roughly double that; DeepSeek ran with about 160 people in 2025. OpenAI is building sales teams, enterprise relationships, support infrastructure, and a platform ecosystem. DeepSeek is running a research lab that happens to publish models. Neither choice is objectively right — but they are fundamentally different bets on what wins the AI race.

## Why Does a Company With No Revenue Threaten the Most Valuable AI Company?

DeepSeek's impact comes from cost, not revenue. When DeepSeek-R1 launched in January 2025, it matched or approached frontier models at a fraction of the reported training cost, and the market repriced the assumption that frontier AI requires billions in compute. Nvidia lost $600 billion in market value in a single day — the largest one-day drop for any US company in history — and DeepSeek's app briefly became the most downloaded free app in the US App Store, ahead of ChatGPT.

The mechanism is open weights. Because DeepSeek releases its models under permissive licenses, anyone can run them, adapt them, and price them at marginal cost. That collapses the pricing power of proprietary leaders. Our [analysis of open-source vs proprietary AI](/blog/open-source-vs-proprietary-ai-market-shift-2026/) documented how the Big 3's combined token share fell from 72% to 33% in twelve months, and DeepSeek's low-cost model is a core driver. OpenAI must recover hundreds of billions in infrastructure and research spending; DeepSeek faces no such obligation, which is why its API pricing sits an order of magnitude below OpenAI's premium tiers, as we showed in our [GPT-5.6 vs DeepSeek-V4 pricing comparison](/blog/gpt-5.6-vs-deepseek-v4-pricing-2026/).

The scale of the disruption is worth spelling out. A single model release repriced the entire AI hardware complex in one trading day: Nvidia lost $600 billion in market value, a record single-day decline for any US company. That event, more than any benchmark score, forced Western AI companies to defend their pricing in public. Anthropic and OpenAI have both responded with cheaper tiers and more aggressive API pricing, and the compression has flowed all the way down to consumers — today's budget-tier frontier models cost a fraction of what frontier access cost in 2024. The economic logic is now circular: DeepSeek's cost model makes it cheap, its cheapness forces competitors to cut prices, and the resulting price war validates the very cost advantage that started it.

The geographic angle matters too. DeepSeek's open-weight models are especially attractive in markets where Western platforms are expensive, sanctioned, or mistrusted — including large parts of the Global South and, increasingly, enterprises that want data sovereignty. High-Flyer's parent relationship gives DeepSeek infrastructure that is partially insulated from US export controls, and its models run on domestic and more affordable compute. The result is not just a cheaper model but a second center of gravity for the AI supply chain, which is precisely why Western regulators in the US and Australia have moved to restrict DeepSeek in government environments while its open-weight ecosystem keeps spreading commercially.

## Can DeepSeek Keep Running on No Revenue?

DeepSeek can run without revenue because its cost structure is radically different. A ~160-person team, open-weight distribution that pushes serving costs to the community and cloud providers, cheaper domestic compute, and a parent hedge fund that generates its own profits all mean DeepSeek's burn is a rounding error next to OpenAI's. High-Flyer built its own compute clusters — the Fire-Flyer clusters, including a 10,000-GPU A100 fleet acquired before US export restrictions tightened — giving DeepSeek infrastructure that was partially paid for by trading profits.

The open question is sustainability at the frontier. Training ever-larger models gets more expensive, and DeepSeek's own API documentation notes plans to raise prices significantly. A $300 million round would give it a funding cushion, and reported IPO preparations suggest the company is starting to build a conventional capital structure. But the core tension remains: the business model that makes DeepSeek disruptive — giving away frontier models — is the same one that makes it hard to convert that influence into the kind of revenue OpenAI generates.

## What Happens When the Two Models Converge?

## What Does the IPO Race Tell Us?

Both companies are preparing public listings, and the timing says a lot about their models. OpenAI filed confidentially with the SEC in mid-2026 and could debut in the fall; DeepSeek's reported preparations point to a possible 2027 listing. OpenAI is raising from global capital markets because its model needs enormous external funding to sustain frontier research. DeepSeek is preparing a listing despite years of saying it had no commercialization plans — a signal that funding frontier research on hedge-fund profits has limits, and that the company needs conventional capital to keep up.

The IPO race also changes the competitive math. A public OpenAI faces quarterly earnings scrutiny that may pressure it toward profitability faster than it wants, while an unlisted DeepSeek can keep prioritizing research. But a listed DeepSeek would inherit the same investor pressure OpenAI has: markets eventually demand revenue, margins, and returns. The pure research lab that upended the industry may not survive contact with the public markets intact — and the company that loses its cost discipline may lose the very advantage that made it a threat.

The two companies are already moving toward each other. OpenAI launched budget-tier pricing (GPT-5.6 Luna) that compresses its own margins, and it is exploring advertising to monetize free users. DeepSeek is exploring conventional funding and an eventual IPO. But the trajectories reveal the endgame of the US-China AI competition better than any benchmark: OpenAI is monetizing an 800-million-user distribution platform, while DeepSeek is weaponizing cost efficiency. The former sells intelligence at a premium; the latter commoditizes it.

Advertising is OpenAI's most important new revenue line and its clearest signal of intent. Reports put projected 2026 advertising revenue around $2.5 billion, with estimates rising to $100 billion annually by 2030 — a number that only makes sense if advertising becomes a first-class monetization layer inside ChatGPT's free tier. That would make OpenAI structurally resemble Google: a massive free consumer product monetized through ads, with premium subscriptions and enterprise contracts on top. It is a rational move for a company whose 700 million weekly users are its single greatest asset, but it also marks a strategic shift from "sell the best model" to "own the biggest distribution platform."

The open-source pressure deepens the logic. Because DeepSeek and other open-weight models are free to run, the marginal price of intelligence keeps falling, which erodes the premium that made API revenue attractive. OpenAI's answer is to sell distribution and convenience rather than raw capability. DeepSeek's answer is that commoditized intelligence benefits whoever runs the most efficient stack. The two companies are converging on the same realization from opposite directions: the model itself is becoming a commodity, and the value is migrating to the platform around it.

The data does not yet show a winner. OpenAI's $20 billion annualized revenue is real, but so is its $9 billion annual loss and the structural risk that open-weight rivals keep compressing its pricing power. DeepSeek's cost advantage is real, but so is its lack of a revenue engine and the question of whether it can fund frontier research forever on hedge-fund profits. What the comparison makes clear is that the US and China have built two different machines for the same race — and the machine that wins may not be the one with more money, but the one whose economics survive the next three years of price compression.

---

## Frequently Asked Questions

{{< faq-schema >}}
[
  {
    "q": "How does OpenAI make money in 2026?",
    "a": "OpenAI makes money through ChatGPT subscriptions ($20–$200/month), enterprise plans with about 5 million business users, API usage fees, and newly introduced advertising projected at roughly $2.5 billion for 2026. The company reported $13.1 billion in 2025 revenue and crossed $20 billion in annualized revenue by January 2026."
  },
  {
    "q": "Does DeepSeek make money?",
    "a": "DeepSeek has disclosed no revenue figures and says it focuses on research with no immediate commercialization plans. It does charge for API access — its V2 model priced around 2 RMB per million output tokens — and offers a free chat app. It is funded by the Chinese hedge fund High-Flyer."
  },
  {
    "q": "How much is DeepSeek worth compared to OpenAI?",
    "a": "OpenAI's latest reported valuation is around $852 billion (April 2026), while DeepSeek was in talks for a $300 million round at roughly a $10 billion valuation. That is an approximately 85x gap. OpenAI also raised about $122 billion in committed capital in 2026 versus the roughly $300 million discussed for DeepSeek."
  },
  {
    "q": "Why is DeepSeek so cheap to run?",
    "a": "DeepSeek trains on cheaper domestic compute, uses a lean ~160-person team, releases open-weight models that push serving costs to the community, and is backed by High-Flyer's hedge fund profits. It reported V3 training cost of about $5.6 million versus OpenAI's reported $100 million figure for GPT-4."
  },
  {
    "q": "Which AI company has a better business model?",
    "a": "OpenAI has proven revenue generation ($13.1B in 2025) but large losses ($9B) and a massive cost base. DeepSeek has dramatically lower costs but no meaningful revenue engine. The outcome will be decided by price compression over the next few years: whether OpenAI's distribution advantage survives open-weight cost competition."
  }
]
{{< /faq-schema >}}
