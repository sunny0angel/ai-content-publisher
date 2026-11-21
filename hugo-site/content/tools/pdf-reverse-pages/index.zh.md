---
title: "PDF 页面倒序"
date: 2026-11-20
lastmod: 2026-11-21
description: "一键把 PDF 的页面顺序整体反转——最后一页变第一页。免费本地工具，不上传。"
tags: [PDF倒序, PDF页面反转, PDF顺序翻转, PDF反向]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-reverse-pages"
faq:
  - q: "什么时候需要反转页面顺序？"
    a: "双面扫描存反了、右开本漫画、传真倒序到达，都是常见场景。"
  - q: "超大文件能用吗？"
    a: "工具会把整个文档读入内存，超过约 100 MB 建议在桌面浏览器中处理。"
  - q: "反转会把页面内容镜像吗？"
    a: "不会。只改变页面顺序，文字和图片方向不变。"
related: [pdf-reorder, pdf-rotate, pdf-duplicate-pages, pdf-n-up]
---

把 PDF 从头到尾翻过来——最后一页变成第一页。适合从右往左的扫描件、双面纸张复原，以及撤销误操作的反转。

<!--more-->

{{< pdf-reverse-pages >}}

## 工作原理

所有页面索引反转后复制进新文档，旋转、注释和页面尺寸都保持不变。若想自定义顺序而非整体反转，请用[页面重排](/zh/tools/pdf-reorder/)。

## 使用提示

- 双面扫描进纸方向错了经常需要这一招
- 执行两次即可回到原来的顺序
- 很大的 PDF 需要几秒——请保持标签页打开
