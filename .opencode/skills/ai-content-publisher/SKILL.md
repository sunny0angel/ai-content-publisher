---
name: ai-content-publisher
description: Use when the user says "/publish" or asks to write/create/publish a new article. Generates SEO/AEO-optimized multi-language (EN/JA/ZH) blog articles, sources hero images, and publishes via Hugo to Cloudflare Pages.
---

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
Step 3.5: データ精査＆強化（下記「Data Verification & Enhancement」を必ず実行）
Step 4: SEOメタデータを生成（SEO Metadataプロンプトリファレンス）
Step 5: 日本語に翻訳（同じプロンプト、lang=jaで再実行）
Step 6: 中国語に翻訳（同じプロンプト、lang=zhで再実行）
Step 7: フリー画像サイトから該当記事に関連する画像をダウンロード（下記「Image Sourcing」参照）
Step 8: 画像を `hugo-site/static/images/{slug}.jpg` に保存
Step 9: Hugo記事ファイル（index.md）を3言語分作成（画像パスを含む。各言語の記事本文冒頭に画像クレジットを可読blockquoteで追加）
Step 10: Hugo build & 各言語のWordCount検証（確認コマンド: `rg -o 'wordcount[^>]*>[^<]+' public/{en=,zh/,ja/}blog/{slug}/index.html`、全言語2,500語/字以上、draft=false確認）
Step 11: GitHubにプッシュ（draft=Hugoフロントマター）
Step 12: プレビューURLをユーザーに提示
Step 13: ユーザー承認後、draft=falseにして再プッシュ
Step 14: プロモーション投稿文を生成（social-promo.md プロンプトリファレンス）
Step 15: social_poster.py で X + LinkedIn に自動投稿
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

### 5. 言語別ワードカウント＆画像クレジットチェック（翻訳後、必ず実行）
- Hugoビルド後、各言語（EN/JA/ZH）の記事ページで `WordCount` を確認し、すべて2,500語以上であること
- WordCount確認コマンド: `rg -o 'wordcount[^>]*>[^<]+' public/{en=,zh/,ja/}blog/{slug}/index.html`
- 画像クレジットが記事本文冒頭にblockquote形式で可読表示されていること（全3言語）
- 画像クレジットに photographer名へのリンク、プラットフォーム名、ライセンス表記が含まれていること（全3言語）

### 6. AI臭除去チェック
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

## Data Verification & Enhancement (Step 3.5: must complete before SEO metadata)

Step 3（セルフレビュー＆修正）完了後、**必ずデータ面の精査と強化を行ってから** SEOメタデータ生成に進む。

### 1. データ診断チェック
記事内のすべてのデータ/統計/数値主張を以下の基準でチェックする：

- データ不足: 主張に対して裏付けデータがない箇所はないか
- 説得力不足: データはあるが、読者を納得させるに足る強さか
- データ品質: 古いデータ、出典不明、信頼性の低いソースを使っていないか
- 表現の問題: 数値がただ羅列されていて、比較や傾向が読み取りにくくなっていないか
- データの新鮮さ: 2025〜2026年のデータに更新可能か
- 一般論の放置: 「多くの企業が...」「増加傾向にある...」など漠然とした表現を具体データで置き換えられるか

### 2. データ再リサーチ
問題が見つかった場合、以下の方針でデータを再収集する：

- 業界レポート・統計（McKinsey, Gartner, Forrester, IDC, Statista など）
- 政府・公的機関のデータ（US Census Bureau, 経済産業省, 国家統計局 など）
- 査読付き論文・学術研究（Google Scholar, arXiv）
- 上場企業のIR資料・決算発表
- 信頼できるニュースソース（Reuters, Bloomberg, Nikkei, 36Kr など）

収集したデータは、出典URLとともに整理し、記事内でanchor text付きリンクとして自然に引用する。

### 3. データの可視化（テーブル＆チャート）
データを読者に直感的に伝えるため、以下のルールで可視化する：

