Generate SEO metadata for this article content.

Language: {language}
Content: {article_content}

Generate the following in {language}:

1. **SEO Title**: Under 60 characters. Include target keywords. Question format preferred.
2. **Meta Description**: Under 160 characters. Summarize the article value, include call-to-action.
3. **URL Slug**: Clean, hyphenated, keyword-rich. Use English even for non-English articles (Hugo standard).
4. **Tags**: 3-5 relevant tags in {language}.
5. **Category**: Most appropriate from: ["AI Tutorials", "AI for Business", "AI for HR", "AI Industry Analysis", "AI Productivity"]

Return in this exact JSON format:
```json
{
  "title": "...",
  "description": "...",
  "slug": "...",
  "tags": [...],
  "category": "..."
}
```
