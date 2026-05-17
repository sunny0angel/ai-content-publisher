# AI Content Publisher — 設計ドキュメント

## 1. システム概要

### 目的
AIを活用して多言語（英・日・中）のSEO/AEO/GEO最適化コンテンツを自動生成・公開するシステム。

### ゴール
- 副業で週50分の手作業で運用
- 3言語の記事を週2-3本自動公開
- 1-2年後に月間50K-100K PV達成
- AI検索（ChatGPT/Perplexity/Gemini）で引用される権威サイトに育てる

### 核となる考え方
- **製品レビューはしない**（ハウツー・業界分析・活用ガイドのみ）
- **AI検索最適化（AEO/GEO）を最初から組み込む**
- **3言語同時展開でコンテンツ量とリーチを3倍に**
- **あなたの手間は「確認」だけ**

---

## 2. 技術スタック

| レイヤー | 技術 | 理由 |
|---------|------|------|
| 静的サイト生成 | **Hugo** | 高速、多言語内蔵、メンテナンス不要 |
| ホスティング | **Cloudflare Pages** | 無料、エッジCDN、カスタムドメイン無料、SSL無料 |
| バージョン管理 | **GitHub** | 無料、自動デプロイ連携 |
| 記事生成 | **Claude API** | 高品質な長文生成、多言語対応 |
| 画像生成 | **Gemini API** | あなたの会員を活用 |
| Web検索 | **Bing Web Search API / SerpAPI** | 最新情報のリサーチ（月$5-10） |

### 代替：最初は私（Claude）のWeb検索ツールで代用
- research.pyの代わりに、私のWeb検索機能を使う
- API費用ゼロでスタート可能
- 後からresearch.pyを追加して完全自動化

---

## 3. ディレクトリ構造

```
ai-content-publisher/
│
├── DESIGN.md                         ← この設計書
├── README.md                         ← 運用マニュアル
│
├── .opencode/
│   └── skills/
│       └── ai-content-publisher/
│           ├── SKILL.md              ← Claude Code Skill（本体）
│           ├── config.yaml           ← 設定ファイル
│           ├── .env.template         ← APIキーテンプレート
│           │
│           ├── prompts/
│           │   ├── article-generator.md      ← 記事執筆ベースプロンプト
│           │   ├── gemini-prompt-template.md  ← 画像生成プロンプト
│           │   └── seo-metadata.md           ← SEOメタデータ生成
│           │
│           ├── templates/
│           │   ├── article-howto.md          ← ハウツー型テンプレート
│           │   ├── article-analysis.md       ← 業界分析型テンプレート
│           │   └── article-listicle.md       ← リスト型テンプレート
│           │
│           └── scripts/
│               ├── research.py       ← Webリサーチ自動化（後で実装）
│               ├── gemini_img.py     ← Gemini画像生成
│               ├── hugo_publish.py   ← Hugo記事作成・GitHub連携
│               └── requirements.txt  ← Python依存パッケージ
│
└── hugo-site/                        ← Hugoプロジェクト（別途セットアップ）
    ├── config.toml                   ← Hugo設定（3言語）
    ├── content/
    │   ├── en/                       ← 英語記事
    │   │   └── tutorials/
    │   └── ja/                       ← 日本語記事
    │   │   └── tutorials/
    │   └── zh/                       ← 中国語記事
    │       └── tutorials/
    ├── static/
    │   └── images/                   ← 生成画像の保存先
    ├── layouts/
    │   ├── _default/
    │   │   └── single.html           ← 記事テンプレート（Schema.org対応）
    │   └── index.html
    └── themes/                       ← Hugoテーマ
```

---

## 4. コンテンツモデル

### 4.1 記事タイプ

| タイプ | 説明 | 文字数 | 使用頻度 |
|--------|------|--------|---------|
| **howto** | ハウツーガイド（最も多い） | 2,500-4,000語 | 週2本 |
| **analysis** | 業界分析・トレンド解説 | 2,000-3,500語 | 週1本 |
| **listicle** | リスト形式の活用例・手法 | 2,000-3,000語 | 隔週 |
| **comparison** | 比較ガイド（製品比較ではない） | 2,500-3,500語 | 隔週 |

### 4.2 多言語戦略

```
オリジナル（英語）をClaudeが生成
  → 日本語に翻訳（Claudeで、SEOメタデータも含めて）
  → 中国語に翻訳（Claudeで、SEOメタデータも含めて）
  → 各言語のHugo記事ファイルを生成
  → GitHubにpush → Cloudflareが自動デプロイ
```

