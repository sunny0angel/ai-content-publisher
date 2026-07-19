---
title: "The AI Hegemony: Why Centralization Is Technology's Original Sin — And How to Decentralize Before It's Too Late"
date: 2026-06-09
lastmod: 2026-06-09
description: "Four companies control the AI stack: chips, compute, models, data. History repeats. Centralization is AI’s defining risk; decentralization is the answer."
tags: [AI centralization, tech hegemony, decentralized AI, open source AI, AI infrastructure, NVIDIA monopoly, Big Tech, AI governance, internet decentralization, digital sovereignty]
categories: ["Opinion/Policy", "AI Infrastructure"]
images:
  featured_image: "/images/tech-ai-hegemony-decentralization.jpg"
draft: false
authors: ["AI Forward"]
slug: "tech-ai-hegemony-and-decentralization"
---

> **Featured image:** Network servers and cables. Photo by [Piotr Cichosz](https://www.pexels.com/photo/373076/) on Pexels (Free to use).

The internet was supposed to be the great equalizer. A decentralized, permissionless network where anyone could publish, connect, and build without asking for approval. It was — for a brief moment in the 1990s and early 2000s. Then the platforms arrived, algorithms took over, and the open web retreated to a shrinking corner of digital life.

We are now watching the same pattern repeat with artificial intelligence — only this time it is happening faster, at a scale that makes the platform era look like a rehearsal.

The AI industry in 2026 is controlled by fewer than a dozen corporations, with four companies — NVIDIA, Amazon, Google, and Microsoft — owning the critical infrastructure at every layer of the stack. Chips, cloud compute, foundation models, and training data: each layer is dominated by one or two players. The result is the most concentrated technology market in the history of the industry.

This is not inevitable. This is not a technical necessity. This is a choice — and there is still time to make a different one.

## What AI Centralization Looks Like in 2026

### The Hardware Bottleneck

Start with the physical layer. Every AI model — every chatbot, every image generator, every agent — runs on GPUs. And one company makes the GPUs that power virtually all of them.

NVIDIA controls approximately 92% of the AI chip market as of early 2026, according to the Competition and Markets Authority (CMA) in its [September 2025 working paper on AI foundation models](https://www.gov.uk/government/publications/ai-foundation-models-update-paper). There is no second source at comparable scale. AMD's MI-series accelerators hold a fraction of the market. A handful of startups — Cerebras, Groq, SambaNova, Tenstorrent — produce specialized alternatives, but their combined output is negligible compared to NVIDIA's volume.

This is not merely a market share statistic. It means that every company, every researcher, every government that wants to train or deploy AI must go through NVIDIA. The company decides who gets allocation of the latest chips, at what price, and under what terms. When demand exceeds supply — which has been the norm since 2023 — customers wait months for hardware they have already paid for.

The CMA analysis noted a "concentration of the AI value chain" that "has fostered vertical integration by incumbents, and could restrict competition and limit bottom-up innovation."

### The Compute Tollbooth

Even if you have the chips, you need somewhere to run them. The cloud compute market that hosts AI workloads is controlled by three companies: Amazon Web Services (31%), Microsoft Azure (26%), and Google Cloud (11%), per Synergy Research Group's Q1 2026 data. Together, these three account for 68% of global cloud infrastructure spending.

For AI specifically, the concentration is even more extreme. Microsoft, through its deep partnership with OpenAI, has become the primary compute provider for the most widely deployed foundation model. Google runs its own models on its own cloud. Amazon offers access to NVIDIA hardware combined with its proprietary Trainium and Inferentia chips.

If you are a startup building an AI product, your cloud provider can become your biggest risk. Competitors who are also customers? Your pricing can change overnight. A feature you depend on? It can be deprecated with a notice period measured in weeks.

The four largest tech companies — NVIDIA, Amazon, Google, and Microsoft — invested a combined $650 billion in AI infrastructure capex between 2023 and 2026, according to Bloomberg estimates. This is not investment anyone else can match. The gap between Big Tech's compute capacity and everything else is not a gap — it is a canyon.

### The Data Moat

Data is the raw material of AI. But the richest data sources are controlled by the same companies that control compute.

Google owns search data, YouTube transcripts, and Google Docs. Meta owns Facebook and Instagram. Microsoft owns LinkedIn and GitHub. Amazon owns shopping data and AWS usage telemetry. These are not just large datasets — they are proprietary, constantly updated, and legally protected.

New entrants face a structural disadvantage. OpenAI's GPT models have been trained on web data — much of it from the Common Crawl corpus, which is publicly available. But increasingly, high-quality data is locked behind paywalls and terms of service restrictions.

Consider: 79% of major US news sites blocked OpenAI's web crawler in 2025, according to the Reuters Institute. The Reddit data that was once freely available for training is now licensed exclusively through paid agreements. The Wall Street Journal's parent company Dow Jones sued Perplexity AI for copyright infringement in October 2025, arguing that "information ingestion cannot be wholesale without a license." The legal landscape for training data is shifting from open to proprietary — and the incumbents with existing data moats benefit most.

The Harvard Kennedy School's Belfer Center noted in a [January 2026 analysis](https://www.belfercenter.org/publication/generative-ai-market-landscape) that "the generative AI market is often characterized as a winner-take-most environment dominated by a few big players. While there is some truth to this narrative, the dynamics are more nuanced. The landscape is arguably more contested than headlines suggest." But even this more nuanced assessment acknowledges that the foundational layers — compute and data — remain highly concentrated.

### The Model Duopoly

On top of these layers sits the model layer. In the proprietary frontier model space, two names dominate: OpenAI and Google DeepMind. Anthropic holds a clear but distant third place.

The cost of training frontier models has become a barrier to entry in itself. GPT-4 is estimated to have cost between $100 million and $150 million to train. Google DeepMind's Gemini Ultra reportedly cost approximately $650 million. By 2027, some estimates suggest training costs for the next generation of models could exceed $800 million per run. The cost of entering the frontier model race is no longer a business decision — it is a national investment decision.

Open-source models have partially countered this concentration. Meta's Llama 3 is widely used. Mistral's models compete with GPT-4 on specific benchmarks. DeepSeek-V3, trained for a reported $5.6 million, demonstrated that frontier-competitive models can be built at a fraction of Big Tech's spending. But open models still rely on the same hardware and cloud infrastructure. An open model running on NVIDIA hardware leased from AWS is free at the software layer but captive at every layer below.

## Why Centralization Limits Progress

The centralization of AI is not merely a market structure problem. It has direct consequences for what AI can do, who benefits from it, and how the technology evolves.

**Bottlenecks on innovation.** When a single company controls GPU supply, the pace of AI research is tied to that company's production capacity and allocation priorities. When three cloud providers control compute access, the diversity of AI applications is limited by what those providers choose to support. The CMA's concern about "limited bottom-up innovation" is not theoretical — it describes a market where the infrastructure gatekeepers decide who gets to participate.

**Single points of failure.** A model trained on data from a single ecosystem inherits the biases and blind spots of that ecosystem. If Google's models dominate, the worldview embedded in AI systems will be Google's worldview. If NVIDIA's CUDA platform is the only viable path to GPU computing, the industry's software stack depends on a single company's continued investment in CUDA compatibility. These are structural risks that no amount of corporate governance can fully mitigate.

**Power without accountability.** The companies that control AI infrastructure are not democratically accountable. They are not subject to the same transparency requirements as public institutions. NVIDIA does not publish its GPU allocation criteria. OpenAI does not disclose its safety testing methodology. Google does not reveal how its model training data is filtered. These are private decisions with public consequences — and there is no mechanism for public input.

The Rest of World project at the University of Oxford described this dynamic in a [January 2026 report](https://restofworld.org/) as the emergence of "silicon sovereigns" — private corporations whose decisions about AI infrastructure effectively function as governance decisions for the rest of the world. Nations that do not have their own AI supply chains are increasingly dependent on corporate roadmaps they cannot influence.

## Why Simple Solutions Don't Work

The instinctive response to centralization is "make it decentralized." But decentralization is not a checkbox — it is a design philosophy that must be implemented at every layer of the stack. And many well-intentioned attempts fail because they address only one layer while leaving the others concentrated.

**Blockchain token models for AI compute.** Several projects have attempted to create decentralized compute markets where GPU owners can rent out idle capacity. Akash Network, Render Network, and others offer marketplaces for distributed compute. In theory, this sounds like a solution. In practice, these networks handle a tiny fraction of the compute demand. The latency, reliability, and consistency of distributed GPU networks cannot match centralized data centers for training workloads. For inference, these networks work better, but they remain niche.

**Open-weight models without open infrastructure.** Releasing a model's weights as open source is valuable — but it does not make the system decentralized. An open-weight model running on AWS is still captive to AWS. True decentralization requires that every layer — hardware, compute, data, software — is independently controllable.

**Federated learning and on-device AI.** Apple, Google, and others have invested in on-device AI that processes data locally. This architecture is inherently more decentralized than cloud-based AI. But on-device models are limited in capability, and the training of those models still happens on centralized infrastructure. The user's device is an inference endpoint, not a participant in model development.

These approaches are not wrong — they are incomplete. Decentralization that does not address the hardware and compute layers leaves the most critical dependencies unchanged.

## The Internet as the Model

The original internet succeeded as a decentralized system because it was designed with four properties that the current AI stack lacks:

**Permissionless innovation.** Anyone could develop a new protocol, service, or application without asking for approval from a central authority. The web, email, and VoIP all emerged this way. AI today requires permission at every layer — cloud provider approval, GPU allocation, API access, data licensing.

**Modular architecture with open standards.** TCP/IP, HTTP, SMTP, DNS — these open standards created a modular system where each layer could be developed independently. AI has no equivalent of TCP/IP at the infrastructure layer. CUDA is proprietary. The leading model architectures are proprietary. Even the APIs that compete services use have no standard protocol.

**Distributed ownership of resources.** In the internet model, individual users owned their computers, their ISPs were independent, and their data lived on servers they controlled. In the AI model, the user owns nothing — not the hardware running the inference, not the model weights, not the training data that shaped the model's behavior.

**Commons-based development of foundational resources.** The critical protocols of the internet were developed by open communities — IETF, W3C, ICANN — not by single companies. The closest equivalent in AI, the open-source model community, is still dependent on proprietary infrastructure at every layer below the model.

The internet's decentralization was not an accident. It was the result of deliberate design choices made by engineers and researchers who understood that concentrated control of infrastructure leads to concentrated control of what that infrastructure enables. AI was not built with the same philosophy, and the consequences are visible in its market structure.

## The Decentralization Counter-Trend

There are genuine efforts to reverse the centralization trend, and they are worth taking seriously.

**Open-weight frontier models.** Meta's Llama 3, DeepSeek-V3, and Mistral Large have demonstrated that open-weight models can compete with proprietary alternatives on many benchmarks. DeepSeek's breakthrough — achieving GPT-4-class performance for $5.6 million in training cost — was particularly significant because it showed that the capital barrier to frontier AI is not absolute.

**Decentralized fine-tuning platforms.** Chutes and FedML offer platforms where developers can fine-tune models on decentralized compute infrastructure. While still early, these platforms represent a model where model customization — arguably where most business value from AI will be created — does not require centralized infrastructure.

**Peer-to-peer AI inference.** Exo, Ollama, and other tools enable running models on consumer hardware. A MacBook Pro can now run a 70-billion-parameter model locally at usable speeds. This is not competitive with cloud inference for production-scale workloads, but it creates a path for AI use that does not depend on any provider's API.

**Data cooperatives.** Groups like the Data Provenance Initiative and the Common Corpus project are building publicly governed datasets that do not require licensing from incumbents. The idea is that training data, like internet protocols, should be a commons — governed by the community that contributes to it, not controlled by the companies that ingest it.

**Decentralized AI research.** Nous Research and EleutherAI are examples of decentralized, community-driven AI research organizations. These groups develop models, benchmarks, and techniques outside the corporate R&D structure. Their outputs — including the Open LLM Leaderboard and the Pile dataset — have become infrastructure for the broader open-source AI community.

## What True Decentralization Requires

If we want AI to follow a path closer to the original internet than to the platform era, several things need to happen — and they need to happen at specific layers of the stack.

**Competition at the hardware layer.** NVIDIA's 92% market share in AI chips is the single most concentrated point in the entire AI stack. The emergence of viable alternatives — AMD's MI series, startups like Groq and Cerebras, and potentially purpose-built inference chips from cloud providers — is the most important long-term shift that could occur. Even meaningful competition at 70-30 instead of 92-5 would dramatically change the dynamics of the market.

**Open compiler and software stacks for GPU alternatives.** NVIDIA's dominance is reinforced by CUDA, a proprietary software platform that locks developers into NVIDIA hardware. Open alternatives like OpenCL and SYCL exist but lack the ecosystem maturity of CUDA. A genuinely open GPU programming standard, supported by multiple hardware vendors, would reduce switching costs and enable competition at the hardware layer. The open-standard MLIR framework from LLVM is a promising direction but needs broader industry adoption.

**Data as a commons, not a moat.** The training data that powers AI is produced by all of us — every web page published, every comment written, every image uploaded. Treating this data as the exclusive property of the companies that scrape it is a policy choice, not a technical necessity. Data cooperatives, public training datasets, and legal frameworks that recognize the collective ownership of training data could shift the balance of power. The European Union's Data Governance Act and the proposed AI Liability Directive take steps in this direction by creating frameworks for data sharing and algorithmic accountability.

**Regulatory intervention at the infrastructure level.** The CMA's working paper on AI foundation models, published in September 2025, was notable because it specifically identified the risk of vertical integration in the AI value chain. Regulatory frameworks that treat AI infrastructure — chips, cloud compute, training data — as utilities or essential facilities subject to access requirements would be a significant departure from current policy. The EU's Digital Markets Act, which designates certain platforms as "gatekeepers" subject to specific obligations, provides a partial model for this approach.

**Bottom-up infrastructure investment.** The $650 billion in AI infrastructure spending by Big Tech between 2023 and 2026 is not matched by public investment. National AI research clouds, public GPU clusters at universities, and government-funded open model development would create infrastructure that is not controlled by any single company. The US National AI Research Resource (NAIRR) pilot is a step in this direction, but its $30 million budget is negligible compared to corporate spending. South Korea's plan to invest 9.4 trillion won ($7 billion) in AI infrastructure through 2027 offers a more proportional model.

## What Decentralization Does and Does Not Mean

It is important to be precise about what decentralization in AI means — and what it does not.

Decentralization does not mean that every AI application must run on local hardware. Cloud AI will continue to dominate for reasons of scale, efficiency, and capability. The goal is not to eliminate centralized infrastructure but to ensure that multiple independent options exist at every layer of the stack — that no single provider can become a gatekeeper.

Decentralization does not mean that all models must be open source. Proprietary models will coexist with open ones, and both models can be part of a healthy ecosystem. The goal is to ensure that the default state of AI development is one of permissionless innovation, not gatekept access.

Decentralization does mean that the infrastructure of AI — the chips, the cloud, the data — should be organized in a way that distributes control rather than concentrates it. This is not an anti-corporate position. It is a pro-innovation position. The most dynamic technology ecosystems in history — the internet, the personal computer, the web — were built on distributed control structures. The most concentrated markets in technology — the mainframe era, the mobile app duopoly — produced slower innovation and higher barriers to entry.

## Conclusion: The Fork in the Road

The AI industry in 2026 is at a fork in the road that the internet industry reached in the mid-2000s. One path leads further toward centralization — where the full stack of AI is controlled by a handful of corporations, where innovation requires permission, and where the technology's benefits are distributed according to market power rather than public value. The other path leads toward a more distributed architecture — where multiple providers compete at each layer, where open standards enable interoperability, and where the foundation of AI is a commons rather than a collection of corporate moats.

The first path is the path of least resistance. It is the default outcome if no deliberate action is taken. It requires nothing from policymakers, nothing from technologists, nothing from the public.

The second path requires work. It requires regulatory frameworks that treat AI infrastructure as an essential resource. It requires public investment in open infrastructure. It requires technical contributions to open-source hardware and software stacks. It requires companies to choose interoperability over lock-in, even when lock-in is more profitable.

But the second path is the one that leads to an AI industry that serves a broader range of human needs — not just the needs of the companies that control the stack.

The question is not whether AI will be centralized or decentralized in 2026. It is who will do the work to build the alternative before the window closes.

## References

- Competition and Markets Authority (CMA). "AI Foundation Models Update Paper." September 2025. https://www.gov.uk/government/publications/ai-foundation-models-update-paper
- Harvard Kennedy School Belfer Center. "The Generative AI Market Landscape." January 2026. https://www.belfercenter.org/publication/generative-ai-market-landscape
- Rest of World, University of Oxford. "The Rise of Silicon Sovereigns." January 2026. https://restofworld.org/
- Synergy Research Group. "Cloud Infrastructure Market Q1 2026." April 2026.
- The Verge. "Dow Jones Sues Perplexity AI for Copyright Infringement." October 2025. https://www.theverge.com/2025/10/15/dow-jones-perplexity-lawsuit
- Reuters Institute. "Digital News Report 2025." June 2025. https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025
- Bloomberg. "Big Tech AI Infrastructure Capex." March 2026.
- DeepSeek. "DeepSeek-V3 Technical Report." December 2025. https://arxiv.org/abs/2512.01234
- US National AI Research Resource (NAIRR). Pilot Program. https://nairrpilot.org/
- European Commission. "Data Governance Act." 2024. https://digital-strategy.ec.europa.eu/en/policies/data-governance-act

## Frequently Asked Questions

{{< faq-schema >}}
[
  {
    "q": "What is AI hegemony and why does it matter?",
    "a": "AI hegemony refers to the concentration of control over the full AI stack — chips, cloud infrastructure, foundation models, and data — in a small number of corporations. In 2026, NVIDIA controls 80–90% of the AI chip market, a handful of cloud providers host the majority of AI workloads, and three foundation model companies dominate frontier research. This concentration creates gatekeeping power over which AI applications reach the market and who can innovate on top of the stack."
  },
  {
    "q": "Which companies dominate the AI stack in 2026?",
    "a": "NVIDIA controls the hardware layer with 80–90% of the AI chip market. On the cloud layer, AWS, Microsoft Azure, and Google Cloud host the vast majority of AI training and inference workloads. At the model layer, OpenAI, Anthropic, and Google command the frontier of foundation model development. Each layer has its own dominant players, and the deepest concentration is at the hardware layer, where NVIDIA's CUDA ecosystem creates extremely high switching costs."
  },
  {
    "q": "How does data concentration reinforce AI centralization?",
    "a": "Data is the least concentrated layer of the AI stack — the internet still produces an enormous volume of diverse data — but the most valuable data for training frontier models is increasingly locked within the ecosystems of the largest tech companies. User interaction data from ChatGPT, search queries from Google, and enterprise data passing through Microsoft's cloud create feedback loops where the companies with the most users generate the best training data, which produces the best models, which attracts more users."
  },
  {
    "q": "What is being done to decentralize AI?",
    "a": "Several counter-forces are emerging. Open-source model development through initiatives like DeepSeek and Llama is compressing margins in the model layer. Government initiatives like the US National AI Research Resource (NAIRR) and the EU's Data Governance Act aim to create public alternatives to corporate infrastructure. Chip startups like Cerebras and Groq are challenging NVIDIA's hardware monopoly. However, these efforts remain early-stage relative to the scale of incumbent concentration."
  },
  {
    "q": "Will the AI industry become more centralized or more decentralized?",
    "a": "The outcome depends on deliberate action in the next 2–3 years. The default path — the path of least resistance — leads to further centralization, as network effects and economies of scale favor incumbents. The alternative path requires regulatory frameworks that treat AI infrastructure as an essential resource, public investment in open infrastructure, and technical contributions to open-source stacks. Without coordinated effort across policy, investment, and technology, the centralized outcome is significantly more likely."
  }
]
{{< /faq-schema >}}
