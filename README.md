# Black Flies of the Oriental Region

Identification keys and species pages for Simuliidae (Diptera), built with the **key-builder** toolkit
(`~/.claude/skills/key-builder`).

- Settings: `project.json` (genera, regions, focus country, search terms, home page text)
- Keys: `data/transcriptions/*.txt` -> `data/keys.csv`; species: `data/taxa.csv`; conflicts: `data/conflicts.csv`
- New PDFs: put them in `inbox/` and ask Claude Code `/key-builder add` (or `/key-builder update` to also search)
- Rebuild: `python scripts/update_site.py` (or double-click `update.bat`); output in `site/`
- Publish: push to GitHub; `.github/workflows/pages.yml` rebuilds and deploys to GitHub Pages
  (once: Settings -> Pages -> Source: GitHub Actions). PDFs are git-ignored.
