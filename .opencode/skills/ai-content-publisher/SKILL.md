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
Step 3: SEOメタデータを生成（SEO Metadataプロンプトリファレンス）
Step 4: 日本語に翻訳（同じプロンプト、lang=jaで再実行）
Step 5: 中国語に翻訳（同じプロンプト、lang=zhで再実行）
Step 6: 画像プロンプトを生成し、ユーザーに提示（gemini-prompt-template.md）
Step 7: ユーザーがGeminiで生成 → 指定パスに保存
Step 8: Hugo記事ファイル（index.md）を3言語分作成（画像パスを含む）
Step 9: GitHubにプッシュ（draft=Hugoフロントマター）
Step 10: プレビューURLをユーザーに提示
Step 11: ユーザー承認後、draft=falseにして再プッシュ
```

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

## Scripts Reference

### hugo_publish.py (for future full automation)
```
python scripts/hugo_publish.py --commit --push
```
