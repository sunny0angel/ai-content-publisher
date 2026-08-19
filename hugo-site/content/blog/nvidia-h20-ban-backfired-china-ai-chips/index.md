---
title: "The Nvidia H20 Ban Backfired: How China Built Its Own AI Chip Answer in 18 Months"
date: 2026-08-19
lastmod: 2026-08-19
description: "The H20 export ban forced China to build its own AI chips: Huawei Ascend hit ~60% of H100 inference, SMIC reached 5nm-class without EUV, then the IPOs followed"
tags: [Nvidia H20, export controls, Huawei Ascend, SMIC, China AI chips, US China tech war, AI chips]
categories: ["AI Industry Analysis"]
images:
  featured_image: "/images/nvidia-h20-ban-backfired-china-ai-chips.jpg"
draft: false
authors: ["AI Forward"]
slug: "nvidia-h20-ban-backfired-china-ai-chips"
---

> **Featured image:** Close-up of a modern microprocessor circuit board with intricate circuitry. Photo by [ed br](https://www.pexels.com/photo/close-up-of-a-modern-microprocessor-circuit-board-37052613/) on Pexels (Free to use).

In April 2025, the United States cut off Nvidia's H20 — the only premium AI chip American companies could still legally sell into China. Sixteen months later, the decision looks less like a surgical strike and more like the single most effective accelerator of China's domestic AI chip industry since the 2022 controls began. Huawei's Ascend line scaled from a research curiosity to the default answer for China's largest cloud providers, SMIC pushed its no-EUV process to 5nm-class, and the country's chip startups went public in the most extreme IPO run of the decade. The ban did not stop Chinese AI. It industrialized the alternative.

This analysis walks through what the H20 restriction actually did, how Huawei, SMIC, and a broad ecosystem responded, and what the evidence says about whether the United States gained or lost ground. It draws on reporting from Reuters, the Wall Street Journal, Tom's Hardware, TechInsights, SCMP, and the [Wikipedia profile of China's semiconductor industry](https://en.wikipedia.org/wiki/Semiconductor_industry_in_China), among others.

## What Was the H20 Ban and Why Did It Matter?

The H20 export ban removed the last legitimate premium AI accelerator available to Chinese buyers, forcing them to either stockpile aggressively or switch to domestic alternatives almost overnight. On April 9, 2025, Washington notified Nvidia that H20 exports to China would require licenses; by April 16, the Commerce Department had formalized the requirement for the H20 and AMD's MI308. The stated reason was that the chip's high memory bandwidth and interconnect speed could be used to build the kind of supercomputers the United States has restricted since 2022.

The H20 was not a flagship product — it was a compliance product. It delivered only a fraction of the H100's compute (third-party teardowns put its dense FP8 throughput near 148 TFLOPS, roughly one-thirteenth of the H100's peak FP8 rating), but it kept 96GB of HBM3, 4.0 TB/s of memory bandwidth, and 900 GB/s of NVLink interconnect, which made it unexpectedly strong at inference workloads. That combination mattered: inference, not training, is where most real-world AI demand sits. Reuters reported in February 2025 that Chinese firms had shipped roughly one million H20 units and generated more than $12 billion in revenue for Nvidia in 2024, making it Nvidia's single largest China product line.

The result was a scramble. Chinese cloud giants Alibaba, Tencent, and ByteDance accelerated H20 purchases in the first quarter of 2025 as DeepSeek's models drove demand, with media estimates of $12–16 billion in combined orders before the ban landed. Nvidia then took a $5.5 billion inventory charge in the first quarter of its fiscal 2026, which it disclosed in an [SEC filing](https://www.sec.gov/ix?doc=/Archives/edgar/data/0001045810/000104581025000082/nvda-20250409.htm) and [Reuters](https://www.reuters.com/technology/nvidia-expects-up-55-billion-charge-first-quarter-2025-04-15/) reported at the time. For Chinese buyers, the message was unmistakable: the last legal Nvidia lifeline had been pulled, and waiting for Washington to change its mind was not a procurement strategy.

| Date | Event |
|------|-------|
| Oct 2022 | US imposes first AI/semiconductor export controls on China |
| Feb 2025 | Chinese firms stockpile H20 (~1M units in 2024, $12B+ revenue) |
| Apr 9, 2025 | Washington notifies Nvidia that H20 exports require licenses |
| Apr 16, 2025 | Commerce formalizes H20 and AMD MI308 license requirements |
| Apr 2025 | Nvidia books $5.5B inventory charge for unsold H20 |
| Aug 2025 | US begins granting H20 export licenses again (partial reversal) |
| Jan 2026 | H200 approved for export; China customs blocks shipments |
| May 2026 | H200 approved for 10 Chinese firms incl. Alibaba, Tencent, ByteDance |

