---
title: "PDF 元数据编辑器"
date: 2026-11-20
lastmod: 2026-11-20
description: "查看并修改 PDF 的标题、作者、主题、关键词和创建工具后下载。本地、免费、不上传。"
tags: [PDF元数据, 修改PDF属性, PDF作者, PDF标题, 清除PDF信息]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "pdf-metadata"
---

查看 PDF 自我描述的信息——标题、作者、主题、关键词、创建工具——并在分享前改写这些字段。

<!--more-->

{{< pdf-metadata >}}

## 工作原理

pdf-lib 在加载时读取文档信息字典，保存时写入你的修改。元数据不加密，会随文件一起传播，因此发布前值得检查：内部项目名或个人作者字段很容易泄露。想一次看全，用 [PDF 检查](/zh/tools/pdf-info/)。

## 使用提示

- 个人作者名可替换为团队或品牌名
- 关键词对部分文档管理软件有用，但不是 SEO 标签
- 修改元数据不会删除隐藏内容或注释
