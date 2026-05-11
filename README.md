# Interesting HCI Papers

A daily reading log of human-computer interaction papers from arXiv.

This repository is a small habit engine: each day, an automated workflow finds a recent paper from `cs.HC`, lightly ranks it for HCI relevance, and appends it to [papers.md](papers.md). The goal is not to make a definitive leaderboard. It is to keep a steady trail of papers worth opening, skimming, and thinking about.

## What Gets Logged

Each entry includes:

- the paper title
- arXiv and PDF links
- authors
- publication date
- arXiv categories
- abstract summary

The current focus is HCI and adjacent human-centered computing topics: interaction, interfaces, accessibility, design, evaluation, collaboration, visualization, education, mixed reality, and user experience.

## Latest Log

Read the paper log here:

[papers.md](papers.md)

## How It Works

The daily update is powered by:

- [scripts/add_daily_paper.py](scripts/add_daily_paper.py), which fetches recent arXiv papers and appends one unseen HCI-focused entry
- [.github/workflows/daily-paper.yml](.github/workflows/daily-paper.yml), which runs the script on a schedule and commits the result

The workflow runs every day at `13:00 UTC`, which is `9:00 AM` in New York during daylight saving time. Log dates use `America/New_York`, so entries match the local day rather than the GitHub runner's UTC clock.

## Run Locally

Append a paper:

```bash
python scripts/add_daily_paper.py
```

Preview without writing:

```bash
python scripts/add_daily_paper.py --dry-run
```

Use a different timezone for the log date:

```bash
python scripts/add_daily_paper.py --timezone America/Los_Angeles
```

Search a different category mix:

```bash
python scripts/add_daily_paper.py --category cs.HC --category cs.CY
```
