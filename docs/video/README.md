# EasyEPS overview video

`easyeps-overview.mp4` — 77-second narrated product overview, 1920×1080 H.264 + AAC, ~11 MB.

GitHub plays this file directly in the file view, so the blob URL is a watchable link:

    https://github.com/Mouno6969/EasyEPS/blob/<branch>/docs/video/easyeps-overview.mp4

## What is in it

Nine narrated scenes in the product's design language (cream / navy / gold): title, the
Korean-only-prep problem, the 8-module Hangul Basics track, curriculum stats (60 chapters,
1,922 vocabulary, 1,200 practice, 1,196 exam questions), picture questions on the repo's
original SVG artwork, timed mocks, generated-audio story, learner features, end card.
All figures were counted from `content/lessons/*.json` and are enforced in CI.

## How it was made (and how to regenerate)

Not a screen recording — no browser can run in the build sandbox. Every frame is composed
from this repo's own assets (`client/public/basics/*.jpg`, `client/public/eps-images/*.svg`)
with the site's real palette and typography:

1. Bangla and Korean text is shaped with HarfBuzz (WASM, npm `harfbuzzjs`) and emitted as
   SVG glyph `<path>` geometry, because no rasteriser available in the sandbox can resolve
   those fonts (librsvg ignores `@font-face` and falls back to tofu boxes). Fonts come from
   fontsource npm packages, woff2→TTF via `wawoff2`.
2. Scene SVGs are rasterised to 1080p PNG with `sharp` (prebuilt libvips).
3. ffmpeg adds Ken Burns movement per scene, 0.6 s crossfades, and mixes the generated
   voiceover (AAC).

The generator scripts live outside the repo on purpose: they need `sharp`, `harfbuzzjs`
and `wawoff2`, which are build-time video tooling, not application dependencies.

The web encode here is CRF 24; a CRF 19 master (~20 MB) exists at the build workspace
`/home/user/video/easyeps-overview.mp4` if a higher-bitrate cut is ever needed.
