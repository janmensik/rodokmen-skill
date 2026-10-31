# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen** v aplikaci Antigravity / Gemini. Na začátku každé konverzace:
1. Načti skill `rodokmen` (`SKILL.md`, pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.

## Technická pravidla prostředí (Windows / Antigravity)
- Python skripty spouštěj vždy přes `python -I -X utf8 tools/<nástroj>.py` (ne `python3`).
- ImageMagick je `magick` (nikdy `convert`).
- Skripty `.sh` spouštěj přes Git Bash (`bash tools/…`).
- Datové soubory zapisuj v UTF-8 bez BOM (přes `write_file` / `edit_file`).
