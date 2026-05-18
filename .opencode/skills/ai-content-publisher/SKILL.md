# AI Content Publisher Skill

## Trigger

```
/publish "<topic>" [/count:<n>] [/lang:<en|ja|zh>] [/type:<howto|analysis|listicle>]
```

Examples:
- `/publish "How AI is transforming HR document processing in 2026"`
- `/publish "5 ways to automate business workflows with AI" /count:2`
- `/publish "AI-powered resume screening guide" /lang:ja`
- `/publish "ChatGPT API tutorial for beginners" /type:howto`

## Defaults

- count: 1 (記事数)
- lang: all (3言語全部)
- type: auto-detect from topic

## Overall Workflow

```
Step 0: コンテンツタイプを自動判定
Step 1: Webリサーチ（WebFetchツール or research.py）
Step 2: 英語記事を生成（Article Generatorプロンプトリファレンス）
Step 3: セルフレビュー＆修正（下記「Article Review Checklist」を必ず実行）
Step 4: SEOメタデータを生成（SEO Metadataプロンプトリファレンス）
Step 5: 日本語に翻訳（同じプロンプト、lang=jaで再実行）
Step 6: 中国語に翻訳（同じプロンプト、lang=zhで再実行）
Step 7: 画像プロンプトを生成し、ユーザーに提示（gemini-prompt-template.md）
Step 8: ユーザーがGeminiで生成 → 指定パスに保存
Step 9: Hugo記事ファイル（index.md）を3言語分作成（画像パスを含む）
Step 10: GitHubにプッシュ（draft=Hugoフロントマター）
Step 11: プレビューURLをユーザーに提示
Step 12: ユーザー承認後、draft=falseにして再プッシュ
Step 13: プロモーション投稿文を生成（social-promo.md プロンプトリファレンス）
Step 14: social_poster.py で X + LinkedIn に自動投稿
```

## Article Review Checklist (Step 3: must complete before translation)

英語記事を生成したら、**必ずすべての項目を順にチェックし、問題があれば修正してから** 翻訳に進む。

### 1. ロジック・構成チェック
- 記事全体の論理の流れは自然か（主張 → 根拠 → 具体例 → 結論）
- 同じ内容が複数セクションで重複していないか
- セクション間のトランジションはスムーズか
- 結論は分析を踏まえたものになっているか（単なる感想や予測で終わっていないか）

### 2. 深掘り不足チェック
- 「なぜ」が十分に説明されていない箇所はないか
- 読者が次に知りたくなる質問が unanswered のまま残っていないか
- 表面的な一般論で済ませているセクションはないか
- 各セクションに固有の主張があるか（他のセクションの言い換えになっていないか）

### 3. 具体例・データチェック
- 抽象的な主張には具体例（企業名、業種、具体的な数字、シナリオ）が付随しているか
- データがない主張には統計や調査結果を追加できるか
- データは最新か（可能なら2025-2026年のソースを優先）
- 「多くの企業が...」のような漠然とした主語を具体化できるか

### 4. データソースの信頼性チェック
- 引用した統計や調査は信頼できる一次ソースか（SBE Council, Salesforce, McKinsey, JP Morgan, US Census Bureau など）
- ブログの二次引用やベンダーのマーケティングデータを一次ソースのように使っていないか
- 各データには出典URLへのハイパーリンクが付いているか
- リンクはanchor textとして自然に埋め込まれているか（「調査によると」ではなく「SBE Councilの[2026年調査](URL)によると」）

### 5. AI臭除去チェック
以下のような典型的な「AI文章パターン」がないか徹底的になくす：
- ✗ 「In today's rapidly evolving landscape...」— 削除
- ✗ 「It is important to note that...」— 削除または言い換え
- ✗ 「This article will explore...」— 「This article examines...」などすべて削除
- ✗ 「Let's dive into...」— 削除
- ✗ 「In conclusion...」— 削除または自然な締めに
- ✗ 「It's worth mentioning that...」— 削除
- ✗ 「The truth is that...」— 削除
- ✗ 各段落の先頭が「According to [Source]...」の繰り返し— 構造を変える
- ✗ 同じ文型（「X found that Y...」）の連続— バリエーションをつける
- ✗ 過剰な接続詞（However, Moreover, Furthermore, Consequently）— 半分以上削除
- ✗ 疑問文で始まるセクションがテンプレート化していないか— 言い回しを変える
- ✗ どの記事にも同じ文体パターンが現れていないか— 記事ごとに変える
- ✓ チェック後、声に出して読んでみて「人間が書いた」と感じるか確認

## Content Rules (NEVER VIOLATE)

### Absolute Prohibitions
- ❌ Product reviews ("I tested X", "My experience with Y")
- ❌ "Best", "Top N" style affiliate-focused headlines
- ❌ Making unverifiable claims
- ❌ Recommending specific products/services with affiliate intent
- ❌ Using your own "personal testing" as authority

