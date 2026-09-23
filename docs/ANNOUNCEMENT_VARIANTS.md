# EasyEPS — Platform-Specific Announcement Variants

> Cut-down versions of [`docs/ANNOUNCEMENT.md`](./ANNOUNCEMENT.md) sized for specific channels.
> Bangla long form: [`docs/ANNOUNCEMENT_BN.md`](./ANNOUNCEMENT_BN.md)
> Every figure was counted from `content/lessons/*.json`, `content/manifest.json`, and the test files — see the long form for the audit method.

---

## 1. LinkedIn

**Suggested: post as an article or a long-form status. ~380 words.**

I built an open-source EPS-TOPIK preparation platform for Bangladeshi workers going to Korea. Here's what the problem actually looks like, and what I did about it.

The EPS-TOPIK is the exam that qualifies foreign workers for employment in Korea. It's written in Korean. The official textbook is in Korean. Nearly every free prep resource online assumes you can already read Hangul — and almost nothing explains any of it in Bangla.

So a learner in Rangpur typically faces two walls at once: they can't read the script, and they have no material in their own language. Most quit at the first one.

**EasyEPS** starts below the first wall.

There's an 8-module Hangul track — consonants, vowels, syllable building, batchim, a speak lab with speech recognition, a write lab with stroke-order tracing — ending in a server-graded checkpoint that unlocks the curriculum. That unlock is deliberately not client-side: `basicsProgress.completed` is only written by server grading, a trusted legacy migration, or an admin. Never by whatever the browser reports.

Past that gate: **60 chapters** of original curriculum covering the standard EPS-TOPIK topics. Counted from the lesson files — **1,922 vocabulary items** (each with Korean, romanization, Bangla, English, part of speech, a trilingual example sentence, and a Bangla pronunciation tip), **1,200 practice questions**, and **1,196 exam-style questions** (858 reading / 338 listening). **571** of those carry picture prompts, using 33 original SVG assets — safety signage, machinery, hand tools — matching the real exam's picture-question format.

Three timed mocks (10/20/40 questions), spaced repetition, a Bangla AI tutor on xAI Grok, printable certificates with public verification, PWA + offline study, and a guest mode that needs no account at all. Guest progress merges into your account when you finally sign in.

Two engineering decisions I'd defend in any review:

**Lesson JSON is the public source of truth.** Curriculum reads hit validated JSON files, not the database. `DATABASE_URL` is genuinely optional — without it the whole curriculum still works. Anyone can clone the repo and read 60 chapters of content with zero infrastructure.

**Trust boundaries are explicit.** Client-reported progress is fine for UX. Anything that unlocks content, records an attempt, or issues a certificate is decided server-side. Badges and certificates are awarded from server-graded attempts, never from a client-computed score.

Stack: React 19, Tailwind 4, Express, tRPC 11, Drizzle, MySQL, Zod 4, Vitest (153 tests across 14 suites), GitHub Actions CI running typecheck → tests → content audits → build.

MIT licensed. Live at https://easy-eps.vercel.app, source at https://github.com/Mouno6969/EasyEPS.

One honest caveat: this is an independent, unofficial project. All content is original. It teaches and supports preparation — official schedules, registration and results always come from HRD Korea, which the app links out to rather than reproducing.

If you know someone preparing for EPS-TOPIK, send them the link. If you're a developer, content authoring for workplace scenarios and the audio work are where help would land hardest.

---

## 2. X / Twitter thread

**6 tweets. Character counts below were verified with Twitter's t.co accounting (every URL counts as 23 characters, so the real limit is tighter than it looks).**

