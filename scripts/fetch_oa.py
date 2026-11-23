"""Download open-access PDFs listed in data/oa_downloads.csv into inbox/<folder>/.
Columns: folder,url,doi,title. Skips existing files, keeps only real PDFs (checks %PDF header).
Writes data/oa_download_report.csv with ok/failed per row."""
import csv, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(ROOT / "data/oa_downloads.csv", encoding="utf-8")))
report = []
for r in rows:
    d = ROOT / "inbox" / r["folder"]
    d.mkdir(parents=True, exist_ok=True)
    out = d / (r["folder"] + ".pdf")
    if out.exists() and out.read_bytes()[:4] == b"%PDF":
        report.append({**r, "status": "ok"}); continue
    ok = False
    for url in r["url"].split("|"):
        subprocess.run(["curl", "-sSL", "--max-time", "120", "-A",
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
                        "-o", str(out), url.strip()], capture_output=True)
        if out.exists() and out.read_bytes()[:4] == b"%PDF" and out.stat().st_size > 20000:
            ok = True; break
    if not ok:
        out.unlink(missing_ok=True)
        try: d.rmdir()
        except OSError: pass
    report.append({**r, "status": "ok" if ok else "failed"})
    print(("OK   " if ok else "FAIL ") + r["folder"], flush=True)
with open(ROOT / "data/oa_download_report.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) + ["status"]); w.writeheader(); w.writerows(report)
