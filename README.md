# Black Flies of the World

Identification keys and species pages for black flies (Diptera: Simuliidae), with a focus on Thailand,
built with the **key-builder** toolkit (`~/.claude/skills/key-builder`).

**Live site:** https://chavanutj.github.io/black-flies-id/

The site has 59 dichotomous keys (about 1,290 couplets) and 395 taxa. Every key is transcribed word for word
from the published sources. It also has a glossary with clickable labelled diagrams, a biology page, a figure
viewer, a list of conflicts between sources, and a Thailand checklist. The site can be installed as an app
and works offline.

## Where things are

| What | File |
|---|---|
| Settings (title, genera, regions, focus country, search terms, home page text) | `project.json` |
| Keys | `data/transcriptions/*.txt` -> `data/keys.csv`, `data/keys_index.csv` |
| Species and higher taxa | `data/taxa.csv` |
| Sources, figures and conflicts | `data/sources.csv`, `data/figures.csv`, `data/conflicts.csv` |
| Glossary and diagrams | `data/glossary.csv`, `data/abbreviations.csv`, `data/diagrams.csv`, `data/hotspots.csv` |
| Literature found so far | `data/literature_log.csv` |
| **Papers still to download** | [`PAPERS_TO_OBTAIN.md`](PAPERS_TO_OBTAIN.md) (also `data/papers_to_obtain.csv`), with DOI, priority and access |

## Workflow

1. **Add papers:** save PDFs into `inbox/`, then ask Claude Code `/key-builder add`
   (or `/key-builder update` to also search for new literature).
2. **Rebuild:** `python scripts/update_site.py` (or double-click `update.bat`). The output goes to `site/`.
3. **Refresh the download list:** `python scripts/papers_to_obtain.py`.
4. **Publish:** push to GitHub. `.github/workflows/pages.yml` rebuilds the site and deploys it to GitHub Pages.

Source PDFs are copyrighted and git-ignored. They stay on your computer and are never pushed.