**1/**
The EPS-TOPIK is how foreign workers qualify for jobs in Korea. It's in Korean. So is the textbook. Almost every free prep resource assumes you can read Hangul — and none of it is in Bangla.

So I built EasyEPS: open source, MIT, Bangla-first.

easy-eps.vercel.app

**2/**
It starts below the alphabet wall: an 8-module Hangul track — consonants, vowels, syllable building, batchim, a speak lab with speech recognition, a write lab with stroke tracing — ending in a server-graded checkpoint that unlocks the curriculum.

**3/**
That unlock is not client-side. basicsProgress.completed is written only by server grading, a trusted legacy migration, or an admin. Never by whatever the browser reports. There's a documented flag rollout, backfill script, and rollback plan.

**4/**
Past the gate: 60 chapters, all original content.

1,922 vocabulary items
1,200 practice questions
1,196 exam questions (858 reading / 338 listening)
571 picture questions — safety signs, machinery, tools — on 33 original SVGs

Every question has a Bangla explanation.

**5/**
Timed mocks at 10 / 20 / 40 questions. Spaced repetition. Bangla AI tutor on Grok, key server-side only. Certificates with public verification. PWA + offline. Guest mode needs no account — and guest progress merges when you sign in.

Audio: zero pre-recorded files.

**6/**
React 19 · Tailwind 4 · Express · tRPC · Drizzle · MySQL · Zod · Vitest (153 tests). CI: typecheck → tests → content audits → build.

Lesson JSON is the source of truth, so DATABASE_URL is optional — clone it and read all 60 chapters with zero infra.

github.com/Mouno6969/EasyEPS

---

## 3. Reddit

### 3a. r/Korean or r/LanguageLearning

**Title:** I built an open-source EPS-TOPIK prep platform in Bangla — 60 chapters, 1,196 exam questions, and a Hangul track that gates the curriculum

**Body:**

Sharing this partly because it exists, partly because the content pipeline might be reusable for other language pairs.

**Context:** EPS-TOPIK is the exam that qualifies foreign workers for employment in Korea. Bangladesh sends a large number of candidates. The exam and the official textbook are Korean-only, most free prep material assumes existing Hangul literacy, and there's very little that explains anything in Bangla. EasyEPS is an independent, unofficial, MIT-licensed attempt at that gap. Default language Bangla, Korean as the subject, English as support.

**The part I think is interesting** — the curriculum is gated behind a literacy track. Eight modules: welcome, consonants, vowels, syllables, batchim, speak lab (speech recognition), write lab (stroke-order tracing), then a capstone checkpoint. The unlock is server-graded. `basicsProgress.completed` is written only by server-side grading of checkpoint answers, a trusted legacy-user grandfather migration, or an admin — never from client-reported state. There's a `BASICS_GATE_ENABLED` flag that defaults off, an idempotent backfill script that grandfathers anyone with existing progress, and a documented rollback. I didn't want to ship a gate that could lock out learners who'd already earned their progress.

**Content, counted from the lesson JSON rather than from the README:**

- 60 chapters, all validated against a Zod schema
- 1,922 vocabulary items — Korean, romanization, Bangla, English, part of speech, trilingual example sentence, Bangla pronunciation tip
- 1,200 practice questions (522 multiple-choice / 423 fill-blank / 255 matching)
- 1,196 EPS-style questions: 858 reading, 338 listening
- 571 picture questions on 33 original SVGs (safety signage, machinery, hand tools, workplace objects), mirroring the real exam's picture format
- Chapter weighting follows the exam: 24 daily life, 22 workplace, 6 culture, 4 safety, 4 laws

All content is original. No official textbook PDFs are stored or redistributed.

**No audio files at all.** Pronunciation comes from the Web Speech API (`ko-KR`) plus a multi-speaker dialogue engine. Where the browser has two or more Korean voices it picks a gendered pair; with one voice it reuses it at clearly different pitches (0.75 / 1.3) with a 420ms turn gap. Speaker labels are never read aloud. All 338 listening passages are normalized to a canonical two-speaker format and there's a Python audit that fails the build if they drift.

**Mocks:** 10 questions / 12 min, 20 / 25 min, 40 / 50 min. A "smart" mode pulls due items from the SRS queue plus recently-missed items, interleaves chapters so you don't get five from one chapter in a row, and uses Fisher–Yates with an answer key rebalanced across A–D. Listening passages stay hidden until you submit.

**Architecture notes that might be useful to others:**

Lesson JSON is the public source of truth — curriculum reads hit validated files, not the DB. `DATABASE_URL` is genuinely optional; without it the full curriculum works and protected procedures return a clear availability error instead of crashing. Trust boundaries are explicit: client-reported step progress is allowed for UX, but anything that unlocks content, records an attempt, or issues a certificate is decided server-side.

Stack: React 19, Tailwind 4, Vite 7, Express, tRPC 11, Drizzle, MySQL, Zod 4, Vitest (153 tests / 14 suites). CI: typecheck → tests → two content audits → production build.

Live: https://easy-eps.vercel.app · Source: https://github.com/Mouno6969/EasyEPS

Happy to answer questions about the content pipeline — the schema, validator, manifest and audit scripts are the part I'd most want feedback on, since they're what makes 60 chapters maintainable by one person.

### 3b. r/bangladesh (Bangla, casual)

**Title:** কোরিয়া যাবার জন্য EPS-TOPIK প্রস্তুতি নিচ্ছেন? বাংলায় একটা ফ্রি ওপেন-সোর্স প্ল্যাটফর্ম বানিয়েছি

**Body:**

EPS-TOPIK পরীক্ষাটা কোরীয় ভাষায় হয়, অফিসিয়াল বইও কোরীয় ভাষায়। অনলাইনে যা কিছু ফ্রি ম্যাটেরিয়াল আছে তার বেশিরভাগই ধরে নেয় আপনি হাঙ্গুল পড়তে পারেন — আর বাংলায় ব্যাখ্যা করা ম্যাটেরিয়াল বলতে গেলে নেই।

তাই **EasyEPS** বানিয়েছি। ডিফল্ট ভাষা বাংলা, কোরীয়টা শেখার বিষয়, ইংরেজি সহায়ক ভাষা হিসেবে। সম্পূর্ণ ফ্রি ও ওপেন সোর্স (MIT)।

**যা আছে:**

- **হাঙ্গুল শেখার আলাদা ট্র্যাক** (৮টি মডিউল) — ব্যঞ্জনবর্ণ, স্বরবর্ণ, সিলেবল তৈরি, 받িম, শুনে বলা, স্ট্রোক ধরে লেখা, শেষে একটা চেকপয়েন্ট পরীক্ষা। এটা পাস না করলে মূল কোর্স খোলে না — কারণ অধ্যায় ১ খুলেই অনেকে আটকে যান যেহেতু কোরীয় পড়তেই পারেন না।
- **৬০ অধ্যায়** — ১,৯২২টি শব্দ (প্রতিটিতে কোরীয়, উচ্চারণ, বাংলা, ইংরেজি, উদাহরণ বাক্য), ১,২০০ অনুশীলন প্রশ্ন, ১,১৯৬টি পরীক্ষার ধরনের প্রশ্ন (৮৫৮ reading / ৩৩৮ listening)।
- **৫৭১টি ছবিওয়ালা প্রশ্ন** — সেফটি সাইন, মেশিন, যন্ত্রপাতি। আসল পরীক্ষায়ও এই ধরনের প্রশ্ন আসে।
- **মক টেস্ট** — ১০ / ২০ / ৪০ প্রশ্নের, টাইমারসহ। জমা দেওয়ার পর প্রতিটি প্রশ্নের বাংলা ব্যাখ্যা।
- **বাংলা AI টিউটর**, সনদ, প্ল্যানার, অফলাইনে পড়ার সুবিধা।
- **অ্যাকাউন্ট ছাড়াই** পড়া ও মক টেস্ট দেওয়া যায়। পরে অ্যাকাউন্ট খুললে আগের অগ্রগতি মার্জ হয়ে যায়।

লিংক: https://easy-eps.vercel.app
কোড: https://github.com/Mouno6969/EasyEPS

একটা কথা পরিষ্কার করে বলি — এটা সম্পূর্ণ ব্যক্তিগত ও অনানুষ্ঠানিক প্রকল্প, HRD Korea বা সরকারের সাথে সম্পর্কিত নয়। পরীক্ষার সময়সূচি, রেজিস্ট্রেশন, ফলাফল এসবের সরকারি সূত্রই চূড়ান্ত; অ্যাপে সেই লিংক দেওয়া আছে, নিজেরা এসব তথ্য ছাপা হয় না। সব পড়াশোনার কনটেন্ট নিজের লেখা, কোনো বইয়ের কপি নয়।

বাগ পেলে বা কোথাও আটকে গেলে জানাবেন — ঠিক করে দেব। আর কেউ যদি কোরিয়া যাবার প্রস্তুতি নিচ্ছেন, একটু জানালে ভালো হয় কোন অংশটা আরও দরকারি।

---

## 4. Product Hunt

**Name:** EasyEPS

**Tagline (60 chars max):**
Bangla-first EPS-TOPIK prep: Hangul to 60-chapter mock exams

**Description (260 chars max):**
Open-source Korean EPS-TOPIK prep for Bangladeshi workers. An 8-module Hangul track gates 60 chapters — 1,922 vocab items, 1,196 exam questions, 571 picture items. Timed mocks, spaced repetition, Bangla AI tutor, offline PWA. No account needed. MIT.

**Topics:** Education · Language Learning · Open Source · Web App · Design Tools

**First maker comment:**

Hi PH 👋

I built EasyEPS because of a specific dead end. The EPS-TOPIK is how workers from Bangladesh qualify for jobs in Korea. The exam is in Korean, the textbook is in Korean, and nearly every free prep resource assumes you can already read Hangul. Nothing explains any of it in Bangla. So people hit two walls at once and most stop at the first one.

The app starts below that first wall. There's a Hangul track — jamo, syllable building, stroke writing, a speak lab, a checkpoint exam — and it genuinely gates the curriculum. That gate is server-graded, not client-side, and it ships behind a flag with a backfill script so existing learners are grandfathered rather than locked out.

Behind it: 60 chapters of original content. 1,922 vocabulary items, 1,200 practice questions, 1,196 exam questions (858 reading / 338 listening), 571 of them picture-based using 33 original SVGs — safety signs, machinery, tools — because the real exam asks that way.

Some things I'd point at specifically:

- **No audio files anywhere.** All pronunciation is generated via the Web Speech API with a multi-speaker dialogue engine. Two Korean voices → gendered pair. One voice → distinct pitches plus a 420ms turn gap. Labels are never read aloud, like real exam audio.
- **Guest mode is complete, not crippled.** Study, practice, take full mocks, all with local progress — no account. Sign in later and it merges.
- **Lesson JSON is the source of truth,** not the database. `DATABASE_URL` is optional; clone the repo and the whole curriculum works with zero infrastructure.
- **Credentials are server-decided.** Badges and certificates come from server-graded attempts. The client score is never trusted for anything that grants something.

React 19, Tailwind 4, Express, tRPC, Drizzle, MySQL, Zod, Vitest (153 tests), GitHub Actions CI. MIT licensed.

One caveat I want to be upfront about: this is independent and unofficial. All content is original — no textbook PDFs stored or redistributed — and official schedules, registration and results always come from HRD Korea, which the app links to rather than reproducing.

Would love feedback on the Hangul track especially. That's the part with the least precedent to copy from.

---

## 5. Hacker News (Show HN)

**Title:** Show HN: EasyEPS – Open-source Bangla-first EPS-TOPIK prep with a server-gated Hangul track

**Body:**

EasyEPS is an MIT-licensed platform for Bangladeshi workers preparing for the EPS-TOPIK, the exam that qualifies foreign workers for employment in Korea. Bangla is the default language; Korean is the subject; English is support.

https://easy-eps.vercel.app · https://github.com/Mouno6969/EasyEPS

The reason it exists: the exam and the official textbook are Korean-only, and most free prep material assumes existing Hangul literacy. Learners hit a script barrier and a language barrier simultaneously.

**The interesting engineering problem was the gate.** The curriculum sits behind an 8-module Hangul track ending in a capstone checkpoint. The unlock has to be trustworthy — a learner who passes should be able to reach chapter 1, and one who hasn't shouldn't be able to fake it from devtools. So `basicsProgress.completed` is written only by server-side grading of checkpoint answers, a legacy-user grandfather migration, or an admin. Client-reported module step progress is accepted freely for UX; the unlock decision is not.

Shipping a gate onto an existing user base is the harder half. It goes out behind `BASICS_GATE_ENABLED` (off by default), with an idempotent backfill that grandfathers anyone who has any existing progress row or attempt — including mock-test-only users — plus a documented rollback. There's a runbook in `docs/BASICS_RUNBOOK.md` covering the staging sequence and the smoke tests for each flag state.

**Content as data, with CI-enforced invariants.** 60 chapters live as JSON validated by a Zod schema on load. Per chapter: 30–35 vocabulary items, 4–5 grammar patterns, 3 dialogues, exactly 20 practice questions, 19–20 EPS questions. Corpus totals 1,922 / 1,200 / 1,196 (858 reading, 338 listening), with 571 picture questions on 33 original SVGs.

Because content is data, drift is the main failure mode, and I've been bitten by it twice:

- A bulk edit appended image questions to every chapter without re-running the manifest sync script, so the resumability manifest claimed 971 EPS questions when the files held 1,196. The audit that CI runs now verifies manifest counts against the lesson files and fails on mismatch.
- 56 listening passages still used a legacy single-line `남: … / 여: …` format that the multi-speaker TTS parser reads incorrectly. The repo's own normalizer fixed the labels but left the `/` separator dangling, so its audit still failed. Both are fixed and the generators that emitted the legacy format were corrected at the source.

**Lesson JSON is the public source of truth,** not the database. Curriculum reads hit validated files. `DATABASE_URL` is genuinely optional — without it the full curriculum, lessons and exams work, and protected procedures return a clear availability error instead of crashing. That makes the repo clone-and-read with zero infrastructure.

**No audio files exist.** Pronunciation is generated via the Web Speech API (`ko-KR`) with a dialogue engine that assigns distinct voices per speaker: a gendered pair when the browser exposes two or more Korean voices, otherwise the same voice at pitches 0.75 / 1.3 with a 420ms turn gap. Labels are stripped so they're never read aloud.

Stack: React 19, Tailwind 4, Vite 7, Express, tRPC 11, Drizzle, MySQL, Zod 4, Vitest (153 tests across 14 suites). CI runs typecheck → tests → two content audits → production build on every push and PR.

Caveat: independent and unofficial. All content is original, no textbook PDFs are stored or redistributed, and official schedules, registration and results are linked out to HRD Korea rather than reproduced.

Happy to answer questions about gating a feature onto existing users, or about maintaining 60 chapters of content as a solo author — the schema, validator, manifest and audit scripts are what make that tractable.

---

## 6. Discord / community intro (~120 words)

**EasyEPS** — free, open-source EPS-TOPIK prep for Bangladeshi workers going to Korea. Bangla-first UI.

It starts with an 8-module Hangul track (letters, syllables, stroke writing, speaking, checkpoint exam) that unlocks 60 chapters of original content: 1,922 vocab items, 1,200 practice questions, 1,196 exam questions including 571 picture-based ones. Timed mocks at 10/20/40 questions, spaced repetition, Bangla AI tutor, certificates, offline PWA. Works fully without an account.

React 19 · tRPC · Drizzle · MySQL · Vitest. MIT.

Live: https://easy-eps.vercel.app
Code: https://github.com/Mouno6969/EasyEPS

Unofficial and independent — official exam info always comes from HRD Korea. Feedback welcome, especially on the Hangul track.

---

## Usage notes

- **Verify the live URL before posting.** `https://easy-eps.vercel.app` is the `homepage` field on the GitHub repo, but the Vercel project's deployment state should be confirmed — a dead link in a launch post is the worst possible first impression.
- **Don't claim official status anywhere.** Every variant carries the unofficial/independent caveat. Keep it. The app itself links out to HRD Korea rather than reproducing schedules or results, and the posts should stay consistent with that.
- **Numbers reflect the corpus as reconciled with the manifest.** If content is added, re-run `python3 scripts/update-manifest-eps.py` and recount before reusing these posts. `scripts/audit_runtime_contract.py` will fail CI if the manifest drifts.
- **X thread character counts** were checked at authoring time; re-check after any edit, since URLs count as 23 characters regardless of length.
