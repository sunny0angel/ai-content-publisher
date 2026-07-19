All responses must be written in Chinese / 所有回复必须使用中文.

## 部署后操作

### Search Console 站点地图提交

部署到 Cloudflare Pages 后，在 Google Search Console 中提交以下站点地图 URL：

```
https://aifwd.net/sitemap.xml
```

Hugo 会自动从该索引文件发现各语言的子站点地图：
- `/en/sitemap.xml` — 英文页面
- `/ja/sitemap.xml` — 日文页面
- `/zh/sitemap.xml` — 中文页面

⚠️ 不要提交 `/index.xml`、`/zh/index.xml`、`/ja/index.xml`（这些是 RSS 订阅源，不是标准站点地图，仅包含最近 20 篇文章）。
