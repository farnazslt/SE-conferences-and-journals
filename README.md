# SE Conferences and Journals

A curated reference of top **software engineering conferences and journals** — CORE rankings, approximate impact factors, typical submission deadlines, and co-located events — published as a documentation website with the [Just the Docs](https://just-the-docs.github.io/) Jekyll theme.

**Live site:** https://farnazslt.github.io/SE-conferences-and-journals/

## Contents

- `index.md` — home page and top-tier summary
- `conferences.md` — CORE A*/A conferences, typical deadlines, co-located events
- `journals.md` — main SE journals, publishers, approximate impact factors
- `deadlines.md` — quick-reference annual deadline cycle + reminder overview
- `setup.md` — hosting and email-reminder setup guide

## Email deadline reminders

`deadlines.json` + `send_reminders.py` + `.github/workflows/reminder.yml` form a daily GitHub Actions job that emails a reminder 14, 7, and 1 days before each listed deadline. It needs three repository secrets: `SMTP_USER`, `SMTP_PASSWORD` (Gmail App Password), and `MY_EMAIL`. See the Setup page on the live site for full instructions.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

## Disclaimer

Rankings, impact factors, and deadlines are indicative and change yearly. Always verify against the official call for papers or journal page before submitting.

## License

MIT — see `LICENSE`.
