---
title: "20 PDF Tools That Never Upload Your Files"
date: 2026-11-20
lastmod: 2026-11-20
description: "Merge, split, rotate, sign, compress, and convert PDFs entirely in your browser. Twenty local PDF tools built on pdf-lib and PDF.js — no uploads, no accounts, no file-size paywalls."
tags: [free PDF tools, merge PDF, split PDF, compress PDF, sign PDF, PDF to JPG, browser tools, privacy]
categories: ["AI Tools"]
images:
  featured_image: "/images/pdf-tools-roundup.jpg"
draft: false
authors: ["AI Forward"]
slug: "pdf-tools-roundup"
---

> **Featured image:** A close-up of a binder with documents in sepia tone. Photo by [Joachim Schnürle](https://www.pexels.com/photo/close-up-of-a-binder-with-documents-in-sepia-tone-32201000/) on Pexels (Free to use).

PDF is where the documents you cannot afford to leak live: contracts, invoices, passports, medical letters, signed offers. Yet almost every "free PDF tool" online asks you to upload that file to a stranger's server, wait in a queue, and accept a two-files-per-hour limit — because server-side processing is expensive for the operator.

There is no technical reason for that trade anymore. Browsers ship with the same primitives PDF services use: a PDF parser and writer, a renderer, a canvas, and enough memory for ordinary documents. So we built **20 PDF tools that run entirely in your tab**, on top of two open-source libraries — [pdf-lib](https://pdf-lib.js.org/) for document structure and [PDF.js](https://mozilla.github.io/pdf.js/) for rendering. No upload, no account, no watermark, and no queue. Your file is read from disk by the browser and written back to disk by the browser; the network is never involved.

## The full set at a glance

| What you need to do | Tool |
|---|---|
| Combine several PDFs | [Merge PDF](/tools/pdf-merge/) |
| Pull out selected pages | [Split PDF](/tools/pdf-split/) |
| Remove pages | [Delete PDF Pages](/tools/pdf-delete-pages/) |
| Fix sideways or upside-down scans | [Rotate PDF](/tools/pdf-rotate/) |
| Change paper size | [Resize PDF](/tools/pdf-resize/) |
| Add page numbers | [Add Page Numbers](/tools/pdf-page-numbers/) |
| Mark a draft or confidential copy | [Add Watermark](/tools/pdf-watermark/) |
| Check what the file reveals | [PDF Inspector](/tools/pdf-info/) |
| Remove author and title metadata | [PDF Metadata Editor](/tools/pdf-metadata/) |
| Lock filled form values | [Flatten PDF Forms](/tools/pdf-flatten/) |
| Stamp a signature | [Sign PDF](/tools/pdf-sign/) |
| Shrink a scan | [Compress PDF](/tools/pdf-compress/) |
| Turn pages into images | [PDF to JPG](/tools/pdf-to-jpg/) |
| Turn images into a PDF | [Images to PDF](/tools/images-to-pdf/) |

## 1. Organize pages without re-encoding them

The first family is pure page surgery: [merge](/tools/pdf-merge/), [split](/tools/pdf-split/), [delete](/tools/pdf-delete-pages/), [reorder](/tools/pdf-reorder/), [reverse](/tools/pdf-reverse-pages/), [duplicate](/tools/pdf-duplicate-pages/), [blank pages](/tools/pdf-blank-pages/), and [N-up](/tools/pdf-n-up/).

All of them work the same way: pages are copied as objects into a new document, not re-rendered as pixels. That distinction matters. A merge or split performed this way keeps text selectable, links intact, and vector graphics sharp; a tool that rasterizes pages to combine them does not. It also means the operations are fast — a 200-page merge is a file-copy problem, not a rendering problem.

Two practical notes. First, page ranges are 1-based, matching what your PDF reader shows. Second, omissions are deletions: in the reorder tool, if you type `3, 1` for a five-page document, you get two pages, not five. That is deliberate — it makes the same tool useful for both reordering and pruning — but it is worth knowing before you click download.

N-up deserves a separate mention because it is the rare "green" PDF tool: two or four pages are embedded as vector forms on one landscape sheet, cutting paper use by half or a quarter without turning text into an image. For slide decks and handout packs, it is the difference between a 40-page print job and a 10-page one.

## 2. Fix the page, not the content

The second family adjusts presentation: [rotate](/tools/pdf-rotate/), [resize](/tools/pdf-resize/), [crop](/tools/pdf-crop/), [page numbers](/tools/pdf-page-numbers/), and [watermarks](/tools/pdf-watermark/).

These tools deliberately avoid re-rendering. Rotation is written into the page's rotation attribute; resizing changes the media box; cropping sets a crop box; page numbers and watermarks are drawn as vector text on top. The content stream is untouched, so a rotated scan does not lose a generation of quality, and a numbered document remains searchable.

The crop tool is the one people misunderstand most. Cropping hides everything outside the box — readers and printers ignore it — but the data is still in the file. That is good for reversibility (set the margins back to zero and the page returns) and bad for redaction. If the goal is to remove sensitive content, cropping is not enough; the content must be deleted, not covered.

Watermarking has the same honesty requirement. A text watermark is a visual mark, not access control. At 15–20% opacity it deters casual sharing and labels a draft clearly, but anyone with a PDF editor can remove it. Treat it as communication, not security.

## 3. The privacy layer: inspect before you share

Three tools exist specifically because PDFs leak more than people expect: the [inspector](/tools/pdf-info/), the [metadata editor](/tools/pdf-metadata/), and the [form flattener](/tools/pdf-flatten/).

Open almost any PDF and you will find a document information dictionary: title, author, subject, keywords, creator, producer. It is not encrypted, it travels with the file, and it is frequently wrong in the most revealing way — a internal project codename in the title, a personal name in the author field, a template path in the producer field. The inspector shows all of it at once; the metadata editor lets you replace it before the file leaves your machine.

The form flattener solves a different problem. A filled AcroForm still contains editable fields; a recipient can change a quantity, a date, or a name, and the document will look untouched. Flattening bakes the current values into the page content and removes the interactive structure. It is the correct last step before archiving a filled order form or a completed onboarding packet. It is not encryption — the page can still be edited graphically — but the values are no longer a form.

[Signing](/tools/pdf-sign/) belongs here too, with a clear caveat. Stamping a signature image is an e-signature in the everyday sense: it records intent and makes the document look executed. It is not a cryptographic digital signature and does not prove who signed. For contracts that need identity assurance, use a certificate-based service. For internal approvals and quick turnarounds, a stamped PNG is often exactly the right amount of ceremony.

## 4. Convert and shrink — with eyes open

The conversion family is [images to PDF](/tools/images-to-pdf/), [PDF to JPG](/tools/pdf-to-jpg/), and [compress PDF](/tools/pdf-compress/).

Images-to-PDF embeds each JPG or PNG at full resolution and fits it to the page without distortion — the fastest way to turn phone photos of paper into one shareable file. PDF-to-JPG goes the other direction, rendering pages at 96, 150, or 300 DPI through PDF.js and letting you download individual pages or the whole set. Both are local, so a passport scan never crosses the network.

Compression is the tool that needs the most honesty. It works by rendering each page to a canvas and rebuilding the PDF from JPEG images. That is extremely effective on scans and image-heavy decks — 50–80% reductions are normal at 110 DPI and 65% quality — but it rasterizes text. After compression, the text is no longer selectable or searchable. For a scanned contract that was never searchable, this is a pure win. For a digitally generated report, it is a trade you should make consciously, keeping the original.

## Why local processing is not just a slogan

Three practical differences separate a local PDF tool from an upload service.

**Privacy is structural, not contractual.** A upload service can promise to delete your file in an hour; a local tool cannot receive it in the first place. For legal, medical, and HR documents, that changes the risk calculation entirely — there is no vendor to trust, no retention policy to audit, no breach notification to wait for.

**No artificial limits.** There is no two-file cap, no 10 MB ceiling, no "upgrade to Pro" for batch processing. The limits are your device's memory and your patience. A 300-page scan may take a few seconds longer; it will not ask for a credit card.

**It works offline.** After the page has loaded, the libraries are cached and the tools keep working without a network connection. That matters on trains, in client offices with guest Wi-Fi, and anywhere you would rather not upload a document to begin with.

## The honest limitations

Local tools have real edges, and pretending otherwise would be the same marketing everyone else does.

- **Encrypted PDFs are rejected.** pdf-lib cannot open password-protected files. Remove the password in your PDF reader first; the tools will tell you clearly when this is the problem.
- **No OCR.** Scanned text stays an image. If you need searchable scans, run OCR in a dedicated tool first, then compress or organize here.
- **Compression rasterizes.** As above: smaller scans, but no selectable text. Keep the original if the document may need to be searched later.
- **A stamped signature is not a certificate.** It shows intent, not identity.
- **Complex print workflows are out of scope.** Imposition for a professional print shop, PDF/X validation, and color separation belong to desktop publishing software.

Within those edges, the set covers the PDF chores that actually recur in an office week: combining a signed page into a contract, pulling an appendix out of a report, rotating a batch of scans, adding page numbers before a board pack, stripping a client name from metadata, and shrinking a 40 MB scan to something an email server will accept.

## Frequently Asked Questions

{{< faq-schema >}}
[
  {"q": "Are these PDF tools really free, and do I need an account?", "a": "Yes. All 20 tools are static pages with no backend, no signup, and no usage limits. The only cost is your own bandwidth for loading the page once."},
  {"q": "Where do my PDF files go when I use these tools?", "a": "Nowhere. The file is read with the browser's File API, processed in memory by pdf-lib or PDF.js, and downloaded as a new file. There is no server endpoint to receive it, so nothing is uploaded."},
  {"q": "Can I merge or split a password-protected PDF?", "a": "Not directly. Encrypted PDFs must be unlocked first in your PDF reader, then saved without a password. The tools will show an error rather than silently producing a broken file."},
  {"q": "Does compressing a PDF reduce quality?", "a": "It reduces resolution and re-encodes pages as JPEG, so scans look slightly softer and text becomes non-selectable. At 110 DPI and 65% quality the visual difference is small on scanned documents; keep the original for text-heavy files."},
  {"q": "Is the signature tool legally binding?", "a": "It creates a visual e-signature, which is fine for internal approvals and many everyday agreements, but it is not a certificate-based digital signature and does not verify identity. Use a qualified e-signature provider where the law requires one."},
  {"q": "Do the tools work on iPhone and Android?", "a": "Yes. They use standard browser APIs and run in mobile Safari and Chrome. Very large PDFs are limited by the device's available memory rather than by an arbitrary file-size cap."}
]
{{< /faq-schema >}}

## Where to start

If you only need one thing, start with the job in front of you: the [merge tool](/tools/pdf-merge/) for combining files, the [compressor](/tools/pdf-compress/) for an oversized scan, or the [metadata editor](/tools/pdf-metadata/) before sending a document outside your organization.

If you want the whole picture, the [tools hub](/tools/) groups all 66 browser tools by job — PDF, comparison, developer, image, audio, video, and everyday math. The PDF group is the newest, and it is the one we built with the most attention to the least glamorous part of the job: making sure the file never leaves your machine.
