# EasyEPS — Overview Video Recording Guide

A timed shot list for recording a ~90-second product tour of the real running app.
Every label, route and behaviour below was read out of the codebase, so what you see on
screen will match what this document says to point at.

---

## Before you record

**App URL:** the live preview link for this sandbox (port 3000). If it does not load, tell
me and I will restart the server — see "If the preview is down" at the bottom.

| Setting | Use this | Why |
|---|---|---|
| Window / viewport | **1920×1080**, browser maximised | Native 1080p, no upscaling |
| Browser zoom | **100%** | The layout is verified responsive but zoom changes type sizes |
| Theme | Light, and hide bookmarks bar | The design is cream/navy/gold — a dark browser chrome fights it |
| Captions | Turn **off** | Video captions overlay the Bangla UI |
| Browser | Chrome or Edge, **with a Korean voice installed** | Listening items use the Web Speech API. Windows ships `Microsoft Heera`/Korean voices; macOS ships `Yuna`. Without one, the audio button silently does nothing |
| Recording | OS recorder (Win+G / Cmd+Shift+5) or OBS, **with system audio on** | You want the Korean TTS in the video — it is the single best demo moment |
| Cursor | Slow, deliberate movements; pause before each click | Fast clicking reads as nervous on playback |

**Do one full dry run without recording.** The exam timer starts the moment you click, and
TTS audio takes a second to spin up on first use.

---

## The shot list

Total ~90 seconds. Timestamps are cumulative targets, not hard limits.

### 0:00–0:08 — Landing (`/`)

Load the page and let it settle for a beat before moving. Scroll down **slowly** through
the hero into the learning roadmap and study-plan cards.

> **Say:** "EasyEPS — Bangla-first EPS-TOPIK preparation, built for Bangladeshi learners
> going to Korea."

The hero headline is **জীবন ও কাজের জন্য প্রস্তুত হন**. Don't scroll past it fast; it is
the money frame.

### 0:08–0:20 — Hangul Basics (`/basics`)

This is your differentiator, so give it real time. Show the module grid — eight modules
from alphabet through to the checkpoint. Open one module (**অক্ষর গঠন** / consonants is the
most visual) and show a step.

> **Say:** "Most prep material assumes you can already read Hangul. EasyEPS starts below
> that — eight modules of alphabet, syllable building, stroke writing and speaking, ending
> in a graded checkpoint that unlocks the curriculum."

If you can, click into the **write lab** and trace one stroke. Movement on screen here is
worth more than any narration.

### 0:20–0:32 — Curriculum (`/curriculum`)

Three beats, in this order:

1. The full 60-chapter grid.
2. Type into the search box — placeholder reads **অধ্যায়, বিষয় বা Korean title খুঁজুন**.
   Search `work` or `안전` and let the grid filter live.
3. Click a category filter, then reset it.

Point at the **অতিথি মোড** (guest mode) indicator while you're here.

> **Say:** "Sixty chapters of original curriculum — daily life, workplace, culture,
> industrial safety, laws. Searchable and filterable, and fully usable with no account."

### 0:32–0:55 — A lesson (`/lesson/1`) — *the core of the video*

This page has six tabs. Walk them left to right:

| Tab | What to show | Dwell |
|---|---|---|
| **পাঠ পরিচিতি** | Chapter objectives | 2s |
| **শব্দভাণ্ডার** | Vocab cards — Korean, romanisation, Bangla, English, example sentence | 4s |
| **ব্যাকরণ** | Grammar patterns with Bangla explanations | 3s |
| **সংলাপ** | Dialogues — **press the listen button** | 5s |
| **অনুশীলন** | Answer one practice question correctly | 4s |
| **অধ্যায় পরীক্ষা** | The chapter exam with its countdown timer running | 5s |

**The two moments that sell this product:**

- On **সংলাপ**, press the listen control. The label is **শুনতে চাপুন · script লুকানো** —
  the script stays hidden, exactly like the real exam. Two distinct voices speak the
  dialogue. *Let the audio play on camera.* Do not talk over it.
- On **অধ্যায় পরীক্ষা**, the countdown timer is visibly running. Answer one question and
  submit to show the Bangla explanation appearing.

> **Say:** "Every chapter runs the same loop — vocabulary, grammar, dialogue, practice,
> then a timed chapter exam. Listening uses generated Korean audio with the script hidden
> until you submit, so it behaves like the real test. And every answer comes back with an
> explanation in Bangla."

### 0:55–1:12 — Mock test (`/mock-test`)

1. The three configuration cards: **১০ / ২০ / ৪০** questions — ১২, ২৫ and ৫০ minutes.
2. Select **২০** and start.
3. In the runner, show: the countdown timer, the reading/listening section badge, the
   question palette on the right with answered vs. unanswered state.
4. Answer two or three questions so the palette visibly fills in.
5. **Do not submit** — cut away while the timer runs. Submitting ends the demo.

> **Say:** "Three timed mocks, up to forty questions. A smart mode pulls the words you
> actually got wrong and interleaves chapters so you can't pattern-match your way to a
> score."

### 1:12–1:22 — The rest, quick cuts (~2s each)

- `/faq` — learner support
- `/dashboard` — show the sign-in gate honestly rather than hiding it
- `/certificate/TEST-CODE-123` — the public verification page renders an error card for an
  invalid code, which is itself a decent shot ("certificates verify publicly")

> **Say:** "Progress, planner, badges and publicly verifiable certificates when you sign
> in. Guest progress merges into your account instead of being thrown away."

### 1:22–1:30 — End card

Return to `/` and let it sit. Overlay or say:

> "EasyEPS. Open source, MIT licensed. github.com/Mouno6969/EasyEPS"

---

## What to avoid

- **Don't record the AI tutor page.** It needs an `XAI_API_KEY` that this environment does
  not have, so it will show an error. Mention it in narration instead, or skip it.
- **Don't linger on sign-in gates.** One quick honest pass is fine; dwelling looks broken.
- **Don't submit the 40-question mock.** It takes fifty minutes of timer and the score
  screen is better shown from a chapter exam, which you already captured.
- **Don't resize the window mid-recording.** Pick 1920×1080 and stay there.
- **Don't narrate over the Korean audio.** Silence during TTS playback is the point.

---

## After recording

If you want it hosted on GitHub, send me the file and I will attach it to a GitHub Release
on `Mouno6969/EasyEPS` and give you a permanent link.

**Do not commit the video into the repository.** The repo is already at GitHub's 128 MB
warning threshold, and a video in git history inflates every future clone forever. A
Release asset is the right home — it does not touch history and GitHub allows up to 2 GB
per asset.

I can also write you a description, chapter markers for YouTube, and a set of tags once the
video exists.

---

## If the preview is down

The sandbox this runs in resets its filesystem between conversation turns, which removes
`node_modules` and kills the server. If the preview URL refuses to load:

1. Tell me. Reinstalling dependencies takes about 20 seconds and restarting the server
   about 3 seconds.
2. Record promptly after I confirm it is up, in the same sitting.

To restart it yourself if you have shell access:

```bash
cd /home/user/EasyEPS
pnpm install --frozen-lockfile
pnpm rebuild esbuild @tailwindcss/oxide
cp .env.example .env   # guest mode needs no real secrets
pnpm dev               # serves on 0.0.0.0:3000
```

The OAuth error in the startup log is **expected and harmless** — it only affects the
sign-in button, and every page in this shot list works in guest mode without it.
