#!/usr/bin/env python3
"""Append one real CS paper from arXiv to a Markdown reading log."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import pathlib
import re
import sys
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


ARXIV_API_URL = "https://export.arxiv.org/api/query"
DEFAULT_LOG_PATH = pathlib.Path("papers.md")
DEFAULT_CATEGORIES = ("cs.HC",)
DEFAULT_TIMEZONE = "America/New_York"
HCI_KEYWORDS = (
    "accessibility",
    "collaboration",
    "creativity",
    "design",
    "education",
    "evaluation",
    "experience",
    "human",
    "interaction",
    "interface",
    "mixed reality",
    "participatory",
    "social",
    "usability",
    "user",
    "visualization",
    "vr",
    "xr",
)
ATOM = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV = {"arxiv": "http://arxiv.org/schemas/atom"}


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def arxiv_id_from_url(url: str) -> str:
    return url.rstrip("/").rsplit("/", 1)[-1]


def read_seen_ids(log_path: pathlib.Path) -> set[str]:
    if not log_path.exists():
        return set()

    ids = set()
    for match in re.finditer(r"arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+(?:v[0-9]+)?)", log_path.read_text()):
        ids.add(match.group(1))
        ids.add(match.group(1).split("v", 1)[0])
    return ids


def build_query(categories: list[str]) -> str:
    return " OR ".join(f"cat:{category}" for category in categories)


def fetch_recent_papers(categories: list[str], max_results: int) -> list[dict[str, object]]:
    params = {
        "search_query": build_query(categories),
        "start": "0",
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API_URL}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "interesting-papers-bot/1.0 (daily markdown log)"},
    )

    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = response.read()
            break
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt < 2:
                time.sleep(10 * (attempt + 1))
                continue
            raise RuntimeError(f"Could not fetch arXiv papers: {exc}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Could not fetch arXiv papers: {exc}") from exc
    else:
        raise RuntimeError("Could not fetch arXiv papers.")

    root = ET.fromstring(payload)
    papers = []
    for entry in root.findall("atom:entry", ATOM):
        abs_url = entry.findtext("atom:id", default="", namespaces=ATOM)
        arxiv_id = arxiv_id_from_url(abs_url)
        versionless_id = arxiv_id.split("v", 1)[0]
        title = normalize_whitespace(entry.findtext("atom:title", default="", namespaces=ATOM))
        summary = normalize_whitespace(entry.findtext("atom:summary", default="", namespaces=ATOM))
        published = entry.findtext("atom:published", default="", namespaces=ATOM)
        updated = entry.findtext("atom:updated", default="", namespaces=ATOM)
        authors = [
            normalize_whitespace(author.findtext("atom:name", default="", namespaces=ATOM))
            for author in entry.findall("atom:author", ATOM)
        ]
        categories_found = [
            category.attrib.get("term", "")
            for category in entry.findall("atom:category", ATOM)
            if category.attrib.get("term", "").startswith("cs.")
        ]
        primary_category = entry.find("arxiv:primary_category", ARXIV)
        primary = primary_category.attrib.get("term", "") if primary_category is not None else ""
        pdf_url = ""
        for link in entry.findall("atom:link", ATOM):
            if link.attrib.get("title") == "pdf":
                pdf_url = link.attrib.get("href", "")
                break

        papers.append(
            {
                "id": arxiv_id,
                "versionless_id": versionless_id,
                "title": title,
                "summary": summary,
                "published": published,
                "updated": updated,
                "authors": [author for author in authors if author],
                "categories": categories_found,
                "primary_category": primary,
                "abs_url": abs_url,
                "pdf_url": pdf_url or f"https://arxiv.org/pdf/{arxiv_id}",
            }
        )
    return papers


def choose_daily_paper(papers: list[dict[str, object]], seen_ids: set[str], run_date: dt.date) -> dict[str, object]:
    unseen = [
        paper
        for paper in papers
        if paper["id"] not in seen_ids and paper["versionless_id"] not in seen_ids
    ]
    if not unseen:
        raise RuntimeError("No unseen papers found in the fetched arXiv results.")

    scored = sorted(
        unseen,
        key=lambda paper: (
            hci_relevance_score(paper),
            str(paper["published"]),
            stable_daily_tiebreaker(paper, run_date),
        ),
        reverse=True,
    )
    return scored[0]


def hci_relevance_score(paper: dict[str, object]) -> int:
    text = f"{paper['title']} {paper['summary']}".lower()
    score = 0
    if "cs.HC" in paper["categories"]:
        score += 10
    for keyword in HCI_KEYWORDS:
        if keyword in text:
            score += 1
    return score


def stable_daily_tiebreaker(paper: dict[str, object], run_date: dt.date) -> str:
    value = f"{run_date.isoformat()}:{paper['id']}:{paper['title']}"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def local_run_date(timezone_name: str) -> dt.date:
    try:
        timezone = ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as exc:
        raise argparse.ArgumentTypeError(f"Unknown timezone: {timezone_name}") from exc
    return dt.datetime.now(timezone).date()


def format_entry(paper: dict[str, object], run_date: dt.date) -> str:
    authors = paper["authors"]
    author_text = ", ".join(authors[:6])
    if len(authors) > 6:
        author_text += ", et al."

    categories = paper["categories"]
    category_text = ", ".join(categories[:8]) if categories else str(paper["primary_category"])
    summary = textwrap.fill(str(paper["summary"]), width=88)

    return f"""### {run_date.isoformat()} - {paper["title"]}

- **arXiv:** [{paper["id"]}]({paper["abs_url"]})
- **PDF:** [{paper["id"]}.pdf]({paper["pdf_url"]})
- **Authors:** {markdown_escape(author_text)}
- **Published:** {str(paper["published"])[:10]}
- **Categories:** {markdown_escape(category_text)}
- **Summary:** {summary}

"""


def ensure_log_header(log_path: pathlib.Path) -> None:
    if log_path.exists() and log_path.read_text().strip():
        return

    log_path.write_text(
        "# Interesting CS Papers\n\n"
        "A daily log of computer science papers pulled from arXiv.\n\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", type=pathlib.Path, default=DEFAULT_LOG_PATH)
    parser.add_argument("--max-results", type=int, default=75)
    parser.add_argument(
        "--timezone",
        default=DEFAULT_TIMEZONE,
        help=f"Timezone used for the default log date. Defaults to {DEFAULT_TIMEZONE}.",
    )
    parser.add_argument(
        "--category",
        action="append",
        dest="categories",
        help="arXiv CS category to search. Repeat to add more. Defaults to cs.HC for HCI papers.",
    )
    parser.add_argument(
        "--date",
        type=dt.date.fromisoformat,
        default=None,
        help="Date used to deterministically choose a paper, in YYYY-MM-DD format.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print the selected entry without writing.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    categories = args.categories or list(DEFAULT_CATEGORIES)
    run_date = args.date or local_run_date(args.timezone)

    papers = fetch_recent_papers(categories, args.max_results)
    seen_ids = read_seen_ids(args.log)
    paper = choose_daily_paper(papers, seen_ids, run_date)
    entry = format_entry(paper, run_date)

    if args.dry_run:
        print(entry)
        return 0

    ensure_log_header(args.log)
    with args.log.open("a", encoding="utf-8") as handle:
        handle.write(entry)

    print(f"Added arXiv paper {paper['id']}: {paper['title']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(1)
