---
title: Deadlines & Reminders
layout: default
nav_order: 4
description: Quick-reference deadlines and email reminders
---

# Deadlines & Reminders

## Quick reference — typical annual cycle

Ordered roughly by when in the year the deadline falls. All dates are *typical* — see [Conferences](conferences.md) for notes and always confirm the official CFP.

| Month | Venues typically due |
|---|---|
| January | MSR, ICPC, ISSTA, SEAMS, CHASE, EASE, FSE (spring cycle) |
| February | MSR (paper), ISSTA (paper) |
| March | ICSME, ECSA |
| April | ASE, RE, ESEM, SPLC |
| May | ASE (paper) |
| June | FSE (fall cycle), MODELS |
| August | ISSRE, ICSE (abstract, recent cycles) |
| September | ICSE (abstract) |
| October | ICSE (paper), SANER, ICST |
| December | MSR Mining Challenge (abstract mid-Dec, paper late Dec) |

## Email reminders from this repository

This repository contains a ready-to-use reminder system:

- `deadlines.json` — the list of concrete deadlines to watch (edit this with real, dated CFPs).
- `send_reminders.py` — checks the list and emails you when a deadline is **14, 7, or 1 days** away.
- `.github/workflows/reminder.yml` — runs the check automatically **every day at 08:00 UTC** via GitHub Actions.

To switch it on, add three repository secrets (Settings → Secrets and variables → Actions): `SMTP_USER`, `SMTP_PASSWORD` (a Gmail App Password), and `MY_EMAIL`. Full step-by-step instructions are on the [Setup & Automation](setup.md) page.

{: .warning }
> The example entries in `deadlines.json` are placeholders based on typical cycles. Replace them with the exact dated deadlines of the editions you are actually targeting, otherwise reminders will fire for the wrong dates.
