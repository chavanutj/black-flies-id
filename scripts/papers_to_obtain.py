"""Write data/papers_to_obtain.csv and PAPERS_TO_OBTAIN.md: every logged paper whose PDF is not yet in inbox/ or sources/.
Re-run after you drop PDFs in inbox/<any-folder>/ (the folder or file name should contain the DOI tail or first-author+year)."""
import csv, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
have = " ".join(p.stem.lower() for d in ("inbox", "sources") for p in (ROOT / d).rglob("*.pdf"))
rep = {r["doi"]: r for r in csv.DictReader(open(ROOT / "data/oa_download_report.csv", encoding="utf-8")) if r["status"] == "ok"}
rows = []
for r in csv.DictReader(open(ROOT / "data/literature_log.csv", encoding="utf-8")):
    doi = r["doi"].strip()
    if doi and doi in rep:
        continue
    m = re.match(r"\s*([A-Za-z'\-]+)", r["citation"])
    tag = (m.group(1).lower() + r["year"]) if m else ""
    tail = doi.split("/")[-1].lower() if doi else "@@"
    if tail in have:
        continue
    pr = re.search(r"PRIORITY ([A-C/]+)", r["notes"])
    oa = "open access (download failed or not tried)" if re.search(r"\bOA\b|free|open", r["notes"], re.I) and not re.search(r"Not OA", r["notes"]) else "subscription / library"
    url = re.search(r"https?://\S+", r["notes"])
    rows.append({"priority": pr.group(1) if pr else "", "year": r["year"], "doi": doi,
                 "title_citation": r["citation"], "content": r["content"], "access": oa,
                 "link": ("https://doi.org/" + doi) if doi else (url.group(0).rstrip(";,") if url else ""),
                 "suggested_folder": f"inbox/{tag}_{tail if doi else 'nodoi'}/", "why": r["notes"]})
rows.sort(key=lambda x: (x["priority"] or "Z", x["year"]))
with open(ROOT / "data/papers_to_obtain.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
md = ["# Papers to obtain", "", f"{len(rows)} papers are logged but not yet downloaded. Save each PDF into `inbox/` "
      "(any sub-folder; the suggested folder name is fine), then run `update.bat` or ask the agent to process the inbox.",
      "Regenerate this list with `python scripts/papers_to_obtain.py`.", "",
      "| Priority | Year | DOI / link | Title / citation | Access |", "|---|---|---|---|---|"]
for r in rows:
    md.append(f"| {r['priority']} | {r['year']} | {r['link']} | {r['title_citation'].replace('|', '/')} | {r['access']} |")
(ROOT / "PAPERS_TO_OBTAIN.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print(len(rows), "papers to obtain")
