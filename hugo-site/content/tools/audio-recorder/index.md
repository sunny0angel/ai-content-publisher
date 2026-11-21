---
title: "Online Audio Recorder"
date: 2026-11-19
lastmod: 2026-11-21
description: "Record audio from your microphone in the browser and download it. Free local tool — recordings never leave your machine."
tags: [audio recorder, record audio online, voice recorder, mic recorder, online voice recorder]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "audio-recorder"
faq:
  - q: "Where is the recording stored?"
    a: "In memory in this tab until you download it. Nothing is uploaded, and closing the page discards an unsaved recording."
  - q: "Which format is the download?"
    a: "WebM audio with Opus, which browsers and most editors accept. Convert to MP3 if a platform requires it."
  - q: "Why is the microphone blocked?"
    a: "Browsers require HTTPS and explicit permission. Allow the mic in the address bar; if you denied it earlier, reset the site permission."
  - q: "Can I record system audio?"
    a: "Only microphone input. Capturing a tab or system sound requires a screen-recording tool."
related: [audio-speed, audio-waveform, text-to-speech, video-extract-audio]
---

Record from your microphone with one click, play it back, and download the recording. The audio is captured and stored entirely in your browser — nothing is uploaded anywhere.

<!--more-->

{{< audio-recorder >}}

## How it works

The tool uses the MediaRecorder API to capture your microphone stream into a WebM blob. Output format is WebM (browser-dependent); convert or re-encode elsewhere if you need MP3. For playback speed adjustments, the [audio speed player](/tools/audio-speed/) handles that side.
