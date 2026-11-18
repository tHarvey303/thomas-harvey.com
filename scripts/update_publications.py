#!/usr/bin/env python3
"""Rebuild _data/publications.json from public sources. No API keys needed.

Sources, merged into one list:
  1. arXiv   - every astro-ph paper with a matching author name: title, full
               author list, abstract, and the journal DOI once the authors add it.
  2. ORCID   - the works on the ORCID record: journal names, DOIs, dates.
  3. Crossref - author lists and journal names for DOIs arXiv does not cover.
  4. _data/publications_extra.yml - hand-written additions and exclusions.

Run by hand (`python3 scripts/update_publications.py`) or let the
"Update publications" GitHub Action run it every week. Python 3.8+, standard
library only.
"""
import difflib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ORCID = "0000-0002-4130-636X"
ARXIV_QUERIES = ["au:Harvey_Thomas", "au:Harvey_Tom"]      # results are filtered to astro-ph and to NAME
NAME = re.compile(r"^(thomas|tom|t\.?)\s+harvey$", re.I)   # exact author names accepted as "me"
SINCE = 2022                                               # ignore namesakes' older papers
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_data" / "publications.json"
EXTRA = ROOT / "_data" / "publications_extra.yml"
UA = "thomas-harvey.com publication updater (https://github.com/tHarvey303/thomas-harvey.com)"

JOURNALS = {
    "monthly notices of the royal astronomical society": "MNRAS",
    "royal astronomical society. monthly notices": "MNRAS",
    "the astrophysical journal": "ApJ",
    "astrophysical journal": "ApJ",
    "the astrophysical journal letters": "ApJL",
    "astronomy & astrophysics": "A&A",
    "astronomy and astrophysics": "A&A",
    "astronomy &amp; astrophysics": "A&A",
    "journal of open source software": "JOSS",
    "the astrophysical journal supplement series": "ApJS",
    "the open journal of astrophysics": "OJAp",
}


def fetch(url, accept=None, tries=3):
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(3 * (attempt + 1))
        except Exception:
            time.sleep(3 * (attempt + 1))
    return None


def clean(text):
    """Plain text with TeX maths left in place for MathJax."""
    text = html.unescape(html.unescape(text or ""))
    text = re.sub(r"</?[A-Za-z][A-Za-z0-9:]*( [^<>]*)?>", "", text)   # tags only, so "6.5 < z < 13" survives
    return re.sub(r"\s+", " ", text).strip()


def key(title):
    t = re.sub(r"\$|\\[a-zA-Z]+|[{}]", "", title.lower())
    return re.sub(r"[^a-z0-9]", "", t.replace("modelling", "modeling").replace("ionis", "ioniz"))


def same_title(a, b):
    ka, kb = key(a), key(b)
    if not ka or not kb:
        return False
    if ka[:40] == kb[:40]:
        return True
    return difflib.SequenceMatcher(None, ka, kb).ratio() > 0.86


def short_journal(name):
    return JOURNALS.get((name or "").strip().lower(), (name or "").strip())


def authors_summary(names):
    """names: list of 'Given Family'. Returns display string, my position, count."""
    position = next((i + 1 for i, n in enumerate(names) if NAME.match(n.strip())), 0)

    def fmt(n):
        parts = n.split()
        k = len(parts) - 1
        while k > 1 and parts[k - 1].lower() in ("le", "de", "del", "della", "van", "von", "der", "den", "da", "di", "la", "du"):
            k -= 1   # keep "Le Conte", "van der Wel" together
        return " ".join(parts[k:]) + " " + "".join(p[0] + "." for p in parts[:k])
    shown = [fmt(n) for n in names[:3]]
    if position > 3:
        shown = [fmt(n) for n in names[:2]] + ["… " + fmt(names[position - 1])]
    text = ", ".join(shown).replace(", … ", " … ")
    if len(names) > 3:
        text += ", et al."
    return text, position, len(names)


ARXIV_NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}