### Content Categories (what to write instead)
- ✅ How-to guides / tutorials
- ✅ Industry analysis and trends
- ✅ Use cases and applications
- ✅ Comparison of approaches/methodologies (NOT products)
- ✅ Research summaries and case study compilations

## AEO/GEO Rules (AI Search Optimization)

Every article MUST include these:

### 1. Question-Form Headings
Convert all H2/H3 headings into question form:
```
❌ "AI Document Processing Overview"
✅ "How Does AI Document Processing Work?"
✅ "What Are the Key Benefits of AI in HR?"
```

### 2. Answer Capsule Pattern
After every H2/H3 heading, the FIRST paragraph must be a self-contained answer:
- Length: 40-60 words
- Must make sense if extracted alone
- Directly answers the heading question
- Front-load the key information

### 3. FAQ Section
Include 3-5 FAQ entries at the bottom of every article:
- Real search queries people would ask
- Each Q is an H3 heading
- Each A is 30-50 words
- This is prime AI citation material

### 4. Data & Statistics
Every article must include at least 2 specific data points or statistics:
- "According to a 2026 study..."
- "Companies implementing X report Y% improvement..."
- Cite sources where possible

### 5. Content Depth
- Minimum 2,500 words per article
- Maximum 4,000 words
- Use tables for data comparison when applicable
- Include step-by-step sections for how-to content

### 6. Freshness Signal
Include the current date context:
- "As of May 2026..."
- "In 2026, organizations are..."
- Final article gets `lastmod` frontmatter set to today

### 7. Internal Linking
- Add links to 2-3 other articles on the same site
- Use descriptive anchor text

## Tone & Style

- **Tone**: Professional, educational, practical
- **Audience**: Business professionals interested in AI
- **Voice**: Third person, authoritative but not promotional
- **Example opening**: "As organizations increasingly adopt AI technologies, one question arises: how can these tools be effectively applied to [topic]? This guide explores the practical approaches and real-world applications."

## Multi-Language Handling

### English (primary)
- Full original article with complete SEO optimization
- Target: Informational/buyer-intent keywords (no product comparison)

### Japanese (translation)
- Same structure, fully translated
- SEO metadata in Japanese (title, description, tags)
- Japanese business-appropriate tone (丁寧語, not 敬語)
- Target JP keywords: 〜方法、〜ガイド、AI活用

### Chinese (translation)
- Same structure, fully translated
- SEO metadata in Chinese
- Simplified Chinese (not Traditional)
- Target CN keywords

### Translation Quality Rules
- Do NOT use machine-translation-sounding language
- Adapt idioms and examples to be culturally relevant
- Keep technical terms in English where appropriate (AI, API, SaaS)
- SEO titles must be optimized per language, NOT direct translations

## File Format (Hugo Markdown)

```markdown
---
title: "Article Title (SEO optimized)"
date: 2026-05-18
lastmod: 2026-05-18
description: "Meta description under 160 chars"
tags: [tag1, tag2, tag3]
categories: ["Category Name"]
image: "/images/slugified-name.jpg"
draft: true
slug: "url-slug"
---

## Question-Form Heading Here

[Answer capsule: 40-60 word self-contained answer]

[Elaboration: 2-3 paragraphs with detail, examples, data...]
```

## Image Requirements

- Aspect ratio: 16:9 (1200×675 recommended)
- Style: Modern, clean, tech-themed
- Color: Blue/white/tech gradient palette
- No text overlays in the image
- File naming: `{slug}.jpg` (lowercase, hyphenated)
- Save to: `hugo-site/static/images/{slug}.jpg`

## Image Prompt Generation

Use `prompts/gemini-prompt-template.md` to generate the prompt.
Present to user with exact save path:
```
Please generate this image with Gemini and save to:
hugo-site/static/images/{slug}.jpg

Prompt: [generated prompt]
```

## Publishing Process

1. Create all article files
2. Place images in static/images/
3. Set `draft: true` initially
4. Run git commands for commit + push
5. Tell user the preview URL
6. Wait for user approval ("公開で" or "publish")
7. Change draft to false, git commit + push again
8. Generate social promo posts (X + LinkedIn) using `prompts/social-promo.md`
9. Post to X and LinkedIn via `scripts/social_poster.py both "<text>"`

## Scripts Reference

### hugo_publish.py (for future full automation)
```
python scripts/hugo_publish.py --commit --push
```

### social_poster.py (X / LinkedIn auto-post)
```
python scripts/social_poster.py both "Your promotional text here"
python scripts/social_poster.py x "Only for X"
python scripts/social_poster.py linkedin "Only for LinkedIn"
```
Requires API keys in `.env`:
- X: `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_SECRET`
- LinkedIn: `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET`, `LINKEDIN_ACCESS_TOKEN`

### linkedin_oauth.py (get LinkedIn access token)
```
python scripts/linkedin_oauth.py
```
Opens browser for OAuth, prints the token.
