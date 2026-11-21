---
title: "Text to Speech (TTS)"
date: 2026-11-19
lastmod: 2026-11-21
description: "Listen to any text read aloud by your browser's built-in voices, with adjustable rate. Free local tool — nothing is uploaded."
tags: [text to speech, tts online, read text aloud, speech synthesis, text reader]
categories: ["Tools"]
draft: false
authors: ["AI Forward"]
slug: "text-to-speech"
faq:
  - q: "Which voices are available?"
    a: "The voices installed in your browser and operating system. Chrome, Edge, macOS and Windows expose different sets, and some platform voices are cloud-backed."
  - q: "Is my text uploaded?"
    a: "The Web Speech API usually runs locally, but some voices use a network service. Do not paste confidential text if you are unsure about the selected voice."
  - q: "Can I download the audio?"
    a: "No. The API plays audio without exposing a file; use a recording tool if you need an audio file."
  - q: "Why is the voice list empty?"
    a: "Voices load asynchronously. Wait a moment or reload; some browsers populate the list only after the first interaction."
related: [audio-recorder, audio-speed, audio-waveform, video-extract-audio]
---

Paste any text and hear it read aloud with your browser's built-in voices — pick the voice and language, adjust the rate. Works offline, uploads nothing, and needs no account.

<!--more-->

{{< text-to-speech >}}

## How it works

The tool drives the browser's SpeechSynthesis API with your chosen voice and rate. It is a listening tool — it does not download audio files. For recording your own voice instead, the [audio recorder](/tools/audio-recorder/) handles the other direction.
