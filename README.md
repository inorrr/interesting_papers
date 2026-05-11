# Interesting Papers

This repository keeps a daily Markdown log of real human-computer interaction papers from arXiv.

## Files

- `scripts/add_daily_paper.py` fetches recent HCI papers from arXiv, chooses one unseen paper for the day, and appends it to `papers.md`. By default it uses `cs.HC`; pass `--category` more than once to broaden the feed.
- `.github/workflows/daily-paper.yml` runs the script every day and commits the updated log back to the repository.
- `papers.md` is created automatically the first time the script writes an entry.

## Run Locally

```bash
python scripts/add_daily_paper.py
```

Preview the entry without writing:

```bash
python scripts/add_daily_paper.py --dry-run
```

By default, the log date uses `America/New_York`, even when the script runs on GitHub's UTC-hosted runners:

```bash
python scripts/add_daily_paper.py --timezone America/Los_Angeles
```

Pull from a different category set:

```bash
python scripts/add_daily_paper.py --category cs.HC --category cs.CY
```

## GitHub Setup

1. Push these files to a GitHub repository.
2. In the repository settings, make sure GitHub Actions has read and write permissions:
   `Settings -> Actions -> General -> Workflow permissions -> Read and write permissions`.
3. The workflow runs daily at `13:00 UTC`, which is `9:00 AM` in New York during daylight saving time.
4. You can also run it manually from the Actions tab with `Run workflow`.