#### テーブル（Hugo Markdown標準テーブル）
- 複数のデータポイントの比較には必ずテーブルを使用
- 例:
  ```markdown
  | 指標 | 2024 | 2025 | 2026 (予測) |
  |------|------|------|-------------|
  | AI導入率 | 35% | 55% | 72% |
  | コスト削減率 | 12% | 18% | 25% |
  ```

#### チャート画像（scripts/chart_generator.py を使用）
以下の条件下では**必ずチャート画像を生成して記事に埋め込む**：
- 時系列の傾向を示す → **折れ線グラフ（line）**
- カテゴリ間の比較 → **棒グラフ（bar）** または **横向き棒グラフ（hbar）**
- 構成比・シェアを示す → **円グラフ（pie）**
- データが3項目以上あり、テーブルだけでは直感的でない
- 読者が一目で傾向を把握できるべき重要なデータ

##### チャート生成手順
1. データをJSONファイルにまとめる（テンプレート参照）
2. `python scripts/chart_generator.py <json_file>` を実行
3. 画像が `hugo-site/static/images/charts/{filename}` に生成される
4. 記事のMarkdown内で以下のように画像を埋め込む:
   ```markdown
   ![Chart title](/images/charts/{filename})
   ```
5. 画像のalt textはSEOとアクセシビリティのため説明的に記述する
6. チャート画像の下に出典を明記する:
   ```markdown
   出典: [Source Name](URL), [Year]
   ```

##### JSONテンプレート

**棒グラフ（bar）:**
```json
{
  "type": "bar",
  "filename": "ai-adoption-rates.png",
  "title": "AI導入率の業界別比較（2026年）",
  "xlabel": "業界",
  "ylabel": "導入率 (%)",
  "color": "#2563eb",
  "data": [
    {"label": "IT", "value": 85},
    {"label": "金融", "value": 72},
    {"label": "医療", "value": 58},
    {"label": "製造", "value": 65},
    {"label": "小売", "value": 48}
  ]
}
```

**円グラフ（pie）:**
```json
{
  "type": "pie",
  "filename": "ai-budget-allocation.png",
  "title": "AI予算配分の内訳（2026年）",
  "data": [
    {"label": "インフラ", "value": 35},
    {"label": "人材", "value": 28},
    {"label": "ソフトウェア", "value": 22},
    {"label": "コンサルティング", "value": 15}
  ]
}
```

**折れ線グラフ（line）:**
```json
{
  "type": "line",
  "filename": "ai-market-growth.png",
  "title": "AI市場規模の推移（2022-2026年）",
  "xlabel": "年",
  "ylabel": "市場規模 (億$)",
  "color": "#2563eb",
  "data": [
    {"label": "2022", "value": 870},
    {"label": "2023", "value": 1130},
    {"label": "2024", "value": 1520},
    {"label": "2025", "value": 1980},
    {"label": "2026", "value": 2540}
  ]
}
```

**横向き棒グラフ（hbar）:**
```json
{
  "type": "hbar",
  "filename": "roi-by-sector.png",
  "title": "AI投資ROIの業界別比較",
  "xlabel": "ROI (%)",
  "ylabel": "業界",
  "color": "#2563eb",
  "data": [
    {"label": "IT", "value": 320},
    {"label": "金融", "value": 285},
    {"label": "医療", "value": 210},
    {"label": "製造", "value": 195},
    {"label": "小売", "value": 160}
  ]
}
```

