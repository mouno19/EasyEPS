# EasyEPS — Announcement Post

> Draft announcement, written from the current state of the repository.
> All numbers below were counted directly from `content/lessons/*.json`, `content/manifest.json`, and the `*.test.ts` suites — and cross-checked against `scripts/audit_runtime_contract.py`, which now verifies the manifest in CI.

---

## EasyEPS: a Bangla-first EPS-TOPIK prep platform, built from scratch for Bangladeshi learners going to Korea

Every year tens of thousands of Bangladeshi workers sit the **EPS-TOPIK** to qualify for employment in Korea. The exam is in Korean. The official textbook is in Korean. Most free prep material online assumes you can already read Hangul — and almost none of it explains anything in Bangla.

**EasyEPS** closes that gap. It is a complete, open-source (MIT) learning platform where the default language is **Bangla**, Korean is the subject being learned, and English is a supporting language. A learner can go from "I cannot read a single Korean letter" to "I just scored myself on a 40-question timed mock exam" without ever leaving the app, and without creating an account.

- **Live app:** https://easy-eps.vercel.app
- **Source:** https://github.com/Mouno6969/EasyEPS

---

## What is actually in it

### 1. A Hangul literacy track that comes *before* Chapter 1

The single biggest failure mode in EPS prep is a learner opening Chapter 1 (자기소개 / Self Introduction) and being unable to read the vocabulary cards. EasyEPS ships a dedicated **Basics track** with eight sequential modules:

| # | Module | What the learner does |
|---|---|---|
| 1 | Welcome | Orientation, how the track works |
| 2 | Consonants | 자모 recognition and sound |
| 3 | Vowels | 모음 recognition and sound |
| 4 | Syllables | Syllable-block composition, built live from jamo |
| 5 | Batchim | 받침 (final consonant) introduction |
| 6 | Speak Lab | Listen-and-repeat with speech recognition |
| 7 | Write Lab | Stroke-order tracing and writing practice |
| 8 | Checkpoint | Server-graded capstone that unlocks the curriculum |

The unlock is **not** client-side. `basicsProgress.completed` is written only by server-side grading of checkpoint answers, a trusted legacy-user grandfather migration, or an admin — never by whatever the browser reports. There is a documented flag rollout (`BASICS_GATE_ENABLED`, off by default) plus a backfill script and rollback plan in `docs/BASICS_RUNBOOK.md`, so existing learners are never locked out of progress they already earned.

### 2. 60 chapters of original EPS-TOPIK curriculum

All content is **original authored material** covering the standard 60 EPS-TOPIK textbook topics. No official textbook PDFs are stored or redistributed. Counted across `content/lessons/lesson-01.json` … `lesson-60.json`:

| Metric | Count |
|---|---|
| Chapters | **60** (all validated against the v2 schema) |
| Vocabulary items | **1,922** |
| Practice questions | **1,200** |
| EPS-style exam questions | **1,196** — 858 reading / 338 listening |
| Picture-based exam questions | **571** |

Chapter coverage follows the real exam weighting: **24 daily life · 22 workplace · 6 culture · 4 industrial safety · 4 laws & regulations**.

Every vocabulary item carries Korean, romanization, Bangla, English, part of speech, a trilingual example sentence, and a Bangla pronunciation tip. Every question carries a Bangla explanation of the answer, so a wrong answer teaches something instead of just marking red.

The 571 picture questions use **33 original SVG assets** authored for this project — hand tools, machinery (excavator, forklift, tiller, tractor), workplace objects, actions, and safety signage (hard hat, ear protection, electric hazard, emergency exit, no smoking, wet floor, first aid). This mirrors the EPS-TOPIK's own picture-and-sign question format.

### 3. Three timed mock exams, plus a "smart" mode

| Test | Questions | Time | Split |
|---|---|---|---|
| মাইক্রো টেস্ট (micro) | 10 | 12 min | 6 reading + 4 listening |
| দ্রুত অনুশীলন (quick) | 20 | 25 min | 12 reading + 8 listening |
| পূর্ণাঙ্গ পরীক্ষা (full) | 40 | 50 min | 24 reading + 16 listening |

