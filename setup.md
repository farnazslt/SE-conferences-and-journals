---
title: Setup & Automation
layout: default
nav_order: 5
description: How this site is hosted and how email reminders work
---

# Setup & Automation

## Hosting — GitHub Pages (public repository)

This site is built with Jekyll and the *Just the Docs* theme, and hosted for free with GitHub Pages:

1. Repository **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Every push to `main` triggers `.github/workflows/pages.yml`, which builds the site and deploys it.
3. The live site is: <https://farnazslt.github.io/SE-conferences-and-journals/>
4. `_config.yml` sets `url: "https://farnazslt.github.io"` and `baseurl: "/SE-conferences-and-journals"` so all links and assets resolve correctly under the repository path.

> **Private repositories:** standard GitHub Pages on a free plan requires a public repository. If you later want the *source* private, keep a public mirror for Pages, or deploy the same Jekyll build from a private repo via Netlify or Vercel (both free for personal sites). Repository *secrets* (below) are private even in a public repository — nobody can read them.

## Email reminders — step by step

1. **Edit `deadlines.json`** in the repository root with the conferences and exact dates you care about.
2. **Create a Gmail App Password**: Google Account → Security → 2-Step Verification → App passwords. (Your normal Gmail password will not work.)
3. **Add repository secrets** (Settings → Secrets and variables → Actions → New repository secret):
   - `SMTP_USER` — your Gmail address
   - `SMTP_PASSWORD` — the App Password from step 2
   - `MY_EMAIL` — the address reminders should go to (can be the same Gmail)
4. **Test it**: Actions tab → *Daily Conference Deadline Reminder* → Run workflow. If a deadline in `deadlines.json` is exactly 14, 7, or 1 days away, an email is sent; otherwise the run succeeds silently.
5. The workflow then runs automatically every day at 08:00 UTC.

## Updating the site

Edit any `.md` file (via the pencil icon on GitHub, or locally) and push to `main`. The site rebuilds in 1–2 minutes. To preview locally:

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000/SE-conferences-and-journals/
```