##### チャートデザインルール
- カラー: 青系 (#2563eb, #3b82f6, #60a5fa ...) を使用
- アスペクト比: bar/line/hbar は 10:6、pie は 8:8
- DPI: 150（Web表示最適化）
- フォントサイズ: タイトル14pt, 軸ラベル12pt, データラベル11pt bold
- 枠線: top/right は非表示（clean design）
- ファイル名: `{slug}-chart-{n}.png`（lowercase, hyphenated）
- 保存先: `hugo-site/static/images/charts/`

### 4. データ検証の合格基準
以下のすべてを満たすまで修正を繰り返す：
- 各主要主張に少なくとも1つの具体的データが付随している
- データは2025〜2026年の最新ソースである
- すべてのデータに出典リンクが付いている
- 3項目以上の比較データはテーブルまたはチャートで可視化されている
- グラフやテーブルは単独で意味をなす（記事を読まなくても理解できる）
- チャート画像のalt textが出典付きで設定されている

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
- Minimum 2,500 words/characters per article (EN / JA / ZH 各言語別に達成すること)
- Maximum 4,000 words/characters per article (各言語別)
- 各言語のHugoビルド後の `WordCount` を確認し、すべての言語が2,500語/字以上であることを検証する
- 確認コマンド: `rg -o 'wordcount[^>]*>[^<]+' public/{en=,zh/,ja/}blog/{slug}/index.html`
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
images:
  featured_image: "/images/slugified-name.jpg"
draft: true
slug: "url-slug"
---

## Question-Form Heading Here

[Answer capsule: 40-60 word self-contained answer]

[Elaboration: 2-3 paragraphs with detail, examples, data...]
```

**NOTE:** Do NOT include `wordcount` or `readingtime` in front matter. With `hasCJKLanguage = true` in `hugo.toml`, Hugo's built-in `.WordCount` and `.ReadingTime` correctly handle CJK languages (counting each CJK character as one word and using 500 chars/min reading speed). The blog template uses `.ReadingTime` directly and displays language-appropriate labels via i18n (`words` key: EN="words", ZH="字", JA="文字").

## Image Requirements

- Aspect ratio: 16:9 (1200px width recommended)
- Style: Modern, clean, tech-themed photo
- Color: Blue/white/tech gradient palette
- No text overlays in the image
- File naming: `{slug}.jpg` (lowercase, hyphenated, slugと一致させる)
- Save to: `hugo-site/static/images/{slug}.jpg`
- Attribution: 記事本文の冒頭に **可読なブロック引用** として表示（HTMLコメントだけでは不可）:
  ```markdown
  > **Featured image:** [description of image]. Photo by [Photographer](https://source-url) on [Platform] ([License]).
  ```

## Image Sourcing

Download a free image from one of these sites (CC0/public domain or free license). Save to `hugo-site/static/images/{slug}.jpg` (1200px width recommended).

### Preferred Sources
- **Pexels** (https://www.pexels.com) — すべて無料, attribution不要だが推奨. 写真家名とPexelsリンクを添える.
- **Pixabay** (https://pixabay.com) — CC0, attribution不要だが推奨.
- **Unsplash** (https://unsplash.com) — Unsplash License, attribution推奨.

### Search Strategy
Search with keywords related to the article topic. Prefer photos over illustrations. 16:9 aspect ratio (landscape) recommended.

### Attribution Format (必須 — HTMLコメントではなく可読表示)
画像のクレジットは**記事本文の冒頭**にblockquote形式で可読表示する。HTMLコメントだけでは不可。

**EN:**
```markdown
> **Featured image:** Robotic hand reaching into a digital network. Photo by [Tara Winstead](https://www.pexels.com/photo/white-robot-on-wooden-surface-8386440/) on Pexels (Free to use).
```

**JA:**
```markdown
> **注目の画像:** デジタルネットワークに差し伸べられたロボットハンド。写真提供: [Tara Winstead](https://www.pexels.com/photo/white-robot-on-wooden-surface-8386440/)（Pexels / 無料利用可）
```

**ZH:**
```markdown
> **Featured image:** 伸向数字网络的机械手。Photo by [Tara Winstead](https://www.pexels.com/photo/white-robot-on-wooden-surface-8386440/) on Pexels（免费使用）
```

ルール:
- 写真家名へのリンク、プラットフォーム名、ライセンス表記を必ず含める
- 各言語で自然に翻訳する（英語は英語らしく、日本語は日本語らしく）
- 3言語すべての記事ファイルに同じattributionを追加する

### Download Command
```bash
curl -sL -o hugo-site/static/images/{slug}.jpg "[image direct URL]" && file hugo-site/static/images/{slug}.jpg
```

## CJK Word Count & Reading Time Configuration

JA/ZH articles require special handling for word count and reading time. The following are already set up and must NOT be changed:

### hugo.toml
```toml
hasCJKLanguage = true
```
This tells Hugo to count each CJK character as one word and use 500 chars/min reading speed for CJK content.

### layouts/blog/single.html (overridden)
```go
{{- $wc := .WordCount -}}
{{- with .Params.wordcount -}}{{- $wc = . -}}{{- end -}}
<span id="wordcount" class="wordcount">{{ $wc }} {{ i18n "words" }}</span>
{{ $readingTime := .ReadingTime }}
{{ if lt $readingTime 1 }}
  {{ $readingTime = 1 }}
{{ end }}
{{- with .Params.readingtime -}}{{- $readingTime = . -}}{{- end -}}
<span id="reading-time" class="reading-time">{{ $readingTime }} {{ i18n "min_read" | default "min read" }}</span>
```
Key points:
- Uses Hugo's `.ReadingTime` (not `div $wc 200`) so CJK reading speed (500 cpm) is automatically applied
- Uses i18n for the "words" label (EN="words", ZH="字", JA="文字")
- Front matter `wordcount`/`readingtime` overrides are allowed but should NOT be used (they override accurate Hugo calculations)

### i18n keys
- EN `words`: "words"
- ZH `words`: "字"
- JA `words`: "文字"

## Publishing Process

1. Create all article files
2. Download image from Pexels/Pixabay/Unsplash, save to `static/images/{slug}.jpg`
3. Add attribution blockquote at the top of each language's article body (visible, not HTML comment)
4. Set `draft: true` initially
5. Hugo buildを実行して画像パス確認 + 各言語のWordCountとreading-timeを確認（確認コマンド: `rg -o 'wordcount[^>]*>[^<]+' public/{en=,zh/,ja/}blog/{slug}/index.html`、全言語2,500語/字以上）
6. Run git commands for commit + push
7. Tell user the preview URL
8. Wait for user approval ("公開で" or "publish")
9. Change draft to false, git commit + push again
10. Generate social promo posts (X + LinkedIn) using `prompts/social-promo.md`
11. Post to X and LinkedIn via `scripts/social_poster.py both "<text>"`

## Scripts Reference

### hugo_publish.py (for future full automation)
```
python scripts/hugo_publish.py --commit --push
```

## Post-Deployment: Search Console 站点地图提交

### 提交的 URL

部署到 Cloudflare Pages 后，在 Google Search Console 中提交：

```
https://aifwd.net/sitemap.xml
```

Hugo 会自动从该索引文件发现各语言的子站点地图：
- `/en/sitemap.xml` — 英文页面
- `/ja/sitemap.xml` — 日文页面
- `/zh/sitemap.xml` — 中文页面

### ⚠️ 不要提交的 URL

| URL | 原因 |
|-----|------|
| `/index.xml` | RSS 订阅源，不是标准站点地图 |
| `/zh/index.xml` | RSS 订阅源，仅包含最近 20 篇文章 |
| `/ja/index.xml` | RSS 订阅源，仅包含最近 20 篇文章 |

### social_poster.py (X / LinkedIn auto-post)
```
python scripts/social_poster.py both "Your promotional text here"
python scripts/social_poster.py x "Only for X"
python scripts/social_poster.py linkedin "Only for LinkedIn"
```
Requires API keys in `.env`:
- X: `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_SECRET`
- LinkedIn: `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET`, `LINKEDIN_ACCESS_TOKEN`

### chart_generator.py (データ可視化チャート生成)
```
python scripts/chart_generator.py <data.json>
```
JSONファイルで定義したデータから棒グラフ(bar)、折れ線グラフ(line)、円グラフ(pie)、横向き棒グラフ(hbar)を生成する。
出力先: `hugo-site/static/images/charts/{filename}.png`
必要な依存: matplotlib, Pillow（`pip install matplotlib Pillow`）

### linkedin_oauth.py (get LinkedIn access token)
```
python scripts/linkedin_oauth.py
```
Opens browser for OAuth, prints the token.