The runner has a countdown timer, a question palette with answered/unanswered state, prev/next navigation, section badges, and a post-submit review with per-question Bangla explanations and study tips that differ for reading vs. listening items.

**Smart mock** goes further: it pulls due items from the spaced-repetition queue plus recently-missed items, interleaves chapters so you never see five questions from one chapter in a row, and uses Fisher–Yates shuffling with a rebalanced answer key across options A–D so guessing patterns don't inflate scores. Section focus can be pinned to reading or listening.

Listening passages stay **hidden until you submit** — you press the headphone button and listen, exactly like the real exam.

### 4. Audio without a single audio file

Pronunciation is generated dynamically through the browser's Web Speech API (`ko-KR`) and a multi-speaker dialogue engine, so there are **zero pre-recorded audio files** in the repository. Listening dialogues assign distinct voices to distinct speakers — a gendered voice pair when the browser has two or more Korean voices, and clearly different pitches (0.75 male / 1.3 female) with a 420ms turn gap when it has only one. Speaker labels are never read aloud, exactly like real exam audio.

All 338 listening passages are normalized to the canonical two-speaker format (`남자:` / `여자:`, one turn per line), and `scripts/audit-listening-dialogues.py` enforces it — 276 passages are speaker-labelled dialogues, 62 are single-voice narration. A **Pronunciation Coach** uses speech recognition to listen to the learner and score their attempt.

### 5. A Bangla AI tutor

Signed-in learners get a tutor at `/tutor` that answers EPS-TOPIK questions in Bangla, with chapter-aware prompting. It runs on **xAI Grok** (`grok-4.5` by default, configurable). The API key is read **only on the server** in `server/_core/llm.ts` and never enters any `VITE_*` client environment variable. Tutor calls are rate-limited.

### 6. Progress that survives without an account

Guest mode is a first-class citizen, not a crippled demo:

- Study, practice, take chapter exams and full mocks, all with `localStorage` progress
- Spaced repetition (due reviews + weak items), weekly mock challenge, daily study plan
- On sign-in, guest progress **merges** into the account and the learner gets a confirmation toast
- Signed-in adds durable cross-device progress, streaks, badges, the planner, certificates, and the admin-gated dashboard

Certificates are printable, carry a recipient snapshot, and verify publicly at `/certificate/:code`. Badges and certificates are awarded from **server-graded attempts** — the client-computed score is deliberately not trusted for anything that grants a credential.

### 7. Installable and offline-capable

A PWA shell (manifest, service worker, `OfflineLessonManager`) means the app installs to a home screen and lessons can be cached for study without a connection — which matters a lot for learners on metered mobile data.

---

## Design

A deliberately calm, editorial identity rather than the usual gamified-bright learning-app look: **cream paper surfaces, deep navy headlines, muted gold line art, sage accents**, sacred-geometry grid motifs, and Bengali serif display typography. Built on shadcn/ui + Radix primitives, Framer Motion, and Tailwind 4 design tokens. Accessibility work includes a skip-to-content link, visible focus states, and respect for reduced-motion preferences. It is verified responsive down to a 375px viewport.

---

## Stack

| Layer | Technology |
|---|---|
| Frontend | React 19, Tailwind CSS 4, Vite 7, wouter, TanStack Query, Framer Motion, Recharts, shadcn/ui + Radix |
| API | Express + **tRPC 11** (end-to-end typed, superjson) |
| Data | Drizzle ORM + MySQL, Zod 4 validation on every lesson load |
| Auth | OAuth (Manus portal), JWT sessions, role-based admin procedures |
| AI | xAI Grok, server-side only |
| Tests | Vitest — **153 test cases across 14 suites**: 12 server suites, 131 cases (basics gating 49, profile 20, image questions 10, learner efficiency 9, scoring 8, curriculum 8, certificates 8, hangul composition 7, validation errors 5 + 3, mock-test scoring 3, auth logout 1) and 2 client suites, 22 cases (dialogue TTS 17, Korean speech 5) |
| Content audits | Two Python pipelines: `audit_runtime_contract.py` (practice/EPS field contract + manifest sync) and `audit-listening-dialogues.py` (dialogue speaker formatting) |
| CI | GitHub Actions: typecheck → unit tests → content contract audit → production build, on every push and PR |