def arxiv_entries(params):
    """One arXiv API call; returns the papers on which NAME is an author."""
    ns = ARXIV_NS
    raw = fetch("https://export.arxiv.org/api/query?" + params + "&max_results=300")
    time.sleep(3)   # arXiv asks for one request every three seconds
    if not raw:
        return None
    papers = []
    for e in ET.fromstring(raw).findall("a:entry", ns):
        if e.find("a:published", ns) is None:
            continue
        names = [a.find("a:name", ns).text.strip() for a in e.findall("a:author", ns)]
        published = e.find("a:published", ns).text
        primary = e.find("x:primary_category", ns)
        if not any(NAME.match(n) for n in names) or int(published[:4]) < SINCE:
            continue
        if primary is None or not primary.get("term", "").startswith("astro-ph"):
            continue
        doi = e.find("x:doi", ns)
        papers.append({
            "arxiv": re.sub(r"v\d+$", "", e.find("a:id", ns).text.split("/abs/")[-1]),
            "title": clean(e.find("a:title", ns).text),
            "abstract": clean(e.find("a:summary", ns).text),
            "names": names,
            "year": int(published[:4]), "month": int(published[5:7]),
            "doi": doi.text.strip().lower() if doi is not None else None,
            "journal": "",
        })
    return papers


def arxiv_papers():
    found = {}
    for query in ARXIV_QUERIES:
        got = arxiv_entries("search_query=%s&sortBy=submittedDate&sortOrder=descending" % urllib.parse.quote(query))
        if got is None:
            sys.exit("Could not reach arXiv; leaving %s unchanged." % OUT.name)
        for p in got:
            found.setdefault(p["arxiv"], p)
    return list(found.values())


def arxiv_by_id(ids):
    return arxiv_entries("id_list=" + ",".join(ids)) or [] if ids else []


def orcid_works():
    raw = fetch("https://pub.orcid.org/v3.0/%s/works" % ORCID, accept="application/json")
    if not raw:
        print("Could not reach ORCID; using arXiv only.", file=sys.stderr)
        return []
    works = []
    for group in json.loads(raw).get("group", []):
        doi = arxiv = None
        for s in group["work-summary"]:
            for e in (s.get("external-ids") or {}).get("external-id", []):
                kind, value = e["external-id-type"], e["external-id-value"].strip()
                if kind == "doi" and value.lower().startswith("10.48550/arxiv."):
                    arxiv = arxiv or value[len("10.48550/arxiv."):]
                elif kind == "doi":
                    doi = doi or value.lower()
                elif kind == "arxiv":
                    arxiv = arxiv or value.replace("arXiv:", "")
        s = group["work-summary"][0]
        date = s.get("publication-date") or {}
        works.append({
            "title": clean(s["title"]["title"]["value"]),
            "journal": clean((s.get("journal-title") or {}).get("value", "")),
            "year": int((date.get("year") or {}).get("value") or 0),
            "month": int((date.get("month") or {}).get("value") or 0),
            "doi": doi, "arxiv": arxiv,
        })
    return works


