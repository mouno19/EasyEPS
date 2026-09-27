# Contributing to EasyEPS

Thank you for helping make EPS-TOPIK preparation more accessible to Bangladeshi learners.

## Good first contributions

- Report inaccurate Korean, Bangla, or English content
- Improve explanations, translations, accessibility, or mobile usability
- Add tests and documentation
- Fix reproducible bugs with a focused pull request

## Before opening a pull request

1. Explain the learner or maintenance problem being solved.
2. Keep changes focused and avoid regenerating existing lesson files.
3. Validate lesson changes against the content schema and update the manifest when needed.
4. Run `pnpm check`, `pnpm test`, `pnpm build`, and `pnpm content:audit` when applicable.
5. Do not commit credentials, private learner data, generated secrets, or production configuration.

For security vulnerabilities, follow [`SECURITY.md`](SECURITY.md) instead of opening a public issue with exploit details.