**URL構造**：
```
site.com/en/how-to-automate-resume-screening-with-ai/
site.com/ja/how-to-automate-resume-screening-with-ai/
site.com/zh/how-to-automate-resume-screening-with-ai/
```

**SEO上の注意**：
- hreflangタグはHugoが自動生成
- 各言語の記事は独立したSEOメタデータを持つ
- 言語ごとにキーワードは異なる（日本語キーワードは日本語でリサーチ）

### 4.3 テーマ領域

あなたのSAP HR経験 + AI + ITバックグラウンドを活かす：

| カテゴリ | 例 |
|---------|-----|
| AI for Business | How to automate document processing, AI workflow guides |
| AI for HR | AI-powered resume screening, employee analytics |
| AI Tutorials | Using ChatGPT API, building AI agents |
| Tech & Productivity | AI tools comparison, automation best practices |

---

## 5. AEO/GEO戦略（AI検索最適化）

### 5.1 技術的基盤（Hugo設定で対応）

| 対策 | 実装方法 | 優先度 |
|------|---------|--------|
| robots.txtでAIクローラー許可 | Hugoテンプレート | 🔴 高 |
| llms.txt配置 | Hugoテンプレート | 🔴 高 |
| Schema.org構造化データ | レイアウトテンプレートに埋め込み | 🔴 高 |
| hreflangタグ | Hugo多言語機能で自動生成 | 🔴 高 |
| 高速表示 | 静的サイト＋Cloudflare CDNで自動達成 | 🟢 低 |
| sitemap.xml | Hugo自動生成 | 🟡 中 |

### 5.2 記事内AEO対策（SKILL.mdに組み込むルール）

```
【記事執筆時の必須ルール】

① 見出しは疑問形に
   ❌ "AI Resume Screening Overview"
   ✅ "How Does AI Resume Screening Work?"

② 各H2の直後に「Answer Capsule」を配置
   40-60語の自己完結型回答段落
   （AIがこの段落だけ引用しても成立する）

③ FAQセクションを3-5個
   実際の検索クエリを想定したQ&A

④ 具体的な数字・統計を各記事に最低2つ
   "According to a 2026 study..."
   "Companies using AI for X report Y% improvement..."

⑤ 最終更新日を明記
   Hugoのdateフィールドを活用

⑥ 内部リンクを2-3個
   サイト内の関連記事へのリンク
```

### 5.3 llms.txt戦略

```
# AI Content Hub

## AI for HR
- https://site.com/en/hr/guide-1/: Complete guide to AI in HR
- https://site.com/en/hr/guide-2/: How AI transforms recruitment

## AI Tutorials  
- https://site.com/en/tutorials/guide-1/: Step-by-step AI automation
```

- 公開済みの全記事を自動リスト
- Hugoテンプレートで自動生成
- 新しい記事が公開されるたびに更新

---

## 6. パブリッシングワークフロー（週次）

### 6.1 あなたの作業（週50分）

```
日曜 夜（15分）:  私が提案する10トピックから3つ選ぶ
月曜 朝（30分）:  出来上がった記事（3言語×3本=9記事）を読む
月曜 朝（5分）:   問題なければ「公開で」と言う
                  ↓
                  私がGitHubプッシュ → Cloudflare自動デプロイ
```

### 6.2 私（Claude）の作業

```
Step 1: トピック選定（あなたと相談 or 自動提案）
Step 2: Webリサーチ（キーワード分析、競合分析）
Step 3: 英語記事を生成（AEO構造化）
Step 4: 日本語・中国語に翻訳（SEO最適化含む）
Step 5: GeminiAPIでアイキャッチ画像を生成
Step 6: Hugo記事ファイル（index.md）を3言語分作成
Step 7: images/に画像保存
Step 8: GitHubにプッシュ（あなたの確認後 or 下書き状態で）
Step 9: Cloudflare Pagesが自動デプロイ
```

### 6.3 Hugo記事ファイルの構造

```markdown
---
title: "How AI Is Transforming HR Document Processing in 2026"
date: 2026-05-18
lastmod: 2026-05-18
description: "Learn how AI-powered document processing is revolutionizing HR workflows, reducing processing time by 80% and improving accuracy."
tags: ["AI", "HR", "document processing", "automation"]
categories: ["AI for HR"]
image: "/images/hr-document-processing-2026.jpg"
draft: true
---

## How Does AI Document Processing Work?

AI document processing uses machine learning models... [Answer capsule: 40-60 words]

[Elaboration paragraph...]

## What Are the Key Benefits for HR Departments?

[Answer capsule...]
```

---

## 7. Skillアーキテクチャ

### 7.1 SKILL.mdの責務

SKILL.mdは以下の全体フローを定義する：

