---
title: "Video Info Checker"
date: 2026-11-19
lastmod: 2026-11-21
description: "Read a video's resolution, duration, and file size locally in your browser. Free tool — nothing is uploaded."
tags: [video info, video metadata, check video resolution, video duration, video file info]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "video-info"
faq:
  - q: "What does it read?"
    a: "Resolution, duration and file size as reported by the browser, plus the file type."
  - q: "Does it upload the video?"
    a: "No. Metadata is read from the local file in the tab."
  - q: "Why is the duration 0 or Infinity?"
    a: "Some WebM and MKV files lack a duration header. Convert to MP4 for reliable metadata."
  - q: "Can it show codec or bitrate?"
    a: "No. Browsers expose only basic metadata; use ffprobe for codec, bitrate and frame rate."
related: [video-thumbnail, video-extract-audio, audio-waveform, image-resizer]
---

Select a video and instantly see its resolution, duration, and file size — the metadata you need before uploading or encoding. Read locally in your browser; the file is never uploaded.

<!--more-->

{{< video-info >}}

## How it works

The browser reads the file's container metadata as soon as it loads. When a video "won't upload", the size or duration here usually explains why before you even try. Pair with the [video frame grabber](/tools/video-thumbnail/) to preview content at the same time.