def crossref(doi):
    raw = fetch("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if not raw:
        return None
    msg = json.loads(raw).get("message", {})
    names = [("%s %s" % (a.get("given", ""), a.get("family", ""))).strip() for a in msg.get("author", []) if a.get("family")]
    parts = (msg.get("published") or {}).get("date-parts", [[0]])[0]
    return {"names": names, "journal": clean((msg.get("container-title") or [""])[0]),
            "abstract": clean(re.sub(r"^\s*abstract\s*", "", clean(msg.get("abstract", "")), flags=re.I)),
            "year": parts[0] if parts else 0, "month": parts[1] if len(parts) > 1 else 0}


def read_extra():
    """A tiny reader for publications_extra.yml: a list of flat key: value maps."""
    if not EXTRA.exists():
        return []
    items, cur = [], None
    for line in EXTRA.read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^(-\s+|\s+)([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        if m.group(1).startswith("-"):
            cur = {}
            items.append(cur)
        if cur is None:
            continue
        value = m.group(3).strip()
        if len(value) > 1 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        cur[m.group(2)] = int(value) if value.isdigit() else value
    return items


def main():
    papers = arxiv_papers()
    extra = read_extra()

    # Papers listed under another form of the name ("T. Harvey") are found by arXiv id instead.
    works = orcid_works()
    have = {p["arxiv"] for p in papers}
    wanted = {w["arxiv"] for w in works if w["arxiv"]} | {str(e["arxiv"]) for e in extra if e.get("arxiv") and not e.get("exclude")}
    papers += arxiv_by_id(sorted(wanted - have))

    # Fold the ORCID record in: it knows where and when each paper was published.
    for w in works:
        match = None
        for p in papers:
            if (w["arxiv"] and w["arxiv"] == p["arxiv"]) or (w["doi"] and w["doi"] == p["doi"]) or same_title(w["title"], p["title"]):
                match = p
                break
        if match:
            if w["doi"]:
                match["doi"] = w["doi"]
                match["journal"] = w["journal"] or match["journal"]
                if w["year"]:
                    match["year"], match["month"] = w["year"], w["month"]
        elif w["doi"]:   # published work that is not on arXiv under this name
            papers.append({"arxiv": w["arxiv"], "title": w["title"], "abstract": "", "names": [], "year": w["year"],
                           "month": w["month"], "doi": w["doi"], "journal": w["journal"]})

    # Hand-written overrides: mark a paper as published, add one, or exclude a namesake's.
    for e in extra:
        doi = str(e.get("doi") or "").lower() or None
        arx = str(e.get("arxiv") or "") or None
        by_arxiv = next((p for p in papers if arx and p["arxiv"] == arx), None)
        by_doi = next((p for p in papers if doi and p["doi"] == doi), None)
        if by_arxiv and by_doi and by_arxiv is not by_doi:   # preprint and journal version listed separately: join them
            for k in ("journal", "year", "month"):
                by_arxiv[k] = by_doi[k] or by_arxiv[k]
            by_arxiv["title"] = by_doi["title"] or by_arxiv["title"]
            papers = [p for p in papers if p is not by_doi]
        match = by_arxiv or by_doi
        if e.get("exclude"):
            papers = [p for p in papers if p is not match]
            continue
        if not match:
            match = {"arxiv": arx, "title": e.get("title", ""), "abstract": e.get("abstract", ""), "names": [],
                     "year": 0, "month": 0, "doi": None, "journal": "",
                     "authors_override": e.get("authors", ""), "position_override": int(e.get("position", 0) or 0),
                     "n_override": int(e.get("n_authors", 0) or 0)}
            papers.append(match)
        if doi:
            match["doi"] = doi
        for k in ("journal", "year", "month", "url"):
            if e.get(k):
                match[k] = e[k]

    out = []
    for p in papers:
        if p["doi"] and (not p["names"] or not p["journal"]):
            c = crossref(p["doi"])
            if c:
                p["names"] = p["names"] or c["names"]
                p["journal"] = p["journal"] or c["journal"]
                p["abstract"] = p["abstract"] or c["abstract"]
                if not p["year"]:
                    p["year"], p["month"] = c["year"], c["month"]
        if p["names"]:
            authors, position, n = authors_summary(p["names"])
        else:
            authors, position, n = p.get("authors_override", ""), p.get("position_override", 0), p.get("n_override", 0)
        if not position and not p.get("position_override"):
            continue   # could not confirm authorship
        journal = short_journal(p["journal"]) or ("" if p["doi"] else "arXiv")
        out.append({
            "title": p["title"], "authors": authors, "position": position, "n_authors": n,
            "first_author": position == 1, "journal": journal, "year": p["year"], "month": p["month"],
            "doi": p["doi"], "arxiv": p["arxiv"],
            "url": p.get("url") or (("https://doi.org/" + p["doi"]) if p["doi"] else ("https://arxiv.org/abs/" + p["arxiv"])),
            "abstract": p["abstract"],
        })

    out.sort(key=lambda p: (p["year"], p["month"], p["title"]), reverse=True)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    first = sum(p["first_author"] for p in out)
    print("Wrote %d publications (%d first-author, %d with abstracts) to %s"
          % (len(out), first, sum(bool(p["abstract"]) for p in out), OUT.relative_to(ROOT)))


if __name__ == "__main__":
    main()