1. **起動** → `/publish "<topic>"` で開始
2. **トピック分析** → コンテンツタイプ判定
3. **リサーチ** → Web検索（私のツール or research.py）
4. **記事生成** → article-generator.mdプロンプトで執筆
5. **翻訳** → 日・中に翻訳（SEOメタデータ含む）
6. **画像生成** → gemini_img.pyでGemini呼び出し
7. **Hugoファイル生成** → 各言語のindex.md作成
8. **GitHubプッシュ** → 下書きとしてプッシュ
9. **完了報告** → プレビューURLを提示

### 7.2 設定ファイル（config.yaml）

```yaml
site:
  name: "AI Content Hub"
  url: "https://yourdomain.com"
  languages: ["en", "ja", "zh"]
  default_language: "en"

content:
  min_words: 2500
  max_words: 4000
  default_type: "howto"
  aeo_answer_capsule_max_words: 60
  faq_count: 3
  internal_links_min: 2

image:
  style: "modern, clean, tech-themed, blue/white color scheme"
  aspect_ratio: "16:9"

hugo:
  content_dir: "/path/to/hugo-site/content"
  image_dir: "/path/to/hugo-site/static/images"
  draft_default: true
```

### 7.3 プロンプト構成

| プロンプト | 用途 | 変数 |
|-----------|------|------|
| article-generator.md | 英語記事生成 | `{topic}`, `{research_data}`, `{template}` |
| gemini-prompt-template.md | 画像生成指示 | `{topic}`, `{style}` |
| seo-metadata.md | title/description/slug生成 | `{article_content}`, `{language}` |

---

## 8. スクリプト仕様

### 8.1 gemini_img.py

```python
"""
Gemini画像生成スクリプト
Usage: python gemini_img.py "topic" "output_path"
機能:
 - トピックから画像プロンプトを自動生成
 - Gemini APIで画像生成
 - 指定パスに保存
 - リトライ機構（最大3回）
"""
```

### 8.2 hugo_publish.py

```python
"""
Hugo記事ファイル生成 + GitHub連携
Usage: python hugo_publish.py
       (対話的、または引数で制御)

機能:
 - 各言語のindex.mdを/content/{lang}/ に生成
 - 画像を/static/images/ にコピー
 - git add → commit → push
"""
```

### 8.3 research.py（後日実装）

```python
"""
Webリサーチ自動化
Usage: python research.py "topic"
出力: research_output.json

機能:
 - Bing API or SerpAPIで検索
 - 上位結果をスクレイピング
 - 競合構成を分析
 - キーポイント抽出
"""
```

---

## 9. 初期セットアップ計画

| # | 作業 | 所要時間 | 担当 |
|---|------|---------|------|
| 1 | **ドメイン取得** | 10分 | あなた |
| 2 | **GitHubアカウント確認** | 5分 | あなた |
| 3 | **Gemini APIキー取得** | 5分 | あなた（持ってる？） |
| 4 | **Hugoサイト雛形作成** | 30分 | 私 |
| 5 | **Cloudflare Pages連携設定** | 30分 | 私 |
| 6 | **SKILL.md作成** | 現在ここ | 私 |
| 7 | **プロンプト・テンプレート作成** | 60分 | 私 |
| 8 | **gemini_img.py作成** | 30分 | 私 |
| 9 | **hugo_publish.py作成** | 30分 | 私 |
| 10 | **初回テスト公開** | 30分 | 一緒に |
| **合計** | | **約4時間** | |

---

## 10. 収益化戦略（参考）

| 段階 | トラフィック | 収益源 | 目標月収 |
|------|------------|--------|---------|
| 0-6ヶ月 | 0-5K/月 | なし（トラフィック構築期） | $0 |
| 6-12ヶ月 | 5K-20K/月 | 広告（Ezoic） + デジタル商品 | $500-2,000 |
| 12-18ヶ月 | 20K-80K/月 | Mediavine広告 + プレミアム会員 | $2,000-8,000 |
| 18-24ヶ月 | 80K-200K+ | 複合（広告+会員+スポンサー） | $8,000-20,000+ |

---

## 11. リスクと対策

| リスク | 確率 | 対策 |
|--------|------|------|
| Hugo多言語の初期設定ミス | 低 | テンプレートを事前にテスト |
| Gemini画像生成の品質 | 低 | 複数バリエーション生成、リトライ |
| AIコンテンツのGoogleペナルティ | 中 | オリジナルデータ・視点を追加、低品質生成を避ける |
| 翻訳品質の問題 | 低 | Claudeの翻訳品質は高い。ネイティブチェックは不要 |
| モチベーション低下 | 中 | 週50分だけ。最初から完璧を目指さない |