## Why Did the H20 Ban Backfire?

The ban backfired because it converted a hypothetical domestic-chip risk into a firm national commitment, and China responded with measurable acceleration in capacity, capability, and capital formation. The clearest evidence is market share: Morgan Stanley estimates China's AI chip self-sufficiency rose from about 10% in 2020 to 41% by 2025, with a projection of 86% by 2030 — a trajectory that predates the H20 ban but was hardened by it.

![Line chart showing China's AI chip self-sufficiency rising from 10% in 2020 to 41% in 2025 and a projected 86% by 2030](/images/charts/nvidia-h20-ban-backfired-china-ai-chips-chart-1.png "Source: Morgan Stanley, via Wikipedia, 2025")

Three structural effects followed the April 2025 cut. First, procurement certainty: state-backed guidance had already pushed toward "de-NVIDIA" since September 2024, but the ban removed the last reason for Chinese enterprises to hedge. Second, capital: the IPO window for domestic chip companies opened exactly when the political case for buying domestic became overwhelming. Third, engineering focus: Huawei and SMIC were already the only credible domestic path, and the ban made their success a matter of national strategy rather than commercial convenience.

Timing made the backfire sharper. The United States reversed itself in August 2025, beginning to issue H20 export licenses again and, per Reuters, Nvidia ordered roughly 300,000 H20 units from TSMC in response to resurgent Chinese demand. Then in January 2026, Washington cleared the more capable H200 for export — and Chinese customs blocked the shipments at the border. By May 2026, the US approved H200 sales to ten Chinese companies including [Alibaba, Tencent, ByteDance, and JD.com](https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14). The policy whipsawed from ban to license to ban-adjacent, while China's domestic supply chain kept building. That inconsistency is the core of the backfire argument: each reversal validated the Chinese decision not to wait.

## How Did Huawei's Ascend Line Fill the Gap?

Huawei's Ascend family became China's de facto answer to Nvidia, moving from a niche research chip to the platform of choice for the country's largest clouds in roughly sixteen months. The critical product was the Ascend 910C, which began scaling shipments around May 2025 and, according to research attributed to DeepSeek, delivers roughly 60% of the H100's inference performance. That number is a single-source estimate rather than an independent benchmark, but it represents the first time a fully domestic chip was credibly positioned within striking distance of Nvidia's flagship for the workloads that matter most in production.

The 910C is a dual-die design built by stacking two 910B compute chiplets, manufactured by SMIC on its N+2 (7nm-class) process. The 910B itself was already a breakthrough: a teardown by Tom's Hardware showed it has just 25 DaVinci cores compared with 32 on the TSMC-made original Ascend 910, a direct measure of how far back the process penalty pushed Huawei. Yet Chinese software has been engineered around that penalty. Huawei's CloudMatrix 384 cluster — 384 Ascend 910C units — began shipping in April 2025, and Huawei claims the full optical-interconnect system beats Nvidia's GB200 NVL72 rack on overall performance, at higher power consumption. The claim is vendor-reported, but the fact that a domestic 384-chip cluster can be seriously compared with a GB200 rack at all is itself the story.

The ecosystem signal matters more than any single chip. DeepSeek, the company whose open-weight models triggered the original H20 buying spree, trained R1 on H800 chips but has run inference on Ascend 910C. In March 2026, Reuters reported ByteDance and Alibaba planned orders for Huawei's next-generation Ascend 920, and by April 2026 there were reports of DeepSeek V4 training and inference moving onto an Ascend 950 cluster. The Ascend 920, announced in April 2025, is built on a 6nm-class process with HBM3 memory and roughly 900 TFLOPS of compute, explicitly positioned to fill the void left by the H20.

| Chip | Process | Key specs | Status (as of mid-2026) |
|------|---------|-----------|--------------------------|
| Ascend 910 | TSMC 7nm+ | 256 TFLOPS FP16, 32 DaVinci cores | Pre-ban, limited stock |
| Ascend 910B | SMIC N+1 (7nm-class) | 25 DaVinci cores, DUV multi-patterning | Mass production |
| Ascend 910C | SMIC N+2 (dual 910B) | ~60% of H100 inference (DeepSeek estimate) | Scaling since May 2025 |
| Ascend 920 | SMIC 6nm-class | ~900 TFLOPS, HBM3 | Announced Apr 2025, ramping |
| Ascend 950 | N/A (reported) | Estimated ~1.56 PFLOPS class | Reported in 2026 clusters |

## What Role Did SMIC Play in Manufacturing These Chips?

SMIC is the manufacturing backbone of China's AI chip push, and its progress is the strongest evidence that export controls compressed the technology gap rather than freezing it. The foundry produces Huawei's Kirin and Ascend chips on the N+2 node, a 7nm-class process achieved without EUV lithography by using DUV equipment and multiple patterning. That alone was a landmark: the Kirin 9000S, the chip that announced China could make advanced silicon domestically, shipped in the Mate 60 Pro in August 2023, and was fabricated by SMIC.

The next node, N+3, is the step that turned "behind by a generation" into "within one generation." In late 2025, TechInsights disassembled Huawei's Mate 80 Pro Max and identified its Kirin 9030 as manufactured on SMIC's N+3 process, a 5nm-equivalent node. TechInsights described N+3 as an evolutionary scaling of SMIC's 7nm-class technology that approaches true 5nm capability — accomplished entirely without EUV. Independent analysts dispute how closely N+3 compares with TSMC's 5nm in practice, with estimates of 60–70% yields and roughly 50% higher costs than equivalent TSMC output. But the direction is unambiguous: the gap is closing on the back of the process China is allowed to use, not the one it is denied.

SMIC has also become China's most important equipment test bed. In September 2025, the foundry began testing the country's first domestic immersion DUV lithography tool, designed for 28nm with multiple patterning extension to 7nm/5nm, and by July 2026 it had moved into small-batch production with output scheduled to double in 2027. This is the pattern that worries US policymakers most: a chip in the middle of the pipeline is less significant than a domestic toolchain that can sustain the industry without foreign components. Reuters reported in December 2025 that China had secretly completed a prototype EUV machine in Shenzhen, expected to produce working chips between 2028 and 2030. SMIC's revenue reflects the momentum — the company posted record revenue of roughly $9.3 billion for 2025, per TrendForce, with profitability pressured by the cost of advanced-node development.

## How Is the Chinese AI Chip Ecosystem Expanding Beyond Huawei?

Beyond Huawei, the H20 ban catalyzed the most concentrated wave of AI chip IPOs in history, converting startup technology into public-market commitments with extreme first-day valuations. The chart below shows the first-day stock gains of three of the most prominent listings — a market telling investors, in the loudest way possible, that domestic AI silicon is a national priority with capital-market momentum behind it.

![Bar chart showing first-day stock gains of Chinese AI chip IPOs: Moore Threads +400%, MetaX +700%, Biren +100%](/images/charts/nvidia-h20-ban-backfired-china-ai-chips-chart-2.png "Source: Reuters, CNBC, 2025-2026")

Moore Threads raised roughly RMB 8 billion (~$1.1 billion) in its November 2025 STAR Market listing, the largest tech IPO in China that year, and its shares surged as much as 400% on day one. MetaX listed in December 2025 and gained about 700% on debut. Biren, which reported over RMB 10 billion (~$1.4 billion) in 2025 revenue, completed its Hong Kong IPO in December 2025, raising about $624 million with oversubscription of more than 11 times, and rose more than 100% on its first day. Enflame, the Tencent-backed startup whose largest customer is also its largest investor, won approval for a STAR Market IPO worth roughly $883 million in June 2026. Cambricon, the bellwether, saw its stock rise 383% in 2024, recorded its first annual profit in 2025, and announced its maiden dividend in early 2026 — proof that a domestic AI chip company can be both strategically essential and financially viable.

Underneath the public listings sits a funding machine of unprecedented scale. The National Integrated Circuit Industry Investment Fund — "Big Fund" Phase III — was established in May 2024 with registered capital of RMB 344 billion (~$475 billion), the largest tranche in the fund's history, directed at equipment, materials, wafer fabrication, and advanced packaging. Biren, Moore Threads, MetaX, and Enflame all sit on top of this subsidized foundation, and each IPO converts policy support into market discipline.

## Did the United States Reverse the Ban, and What Happened Then?

The United States did reverse itself, twice, and each reversal reinforced the backfire narrative. In August 2025, the Commerce Department began granting H20 export licenses again, and Nvidia ordered roughly 300,000 H20 units from TSMC to meet renewed Chinese demand. In January 2026, Washington cleared the H200 — a more capable chip than the H20 — for export to China, and Chinese customs promptly blocked the shipments at the border. In May 2026, the US approved H200 sales to ten Chinese companies including Alibaba, Tencent, ByteDance, and JD.com, plus distributors like Lenovo and Foxconn.

The whipsaw is the point. Each reversal proved to Chinese buyers that the United States could not credibly sustain a hard line, which validated the decision of every Chinese enterprise that had already committed to Ascend. The same period also exposed the enforcement problem: in July 2025, Washington proposed restricting AI chip shipments to Thailand and Malaysia over smuggling concerns, and in May 2026 Taiwanese prosecutors detained three people over an alleged scheme to smuggle Nvidia chips to China via Japan. Controls that can be reversed at will and are simultaneously being circumvented do not change long-term procurement plans — they accelerate them.

## What Are the Limits of China's Domestic Chip Push?

China's domestic push has real constraints, and the honest assessment is that each is survivable but none is trivial. The most immediate is yield and cost: SMIC's N+3 node reportedly delivers 60–70% yields at roughly 50% higher cost than comparable TSMC output, which pushes up the price of every Ascend and Kirin chip. The second constraint is compute density — the 910B's reduced core count (25 vs. 32) and the dual-die 910C design are engineering workarounds for process limits, not solutions to them. A chip that reaches 60% of H100 inference is a viable product; it is not parity.

The third constraint is ecosystem lock-in. Nvidia's CUDA software stack is the default environment for AI development worldwide, and Chinese developers have decades of muscle memory tied to it. Huawei's CANN stack and the broader open-source movement — which we examined in our analysis of [open source vs proprietary AI market share](/blog/open-source-vs-proprietary-ai-market-shift-2026/) — are closing that gap, but migration costs remain real. Fourth, and least appreciated, is memory and equipment dependency: even a fully domestic logic chip relies on HBM stacks and lithography tools that China is still years from producing at scale, which is why the reported Shenzhen EUV prototype and domestic DUV tools matter so much. Finally, reliability concerns surfaced in mid-2025 with reports of Ascend 910B/910C overheating and some units failing in the field — a reminder that volume deployment outruns engineering maturity.

## What Does This Mean for the US-China AI Race in 2026 and Beyond?

The H20 ban's legacy is not that China built a better chip than Nvidia — it did not, and probably will not for years. The legacy is that China built a credible, scaling, capital-backed alternative that no longer depends on the continued availability of Nvidia products. Morgan Stanley's 86% self-sufficiency projection for 2030 is a forecast, not a certainty, but the direction of travel is now policy-backed at every level of the Chinese state. The result is a two-tier market: the United States retains the frontier lead in silicon while China consolidates a domestic alternative large enough to absorb its own demand. For global buyers, the practical consequence is a pricing and supply reality we documented in our analysis of [GPT-5.6 vs DeepSeek-V4 API costs](/blog/gpt-5.6-vs-deepseek-v4-pricing-2026/) — the same work costs a fraction of the price on Chinese infrastructure, and the hardware that powers it no longer depends on a single American supplier.

For professionals and investors watching the [US-China AI race](/blog/us-china-ai-race-2026/), the H20 episode offers a specific lesson: export controls that target a single product without a coordinated plan for the full stack — process, equipment, memory, software — buy time but create inertia. Every month the H20 was unavailable, Huawei's software stack matured, SMIC's yields climbed, and the IPO market reallocated capital to domestic chips. The United States still leads. But it spent eighteen months building China's most effective argument for why it should not have to wait for permission to compute.

---

## Frequently Asked Questions

### What was the Nvidia H20 chip, and why was it banned for export to China?

The H20 was Nvidia's China-specific version of the H100, cut back on compute but retaining 96GB of HBM3 memory and high interconnect bandwidth, making it strong at AI inference. In April 2025, the US Commerce Department required export licenses for it, citing potential use in supercomputers, and Nvidia took a $5.5 billion inventory charge.

### How far has China's AI chip self-sufficiency actually come?

Morgan Stanley estimates China's AI chip self-sufficiency rose from about 10% in 2020 to 41% in 2025, with a projected 86% by 2030. Huawei's Ascend 910C reaches roughly 60% of Nvidia H100 inference performance per DeepSeek research, and SMIC has produced a 5nm-class node without EUV.

### Did the United States reverse the H20 ban?

Yes. In August 2025 the US began granting H20 licenses again, and in 2026 it approved the more capable H200 for export to ten Chinese companies including Alibaba, Tencent, and ByteDance — after Chinese customs had blocked earlier H200 shipments in January 2026.

### Why do analysts call the H20 ban a backfire?

Because the ban removed the last legitimate Nvidia product in China and triggered exactly what it was meant to prevent: Huawei's Ascend scaled to become the default domestic option, SMIC advanced its no-EUV process to 5nm-class, and a wave of Chinese AI chip IPOs (Moore Threads, MetaX, Biren, Enflame) attracted massive public-market funding.

### What are the main limits of China's domestic AI chips?

The main limits are yields and cost (SMIC N+3 at roughly 60-70% yield and about 50% higher cost than TSMC equivalents), compute density (910C at ~60% of H100 inference), CUDA ecosystem lock-in, dependency on imported HBM memory and advanced lithography tools, and early reliability issues reported in Ascend 910B/910C deployments.