Two architecture decisions worth calling out:

1. **Lesson JSON is the public source of truth.** Curriculum reads hit validated JSON files, not the database. `DATABASE_URL` is genuinely optional — without it the full curriculum, lessons, and exams still work, and protected procedures return a clear availability error instead of crashing. That makes the repo trivially runnable for anyone who just wants to read the content.
2. **Trust boundaries are explicit.** Client-reported step progress is allowed for UX; anything that unlocks content, records an attempt, or issues a certificate is decided server-side.

---

## Run it locally

```bash
# Node 22+, pnpm 10+
git clone https://github.com/Mouno6969/EasyEPS
cd EasyEPS
pnpm install
cp .env.example .env     # curriculum browsing works with an empty .env

pnpm dev                 # API + Vite on http://localhost:3000

pnpm check               # TypeScript
pnpm test                # Vitest
pnpm build               # production client + server bundle
python3 scripts/audit_runtime_contract.py
```

`docs/DEPLOY.md` covers production hosting (Railway, Fly.io, Render, or any Node 22 host + managed MySQL) and a post-go-live smoke checklist.

---

## What's next

Five feature branches are open right now:

- **Natural Korean audio library fallback** — generated native-speaker audio where browser TTS voices are poor or unavailable
- **Adaptive learning v5** — daily vocabulary, adaptive difficulty, more realistic listening practice
- **Item-level spaced repetition** — drill the specific words you missed, not the whole chapter again
- **Repeated-question prevention in smart mocks**
- **Adaptive learner experience**

Still on the roadmap: production hosting with MySQL and OAuth secrets wired up, workplace scenario content packs, and a full visual lesson editor in the admin panel.

---

## Honest disclaimer

EasyEPS is an **independent, unofficial** learning project. All curriculum content is original. It teaches and supports exam preparation — it does not administer exams, and official schedules, registration, results, immigration, and employment policy always come from HRD Korea and the relevant authorities, which the app links out to explicitly rather than reproducing.

---

## License

MIT. Fork it, translate it, reuse the 60-chapter content pipeline for your own language pair — the schema, validator, manifest, and content-audit scripts are all in the repo and are the part I'd most want other people to steal.

**Repository:** https://github.com/Mouno6969/EasyEPS
**Live app:** https://easy-eps.vercel.app

If you're preparing for EPS-TOPIK, or you know someone in Bangladesh who is, send them the link. If you're a developer, issues and PRs are very welcome — especially on content authoring for workplace scenarios and on the audio work.

---

## Appendix — short social variant (~155 words)

Use this where the long form won't fit (X, LinkedIn, a Discord intro, a forum signature).

> **EasyEPS — Bangla-first EPS-TOPIK prep, open source.**
>
> The EPS-TOPIK is in Korean. Most prep material assumes you can already read Hangul, and almost none of it explains anything in Bangla. EasyEPS starts from zero: an 8-module Hangul track (jamo, syllable building, stroke writing, speak lab, server-graded checkpoint) that unlocks a 60-chapter curriculum — 1,922 vocabulary items, 1,200 practice questions, and 1,196 exam-style questions including 571 picture questions with original safety-sign and machinery artwork.
>
> Timed mocks at 10 / 20 / 40 questions, spaced repetition, a Bangla AI tutor, certificates with public verification, PWA + offline, and guest mode that needs no account.
>
> React 19 · Tailwind 4 · Express · tRPC · Drizzle · MySQL · Vitest (153 tests) · two content-audit pipelines in CI. MIT licensed.
>
> Live: https://easy-eps.vercel.app
> Code: https://github.com/Mouno6969/EasyEPS
