# EasyEPS

[![CI](https://github.com/mouno19/EasyEPS/actions/workflows/ci.yml/badge.svg)](https://github.com/mouno19/EasyEPS/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**EasyEPS is a Bangla-first EPS-TOPIK learning app for Bangladeshi learners preparing to live and work in Korea.** Korean and English are available as supporting languages.

[**Try the live demo →**](https://easy-eps.vercel.app)

## Why EasyEPS

Many aspiring migrant workers need Korean exam preparation that is understandable in Bangla, practical on a phone, and aligned with the EPS-TOPIK format. EasyEPS brings the core study journey into one open-source application:

- **60 chapters** of original curriculum covering vocabulary, grammar, dialogues, practice, and EPS-style exams
- **Enriched chapter content** with roughly 30–35 vocabulary items, 20 practice questions, and reading/listening questions
- **Bangla-first learning experience** with Korean and English support
- **Guest mode** so learners can browse, study, practice, and take mock tests without creating an account
- **Signed-in learning tools** including durable progress, planner, badges, certificates, and an AI tutor
- **Accessible exam practice** through chapter exams and timed 20/40-question mock tests

## Project status

The core 60-chapter curriculum and learning flows are implemented. The project is actively maintained and welcomes feedback from EPS-TOPIK learners, Korean teachers, accessibility advocates, and developers. See the [roadmap and implementation notes](IMPLEMENTATION_PLAN.md) for the product direction.

## Quick start

```bash
# Requirements: Node 22+, pnpm 10+
pnpm install
cp .env.example .env   # fill in values (see below)

# Dev server (API + Vite)
pnpm dev

# Quality gates
pnpm check             # TypeScript
pnpm test              # Vitest
pnpm build             # production client + server bundle
python3 scripts/audit_runtime_contract.py
```

Open [http://localhost:3000](http://localhost:3000) (port may vary if 3000 is taken).

## Environment variables

See [`.env.example`](.env.example). Minimum for local curriculum browsing:

| Variable | Required for | Notes |
|---|---|---|
| `DATABASE_URL` | Signed-in progress / planner / certs | MySQL connection string. Public curriculum works without it. |
| `JWT_SECRET` | Auth sessions | Long random string; never commit it. |
| `VITE_APP_ID` | Login button | Manus app id |
| `VITE_OAUTH_PORTAL_URL` | Login button | Manus OAuth portal |
| `OAUTH_SERVER_URL` | OAuth callback | Manus OAuth API base |
| `OWNER_OPEN_ID` | First admin | Manus openId promoted to `admin` on first login |
| `XAI_API_KEY` | AI tutor | xAI key; server-side only |
| `XAI_BASE_URL` | AI tutor (optional) | Default `https://api.x.ai/v1` |
| `XAI_MODEL` | AI tutor (optional) | Default `grok-4.5` |
| `BUILT_IN_FORGE_API_URL` / `BUILT_IN_FORGE_API_KEY` | Storage / legacy | Optional Manus Forge helpers |

### AI tutor

The AI tutor calls the model from the server. Credentials are never placed in `VITE_*` client variables. Without AI or OAuth configuration, guests can still use the public curriculum and exams.

## Main routes

| Route | Access |
|---|---|
| `/` | Landing |
| `/curriculum` | 60-chapter catalog |
| `/lesson/:chapter` | Lesson player (1–60) |
| `/mock-test` | Timed 20/40-question mock |
| `/dashboard`, `/planner`, `/profile`, `/tutor` | Signed-in learning tools |
| `/certificate/:code` | Public certificate verification |
| `/admin` | Admin role only |

## Content and architecture

- Canonical lessons: `content/lessons/lesson-01.json` … `lesson-60.json`
- Lesson schema: [`content/SCHEMA.md`](content/SCHEMA.md)
- Content manifest: [`content/manifest.json`](content/manifest.json)
- Chapter titles: [`shared/chapters.ts`](shared/chapters.ts)
- Stack: React 19, Tailwind 4, Express, tRPC, Drizzle, MySQL, Zod, and Vitest

Lesson JSON is the public source of truth and is validated with Zod on load. Progress, attempts, planner records, badges, and certificates are stored in MySQL when configured. Exam answers are graded server-side for authenticated records; client scores are not trusted for badges or certificates.

Do not regenerate existing lessons. Author only missing chapters, validate against the schema, update the manifest, and push.

## Scripts

| Command | Purpose |
|---|---|
| `pnpm dev` | Development server |
| `pnpm build` / `pnpm start` | Production build and run |
| `pnpm check` | TypeScript checking |
| `pnpm test` | Vitest test suite |
| `pnpm content:audit` | Curriculum/runtime audits |
| `pnpm db:push` | Generate and migrate Drizzle schema |
| `pnpm db:seed` | Idempotently seed lesson content |
| `pnpm format` | Prettier |

## Contributing and security

Suggestions, content corrections, translations, accessibility improvements, and code contributions are welcome. Please read the repository guidance and open an issue before large changes. For security concerns, follow [`SECURITY.md`](SECURITY.md) and do not disclose sensitive vulnerabilities publicly.

## License

EasyEPS is released under the [MIT License](LICENSE).
